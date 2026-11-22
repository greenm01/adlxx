"""Predict attested Athens analyses from form and neighbouring Greek words."""
import argparse
from collections import Counter
import hashlib
from pathlib import Path
import sqlite3

from corpus_alignment import key
from corpus_build import Athens, DB, REV


def features(words, i):
    form = words[i]
    left = words[i-1] if i else "^"
    right = words[i+1] if i+1 < len(words) else "$"
    yield form, "left", left
    yield form, "right", right
    yield form, "endings", left[-2:], right[-2:]
    yield form, "form"


def train(verses):
    counts = {}
    examples = {}
    for ref, entries in verses:
        words = [key(e[0]) for e in entries]
        for i, e in enumerate(entries):
            reading = e[1:4]
            if not all(reading):
                continue
            examples.setdefault((words[i], reading), e)
            for f in features(words, i):
                counts.setdefault(f, Counter())[reading] += 1
    rules = {}
    for f, votes in counts.items():
        choice, support = votes.most_common(1)[0]
        total = votes.total()
        # Smooth by one hypothetical failure to avoid crediting rare matches.
        confidence = support / (total + 1)
        if confidence >= .98:
            rules[f] = confidence, examples[f[0], choice]
    return rules


def predict(rules, words, i):
    matched = [rules[f] for f in features(words, i) if f in rules]
    if matched:
        return max(matched, key=lambda m: m[0])[1]


def holdout(ref):
    return hashlib.sha256(ref.encode()).digest()[0] < 26


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    args = parser.parse_args()
    verses = Athens(args.repo).verses
    rules = train((ref, rows) for ref, rows in verses.items() if not holdout(ref))
    right = total = 0
    for ref, entries in verses.items():
        if not holdout(ref):
            continue
        words = [key(e[0]) for e in entries]
        for i, e in enumerate(entries):
            candidate = predict(rules, words, i)
            if candidate and all(e[1:4]):
                total += 1
                right += e[1:4] == candidate[1:4]
    print(f"Held-out Athens exact lemma, grammar and gloss: {right}/{total}", flush=True)
    if not total or right / total < .98:
        raise ValueError("Held-out exact agreement below 98%")
    db = sqlite3.connect(DB, timeout=90)
    refs = db.execute("SELECT DISTINCT ref FROM token WHERE basis='needs local analysis'").fetchall()
    changed = 0
    for ref, in refs:
        rows = db.execute("SELECT position,surface,basis FROM token WHERE ref=? ORDER BY position", (ref,)).fetchall()
        words = [key(r[1]) for r in rows]
        updates = []
        for i, (pos, surface, basis) in enumerate(rows):
            if basis == 'needs local analysis' and (e := predict(rules, words, i)):
                updates.append((*e[1:4], *e[4:], REV, ref, pos))
        if updates:
            with db:
                changed += db.executemany("""UPDATE token SET lemma=?,grammar=?,gloss=?,source_ref=?,
                    source_position=?,source_revision=?,basis='Athens lexical prediction'
                    WHERE ref=? AND position=? AND basis='needs local analysis'""", updates).rowcount
    print(f"{changed} lexical predictions")


if __name__ == "__main__":
    main()
