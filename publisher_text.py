"""Inspect and extract numbered verses from cached publisher chapters."""

import csv
import gzip
from html.parser import HTMLParser
import re
from publisher_catalog import CACHE, ROOT


with (ROOT / "data/publisher-numbering.tsv").open() as numbering_file:
    NUMBER_GAPS = {
        (row["book"], row["chapter"]): set(map(int, row["unprinted_labels"].split()))
        for row in csv.DictReader(numbering_file, delimiter="\t")
    }


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
    return parse_numbered(text, label, path.parent.name)


def parse_numbered(text, label, book):
    head, space, body = text.partition(" ")
    if head != label or not space:
        raise ValueError(f"Unexpected chapter heading {head[:35]!r}")
    # The raw HTML retains these printed cross-references. Do not pass their
    # chapter numerals to the address parser or their words to the interlinear.
    body = re.sub(r"\(Κεφ\.\s+[^()]{1,32}\d\s*\)", "", body)
    if book == "PRO" and label in {"15", "16"}:
        body = re.sub(r"\(Μασ\. [^()]{0,18}\d\)\.?", "", body)
    body = re.sub(r"\[(\d+)\s+", r" \1 [", body)
    if (book, label) == ("1KI", "3") and body.startswith("* 2 "):
        body = "2 *" + body[4:]
    # Verse markers can directly touch a Greek word on either side in the HTML.
    body = re.sub(
        r"(?<=[^\W\d_])(?=[0-9])|(?<=[0-9])(?![αβγδεζηθικλμνξοπρστυφχψω]\s)(?=[^\W\d_])",
        " ",
        body,
    )
    # Some numbers are inside an opening parenthesis, or touch the previous
    # sentence's punctuation. Keep the punctuation with the Greek it belongs to.
    body = re.sub(r"\((\d+)\s+", r" \1 (", body)
    body = re.sub(r"(?<=[.,··;—])(?=\d)", " ", body)
    body = re.sub(r"(?<=[0-9])(?=[᾿῾])", " ", body)
    identity = (book, label)
    # These anchors were checked in the publisher page against the surrounding
    # Greek. Only the local address marker changes.
    anchors = {
        ("JOB", "34"): [
            ("7 ὅτι ἐξέκλιναν ἐκ νόμου Θεοῦ", "27 ὅτι ἐξέκλιναν ἐκ νόμου Θεοῦ")
        ],
        ("PSA", "9"): [("(Μασ. 10 1-18).", "")],
        ("PSA", "53"): [("ἰδοὺ γὰρ ὁ Θεὸς βοηθεῖ μοι", "6 ἰδοὺ γὰρ ὁ Θεὸς βοηθεῖ μοι")],
        ("1SA", "16"): [("33 καὶ ἐγενήθη ἐν τῷ εἶναι", "23 καὶ ἐγενήθη ἐν τῷ εἶναι")],
        ("1MA", "3"): [
            ("6 καὶ ὠνομάσθη", "9 καὶ ὠνομάσθη"),
            ("52 καὶ τὰ ἅγιά σου", "51 καὶ τὰ ἅγιά σου"),
        ],
        ("JOS", "9"): [("διαθήκην.καὶ εἶπαν οἱ υἱοὶ", "διαθήκην. 7 καὶ εἶπαν οἱ υἱοὶ")],
        ("ESG", "3"): [("῟13γ", "13γ")],
        ("1KI", "14"): [("*21 ΚΑΙ", "21 *ΚΑΙ")],
    }
    for old, new in anchors.get(identity, ()):
        if body.count(old) != 1:
            raise ValueError(f"Publisher address anchor changed at {identity}: {old}")
        body = body.replace(old, new)
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
    if (
        identity == ("ESG", "1")
        and labels[:2] == ["1", "1β"]
        and labels.count("1") == 2
    ):
        labels[0] = "1α"
    duplicate_labels = {
        ("1CH", "1"): "24",
        ("1KI", "12"): "3",
        ("1KI", "5"): "1",
        ("1KI", "6"): "21",
    }
    if identity in duplicate_labels:
        duplicate = duplicate_labels[identity]
        if labels.count(duplicate) == 2:
            last = len(labels) - 1 - labels[::-1].index(duplicate)
            labels[last] += "#2"
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
    expected -= NUMBER_GAPS.get(identity, set())
    if len(set(labels)) != len(labels) or sorted(numbers) != sorted(expected):
        raise ValueError(f"Nonconsecutive or repeated labels {labels}")
    return list(zip(labels, verses, strict=True))


def addressed_verses(path, book, ch):
    """Map a publisher navigation entry to the canonical addresses it contains."""
    text = chapter_text(path)

    def section(prefix, numbered):
        return [(f"{prefix}:{label}", s) for label, s in numbered]

    if (book, ch) in {("LAM", "1"), ("LJE", "1")}:
        body = text.removeprefix("1 ") if book == "LAM" else text
        opening = "Πῶς ἐκάθισε" if book == "LAM" else "Διὰ τὰς ἁμαρτίας"
        anchor = " 1 " + opening
        if body.count(anchor) != 1:
            raise ValueError("Proem boundary changed")
        proem, following = body.split(anchor)
        return [
            (f"{book} 1:proem", proem.strip()),
            *section(
                f"{book} 1", parse_numbered("1 " + opening + following, "1", book)
            ),
        ]
    if (book, ch) == ("PSA", "150"):
        anchor = "Οὗτος ὁ ψαλμὸς ἰδιόγραφος"
        if text.count(anchor) != 1:
            raise ValueError("Psalm 151 heading changed")
        first, rest = text.split(anchor)
        return section("PSA 150", parse_numbered(first.strip(), "150", book)) + section(
            "PSA 151", parse_numbered("151 " + anchor + rest, "151", book)
        )
    if (book, ch) == ("PRO", "24"):
        # Five printed Masoretic cross-references identify where each displaced
        # passage belongs. Keep the page's order while indexing by verse.
        pieces = re.split(r"\(Μασ\. ([^()]+)\)\.", text)
        if pieces[1::2] != ["ΚΘ´, 27", "Λ´, 1", "ΚΔ´, 23", "Λ´, 15", "ΛΑ´, 1"]:
            raise ValueError("Proverbs 24 cross-references changed")
        out = section("PRO 24", parse_numbered(pieces[0].strip(), "24", book))
        additions = re.split(r"(?<!\S)(22[αβγδ])(?!\S)", pieces[2].strip())
        if additions[1::2] != ["22α", "22β", "22γ", "22δ"] or additions[0]:
            raise ValueError("Proverbs 24 additions changed")
        out += section(
            "PRO 24",
            [
                (k, v.strip())
                for k, v in zip(additions[1::2], additions[2::2], strict=True)
            ],
        )
        for part, ch_num, first, last in [
            (pieces[4], 30, 1, 14),
            (pieces[6], 24, 23, 34),
            (pieces[8], 30, 15, 33),
            (pieces[10], 31, 1, 9),
        ]:
            part = part.strip()
            if ch_num == 30 and first == 1:
                if not part.startswith("22ε "):
                    raise ValueError("Proverbs 30 opening changed")
                part = part[4:]
            segments = re.split(r"(?<!\S)(\d+)(?!\S)", part)
            if segments[1::2] != list(map(str, range(first + 1, last + 1))) or not all(
                s.strip() for s in segments[::2]
            ):
                raise ValueError("Unexpected Proverbs verse boundary")
            out += section(
                f"PRO {ch_num}",
                [(str(n), s.strip()) for n, s in enumerate(segments[::2], first)],
            )
        return out
    if (book, ch) == ("PRO", "29"):
        anchor = "(Μασσ. ΛΑ´, 10)."
        if text.count(anchor) != 1:
            raise ValueError("Proverbs 31:10 marginal reference changed")
        first, rest = text.split(anchor)
        extra = re.split(r"(?<!\S)(\d+)(?!\S)", rest.strip())
        if extra[1::2] != list(map(str, range(11, 32))):
            raise ValueError("Unexpected Proverbs 31 labels")
        return section("PRO 29", parse_numbered(first.strip(), "29", book)) + section(
            "PRO 31", [(str(n), s.strip()) for n, s in enumerate(extra[::2], 10)]
        )
    headings = {
        ("DAG", "0"): ("Σωσάννα", "SUS 1"),
        ("DAG", "13"): ("Βήλ και Δράκων", "BEL 1"),
    }
    if (book, ch) in headings:
        title, address = headings[book, ch]
        if not text.startswith(title + " "):
            raise ValueError(f"Missing {title} heading")
        return section(
            address, parse_numbered("1 " + text[len(title) :].strip(), "1", book)
        )
    if (book, ch) == ("SIR", "0"):
        title = "ΠΡΟΛΟΓΟΣ ΣΟΦΙΑΣ ΣΕΙΡΑΧ"
        if not text.startswith(title + " "):
            raise ValueError("Missing Sirach prologue heading")
        return [("SIR 0:prologue", text[len(title) :].strip())]
    return section(f"{book} {ch}", parse_numbered(text, ch, book))
