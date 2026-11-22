"""Measure contextual reuse against a specified Athens interlinear chapter."""

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
import subprocess
import sys
import unicodedata

from interlinear import TOKEN


def normalized(word):
    return unicodedata.normalize("NFC", word.lower().replace("ς", "σ")).translate(
        str.maketrans({"᾿": "’", "᾽": "’", "'": "’"})
    )


def windows(words):
    words = [None, *words, None]
    return [tuple(words[i : i + 3]) for i in range(len(words) - 2)]


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("athens_repo", type=Path)
    cli.add_argument("--revision", default="3ffd871904268583043ebf1886e700486504cc84")
    cli.add_argument(
        "--chapter",
        default="GEN 1",
        help="Book code and chapter, for example GEN 1",
    )
    args = cli.parse_args()
    book, chapter = args.chapter.split()
    revision = subprocess.check_output(
        [
            "git",
            "-C",
            str(args.athens_repo),
            "rev-parse",
            "--verify",
            args.revision + "^{commit}",
        ],
        text=True,
    ).strip()
    data = subprocess.check_output(
        [
            "git",
            "-C",
            str(args.athens_repo),
            "show",
            f"{revision}:interlinear/{book}-{int(chapter):03}.tsv",
        ],
        text=True,
    )
    source = defaultdict(list)
    forms = set()
    for row in csv.DictReader(data.splitlines(), delimiter="\t"):
        if row["preference"] == "1" and row["occurrence"] == "1":
            source[row["ref"]].append(row)
            forms.add(normalized(row["surface"]))
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(
        (
            "ref",
            "position",
            "surface",
            "basis",
            "athens_revision",
            "athens_position",
            "lemma",
            "grammar",
            "english",
        )
    )
    with (Path(__file__).resolve().parent / "data/verses.tsv").open() as f:
        selected = [
            r
            for r in csv.DictReader(f, delimiter="\t")
            if r["ref"].split(":")[0] == args.chapter
        ]
    if not selected:
        raise ValueError(f"No AD verses for {args.chapter}")
    for row in selected:
        ref = row["ref"]
        words = TOKEN.findall(row["greek"])
        ad = list(map(normalized, words))
        ath = source[ref]
        aw = [normalized(r["surface"]) for r in ath]
        ad_windows = windows(ad)
        ath_windows = windows(aw)
        counts = Counter(ad_windows)
        matches = defaultdict(list)
        for j, window in enumerate(ath_windows):
            matches[window].append(j)
        for i, (surface, window) in enumerate(zip(words, ad_windows)):
            candidate = None
            if ad == aw:
                basis = "same verse"
                candidate = ath[i]
            elif counts[window] == 1 and len(matches[window]) == 1:
                basis = "unique context"
                candidate = ath[matches[window][0]]
            else:
                basis = "form only" if ad[i] in forms else "no form"
            details = (
                [candidate[k] for k in ("position", "lemma", "grammar", "english")]
                if candidate
                else [""] * 4
            )
            writer.writerow((ref, i + 1, surface, basis, revision, *details))


if __name__ == "__main__":
    main()
