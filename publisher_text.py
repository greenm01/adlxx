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
    body = re.sub(
        r"(?<=[^\W\d_])(?=[0-9])|(?<=[0-9])(?![αβγδεζηθικλμνξοπρστυφχψω]\s)(?=[^\W\d_])",
        " ",
        body,
    )
    # Some numbers are inside an opening parenthesis, or touch the previous
    # sentence's punctuation. Keep the punctuation with the Greek it belongs to.
    body = re.sub(r"\((\d+)\s+", r" \1 (", body)
    body = re.sub(r"(?<=[.,··;])(?=\d)", " ", body)
    identity = (path.parent.name, label)
    if identity == ("LEV", "2"):
        anchor = "ἐὰν δὲ προσφέρῃ δῶρον θυσίαν πεπεμμένην"
        if body.count(anchor) != 1:
            raise ValueError("Leviticus 2:4 anchor changed")
        body = body.replace(anchor, "4 " + anchor)
    if identity == ("NUM", "15"):
        anchor = "9 καὶ ἔσται ὅταν ἔσθητε"
        if body.count(anchor) != 1:
            raise ValueError("Numbers 15:19 anchor changed")
        body = body.replace(anchor, "19 καὶ ἔσται ὅταν ἔσθητε")
    parts = re.split(r"(?<!\S)(\d+(?:[-–]\d+|[αβγδεζηθικλμνξοπρστυφχψω])?)(?!\S)", body)
    labels = ["1", *parts[1::2]]
    verses = [s.strip() for s in parts[::2]]
    if not verses[0]:
        labels, verses = labels[1:], verses[1:]
    if not verses or any(not s or re.search(r"\d", s) for s in verses):
        raise ValueError("Embedded number or empty verse")
    if identity == ("DEU", "3") and labels == [
        *map(str, range(1, 15)),
        "14",
        *map(str, range(15, 30)),
    ]:
        labels[14] = "14#2"
    numbers = []
    for label in labels:
        if re.fullmatch(r"\d+", label):
            numbers.append(int(label))
        elif re.fullmatch(r"\d+[-–]\d+", label):
            first, last = map(int, re.split(r"[-–]", label))
            if last <= first:
                raise ValueError(f"Invalid range {label}")
            numbers.extend(range(first, last + 1))
    # Addresses may be reordered when a publisher places readings after the
    # chapter. Preserve that order and keep its range and subverse labels.
    expected = set(range(1, max(numbers, default=0) + 1))
    if identity == ("1SA", "13"):
        expected.discard(1)
    if len(set(labels)) != len(labels) or sorted(numbers) != sorted(expected):
        raise ValueError(f"Nonconsecutive or repeated labels {labels}")
    return list(zip(labels, verses, strict=True))
