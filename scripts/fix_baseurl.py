#!/usr/bin/env python3
"""Prepend /rslondon to domain-relative internal links/paths in docs/."""

import re
from pathlib import Path

BASEURL = "/rslondon"

# Match domain-relative paths in Markdown links, HTML attributes, and YAML url values.
# Exclude paths already starting with /rslondon/ and protocol-relative URLs (//...).
PATH_RE = re.compile(
    r'(?P<prefix>(?:href|src)="|\]\(|^\s*url:\s*)\s*'
    r'(?P<path>/(?!rslondon/)(?!/)[^\s"\')]*)',
    re.MULTILINE,
)


def fix_file(path):
    text = path.read_text()
    new_text, count = PATH_RE.subn(lambda m: f'{m.group("prefix")}{BASEURL}{m.group("path")}', text)
    if count:
        path.write_text(new_text)
        print(f"  {path}: {count} replacements")
    return count


def main():
    docs = Path("docs")
    total = 0
    for pattern in ("*.md", "*.markdown", "*.yml", "*.html"):
        for path in docs.rglob(pattern):
            if "_site" in path.parts:
                continue
            total += fix_file(path)
    print(f"\nTotal replacements: {total}")


if __name__ == "__main__":
    main()
