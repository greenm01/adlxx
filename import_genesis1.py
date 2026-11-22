"""Extract the 31 publisher verse addresses from a saved Genesis 1 HTML page."""

import argparse
import csv
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from datetime import date

URL = "https://apostoliki-diakonia.gr/bible/genesis/"


class PublisherPage(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cell = None
        self.candidates = []

    def handle_starttag(self, tag, attrs):
        if tag == "td":
            self.cell = []
        elif self.cell is not None and tag in {"br", "p"}:
            self.cell.append(" ")

    def handle_data(self, text):
        if self.cell is not None:
            self.cell.append(text)

    def handle_endtag(self, tag):
        if tag == "td" and self.cell is not None:
            text = " ".join("".join(self.cell).split())
            if text.startswith("1 ΕΝ ἀρχῇ "):
                self.candidates.append(text)
            self.cell = None


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("html", type=Path)
    cli.add_argument("--retrieved", type=date.fromisoformat, required=True)
    args = cli.parse_args()
    page = PublisherPage()
    page.feed(args.html.read_text(encoding="utf-8"))
    if len(page.candidates) != 1:
        raise ValueError("Expected exactly one Genesis 1 text cell")
    parts = re.split(r"(?<!\S)(\d+)(?!\S)", page.candidates[0])
    if list(map(int, parts[1::2])) != list(range(1, 32)) or not all(
        v.strip() for v in parts[2::2]
    ):
        raise ValueError("Expected all 31 numbered verses in order")
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("ref", "url", "retrieved", "greek"))
    for i, verse in enumerate(parts[2::2], 1):
        writer.writerow((f"GEN 1:{i}", URL, args.retrieved, verse.strip()))


if __name__ == "__main__":
    main()
