#!/usr/bin/env python3

import argparse
import json
import sys
import time
import urllib.robotparser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


class LinkInventory:
    def __init__(self, start_url, delay=0.5, timeout=10, user_agent="link-inventory-bot/1.0"):
        self.start_url = start_url
        self.delay = delay
        self.timeout = timeout
        self.user_agent = user_agent
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})

        parsed = urlparse(start_url)
        self.base_netloc = parsed.netloc
        self.scheme = parsed.scheme

        self.visited = {}
        self.to_visit = [start_url]

        self.robots_parser = urllib.robotparser.RobotFileParser()
        self.robots_parser.set_url(urljoin(start_url, "/robots.txt"))
        try:
            self.robots_parser.read()
        except Exception:
            self.robots_parser = None

    def _normalize(self, url):
        url, _ = urldefrag(url)
        parsed = urlparse(url)
        if not parsed.scheme:
            url = urljoin(self.start_url, url)
        return url

    def _is_internal(self, url):
        return urlparse(url).netloc == self.base_netloc

    def _can_fetch(self, url):
        if not self.robots_parser:
            return True
        return self.robots_parser.can_fetch(self.user_agent, url)

    def _fetch(self, url):
        try:
            return self.session.get(url, timeout=self.timeout, allow_redirects=True)
        except requests.RequestException:
            return None

    def _classify(self, url):
        path = urlparse(url).path.lower()
        if any(path.endswith(ext) for ext in [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"]):
            return "document"
        if any(path.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"]):
            return "image"
        if any(path.endswith(ext) for ext in [".css", ".js"]):
            return "asset"
        if urlparse(url).netloc != self.base_netloc:
            return "external"
        return "page"

    def _extract_links(self, response):
        if "text/html" not in response.headers.get("Content-Type", ""):
            return [], ""

        soup = BeautifulSoup(response.text, "html.parser")
        links = []

        for tag in soup.find_all(["a", "link"]):
            href = tag.get("href")
            if href:
                links.append(self._normalize(href))

        for tag in soup.find_all(["img", "script", "source", "video", "audio"]):
            src = tag.get("src")
            if src:
                links.append(self._normalize(src))

        title = ""
        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        return links, title

    def crawl(self):
        while self.to_visit:
            url = self.to_visit.pop(0)
            if url in self.visited:
                continue

            if not self._can_fetch(url):
                self.visited[url] = {
                    "status": "blocked by robots.txt",
                    "title": "",
                    "type": self._classify(url),
                    "links": [],
                }
                continue

            print(f"Crawling: {url}", file=sys.stderr)
            response = self._fetch(url)
            time.sleep(self.delay)

            if response is None:
                self.visited[url] = {
                    "status": "error",
                    "title": "",
                    "type": self._classify(url),
                    "links": [],
                }
                continue

            links, title = self._extract_links(response)

            self.visited[url] = {
                "status": response.status_code,
                "title": title,
                "type": self._classify(url),
                "links": links,
            }

            for link in links:
                normalized = self._normalize(link)
                if (
                    self._is_internal(normalized)
                    and normalized not in self.visited
                    and normalized not in self.to_visit
                    and self._classify(normalized) == "page"
                ):
                    self.to_visit.append(normalized)

        return self.visited

    def to_markdown(self):
        lines = ["| URL | Type | Status | Title |", "|---|---|---|---|"]
        for url, data in sorted(self.visited.items()):
            title = data.get("title", "").replace("|", "\\|")
            lines.append(f"| {url} | {data['type']} | {data['status']} | {title} |")
        return "\n".join(lines)

    def to_json(self):
        return json.dumps(self.visited, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Inventory accessible links on a website.")
    parser.add_argument("url", help="Start URL")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between requests in seconds")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout in seconds")
    parser.add_argument("--json", type=str, help="Output JSON file path")
    parser.add_argument("--md", type=str, help="Output Markdown file path")
    args = parser.parse_args()

    crawler = LinkInventory(args.url, delay=args.delay, timeout=args.timeout)
    crawler.crawl()

    if args.json:
        Path(args.json).write_text(crawler.to_json())
    if args.md:
        Path(args.md).write_text(crawler.to_markdown())

    print(crawler.to_markdown())


if __name__ == "__main__":
    main()
