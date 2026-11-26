# ADLXX: An English Interlinear for the Septuagint

Read the Greek Old Testament one word at a time, with **an English gloss for every Greek word**. ADLXX pairs the Septuagint text published by Apostoliki Diakonia with English glosses, Greek dictionary forms (lemmas), and grammatical analyses. The words stay in Greek order, so you can see how a verse works even when English would put it differently.

**[Download the Greek–English interlinear spreadsheet (compressed TSV)](https://github.com/greenm01/adlxx/releases/download/v0.1.0/adlxx-interlinear.tsv.gz)** · [Download the full SQLite database](https://github.com/greenm01/adlxx/releases/download/v0.1.0/adlxx-ot.sqlite)

## A verse in miniature

In Genesis 1:3, Greek repeats the word for *light*. Here are the last five words of the verse as they appear in the interlinear.

| Greek | γενηθήτω | φῶς | καὶ | ἐγένετο | φῶς |
| --- | --- | --- | --- | --- | --- |
| English gloss | let there be | light | and | there came to be | light |

Sometimes a single Greek verb needs several English words. At Genesis 1:26, *ποιήσωμεν* gets the gloss “let us make.” Its grammatical entry explains the first-person plural subjunctive.

## What’s inside

Version 0.1.0 covers **581,722 Greek word positions in 28,668 verse records**, drawn from all 1,102 pages in the publisher’s 50 book listings. Every position has an English gloss. The spreadsheet gives the reference, word position, Greek spelling, lemma, grammar, English gloss, review status, basis for the reading, and publisher’s page. Unzip it and open the tab-separated file in a spreadsheet app. [Publisher’s Genesis](https://apostoliki-diakonia.gr/bible/genesis/)

The database also records how each reading was chosen. Many glosses come from matching Greek in the Athens Septuagint interlinear. Local models on a Mac and a Linux machine helped draft or select readings where the wording differed. Of the 581,722 readings, **80 have received direct editorial review**. The other **581,642 are drafts**. The release checks verified the Greek against the captured pages and traced readings to their recorded sources. English sense and grammar still call for editorial judgment. [Athens interlinear](https://github.com/greenm01/athens-lxx/tree/3ffd871904268583043ebf1886e700486504cc84/interlinear)

## Look up a passage

With SQLite installed, run this in the directory where you saved the database. Change the reference to read another verse.

```sh
sqlite3 -readonly -header -column adlxx-ot.sqlite \
  "SELECT position, surface, lemma, grammar, gloss, status
   FROM interlinear WHERE ref = 'GEN 1:26' ORDER BY position"
```

The publisher prints one editor's note inside the text, at the end of 4 Maccabees 1: it explains that the Church does not count the book as canonical. The note is not scripture, so it is left out of the verses and words. It is kept verbatim, with an English rendering, in [`data/edition-notes.tsv`](data/edition-notes.tsv) and in the release's `edition_note` table, for use as a footnote or margin note.

For source numbering, matching rules, local model settings, and instructions for rebuilding or checking the database, see the [build notes](docs/build.md).

## How it was checked, and how to correct it

The glosses, lemmas and grammar were drafted with help from local language models and then checked by script and by reading. Every word was compared with the Athens interlinear and with the single-word glosses of the Apostolic Bible Polyglot where the Greek matches, and each difference was decided in its verse. Grammar was checked against the Morpheus parser. Glosses were checked against Brenton's English Septuagint as revised by Boyd. The [review record](docs/abp-gloss-review.md) says what each pass checked and what it changed.

The editors do not read Greek professionally, and no Septuagint scholar has yet reviewed the interlinear. Treat a gloss or parsing as a careful draft, not an authority. If you read Greek and find an error, please [open an issue](https://github.com/greenm01/adlxx/issues) with the reference, the word position and what it should be. Corrections from readers who know the language are the most useful contribution this project can receive.

### Misprints in the online text

The Greek comes from the publisher's website, which has typing errors that the printed edition probably lacks. ADLXX keeps the online Greek exactly as published. Where a word is mistyped, the gloss, lemma and grammar follow the word that was meant, and the [errata list](docs/adlxx-errata.md) records the place. The [list itself](docs/adlxx-errata.tsv) gives each word, the intended word and the witnesses that support it.

## Public domain and source credits

ADLXX dedicates its own code, documentation, original English glosses, editorial work, and any database rights it holds to the public domain under **CC0 1.0 Universal**. You can copy, adapt, and redistribute those contributions, including commercially. The Athens project also dedicates its original English interlinear work to the public domain. [ADLXX license](LICENSE) · [Athens license](https://github.com/greenm01/athens-lxx/blob/3ffd871904268583043ebf1886e700486504cc84/LICENSE)

Apostoliki Diakonia supplies the online Greek text. Perseus Morpheus supplies candidate grammatical analyses. Each source retains its own terms. The ADLXX dedication covers rights its contributors hold. [Apostoliki Diakonia](https://apostoliki-diakonia.gr/bible/genesis/) · [Perseids Morpheus](https://github.com/perseids-tools/morpheus/tree/ab6898ffed335fc6169fa02c9940657a9b5a78e0)

## Lexical study in SQLite

The local database build includes three lookups. The concordance gives the verse and word position for each occurrence of a Greek lemma. The English–Greek index searches whole editorial glosses, including phrases. The analytical lexicon groups attested spellings by lemma and stored grammatical analysis and counts the occurrences of each analysis.

```sql
SELECT ref, occurrence, position, surface, english FROM lexical_concordance
WHERE lemma = 'φῶς' ORDER BY ref, occurrence, position;

SELECT lemma, surface, ref, position FROM english_greek_index
WHERE english = 'light';

SELECT surface, lemma, grammar, occurrences FROM analytical_lexicon
WHERE surface = 'φῶς';

SELECT ref, occurrence, position, surface FROM ab_strong_assignment
WHERE ab_strong = '180.2';
```

AB-Strong numbers are stored as text, including every dotted component. Genesis 1:1–4 has 55 verified single-word assignments, checked against this edition’s own Greek positions. Unassigned tokens have a null AB-Strong number in the concordance. The three lexical lookups use this project’s glosses and analyses. The publisher offers its own concordance, index, and analytical lexicon separately. [ABP numbering introduction](https://apostolicbible.com/intro.pdf) · [Genesis comparison text](https://biblehub.com/interlinear/apostolic/genesis/1.htm)


The local build uses SQLite with FTS5. Search for a word within a gloss, or put a phrase in double quotes inside the search string. Each hit keeps the original gloss and opens on the Greek verse in this edition. This follows the English index, concordance, and inflected-form workflow in the [ABP study guide, pp. 6–11](https://www.apostolicbible.com/studyguide.pdf#page=6).

```sql
SELECT e.ref, e.occurrence, e.position, e.english, e.surface, e.lemma, e.greek_verse
FROM gloss_search s JOIN english_greek_context e ON e.english = s.english
WHERE gloss_search MATCH 'beginning' AND e.ref = 'GEN 1:1';

SELECT ref, position, surface, grammar FROM morphological_concordance
WHERE lemma = 'ἀρχή' AND grammatical_case = 'dative';

SELECT g.ref, head.surface, dependent.surface, g.governed_case
FROM governed_phrase g
JOIN lexical_concordance head USING (ref, occurrence)
JOIN lexical_concordance dependent USING (ref, occurrence)
WHERE head.position = g.governor_position AND dependent.position = g.complement_position;
```

The morphological concordance retains the recorded grammar and exposes part of speech, case, gender, number, tense, voice, mood, verb form, and person where the description supports extraction. A blank feature can mean it is inapplicable, ambiguous, or unparsed. The governed-phrase table contains three reviewed relationships in Genesis 1:1–2, including the dative governed by ἐν. The case belongs to the complement. [ABP study guide, pp. 14–16](https://www.apostolicbible.com/studyguide.pdf#page=14)

Genesis 1:4 illustrates how to extend the numbering across editions. The Polyglot prints 303.1 for an expression this edition writes as two words, ἀνὰ μέσον. Both occurrences are recorded by their full spans in `ab_strong_phrase`. Further assignments require checking the Greek wording and position in this edition. [Genesis comparison text](https://biblehub.com/interlinear/apostolic/genesis/1.htm)

[Genesis 1:1–10 English gloss review against the Apostolic Bible Polyglot](docs/abp-genesis-gloss-review.md)
