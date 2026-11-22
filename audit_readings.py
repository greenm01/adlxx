"""Verify the source of every populated token analysis in a database snapshot."""

import argparse
import csv
import hashlib
import sqlite3
from collections import Counter
from pathlib import Path

from corpus_alignment import key
from corpus_build import DB, REV, Athens
from corpus_choices import accent, candidates, normalized
from corpus_morphology import consensus
from publisher_catalog import ROOT


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("repo", type=Path)
    cli.add_argument("--database", type=Path, default=DB)
    args = cli.parse_args()
    sources = Athens(args.repo).verses
    options = candidates(args.repo)
    db = sqlite3.connect(
        args.database.resolve().as_uri() + "?mode=ro", uri=True, timeout=90
    )
    db.execute("BEGIN")
    errors = Counter()
    checked = Counter()
    for ref, pos, revision, lemma, grammar, gloss, basis in db.execute("""
        SELECT source_ref,source_position,source_revision,lemma,grammar,gloss,basis
        FROM token WHERE basis NOT IN ('needs local analysis','local draft')"""):
        entries = sources.get(ref, ())
        entry = entries[pos - 1] if pos and 0 < pos <= len(entries) else None
        if (
            revision != REV
            or not entry
            or entry[1:] != (lemma, grammar, gloss, ref, pos)
        ):
            errors[basis] += 1
        checked[basis] += 1
    for basis, n in db.execute("""
        SELECT t.basis,count(*) FROM token t WHERE basis='local draft'
        AND NOT EXISTS (SELECT 1 FROM model_reading m WHERE m.ref=t.ref AND m.position=t.position
        AND m.surface=t.surface AND m.lemma=t.lemma AND m.grammar=t.grammar AND m.gloss=t.gloss
        AND length(m.host)>0 AND length(m.model)>0) GROUP BY t.basis"""):
        errors[basis] += n
    for surface, lemma, grammar, gloss, ref, pos, choice in db.execute("""
        SELECT t.surface,t.lemma,t.grammar,t.gloss,t.source_ref,t.source_position,d.choice
        FROM token t LEFT JOIN candidate_decision d ON d.ref=t.ref AND d.position=t.position
        AND d.surface=t.surface AND d.model='qwen3.5:9b' WHERE t.basis='local Athens choice'"""):
        readings = options.get(accent(normalized(surface)), ())
        if (
            not choice
            or choice > len(readings)
            or readings[choice - 1] != (lemma, grammar, gloss, ref, pos)
        ):
            errors["local Athens choice decision"] += 1
    checked["local draft"] = db.execute(
        "SELECT count(*) FROM token WHERE basis='local draft'"
    ).fetchone()[0]
    consistent = consensus(sources)
    surfaces = db.execute("SELECT DISTINCT surface FROM token").fetchall()
    expected = {
        (s, *e[1:3], *e[4:], REV) for (s,) in surfaces if (e := consistent.get(key(s)))
    }
    stored = set(db.execute("SELECT * FROM form_morphology"))
    if differences := len(expected ^ stored):
        errors["form_morphology"] += differences
    checked["form_morphology"] = len(stored)
    lemmas = consensus(sources, lemma_only=True)
    expected = {
        (s, e[1], *e[4:], REV) for (s,) in surfaces if (e := lemmas.get(key(s)))
    }
    stored = set(db.execute("SELECT * FROM form_lemma"))
    if differences := len(expected ^ stored):
        errors["form_lemma"] += differences
    checked["form_lemma"] = len(stored)
    bad_lemmas = db.execute("""
        SELECT count(*) FROM interlinear i JOIN token t USING(ref,position)
        JOIN form_lemma l ON l.surface=t.surface
        LEFT JOIN form_morphology m ON m.surface=t.surface
        WHERE t.basis='local draft' AND i.status<>'reviewed' AND m.surface IS NULL
        AND (i.basis<>'Athens lemma + local parsing and gloss' OR i.lemma IS NOT l.lemma
          OR i.grammar IS NOT t.grammar OR i.gloss IS NOT t.gloss
          OR i.lemma_source_ref IS NOT l.source_ref
          OR i.lemma_source_position IS NOT l.source_position
          OR i.lemma_source_revision IS NOT l.source_revision)""").fetchone()[0]
    if bad_lemmas:
        errors["combined lemma and local analysis"] += bad_lemmas
    bad_combinations = db.execute("""
        SELECT count(*) FROM interlinear i JOIN token t USING(ref,position)
        JOIN form_morphology m ON m.surface=t.surface
        WHERE t.basis='local draft' AND i.status<>'reviewed'
        AND (i.basis<>'Athens morphology + local gloss' OR i.lemma IS NOT m.lemma
          OR i.grammar IS NOT m.grammar OR i.gloss IS NOT t.gloss
          OR i.morphology_source_ref IS NOT m.source_ref
          OR i.morphology_source_position IS NOT m.source_position
          OR i.morphology_source_revision IS NOT m.source_revision)""").fetchone()[0]
    if bad_combinations:
        errors["combined morphology and gloss"] += bad_combinations
    for table, filenames in (
        ("pilot_analysis", ["analyses.tsv"]),
        ("editorial_review", ["reviewed.tsv", "corpus-reviewed.tsv"]),
    ):
        fields = [r[1] for r in db.execute(f"PRAGMA table_info({table})")]
        expected = set()
        for name in filenames:
            with (ROOT / "data" / name).open() as stream:
                for row in csv.DictReader(stream, delimiter="\t"):
                    row["position"] = int(row["position"])
                    expected.add(tuple(row[f] for f in fields))
                    context = db.execute(
                        "SELECT t.surface,v.greek FROM token t JOIN verse v USING(ref) WHERE ref=? AND position=?",
                        (row["ref"], row["position"]),
                    ).fetchone()
                    if (
                        not context
                        or context[0] != row["surface"]
                        or (
                            "context_sha256" in row
                            and hashlib.sha256(context[1].encode()).hexdigest()
                            != row["context_sha256"]
                        )
                    ):
                        errors[table + " context"] += 1
        stored = set(db.execute(f"SELECT * FROM {table}"))
        if stored != expected:
            errors[table] += len(stored ^ expected)
        checked[table] = len(stored)
    print("Checked", dict(checked))
    print("Source mismatches", dict(errors))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
