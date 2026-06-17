#!/usr/bin/env python3

import argparse
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import markdownify
import requests
from bs4 import BeautifulSoup, Comment


DEFAULT_SELECTORS = [
    "article",
    "main",
    '[role="main"]',
    ".entry-content",
    ".post-content",
    ".page-content",
    ".main-content",
    ".content",
]

REMOVE_SELECTORS = [
    "header",
    "nav",
    ".nav",
    ".navigation",
    ".site-header",
    ".menu",
    "footer",
    ".site-footer",
    ".cookie-banner",
    ".cookie-notice",
    "aside",
    ".sidebar",
    ".comments",
    ".widget",
    "script",
    "style",
]


def fetch(url, timeout=20):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.RequestException as exc:
        print(f"Error fetching {url}: {exc}", file=sys.stderr)
        return None


def extract_main_content(soup):
    for selector in DEFAULT_SELECTORS:
        element = soup.select_one(selector)
        if element:
            return element

    body = soup.find("body")
    if not body:
        return soup

    for selector in REMOVE_SELECTORS:
        for tag in body.select(selector):
            tag.decompose()

    for comment in body.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    return body


def clean_title(title):
    title = re.sub(r"\s*[\-|\u2013|\u2014]\s*Research Software London\s*$", "", title)
    return title.strip()


def extract_title(soup, url):
    if soup.title and soup.title.string:
        return clean_title(soup.title.string)

    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)

    return Path(urlparse(url).path).name.replace("-", " ").title() or "Untitled"


def extract_first_h1(soup):
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    return None


def remove_cookie_footer(markdown):
    lines = markdown.splitlines()
    filtered = []

    for line in lines:
        if "Hestia | Developed by" in line:
            continue
        if "This site uses cookies" in line:
            continue
        if line.strip() == "Accept":
            continue
        filtered.append(line)

    while filtered and filtered[-1].strip() == "":
        filtered.pop()

    while filtered and filtered[0].strip() == "":
        filtered.pop(0)

    return "\n".join(filtered)


def html_to_markdown(html):
    return markdownify.markdownify(html, heading_style="atx", bullets="-", strip=["script", "style"])


def url_to_paths(url, output_dir):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "index"

    output_path = Path(output_dir) / f"{path}.md"
    permalink = f"/{path}/"
    return output_path, permalink


def process_url(url, output_dir, delay=0.5):
    print(f"Fetching: {url}", file=sys.stderr)

    html = fetch(url)
    if html is None:
        return False

    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup, url)

    content = extract_main_content(soup)
    markdown = html_to_markdown(str(content))
    markdown = remove_cookie_footer(markdown)

    first_h1 = extract_first_h1(soup)
    if first_h1 and markdown.lstrip().startswith(f"# {first_h1}"):
        pass

    output_path, permalink = url_to_paths(url, output_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    front_matter = f'---\nlayout: single\ntitle: "{title}"\npermalink: {permalink}\n---\n\n'

    output_path.write_text(front_matter + markdown)
    print(f"Wrote: {output_path}", file=sys.stderr)

    time.sleep(delay)
    return True


def main():
    parser = argparse.ArgumentParser(description="Fetch WordPress pages and convert to Jekyll Markdown.")
    parser.add_argument("urls", nargs="*", help="URLs to fetch")
    parser.add_argument("--url-file", type=str, help="File containing one URL per line")
    parser.add_argument("--output-dir", type=str, default="docs", help="Directory to write Markdown files")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between requests in seconds")
    args = parser.parse_args()

    urls = list(args.urls)
    if args.url_file:
        urls.extend(Path(args.url_file).read_text().splitlines())

    urls = [url.strip() for url in urls if url.strip()]

    if not urls:
        print("No URLs provided.", file=sys.stderr)
        sys.exit(1)

    success = 0
    for url in urls:
        if process_url(url, args.output_dir, delay=args.delay):
            success += 1

    print(f"\nConverted {success}/{len(urls)} pages to {args.output_dir}/", file=sys.stderr)


if __name__ == "__main__":
    main()
