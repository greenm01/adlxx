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

The publisher places some numbered verses after the main sequence. The importer keeps their printed order in Joshua 20 and 1 Kingdoms 17–18. It retains the range 18–22 in Joshua 12 as one text with one address. In Deuteronomy 3 the page prints two entries numbered 14. The second has the local address `14#2` so both Greek entries survive. Leviticus 2:4 has an unnumbered opening and Numbers 15:19 prints a single 9 between 18 and 20. Their local boundaries are anchored to the Greek wording in the importer.

`python3 corpus_context.py ../athens-lxx-public` can recover further Athens candidates for unresolved tokens where the same three-word sequence occurs elsewhere in the edition and the preferred analyses of the middle word agree across the matched occurrences. This pass folds grave to acute for matching, retains the publisher's surface and records the Athens position used.

The navigation links group several works under other chapter headings. The Psalm 150 page also contains Psalm 151. Proverbs 24 carries Proverbs 30 and 31:1–9 in sections marked by printed Masoretic cross-references; Proverbs 29 continues with 31:10–31. The first verse of Proverbs 30 follows the publisher's 22ε marker. Daniel's entries 0 and 13 contain Susanna and Bel and the Dragon respectively. Sirach 0 contains the unnumbered prologue. In the staging verse table, `book` and `chapter` identify the source page and `ref` identifies the individual passage.

The optional `corpus_passages.py` pass searches the nearby Athens chapters for unique five-word runs. A center or edge word can receive an attributed draft even when verse divisions differ. Conflicting offsets and repeated sequences are excluded.

`data/publisher-numbering.tsv` records skipped numeric labels observed on particular publisher pages. A skipped label alone does not establish a Greek omission. The importer retains the available Greek under its printed labels. Separately anchored address repairs include Psalm 53:6, 1 Kingdoms 16:23, and 1 Maccabees 3:9 and 3:51. The Greek text at those points was checked against the corresponding Athens clause.

Run `python3 corpus_reader.py` after importing Genesis 1 to install the whole-edition `interlinear` view in the working database. It checks the Genesis pilot snapshot and its editorial decisions against the publisher tokens. Each result identifies its URL, the basis of the gloss, and whether a reading is pending, drafted or directly reviewed. Run `python3 audit_corpus.py` for a read-only audit of cached source checksums, verse order, exact Greek, token positions and reading coverage. The `--final` option also requires all catalog pages and token readings.

For ambiguous forms, `corpus_choices.py ../athens-lxx-public crunch` asks the local model to select a complete Athens analysis in AD verse context, with an option to abstain. A selection retains the exact Athens reference and word position and is labeled a model draft. In three small controls Qwen selected the appropriate reading twice and abstained when both verb options were wrong. Gemma selected a wrong answer on that abstention control, so the candidate-selection run uses Crunch. These controls do not establish a corpus-wide accuracy rate.

Daniel 3 includes an independently numbered Prayer of Azariah and Song of the Three between narrative verses 23 and 24. Its 67 verses have local references S3Y 1:1–67. Lamentations 3 repeats verse 8 and prints 206 at the opening of verse 20. The repeated entry is retained as 8#2. The unnumbered opening of 4 Maccabees 1:9 is anchored to the publisher's own Greek.

Run `python3 corpus_alignment.py ../athens-lxx-public` to align words in verses with at least 80% word-sequence overlap relative to the longer verse and at least five shared words in order. Every optimal alignment must pair the AD word with the same Athens position. The publisher's spelling is retained. The pass recovered 29,020 draft readings on its first full run.

Run `python3 corpus_lexical.py ../athens-lxx-public` for conservative local predictions based on form and neighboring words. It requires at least 98% exact agreement on held-out Athens verses before writing predictions. The first run matched 6,409 of 6,428 tested Athens readings across all three fields. Accuracy on the unresolved AD words has not been measured. These predictions carry their own basis and their Athens source position. The local models process outstanding words in context.

Run `python3 audit_readings.py ../athens-lxx-public` to compare each attributed reading with the exact lemma, grammar and gloss in the pinned Athens source and to check local drafts and candidate selections against the stored model evidence.

`python3 corpus_shifted.py ../athens-lxx-public` applies the same word-alignment rule to closely parallel verses at different addresses in the same book. At least two distinct three-word sequences must each point uniquely to the same Athens verse within that book. If another verse has support, the selected verse must have at least twice as many anchors. These readings retain both verse addresses.
