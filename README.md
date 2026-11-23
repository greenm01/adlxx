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

For source numbering, matching rules, local model settings, and instructions for rebuilding or checking the database, see the [build notes](docs/build.md).

## Public domain and source credits

ADLXX dedicates its own code, documentation, original English glosses, editorial work, and any database rights it holds to the public domain under **CC0 1.0 Universal**. You can copy, adapt, and redistribute those contributions, including commercially. The Athens project also dedicates its original English interlinear work to the public domain. [ADLXX license](LICENSE) · [Athens license](https://github.com/greenm01/athens-lxx/blob/3ffd871904268583043ebf1886e700486504cc84/LICENSE)

Apostoliki Diakonia supplies the online Greek text. Perseus Morpheus supplies candidate grammatical analyses. Each source retains its own terms. The ADLXX dedication covers rights its contributors hold. [Apostoliki Diakonia](https://apostoliki-diakonia.gr/bible/genesis/) · [Perseids Morpheus](https://github.com/perseids-tools/morpheus/tree/ab6898ffed335fc6169fa02c9940657a9b5a78e0)
