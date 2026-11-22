# Apostoliki Diakonia Septuagint Interlinear

A local Greek–English word database for the Septuagint text published online by Apostoliki Diakonia. The chapter pilot covers Genesis 1:1–31. The project takes its Greek, verse addresses and token positions directly from the publisher. [Publisher’s Genesis](https://apostoliki-diakonia.gr/bible/genesis/)

The source table records the Greek wording and punctuation, its URL and retrieval date. HTML whitespace is collapsed. Token positions begin at one within each verse. The full verse retains spaces and punctuation. Lemmas, morphology and English glosses are separate analyses of the Greek in context. Each model reading carries its own status and provenance. An English gloss can depend on the construction as a whole.

## Local build

Start Ollama on the Mac. Crunch must be reachable as the SSH host `crunch` with its Ollama API listening on localhost. The pilot uses Qwen 3.5 9B on Crunch to draft and Gemma 3 12B on the Mac for an independent second reading. Each gets the same Greek verse and numbered tokens. No cloud inference is required.

```sh
python3 interlinear.py --save-snapshot
sqlite3 -header -column build/adlxx.sqlite "SELECT position,surface,model,lemma,grammar,gloss FROM token JOIN analysis USING(ref,position) WHERE ref='GEN 1:1' ORDER BY position,model"
```

Successful responses are cached locally. Rerunning with the same inputs reuses them. A failed build rolls back the database transaction. Both model readings remain drafts, including where they agree. The `interlinear` view shows the Crunch draft unless a separately recorded reading in `data/reviewed.tsv` takes precedence. Each reviewed reading is checked against the source token at its recorded position before loading.

## Genesis 1 review

The chapter has 742 Greek tokens, with 28 directly checked readings. To read the English interlinear in Greek order:

```sh
sqlite3 -header -column build/adlxx.sqlite "SELECT surface,lemma,grammar,gloss,status FROM interlinear WHERE ref='GEN 1:26' ORDER BY position"
```

For example, the reviewed gloss at 1:5 preserves the cardinal “one.” At 1:26 the first-person plural subjunctive is glossed “let us make.” Both underlying model responses remain available in the analysis table.

To verify the source transcription from a saved publisher page, run the importer with the date on which that page was retrieved. It checks for a single chapter text and every numbered verse in order.

```sh
python3 import_genesis1.py build/genesis-1.html --retrieved 2026-11-22 | diff data/verses.tsv -
```

Before distributing a book-length text, identify the underlying printing and document the publisher's terms for reuse.

## Rebuild without inference

The chapter's two model readings are saved in `data/analyses.tsv`. Build the database from a fresh checkout without starting Ollama or connecting to Crunch:

```sh
python3 interlinear.py --from-snapshot
```

The loader verifies each reading’s source token, verse checksum and model identity, and requires complete coverage from both machines.

Ollama reported model digests `56671c2ab9385f9cfcb404638e32cd62d88e3501d44822208363c010179a3c90` for the Crunch draft and `b92b218582c521ba287f38f1d6057dcd3c6cbff036f13cac97b5d861f5e58ec3` for the Mac reading.

## Reusing Athens analyses

The optional comparison reads a pinned Athens chapter and retains AD's own surface forms and token positions.

```sh
python3 athens_candidates.py ../athens-lxx-public > build/athens-candidates.tsv
```

In Genesis 1, 191 of 742 tokens belong to ten verses whose complete word sequences match. Another 422 have the same preceding and following word (or verse boundary) at a unique position in both versions of the verse. The test normalizes case, canonically equivalent Unicode forms and elision marks. A further 108 tokens have a matching form somewhere in Athens Genesis 1. The remaining 21 have no such form in that chapter. Searching the full Athens interlinear found spelling matches for 20 of those 21 occurrences. This leaves 741 of 742 AD tokens with an Athens form candidate somewhere in the corpus. The exception is the spelling of the noun for living creatures at Genesis 1:21. AD prints ζῴων and Athens prints ζώων in the same passage.

For subsequent chapters, whole-verse matches are the first candidates to import as attributed drafts. Use local review for the shorter context matches, especially where a governing verb, antecedent, or negation falls outside the matched words. A spelling match alone can retrieve possible analyses without selecting a gloss. Keep both the Athens reference and revision for any imported reading. The current Genesis model snapshot was generated independently of Athens.

## Whole-edition build in progress

`data/publisher-chapters.tsv` lists 1,102 navigation entries across the publisher’s 50 book pages. Daniel and Sirach include entries numbered zero. Chapter headings and verse boundaries need checking against the publisher, including prologues and Greek additions. This catalog is the download inventory.

`python3 publisher_catalog.py` downloads resumable compressed page copies under `build/publisher`. Run `python3 corpus_build.py ../athens-lxx-public --follow` to stage available chapters in `build/corpus.sqlite`. Each source page has a URL, checksum and import disposition. Nonstandard verse sequences are queued for inspection. The current whole-edition database is a work in progress; the verified Genesis 1 database remains available separately during the build.

Staged token rows carry the Athens revision and source position for each reused reading. A consistent-form candidate means that the pinned Athens interlinear gives the same preferred lemma, grammar and gloss at every recorded occurrence of that form. All reused entries are drafts. Run `python3 corpus_local.py crunch` and `python3 corpus_local.py localhost` with their respective Ollama services available to draft unresolved tokens. Each worker sees the verse, claims distinct positions and records model provenance.
