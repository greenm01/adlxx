"""Install the source-linked interlinear view and the checked Genesis pilot."""

import csv
import hashlib
import sqlite3
from corpus_build import DB
from corpus_morphology import SCHEMA as MORPHOLOGY_SCHEMA
from publisher_catalog import ROOT


def install(db):
    with (ROOT / "data/analyses.tsv").open() as f:
        readings = list(csv.DictReader(f, delimiter="\t"))
    with (ROOT / "data/reviewed.tsv").open() as f:
        reviewed = list(csv.DictReader(f, delimiter="\t"))
    with (ROOT / "data/corpus-reviewed.tsv").open() as f:
        reviewed.extend(csv.DictReader(f, delimiter="\t"))
    with db:
        db.execute(
            """CREATE TABLE IF NOT EXISTS pilot_analysis(ref TEXT,position INTEGER,surface TEXT,role TEXT,host TEXT,model TEXT,lemma TEXT,grammar TEXT,gloss TEXT,PRIMARY KEY(ref,position,role))"""
        )
        db.execute(
            """CREATE TABLE IF NOT EXISTS editorial_review(ref TEXT,position INTEGER,surface TEXT,lemma TEXT,grammar TEXT,gloss TEXT,note TEXT,PRIMARY KEY(ref,position))"""
        )
        db.execute("DELETE FROM pilot_analysis")
        db.execute("DELETE FROM editorial_review")
        for r in readings:
            row = db.execute(
                "SELECT t.surface,v.greek FROM token t JOIN verse v USING(ref) WHERE ref=? AND position=?",
                (r["ref"], r["position"]),
            ).fetchone()
            if (
                not row
                or row[0] != r["surface"]
                or hashlib.sha256(row[1].encode()).hexdigest() != r["context_sha256"]
            ):
                raise ValueError(
                    f"Pilot context changed at {r['ref']} word {r['position']}"
                )
            fields = (
                "ref",
                "position",
                "surface",
                "role",
                "host",
                "model",
                "lemma",
                "grammar",
                "gloss",
            )
            db.execute(
                "INSERT INTO pilot_analysis VALUES(?,?,?,?,?,?,?,?,?)",
                [r[k] for k in fields],
            )
        for r in reviewed:
            if db.execute(
                "SELECT surface FROM token WHERE ref=? AND position=?",
                (r["ref"], r["position"]),
            ).fetchone() != (r["surface"],):
                raise ValueError(f"Review moved at {r['ref']} word {r['position']}")
            db.execute(
                "INSERT INTO editorial_review VALUES(?,?,?,?,?,?,?)",
                [
                    r[k]
                    for k in (
                        "ref",
                        "position",
                        "surface",
                        "lemma",
                        "grammar",
                        "gloss",
                        "note",
                    )
                ],
            )
        db.execute(MORPHOLOGY_SCHEMA)
        db.execute("DROP VIEW IF EXISTS interlinear")
        db.execute("""CREATE VIEW interlinear AS SELECT t.ref,t.position,t.surface,
          COALESCE(r.lemma,m.lemma,t.lemma,p.lemma) AS lemma,
          COALESCE(r.grammar,m.grammar,t.grammar,p.grammar) AS grammar,
          COALESCE(r.gloss,t.gloss,p.gloss) AS gloss,
          CASE WHEN r.ref IS NOT NULL THEN 'reviewed'
               WHEN t.gloss IS NOT NULL OR p.gloss IS NOT NULL THEN 'draft' ELSE 'pending' END AS status,
          CASE WHEN r.ref IS NOT NULL THEN 'editorial review'
               WHEN m.surface IS NOT NULL THEN 'Athens morphology + local gloss'
               WHEN t.gloss IS NULL AND p.ref IS NOT NULL THEN 'Genesis pilot' ELSE t.basis END AS basis,
          sp.url AS publisher_url,
          CASE WHEN r.ref IS NULL THEN COALESCE(m.source_ref,t.source_ref) END AS morphology_source_ref,
          CASE WHEN r.ref IS NULL THEN COALESCE(m.source_position,t.source_position) END AS morphology_source_position,
          CASE WHEN r.ref IS NULL THEN COALESCE(m.source_revision,t.source_revision) END AS morphology_source_revision
          FROM token t JOIN verse v USING(ref)
          JOIN source_page sp ON sp.book=v.book AND sp.chapter=v.chapter
          LEFT JOIN form_morphology m ON m.surface=t.surface AND t.basis='local draft'
          LEFT JOIN editorial_review r USING(ref,position,surface)
          LEFT JOIN pilot_analysis p ON p.ref=t.ref AND p.position=t.position AND p.surface=t.surface AND p.role='draft'""")


if __name__ == "__main__":
    with sqlite3.connect(DB, timeout=90) as db:
        install(db)
