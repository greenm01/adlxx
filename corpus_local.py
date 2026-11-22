"""Run resumable local inference for AD tokens without a reusable Athens analysis."""

import argparse
import json
import os
import sqlite3
import subprocess
import time
from uuid import uuid4

from corpus_build import DB
from interlinear import analyze, ROOT


def claim(db, worker):
    now = int(time.time())
    db.execute("BEGIN IMMEDIATE")
    try:
        result = db.execute(
            """SELECT t.ref,v.greek FROM token t JOIN verse v USING(ref)
        WHERE t.basis='needs local analysis' AND NOT EXISTS
          (SELECT 1 FROM lease l WHERE l.ref=t.ref AND l.expires>?)
        LIMIT 1""",
            (now,),
        ).fetchone()
        if not result:
            db.commit()
            return
        ref, greek = result
        db.execute(
            "INSERT OR REPLACE INTO lease VALUES(?,?,?)", (ref, worker, now + 600)
        )
        tokens = db.execute(
            "SELECT position,surface FROM token WHERE ref=? AND basis='needs local analysis' ORDER BY position LIMIT 16",
            (ref,),
        ).fetchall()
        db.commit()
        return ref, greek, tokens
    except BaseException:
        db.rollback()
        raise


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("host", choices=["crunch", "localhost"])
    args = cli.parse_args()
    host = args.host
    model = "qwen3.5:9b" if host == "crunch" else "gemma3:12b"
    worker = f"{host}:{os.getpid()}:{uuid4().hex[:8]}"
    cache = ROOT / "build/corpus-model-cache"
    cache.mkdir(exist_ok=True)
    with sqlite3.connect(DB, timeout=90) as db:
        db.executescript("""CREATE TABLE IF NOT EXISTS lease(ref TEXT PRIMARY KEY,worker TEXT,expires INTEGER);
        CREATE TABLE IF NOT EXISTS parser_hint(ref TEXT,position INTEGER,model TEXT,candidates TEXT,PRIMARY KEY(ref,position,model));
        CREATE TABLE IF NOT EXISTS model_reading(ref TEXT,position INTEGER,surface TEXT,host TEXT,model TEXT,lemma TEXT,grammar TEXT,gloss TEXT,PRIMARY KEY(ref,position,model));""")
        while True:
            job = claim(db, worker)
            if not job:
                break
            ref, greek, tokens = job
            try:
                positions, words = zip(*tokens)
                has_parser = db.execute(
                    "SELECT 1 FROM sqlite_master WHERE type='table' AND name='morpheus_parse'"
                ).fetchone()
                hints = {}
                if has_parser:
                    for position, surface in tokens:
                        candidates = [
                            row[0]
                            for row in db.execute(
                                """SELECT p.analysis FROM morpheus_form f JOIN morpheus_parse p
                            USING(beta,revision) WHERE f.surface=? ORDER BY p.analysis LIMIT 9""",
                                (surface,),
                            )
                        ]
                        if 0 < len(candidates) <= 8:
                            hints[position] = candidates
                result = analyze(
                    host, model, greek, words, cache, positions, hints=hints
                )
                with db:
                    if db.execute(
                        "SELECT worker FROM lease WHERE ref=?", (ref,)
                    ).fetchone() != (worker,):
                        continue
                    if db.execute(
                        "SELECT greek FROM verse WHERE ref=?", (ref,)
                    ).fetchone() != (greek,):
                        db.execute("DELETE FROM lease WHERE ref=?", (ref,))
                        continue
                    for r in result:
                        db.execute(
                            "INSERT OR REPLACE INTO model_reading VALUES(?,?,?,?,?,?,?,?)",
                            (
                                ref,
                                r["position"],
                                r["surface"],
                                host,
                                model,
                                r["lemma"],
                                r["grammar"],
                                r["gloss"],
                            ),
                        )
                        changed = db.execute(
                            """UPDATE token SET lemma=?,grammar=?,gloss=?,basis='local draft'
                        WHERE ref=? AND position=? AND surface=? AND basis='needs local analysis'""",
                            (
                                r["lemma"],
                                r["grammar"],
                                r["gloss"],
                                ref,
                                r["position"],
                                r["surface"],
                            ),
                        )
                        if changed.rowcount and r["position"] in hints:
                            db.execute(
                                "INSERT OR REPLACE INTO parser_hint VALUES(?,?,?,?)",
                                (
                                    ref,
                                    r["position"],
                                    model,
                                    json.dumps(
                                        hints[r["position"]], ensure_ascii=False
                                    ),
                                ),
                            )
                    db.execute("DELETE FROM lease WHERE ref=?", (ref,))
                print(ref, len(tokens), flush=True)
            except (
                ValueError,
                RuntimeError,
                subprocess.SubprocessError,
                OSError,
                KeyError,
                TypeError,
                IndexError,
            ) as error:
                print(f"{ref}: {error}", flush=True)
                with db:
                    db.execute(
                        "UPDATE lease SET expires=? WHERE ref=? AND worker=?",
                        (int(time.time()) + 3600, ref, worker),
                    )


if __name__ == "__main__":
    main()
