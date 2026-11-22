"""Verify the source of every populated token analysis in a database snapshot."""
import argparse
from collections import Counter
from pathlib import Path
import sqlite3

from corpus_build import Athens, DB, REV
from corpus_choices import candidates, accent, normalized


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("repo", type=Path)
    args = cli.parse_args()
    sources = Athens(args.repo).verses
    options = candidates(args.repo)
    db = sqlite3.connect(DB.resolve().as_uri() + "?mode=ro", uri=True, timeout=90)
    db.execute("BEGIN")
    errors = Counter()
    checked = Counter()
    for ref, pos, revision, lemma, grammar, gloss, basis in db.execute("""
        SELECT source_ref,source_position,source_revision,lemma,grammar,gloss,basis
        FROM token WHERE basis NOT IN ('needs local analysis','local draft')"""):
        entries = sources.get(ref, ())
        entry = entries[pos-1] if pos and 0 < pos <= len(entries) else None
        if revision != REV or not entry or entry[1:] != (lemma, grammar, gloss, ref, pos):
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
        if not choice or choice > len(readings) or readings[choice-1] != (lemma, grammar, gloss, ref, pos):
            errors['local Athens choice decision'] += 1
    checked['local draft'] = db.execute("SELECT count(*) FROM token WHERE basis='local draft'").fetchone()[0]
    print("Checked", dict(checked))
    print("Source mismatches", dict(errors))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
