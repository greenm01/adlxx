"""Find repeated Athens forms whose preferred lemma and full grammar always agree."""

import argparse
import sqlite3
from pathlib import Path

from corpus_alignment import key
from corpus_build import DB, REV, Athens

SCHEMA = """CREATE TABLE IF NOT EXISTS form_morphology(
    surface TEXT PRIMARY KEY,lemma TEXT NOT NULL,grammar TEXT NOT NULL,
    source_ref TEXT NOT NULL,source_position INTEGER NOT NULL,source_revision TEXT NOT NULL)"""


LEMMA_SCHEMA = """CREATE TABLE IF NOT EXISTS form_lemma(
    surface TEXT PRIMARY KEY, lemma TEXT NOT NULL,source_ref TEXT NOT NULL,
    source_position INTEGER NOT NULL,source_revision TEXT NOT NULL)"""


def consensus(verses, *, lemma_only=False):
    stop = 2 if lemma_only else 3
    anchors = {}
    repeated = set()
    for entries in verses.values():
        for e in entries:
            form = key(e[0])
            first = anchors.setdefault(form, e)
            if not first or not all(e[1:stop]) or first[1:stop] != e[1:stop]:
                anchors[form] = None
            elif first[4] != e[4]:
                repeated.add(form)
    return {f: anchors[f] for f in repeated if anchors[f]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    verses = Athens(parser.parse_args().repo).verses
    lookup = consensus(verses)
    lemmas = consensus(verses, lemma_only=True)
    with sqlite3.connect(DB, timeout=90) as db:
        db.execute(SCHEMA)
        db.execute(LEMMA_SCHEMA)
        surfaces = db.execute("SELECT DISTINCT surface FROM token").fetchall()
        rows = [
            (surface, *e[1:3], *e[4:], REV)
            for (surface,) in surfaces
            if (e := lookup.get(key(surface)))
        ]
        lemma_rows = [
            (s, e[1], *e[4:], REV) for (s,) in surfaces if (e := lemmas.get(key(s)))
        ]
        db.execute("DELETE FROM form_lemma")
        db.executemany("INSERT INTO form_lemma VALUES(?,?,?,?,?)", lemma_rows)
        db.execute("DELETE FROM form_morphology")
        db.executemany("INSERT INTO form_morphology VALUES(?,?,?,?,?,?)", rows)
    print(
        f"{len(rows)} distinct AD surface spellings with consistent Athens morphology"
    )


if __name__ == "__main__":
    main()
