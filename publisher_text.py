"""Inspect and extract numbered verses from cached publisher chapters."""

import csv
import gzip
from html.parser import HTMLParser
import re
from publisher_catalog import CACHE, ROOT


class Content(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, text):
        self.parts.append(text)

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "p", "td", "tr", "div", "sup"):
            self.parts.append(" ")

    def handle_endtag(self, tag):
        if tag in ("p", "td", "tr", "div", "sup"):
            self.parts.append(" ")


def chapter_text(path):
    page = gzip.decompress(path.read_bytes()).decode("utf-8-sig")
    content = re.search(
        r'<table\b[^>]*width=["\']450["\'][^>]*>(.*?)</table\s*>', page, re.I | re.S
    )
    if not content:
        raise ValueError("Could not identify the publisher text table")
    parser = Content()
    parser.feed(content[1])
    return " ".join("".join(parser.parts).split())


def main():
    for path in sorted(CACHE.glob("*/index.gz")):
        try:
            s = chapter_text(path)
            print(path.parent.name, s[:85], re.findall(r"(?<!\S)\d+(?!\S)", s)[-3:])
        except ValueError as e:
            print(path.parent.name, e)


if __name__ == "__main__":
    main()


def numbered_verses(path, label):
    """Read ordinary chapter layouts strictly; keep exceptions in the import queue."""
    text = chapter_text(path)
    head, space, body = text.partition(" ")
    if head != label or not space:
        raise ValueError(f"Unexpected chapter heading {head[:35]!r}")
    # The raw HTML retains these printed cross-references. Do not pass their
    # chapter numerals to the address parser or their words to the interlinear.
    body = re.sub(r"\(Κεφ\.\s+[^()]{1,32}\d\)", "", body)
    # Verse markers can directly touch a Greek word on either side in the HTML.
    body = re.sub(r"(?<=[^\W\d_])(?=[0-9])|(?<=[0-9])(?=[^\W\d_])", " ", body)
    parts = re.split(r"(?<!\S)(\d+)(?!\S)", body)
    numbers = list(map(int, parts[1::2]))
    if numbers != list(range(2, 2 + len(numbers))):
        raise ValueError(f"Nonconsecutive verse labels {numbers}")
    verses = [s.strip() for s in parts[::2]]
    if any(not s or re.search(r"\d", s) for s in verses):
        raise ValueError("Embedded number or empty verse")
    return [(str(i), s) for i, s in enumerate(verses, 1)]
