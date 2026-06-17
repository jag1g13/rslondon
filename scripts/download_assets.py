#!/usr/bin/env python3

import argparse
import mimetypes
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"}
DOCUMENT_EXTENSIONS = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"}

MARKDOWN_URL_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)|\[([^\]]*)\]\(([^)]+)\)")
PERMALINK_RE = re.compile(r"^permalink:\s*(.+)$", re.MULTILINE)


def is_asset_url(url):
    parsed = urlparse(url)
    path = unquote(parsed.path).lower()

    if path.startswith("/assets/"):
        return False

    if "/wp-content/uploads/" in path or "/rslondon/wp-content/uploads/" in path:
        return True

    ext = Path(path).suffix.lower()
    if ext in IMAGE_EXTENSIONS or ext in DOCUMENT_EXTENSIONS:
        return True

    guess, _ = mimetypes.guess_type(url)
    if guess and (guess.startswith("image/") or guess == "application/pdf"):
        return True

    return False


def is_internal(url, base_domains):
    parsed = urlparse(url)
    if parsed.scheme:
        return parsed.netloc in base_domains
    return parsed.path.startswith("/")


def classify_asset(url):
    parsed = urlparse(url)
    path = unquote(parsed.path)
    ext = Path(path).suffix.lower()

    if ext in IMAGE_EXTENSIONS:
        return "images"
    if ext in DOCUMENT_EXTENSIONS:
        return "documents"

    guess, _ = mimetypes.guess_type(url)
    if guess and guess.startswith("image/"):
        return "images"
    if guess == "application/pdf":
        return "documents"

    return None


def url_to_relative_path(url, asset_type):
    parsed = urlparse(url)
    path = unquote(parsed.path)
    path = path.lstrip("/")

    for prefix in ["wp-content/uploads/sites/132/", "rslondon/wp-content/uploads/sites/132/"]:
        if path.startswith(prefix):
            path = path[len(prefix):]
            break

    path = Path(path)
    if path.is_absolute():
        path = path.relative_to("/")

    return Path("assets") / asset_type / path


def rewrite_markdown(text, mapping):
    def repl(match):
        alt, img_url, link_text, link_url = match.groups()
        if img_url and img_url in mapping:
            return f"![{alt}]({mapping[img_url]})"
        if link_url and link_url in mapping:
            return f"[{link_text}]({mapping[link_url]})"
        return match.group(0)

    return MARKDOWN_URL_RE.sub(repl, text)


def collect_urls_from_markdown(source_dir):
    urls = set()
    for path in Path(source_dir).rglob("*.md"):
        if str(path).startswith("_site") or str(path).startswith("scripts"):
            continue
        text = path.read_text()
        for match in MARKDOWN_URL_RE.finditer(text):
            _, img_url, _, link_url = match.groups()
            if img_url:
                urls.add(img_url)
            if link_url:
                urls.add(link_url)
    return urls


def collect_page_urls(source_dir, base_url):
    pages = []
    for path in Path(source_dir).rglob("*.md"):
        if str(path).startswith("_site") or str(path).startswith("scripts") or str(path).startswith("_"):
            continue
        text = path.read_text()
        if not text.startswith("---"):
            continue
        match = PERMALINK_RE.search(text)
        if not match:
            continue
        permalink = match.group(1).strip().strip('"').strip("'")
        if not permalink:
            continue
        full_url = base_url.rstrip("/") + permalink
        pages.append((path, full_url))
    return pages


def fetch_html(url, timeout=20):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.RequestException as exc:
        print(f"  FAIL fetching HTML: {url} ({exc})", file=sys.stderr)
        return None


def extract_assets_from_html(html, page_url):
    soup = BeautifulSoup(html, "html.parser")
    urls = set()

    for tag in soup.find_all(["img", "source", "video", "audio"]):
        src = tag.get("src")
        if src:
            urls.add(urljoin(page_url, src))

    for tag in soup.find_all("a"):
        href = tag.get("href")
        if not href:
            continue
        ext = Path(href).suffix.lower()
        if ext in IMAGE_EXTENSIONS or ext in DOCUMENT_EXTENSIONS:
            urls.add(urljoin(page_url, href))

    return urls


def download_asset(url, output_path, timeout=30):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(response.content)
        return True, None
    except Exception as exc:
        return False, str(exc)


def find_references(source_dir):
    refs = {}
    for path in Path(source_dir).rglob("*.md"):
        if str(path).startswith("_site") or str(path).startswith("scripts"):
            continue
        text = path.read_text()
        for match in MARKDOWN_URL_RE.finditer(text):
            _, img_url, _, link_url = match.groups()
            url = img_url or link_url
            if url:
                refs.setdefault(url, set()).add(str(path))
    return refs


def main():
    parser = argparse.ArgumentParser(description="Download remote assets from Markdown and original HTML.")
    parser.add_argument("--source-dir", type=str, default="docs", help="Directory containing Markdown files")
    parser.add_argument("--base-url", type=str, default="https://rslondon.ac.uk", help="Base URL of the old site")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be downloaded without downloading")
    parser.add_argument("--workers", type=int, default=5, help="Concurrent download workers")
    parser.add_argument("--skip-html", action="store_true", help="Skip scanning original HTML for assets")
    args = parser.parse_args()

    base_domains = {urlparse(args.base_url).netloc}

    markdown_urls = collect_urls_from_markdown(args.source_dir)
    print(f"Found {len(markdown_urls)} URLs in Markdown", file=sys.stderr)

    html_urls = set()
    if not args.skip_html:
        pages = collect_page_urls(args.source_dir, args.base_url)
        print(f"Scanning {len(pages)} original HTML pages for assets...", file=sys.stderr)
        for path, page_url in pages:
            html = fetch_html(page_url)
            if html is None:
                continue
            assets = extract_assets_from_html(html, page_url)
            internal = {url for url in assets if is_internal(url, base_domains) and is_asset_url(url)}
            html_urls.update(internal)
        print(f"Found {len(html_urls)} asset URLs from HTML", file=sys.stderr)

    all_urls = markdown_urls | html_urls
    internal_urls = {url for url in all_urls if is_internal(url, base_domains)}
    asset_urls = {url for url in internal_urls if is_asset_url(url)}

    print(f"Total unique internal asset URLs: {len(asset_urls)}", file=sys.stderr)

    source_path = Path(args.source_dir)

    plan = []
    for url in sorted(asset_urls):
        asset_type = classify_asset(url)
        if not asset_type:
            print(f"  SKIP (unrecognized type): {url}", file=sys.stderr)
            continue
        full_url = url if urlparse(url).scheme else args.base_url.rstrip("/") + url
        rel_path = url_to_relative_path(full_url, asset_type)
        output_path = source_path / rel_path
        plan.append((full_url, output_path, rel_path, url))

    if args.dry_run:
        print("\nDry run — would download:", file=sys.stderr)
        for full_url, output_path, rel_path, original_url in plan:
            print(f"  {full_url} -> {output_path}", file=sys.stderr)
        return

    mapping = {}
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_url = {executor.submit(download_asset, full_url, output_path): (full_url, output_path, rel_path, original_url) for full_url, output_path, rel_path, original_url in plan}
        for future in as_completed(future_to_url):
            full_url, output_path, rel_path, original_url = future_to_url[future]
            success, error = future.result()
            if success:
                mapping[original_url] = "/" + str(rel_path)
                print(f"  OK: {full_url} -> {output_path}", file=sys.stderr)
            else:
                print(f"  FAIL: {full_url} ({error})", file=sys.stderr)

    updated = 0
    for path in Path(args.source_dir).rglob("*.md"):
        if str(path).startswith("_site") or str(path).startswith("scripts"):
            continue
        text = path.read_text()
        new_text = rewrite_markdown(text, mapping)
        if new_text != text:
            path.write_text(new_text)
            updated += 1

    print(f"\nDownloaded {len(mapping)}/{len(plan)} assets", file=sys.stderr)
    print(f"Updated {updated} Markdown files", file=sys.stderr)

    refs = find_references(args.source_dir)
    downloaded_local_paths = {v for v in mapping.values()}

    unreferenced = []
    for original_url, local_path in mapping.items():
        referenced_by_markdown = any(original_url in refs or local_path in refs for _ in [0])
        if original_url not in refs and local_path not in refs:
            unreferenced.append((original_url, local_path))

    if unreferenced:
        print("\nDownloaded but not referenced in any Markdown file (may need manual re-insertion):", file=sys.stderr)
        for original_url, local_path in sorted(unreferenced):
            print(f"  {local_path}", file=sys.stderr)
            print(f"    source: {original_url}", file=sys.stderr)

    remote_refs = {url for url in refs if urlparse(url).scheme and urlparse(url).netloc in base_domains}
    missing = remote_refs - mapping.keys()
    if missing:
        print("\nStill-referenced remote URLs that were not downloaded:", file=sys.stderr)
        for url in sorted(missing):
            print(f"  {url}", file=sys.stderr)


if __name__ == "__main__":
    main()
