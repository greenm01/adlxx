# Whole-OT interlinear gloss comparison

This is the review record for both interlinears, ADLXX and [Athens-LXX](https://github.com/greenm01/athens-lxx). The `scripts/adlxx/` tools it names live in a private working repository; the record says what each one checked.

The comparison covers every indexed Greek word position in the local ADLXX and Athens-LXX databases. The comparison text is the digital Apostolic Bible Polyglot hosted by Bible Hub. Use its English gloss as a check wherever the editions share a Greek reading. Each project's Greek text governs its own translation. The publisher describes the ABP Old Testament as excluding the Deuterocanon. [ABP text description](https://apostolicbible.com/text.htm)

Run `python3 scripts/adlxx/abp_gloss_screen.py` from the working checkout of the Royal Way Bible, which is private. It reads the sibling release databases, caches chapter pages under `build/abp-gloss-review/pages`, and writes one compressed table of word positions per edition. Each row gives its edition reference, verse occurrence, word position, preferred gloss, screening result, and available ABP alignment. The pair-frequency tables help prioritize recurring differences. A verse with different numbering can be matched through two non-overlapping four-word sequences unique to that ABP book and a whole-verse similarity threshold. Greek matching folds accents, breathings, iota subscripts, and case. The aligned form, its grammar, and the surrounding clause still require inspection before a change.

| Screening result | ADLXX positions | Athens-LXX positions |
|---|---:|---:|
| Same normalized English | 191,947 | 192,221 |
| English differs, check sense | 135,093 | 130,393 |
| Grouped phrase or supplied word needs review | 88,726 | 87,545 |
| Greek differs or word alignment unresolved | 23,151 | 34,217 |
| Verse alignment unresolved | 42,478 | 51,872 |
| Book outside comparison map | 100,209 | 104,129 |
| Source chapter unavailable and no match elsewhere | 118 | 120 |
| **All indexed positions** | **581,722** | **600,497** |

The totals describe the automated screen. An aligned word with different English can reflect an idiom, grammatical information expressed on a neighboring token, a contextual sense, or a mistake in either digital text. Missing source pages and uncertain alignments retain their own status. Verse and word matches from this run supply candidates for review. They do not write AB-Strong assignments or replace glosses.

## Primary review scope

For each edition, review the preferred English for an individual Greek word aligned to the same Greek form in ABP. Verify the inflection, occurrence, and surrounding sense. Record the edition reference, word position, Greek, both English glosses, and the decision. Accent and breathing differences can be normalized for matching. Keep grouped glosses, unmatched words, and uncertain alignments out of the direct word comparison. Findings about the RPB prose belong to its separate editorial review.

## What the comparison tells us

The saved screen supports a direct, single-word English comparison at 327,002 ADLXX positions (56.2% of the index) and 322,606 Athens positions (53.7%). Within those positions, 58.6% and 59.5% respectively have the same normalized English. These figures measure wording agreement. The reviewed cases were selected for editorial interest, so they cannot establish a corpus-wide translation error rate.

Counting each Greek surface form and pair of English glosses together, with case folded and surrounding spaces stripped, the 100 most frequent differences account for 22,391 ADLXX positions and 22,462 Athens positions. Common examples include *on* beside *upon*, *because* beside *for*, and *the* beside *of the*. The last pair often reflects where an interlinear expresses Greek case. A rule that substitutes the most frequent ABP wording everywhere would erase contextual choices.

For the next editorial pass, prioritize differences that change who acts, what is counted, whether a clause is negated, or which thing a noun names. Check the Greek in each edition before changing a gloss. Track corrections to the interlinear separately from corrections to the RPB reading copy. For verse alignment work, the largest outstanding groups in this run are 1KI (5,096 positions) for ADLXX and JER (6,003) for Athens. These counts describe the saved run before subsequent gloss corrections.

## Direct decisions

- **Genesis 1:1–10.** Each edition has a verse-by-verse review of its preferred English. Both have an additional fulfillment clause at 1:6. Athens also has the clause at 1:7. [ADLXX review](https://github.com/greenm01/adlxx/blob/main/docs/abp-genesis-gloss-review.md) · [Athens review](https://github.com/greenm01/athens-lxx/blob/main/interlinear/abp-genesis-gloss-review.md)
- **Isaiah 8:21, word 4 in both editions.** Retain *you*. Both editions read ὑμᾶς, the second-person plural accusative. The digital ABP also prints the second-person form but gives it a first-person English gloss. This is an English discrepancy in the online comparator. Its origin in print or transcription has yet to be established. [ABP Isaiah 8:21](https://biblehub.com/interlinear/apostolic/isaiah/8.htm)

- **Exodus 35:6, words 3–11 in both editions.** The material list distinguishes spun scarlet, twisted fine linen, and goats’ hair. Both databases now give διπλοῦν as “doubled.” The next participle supplies “spun.” The same distinction holds in the RPB reading copy. [ABP Exodus 35](https://biblehub.com/interlinear/apostolic/exodus/35.htm)
- **Exodus 35:34, word 2 in both editions.** Both interlinears give προβιβάσαι the sense “to teach.” The digital ABP expresses assistance. The infinitive supplies what God enables the two craftsmen to do. Keep “to teach” in the reading copy. A model draft had omitted this action altogether. [ABP Exodus 35](https://biblehub.com/interlinear/apostolic/exodus/35.htm)
- **Leviticus 1:16–17.** Both editions agree with the digital ABP on the crop (1:16 word 4), the feathers (ADLXX word 7, Athens word 8), and the wings (1:17 word 6 in both). At 1:17 words 8–9, the negative and verb form a single prohibition. Read together, the editions and the ABP all say to leave the bird undivided. Retain the word glosses and the negative in running English. [ABP Leviticus 1](https://biblehub.com/interlinear/apostolic/leviticus/1.htm)
- **Exodus 36:16 in both editions corresponds to ABP Exodus 39:9.** The breastpiece is a span long and a span wide. All three Greek texts repeat διπλοῦν at the beginning and end of the description. Retain “doubled” in both places. Athens adds αὐτοῦ after each dimension, shifting the second measure and final adjective to words 11 and 15 (ADLXX words 10 and 13). The automated screen recovered the ADLXX verse link. The Athens correspondence was checked directly against the same ABP verse. [ABP Exodus 39:9](https://biblehub.com/interlinear/apostolic/exodus/39.htm)
- **Exodus 39:2 in both editions corresponds to ABP Exodus 38:25.** All three give a hundred talents and 1,775 shekels. ADLXX and the ABP give seventy and five as separate words. Athens has the compound ἑβδομηκονταπέντε at position 17. Retain the preferred interlinear glosses in both editions. Restore the missing thousand in the RPB reading copy. [ABP Exodus 38:25](https://biblehub.com/interlinear/apostolic/exodus/38.htm)
- **Exodus 38:26 in both editions corresponds to ABP Exodus 38:8.** The women supplied mirrors. A participle identifies them as women who fasted, and the following finite verb repeats “fasted” and gives the place. Both Greek editions and the digital ABP preserve these details. The RPB reading repeats the verb. [ABP Exodus 38:8](https://biblehub.com/interlinear/apostolic/exodus/38.htm)
- **Leviticus 2:5 and 2:7, word 5.** At 2:5, ADLXX, Athens and the digital ABP all have τηγάνου for the cooking vessel. At 2:7, ADLXX repeats τηγάνου, while Athens and the ABP read ἐσχάρας. The RPB reading therefore repeats “griddle” in the ADLXX passage. Athens gives “cooking pan” and the ABP specifies a grate. This is a Greek reading difference between the editions, with a separate question about how precisely to gloss the Athens noun. [ABP Leviticus 2](https://biblehub.com/interlinear/apostolic/leviticus/2.htm)
- **Leviticus 4:24, 29, 33.** The worshipper lays one hand on the animal, then the slaughtering verb changes to third-person plural. ADLXX has this verb at positions 11, 12 and 12 respectively, Athens at 12, 13 and 13. Both editions and the digital ABP preserve that shift. Keep the explicit “they” without identifying the group more narrowly than the Greek does. [ABP Leviticus 4](https://biblehub.com/interlinear/apostolic/leviticus/4.htm)
- **Leviticus 5:16 and 5:24 in ADLXX.** Both require a fifth in addition to restitution. In 5:16 all three editions have the same reference. For the second occurrence compare ADLXX 5:24 word 16, Athens 6:5 word 17, and the latter part of digital ABP 6:4. The ABP verse also contains the preceding list of property to return. Keep the principal and the added fifth distinct. The priest receives the payment in the first case and the owner in the second. [ABP Leviticus 5](https://biblehub.com/interlinear/apostolic/leviticus/5.htm) · [ABP Leviticus 6](https://biblehub.com/interlinear/apostolic/leviticus/6.htm)
- **ADLXX Leviticus 6:2, 5, 6 corresponds to Athens and ABP 6:9, 12, 13.** Each occurrence of οὐ σβεσθήσεται repeats the prohibition on quenching the altar fire. The digital ABP sometimes attaches the English negative to the verb’s displayed gloss. Read the negative and verb together in each edition. The RPB reading repeats “It shall not be quenched” all three times. [ABP Leviticus 6](https://biblehub.com/interlinear/apostolic/leviticus/6.htm)
- **Leviticus 7:5, word 13 in both editions.** Both read πλημμελείας and gloss the expression as a guilt offering. The ABP likewise identifies the trespass offering. The local RPB draft had called it a sin offering, which would obscure the distinction drawn in verse 7. Retain the interlinear entries and correct the reading copy to “trespass offering,” as in chapter 5. [ABP Leviticus 7](https://biblehub.com/interlinear/apostolic/leviticus/7.htm)
- **Leviticus 8:8 and 8:12.** At 8:8 the three Greek texts name δήλωσις followed by ἀλήθεια. Use “Disclosure and Truth,” as in the RPB Exodus 28:26. The local reading draft had reversed the pair and introduced a stone. ADLXX uses a feminine pronoun for the surface on which the breastpiece is set, referring back to the shoulder-piece. Athens reads a masculine pronoun. At 8:12 ADLXX, Athens, and the digital ABP describe Moses pouring some anointing oil onto Aaron’s head. The draft’s additional horn has no counterpart in those texts. [ABP Leviticus 8](https://biblehub.com/interlinear/apostolic/leviticus/8.htm)
- **Leviticus 9:7 and 9:24.** In 9:7 the local RPB draft added a father to the phrase τοῦ οἴκου σου. ADLXX, Athens and the digital ABP identify Aaron’s own household. Keep that distinct from the people for whom he next makes atonement. In 9:24 both interlinears correctly identify ἐξέστη (word 24) as astonishment. The ABP likewise places amazement between seeing the fire and falling upon their faces. [ABP Leviticus 9](https://biblehub.com/interlinear/apostolic/leviticus/9.htm)
- **Leviticus 10:3, word 24 in both editions.** Both read κατενύχθη and gloss it “was stricken.” The digital ABP groups the verb with Aaron’s name and likewise expresses distress. Retain “Aaron was stricken.” At 10:19–20 the related adjective and verb carry “pleasing” from Aaron’s question into Moses’ response. [ABP Leviticus 10](https://biblehub.com/interlinear/apostolic/leviticus/10.htm)
- **Leviticus 11:5–6.** Check the particle immediately before ἀνάγει in each edition. In the hare clause (5), ADLXX reads οὐκ, while Athens and the digital ABP have no negative there. In the hyrax clause (6), ADLXX and the ABP read οὐκ, while Athens again has the affirmative. All three negate the divided-hoof clause in both verses. The RPB ADLXX reading therefore retains both negatives for each animal. The difference in the cud clause belongs to the Greek text. [ABP Leviticus 11](https://biblehub.com/interlinear/apostolic/leviticus/11.htm)
- **Leviticus 11:14, 17, 19.** ADLXX word 6 in 11:14 is the kite, ἴκτινον, previously assigned the lemma for fish. In 11:17 the diving bird at word 4 and the ibis at word 6 had acquired the glosses “a spout” and “the ivy.” Athens has the contextual bird senses and the digital ABP identifies a cormorant and an ibis. Keep the broader “diving bird” in ADLXX. The ADLXX corrections also restore the article before the kite, the list formula for similar kinds, and the conjunction at 11:19 word 9. [ABP Leviticus 11](https://biblehub.com/interlinear/apostolic/leviticus/11.htm)
- **Leviticus 11:40.** ADLXX and the digital ABP require both the eater and the carrier to wash their garments, and add bathing in water only for the carrier. Athens prints the bathing clause in parentheses in both halves. The extra clause for the eater is a difference in the printed Greek. Preserve the distinction in the ADLXX reading. [ABP Leviticus 11](https://biblehub.com/interlinear/apostolic/leviticus/11.htm)
- **Leviticus 12:5.** In both interlinears the two numbers at positions 16 and 19 are sixty and six. The digital ABP likewise preserves both. The RPB draft had dropped the second number and read sixty days. Restore sixty-six for the second period, following the initial twice seven days. [ABP Leviticus 12](https://biblehub.com/interlinear/apostolic/leviticus/12.htm)

- **Leviticus 15:12, word 8.** ADLXX γονορρυής and Athens γονοῤῥυής match the normalized ABP form at word 8. The digital ABP describes a person having a seminal emission. Athens gives “man with a discharge.” ADLXX formerly gave “running with gonorrhea.” Adopt “one with a discharge” in ADLXX and retain the Athens gloss. Both describe the person without introducing a disease diagnosis. Twelve further ADLXX positions were corrected from their Greek contexts. Only 15:12 word 8 is counted here as a direct comparison for this term. [ABP Leviticus 15](https://biblehub.com/interlinear/apostolic/leviticus/15.htm)

- **Follow-up on γονορρυής.** Individually checked eleven occurrences in Leviticus 15 and one each in Numbers 5:2 and 2 Samuel 3:29 against the single-word ABP entries, in both local editions. ABP describes a seminal emission in Leviticus and uses a disease label in Numbers and Samuel. The local gloss describes the person consistently across all three passages. The direct word decisions record all 26 edition positions, including the two previously checked at Leviticus 15:12.

### The two senses of ὅτι

At Nehemiah 9:10 the same conjunction occurs twice in succession around a verb of knowing. The first introduces a reason. The second introduces what God knew. The edition ledgers record the second occurrence at word 26. At Leviticus 24:22 the divine self-identification gives the reason for one judgment for sojourner and native. Both editions and ABP have ὅτι at word 9, and “for” expresses that relationship.

Local references sometimes differ even when the words match. ADLXX Hosea 2:10 and Athens Hosea 2:8 both correspond to ABP Hosea 2:8. At Job 19:2 the Athens verse ends before the clause containing ὅτι in ADLXX and ABP. At Job 27:12 Athens has a different construction. Only ADLXX enters the direct word check for those two Job passages. The decision ledger, one TSV per book and kept privately because it quotes ABP's single-word glosses, gives the edition, both references and both word positions for each verified comparison.

### Leviticus 25 and the year of release

In Leviticus 25:28 both ADLXX and Athens read ἕκτου ἔτους, “sixth year.” The digital ABP reads ἔτους without the ordinal. Its word 23, ἔτους, corresponds to “year.” Its word 25, ἀφέσεως, corresponds to ADLXX word 25 and Athens word 26, “of release.” Keep “sixth” in the local readings and exclude the ordinal from the matched-word comparison. [ABP Leviticus 25](https://biblehub.com/interlinear/apostolic/leviticus/25.htm)

### Comparing the values of Greek numerals

Run `python3 scripts/adlxx/abp_cardinals.py` after generating the position alignments. It reads each current release database and rechecks the corresponding single-word entry on the cached digital ABP page. The two compressed cardinal reports in `build/abp-gloss-review/` record both positions, both glosses, the Greek value and the result. Accents and breathings distinguish forms such as ἕξ (“six”) and ἐξ (“from”). The check covers the Greek spellings in the script's table. English glosses outside its number vocabulary remain available for individual review.

The first run after correcting ADLXX Numbers 2:31 found 2,437 ADLXX and 2,434 Athens positions where both English glosses express the Greek value. A further 188 ADLXX and 181 Athens positions need interpretation of the English wording. The one explicit value disagreement was Athens Numbers 1:35, where the local διακόσιοι means two hundred and the digital ABP says five hundred. The corresponding ADLXX passage is Numbers 1:33 and was verified separately. These automated results overlap the individually checked positions in the decision ledger.

On follow-up, 1 Kings 19:19 required “twelve” for δώδεκα in both editions. The plural article refers back to the twelve teams. At Exodus 39:1 the local εἴκοσι now contributes “twenty.” The preceding two tokens supply “nine and,” and the full amount remains twenty-nine talents. Both corrections are recorded at their exact positions in the decision ledger.

Recognizing English phrases such as “of seventy” and “six measures” brings explicit agreements to 2,619 ADLXX and 2,606 Athens positions. Of the fifteen remaining wording flags, twelve express the expected value in context, including the two elements of “bi-fold” in 1 Kings 6:34. Three have no usable English numeral at the aligned position on the digital page: both editions at 2 Kings 18:2 and Athens at Exodus 28:26. Their local Greek values are twenty and two respectively. The separate explicit disagreement at Athens Numbers 1:35 remains.

### The water clause in Numbers 31:23

Athens and ADLXX both have ἁγνισμοῦ in the expression for water of purification, corresponding to ABP word 17. At the end of the verse the two editions give different instructions. Athens prints a parenthesized οὐ at word 26 before διελεύσεται, “will pass.” ADLXX and the digital ABP both give the affirmative verb there. The parentheses matter when citing Athens. Each edition keeps its own wording. [ABP Numbers 31](https://biblehub.com/interlinear/apostolic/numbers/31.htm)

At Numbers 35:4 both local editions specify two thousand cubits, δισχιλίους. The digital ABP specifies a thousand, χίλιοι. The discrepancy is already present in the Greek and falls outside the matching-word count. [ABP Numbers 35](https://biblehub.com/interlinear/apostolic/numbers/35.htm)

### The hill country in Joshua 17:16

The sons of Joseph speak of the hill country. ADLXX word 4, ἀρέσκει, means “pleases” and matches digital ABP word 7. Athens word 7, ἀρκέσει, means “will suffice.” The negative in each clause makes the distinction audible in English. The hill country does not please them in ADLXX. It will not suffice for them in Athens. Each interlinear retains the sense of its own verb. [ABP Joshua 17](https://biblehub.com/interlinear/apostolic/joshua/17.htm)

### Ruth and 1 Samuel

In Ruth 4:10, Athens and ADLXX both have φυλῆς at word 37, referring to the dead man’s clan. Digital ABP has πύλης at the same position, referring to the gate. In Ruth 4:7 the editions do share ἀγχιστείαν at word 11. Both local glosses, “right of redemption,” fit the kinsman’s role in the transaction. Only the shared word enters the direct comparison ledger. [ABP Ruth 4](https://biblehub.com/interlinear/apostolic/ruth/4.htm)

Two numerical differences also arise in the Greek. In 1 Samuel 4:18 both local editions give Eli twenty years as judge (word 36), while digital ABP gives forty (word 37). In 1 Samuel 9:22 the local accounts put the invited company at about seventy (ADLXX word 26, Athens word 25), while digital ABP gives about thirty (word 25). The local English keeps the numbers in the respective Greek texts. [ABP 1 Samuel 4](https://biblehub.com/interlinear/apostolic/1_samuel/4.htm) and [ABP 1 Samuel 9](https://biblehub.com/interlinear/apostolic/1_samuel/9.htm)

### The ewe lamb in Nathan’s parable

At 2 Samuel 12:6, word 3 is ἀμνάδα, “ewe lamb,” in all three texts. The amount of restitution changes at word 5. Athens has τετραπλάσιον, “fourfold,” in agreement with digital ABP. ADLXX has ἑπταπλασίονα, “sevenfold.” Both local glosses preserve David’s judgement as printed in their own edition. [ABP 2 Samuel 12](https://biblehub.com/interlinear/apostolic/2_samuel/12.htm)

### Ahab’s summons and the following year’s campaign

The demand for Ahab’s silver, gold, wives, and children is at Athens 1 Kings 20:5 and ADLXX 1 Kings 21:5. The same verb δώσεις falls at Athens word 35, ADLXX word 31, and digital ABP 1 Kings 20:5 word 32. In the corresponding verse 22 the prophet tells the king to consider what he will do. The future ποιήσεις is inside that indirect question. Both chapters were aligned by wording before their glosses were compared. [ABP 1 Kings 20](https://biblehub.com/interlinear/apostolic/1_kings/20.htm)

### Joab’s appointment and the Hebronite count

In 1 Chronicles 11:6, ἐγένετο takes Joab as its subject. He went up first and became commander. In 22:7 the same form introduces what was in David’s heart to do. Both editions now distinguish those uses from the narrative opening “it came to pass” found, for example, in 2 Samuel 13:23. [ABP 1 Chronicles 11](https://biblehub.com/interlinear/apostolic/1_chronicles/11.htm) and [ABP 1 Chronicles 22](https://biblehub.com/interlinear/apostolic/1_chronicles/22.htm)

At 1 Chronicles 26:32, word 8 is “seven hundred” in both editions and digital ABP. The preceding numeral differs. At word 7 Athens reads χίλιοι, giving 1,700 men, while ADLXX and ABP read δισχίλιοι, giving 2,700. The two local totals stand. [ABP 1 Chronicles 26](https://biblehub.com/interlinear/apostolic/1_chronicles/26.htm)

Run `python3 scripts/adlxx/verify_abp_decisions.py` after rebuilding either interlinear. It rechecks the surface form and preferred gloss at every recorded local position and checks that the cited digital ABP position still has a single matching Greek word with the recorded English. The ledger gives the editorial reason for each decision.

### Aligning Ezra, Nehemiah, and Job

At Ezra 4:19 both local editions have εὕραμεν, “we found,” at word 9. Digital ABP word 9 is εὑρέθη, “it was found.” At Nehemiah 5:15 both local editions call the payment forty didrachmas (the denomination is word 23), while digital ABP calls it forty shekels (word 22). Each local text keeps its own reading. [ABP Ezra 4](https://biblehub.com/interlinear/apostolic/ezra/4.htm) and [ABP Nehemiah 5](https://biblehub.com/interlinear/apostolic/nehemiah/5.htm)

In Job, chapter boundaries can shift even between the two local editions. The trembling of the heart begins at Athens 36:34, ADLXX 37:1, and digital ABP 37:1. The Lord’s reply begins at Athens 39:31, ADLXX 40:1, and digital ABP 40:1. Align these clauses before comparing words. In Job 5:21 Athens repeats its assurance about fear in a second clause. Only its first φοβηθήσῃ has a matching digital ABP position in that verse. [ABP Job 37](https://biblehub.com/interlinear/apostolic/job/37.htm), [ABP Job 40](https://biblehub.com/interlinear/apostolic/job/40.htm), and [ABP Job 5](https://biblehub.com/interlinear/apostolic/job/5.htm)

### Psalm headings and repeated lines

The opening petition of Psalm 50 is word 1 at local 50:3 and digital ABP 51:1. The petition for a clean heart is local 50:12 and digital ABP 51:10. At local 50:19 ADLXX has the third-person verb ἐξουδενώσει, matching ABP 51:17, while Athens has second-person ἐξουδενώσῃ and addresses God directly. The preceding negative is present in both. [ABP Psalm 51](https://biblehub.com/interlinear/apostolic/psalms/51.htm)

The same future ἐξελεύσῃ occurs in the complaint of local Psalm 43:10 and the prayer of local Psalm 59:12. Both local editions print the first as a statement and the second as a question. Their English word order follows that distinction. Digital ABP numbers the lines 44:9 and 60:10. [ABP Psalm 44](https://biblehub.com/interlinear/apostolic/psalms/44.htm) and [ABP Psalm 60](https://biblehub.com/interlinear/apostolic/psalms/60.htm)

For Psalm 151, look up the individual references. Both local databases contain Psalm 151:1–7. ADLXX stores those verses on the publisher’s Psalm 150 page, so a query for source chapter 151 alone misses all seven. For example, select rows with `ref LIKE 'PSA 151:%'`. The BibleHub digital ABP endpoint for Psalm 151 returned HTTP 404 when checked. All seven local verses therefore remain outside the verified ABP comparison.

### God’s choice in Numbers 16:5

The final clause in ADLXX says that those whom God chose for himself he brought near to himself. Athens prints two negatives in parentheses, (οὐκ) before “chose” and (οὐ) before “brought near.” Digital ABP includes both negatives in its Greek and groups each with its verb in English. The affirmative ADLXX reading stands. At the earlier occurrence in the same verse, “brought near” has a direct single-word counterpart (local word 24, ABP word 21). Only that occurrence of the verb enters the matched-word ledger. [ABP Numbers 16](https://biblehub.com/interlinear/apostolic/numbers/16.htm)

### The agent in Proverbs 22:19

The subject of γνωρίσῃ at word 9 is the Lord who makes the way known. The next word, σοι, names the person to whom he makes it known. Athens and ADLXX both now parse the verb as third-person singular. They differ at the end of the clause: ADLXX has σου, “your” way, and Athens has αὐτοῦ, “his” way. Digital ABP agrees with Athens on the possessive and groups it with the noun. [ABP Proverbs 22](https://biblehub.com/interlinear/apostolic/proverbs/22.htm)

In Proverbs 13:19 both local editions qualify the desires with εὐσεβῶν, “of the godly.” Digital ABP has ἀσεβῶν, “of the impious.” The opposing English senses come from different Greek words. The noun for desires and the verb for sweetening the soul were checked as direct matches. [ABP Proverbs 13](https://biblehub.com/interlinear/apostolic/proverbs/13.htm)

### The censers and Aaron’s rod

ADLXX Numbers 17:2 and 17:4 correspond to Athens and digital ABP 16:37 and 16:39. In both places the perfect passive participle refers to the men who were burned. The bronze censers were recovered and reused. The account of the rod in ADLXX 17:23 corresponds to Athens and digital ABP 17:8. Both interlinears give the broader “nuts” for κάρυα. [ABP Numbers 16](https://biblehub.com/interlinear/apostolic/numbers/16.htm) and [ABP Numbers 17](https://biblehub.com/interlinear/apostolic/numbers/17.htm)

### Isaiah and Numbers 18

The Isaiah review recorded eight matching Greek words in each edition. Fourteen of the sixteen edition-specific checks led to gloss corrections. In Isaiah 22:23 the throne image refers to Eliakim, so ἔσται reads “he shall be.” In 10:17 the fire consumes wood, which supports “will devour.” [ABP Isaiah 22](https://biblehub.com/interlinear/apostolic/isaiah/22.htm) and [ABP Isaiah 10](https://biblehub.com/interlinear/apostolic/isaiah/10.htm)

Numbers 18:21 is a Greek-text difference. At word 6 the AD publisher and the ADLXX database read δώδεκα (“twelve”). Athens and digital ABP read δέδωκα (“I have given”). The RPB reading provisionally supplies “[I have given]” in light of verse 24. The AD interlinear preserves “twelve.” Independent AD print confirmation remains open. [AD Numbers 18](https://apostoliki-diakonia.gr/bible/arithmoi/?file=4.18) and [ABP Numbers 18](https://biblehub.com/interlinear/apostolic/numbers/18.htm)

### Who calls, and who becomes

In ADLXX Hosea 2:18, corresponding to Athens and ABP 2:16, the wife is the subject of both occurrences of καλέσει. Both interlinears now say “she will call.” In Hosea 7:8 the repeated name Ephraim is the subject of ἐγένετο. The image is of Ephraim becoming an unturned cake. In 8:8 the corresponding image for Israel is a useless vessel. [ABP Hosea 2](https://biblehub.com/interlinear/apostolic/hosea/2.htm), [Hosea 7](https://biblehub.com/interlinear/apostolic/hosea/7.htm) and [Hosea 8](https://biblehub.com/interlinear/apostolic/hosea/8.htm)

In Jonah 1:14 both interlinears retain “we perish.” The first-person plural refers to the sailors, who ask the Lord to spare them. In Micah 7:10 both now read “she shall be,” continuing the reference to the speaker’s enemy. [ABP Jonah 1](https://biblehub.com/interlinear/apostolic/jonah/1.htm) and [Micah 7](https://biblehub.com/interlinear/apostolic/micah/7.htm)

### The serpent and the well

In Numbers 21:6, 8–9 the same Greek words support “deadly,” “standard,” “bronze” and the promise that the bitten person who looks will live. AD first identifies the serpent as bronze in verse 9. Digital ABP already has χαλκοῦν in the command in verse 8. In 21:17 digital ABP groups the verb of singing with Israel, its subject. Direct Greek review restored that syntax in both databases. The grouped comparison is excluded from the single-word ledger. [ABP Numbers 21](https://biblehub.com/interlinear/apostolic/numbers/21.htm)

### Fruit, cattle and righteousness

In Leviticus 26:4 the trees “shall yield” their fruit. At 1 Kingdoms 15:3 and 22:19, μόσχου denotes a calf in each list of animals. In Isaiah 1:21 “righteousness” once lodged in the city now given over to murderers. The direct checks cover each occurrence in both databases. At Psalm 10:2 (ABP 11:2), both editions retain “moonless darkness” for σκοτομήνῃ, where digital ABP has “moonlight.” [ABP Leviticus 26](https://biblehub.com/interlinear/apostolic/leviticus/26.htm), [1 Samuel 15](https://biblehub.com/interlinear/apostolic/1_samuel/15.htm), [1 Samuel 22](https://biblehub.com/interlinear/apostolic/1_samuel/22.htm), [Isaiah 1](https://biblehub.com/interlinear/apostolic/isaiah/1.htm) and [Psalm 11](https://biblehub.com/interlinear/apostolic/psalms/11.htm)

### Skin, hide and cedarwood

In Leviticus 13 the priest examines a person’s skin through verse 34. Thirteen occurrences in each interlinear now read “skin” where they previously read “hide.” The referent changes later in the chapter. In verses 49 and 56 the priest examines a leather article, and both interlinears retain “hide.” In the rites of Leviticus 14:4, 6, 49 and 51 the priest takes wood from a cedar. In the property laws of Exodus 22:1 and 10 “a sheep” leaves the animal’s age open. [ABP Leviticus 13](https://biblehub.com/interlinear/apostolic/leviticus/13.htm), [Leviticus 14](https://biblehub.com/interlinear/apostolic/leviticus/14.htm) and [Exodus 22](https://biblehub.com/interlinear/apostolic/exodus/22.htm)

### Balaam and the angel in the road

In Numbers 22:4, Moab says Israel will “lick up” its neighbours as a calf licks up the green growth. Both editions now repeat that verb. They use different forms in the second half of the simile, where digital ABP agrees with AD. In verse 20 Balaam is told to do what God says. In verse 22 the angel rises “to oppose” him. AD has διαβαλεῖν where Athens and ABP have ἐνδιαβάλλειν. Only the Athens word qualifies for the direct ABP ledger there. The ass sees the drawn sword in verse 23, and Balaam sees it in verse 31 after God uncovers his eyes. [ABP Numbers 22](https://biblehub.com/interlinear/apostolic/numbers/22.htm)

### Keeping a command and keeping a feast

In Deuteronomy 16 the object determines the sense of ποιήσεις. At verses 1, 10 and 13 Israel shall keep a feast. In verse 8 the prohibition concerns doing work, and in verse 12 Israel is to keep the commandments. At Numbers 23:26 Balaam promises to do what God says. [ABP Deuteronomy 16](https://biblehub.com/interlinear/apostolic/deuteronomy/16.htm) and [Numbers 23](https://biblehub.com/interlinear/apostolic/numbers/23.htm)

### Who is called lord, husband or wife

At Genesis 45:8 and 45:9 Joseph calls himself master over Pharaoh’s household and over Egypt. Both databases previously gave κύριον the divine title at both occurrences. The existing RPB reading already gave the office to Joseph. At 2 Kingdoms 14:16 the widow speaks of the man threatening her son and their inheritance. Calling him her husband introduced a relationship absent from her account. Leviticus 13:29 and 13:38 likewise describe any man or woman with the stated symptoms. [ABP Genesis 45](https://biblehub.com/interlinear/apostolic/genesis/45.htm), [2 Samuel 14](https://biblehub.com/interlinear/apostolic/2_samuel/14.htm) and [Leviticus 13](https://biblehub.com/interlinear/apostolic/leviticus/13.htm)

### Balaam’s first and second oracles

At Numbers 23:8 ADLXX formerly rendered the actions in Balaam’s two questions as plucking and uprooting. Both ask how he could curse a people whom God does not curse. Digital ABP agrees with the AD form in the first question and the Athens form in the second. At 23:19 the second passive infinitive means “to be threatened.” The first, διαρτηθῆναι, remains an open question in the reading copy. Digital ABP gives “to waver,” while NETS takes the passive to describe being imposed upon. [ABP Numbers 23](https://biblehub.com/interlinear/apostolic/numbers/23.htm) and [NETS Numbers](https://ccat.sas.upenn.edu/nets/edition/04-num-nets.pdf)

### Honor and price

In Isaiah 10:16 the Lord sends dishonor upon Assyria’s honor. The pairing of τιμή and ἀτιμία had disappeared when the first noun was glossed “price.” The same issue affected Isaiah 11:10, 14:18 and 35:2, Job 34:19 and Proverbs 12:9. In Isaiah 55:1 both interlinears retain “price” in the invitation to buy without payment. In Isaiah 24:2 the active and middle participles distinguish the lender from the borrower. The digital ABP English reverses their order. [ABP Isaiah 10](https://biblehub.com/interlinear/apostolic/isaiah/10.htm), [Isaiah 24](https://biblehub.com/interlinear/apostolic/isaiah/24.htm) and [Isaiah 55](https://biblehub.com/interlinear/apostolic/isaiah/55.htm)

### A star and a man

Numbers 24:7 introduces a man who will have dominion over many nations. At 24:17 the paired images are a star rising from Jacob and a man arising from Israel. All three interlinears have ἄνθρωπος in both verses. The seer’s μακαρίζω at 24:17 is active and first person. At 24:20 ἀρχή gives Amalek’s place among the nations, while at 1 Chronicles 29:12 it names a dominion over which the Lord rules. [ABP Numbers 24](https://biblehub.com/interlinear/apostolic/numbers/24.htm) and [1 Chronicles 29](https://biblehub.com/interlinear/apostolic/1_chronicles/29.htm)

### Jephthah’s vow and the initiation at Phogor

Judges 11:39 places the daughter’s return at the end of two months. In Athens, τέλος had been glossed “levy.” In both editions the following relative clause says that Jephthah fulfilled the vow he had vowed. At Numbers 25:3 the AD singular means that Israel was initiated into the worship of Beelphegor, as verse 5 confirms. Digital ABP groups the verb with Israel, and Athens uses the plural form. This correction stands outside the direct single-word total. The interpretation of εἶπον in Numbers 25:12 is still open. [ABP Judges 11](https://biblehub.com/interlinear/apostolic/judges/11.htm), [Numbers 25](https://biblehub.com/interlinear/apostolic/numbers/25.htm) and [NETS Numbers](https://ccat.sas.upenn.edu/nets/edition/04-num-nets.pdf)

### The Numbers 26 census

The twelve tribal counts in the AD publisher’s text total 580,630. Verse 51 states 601,730, a difference of 21,100. The separate Levite count in verse 62 is expressly excluded from the tribal census. All twelve subtotal verses and verse 51 agree between the AD website and the local Greek. The RPB reading preserves each figure. AD, Athens and digital ABP agree on the total *stated* in verse 51. Their tribal lists require alignment by tribe before comparing individual subtotals. [AD Numbers 26](https://apostoliki-diakonia.gr/bible/arithmoi/?file=4.26) and [ABP Numbers 26](https://biblehub.com/interlinear/apostolic/numbers/26.htm)

### Earlier kings, obedience and listening

In 1 Kings 16:25, 30 and 33, ἔμπροσθεν puts Omri and Ahab in relation to the kings who ruled before them. Elijah running ahead of Ahab in 18:46 uses the same word spatially. The temporal sense also occurs in the comparisons with Hoshea, Hezekiah and Josiah at 2 Kings 17:2, 18:5 and 23:25. [ABP 1 Kings 16](https://biblehub.com/interlinear/apostolic/1_kings/16.htm) and [2 Kings 23](https://biblehub.com/interlinear/apostolic/2_kings/23.htm)

At Deuteronomy 21:18 the son refuses to obey his parents even after discipline. In 26:14 the speaker affirms that he obeyed the Lord’s instruction about the tithe. Both databases now express obedience in those passages. Proverbs 17:4 retains “listens to” for attending to lawless speech. [ABP Deuteronomy 21](https://biblehub.com/interlinear/apostolic/deuteronomy/21.htm), [Deuteronomy 26](https://biblehub.com/interlinear/apostolic/deuteronomy/26.htm) and [Proverbs 17](https://biblehub.com/interlinear/apostolic/proverbs/17.htm)

### The daughters’ inheritance and Joshua’s commission

At Numbers 27:9 the AD publisher’s text gives the inheritance to the deceased man’s *father’s brother* if he leaves no daughter. AD 27:10 names the same heir if the man leaves no brothers. Athens and digital ABP name the man’s *own brother* in verse 9 and his father’s brother in verse 10. The RPB reading follows the AD wording at both verses. In 27:16 Moses asks the Lord to appoint a man over the congregation, so that it will have a shepherd. Ezekiel 34:11 uses a related verb when the Lord promises to seek out his scattered sheep and look after them. Both interlinears previously suggested he would call them to account. [AD Numbers 27](https://apostoliki-diakonia.gr/bible/arithmoi/?file=4.27), [ABP Numbers 27](https://biblehub.com/interlinear/apostolic/numbers/27.htm) and [Ezekiel 34](https://biblehub.com/interlinear/apostolic/ezekiel/34.htm)

In Deuteronomy 31:7 Joshua will *allot* the land to the people, and in Numbers 34:18 the tribal chiefs are selected to allot it to them. At Numbers 35:8 the tribes themselves take possession before they give cities to the Levites. The recipient and the object determine which English verb fits. [ABP Deuteronomy 31](https://biblehub.com/interlinear/apostolic/deuteronomy/31.htm), [Numbers 34](https://biblehub.com/interlinear/apostolic/numbers/34.htm) and [Numbers 35](https://biblehub.com/interlinear/apostolic/numbers/35.htm)

### The offerings in Numbers 28

At 28:13 θυσία names the flour and oil accompanying each lamb. Both interlinears now give “a grain offering” at that occurrence. AD 28:4 names the morning and evening lambs with the same verb, now “you shall offer” in both places. At 28:7 the drink offering is strong drink, and the new-moon prescription in 28:14 specifies wine. [ABP Numbers 28](https://biblehub.com/interlinear/apostolic/numbers/28.htm)

### The seven days and the eighth

Numbers 29:13–34 prescribes thirteen calves on the first day, then twelve, eleven, ten, nine, eight and seven. The rams and lambs stay at two and fourteen on each of those seven days. Verse 36 gives the eighth day a separate count of one calf, one ram and seven lambs. Throughout the calendar πλήν introduces offerings made *besides* the regular ones. The earlier gloss “except” risked making the special offerings replace the daily offering. The same additive construction occurs at 28:23 and 28:31. [ABP Numbers 28](https://biblehub.com/interlinear/apostolic/numbers/28.htm) and [Numbers 29](https://biblehub.com/interlinear/apostolic/numbers/29.htm)

### A vow laid upon oneself

In Numbers 30 κατά with the genitive τῆς ψυχῆς identifies the person upon whom a binding obligation rests. The accusative after the same preposition in 30:7 identifies the terms of the utterance. Both databases now distinguish those constructions. At AD and Athens 30:14, corresponding to digital ABP 30:13, the husband can confirm the vow *for her* or annul it. At AD and Athens 30:16, corresponding to ABP 30:15, the masculine possessive assigns the sin of late annulment to the husband. The ledger gives both references and the individual word positions. [ABP Numbers 30](https://biblehub.com/interlinear/apostolic/numbers/30.htm)

In Ezekiel 34:10 the Lord demands the flock back from the shepherds’ hands. In 34:11–12 he seeks out the scattered sheep. Rendering the same verb ἐκζητήσω according to its object and surrounding clause preserves the shift from the shepherds’ accountability to the flock’s rescue. [ABP Ezekiel 34](https://biblehub.com/interlinear/apostolic/ezekiel/34.htm)

In Numbers 31:41 τέλος names the levy Moses delivers to Eleazar. Both interlinears now read “levy” where they previously read “end.” In Numbers 35:20 and 35:22 the contrast turns on the thrower’s intent. Both interlinears now use “object” for σκεῦος in these clauses, preserving the law’s scope.

In Deuteronomy 17:8 the repeated ἀντιλογία names a dispute referred to the court. The same word names a matter for priestly judgment in 21:5 and a dispute between parties in 25:1. Both editions now read “dispute” at all four positions. In 21:14 πράσει names the sale of a captive woman that the law forbids. Both editions now give the noun its own gloss, “by sale.”

In Deuteronomy 27:25 the gifts are bribes paid to shed innocent blood. In 28:48 the iron restraint fastened to the neck is a collar. In 31:29 the dative noun contributes “in lawlessness” beside its cognate verb. Both editions now reflect those details. Two differences with ABP warrant retaining the local glosses. The Lord will not let Joshua go (31:8), and the people had trusted in their gods (32:37).

In Joshua 12:2 Athens names the Arnon gorge. Its interlinear had treated Ἀρνῶν as a plural common noun and glossed it “lambs.” The corrected entry follows the river name already used in 12:1. AD has “in the gorge” at 12:2 and supplies no corresponding river-name token.

In Judges 1:14 the woman is urged to petition her father. Both editions now identify her as the object of the urging. In Judges 14:17 Samson tells the answer to his wife, who then tells her people. Both editions now gloss the dative pronoun “to her” and retain “she” for the subject of the next clause.

In 2 Kingdoms 13:26 (2SA 13:26), David asks Absalom why Amnon should accompany him. Both editions now gloss πορευθῇ as “should he go.” In 17:19 the local editions have ἀραφώθ while ABP has a different Greek word at that point in the account of the covered well. That difference supplies no direct English check for the local word.

In Numbers 35:12 εἰς κρίσιν describes the hearing before the congregation. Both editions now read “judgment” for κρίσιν. In 4 Kingdoms 4:27 (2KI 4:27), Elisha tells Gehazi to leave the grieving woman alone as Gehazi moves to push her away. Both editions now gloss ἄφες as “let be.”

In 2 Chronicles 8:11 the dative αὐτῇ identifies Pharaoh’s daughter as the person for whom Solomon built the house. Both editions now read “for her.” At 24:19 both retain “he warned” because διεμαρτύρατο is singular even though the preceding clause mentions prophets.

In Deuteronomy 1:28 the scouts “turned away” the people’s heart. The verb describes their discouraging Israel from going up. At 1:30 the Lord joins Israel in fighting its enemies. In 1:27 AD has an imperfect verb for murmuring and Athens an aorist. Only Athens has the exact form printed in the digital ABP at that position.

In Job 13:15 the mighty one is the subject of “he has begun” in both local editions, despite other differences in the verse. In 31:39 Job asks whether he caused the landowner grief. The active verb has a sufferer distinct from Job.

At Deuteronomy 2:7 the people lacked nothing during the wilderness journey. ADLXX now glosses ῥήματος as “anything,” as Athens already did. In 2:5 both retain “a step” for βῆμα. The footstep expresses how much of Esau’s land Israel could claim.

In Deuteronomy 3:28 Moses is to strengthen Joshua and encourage him as he prepares to lead Israel across the Jordan. Both editions now gloss παρακάλεσον as “encourage.” In Psalm 131:6 (ABP 132:6), both retain “it” for the two feminine pronouns. The ark named in verse 8 supplies a natural referent.

In Proverbs 5:19 the wife of verse 18 remains the subject of the three imperatives. Both interlinears now identify her in the glosses and render the deer as a hind. At ἡγείσθω σου the local reading is “let her lead you.” ABP takes the verb in the sense of being esteemed. The difference concerns the interpretation of the same wording.

In Deuteronomy 4:34 both editions now gloss ὁράμασι as “sights.” Israel saw the acts in Egypt, and the verse closes by recalling its eyewitnesses. In Jeremiah 11:21 the men of Anathoth threaten Jeremiah directly. Both interlinears now give “you will die” for ἀποθάνῃ. The grammatical note records the tension between this address and the printed accent.

Deuteronomy 5:14 gives the servants rest on the Sabbath. Both editions and ABP share the verb for resting. AD also repeats the beast of burden in the purpose clause, a detail preserved in its reading copy. In 5:33 both editions retain “may give rest” because the pronoun following the verb identifies the person who receives it.

In Hosea’s marriage allegory the wife remains the person who receives gifts and is compared to dry land. Both releases now consistently identify her in the checked clauses at Athens 2:3, 8, 10, 13 and 14, corresponding to AD 2:5, 10, 12, 15 and 16. In Deuteronomy 6:16 the Greek name for Testing repeats the verb for putting God to the test, as in Exodus 17:7.

At Deuteronomy 7:21 τρωθήσῃ is a future passive of wounding. Both editions now distinguish the promise “thou shalt not be wounded” from the instruction against fear in verse 18. In Micah 1:11 the feminine participle identifies the inhabitant addressed in the lament. Both editions now give “she will receive” for λήψεται.

Deuteronomy 8:4 describes feet growing calloused, and 8:9 describes mining copper from the hills. In both editions the dative αὐτῇ in 4 Kingdoms 4:27 refers to the grieving Shunammite woman. In Jeremiah 15:8 αὐτήν refers back to the mother upon whom terror falls.

At Isaiah 11:10 both interlinears previously gave “against | it” for ἐπ᾽ αὐτῷ. The nations place their hope in the one who rises to rule them, so the corrected pair reads “in | him.” In Zephaniah 3:9 the peoples call on the Lord and serve him. In Judges 11:11 the people appoint Jephthah, and in 2 Kingdoms 23:9 the pronoun refers to the preceding warrior in the list.

In Isaiah 31:1 the people seek help from Egypt and trust in horses and chariots. In Jeremiah 7:14 they trust in the temple. Both interlinears now preserve those relationships. At Athens Jeremiah 26:25 (ABP 46:25) the last preposition identifies Pharaoh as the object of his followers’ trust. The earlier prepositions in that verse introduce objects of judgment.

Deuteronomy 11:10 compares irrigation in Egypt to watering a vegetable garden. Both editions now gloss λαχανείας as “vegetables.” The next verse changes the subject to the land itself, which drinks rain from heaven. Verse 15 describes fodder for the livestock.

Deuteronomy 12:15 and 12:21 use θύσεις for slaughtering animals for a meal in one's own city. Both interlinears already distinguish this act from bringing offerings to the chosen place. At 12:23 the repeated ψυχή is “life” both times. At 12:27 the blood is poured at the base of the altar.

At 12:6 ADLXX lists both ἑκούσια and ὁμολογίας. Its interlinear formerly glossed both as “freewill offerings.” It now reads “freewill offerings” and “offerings of acknowledgment.” ABP distinguishes voluntary gifts from offerings of acknowledgment, and the RPB reading preserves that distinction. Athens omits the latter term at 12:6. Both editions have it at 12:17 and now read “offerings of acknowledgment” there. ABP groups the noun with its possessive at both references, so these observations are recorded separately from direct single-word decisions.

In 1 Kingdoms 8:3 (1 Samuel), Samuel's sons accept δῶρα and pervert judgments. Both interlinears now read “bribes.” At 3 Kingdoms 5:13–14 (1 Kings), Athens calls Solomon's requisition of men a “levy.” The count is in men, and they go to Lebanon in shifts. Both editions retain “forced labor” for the office Adoniram held at 12:18 and “tributes” among the sources of royal revenue at 10:15.

In ADLXX Deuteronomy 13:17 (Athens and ABP 13:16), πανδημεί identifies who takes part. Both interlinears now give “with all the people.” In ADLXX 13:10 (Athens and ABP 13:9), the command opens with a participle that emphasizes the following verb, “thou shalt surely report.” The AD interlinear formerly parsed its single-lambda spelling ἀναγγέλων as “of messengers.” The source spelling is preserved, and the analysis now identifies a participle of ἀναγγέλλω. The spelling difference excludes that participle from the direct single-word ledger.

At Nehemiah 5:4 the people borrow silver to pay the king's taxes. At 5:11 Nehemiah orders the creditors to give back property. Their answer at 5:12 begins ἀποδώσομεν, “we will give back.” Both interlinears formerly had “shall we give back,” which made the promise sound like a question. The following promises and oath confirm the declarative reading.

At Ezra 7:24 the local Greek uses φόρος in the notification about temple personnel. ABP's Greek enumerates three charges there. That difference belongs to the Greek texts. It supplies no basis for inserting three charges into either local interlinear.

Deuteronomy 14:13 lists the kite among the birds. The AD interlinear formerly attached ἴκτινον to ἰχθύς and glossed it “fish.” The corrected lemma is ἰκτῖνος, “kite.” Athens and ABP have the alternate accusative ἰκτῖνα. Only the Athens occurrence qualifies for the matching-form ledger. In 14:25 both interlinears correctly describe selling the tithe and carrying the proceeds to the chosen place.

Deuteronomy 15:2–3 repeats ἀπαιτήσεις, the creditor's act of exacting payment. The negative in verse 2 protects the brother, while verse 3 allows collection from the foreigner. Both interlinears preserve that change. At 15:18 the Greek wage comparison is explicitly yearly in both editions and ABP.

Deuteronomy 16:19 directs judges to refuse bribes. AD uses a singular in the prohibition and a plural in the explanation. Athens uses plurals in both. At 16:20 the AD interlinear had read “you may divide.” The verb is διώκω, “pursue,” with what is just as its object. Both editions now read “shall pursue.” The RPB reading preserves the repeated root in “Justly shalt thou pursue what is just.”

At Deuteronomy 17:6 the repeated noun marks the difference between two or three witnesses and a single witness. At 17:15 the designation ἄρχοντα recurs for the ruler to be appointed. Both interlinears preserve those repetitions. The end of 17:3 requires separate textual review. AD reads προσέξατέ σοι. Athens and ABP have προσέταξα, “I commanded.” The AD reading copy provisionally follows its second-person plural verb. The final singular dative remains unresolved.

Deuteronomy 18:15 and 18:18 repeat the promise to raise up a prophet. Moses speaks in verse 15, and the Lord addresses Moses in verse 18. In 18:19 the Lord exacts punishment from the hearer who refuses the prophet's words. Both interlinears now give “will exact punishment” for ἐκδικήσω. At 18:22 AD has ἐφέξεσθε αὐτοῦ, whereas Athens and ABP have ἀφέξεσθε ἀπ᾽ αὐτοῦ. The closing AD clause is provisional and was excluded from the matching-word decisions.

Daniel 5:3 uses a plural passive for the temple vessels. Both local interlinears retain “were brought,” leaving the bearers unnamed as the Greek does. In 7:14 the figure like a son of man receives dominion, and in 7:27 the holy ones receive the kingdom. Both local editions preserve the direction of giving in each passage. At 10:11 the messenger tells Daniel “I was sent.” Suggested changes at Hosea 2:16 (AD 2:18) and Micah 1:11 and 7:10 were already present in the rebuilt corpora and are counted only once.

In Deuteronomy 19:12 the γερουσία acts for the fugitive's city. Both interlinears now identify the “council of elders.” At 19:17 ἀντιλογία is the dispute between the two men who appear before the judges. The previous gloss “contradiction” left the nature of the hearing unclear.

At Deuteronomy 20:12 Athens and ABP read περικαθιεῖς, “thou shalt besiege.” The AD text has περικαθαριεῖς, which its interlinear renders “you will purify.” The RPB reading provisionally gives “thou shalt cleanse it” and flags the difficult wording for textual review. The Athens verb is a direct ABP match. The AD verb is recorded separately.

In Deuteronomy 21:15–17 a father's preference for one wife does not transfer the firstborn son's inheritance. Both interlinears preserve the double portion and identify its recipient. The clause identifying the hated wife's son as firstborn falls in AD and ABP 21:15 but in Athens 21:16. The ledger records the two references for that match.

Deuteronomy 22:25 and 22:28 use the same participle, βιασάμενος, for the man's use of force. At 22:25 μόνον restricts the penalty to the man, and 22:26 explicitly clears the young woman. Both interlinears preserve these distinctions. The fine in 22:19 is reckoned in shekels, while the payment in 22:29 is reckoned in didrachms.

In the Balaam account, AD Deuteronomy 23:6 corresponds to Athens and ABP 23:5. Both local interlinears now give “loved” for ἠγάπησε, the reason for the Lord's past reversal of the curses. AD says that the curses became “a blessing”; Athens and ABP have the plural noun. The RPB reading follows AD's singular.

Deuteronomy 24:11–15 distinguishes a debtor's pledge from a worker's wages. The debtor brings his pledge outside. If he is poor, the creditor returns his garment at sunset so he can sleep in it. At 24:13 both interlinears now describe the return as “an act of mercy” (ἐλεημοσύνη). At 24:14 μισθόν names the wages owed for work. The next verse requires payment that same day.

Deuteronomy 25:1 has a small Greek difference with an audible effect in English. AD reads τὸ δίκαιον, “what is right,” whereas Athens reads τὸν δίκαιον, “the righteous man.” At 25:15 the same adjective describes a commercial weight and a measure. Both interlinears now read “just” in both places, preserving the repetition in “a true and just weight” and “a true and just measure.”

Deuteronomy 26:12 distinguishes the third year from the second tithe, which goes to the Levite, the sojourner, the fatherless, and the widow. At 26:17–18 the subject changes: Israel chooses God, then the Lord chooses Israel. Only the second verb is a single-word ABP alignment; the first is grouped with its object in ABP.

Deuteronomy 27:15–26 has thirteen occurrences of γένοιτο in each edition, distributed differently. Athens repeats the word consecutively at 27:16, where AD and ABP use it once. At 27:23 AD and ABP include both the mother-in-law and the wife's sister, each followed by “Be it so.” Athens has only the first declaration and response at that reference. The difference belongs to the Greek texts.

Deuteronomy 28:34 reads παράκλητος in AD, provisionally “an advocate.” How the word fits the surrounding curses remains unresolved. Athens and ABP read παράπληκτος, “deranged.” At 28:44 AD twice says that Israel will not lend to the sojourner. Athens says it once. Both readings reverse the direction of lending in verse 12.

At Deuteronomy 31:12 the command to assemble the hearers of the law includes the προσήλυτος living in Israel's cities. AD formerly gave “proselyte.” Both interlinears now read “sojourner,” preserving the residential qualification without implying a rite of conversion.

At Deuteronomy 32:43 AD and ABP place the angels of God in the call to worship and the sons of God in the following summons. Athens has sons first and angels second. The worship verb matches across all three. The ledger records the two noun matches for AD only. Preserve the order of each Greek witness in its English rendering.

At Deuteronomy 34:7 AD prints χελώνια. LSJ cites the verse under χελώνιον and proposes the muscles of the back. The revised AD gloss is “back muscles.” Athens prints χελύνια and gives “jaws.” That form also occurs in ABP, whose English “his lips” covers the noun and possessive together. LSJ attests both jaw and lip for χελύνιον. The comparison therefore supplies no single-word ABP decision here. [LSJ entries for χελώνιον and χελύνιον in the Perseus transcription](https://github.com/PerseusDL/lexica/blob/master/CTS_XML_TEI/perseus/pdllex/grc/lsj/grc.lsj.perseus-eng25.xml)

At Esther 3:9 (ESG 3:9), Haman offers silver for the king's treasury. The word γαζοφυλάκιον at AD position 12 and Athens position 14 matches ABP position 12. Both databases now give “treasury.” The fiscal context distinguishes this use from a chamber used for storage.

The singular εὐλογίας recurs in the name Valley of Blessing at 2 Chronicles 20:26 and in “rain of blessing” at Ezekiel 34:26. Both passages have direct ABP word evidence. At Sirach 37:24 the wise man is filled with blessing, and at 40:27 the fear of the Lord is like a garden of blessing. The two Sirach decisions rest on the Greek construction alone.

The temple rooms require a different English decision from Esther's royal treasury. In Nehemiah 13:5 the room once held offerings, vessels, and tithes. In 13:7 Tobiah has been given that room, and in 13:8 his possessions are thrown out of it. “Chamber,” “storeroom,” and “treasury” all fit this sequence. ABP uses a treasury gloss throughout. The direct-word ledger also records 2 Kings 23:11, Ezra 10:6, and Nehemiah 12:44, 13:4, and 13:9.

At Nehemiah 10:37 both local editions have singular γαζοφυλάκιον and ABP has plural γαζοφυλάκια. At 10:38 both local editions have the plural and ABP has the singular. The opening clauses confirm the verse correspondence. Each English rendering preserves the number of its own Greek source.

At Job 30:29 both editions gave “of sparrows” for στρουθῶν. ABP identifies ostriches at the same word, position 6. Job calls himself their companion in his lament. Both interlinears now give “of ostriches.”

Each of the 39 books mapped by the ABP comparison script now has at least one directly verified word in each local edition. The final five books to receive a first entry were Obadiah 1:15, Nahum 1:7, Habakkuk 2:4, Haggai 1:6, and Malachi 3:10. Book representation measures the reach of the spot-check. The ledger identifies the exact words reviewed.

In Job, a dash at interrogative μή sometimes concealed the question. Both interlinears now mark the questions at 1:9, 8:3, 8:11, 26:5, and 34:33. The question about a book or a scribe occurs at AD and ABP 37:20 and Athens 37:19. Each of these has direct one-word ABP evidence for the opening particle. At 4:2 the local texts ask a question that begins differently in ABP. At 11:7 Athens has μή where AD has ἦ. The corrections at 4:2 in both editions and 11:7 in Athens rest on their Greek. At 22:12 μή and οὐχί work together, and ABP groups their English.

At Isaiah 35:4 the dash under μή had left “be strong” followed by “be afraid” in AD. Both editions now supply “do not” at μή. At 2 Samuel 14:2 the same correction restores Joab's instruction to refrain from anointing. At 2 Chronicles 25:16 and Song 3:3 the speaker asks a question. The local gloss “have” supplies its English opening. ABP uses “Have” in the first passage and expresses the negative question explicitly in the second. By contrast, Job 5:6 has οὐ γὰρ μή. Its opening οὐ carries the negative, and ABP's auxiliary “can” at μή cannot by itself establish a question.

Tobiah's taunt is at AD Nehemiah 3:35 and Athens 4:3. Both ask whether the builders sacrifice and whether a fox will climb the wall. At ABP 4:3 the first clause differs in Greek. The second has a direct match for οὐχί, ABP word 15 and local word 20. Both local question markers are restored. Only the fox question enters the direct-word ledger. At Ecclesiastes 6:6 μή introduces the question and οὐκ supplies its negative. ABP groups the two. The local glosses now preserve “do” and “not” separately.

At 2 Chronicles 32:11–12 the Assyrian speaker expects his hearers to agree with two accusations against Hezekiah. Both local texts now carry the opening negative in each question. At 4 Maccabees 7:22 the writer likewise expects assent when he asks whether a believer would not master the passions through piety. The local verb already supplied “would master.” Both interlinears now give “not” for οὐκ, on Greek evidence alone. At Tobit 6:8 the preceding “no longer” already carries the negative of the whole expression.

At Tobit 10:7 the relative οἵας refers back to the road. The next clause opens with ἡμέρας, “by day,” when the mother ate no bread, followed by her lament by night. At Judith 15:11 τὴν ἡμίονον αὐτῆς now gives the article, mule, and possessive at their own positions. Both corrections rest on the local Greek. A check for parallel errors found the noun gloss repeated under its article at 2 Samuel 13:29 (“mule”) and Numbers 25:8 (“Israelite”). ABP groups the mule with its possessive and the Israelite with the preceding phrase. The corrected articles in both editions are Greek-context decisions.

At Ezekiel 45:12 both editions gave “shekel” twice for τὰ στάθμια. The local Greek has the plural “the weights.” ABP has singular τὸ στάθμιον, “the weight.” The shekels are named separately later in the verse. At 2 Kings 18:18 Athens has an article before “son” which AD and ABP omit. At 1 Esdras 8:57 ἅγια describes the vessels as holy in both local editions. AD repeats the article before the adjective. These are Greek-context corrections.

At Leviticus 8:32 and Judges 6:21 both interlinears had assigned “meat” and the lemma κρέας to the preceding article τῶν as well as the noun. ABP gives the article its own English at word 4 and word 17 respectively. Both corrected articles now give “of the.” At 1 Maccabees 6:6 ἐν πρώτοις is “at first.” The ordinal had also been copied into the preposition's English.

AD Joel 3:1–5 corresponds to ABP Joel 2:28–32, and AD Joel 4:1–21 corresponds to ABP Joel 3:1–21. Athens follows the three-chapter numbering here. The screen checks the Greek sequence at each corresponding reference. This restores the comparison of the sun, moon, and stars at AD Joel 4:15. Psalm 151 accounts for every remaining position classified as a source page unavailable.

Joel 2:10 and AD Joel 4:15 (Athens and ABP 3:15) distinguish two actions. The sun and moon grow dark, and the stars lower their brightness. Both editions now give “will lower” for δύσουσι in both passages. ABP aligns the verb independently but groups the brightness with its possessive. The ledger includes the verb and excludes that grouped phrase.

The outpouring passage is AD Joel 3:1–5 and Athens and ABP Joel 2:28–32. Both editions preserve the repeated verb “I will pour out” and ἀπό, “from.” ABP assigns “my spirit” to a two-word group. That phrase supplies no separate ABP decision for πνεύματος. In the list of signs both interlinears now give “fire” for πῦρ alongside blood and vapor of smoke.

At the end of the passage οὓς Κύριος προσκέκληται has the Lord as subject and the relative pronoun as object. Both local glosses retain “has summoned,” even though ABP gives the verb a passive English rendering. Earlier in the same verse σωθήσεται is passive and promises deliverance to the person who calls upon the Lord. These decisions concern the OT source passage.

At Isaiah 11:2 the two local texts read πνεῦμα τοῦ Θεοῦ, “Spirit of God.” ABP has πνεῦμα Κυρίου, “Spirit of the Lord.” The first πνεῦμα matches directly. The divine title differs in Greek. The local “of the council” for βουλῆς did require correction. In the list of gifts it means “of counsel,” paired with strength.

At Isaiah 11:4 both interlinears now give “by the word” for τῷ λόγῳ. The mouth speaks the word, and the next clause names the breath passing through the lips. Athens also says that he judges “in righteousness” and reproves “in uprightness.” AD omits both phrases. The ledger records matching words at their respective positions.

For βουλή the king follows advice at 1 Kings 12:13–14, and David seeks to frustrate Ahithophel’s advice at 2 Samuel 15:31, 34. Both editions now use “counsel” there. In Isaiah 29:15 the same noun occurs twice for a plan made in secret. Both editions give “plan” at each position. At Numbers 16:2 the context names leaders summoned to a body, so both retain “of the council.” The assembly sense also fits the gathered people at Psalms 1:5, 110:1, and 88:8. The latter two align to ABP 111:1 and 89:7.

A review of λόγος glossed “thing” recovered several kinds of speech. The earth is summoned to hear the Lord’s *word* at Jeremiah 22:29, and at Proverbs 26:6 the fool carries a *message*. At Exodus 33:17 the Lord agrees to grant Moses’ *request*. In each case the reference to speech governs the English choice. “Things” remains appropriate for what Israel saw with its own eyes at Deuteronomy 4:9. At 2 Kings 20:13 “a thing” refers to the possessions Hezekiah showed his visitors.

At Isaiah 11:6 AD had assigned “the wolf” to ἐρίφω. The wolf grazes with the lamb in the first clause. In the next clause the leopard rests with a young goat. AD now gives the correct lemma ἔριφος and the contextual dative reading. Athens already had “young goat.” At 11:13 “jealousy” now identifies Ephraim’s rivalry with Judah in both editions. At 11:14 both retain “ships” for πλοίοις despite the anomalous English “boast” in the digital ABP comparison.

The follow-up to Isaiah 11:6 found a genuine difference in number at Ezekiel 43:22. AD and Athens have ἐρίφους, “young goats,” while ABP has ἔριφον, “a young goat.” Each local edition keeps its plural. At Isaiah 65:25 wolves and lambs graze together in all three texts. At local Jeremiah 28:40 the young goats match ABP 51:40 directly.

At Isaiah 53:4 the speakers recount how they regarded the sufferer. In that description ὑπὸ Θεοῦ identifies agency, “by God.” At 53:5 AD has the perfect passive μεμαλάκισται, “has been weakened,” while Athens has the aorist ἐμαλακίσθη, “was made weak.” ABP matches the AD form. At 53:7 the sheep is led to slaughter and the lamb is silent before the shearer. At 53:8 both local texts give “humiliation” for ταπεινώσει. The subject of the following passive verb is his judgment. The comparison concerns the OT text.

At Isaiah 53:10 AD and ABP address plural hearers with δῶτε. Athens has the third-person singular δῶται. At 53:11 δίκαιον is the object of δικαιῶσαι, and εὖ is the adverb modifying service. At 53:12 the sufferer is counted among lawless people. Both editions have ἁμαρτίας when he bears the sins of many. In the closing clause AD repeats the accusative plural ἁμαρτίας, “sins.” Athens and ABP have ἀνομίας, “lawless deeds.” AD's former “sin offering” depended on a genitive singular analysis incompatible with τὰς. The closing AD noun is a Greek-context correction.

At 1 Samuel 15:23 Samuel calls divination a sin. Both editions had glossed ἁμαρτία as a sin offering. At Hosea 8:11 Ephraim is the subject who multiplies altars. AD and ABP have εἰς ἁμαρτίας, “for sins,” while Athens has the singular εἰς ἁμαρτίαν, “for sin.” ABP groups Ephraim with the verb. In the sacrificial directions “sin offering” often fits the same noun. Athens Leviticus 6:25 uses an accusative plural after the verb of slaughter. AD 6:18 and ABP 6:25 use a construction with the genitive singular for sin. The identical spelling ἁμαρτίας alone cannot establish agreement in number.

The name Ephraim is indeclinable. In Hosea 6:4 and 11:8 the speaker addresses Ephraim directly. In 9:3 and 11:5 Ephraim dwells in Egypt. In 9:8 the name qualifies the watchman, so “of Ephraim” remains appropriate. In AD Hosea 14:9 (Athens and ABP 14:8) the dative article marks a change of topic, rendered “as for Ephraim.” At 9:3 and 11:5 ABP groups the name with “dwelt,” and the ledger excludes those four local decisions from the single-word total.

AD Hosea 2:1–2 aligns with ABP 1:10–11, and AD 2:3–25 with ABP 2:1–23. AD 12:1 and 14:1 close ABP chapters 11 and 13 respectively. The rest of those two AD chapters runs one verse ahead of ABP. Athens uses the ABP numbering at these breaks. The direct-reference check still requires agreement in the Greek sequence.

At AD Hosea 2:3 both local editions address a single brother, while ABP 2:1 has brothers. At AD 2:23 heaven answers the earth. AD uses a pronoun for heaven in the second clause, while Athens and ABP 2:21 repeat the noun. At AD 14:5 (Athens 14:4) the speaker promises to turn his anger away “from him.” ABP ends with a plural pronoun. The local singular is a Greek-context correction.

At Hosea 13:4 both local editions include a creation clause between the divine self-identification and the recollection of Egypt. ABP proceeds directly to Egypt. Within the local clause οὗ αἱ χεῖρες means “whose hands,” and those hands created the host of heaven. The possessive and the genitive phrase were checked from the local Greek. The shared wording resumes with ἐγὼ ἀνήγαγόν σε, “I brought you up.” The final participle names the “one who saves.” The ledger identifies the individually aligned words on either side of the longer local reading.

Hosea 6:10 opens in both local editions with the house of Israel. ABP places that phrase at the end of 6:9. Its 6:10 starts with εἶδον, “I saw.” The form can also mean “they saw,” but the prophetic speaker reports his own observation. Both interlinears now give the first-person reading. Athens continues with the command to harvest within 6:10, whereas AD and ABP place it in 6:11. The next healing clause starts at AD 6:11 word 13 and Athens and ABP 7:1 word 1. In all three, τὸν Ἰσραήλ identifies Israel as the object of healing. ABP groups the infinitive and its first-person subject but translates Israel separately.

In Hosea 4:4 the second μήτε gives “nor” in both editions. Athens places the comparison with a priest at the start of 4:5, where AD and ABP close 4:4 with it. At 5:2 the four Athens words identifying the speaker as the hearers’ disciplinarian correspond to two grouped ABP glosses. At 7:7 AD and ABP have a plural verb, “they devoured,” with the judges as its object. Athens has a singular verb and names fire as its subject. At 8:9 both local texts say Ephraim flourished by himself and then use the plural “they loved.” ABP uses the singular in that last clause.

In the Joseph narrative, εἶδον and ἴδον can express either “I saw” or “they saw.” Both officials dream in Genesis 40:5, but the baker speaks for himself at 40:16. Pharaoh describes his own experience in 41:19 and 41:22. At 44:28 Judah quotes his father saying he has not seen his missing son since. The AD parsing at 41:19 and the Athens readings at 41:22 and 44:28 now identify the first-person speaker. ABP groups the negative and verb at 41:19 and 44:28. Its ungrouped verb at 41:22 matches the AD spelling.

In Ezekiel 11:1 the prophet sees two leaders among the men at the gate. In 37:8 he sees sinews and flesh on the bones. Both AD verbs now specify “I saw.” Athens 8:10 has an additional seeing verb before the idols. It also takes the prophet as subject. At 16:50 the speaker has just said that he removed them and continues “as I saw.” Digital ABP gives a second-person English gloss for εἶδον. That Greek form admits first singular or third plural. In 20:28 the people who entered the land supply a genuine plural subject.

At Ezekiel 37:8 AD's ἐφύοντο describes sinews and flesh growing on the bones. The lemma is φύω. Athens has the compound ἀνεφύοντο, “were springing up.” The completed bodies have no breath. At 37:9 the prophet calls from the four winds and is told to breathe into the dead. At 37:10 ἔζησαν marks their coming to life. At 37:14 God promises to place the people on their land. The sense of πνεῦμα in each clause follows its role in the vision.

In Ezekiel 37:22, εἰς δύο βασιλείας means “into two kingdoms.” Both interlinears had taken βασιλείας as singular. At 37:23 AD’s ῥύσομαι promises rescue from lawlessness. Athens already carried the rescue sense. At 37:24 ποιήσουσιν refers back to the ordinances. Both interlinears now say that the people will do them. These three corrections concern English sense or parsing where the Greek words match ABP.

A corpus search for ποιέω glossed with “give” found four further occurrences of ποιήσουσιν in each edition. Its objects and complements determine the English. At Ezekiel 16:41 the enemies execute acts of vengeance. At 23:29 they deal with the addressee in hatred. At 43:11 the people do what the commands prescribe. At 43:25 the priests offer the sacrificial animals. In 1 Kings 3:28 both editions retain “to give” because ποιεῖν δικαίωμα describes Solomon giving a judgment.

The future ῥύσομαι promises rescue. In Isaiah 38:6 the Lord rescues the addressee and the city from the king of Assyria. AD had “I will wash.” In Hosea 13:14 AD’s “I will be loosed” reversed the speaker’s role. The Lord actively rescues from Hades, then promises redemption from death with λυτρώσομαι. Isaiah 49:25 likewise promises rescue for the children. At Exodus 6:6 AD’s English “I will deliver” already fits, but its lemma required correction from λύω to ῥύομαι. Psalm 90:14 aligns with ABP Psalm 91:14. At Jeremiah 15:21 Athens reads ῥύσομαι before “from the hand of the wicked,” where ABP reads σώσω. In the final clause, before “from the hand of the pestilent,” Athens, AD and ABP all read λυτρώσομαι.

In both editions, “I will redeem” fits all six occurrences of λυτρώσομαι checked against ABP’s ransom gloss. These occur at Exodus 6:6 and 13:15, Hosea 13:14, Zechariah 10:8, Isaiah 44:22 and Jeremiah 15:21.

At 2 Kings 10:27 AD and ABP both have λυτρῶνα, accusative singular, for the use to which Baal’s site was put. AD now reads “a bathhouse” following ABP. LSJ supports the bathing-place sense under the spelling λουτρών. Its entry does not cite this verse. Athens has the plural λυτρῶνας, glossed “latrines,” so the singular ABP token supplies no exact-form decision for Athens. [LSJ, λουτρών](https://logeion.uchicago.edu/λουτρών)

At 1 Samuel 23:1 the Philistines plunder the threshing floors at Keilah. In AD, τοὺς ἅλω has a masculine plural article. The English gloss now gives the plural “threshing floors,” as does ABP for the same Greek form. Athens has τοὺς ἅλωνας. Its English was already plural, and its parsing now records masculine gender. At Ruth 3:2 the barley and the act of winnowing establish the agricultural sense. At Genesis 50:10–11 the threshing floor of Atad serves as a named landmark.

The noun ληνός takes its sense from what the vessel holds or what people do there. In Genesis 30:38 and 30:41 the flock comes to drink, so both editions retain “troughs.” At Judges 6:11 Gideon uses a winepress to thresh grain. Joel 2:24 names both wine and oil, which favors the broader “vats.” The full press in AD Joel 4:13 aligns with Athens and ABP Joel 3:13. The ABP entries at Deuteronomy 16:13, Proverbs 3:10 and ABP Jeremiah 48:33 group the noun with its possessor and were excluded from this direct-word count.

The direct comparisons for ἔλαιον in Genesis, Leviticus and Numbers support “oil,” including the oil Jacob pours on his pillar and the oil mixed with flour in Numbers 7. A separate search turned up preferred glosses consisting only of “of.” Both editions now restore the missing nouns in Judith 10:5 (“of wine,” “of oil”), Tobit 6:15 (“of mother”), Judith 7:7 and 1 Maccabees 15:13 (“of men”). These corrections follow the Greek clauses in the two editions. The ABP dataset used here omits those books, so none of the corrections count as ABP decisions.

At Genesis 24:12, 14, 44 and 49, both interlinears retain “kindness” for ἔλεος where ABP uses “mercy.” Abraham’s servant first asks God to show kindness to his master and later asks the family to deal kindly with him. In AD Deuteronomy 13:18, corresponding to Athens and ABP 13:17, both interlinears now give singular “mercy” for the direct object of δώσῃ. The following verb ἐλεήσῃ repeats the idea in verbal form.

Psalm 135 in both editions corresponds verse for verse to ABP Psalm 136. All 26 refrains end with the same Greek sequence after normalization. The digital ABP groups ἔλεος and αὐτοῦ in each refrain, so the comparison confirms “his mercy” at phrase level without adding single-word decisions for either token. At 135:1 AD now opens with “give thanks,” the sense of ἐξομολογεῖσθε in the repeated summons at verses 1–3 and 26. Athens already has that reading. In verse 26, τοῦ οὐρανοῦ identifies the God to whom the thanksgiving is addressed as the God of heaven.

All thirteen occurrences of ἐξομολογεῖσθε in each Psalter were checked against the corresponding ABP words. At AD Psalms 104:1 and 105:1 the opening now reads as a command, “give thanks.” Psalms 106:1 and 117:1 use the same gloss. At 117:1 and 117:29 the repeated wording frames the psalm. The pairing of thanksgiving with song in 29:5 corresponds to ABP 30:4, a difference in both chapter and verse numbering. This ruling applies to these summonses to worship.

Psalm 150:1–5 addresses worshippers with αἰνεῖτε twice in each verse. Both editions give “praise” in all ten positions. At 150:6 the subject changes to πᾶσα πνοή, “every breath,” and the third-person singular αἰνεσάτω gives “let it praise.” At 150:4 the local “a dance” and ABP’s reference to the company of dancers both fit the musical setting of χορῷ. At 150:5 both occurrences of κυμβάλοις were aligned in order within their respective clauses.

At Psalm 149:1 AD’s capitalized ΑΣΑΤΕ addresses the worshippers directly. The verb is the plural imperative of ᾄδω, “sing,” and its object is a new song. AD previously read “let them not be silent.” The openings of Psalms 95 and 97 use the same capitalized form. Their AD dictionary entries now also point to ᾄδω. The distinction in Psalm 149 matters because verses 2 and 3 do use third-person commands, inviting the sons of Zion to exult and praise.

Psalm 148:5 gives God the active verbs “spoke” and “commanded.” The creatures “came into being” and “were created.” Both editions preserve the subjects and voice. At 148:6 the negative οὐ precedes the verb for passing away, so the decree endures. At 148:8 the hail, snow, ice and storm wind belong to the same list. The neuter plural τὰ ποιοῦντα gathers the elements together as agents that carry out God’s word. Both interlinears use “wind” for πνεῦμα here.

Local Psalm 146:1–11 corresponds to ABP 147:1–11, and local Psalm 147:1–9 continues at ABP 147:12–20. At local 147:1 Jerusalem is addressed directly, followed by a parallel command to Zion. AD now reads “praise” for the opening imperative. At local 147:7 God sends his word, the ice melts, his wind blows and the waters flow. The last verb is a form of ῥέω, with the neuter plural “waters” taking a singular verb. AD previously gave “will loosen.” Athens already identified the verb and glossed it “will flow.”

In local Psalm 145:1 (ABP 146:1) the psalmist addresses his own soul with the singular imperative “praise.” AD’s capitalized ΑΙΝΕΙ previously read “praises.” Verse 2 shifts to the psalmist’s first-person vow and verse 3 warns against trusting rulers for salvation. At verse 8 both local editions and ABP read σοφοῖ τυφλούς. Both interlinears preserve the particular action expressed by σοφόω, “makes wise.”

At Psalm 144:1 AD now reads “I will exalt,” in parallel with “I will bless.” At 144:5 the psalmist speaks of the majesty of divine glory, and AD now glosses δόξης as “glory.” The line about the Lord’s faithfulness has three reference conventions. AD places it in 144:13α, Athens opens 144:14 with it, and ABP places it at the end of 145:13. All fourteen Greek words align after normalization.

At local Psalm 143:12 (ABP 144:12), ὧν, “whose,” links the sons to the foreigners in verse 11. Athens and ABP also have an explicit “their” after “sons.” AD goes directly to the comparison with young plants. AD and ABP describe the plants as firmly established, while Athens uses a different participle for growing strong. The third-person possessives continue through the flocks and cattle in verses 13–14. In verse 15 the psalmist reports whom “they called blessed” before pronouncing blessed the people whose God is the Lord.

At Psalm 142:7 (ABP 143:7) the subject of ἐξέλιπε is “my spirit.” AD now reads “has failed.” The psalmist is alive and urgently seeking an answer. Athens reads the imperfect ἐξέλειπε, “was failing.” At Genesis 49:33, Jacob himself is the subject of ἐξέλιπε and is then gathered to his people. Both interlinears retain “breathed his last” there. At Psalm 142:2 the passive δικαιωθήσεται gives “will be justified” in both editions even though digital ABP renders the verb actively.

Local Psalm 141:1 is the heading. Local 141:2–8 aligns with ABP 142:1–7. In 141:2 AD previously parsed the initial ΦΩΝῌ as nominative. It is an instrumental dative in both halves of the verse, giving “with my voice” alongside the possessive μου. ABP groups those two words each time. The correction is recorded here as a phrase-level check. In 141:4 the speaker’s own spirit is failing, and in 141:8 release from prison allows him to give thanks.

In Psalm 140:5 (ABP 141:5), ἐλέει describes the mercy with which a righteous person corrects the speaker. Both instances of με are direct objects, first of “will discipline” and then of “will rebuke.” The next clause has a different subject, ἔλαιον, “oil.” Both interlinears now gloss λιπανάτω as “let it anoint.” The preceding μή negates the command, giving the sense “let a sinner’s oil not anoint my head.” ABP has the same Greek verb and the anointing sense.

The prayer in local Psalm 139:2–14 aligns with ABP 140:1–13. In 139:2 and 58:2 the capitalized ΕΞΕΛΟΥ addresses God. Both AD entries now identify the aorist middle imperative of ἐξαιρέω. At 139:2 “deliver” already fit. At 58:2 (ABP 59:1), “I release” reversed the roles. The speaker asks to be delivered from his enemies. At local 139:13 the parallel nouns κρίσιν and δίκην refer to the judgment and cause of the poor and needy.

At local Psalm 138:16 (ABP 139:16), the subject of εἶδον follows the verb: οἱ ὀφθαλμοί σου, “your eyes.” AD previously assigned the seeing to the speaker. It now reads “they saw” and parses the verb as third-person plural. Athens reads εἶδοσαν, a distinct third-person plural form, with the same subject. At 138:8 both editions give “you are present” for πάρει in the clause about descending to Hades.

At Psalm 137:1 (ABP 138:1), AD now repeats the thanksgiving verb of verse 2 with the same sense and parsing, “I will give thanks.” AD and ABP include a reason for the song: God heard the speaker’s words. The AD gloss for ἤκουσας now reads as a statement. Athens ends verse 1 after the promise to sing and starts verse 2 with the promise to bow toward the temple. At verse 5 AD now gives the plural command “let them sing,” continuing the invitation to the kings in verse 4. At verse 7 the second-person form ζήσεις addresses God directly in both local texts, even where the digital ABP gloss uses the third person.

At Psalm 136:4 (ABP 137:4), πῶς introduces the exiles’ question. AD and ABP use the deliberative subjunctive ᾄσωμεν, “should we sing.” Athens uses the future indicative ᾄσομεν, “shall we sing.” In both local editions ἐπί governs the genitive phrase for “on foreign soil.” Verse 5 moves from “we” to the individual speaker’s vow. At verse 8 ἀνταπέδωκας addresses Babylon in the second person. Both interlinears preserve “you repaid,” while the digital ABP English uses the third person for the same form.

At Psalm 134:1 (ABP 135:1) the same command occurs twice. AD now renders both occurrences “praise.” Verse 3 introduces a separate verb for singing praise. All six capitalized ΑΙΝΕΙΤΕ openings in AD now point to αἰνέω in the lexical index. At 134:17 πνεῦμα is the breath absent from the idols’ mouths, and at 134:18 γένοιντο expresses a wish concerning the people who make and trust those idols.

At local Psalm 132:2–3 (ABP 133:2–3), the participle for “descending” occurs twice with the ointment and then in a feminine form with the dew. Both interlinears preserve the repetition. In 132:1 AD writes ἐπὶ τὸ αὐτό as three tokens, while Athens and the digital ABP present “together” as one token. At local 133:1–2 the servants are told collectively to bless the Lord. In verse 3 the Lord is the subject of the optative εὐλογήσαι and σε is singular. The blessing is addressed to one person.

At local Psalm 131:7 (ABP 132:7), AD prints προσκυνήσομεν, “we will worship.” Its parsing now gives future indicative. Athens and ABP print προσκυνήσωμεν with omega. Athens renders the invitation “let us bow down.” Only Athens supplies an exact-form decision against ABP for this verb. In 131:2 David swears to the Lord. In 131:11 the Lord swears to David and promises to place one of his descendants on his throne.

In Psalm 129, both local editions give “atonement” for ἱλασμός at 129:4. The grounds for waiting differ. AD 129:5 has “for the sake of your name,” matching the wording at the end of ABP 130:4. Athens 129:4 has “for the sake of your law.” The first-person verb “I waited” begins Athens 129:5. Both local editions repeat the morning-watch phrase, which appears once in digital ABP. The call for Israel to hope falls at AD 129:6, Athens 129:7 and ABP 130:7. Local 130:3 (ABP 131:3) repeats that summons. The name/law difference is in the Greek texts.

Local Psalm 127:4 (ABP 128:4) describes the blessing in the future passive. At 127:5–6 the speaker wishes that the Lord may bless the addressee and that the addressee may see Jerusalem’s prosperity and his grandchildren. In local 128:6–8 (ABP 129:6–8), the rooftop grass withers before harvest. The passersby’s greeting is quoted after “they did not say,” so the harvest blessing is withheld. Both editions retain the first-person plural perfect in the quoted words εὐλογήκαμεν ὑμᾶς, “we have blessed you.”

At local Psalm 125:4 (ABP 126:4), Athens supplies the singular article ὁ before the word for a torrent. Its singular “torrent” preserves that reading. AD and ABP have no article there, and both give a plural English gloss. At local 126:2 the Lord gives sleep to his beloved. In 126:3 both interlinears take “sons” as the subject of the statement about the Lord’s inheritance. Digital ABP renders the same form as a direct address.

At local Psalm 123:4 (ABP 124:4), AD and ABP have ἄν with the aorist indicative. The water “would have drowned us” had the Lord not been on Israel’s side. AD’s earlier parsing referred to a subjunctive verb absent from this verse. Athens omits the particle at this position but preserves the conditional English from the preceding clauses. In 123:7 the singular “was delivered” refers to the soul compared with a sparrow, and the plural “were delivered” refers to the speakers. At 124:2 the repeated κύκλῳ connects the mountains around Jerusalem with the Lord around his people.

In local Psalm 121:1 (ABP 122:1), εὐφράνθην recalls the speaker’s joy at hearing the invitation. Both editions now give “I rejoiced.” The AD parsing records the aorist passive form. Digital ABP uses future English for the same Greek verb. At local 122:2 (ABP 123:2), AD accents οἰκτειρῆσαι as an infinitive. The word gloss now gives “to have compassion on,” followed by “us.” Athens accents οἰκτειρήσαι as an optative and gives “he may pity.” The alignment test removes accents, so its match here confirms the Greek letters only. Both readings express the worshippers’ dependence on God for mercy.

At local Psalm 119:2 (ABP 120:2), AD now gives “deliver” for the middle imperative ῥῦσαι. The speaker asks the Lord to deliver his soul from deceitful speech. At local 120:3 (ABP 121:3), AD previously gave “may stumble” for νυστάξῃ. The first clause concerns the traveller’s foot, but the subject of the second clause is the guardian, and the verb means “may slumber.” The following verse repeats the verb alongside “sleep.” Athens reads the future νυστάξει in verse 3 and already has the slumber sense.

A scan across all 176 verses of local Psalm 118 (ABP 119) covered the nouns indexed as νόμος, ἐντολή, μαρτύριον, δικαίωμα and κρίμα. At 118:132 the petitioner asks for mercy in keeping with God’s customary treatment of those who love his name. Both editions now give “custom” for κρίμα here. At 118:160 “judgments” remains appropriate for the enduring divine decisions. The scan found 12 directly comparable noun positions in each edition. ABP groups another 123 AD and 122 Athens positions with adjacent words. Two Athens positions lacked a secure alignment in this scan.

Both outstanding Athens noun positions in the Psalm 118 scan have been identified. At 118:27 word 4, Athens places “teach me your ordinances” at the start of the verse. AD 118:26 and ABP 119:26 end with the same five Greek words. ABP groups “your ordinances.” At Athens 118:151 word 8, “commandments” reflects ἐντολαί. AD 118:151 and ABP 119:151 read ὁδοί, “ways.” This is a Greek wording difference. Neither noun position qualifies as a direct single-word match. In 118:5 the particle ὄφελον and the optative express a wish that the speaker’s ways might be directed.

In Psalm 118:24 AD now gives “are” for ἐστι because its subject, “your testimonies,” is plural in English. The Greek verb remains singular. At 118:28 AD and ABP both read ἐνύσταξεν. The speaker’s soul grew drowsy from despondency. Athens reads ἔσταξεν, “dripped,” from στάζω. At 118:13 both local interlinears preserve the aorist “I declared” for ἐξήγγειλα. Digital ABP gives future English there, though it renders the same form in the past at 119:26.

At Psalm 118:33 αὐτήν refers to the singular “way” of the ordinances. Both local editions give “it,” while digital ABP uses a plural pronoun in English. At 118:62 AD now gives “I would rise” for the speaker’s action at midnight and “to give thanks” for its purpose. AD and ABP share the present infinitive ἐξομολογεῖσθαι. Athens uses the aorist infinitive ἐξομολογήσασθαι with the same thanksgiving sense. The AD rising verb also differs in spelling from ABP and was checked from its local clause.

### Psalm 118:65–96 (ABP Psalm 119:65–96)

Verified 125 ADLXX and 109 Athens word decisions. At 118:87 the persecutors nearly destroyed the speaker, then ἐγὼ δὲ οὐκ changes the subject to “but I did not.” ADLXX word 11, ἐγκατέλιπον, can be first singular or third plural in isolation. Corrected “they abandoned” to “I abandoned” and recorded first singular. Athens word 10 already has the first person with its imperfect ἐγκατέλειπον. ADLXX splits παρὰ βραχύ across words 1–2 where Athens writes Παραβραχύ (“almost”). Those two ADLXX positions remain outside the single-word decisions because their force comes from the phrase.

### Psalm 118:97–176 (ABP Psalm 119:97–176)

Verified 295 ADLXX and 281 Athens decisions. At 118:126 word 6 both editions read διεσκέδασαν with “your law” as its object. Promoted “they have made void” in Athens and adopted the same gloss in ADLXX. The prior “they have scattered” obscured the force of the verb with an abstract object.

At 118:166 word 1 ADLXX προσεδόκων is imperfect. Changed “I expect” to “I was awaiting.” Athens already expresses the imperfect in its differently spelled προσεδόκουν. At 118:125 word 8 both editions retain “I will know” for γνώσομαι. The speaker asks for understanding so that he himself will know the testimonies. ABP’s causative English would change who gains that knowledge.

### Recurring English wording across 37 books

A rule-based pass resolved the lexical comparison at 2,829 additional single-word positions (1,428 ADLXX and 1,401 Athens). At 2,753 positions the local analysis identifies a Greek future indicative, and the English tokens agree except for “shall” and “will.” For example, both render δώσω at 1 Chronicles 16:18 word 3 with the verb “give.” These decisions cover the lexical verb only. A literary translation still has to decide how the passage expresses a prediction, promise, or obligation.

The other 76 positions have equivalent prepositions such as “toward” and “towards,” or use “answered” and “responded” for ἀποκρίνομαι. Each decision records both verse and token positions under “retain lexical sense.” The full ledger verifier checked the current local Greek and preferred English, the normalized ABP Greek, the ABP English, and the single-word status for every entry.

### English articles and subject pronouns across 39 books

A rule-based comparison verified 17,888 additional single-word matches. At 12,042 noun positions both English readings use the same noun with the same capitalization, and one includes an article. At 5,846 indicative verb positions both use the same English verb form, and one expresses a subject pronoun consistent with the local Greek person and number. For example, ADLXX at 1 Chronicles 10:1 word 2 has “Philistines” alongside ABP’s “the Philistines.” At word 13 the readings are “fell” and “they fell.”

The ledger retains each lexical choice and records the grammatical difference. Decisions in this pass cover the word choice only. Article use in running English and the identity of a pronoun’s referent still depend on the clause. The verifier checked all 29,329 ledger entries against the current local databases and the ABP source positions.

### Genesis agency, animals, and compass directions

At Genesis 43:14 word 12 in both editions (ABP 43:15 word 12), corrected ἔλαβον from “I took” to “they took.” The narrative names the men as the subject, uses plural participles, and says they took the silver in their hands. The form in isolation permits either person.

At Genesis 49:31 ADLXX word 18 reads ἔθαψα, “I buried,” with Leah as the object. The online ABP interlinear also displays ἔθαψα here but gives it plural English, repeating its rendering of the two preceding plural verbs. Athens word 20 actually reads ἔθαψαν, “they buried.” The difference in the two local renderings belongs to the Greek texts.

Retained “rule” for the luminaries at Genesis 1:16 and “to rule over” at 1:18. The appointment of the lights over day and night supports the governing sense. The comparison also supports retaining the broader animal categories in Genesis, including “sea creatures” at 1:21. At 12:8, 13:14, and 28:14 “the sea” preserves the literal compass designation in the interlinear. All three passages point west. This Genesis pass added 198 verified entries in total.

### First-person singular and third-person plural verbs

A cross-book search found 34 outstanding single-word alignments where one English gloss begins with “I” and the other with “they.” Clause review resolved 32 positions, correcting 24 and retaining eight. Two positions at Hosea 9:13 remain open. The wording there shifts between Ephraim and a plural verb, and εἶδον alone does not establish the speaker.

At Hosea 11:3 word 6 both editions now read “I took up.” The explicit “I” at the start of the verse and “my arm” identify God as the one taking up Ephraim. In Zechariah 11:13 the prophet obeys the command to take the silver. ADLXX word 22 and Athens word 23 now read “I took.” At ADLXX Psalm 94:9 word 10, the fathers who tested God are also the ones who saw his works. The correction is “they saw.”

At Ecclesiastes 2:11, both local editions retain “they made.” The speaker surveys his own work, but “my hands” is the grammatical subject of this particular verb. At Psalm 61:5, the series of plural actions by the speaker’s opponents supports retaining “they ran.” Each ledger row records the local Greek, both interlinear positions, and the clause evidence for the decision.

### Hosea 9:13 and third-person subjects

Resolved the two open Hosea 9:13 positions. Both editions now give “I saw” for εἶδον at word 4. In the comparative clause ὃν τρόπον εἶδον the speaker reports his observation of Ephraim. The following παρέστησαν describes the people presenting their children. NETS independently reads the two clauses this way, as does ABP. The form εἶδον by itself permits either person. [NETS, Hosee 9:13](https://ccat.sas.upenn.edu/nets/edition/32-twelve-nets.pdf)

The additional “he” versus “they” screen found 12 direct positions. At ADLXX 1 Chronicles 19:15 word 25 the Ammonites came into the city, then Joab went to Jerusalem. At Ruth 1:14 word 2 the women lifted their voices. At 2 Kings 23:18 word 12 the bones were spared. At Isaiah 44:15 word 20 the workers fashioned gods from the remaining wood. Both editions now render the singular verb at Ezekiel 26:12 “he will cast.” At Leviticus 14:13 both retain the plural marked by the Greek verb. All 12 decisions were recorded separately from the Hosea corrections.

### Other explicit subject-pronoun disagreements

Reviewed 63 further single-word alignments in which the two English glosses begin with different subject pronouns. Clause review led to 27 changes and 36 retained glosses. At Isaiah 37:36 both editions now give “they found.” The people who rose in the morning (ἀναστάντες) found the bodies. The plural participle resolves εὗρον even though the local glosses and ABP previously offered different singular subjects.

At ADLXX Judges 5:26 words 16 and 21, Jael “pierced” Sisera’s head and temple. At Ruth 2:17 word 9, Ruth “beat out” the grain she had gleaned. At Psalm 8:5 word 5, “you remember” restores both the lexical meaning and the psalmist’s direct address to God. At Job 5:20 and Psalm 17:18, ῥύσεται means “he will rescue.” The next word supplies the object in each verse.

Leviticus 12:3 illustrates a limit of the comparison. Both editions now give “shall circumcise” for περιτεμεῖ and retain the third-singular active analysis. The verb leaves the person's gender unexpressed. By contrast, at Job 39:18 the preceding account identifies the bird through her eggs and repeated feminine pronouns, supporting “she will lift up.” The comparison covered explicit pronouns at the start of both English glosses. Other ways of expressing the subject fall outside this particular search.

### Pronouns after prepositions and differences in the recipient

At Genesis 48:21 word 14 in both editions, Israel tells Joseph that God will be with the family. The preposition μετά governs the Greek genitive ὑμῶν. English needs “with you,” so the pronoun gloss changes from “your” to “you.” The same construction occurs in Zechariah 8:23. A rule-based check of adjacent prepositions and genitive pronouns yielded 119 ADLXX and 103 Athens corrections. Each ledger entry identifies the governing word. The existing Greek case analysis remains genitive.

At five other passages the ABP English identifies a different recipient or referent. Both local editions retain “to you” in Deuteronomy 11:31, “to us” in ADLXX 29:28 (Athens and ABP 29:29), and “to them” in 3:20. Genesis 43:6 (ABP 43:7) reports the question addressed to the brothers. In Joshua 22:5 the people are to cling to the Lord, and αὐτῷ is singular. These ten edition-specific decisions rest on the matching Greek pronouns. Other case differences and masculine or neuter referents require their own contextual review.

### Pronouns with verbs of hearing, memory, and rule

At Genesis 27:8 word 6 in both editions, Rebekah tells Jacob to listen to her. After the local verb gloss “listen,” μου now reads “to me.” At 1 Kings 18:26 the repeated appeal is “hear us,” so ἡμῶν takes “us.” At Genesis 40:23 Joseph is the person forgotten by the chief cupbearer. Both editions now give “him” for αὐτοῦ. The Greek genitive in these passages marks the person affected by the verb.

At ADLXX Job 21:2 word 3, Job asks his hearers to hear his words, and μου supplies “my” with the following noun. At ADLXX Psalm 25:7 word 3 (ABP 26:7), με is the accusative subject of the infinitive, explaining who is to hear the voice of praise. The interlinear retains “me.” These contexts illustrate why a fixed English equivalent for a pronoun case would produce errors. This pass covers 72 direct positions, with 69 preferred glosses corrected.

### Negation in Job, Isaiah, Proverbs, and oaths

At ADLXX Job 1:22 word 7, “at all” left the following “sinned” affirmative. Changed οὐδέν to “not at all.” Athens has οὐχ before “sinned” and also has οὐδέν after Job’s name. Its text already denies that Job sinned. At Proverbs 4:2 word 9, both editions require “not” for μή in the instruction against abandoning the law. In Isaiah 14:23, 40:23 and 40:26 both editions now give “nothing” where the pronoun itself carries the negation.

At 2 Kings 6:31 the speaker explicitly invokes a curse on himself if Elisha’s head remains on him that day. Both editions now give “if” for εἰ at word 11. At 2 Kings 2:2, 2:4 and 2:6 the oath formula expresses Elisha’s resolve never to leave Elijah. The local “surely not” retains that force. Each decision records the precise local and ABP positions.

The first pass through the negation screen resolved 38 contextual comparisons, including 11 corrections. Another 94 direct positions have forms of ἄμωμος glossed “without blemish” or “without defect” locally and “unblemished” in ABP. Those positions agree on the adjective’s meaning.

### A negative in the clause or in the English gloss

Jeremiah 18:18 has a material wording difference. ADLXX word 30 is ἀκουσόμεθα, “we will listen,” with no negative in that clause. Athens word 31 is the same verb, but its word 30 is οὐκ, so the speakers say they will not listen. The online ABP Greek at word 29 agrees with ADLXX at this point, while the attached ABP English gives the negative reading. Both local editions retain the verb gloss, and the separate Athens particle preserves the difference in sense.

At Genesis 14:23, both editions now give “surely not” for the oath particle εἰ. Abram has raised his hand to God and pledges to take nothing from the king of Sodom. At Judges 16:11, ADLXX describes ropes with which no work “was done.” The negative is a separate Greek word. At Job 31:20 both editions now give “they were warmed” for the passive verb describing the recipients of Job’s fleece.

This pass recorded 140 additional decisions, including five preferred-gloss corrections. Decisions about καί rendered “and” or “nor” cover the lexical conjunction. The wording of the surrounding clause determines the scope of the negation.

### Sarah’s name and questions introduced by μή

At Genesis 18:14, ADLXX word 19 is Σάρρᾳ, the dative of Sarah’s name. The previous gloss “to the grave” obscured the promise that Sarah would have a son. ABP independently aligns the name as “to Sarah.” Checking other direct Genesis matches for the same name corrected ADLXX Genesis 21:6, where Sarah speaks after Isaac’s birth, and 21:12, where God tells Abraham to heed what Sarah says. At 17:15 the new name after “but” now reads “Sarah.” The Greek changes from single rho to double rho.

The opening μή in Genesis 18:14 marks the question about whether anything is impossible for God. At Numbers 20:10 Moses asks whether water is to be brought from the rock. Rendering the particle as a prohibition had changed the force of his speech. In these questions the preferred word gloss now identifies the particle as a question marker. In Deuteronomy 20:5–7, by contrast, the men are sent home lest they die in battle, and in Numbers 32:7 and 32:9 μή negates entering the land. The local wording determines each gloss.

### Abram, Er, and the river in Genesis 2

At Genesis 17:5 the Greek distinguishes Αβραμ from Αβρααμ. ADLXX had given “Abraham” for both names. Checking every Genesis occurrence of the shorter form corrected 65 English glosses and the lexical analysis at one further position that already read “Abram.” Of those 66 ADLXX positions, 47 have a verified single-word ABP alignment. The other 19 corrections rest on the local Greek. Athens already distinguished the two names.

At Genesis 38:6, ADLXX had identified Judah’s son Er as a feminine article. His name now agrees with the surrounding family narrative and the genealogy in 46:12. At 10:7, Regma appears first as a son of Chous and then as a father. Both ADLXX positions had read “a flood.” ABP identifies him as Raamah. Athens writes the name with an additional consonant and transliterates it Rhenchma. At 2:11 the first river is named Phison. The participle describing how it encircles the land comes three words later.

This Genesis pass added 1,500 direct name comparisons. The name decisions establish the identity conveyed by a matching Greek word. They do not adjudicate every English case marker or every grouped phrase.

### The place name On and the participle “being”

At Exodus 1:11 word 25, ADLXX Ων is the last of three city names. The next words identify it as Heliopolis. The former gloss “being” and lemma εἰμί have been replaced by “On” and a place-name analysis. Five passages in Hosea and Amos 1:5 also use these letters in place names. Their local context and the directly matched ABP name support “of On.” At 2 Chronicles 33:21 and 36:5 the same printed letters introduce a king’s age and do function as a participle.

At ADLXX Jeremiah 50:13 word 8 the pillars are in On. ABP Jeremiah 43:13 reads “in Egypt” at that position, a difference in the Greek text. The ADLXX correction is supported by its own clause. At Esther 8:12α the letters introduce a relative clause referring to the copy of the letter. The preferred gloss there is “of which.”

The pass recorded 917 Exodus name and title identifications, plus 16 direct comparisons involving On and a separate conditional construction. At Exodus 18:23 both local editions now give “if” for the opening ἐάν in Jethro’s counsel to Moses. The analogous correction in Sirach 18:31 in both editions, and the two ADLXX readings in Jeremiah and Esther, are local Greek decisions outside the direct ABP count.

### Mount Hor, Hur, and the Horites

At Numbers 20:22 ADLXX had “hour” for Ωρ. Israel arrives at Hor, and the following Greek noun identifies it as a mountain. The same error recurred along the itinerary, including 33:37, where “of the morning” obscured the campsite. Ten ADLXX positions in Numbers and Deuteronomy now identify Mount Hor. Athens also had the personal name Hur as a possible reading at Numbers 21:4, where the people set out from the mountain. At Numbers 33:38 Athens explicitly repeats the mountain name. ADLXX says that Aaron died “there.” That particular Athens token has no direct ABP match in the alignment.

The same Greek letters name a man in Exodus. At 17:10 Hur ascends with Moses and Aaron, and at 17:12 he helps support Moses’ hands. Five existing ADLXX decisions now use “Hur” consistently for the man. Deuteronomy 2:22 presented a separate mistake: the sons of Esau displaced the Horite people. ADLXX had rendered Χορραῖον as “land.” The corrected gloss is “Horite.”

The direct comparison also checked 962 matching personal names and titles in Leviticus, Numbers, and Deuteronomy. Those entries verify identity, including cases in which ABP and the local interlinear spell the same name differently.

### Caleb’s allotment and the name of Joshua

At Joshua 14:13 both editions had “to” for Χάλεβ and had parsed the name as an article. The preceding τῷ already marks the recipient. The corrected gloss “Caleb” identifies the man to whom Joshua gave Hebron. At Joshua 13:12 ADLXX had “in” where Ωγ names Og, the king whose kingdom in Bashan is described. At 5:12 ADLXX prints capitalized Φοινίκων and ABP identifies the people as Phoenicians. Athens prints lowercase φοινίκων and gives the palm-tree sense. Capitalization records an editorial interpretation here.

The ADLXX corrections to the name of Joshua include nine positions at which the former gloss was “Jesus” or “of Jesus.” At 10:17 the name is directly aligned, and the report about the five kings is given to Joshua. At 14:2 the editions differ in their Greek wording. ADLXX reads Ἰησοῦ in “by the hand of Joshua.” Athens and ABP read Μωυσῆ, naming Moses. The local ADLXX correction is therefore outside the direct-match count. At ADLXX 9:2ε word 6, Joshua is the explicit subject of reading aloud. Online ABP 8:34 supplies Joshua’s name in English alongside a Greek verb. That alignment verifies no Greek name token.

The pass added 597 direct decisions across Joshua, Judges, and Ruth. Six preferred gloss changes have direct single-word comparisons. Eight additional ADLXX name corrections are based on the local Greek.

### David at En Gedi and the role of Abishai

At ADLXX 1 Samuel 24:1 word 10 (ABP 23:29 word 10), Engaddi names the location of David’s strongholds. The previous English repeated “in the narrow places” from the preceding phrase and lost the place name. The next local verse places David in the wilderness of Engaddi. The first name token has a direct ABP match, while the second correction rests on the local clause.

At ADLXX 2 Samuel 16:9, Abishai speaks to David. At 21:17, he comes to David’s aid. Both name tokens had read “of Abessa,” which obscured who performed the action. At 10:10 the genitive is appropriate: Joab places the remaining troops in the hand of Abishai. The reviewed readings preserve “Abessa,” the local rendering of his name, and identify its grammatical role in each passage. At 1 Samuel 4:11 “Ophni” and Phinehas name the two sons of Eli who died. The earlier “to Ophni” incorrectly implied a recipient.

At ADLXX 2 Samuel 23:11 the capitalized Θηρία identifies the destination where the Philistines gathered. ABP gives Theria; ADLXX now does likewise. Athens prints lowercase θηρία and has the common-noun gloss “wild animals.” The name decision here pertains to ADLXX.

The pass added 1,781 direct comparisons in 1–2 Samuel and corrected 20 ADLXX glosses. Thirteen gloss corrections have direct ABP evidence. Seven additional changes follow the local Greek clauses.

### Gehazi, Jehu, and the royal names in Kings

At 2 Kings 4:31 word 2, ADLXX had converted Γιεζί into the verb “he went.” Gehazi is the subject. At 8:4 word 6, the king speaks to Gehazi, Elisha’s servant, whom the previous gloss called Jesus. In 9:21–22, three tokens of Jehu’s name had become exclamations. Restoring the name identifies whom the kings went to meet and whom Joram addressed. At 8:16 word 7, Joram is the son of Ahab. The former ADLXX gloss named Ahaziah.

At 2 Kings 9:31 word 11, both editions retain Zambri (Zimri), whom Jezebel describes as his master’s killer. The online ABP pairs the same Greek name with the English name Omri. The local editions distinguish the two men. Where ABP explicitly supplied a personal name in English for a Greek verb or pronoun, this pass excluded the position from direct name comparisons.

The pass added 944 direct name comparisons across 1–2 Kings. Of 67 corrected ADLXX glosses, 35 have a single-word ABP alignment. The other 32 corrections were checked against the local Greek. Name-identification decisions leave the surrounding syntax for separate review.

### Genealogies and royal names in Chronicles

At 1 Chronicles 2:20 word 2, ADLXX had rendered Ωρ as “the hour.” Hur is the father named in the genealogy. At 2:26 word 6, the narrative names Jerahmeel in introducing his other wife. The previous gloss said “priest.” At 4:21 word 5, Er is named among the sons of Shelah. The old gloss, “he was,” treated the name as a verb. All three corrections have direct ABP name matches.

At 2 Chronicles 25:17 word 14, the genealogy identifies Joash as son of Jehoahaz and grandson of Jehu. ADLXX repeated Jehoahaz in the second generation. At 35:16 word 30 and 35:26 word 6, Ἰωσίου identifies Josiah in the Passover account and the account of his reign. The former glosses named Joseph and Jesus respectively.

This pass added 1,331 direct name comparisons. Of the 28 corrected ADLXX glosses, 22 had direct ABP matches and six were checked from their local Greek clauses. The ledger records the spelling of each local word and its ABP position.

### Personal names in Ezra, Nehemiah, and Greek Esther

This pass reviewed 566 direct matches for name identification (300 ADLXX and 266 Athens). Six ADLXX corrections have direct ABP counterparts. At Nehemiah 9:7 the first name is Abram, but the new name at word 22 is Abraham. The other corrections identify Ezra (Ezra 10:2, word 12), Pileha (Nehemiah 10:24, word 2), Eliashib (Nehemiah 12:22, word 5), Hanani (Nehemiah 12:36, word 13), and Haman (Esther 9:24, word 2).

The local Greek also establishes two corrections at Nehemiah 12:10. Both occurrences of Eliashib had read “Elizabeth.” Word 10 names Joiakim’s son, and word 12 repeats Eliashib as the father in the next clause. Both were corrected from context and excluded from the direct-match count.

Two direct matches in Nehemiah remain open for editorial judgment. At 3:9, word 8 in both local editions gives “Zur” for Σούρ. ABP word 8 gives “of Hur.” The spelling and English treatment of the name differ. At 3:31, local word 7 gives “the goldsmiths” for Σαρεφί, while ABP word 8 gives “of Sarefi.” This affects whether readers understand a trade or a personal name. Both comparisons match the Greek token after accent normalization. Neither establishes a Greek-witness difference. Muse independently found the two English differences in Athens on Crunch. The positions above were checked locally in both editions against the cached ABP text.

### Direct address, calls to attention, and the word for an age

The direct-word review retained 3,113 readings across the two editions: 1,822 instances of ἰδού, 713 of κύριε, 339 of αἰῶνα, and 239 of υἱέ. The recurring English differences included “look” and “behold,” “age” and “eon,” and English vocatives with or without “O.” At 1 Kings 3:15, word 5 in both editions, Solomon wakes and discovers that he has been dreaming. The ABP interlinear cell gives “knew” for ἰδού. The Greek introduces what Solomon sees, so both editions retain “behold.”

A separate review corrected 47 ADLXX and 52 Athens occurrences of κύριε formerly rendered “the Lord.” Of these, 32 corrections have a direct single-word ABP match in the ledger. The remaining 67 were corrected on the local Greek. For example, Nehemiah 1:11 begins a plea addressed to God, while Judith 11:17 addresses Holofernes. The corrected glosses distinguish “O Lord” in prayer from “lord” addressed to a human superior.

### Missing negation

At 2 Samuel 13:20, word 26, both interlinears left μή blank before “you set.” Absalom tells Tamar **not** to set her heart on the matter. Both now give “do not,” directly supported by the aligned ABP word. At Hosea 4:15, word 4, both also left the prohibition addressed to Israel blank. ABP conveys it in a two-word Greek group. The corrected gloss is supported by that phrase and is excluded from the direct-word count.

Two more clauses required the same repair from local Greek. In Tobit 1:11, word 7, Tobit guards himself so as **not** to eat. In Sirach, a second prohibition tells the hearer **not** to chatter while someone else speaks (ADLXX 32:9 and Athens 35:9, word 9 in both). These four local positions have no direct ABP match in the screen. By contrast, at Job 5:6 the English already carries the negation on οὐ in οὐ γὰρ μή. Adding a second “not” there would distort the clause.

A search of direct pairs for opposite English glosses in seven sets (good/evil, life/death, light/darkness, clean/unclean, love/hate, right/left, and man/woman) found five candidates. All five concerned ἀνδρί in a marriage expression with γίνομαι: Deuteronomy 24:2 in ADLXX, and Numbers 30:7 and Ezekiel 44:25 in both editions. The Greek dative names the man. ABP supplies “wife” to convey the relationship in English. All five local glosses stand. This search covered the specified English terms only.

Muse’s independent negation screen on Crunch covered 37 Athens book units and 727 chapters with cached ABP material. A check against the current local releases confirmed three further passages.

- At 2 Samuel 7:5 (ADLXX word 12, Athens word 11), both editions glossed οὐ as “will.” Both now give “not.” In the oracle to David, the negative falls before the emphatic “you.” ABP translates the particle and pronoun together.
- At Greek Daniel 11:37, word 8 in both editions, the first οὐ had acquired the following verb’s gloss, “will pay attention.” Both editions now give “not.” ABP translates the particle and verb together. The second οὐ in the same verse already carried the negative.
- At 1 Samuel 10:1, word 20, Athens omitted the negative force of Samuel’s question to Saul. Athens now gives “has not,” and ADLXX already gave “not.” Both match the same single ABP token at word 20. ABP has an additional ὅτι immediately after it. This local alignment was verified against the surrounding words despite the automated verse screen leaving the position unresolved.

The ledger also records 193 direct comparisons for transparent expressions of absence, cessation, or exclusion. Examples include ἄνευ (“without”), οὐκέτι (“no longer”), and οὐδέποτε (“never”). Sites where English carries the negative on a neighboring word require a clause-level decision.

The cached ABP Greek cannot independently distinguish οὐ (“not”) from οὗ (“of whom,” “where”) by breathing at any of the 2,715 screened single-token ου matches across the two editions. A breathing is absent on at least one side of every pair. Use the accented local text and the clause when assessing apparent reversals involving this spelling.

### Who speaks and who is addressed

A comparison of 19 first- and second-person pronoun forms added 17,048 direct decisions. At 17,035 positions both English glosses preserve the same personal reference. Six more positions belong to the idiom ἐν ἐμοί introducing a plea. Both interlinears give “please” on the first word and leave the second blank (1 Samuel 1:26 and 1 Kings 3:17, 3:26). At 1 Kings 3:17 the woman addresses Solomon as judge. ADLXX word 8 now reads “lord,” consistent with the addressee and with the petitioner’s later appeal at 3:26.

Seven positions across four verses have first-person plural Greek paired with second-person English in the ABP cell. Both local editions retain “we” at Genesis 47:19, word 21, “us” at Deuteronomy 1:6, word 6, and “with us” at Joshua 8:5 (ADLXX word 22, Athens word 24). ADLXX likewise retains “us” at Deuteronomy 1:21, word 3. Athens lacks that first pronoun in this verse. ABP’s cell at Genesis 47:19 adds “to you” after the preceding verb has already supplied “we will be.”

A separate search of the local Greek found three person errors outside the direct comparison. At 1 Maccabees 13:40, word 5, Athens has ἡμῶν (“of us”); ADLXX has ὑμῶν. At 1 Maccabees 5:38, word 20, Athens has ὑμῶν (“you” after “round about”); ADLXX has ἡμῶν. At Nehemiah 4:15, word 7, Athens has ὑμῶν, so the enemies are “your” enemies. ADLXX 4:9, word 7, has ἡμῶν, as does ABP. All three Athens glosses now follow the local Greek.

In the same sentence, ADLXX Nehemiah 4:9, word 4, had rendered ἥκουσαν as a feminine singular participle, “having come.” The subject is plural (“our enemies”), and the following clause tells what they heard. The corrected gloss is “they heard,” with a direct ABP match at Nehemiah 4:15, word 4. The source spelling is preserved.

### Third-person pronouns and their referents

At 2 Chronicles 35:12, word 6, both editions had made the burnt offering the object of the dative αὐτοῖς. The offering is what is delivered. The pronoun names its recipients (“to them”). At 1 Maccabees 9:7, word 13, the fighting presses Judas himself (“him”). At Job 37:23 the two clauses repeat the same object: people fear him, and the wise also fear him. Athens had changed the second “him” to “them” at word 7.

At Nehemiah 3:10 (word 16), 3:12 (word 4), 3:17 (word 11), and 3:19 (word 5), each edition now gives “his” in the expression locating the next worker beside an individual builder. The earlier plural at 3:10, word 4, refers to a different set of builders. ABP translates some of these expressions as a group. At 2 Chronicles 34:4 Athens describes people overturning altars before Josiah, while ADLXX gives a singular verb. Both have the singular pronoun referring to Josiah.

A plural English pronoun can also be justified by a collective antecedent. At Joshua 24:25 Joshua gives the people a law: the Greek resumes the singular noun λαόν with αὐτῷ, and “to them” refers to the people. At Nehemiah 8:7 “their place” likewise refers to the assembled people. These clauses warranted retaining the local gloss.

The third-person pass added 12,664 direct word decisions, including six corrections with direct ABP counterparts (both editions at 2 Chronicles 35:12, Jonah 1:5, and Ezekiel 42:5). Across both databases, 32 pronoun positions and one accompanying preposition were corrected. In Proverbs the evil “ways” supply the antecedent for “turn from them” (ADLXX 22:14α, word 12; Athens 22:14, word 24). At Psalm 13:7, ADLXX word 30, the reflexive plural refers to “their own” tongues. The other 26 pronoun corrections do not count as direct ABP confirmations.

Two ADLXX verbs also changed on the evidence of their Greek clauses. At 1 Kings 19:20, word 7, Elisha runs after Elijah before he begins to speak. κατέδραμεν therefore reads “he ran down.” At 1 Maccabees 15:9, word 8, δοξάσομέν continues the royal first-person plural: “we will glorify.” The Athens reading δοξάσωμέν differs in mood. Neither correction is included in the direct ABP ledger.

Further checks of ADLXX verb forms corrected three changes of subject. At Joshua 5:4, word 4, Joshua “purified” the people; the previous gloss said “we encompassed.” At Greek Daniel 5:15, word 24, the wise men were unable “to report” the interpretation to the king. At 4 Maccabees 14:9, word 26, it was the young men who endured the suffering. The first-person “we” describes the listeners earlier in the sentence. At 1 Samuel 10:18, word 14, the English “I brought up” was sound. The explicit ἐγώ establishes first singular, and the grammatical analysis now agrees.

Muse independently checked first-person verb number on Crunch in 37 Athens book units with cached ABP material. The three English differences it identified are at Genesis 20:13 (“we enter”), Genesis 37:10 (“shall we come”), and Joel 1:19 (“I will cry out”). At all three, the local Greek confirms the local English. Genesis 37:10 is a grouped ABP rendering; the remaining two direct decisions were already recorded. This search could detect explicit English person markers and does not measure verbs with an unexpressed English subject.

A separate check resolved 5,392 previously outstanding preposition comparisons whose English wording differed: 2,996 “on”/“upon” for ἐπί and its elided forms, 1,788 “from”/“from out of” for ἐκ or ἐξ, and 608 “because of”/“on account of” for διά. Both the local release gloss and the single-word ABP alignment were checked at each position.

### Genitive articles and covenant language

At 1 Chronicles 15:25, word 17, both interlinears had “ark | the | covenant.” The Greek τῆς marks the relation between the two nouns, and ABP gives “of the” on the article. Both now read “ark | of the | covenant.” Across the two editions, 199 such corrections (99 ADLXX, 100 Athens) restore the relationship between adjacent noun glosses, including names of people, sons of the king, and rulers of military or tribal groups. In another 185 positions a preceding preposition already expresses the relationship. For example, πέραν τοῦ ποταμοῦ is “beyond the river.” Both decisions were checked against the individual ABP cells.

A separate pass retained 4,594 differing English glosses of conjunctions, adverbs, and particles. Of these, 3,366 pair causal “because” with explanatory “for” or vice versa. The decision concerns the reason given by the conjunction. At Isaiah 58:3, “why” on τί covers τί ὅτι as a unit.

At Sirach 44:22, word 16, both editions now give “covenant” for διαθήκην. The passage recounts the blessing and covenant established with Isaac through Abraham. The same word in Sirach 38:33 belongs to a legal expression about judgment and retains “ordinance.” The corrections in Sirach were verified from local Greek; Sirach has no ABP coverage in this comparison.

The review of διαθήκη, κιβωτός, and μαρτύριον recorded 1,003 direct word comparisons. In 1 Samuel 13:8 and 13:11, ABP gives “testimony” and both interlinears retain “appointed time.” Samuel had named a seven-day interval at 10:8; Saul’s explanation at 13:11 refers back to those days. At 20:35 the appointment is Jonathan’s agreed meeting with David in the field. These are contextual English differences on matching Greek.

### Judgment, dispute, and legal entitlement

Muse identified judicial language where a stock gloss could change the participants’ roles. At Isaiah 43:26, word 5, both interlinears now give “let us plead together.” The speaker invites the addressee to state the case. ABP likewise uses a verb of pleading. At Proverbs 26:17, word 10, the man who grabs a dog’s tail is compared to someone who gets involved in another person’s dispute. At Proverbs 30:33, word 17, forcing words produces “disputes” and fights. Both editions now distinguish these disputes from delivered verdicts. The last noun is nominative plural, a subject of “will come out.”

Deuteronomy 18:3 uses κρίσις for the priests’ “due” (ADLXX word 4, Athens word 5). The text specifies the shoulder, cheeks, and stomach. ABP has a corresponding Greek token but its English cell is less specific. The entitlement sense comes from the local list. All eight corrected positions and fourteen retained readings have verified single-word alignments.

### Creation and foundation

At Sirach 1:4, word 3, ἔκτισται had received the stock gloss “it was founded.” Wisdom is the explicit subject. Both interlinears now give “has been created.” The same correction applies to pride (10:18, within a negative clause), toil (40:1), and wine (ADLXX 31:27, Athens 34:27). At 39:21, 25, 28, and 29 the Greek singular verb accompanies a neuter plural subject, so English takes “have been created.” These sixteen corrections rest on the Greek of Sirach. A local model helped identify the subjects; each decision was checked against the clause.

Exodus 9:18, word 20, retains “it was founded” because the clause dates the hailstorm relative to Egypt’s foundation. In Leviticus 16:16, word 29, “set up” describes the tent among the people. Both differ from ABP’s use of “created” on the matching Greek. This lexical pass recorded 34 direct comparisons.

### Release, ransom, and speech formulas

Numbers 18:15 uses different voices for the two commands. Word 20 in both local editions is λυτρωθήσεται, “shall be redeemed,” with the human firstborn as subject. The matching ABP cell supplies a second-person active verb. Later in the same verse the local Greek really does address the hearer with λυτρώσῃ. Both local glosses stand. In Joel 1:20 the watercourses have dried up: the plural ἀφέσεις refers to outflows. In Judges 1:15 Achsah seeks relief for dry land, which Caleb grants through the upper and lower water sources.

The comparison recorded 150 direct decisions for release and redemption vocabulary and 91 noun comparisons for which English article placement accounts for the difference. One word qualified for both checks (ADLXX Jeremiah 41:17, word 12) and has one ledger entry. Another 691 comparisons concern τάδε immediately followed by a speech verb. The local “these things” introduces the ensuing words much as ABP’s “thus” does.

### Words displaced by an article or conjunction

At Isaiah 63:2, word 5, the question asks why the **clothes** are red. Both local noun cells had repeated “the” from the preceding article. At 1 Kings 11:38, word 14, **ways** had disappeared from the instruction to Jeroboam to walk in the Lord’s ways. ABP directly confirms the noun in Isaiah and groups “my ways” in Kings. At 2 Samuel 1:12, word 3 is the conjunction between wailing and weeping; the next word already supplies “wept.”

In Tobit, the noun and conjunction now give “liver | and” at ADLXX 8:2, words 22–23, and Athens 8:3, words 9–10. The name in ADLXX 1 Chronicles 4:18, word 6, is Adia; Athens gives Idia and ABP has a different Greek spelling. At Athens Joshua 19:13, word 14, the local word is καί. Correcting the previous “Iaphtha” also removed the obsolete unnumbered lemma entry for that erroneous analysis. Together these checks corrected 51 local positions; 14 had direct single-word ABP evidence in the screen.

### Paired adverbs of place

At Numbers 11:31 the quail extend a day’s journey on either side of the camp. At Greek Daniel 12:5 one figure stands on each bank of the river. A repeated Greek adverb can point to the opposite side on its second occurrence. Muse found this pattern in the Athens data, and both local editions were checked. The review corrected 28 local positions and recorded 18 direct comparisons (14 corrections and four retained readings). Ezekiel 41:3 repeats a seven-cubit measurement in both local editions. The ABP text gives only the first side, so the second local member supplies no direct comparison.

For an up-to-date list of outstanding single-word differences, run `python3 scripts/adlxx/abp_open_positions.py adlxx` or substitute `athens`. The tab-separated output uses current release glosses and the cached alignment and excludes recorded decisions that still match the local reading. The command checks Greek positions against the release as it reads. Grouped ABP cells, blank glosses, and unresolved Greek alignments remain separate review categories.

### Personal names in direct address and measured portions

Hosea addresses Israel directly in 9:1 and again in ADLXX 14:2 (Athens 14:1). Both editions had supplied “of Israel.” Both now identify Israel as the addressee. At Judges 3:9 the Lord raises a deliverer for Israel. The dative introduces the beneficiary. At Isaiah 16:2, word 12, ADLXX had confused the place name Arnon with the genitive plural of “lamb.” ABP identifies Arnon on the matching Greek word. Athens already identified the name.

The pass recorded 257 direct comparisons for halves, multiples, and garment terms, and 273 for names whose preposition was already carried by the preceding local word. Nineteen more ledger positions support the corrections to grammatical relations. The Arnon correction adds a separate direct comparison.

At Isaiah 61:7, word 5, Athens now gives the adjective διπλᾶς as “double.” Its former “double portions” supplied a noun and settled how the adjective attaches. The related ADLXX clause ends verse 6 and uses τῆς διπλῆς. The cached ABP text has no counterpart for this clause. The Athens correction is based on the local Greek and excluded from the direct count.

### Kinship, verb senses, and future forms

At Exodus 18:27, ADLXX word 6 now calls Jethro Moses’ father-in-law. The former gloss reversed their relationship. At Deuteronomy 22:6, word 40 in both editions now calls the mother bird’s offspring her “young.” At Jonah 4:5, ADLXX word 23 now says Jonah waited so that “he might see” what would happen to the city. All four positions have direct ABP entries in the decision ledger.

A separate pass checked 495 matching future-form positions whose English differed only in the choice of “shall” or “will.” The review retained the local glosses. The ADLXX search for the literal placeholder “he/she/it” fell from 78 occurrences to 22 after contextual review. The ledger counts each repaired position only when it has a verified ABP counterpart.

### Genitive articles and contextual verb senses

At 1 Chronicles 11:10, word 5, ADLXX glosses τῶν as “the,” and the next word, δυνατῶν, as “of the mighty.” ABP places the genitive relation on the article. Across both editions 549 individual article decisions document the following Greek form and its current English gloss. In each case the following form is genitive and its local gloss already begins with “of.” This checks the direct lexical choices. A reader still has to put the English phrase in order.

Another 618 verified positions retained the local English. They comprise 261 cardinal-number glosses for 100, 341 comparative conjunctions, and 16 forms of the verb for fighting.

Nineteen ADLXX contextual repairs reduced the “he/she/it” placeholders from 22 to three. Seven have verified direct ABP entries, including Leviticus 25:26 word 9 (the seller gains the means to redeem), Proverbs 11:8 word 4 (the righteous person escapes), and Job 8:15 word 2 (he props up his house). In the local text of Deuteronomy 21:16 word 6 the father assigns the inheritance to his sons. That repair has no entry in the direct ledger. Three difficult forms remain for source review at Job 21:11 word 1, Sirach 4:7 word 1, and 1 Kings 6:20 word 15.

### Foreign residents

Muse screened 220 Athens occurrences in four word families on Crunch. Some English cells in that export contained only alignment numbers. For the direct decisions we checked the cached ABP words and positions separately.

In Ezekiel 22:7 and 22:29 the prophet condemns mistreatment of the προσήλυτος alongside other people vulnerable to injustice. Both editions now gloss the word “resident alien.” “Proselyte” suggested a religious conversion the passage does not specify. The positions are word 10 in both editions at 22:7, and ADLXX word 16 and Athens word 18 at 22:29. Both editions also use “resident alien” at Numbers 15:16 word 11, where the next phrase explicitly describes living among the people. All six have direct ABP counterparts. Another 89 Pentateuchal positions retain local glosses such as “sojourner” or “resident alien” where ABP uses “foreigner.”

### Strangers, property, and tribute

Muse’s stranger-vocabulary screen led to 22 changes across the two editions. Twelve have one-to-one ABP entries in the ledger. In Hosea 10:6 word 7, both now read “tribute gifts” for ξένια carried to the Assyrian king. In Job 31:32 word 5, the open door and the traveler lodging outside establish the hospitality sense “stranger.” In Ecclesiastes 6:2 word 35, ξένος describes the man who enjoys another’s wealth. At Proverbs 2:16 word 9, ἀλλότριον describes a person estranged from sound judgment. In Proverbs 23:27 words 5 and 10, the adjective describes another’s house and well.

The other ten changes rest on the local clauses. At Proverbs 9:18 Athens words 33, 37, 41 and 46 describe another’s water, river and spring. ADLXX divides the corresponding lines between 9:18β words 5 and 9 and 9:18γ words 4 and 9. At Athens Proverbs 11:24 word 14, the contrast is between one’s own property and what belongs to others. The ADLXX verse lacks the phrase τὰ ἀλλότρια. At Athens Proverbs 20:16 word 7, the person giving surety has guaranteed a stranger.

### Negative particles

In 3,428 direct positions, ABP placed an English auxiliary on the negative particle and the local gloss was “not.” Each decision records the adjacent Greek verb and its grammatical analysis. For example, at ADLXX 1 Chronicles 10:14 the particle precedes ἐζήτησε (“he sought”). The phrase says that he did not seek. The local word glosses already supply both the negation and the verb.

At 2 Samuel 3:35 word 27, both editions had glossed μή alone as “until,” even though ἐάν at word 26 was already “if.” Both now gloss μή as “not.” The condition concerns the sun having set, and the following emphatic negative concerns David eating. In continuous English, David vows to eat nothing until sunset.
The ABP cells put “until” on ἐάν and the auxiliary on μή. The parallel supports the meaning of the clause. The choice of “not” as the direct gloss follows the local Greek construction.

### Obligation, life, and spirit

In Job 6:20 those who rely on cities and riches “will incur” shame. In Proverbs 14:9 the houses “will require” cleansing. Both editions and ABP use the same Greek verb, ὀφείλω. A second reading in context refined four earlier decisions which had accepted “will owe.” Both editions also distinguish liability to death at Tobit 6:13 word 33, incurring punishment at 4 Maccabees 11:3 word 12, and the obligation to endure suffering at 4 Maccabees 16:19 word 4. Those six local repairs have no direct ABP counterpart in the cached corpus.

Deuteronomy 24:6 and 24:7 show why ψυχή needs separate decisions even in consecutive verses. Taking the millstone in pledge takes “a life” in pledge (verse 6, word 7). Kidnapping seizes an actual “person” (verse 7, word 6). Both editions now preserve that distinction. All four positions have direct ABP entries. The Mac model flagged both verses and the Greek clauses determined the two different outcomes.

In Ezekiel 1:12, 1:20 and 1:21, the spirit directs the living creatures and the spirit of life is in the wheels. In 2:2, 3:12, 3:14 and 3:24 the spirit raises or carries the prophet. Both editions now give πνεῦμα as “spirit” at eight positions each. All sixteen have single-word ABP matches. At 3:14, Athens has πνεῦμα Κυρίου while ADLXX has πνεῦμα alone at that point. Its parallel gloss therefore carries no added “of the Lord.” The storm wind in Ezekiel 1:4 retains its meteorological sense.

The review also checked 2,040 future verbs where one English gloss supplied the subject pronoun and both gave the same predicate, and 37 occurrences of στόμα followed by a genitive word for sword, where “edge” expresses the cutting edge. At three more positions Athens and ABP use the same English noun, and Athens supplies the definite article on the preceding word.

At Leviticus 21:1 word 19, ψυχαῖς now reads “dead bodies” in both editions. “Persons” omitted the fact that these people have died, which is essential to the priestly restriction and its exceptions for close relatives. By contrast, at 21:11 the participle τετελευτηκυίᾳ explicitly supplies “dead” on a separate word. In 46 other direct comparisons, the local English already expressed the relevant sense of ψυχή, including household members counted in Genesis 46, the people sharing the Passover lamb in Exodus 12:4, and creatures included in the covenant of Genesis 9.

### Court homage and worship at the temple gate

Esther 3:2 uses the same verb for the court’s bow to Haman (word 7) and the bow Mordecai refuses (word 19). Both editions now give “would bow down to” at word 7. All four occurrences were checked against ABP. Mordecai’s prayer in the Greek additions explains the religious significance he attached to the gesture. The court narrative itself reports the king’s command and the courtiers’ response.

At Ezekiel 46:3 words 2 and 19, both editions had analyzed προσκυνήσει as a dative noun and glossed it “for worship.” Both are future verbs. First the prince will worship at the threshold and leave. Then the people will worship before the Lord. The local verse crosses the digital ABP verse division. The prince’s verb matches ABP 46:2 word 33, and the people’s verb matches ABP 46:3 word 2. Each match was checked in its clause. Sirach 50:21 uses the same written form as a genuine noun after ἐν.

In Ezekiel 40–46 the architectural loanword αἰλάμ now reads “porch” in 57 positions across the two editions. Forty have direct English ABP counterparts. At Ezekiel 46:2 and 46:3, eight further decisions identify the gate to which the porch and threshold belong and locate the prince and people at its entrance. The review also restored 444 genitive relations in which adjacent glosses had left the relationship unexpressed. For example, Athens Exodus 19:7 word 8 connects the elders to the people.

The Pentateuchal formula εἰς ὀσμὴν εὐωδίας describes what an offering serves as. At Numbers 28:8, ADLXX word 20 and Athens word 22, both editions now have “as” before the noun for aroma. The same repair applies to 42 occurrences in Exodus, Leviticus and Numbers, of which 36 have directly matched ABP cells.

At Deuteronomy 7:18 word 6 the hearer is to remember “all that” the Lord did to Pharaoh. At the fall of Jericho the city and “all that” was in it are devoted to destruction (ADLXX Joshua 6:21 word 6, Athens 6:20 word 5, ABP 6:21 word 5). In those clauses ὅσα stands on its own. Across 137 other direct positions a preceding form of πᾶς or ἅπας already expresses “all,” so the local “that” carries the relative clause without repeating “all.”

### Houses, households, and presentation in Joshua

At Leviticus 14:38 word 12 the priest goes to the door of the house he is inspecting. All three occurrences in the verse denote the building. Both editions had glossed the middle occurrence “household” and now give “house.” In Judges 6:27 (ADLXX word 23, Athens word 22), Gideon fears the members of his father’s household. The same distinction identifies the king’s household crossing the Jordan at 2 Samuel 19:18 word 16 and the household receiving food at Proverbs 31:15 word 9. All eight corrected positions have direct ABP matches.

Joshua 7:14 gives instructions for identifying an offender. Both editions now have “you shall bring forward” for each of the three occurrences of προσάξετε. The former “you shall offer” suggested sacrifice. The corresponding ABP positions are 17, 27 and 39. The grouping differs slightly in Greek. ADLXX word 28 has singular οἶκον after distributive κατά, while Athens word 27 has plural οἴκους. Their glosses preserve the difference as “household” and “households.” Only the ADLXX singular has a direct match in the ledger.

Among 642 additional direct decisions, the preceding Greek article already carried the genitive or dative relation in English. A further 142 phrases needed that relation restored on the article before a divine title, as in “ark of God” and “angel of God.” The ledger records the direct ABP comparison for the title itself. The article edits follow the local syntax.

### David’s house and the named tribes

At 2 Samuel 7:11 both local editions read οἶκον οἰκοδομήσεις αὐτῷ (“you will build a house for him”). Digital ABP reads οἶκον οἰκοδομήσει σοι (“he will build a house for you”). The noun is a direct match. The verb’s person and the beneficiary differ in the Greek witnesses. In 7:16 both local editions say “his house” and “his kingdom,” while ABP has second-person possessives. The English follows each local text.

The parallel at 1 Chronicles 17:10 explicitly names the Lord as the builder. At word 19 both editions now give αὐξήσω as “I will make great,” addressed to David. At word 24, σοι is “for you,” the beneficiary of the promised house. ABP has the same pronoun at word 23 in a different word order. The noun “house” carries the dynastic promise and recalls the house built for the Lord’s name in 2 Samuel 7:13.

At Numbers 1:21 word 6 and Joshua 13:29 word 6 in both editions, φυλή denotes the named tribes of Reuben and Manasseh. In the census and allotment lists, “clan” would put an entire tribe at the level of one of its subdivisions. The review changed 241 positions naming Israelite tribes (121 ADLXX and 120 Athens). Of these, 169 have direct, single-word ABP entries in the ledger.

Another 1,554 direct decisions retained the local verb sense. They include “went up” and “ascended” for ἀναβαίνω, “commanded” and “gave charge” for ἐντέλλομαι, and articular plural participles of κατοικέω naming inhabitants.

The surrounding passage supplied the same distinction at 57 further positions. Numbers 31:4–6 draws a thousand men from each tribe. Joshua 4 assigns one representative and one memorial stone per tribe. Numbers 36:3–12 addresses the transfer of inherited land between tribes. Fifty-four of these positions have direct ABP matches.

Zechariah 12:12–14 uses φυλή differently. The mourners gather by ancestral clan, with David’s and Nathan’s houses named separately. The repeated καθ᾽ ἑαυτήν means that each clan mourns by itself, and καθ᾽ ἑαυτάς says the women mourn by themselves. Both editions had used “concerning” for the preposition. The review corrected 55 word positions in these verses, including the duplicated “clan by clan” gloss at verse 12 words 6 and 7. Fifty have direct ABP entries. Athens has an additional mourning clause before the house of David at 12:12. The first preposition for David’s house is therefore Athens word 20, ADLXX word 11, and ABP word 11.

### Obadiah’s opening summons

At Obadiah 1:1 the Lord speaks to Idumea, a dispatch goes **to** the nations, and the summons calls them to rise **for** war. In verse 2 Edom is small **among** the nations. Both editions now give these relations explicitly. At 1:1 word 13, παρά already supplies “from,” so Κυρίου now reads “the Lord.” The review applied that correction at 65 positions across the two databases where an immediately preceding preposition already supplied “from” or “out of.” The two opening verses have 30 direct word decisions in this pass.

### Obadiah through verse 21

All 21 verses have now been checked for outstanding, directly aligned single-word English differences. The ledger contains 173 decisions for ADLXX and 170 for Athens in Obadiah. The source alignment also classifies 82 ADLXX and 79 Athens positions as grouped or supplied wording, and 25 ADLXX and 31 Athens positions as differing Greek or uncertain alignment. Those categories lie outside the single-word totals.

At 1:5 both editions now show the negative in the two questions about thieves and grape pickers. At 1:7 the allies prevail *against* Edom. Athens adds an explicit possessive after “borders” where ADLXX has none. At 1:14 ADLXX’s ἐπιστῇς warns Edom against taking its stand at the escape routes. The former “fix” obscured the action. The following participle describes the fugitives escaping. At 1:21 the survivors go up from Zion “to exact judgment on” Mount Esau.

Verse 18 requires separate treatment for the two Greek spellings. Athens has πυρφόρος (“fire bearer”). ADLXX and the digital ABP have πυροφόρος. For the latter spelling LSJ records both a fire-bearing word and a separate agricultural word for bearing wheat. ADLXX retains “fire-bearer” on the strength of the fire, flame, and stubble imagery immediately preceding it. ABP takes the agricultural sense. Only ADLXX has a matching Greek word for this direct comparison. [LSJ entries in the Perseus Digital Library transcription](https://github.com/PerseusDL/lexica/blob/1c34cdf756c63cf37db61bd366d733431dbd7aa0/CTS_XML_TEI/perseus/pdllex/grc/lsj/grc.lsj.perseus-eng17.xml#L589790-L589858)

### Genesis 1–2 and the river Geon

Genesis 2:13 word 7 in ADLXX had analyzed Γεῶν as plural and glossed it “of the Getae.” The sentence names the second river, Geon, and describes its course around Ethiopia. Athens spells it Γηών and already identifies the river. The directly aligned ABP word spells it Γεών and calls it Gihon. In Genesis 2:14 the Tigris flows onward in ADLXX (προπορευόμενος) and flows in Athens (πορευόμενος). At 2:19 the name is given to the creature. ADLXX has the dative αὐτῷ, and Athens has possessive αὐτοῦ.

In both editions Genesis 1:24 now gives ψυχὴν ζῶσαν the same “living being” sense found in 2:7 and 2:19. At 2:7 and 2:24 εἰς marks a result: the man becomes a living being, and the two become one flesh. At 1:26 the cached Apostoliki Diakonia publisher page itself prints γῆς twice at the end of the verse. ADLXX preserves both tokens. Athens prints τῆς γῆς. A direct comparison of one occurrence does not establish agreement on the repeated phrase.

At Genesis 1:6 word 9 the article now expresses the relation in “the midst of the water.” The same repair applies to 189 positions with a genitive complement to “midst” or “middle,” including 104 with directly aligned ABP article glosses.

Muse’s household review also identified Ahithophel’s two uses of “house” in 2 Samuel 17:23. He goes to his house (word 21) and gives instructions to his household (word 30). Both editions now distinguish them. The ABP English groups the noun and possessive at both positions. Those grouped phrases supply context and are excluded from the single-word ledger.

### Genesis 3

The direct single-word review has no open positions in Genesis 3 in either edition. At Genesis 3:8 the ADLXX interlinear now reads “the” + “voice” across the article and noun. At Genesis 3:11 (twice) and 3:17 both editions use “you” for the person told or commanded. These seven changes affect the English glosses.

At Genesis 3:15 both local Greek texts repeat τηρέω for the head and the heel. Both interlinears retain “will watch for” in each clause. ABP groups the first verb with a pronoun, so only the second occurrence supplies a direct single-word comparison. At Genesis 3:20 “Life” preserves the connection between the name Ζωή and “living” in the same verse.

### Genesis 4:20

Ada's son is now “Iobel” in ADLXX (᾿Ιωβήλ). “Jubilee” was an incorrect common-noun gloss. ABP calls him “Jabel.” The same verse ends with κτηνοτρο‘φων in the stored publisher text. The internal punctuation splits the compound into two database positions. The glosses now read “livestock” + “keepers.” Athens has the intact κτηνοτρόφων. The ADLXX repair to the compound is contextual and contributes no direct ABP word decisions.

### Genesis 4:13–15 and Genesis 5

At 4:13 both editions now gloss με as “me.” Cain describes his guilt as too great for him to be forgiven. At 4:15 both retain “will release” for παραλύσει. The verb is active, the person who kills Cain is the subject, and ἑπτὰ ἐκδικούμενα supplies what the killing would unleash. ABP's passive wording changes that relationship. The [NETS Genesis translation](https://ccat.sas.upenn.edu/nets/edition/01-gen-nets.pdf) independently reads the clause with an active verb and plural object.

Three ADLXX corrections in the Genesis 5 genealogy concern syntax. At 5:4 μετά with the articular infinitive marks time after Seth's birth. At 5:14 Καϊνᾶν identifies whose days are counted (“of Cainan”). At 5:32 Σήμ stands in apposition to Noah's sons (“Shem”). Both names are indeclinable, so their function comes from the surrounding words.

### Genesis 6 and the name Shem

At 6:2 Athens has ἄγγελοι (“angels”) and ADLXX has υἱοί (“sons”). At 6:4 both have υἱοί. The difference at 6:2 belongs to the Greek texts and falls outside direct gloss scoring. At 6:6 διενοήθη describes God's reflection (“pondered”). At 6:7 the first-person μετεμελήθην introduces God's stated regret (“I regretted”). The interlinears preserve both verbs.

At 6:10 ADLXX had “of Shem” where the name identifies one of the three sons Noah fathered. A concordance check found five more places where this gloss obscured the syntax or duplicated a preceding genitive marker. ADLXX now reads “Shem” at Genesis 6:10, 7:13, 9:18, 9:26, 10:1 and 1 Chronicles 1:4. Where the name alone identifies a possessor, as in “sons of Shem” at Genesis 10:22, the genitive gloss remains.

A corpus-wide spelling pass also checked direct matches where the English differed only in regional spelling or hyphenation, including “favour” and “favor,” and “firstborn” and “first-born.” Each ledger entry retains the verse, position, Greek and both English forms.

### Genesis 7–8

- At 7:11 ADLXX now says that the springs of the deep “burst open.” The floodgates of heaven open at 7:11 and close at 8:2. ADLXX had assigned the same Greek noun unrelated English glosses at these two positions. Both entries now give “floodgates,” as in Athens. At 7:18 both editions now say the ark “was being carried” on the water.
- At 7:4 and 7:23 both interlinears retain “living thing” for ἀνάστημα. The destruction promised at 7:4 is fulfilled at 7:23, where the text enumerates humans, animals, creeping things and birds. ABP's “height” obscures that reference.
- At 7:6 ADLXX says the flood of water came upon the earth. Athens says the flood was upon the earth. At 8:13 ADLXX repeats ἐξέλιπε and now gives “had gone” both times. Athens has an imperfect in the second clause. At 8:20 ADLXX uses εἰς to identify what the animals were offered as. Athens has the offering noun without this preposition.
- The concordance distinguishes other senses of καταρράκτης. Malachi 3:10 also speaks of the floodgates of heaven. Deuteronomy 14:17 names a diving bird in a dietary list, and Jeremiah 20:2–3 describes confinement and release. The precise form of restraint is uncertain. ADLXX uses “stocks” at both Jeremiah positions, consistent with Athens and Jeremiah 36:26.

### Genesis 9–10

At 9:4 both interlinears now render ἐν as “with” in the prohibition on eating flesh with its lifeblood. At 9:10 μεθ᾿ ὑμῶν means “with you,” referring to animals with the people in the ark. At 9:9 the accusative μεθ᾿ ὑμᾶς means “after you,” referring to their descendants. Identical English for both prepositions would change the covenant's recipients.

At 9:25 both witnesses curse Canaan. At 9:26 ADLXX repeats παῖς οἰκέτης (“servant,” “household slave”), while Athens has παῖς alone. In 9:27 Canaan is the subject of Noah's wish. ADLXX has αὐτοῦ (“his”) and Athens has αὐτῶν (“their”).

At 10:4 ADLXX now identifies Javan as the father and renders the plural Ρόδιοι as “Rhodians.” ABP's English gives “Dodanim” at the aligned position. At 10:12 Δασή is the name of the city between Nineveh and Chalach. Athens spells the name Δασέμ. At 10:19 ADLXX prints τὰ ὅραι, but traces territorial limits from Sidon onward. “Boundaries” is a contextual interpretation supported by Athens τὰ ὅρια. The publisher's Greek spelling is preserved and the interpretation is recorded on the word itself.

### Genesis 11–12

At 11:9 the Greek names the city Σύγχυσις (“Confusion”) and says that the Lord συνέχεε (“confused”) the people's speech. ADLXX now distinguishes Arran, Lot's father (11:26–31), from Harran, the family's destination (11:31–32). It also gives Eber, Ragau and Melcha consistently where the genealogy repeats their names.

At 12:2 εὐλογημένος is a perfect passive participle. Both interlinears retain “blessed” in the promise to Abram. At 12:3 both now give “earth” in “all the tribes of the earth.” At 12:7 the land promised to Abram's offspring is particular, and ADLXX now gives “to” for the dative marking Abram as the person to whom the Lord appeared.

The earlier name review identified Abram correctly but missed a genitive relationship at three ADLXX positions. Genesis 11:31 and 12:17 identify Sara as the wife of Abram. Genesis 14:12 identifies Lot as the son of Abram's brother. Each name now supplies “of Abram.” At 13:7 and 14:13 a preceding article already supplies “of.”

### Genesis 13–14

At 13:14 Abram looks toward the sea. Both editions now read “the sea (west),” preserving the geographical landmark behind ABP’s “west.” At 13:16 the two clauses repeat “the sand of the earth.” The second clause has a passive verb: if the sand could be counted, Abram’s offspring too would be counted.

At 14:19 Melchizedek blesses Abram in the name of the creator of heaven and earth. Abram repeats the expression in his oath at 14:22. Both editions now give “earth” at both references. At 14:6 ADLXX identifies the landmark as the terebinth of Pharan. At 14:23 the object Abram refuses belongs to a sandal. “A fastening” preserves that sense without specifying its shape. ADLXX spells the word σφυρωτῆρος and Athens σφαιρωτῆρος.

### Genesis 15–16

In 15:3–4 Abram asks who will be his heir, and God identifies the child who will come from Abram himself. At 15:6 Abram believes God, and it is reckoned to him as righteousness. Both interlinears now flag the dative article before “God” so a reader can assemble the English clause.

Two ADLXX word analyses had changed the sense. At 15:11 συνεκάθησεν describes Abram sitting down with them. At 15:16 Ἀμορραίων names the Amorites, the people whose sins have not yet reached their full measure. ADLXX had repeated “sins” where the Greek names the people.

At 16:13 Hagar calls God the one who looked upon her. ADLXX has ἐπιδών and Athens has ἐφιδών. The ADLXX analysis had associated the spelling with giving. The participle, its object “me,” and Hagar's own words about seeing the one who appeared to her support the visual sense. At 16:10 Athens has ἀπό and ADLXX has ὑπό. Both introduce the great number of Hagar's descendants as the reason they cannot be counted.

### Genesis 17–18

At 17:7, ADLXX μετὰ σέ refers to descendants who come *after* Abraham. At 17:20 God promises to make Ishmael into a great nation. At 17:21 both interlinears now render πρὸς Ἰσαάκ as “with Isaac,” consistent with the same covenant construction at 17:19. At 17:15 both preserve the Greek name change Σάρα → Σάρρα as “Sara” → “Sarah.”

At 18:10 Sarah listens *by* the tent door, behind the visitor. In 18:10 and 18:14 the repeated εἰς ὥρας is rendered “in due season.” At 18:19 ADLXX μετ᾿ αὐτόν, like Athens μεθ᾿ ἑαυτόν, places Abraham's household *after* him.

At 18:24 ADLXX πάντα τὸν τόπον extends Abraham's plea to the whole place. The form πάντα is masculine singular here and qualifies “place.” Athens has τὸν τόπον without πάντα in this question. The divine reply at 18:26 gives the scope of the promise.

The two Genesis corrections prompted a corpus-wide check of open direct comparisons where the local gloss for μετά was “with” and ABP gave “after.” A check of each complement and clause found 49 further corrections to “after.” These include the end of the 430 years at Exodus 12:41, the fire following the earthquake at 1 Kings 19:12, and the order of workers along the wall in Nehemiah 3. Thirteen local readings retain “with,” including the sons serving with their father in Numbers 18:7. The Joshua comparison (ADLXX 24:29, Athens 24:31) remains open.

### Genesis 19–20

At 19:3 Lot presses his visitors to stay. ADLXX κατεβιάζετο had been assigned to καταβαίνω (“go down”). Its context and morphology support καταβιάζομαι. Athens uses παρεβιάζετο in the same exchange. At 19:26 Lot’s wife looks back, while in 19:28 Abraham looks toward the cities. The directional expression for looking behind is present only in the former clause. Both interlinears now preserve the distinction.

At 19:21 the city is the topic of Lot’s request. The phrase περὶ ἧς ἐλάλησας means “concerning which you spoke.” A review of similar constructions across the OT corrected 28 directly aligned positions in total, including the queen’s report concerning Solomon’s wisdom (2 Chronicles 9:5). The article and noun also determine the sense of πᾶς. A separate pass corrected 176 positions with specific definite singular phrases such as πᾶς ὁ λαός (“all the people”). At 20:18 πᾶσαν μήτραν has a singular noun without the article (“every womb”).

At 20:6 the ADLXX source includes an unexpected λίγο immediately before εἶπε. Both the cached publisher chapter and the live chapter show the word. Athens begins with the verb of speaking. This source difference is outside the direct word comparison and its textual origin is unresolved. [Apostoliki Diakonia, Genesis 20](https://apostoliki-diakonia.gr/bible/genesis/?file=1.20)

### Genesis 21–22

In 21:16 both editions make the child the subject of “wept.” At 21:17 God hears the child and the angel addresses Hagar. At 21:25 ADLXX had assigned ἀφείλοντο to the wrong verb and glossed it “they let.” The servants took the wells away, which explains Abraham's complaint. Athens already gives that sense with ἀφείλαντο. The two men swear an oath there, explaining the name “Well of the Oath” at 21:31–32.

At 22:6 the fire and knife are in Abraham's hands. ADLXX has μετὰ χεῖρας (plural) and Athens μετὰ χεῖρα (singular). Both describe how he carried them. At 22:13 the Greek names Sabek where the aligned ABP rendering describes a thicket. Both local texts retain the ram as the offering in Isaac's place. At 22:17 the participles repeat the verbs “bless” and “multiply.” The interlinears now show both repetitions in the oath. At 22:24 ADLXX Μοχά and Athens Μωχά are rendered “Mocha.” The former ADLXX gloss “Mahalalel” identified a different person.

A follow-up check of μετά found 49 other positions where the genitive describes company or manner. Exodus 19:24, for example, permits Aaron to go up *with* Moses. Five local “after” glosses were retained where the case and clause support succession, including the articular infinitives in Judges 19:23 and Jeremiah 47:1.

### Genesis 23

The review recorded 89 new ADLXX decisions and 90 new Athens decisions for Greek words aligned individually to ABP. Both editions now identify the “sons of Heth” consistently and render the field as lying opposite Mamre. In 23:8 Abraham asks his hearers to speak to Ephron, son of Zohar. In 23:16 Abraham pays Ephron in silver. The ADLXX verb gloss now identifies Abraham as the payer. These corrections concern the English sense of the local Greek.

### Genesis 24

In 24:4 ADLXX has ἐγεννήθην (“I was born”), while Athens has ἐγενόμην (“I came to be”). Each interlinear follows its own verb. In 24:5 both editions now gloss ὀπίσω as “back.” The servant asks whether the woman will come back with him and whether he should take Isaac back if she declines. In 24:8 μόνον introduces Abraham’s one restriction, so the gloss reads “only.” At 24:16 both editions now give “virgin” for the first occurrence of παρθένος. The Greek repeats the noun and adds that no man had known Rebekah.

In 24:26 the servant responds to the news about Rebekah by worshipping God. When he retells the event in 24:48 he uses the same participle, εὐδοκήσας. Both editions now read “being well pleased” in both passages. The family gives its answer later, in 24:50–51.

In 24:41 the servant explains what will release him from his oath. ADLXX now reads “free” at both occurrences of ἀθῷος and “from” at the first ἀπό. Athens already expressed that sense. In 24:42 ADLXX’s αὐτῇ refers to the road. In 24:51 both editions now give “let her be” for ἔστω, with Rebekah as the subject.

### Genesis 25 and the well report in 26:32

In 25:1 the ADLXX naming clause now identifies the woman *whose* name was Keturah. In 25:9 ADLXX’s masculine relative refers to the field opposite Mamre. Athens has a neuter relative, which can refer to the cave. Both locate the burial property. In 25:18 the territory extends from Havilah to Shur. The same endpoints recur at 1 Samuel 15:7. ADLXX now gives Havilah in both passages.

In 25:31 and 25:33 both interlinears retain “sell” and “sold.” Esau accepts food in exchange for his birthright and confirms the transaction by oath.

In 26:32 both local Greek texts end the servants’ report with οὐχ εὕρομεν ὕδωρ and a full stop. They report that they did not find water. The aligned ABP Greek and English also express the negative.

### Genesis 26

At 26:16 Abimelech gives his reason for sending Isaac away. Both editions now gloss ἐγένου as “you have become.” At 26:19 ζῶντος describes the water the servants found. “Flowing” conveys the sense of living water in a newly dug well. At 26:20 and 26:22 the English well names preserve the connections between Wrongdoing and the wrong done to Isaac, and between Roominess and the room the Lord has made for him.

At 26:24 ADLXX now gives “because of Abraham” for δι᾿ Ἀβραὰμ. The accusative πατέρα in apposition to the name confirms the construction. Athens already expressed the same reason for the promise. In 26:35 both editions now make explicit whom Esau’s wives were quarreling with, Isaac and Rebekah.

### Genesis 27

At 27:37 Isaac twice describes what his blessing has established. ADLXX’s perfect forms of ποιέω now read “I have made.” Jacob is master, and his brothers are his servants. Athens uses aorists and reads “I made.” At 27:38 Esau asks his father whether he has only one blessing. ADLXX had assigned a masculine subject to ἐστι. Its subject here is the blessing.

At 27:45 Rebekah fears losing both sons in one day. ADLXX’s ἀποτεκνωθῶ now reads “I may be bereaved.” The directly aligned ABP word supports that sense. Athens uses a different verb, ἀτεκνωθῶ, and already expresses being left childless.

### Genesis 28–29

At 28:9 Esau marries Mahalath, the sister of Nebaioth. ADLXX previously had “Naboth.” The genealogy identifies Nebaioth as Ishmael’s firstborn in 25:13, and the same sister-of-Nebaioth formula recurs in 36:3. All three ADLXX entries now give the name and its grammatical role. Of these three, 28:9 was checked directly against the aligned ABP word. At Bethel, 28:15 promises Jacob protection and a return to this land. In 28:20–22 Jacob asks for protection and a safe return and vows a tenth of what God gives him.

At 29:3 the shepherds would gather the flocks, roll the stone away, water the sheep and put the stone back. ADLXX had parsed the last verb as first-person singular. At 29:18, 20 and 25 both editions now repeat “for Rachel” in the proposal, the account of Jacob’s service and his complaint to Laban. At 29:35 ADLXX now identifies Leah’s fourth son as Judah.

### Genesis 30

At 30:3 Rachel expects to have children through Bilhah. At 30:8 ADLXX συναντελάβετό μου now reads “has helped me.” Athens uses a different verb with a dative complement, συνελάβετό μοι, and conveys the same help. The ADLXX correction at 30:8 rests on its Greek clause. Its verb was outside the direct ABP word alignment.

At 30:32 Jacob stipulates which animals will count as his wages. ADLXX had rendered ραντόν as “bleeding.” The aligned ABP word, the same marking in 30:33, and the selection of goats in 30:35 all support “spotted.” Athens already gives “speckled” for ῥαντόν in its longer list. Both editions now mark the sheep in 30:36 and 30:40 as belonging to Laban, keeping them distinct from Jacob’s animals.

### Genesis 31

In 31:39 Jacob accounts for the sheep lost under his care. ADLXX has οὐκ ἐνήνοχά σοι, “I have not brought [it] to you.” Athens includes the modal particle ἄν and retains “I would not have brought.” The following clause makes Jacob responsible for the cost of thefts.

At 31:42 both editions now identify “the Fear of Isaac” and say that God was with Jacob. Jacob invokes the same title when he swears his oath. In the covenant formula the two names are genitives in sense. Both interlinears now read “the God of Abraham and the God of Nahor.” The local references are ADLXX 31:53 and Athens 31:54. Both align to ABP 31:53.

### Genesis 32

In 32:1–2 the camp belongs to God. Both editions now give “of God” for the genitive following “camp.” The angels who meet Jacob in 32:1 and the messengers Jacob sends to Esau in 32:3 share the Greek noun ἄγγελος. Their senders and actions explain the different English choices.

In 32:8 the feminine pronoun refers to one of Jacob’s two camps. Both editions now give “it.” ADLXX κόψῃ describes Esau striking the camp, while Athens has the compound ἐκκόψῃ. In 32:11 Jacob prays for the mothers together with their children.

At 32:24 the wrestling lasts until morning. At 32:28 ADLXX explicitly says “you shall be” strong with human beings. Athens has the adjective δυνατός without that final verb. At 32:30 both editions preserve Jacob’s declaration that he saw God face to face and that his life was saved. The temporal phrase in 32:32 carries the custom concerning the sinew forward to the narrator’s own day.

### Genesis 33

In 33:1 Jacob divides the children among their mothers, who approach with those children in verses 6–7. Both local glosses retain “children.” In 33:10 Jacob compares seeing Esau’s face to seeing the face of God, echoing his words at 32:30. The genitive now reads “of God” in both interlinears. At 33:12 ADLXX’s πορευσώμεθα proposes action, “let us go.” Athens likewise expresses an invitation and then adds a first-person singular verb.

At 33:19 the field is bought *from* the father of Shechem. At 33:20 Jacob sets up the altar and calls upon “the God of Israel.” Both editions now express these relationships.

### Genesis 34

At 34:7 Jacob’s sons are cut to the heart when they hear what happened to Dinah. The former ADLXX gloss “felt compunction” suggested remorse on their part. At 34:8 Hamor says his son *chose* Dinah. ADLXX had glossed προείλετο as “foretold.” At 34:17 λαβόντες means “having taken.” The brothers say they will take Dinah and leave if their terms are refused.

At 34:27 both local editions and ABP have ἐμίαναν, an active plural verb with Dinah as its object. ABP renders the clause in the passive. Both local interlinears retain the active sense “had defiled.” This difference arises in the English rendering of the same Greek form.

### Genesis 35

At 35:7 Jacob gives the place the name Bethel. Both editions now read “Bethel” in the naming clause. At 35:16 the ADLXX gloss “Apahras” made the opening word look like a personal name. Ἀπάρας is a participle of ἀπαίρω. Jacob is the one who sets out from Bethel. ABP’s aligned verb confirms the action.

At 35:18 both Greek editions give the words of Rachel’s name for her son, “Son of My Pain,” followed by the name Benjamin given by his father. At 35:25–26 the genitives identify Bilhah and Zilpah as mothers and distinguish Rachel’s servant from Leah’s. The Reuben and Bilhah episode is ADLXX 35:21 and Athens 35:22, both aligned to ABP 35:21.

### Genesis 36

At 36:5 the verb describes sons *born* to Esau in Canaan. The family headings identify Esau as father of Edom (36:9) and name his wives in apposition to their names (36:10–18). In 36:29–30 the chiefs’ names follow their titles directly.

In 36:36–37 ADLXX names the same king, Σαμαδά, at his accession and his death. Its English now reads “Samada” in both places. Athens consistently has Σαλαμά, “Salama.” The former ADLXX glosses “Samaria” for the king and “of Meshach” for his place of origin obscured the succession. The place is Μασεκκᾶς, Masekkas, also named in the parallel succession at 1 Chronicles 1:47. The repeated phrase ἀντ᾽ αὐτοῦ in 36:33–39 describes the next king reigning in his predecessor’s place.

At 36:20 the ADLXX entry Ἀνά names Ana among Seir’s sons. The former gloss “from” dropped him from the list. The parallel genealogy in 1 Chronicles 1:38 confirms his identity. At 36:23 ADLXX’s Γωλάμ names Golam, a son of Sobal. The former English “Goliath” identified a different person.

At 36:24 both local editions have Ἰαμείν, which ABP interprets as “mules.” The passage says the discovery took place while the finder was pasturing his father’s animals. That context does not establish what he found. The local interlinears retain the transliteration. The finder is named Ana in ADLXX and Onas in Athens.

### Genesis 37

At 37:1 ADLXX had assigned both verbs to lemmas for sleeping. Κατῴκει describes Jacob dwelling in Canaan, and παρῴκησεν describes his father sojourning there. Athens already preserved that distinction. At 37:21 ADLXX ἐξείλετο means that Reuben *rescued* Joseph from his brothers. The following verse explains his intention to return Joseph to his father.

At 37:26 Judah asks what profit there is *if* the brothers kill Joseph. Both interlinears now preserve the condition, which leads to Judah’s alternative proposal in 37:27. At 37:28 both local editions and ABP specify twenty pieces of **gold**. The “ferocious wild beast” proposed by the brothers in 37:20 recurs in Jacob’s own conclusion in 37:33 after he recognizes the bloodstained coat.

### Genesis 38

At 38:8–9 Judah tells Onan to raise up offspring for his brother. The repeated dative identifies the brother for whom the offspring would count. At 38:11 Judah fears that his remaining son might die too. Both interlinears now express that fear in his reason for sending Tamar home.

At 38:18 ADLXX had misidentified ἀρραβῶνά as “bridegroom.” The aligned ABP word means a deposit, and the same noun occurs in 38:17 and 38:20. ADLXX now reads “pledge” throughout the exchange. Tamar identifies its owner by the signet ring, cord and staff in 38:25. At 38:27 ADLXX now gives ἔτικτε as “was giving birth,” describing the labor in which the twins are born.

### Genesis 39

At 39:5 the Lord blesses the Egyptian’s household because of Joseph. Both interlinears retain “of the Lord” for Κυρίου in εὐλογία Κυρίου, linking the blessing to the Lord just named as its giver. ABP reads the same genitive as referring to Joseph’s human master. At 39:16 the household setting supports the human referent: the woman retains Joseph’s clothing until her husband comes home. ADLXX now gives “master” there.

At 39:9 Joseph asks how he could commit such a wicked *deed* and sin before God. At 39:12 the woman seizes him by his clothes and he flees. Her later account reverses who initiated the encounter. Athens begins that report to the household in 39:13, while ADLXX begins it in 39:14.

### Genesis 40

At 40:8 Joseph says that the interpretation of the dreams comes through God. Both local editions and ABP preserve διὰ τοῦ Θεοῦ. The local “interpretation” and ABP’s “explanation” convey the same sense.

At 40:10 both local editions now distinguish the vine’s three branches (πυθμένες) from the shoots it puts forth (βλαστούς). Joseph repeats “three branches” in 40:12 and identifies them as three days. His promise that the cupbearer will return *to* his office at 40:13 is fulfilled in 40:21. For the baker, the three baskets mark the same interval but lead to a different outcome (40:18–19, 22).

### Genesis 41:1–16

At 41:5 the ears of grain grow on one stalk (πυθμήν). The same noun denotes a vine branch in 40:10. At 41:13 the cupbearer recalls his restoration *to* his office, the outcome Joseph predicted in 40:13 and the narrator recorded in 40:21.

At 41:16 both local editions gloss σωτήριον as “welfare.” ABP gives “deliverance.” The Greek word matches, and Joseph makes the answer to Pharaoh depend on God in all three renderings.

### Genesis 41:17–57

At 41:21 Pharaoh adds a detail to his first account of the dream. The lean cows swallowed the healthy cows, yet no one could tell **that** they had swallowed them. Both interlinears now give this sense to ὅτι. At 41:29 ADLXX and ABP read the genitive Αἰγύπτου, “of Egypt.” Athens reads the dative Αἰγύπτῳ in the phrase locating the plenty throughout the land. We retained the Athens reading.

At 41:37 ADLXX’s Ηρεσε means “was pleasing.” The subject is Joseph’s proposal, and Pharaoh and his servants approve it. The earlier “he answered” introduced a speaker. Athens already had “pleased,” with a plural subject in its Greek text. At 41:42 the first αὐτόν refers to the ring Pharaoh puts on Joseph’s hand. The second refers to Joseph, whom Pharaoh clothes. Both interlinears now distinguish “it” and “him.”

### Genesis 42

At 42:1 both editions begin with ΙΔΩΝ. The capital letters had led both interlinears to treat it as a personal name. The verb form and the parallel wording at 42:7 identify it as “having seen,” from ὁράω. Jacob sees that grain is for sale. ADLXX also confused πρᾶσις (“sale”) with πρᾶξις (“action”). Athens already identified the sale correctly. The corrected Athens verb retains Strong’s G3708.

At 42:13 and 42:32 the brothers say their youngest brother is **with** their father. The genitive after μετά supports “with” in both places. At 42:20 the local texts and ABP have the same future passive πιστευθήσονται. Both local interlinears retain “will be believed” because the brothers’ words are the subject. ABP’s first-person active English gives Joseph’s side of the exchange.

At 42:24 Joseph turns away and weeps. His name follows the verb as its subject. At 42:36 Jacob says that all these things have happened to him. The singular Greek verb ἐγένετο has a neuter plural subject, which takes a plural verb in English. Muse on crunch independently reviewed the chapter, including these clauses at 42:1, 42:13, 42:20, 42:32 and 42:36.

### Genesis 43

At 43:8 Judah answers for Benjamin. He invites his father to hold him personally responsible if he fails to bring the boy back. At 43:17 and 43:19 τὴν ἀρχήν refers to the brothers’ first trip to Egypt. At 43:24 ἀριστᾶν refers to eating the midday meal.

At 43:31 καθ᾿ ἑαυτούς occurs twice. The brothers and the Egyptians are each served “by themselves.” At 43:33 Athens has singular μερίδα (“a portion”) at word 3, while ADLXX and the corresponding ABP verse (43:34) have plural μερίδας (“portions”). The English interlinears now preserve that difference. Both local texts then distinguish the brothers’ drinking (ἔπιον) from its result (ἐμεθύσθησαν, “became drunk”). Muse independently flagged the number difference and the two verbs on crunch.

### Genesis 44–46

At 44:7 the brothers address a human master. At 44:8 the owner of the house is Joseph. At 44:24 Judah recalls Joseph’s words to Jacob, and at 44:33 he offers to serve Joseph in Benjamin’s place. Both editions now use “master” for these human referents. At 44:5 the steward’s accusation describes divining **by the cup**.

At 45:6 Joseph predicts five more years without ploughing or harvest. ADLXX had “unplowed” and an unrelated lemma for ἄμητος. The corrected entry gives “harvest,” matching Athens and ABP. At 45:22 the brothers receive robes, and Benjamin also receives three hundred **gold pieces**. At 45:26 Jacob is stunned when his sons tell him Joseph is alive.

At 46:13 ADLXX’s Ζαμβράμ is the name of a son of Issachar. The interlinear had mistaken the name for an adjective and rendered it “ambrosial.” ADLXX now gives “Zambram.” Athens has Σαμβράν, “Sambran.” At 46:29 ADLXX describes Joseph’s weeping with πίονι (“copious”), whereas Athens has πλείονι (“greater”). Muse independently identified both differences.

### Genesis 47–50

At 47:1 the capitalized ΕΛΘΩΝ is a participle. Both editions now read “having come,” with Joseph as its subject. The Athens entry for ἔρχομαι retains G2064. At 47:17 the repeated ἀντί describes the exchange of livestock for bread. At 47:18 the Egyptians address Joseph as their master.

At 48:14 Jacob crosses his hands to lay his right hand on Ephraim, the younger son. At 48:20 the verb ἔθηκε expresses the precedence Jacob gives Ephraim over Manasseh. The previous “stored” obscured that act.

At 49:6 ADLXX has ἐρείσαι. The active verb ἐρείδω can express resting on something; Jacob asks that his inward parts may not rest in the brothers’ assembly. Athens has ἐρίσαι and retains its gloss “join in strife.” The poetic syntax leaves the interpretation less certain than the spelling difference. At 49:10 ADLXX and ABP have τὰ ἀποκείμενα αὐτῷ, “the things reserved for him.” Athens has ᾧ ἀπόκειται, “for whom it is reserved.” The readings give different subjects to “comes.”

At 50:19 Joseph reassures his brothers that he belongs to God. The Greek gives Θεοῦ in the genitive. At 50:20 the brothers planned harm, but God intended good. ADLXX ends with καὶ τραφῇ and Athens with ἵνα διατραφῇ. Both express the preservation of a numerous people. Muse on crunch independently reviewed the four chapters.

### Exodus 1–5

At 1:7 ADLXX’s κατίσχυον says the Israelites “were growing strong.” Its earlier gloss, “they were weak,” reversed the sense of the verb and the reason for Pharaoh’s alarm. ABP has the same imperfect form. Athens already read “grew strong” for its aorist κατίσχυσαν.

At 2:3 the mother coats the basket with pitch. At 2:5 Pharaoh’s daughter sees the same basket. ADLXX had assigned θῖβιν different lemmas and glossed it as “pitch” and “storm” in these verses. Both are now “basket,” consistent with θίβις and its dative in 2:6. At 1:15 Shiphrah is the midwife named with Puah. Moses’ wife Zipporah appears at 2:21. The local Greek spelling of the two names is the same.

At 3:14 both editions retain “the one who is” for ὁ ὤν, including its repetition in the message to Israel. At 3:22 ADLXX’s σκυλεύσετε is future indicative, “you will plunder.” Its earlier “you may scourge” changed the action and the mood. ABP has the same Greek verb. Athens uses συσκευάσετε for the stripping of the Egyptians.

At 4:7 the command to Moses is “put in,” and his hand subsequently returns to its former condition. At 4:23 ADLXX and ABP have plural αὐτούς, the object of “send away.” Athens has singular αὐτόν, referring to Israel collectively. The verse immediately follows God’s designation of Israel as his firstborn son. At 5:22 Moses asks **why** the people have suffered. Muse on crunch independently reviewed these five chapters.

### Exodus 6–10

The review added 1,309 single-word decisions across the two editions and revised four earlier decisions. At Exodus 6:18 ADLXX names Kohath’s son Izhar (Ἰσαάρ). The earlier gloss identified him as Isaac. At 7:9 ῥίψον tells Aaron to throw his staff. At 10:8 ἀπέστρεψαν describes Moses and Aaron being brought back. At 10:17 both editions use “forgive” for Pharaoh’s request concerning his sin.

The insect names also exposed errors outside the exact-form count. ADLXX 8:12–14 corresponds to Athens and ABP 8:16–18. The ADLXX glosses now consistently identify gnats. Athens and ADLXX have σκνίφες where ABP has σκνίπες (“midges”). At ADLXX 8:17, 20 the plague is dog-flies (κυνομυίης), corresponding to Athens and ABP 8:21, 24 (κυνομυίας).

At 9:15 both editions now render πατάξω “I will strike.” The surrounding Greek differs. ADLXX θανατώσω supplies a second verb, “I shall put to death.” Athens θανάτῳ describes the means, “with pestilence.”

### Exodus 11

Verified 55 ADLXX and 57 Athens single-word decisions. In Athens 11:2 γυνὴ now reads “a woman” in the instruction to ask a female neighbor. At 11:5 and 11:7 both editions use “to” for ἕως in the ranges from one firstborn to another and from human to animal. At 11:3 both retain “lent” for ἔχρησαν in light of the preceding request for valuables and clothing.

A separate ADLXX correction at 11:1 restores Pharaoh as the subject of ἐξαποστέλλῃ, “he sends away,” with ὑμᾶς as the object. Athens has the shorter verb ἀποστέλλῃ. The ADLXX correction is outside the 55 exact-form decisions.

### Exodus 12–15

At 12:34 both editions now identify lumps of dough wrapped in clothing. At 15:13 both read “righteousness” for δικαιοσύνῃ, replacing “steadfast love.” ABP groups the possessive with the noun in each passage, so these are phrase-level checks outside the single-word ledger.

In ADLXX 13:19 Joseph asks Israel to carry his bones up with them. At 14:3 the wilderness has shut the Israelites in. At 14:21 the water was divided, and at 14:27 it returned. In both editions 15:15 now says that the chiefs of Edom hastened. The following clause describes trembling among the leaders of Moab.

At 12:18 the calendar instruction still specifies the twenty-first day. The two interlinear components μιᾶς and εἰκάδος supply one and twenty respectively. At 12:46 the meat stays in the one house. At 14:11 παρά introduces the Israelites’ sarcastic question about the lack of graves in Egypt.

At 14:28 the Apostoliki Diakonia publisher prints κατελήφθη, the form transcribed in ADLXX. Its current lexical gloss “was taken” stands. Athens and ABP print κατελείφθη, “was left.” The unambiguous ending οὐδὲ εἷς now reads “not even one” in both interlinears. Only the shared ending enters the cross-edition comparison for this correction. [Apostoliki Diakonia, Exodus 14](https://apostoliki-diakonia.gr/bible/exodos/?file=2.14)

At 12:37 the first εἰς introduces Succoth as the destination. The second introduces an approximate count of the men on foot, “about six hundred thousand.” At 12:39 the provisions are “for” the journey.

The remaining Exodus 12 decisions include the household counting rule at 12:4, the sandals “on” the feet at 12:11, and the cattle Pharaoh releases at 12:32. At 12:44 ADLXX reads ἢ (“or”). The ABP transcription displays unaccented η with a relative English gloss. The accent-insensitive match cannot establish agreement in sense here. Athens has τινὸς καὶ at this point.

At 13:17 both editions now render μεταμελήσῃ “change their minds.” Seeing war might induce the people to return to Egypt. The shorter Athens verse defeated the automatic verse alignment, but its two verbs correspond directly to ABP 13:17 words 24 and 30. At 13:2 and 13:15 “from human to animal” gives the range of firstborn covered by the statement.

At 14:16 Moses is commanded to divide the sea. The ADLXX analysis of ρῆξον now identifies a second-person singular imperative of ῥήγνυμι. At 14:19 the pillar moves from the front of the camp and stands at the rear. At 15:9 both editions retain “I will kill” for ἀνελῶ. The enemy names his sword as the instrument of the threatened killing. At 15:17 the plural ἡτοίμασαν agrees with “your hands,” so the hands prepared the sanctuary.

### Exodus 16–18

At 16:16 ADLXX συσκηνίοις identifies the people sharing the tents. This matters for the instruction to count portions of food by persons. At 16:20 ADLXX ἐξέζεσε and Athens ἔζεσε both describe the food breeding worms. Their Greek forms differ. At 16:35 μάν names the food the Israelites ate for forty years. The previous “of Man” obscured both the referent and the grammar.

At 16:16 and 16:18 the masculine plural καθήκοντας describes the people belonging to a household. At 16:21 the neuter singular καθῆκον describes what each person needed. At 17:2 the Athens imperative δός reads “give” in the request for water. At 18:26 difficult cases are referred *to* Moses.

Two ADLXX readings in Exodus 17 were checked against the publisher. At 17:14 μνημόσυνονἐν is printed without a space. Its gloss now includes both “a memorial” and “in,” preserving the preposition that introduces the scroll. At 17:16 the publisher prints εἰς γενεᾶς. Athens prints εἰς γενεάς, the expected accusative plural. ADLXX retains the singular gloss and flags the unusual form. [Apostoliki Diakonia, Exodus 17](https://apostoliki-diakonia.gr/bible/exodos/?file=2.17)

### Exodus 19–21

At 19:2 ADLXX names Rephidim, the camp named at 17:1. The former gloss “reed” lost the place name. At 20:7 the ADLXX article ὁ introduces Θεός in “the Lord your God.” The later participle names the person taking the divine name in vain. Athens has the shorter subject Κύριος. At 20:23 ADLXX repeats ὑμῖν αὐτοῖς, referring to the people addressed both times.

At 19:22 the warning to priests who draw near includes ἀπαλλάξῃ ἀπ᾽ αὐτῶν, “remove some of them.” At 20:25 ABP takes the final verb as plural and understands the stones as defiled. Both local editions retain “it has been defiled” with singular αὐτό immediately before the verb, referring to the altar on which the tool was used. The English difference can arise from the referent without a different Greek spelling. NETS also takes the altar as the referent. [NETS Exodus](https://ccat.sas.upenn.edu/nets/edition/02-exod-nets.pdf)

At ADLXX 21:2 the servant goes out free in the seventh year. At 21:8 “he betrothed” is affirmative. The earlier negative qualifies the woman's failure to please the master. At 21:14 the deliberate killer is taken *from* the altar. At 21:33 the pit is the antecedent of the pronoun in the instruction to cover it.

### Exodus 22–23

At 22:8 and 22:11 both editions introduce the oath with ἦ μήν, “surely.” The former gloss “or” treated the first word as the disjunction ἤ. At 23:9 αὐτοί refers to the people addressed, who were themselves strangers in Egypt.

At 23:5 the AD publisher prints γόνον (from γόνος). Athens prints γόμον (from γόμος), and ABP groups the latter form with its possessive in the sense “load.” The difference is one consonant. The context favors “load,” but that is the lexical sense of the Athens form. ADLXX's existing “semen” remains an unresolved contextual gloss. Its verb συναρεῖς can independently be corrected to “you shall help lift.” [Apostoliki Diakonia, Exodus 23](https://apostoliki-diakonia.gr/bible/exodos/?file=2.23)

At 22:28 both editions retain the lexical gloss “gods” for θεούς. ABP interprets the referents as magistrates. The next clause explicitly names a ruler, ἄρχοντα, in the singular. At 23:21 ὑποστείληταί σε concerns the messenger shrinking from the person addressed. The emphatic negative says that he will not do so. At 23:31 both occurrences of ἕως mark geographical endpoints.

### Exodus 24–27

At 24:10 the named group sees *the place where the God of Israel stood*. ADLXX εἶδον and Athens ἴδον both take the plural subject established in 24:9. ABP has the Athens spelling. At 24:15 ADLXX explicitly names Joshua alongside Moses. Athens and ABP name only Moses in this verse.

At ADLXX 25:21 and Athens 25:22 γνωσθήσομαί σοι now reads “I will make myself known to you.” The following verb introduces God's speech from above the mercy-seat. In the instructions about stones, ADLXX 25:6 aligns with Athens and ABP 25:7. Both editions have σαρδίου, “of sardius.” The earlier gloss identified the stone as onyx. At ADLXX 25:15 δῷ is third person, “gives.” Athens 25:16 has first-person δῶ, “I give.”

At ADLXX 26:8 and 26:10 δέρρεως refers to the tent covering. Length and width are its dimensions. The loops run along its edge. At 26:28 the middle bar runs from one side to the other.

### Exodus 28–30

At ADLXX 28:22 and 28:24 κρωσσοί are the plaited gold tassels attached to the breastpiece. The chain-work is described separately. At 28:29–30 the ornaments around the robe are little pomegranates interspersed with bells. At 30:25 χρῖσμα identifies the sacred anointing preparation.

At Exodus 29:21 ῥανεῖς directs Moses to sprinkle the priests and their garments. The altar instruction uses προσχεεῖς for pouring blood against the altar. At 29:42 γνωσθήσομαι means “I will make myself known.” At 29:43 τάξομαι means “I will give instructions.” At 30:25 ἅγιον describes the anointing preparation as holy. The genitive τοῦ ἁγίου at 30:24 refers to the sanctuary in the instruction about weights.

### Exodus 31–40

At ADLXX 32:20 Moses ground the calf fine before scattering it. At 34:15–16 ὀπίσω describes following foreign gods. At 36:34 the ornament is a pomegranate, at 37:14 the fabric is spun fine linen, and at 38:22 the bronze comes from the fire-pans of Korah’s assembly.

At Exodus 31:18 both interlinears retain “finished” for κατέπαυσε. In 31:17 the same form describes the Lord resting on the seventh day. In 31:18 the participle λαλῶν tells what ended. The Lord finished speaking to Moses and gave him the tablets. At 31:6 ABP uses the conventional English name Aholiab for the craftsman whom both interlinears call Eliab. The aligned Greek name supports Eliab.

Exodus 31 now has a decision for every open matching-word comparison in both editions. At 31:14 ἐν αὐτῷ means “on it.” The pronoun refers to the Sabbath on which work is prohibited. At 31:16 the plural σάββατα is the object of “keep.” At 31:17 the scope of creation calls for “heaven and earth.” The editions diverge at 31:13, where Athens has ἐν ὑμῖν (“among you”) and ADLXX has ἐν ἐμοί (“in me”). The shared preposition does not justify harmonizing the pronouns.

At Exodus 32:20 both interlinears retain “strewed” for ἔσπειρεν. Moses has already ground the calf fine. The verb describes scattering that material on water, which Moses then makes the Israelites drink.

At Exodus 32:11–14, Moses asks why the Lord is angry *against* his people. At 32:12 ἵλεως is an adjective paired with γενοῦ, “be gracious.” At 32:13 the Lord swore by himself, and αὐτήν refers to the promised land (“it”). At 32:14 the following relative clause makes the sense of κακία specific. It is the calamity that the Lord had spoken of bringing upon the people.

Across the OT, a further 429 aligned positions differ in the English spelling of a name. Examples include Joram/Jehoram for Ἰωράμ and Choreb/Horeb for Χωρήβ. The decisions record the two English forms and the Greek at each position. The review retained the local spellings.

At Exodus 32:4 Aaron shapes the gold *with* an engraving tool. The preposition introduces the instrument. At 32:5 Aaron announces “tomorrow” in direct speech. At 32:26 Moses stands *at* the gate and asks who is *for* the Lord. ADLXX 32:9 and Athens 32:10 direct the Lord’s anger *against* the people. The latter correction follows the Athens Greek at its own verse number.

At Exodus 33:3 ADLXX εἰσάξω has the Lord say “I will bring [you] in.” Athens εἰσάξει has “he will bring [you] in,” continuing the promise about the angel. At 33:14 both editions have καταπαύσω σε, “I will give you rest.” At 33:16 ADLXX has first-person singular ἐνδοξασθήσομαι, while Athens has first-person plural ἐνδοξασθησόμεθα. At 33:17 both editions use the masculine relative ὃν because its antecedent is λόγον. The Lord agrees to grant Moses’ request, so the English relative is “which.”

At Exodus 34:7 ADLXX οὐ καθαριεῖ τὸν ἔνοχον means that the Lord will not acquit the guilty. Athens already gave the judicial sense of καθαριεῖ. Later in the verse ADLXX reads ἀνομίας (“iniquities”) where Athens has ἁμαρτίας (“sins”). Both readings stand. At 34:8 Moses bows to the ground. At 34:22 ποιήσεις takes the Feast of Weeks as its object, giving “you shall observe” the feast. At 34:33 κατέπαυσε with λαλῶν means Moses finished speaking before he put on the veil.


At Exodus 35:2 ADLXX has the neuter plural ἅγια σάββατα and Athens has the singular ἅγιον σάββατον. In both, the adjective describes the Sabbath. In 35:33 ἔργῳ refers to work in general. The surrounding examples are stonework and carpentry, and the word itself does not identify netting.

ADLXX 35:8 corresponds to ABP 35:9 and ADLXX 35:9 to ABP 35:10. The ledger records 21 single-word comparisons recovered by checking those references directly. At the end of the first verse ADLXX has ποδήρη, the long robe, where ABP has λογεῖον, the breastpiece. In the second verse ADLXX has καρδίᾳ, “heart,” where ABP has διανοίᾳ, “mind.” These two differences belong to the Greek texts.

At Exodus 36:3 the artisans receive the offerings from Moses for the work. At 36:13, corresponding to ABP 39:6, both interlinears now give σμαράγδου as “of emerald.” The verse describes the two shoulder stones engraved with the names of Israel’s sons. At ADLXX 36:40 and Athens 36:38, corresponding to ABP 39:31, λῶμα names the band holding the plate on the head covering. Its colour comes from the following adjective.

The direct review recovered 76 single-word Athens comparisons outside the automatic alignment. Athens 36:12, 16, 20, 21 and 33 correspond to ABP 39:5, 9, 13, 14 and 26 respectively. At 36:16 both dimensions of the doubled breastpiece are one span. The possessives after “length” and “breadth” are present in Athens.

At Exodus 37:2 both interlinears previously treated αὐλαίας as accusative plural. In both occurrences τῆς αὐλαίας τῆς μιᾶς means “of one curtain.” The length is twenty-eight cubits and the width four, with the same dimensions for every curtain. The parallel is ABP 36:9. ABP 36:15 shares some wording but describes a different covering with a length of thirty cubits.

For Exodus 37 the ledger adds 109 previously flagged positions and 145 further comparisons from direct verse alignment. The veil and entrance screen correspond to ABP 36:35–38. The court, its furnishings and the account of its construction correspond to ABP 38:9–23. Only individually matched Greek forms with a single-word alignment are counted.

At Exodus 38:12 σπείσει is singular and denotes pouring a libation. ABP 37:16 supplies “priest” in English. Neither local Greek clause names the officiant at that word. At ADLXX 38:16, words 15 and 26, the lamps (λύχνοι) are set on the ἐνθέμια. The new gloss “lamp supports” describes their function. Their shape remains uncertain. Athens has ἀνθέμια, “blossoms.” The ADLXX correction follows its own Greek and is outside the count of direct ABP matches.

At Exodus 39:4–5 the same noun κεφαλίς occurs four times. The two local verses together correspond to ABP 38:27. All three Greek texts name capitals, with one talent of silver per capital. The phrases “capitals (sockets)” and “per socket” at 39:5 have been made consistent with 39:4. The rendering “capitals” also appears in the [NETS translation of Exodus](https://ccat.sas.upenn.edu/nets/edition/02-exod-nets.pdf).

At ADLXX 40:19 and Athens 40:21 Moses carries the ark *into* the tent. At ADLXX 40:29 and Athens 40:35 the same construction expresses Moses’ inability to enter the tent when the cloud overshadows it.

### Leviticus 1–3

At ADLXX 1:6 ἐκδείραντες means “having skinned.” Skinning precedes cutting the animal into pieces. Athens uses the shorter form δείραντες and already had “skinning.” At ADLXX 1:7 the priests pile wood on the fire. At ADLXX 2:13 the negative and διαπαύσατε prohibit omitting the covenant salt. The earlier “you exhort” had assigned the verb to the wrong lemma. These corrections at 1:7 and 2:13 follow the local Greek outside the tally of directly aligned words.

The material determines the sense of θυσία. At 2:1 the offerer brings flour, oil and frankincense, which supports “grain offering.” At ADLXX 3:6 the offerer selects an animal from the flock. Here θυσία σωτηρίου is a sacrifice of well-being. At 9:4 both editions name a calf and a ram before mentioning the flour separately.

### Leviticus 4–9 (selected corrections)

At ADLXX 4:17 the priest sprinkles blood seven times before the veil. Both editions have the verb from ῥαίνω. ADLXX presents the preceding conjunction across two source tokens, κα’ and Ι. Its gloss is carried on the first token. At 8:6 both interlinears had assigned αὐτούς to the lemma for water. It is the direct object “them,” referring to Aaron and his sons. The following ὕδατι supplies “with water.”

### Leviticus 4–5

At 4:20 the priest makes atonement *for them* (περὶ αὐτῶν), the congregation. The following passive verb has “the sin” as its subject, and αὐτοῖς identifies the people who receive forgiveness. At 4:27 γῆς in “one of the people of the land” refers to the land. At 5:16 the offender repays the loss, adds a fifth and gives it to the priest. The priest then makes atonement for the offender with the ram. The two actions have different agents.

ABP 6:4 covers two local verses, ADLXX 5:23–24 and Athens 6:4–5. Joining each pair for comparison recovered 104 single-word decisions. In both editions ἤ introduces another kind of property the offender must restore, so it reads “or.” The relative οὗ refers to the matter about which the offender swore falsely. The principal and the additional fifth are owed to the owner.

### Leviticus 6–7

At ADLXX 6:2, 5–6 (Athens and ABP 6:9, 12–13), the subject of καυθήσεται is the fire. The priests must keep it burning on the altar. At ADLXX 6:14 the griddle offering is described as ἑλικτά, “rolled pieces.” Athens 6:21 has ἐρικτά, “crushed.” The ADLXX reading agrees with the description of the offering in [NETS Leviticus](https://ccat.sas.upenn.edu/nets/edition/03-leu-nets.pdf).

ADLXX 6:22 and Athens 6:29 correspond to ABP 6:29. The phrase ἐν τοῖς ἱερεῦσι identifies who may eat the offering, “among the priests.” Both editions read the plural αὐτά, “them,” where ABP has singular αὐτό, “it.” At the end of the verse ADLXX and ABP have Κυρίῳ, “to the Lord,” whereas Athens has Κυρίου, “of the Lord.” The paired adjectives ἅγια ἁγίων express “most holy” here and at 7:6.

At 7:34 the breast is part of the additional offering that goes to the priests. The former gloss for ἐπιθέματος implied that the breast was put on the altar. Verse 31 assigns the fat to the altar and the breast to Aaron and his sons.

### Leviticus 8–10

At 8:26 Moses places a loaf made with oil among the items used for consecration. Both interlinears had glossed ἄρτον as “food” where the list identifies the kind of bread. At 8:36 Aaron and his sons carry out the commands, and at 9:22 Aaron raises his hands and blesses the people. Both editions now identify Aaron as the subject. The ABP alignment at 9:22 groups the name with the participle, so that correction rests on each edition’s Greek and is outside the single-word count.

At ADLXX 10:16 the goat “had been burned up” (ἐνεπεπύριστο). Moses then becomes angry with the surviving sons (ἐθυμώθη). The former gloss “he was indignant” assigned Moses’ reaction to the verb describing the goat. Athens already distinguished the two actions.

### Leviticus 11–12

In Lev 11:5–6, ADLXX places οὐκ before ἀνάγει for both animals. Athens has the affirmative in both verses. ABP agrees with Athens in verse 5 and ADLXX in verse 6. In Lev 12:4–5, ADLXX describes the blood as ἀκαθάρτῳ (“unclean”) and Athens reads καθαρῷ (“clean”). Each interlinear follows its own Greek. A separate English correction in ADLXX at 12:5 gives καθεσθήσεται as “she shall remain.”

The dietary laws supplied context for several corrections in both editions. Lev 11:3, 4, 7 and 26 refer to hooves, 11:27 refers to paws, and συναγωγῆς in 11:36 describes a collection of water. The animal names include a probable bearded vulture in 11:13, a long-eared owl in 11:17, and a snake-fighting grasshopper in 11:22. The species identification in 11:13 remains tentative. [LSJ lexicon](https://github.com/PerseusDL/lexica/tree/master/CTS_XML_TEI/perseus/pdllex/grc/lsj) · [NETS Leviticus](https://ccat.sas.upenn.edu/nets/edition/03-leu-nets.pdf)

### Leviticus 13

Both editions now gloss ἤ as “or” at Lev 13:29, 30, 42 (twice), 43, and 51, where the law lists alternative sites or materials. In 13:36 the priest examines the hair, and in 13:49, 52, 53, 57, and 58 the law covers any leather article. These are corrections to the English for matching Greek words. The review also retained “lesion” for ἁφή and “weft” for κρόκη where ABP uses “infection” and “woof.” The first term describes the affected area under inspection, and the second names the threads crossing the warp.

At Lev 13:7 the priest sees the patient. Both interlinears now identify αὐτόν as the object of ἰδεῖν, consistent with the grammatical note on τὸν ἱερέα and with NETS. In ADLXX, the signs in 13:19, 24, 43, and 49 describe reddish coloration. In 13:56 the damaged material is torn off. Both editions distinguish cloth made of tow (13:47, 59) from the more general reference to linen (13:48, 52). Both retain “scab” for θραῦσμα in 13:31–37. LSJ cites 13:30 for precisely this use. [LSJ](https://github.com/PerseusDL/lexica/blob/master/CTS_XML_TEI/perseus/pdllex/grc/lsj/grc.lsj.perseus-eng9.xml) · [NETS Leviticus](https://ccat.sas.upenn.edu/nets/edition/03-leu-nets.pdf)

Lev 13:55 has a Greek difference. ADLXX reads ἥδε (“this”), where Athens reads ἴδε (“look”). The ADLXX correction removes a stray English article. Each edition retains its Greek reading.

### Leviticus 14

At 14:4 both editions had assigned the gloss for the person being cleansed to λήψονται. The verb now reads “they shall take,” with the beneficiary expressed separately. At 14:10 both now identify the measured ingredient as fine flour. The ADLXX publisher page spells the following participle περυραμένης. The parallel in 14:21 and the Athens reading support “mixed” with oil. This particular spelling was checked against the cached publisher page and the parallel passage, separately from the matched-word decisions.

At 14:16 and 27 ADLXX now specifies sprinkling oil seven times. At 14:37 the wall markings are reddish, and in 14:41 the inside of the house is scraped. At 14:14, 17, 25, and 28 both editions use “extremity” for ἄκρον. The following Greek words supply “hand” or “foot.” ABP renders the expressions together as thumb and big toe.

### Leviticus 15

At 15:2 ADLXX now renders both occurrences of ῥύσις as “discharge.” The same noun in 15:13, 25, 26, and 30 had sometimes been confused with the subsequent cleansing. At 15:9 the ADLXX verb describes mounting the donkey's saddle, while Athens describes sitting on it. At 15:29 ADLXX has the nominative αὕτη referring to the woman taking the birds. Athens has the dative αὐτῇ, “for herself.”

In 15:23 the final αὐτῆς in both editions refers to touching the woman. The opening participle describes her lying on the bed or sitting on the object. The intervening σκεῦος is neuter. Both ABP and NETS support “her.” [NETS Leviticus](https://ccat.sas.upenn.edu/nets/edition/03-leu-nets.pdf)

### Leviticus 16

At 16:14 the first κατά in ADLXX directs the sprinkling toward the east. The second κατά begins κατὰ πρόσωπον, “in front of.” At 16:19 the priest sprinkles the altar with blood. The ADLXX gloss for ρανεῖ had instead instructed him to wash. In 16:4 Athens explicitly reads τράχηλον (“neck”), which ADLXX lacks. Each interlinear retains its edition’s wording.

### Leviticus 17–18

At 17:13 both editions describe the hunted animal or bird as one that is eaten. At 18:19 γυναῖκα denotes a woman, with no marital qualification in the clause. At 18:25 ADLXX’s ἐξεμιάνθη and Athens’s ἐμιάνθη both say the land was defiled. The earlier ADLXX gloss “was purged” reversed the sense. The editions differ in the Greek verb form and agree on the direction of the action.

### Leviticus 19–20

At 19:12 ADLXX now reads “holy” for ἅγιον. The adjective modifies God’s name. At 19:15 θαυμάσῃς πρόσωπον δυνάστου forbids showing deference to the powerful party in judgment. The clothing prohibition ends at ADLXX 19:19 and continues into Athens 19:20. Both now describe putting on the mixed garment. At 20:17 both Greek editions explicitly switch subject to the sister. Their interlinears now read “she sees” at the second ἴδῃ.

### Leviticus 21

The anointing oil rests “upon” the priest at 21:12. At 21:18 both editions read κολοβόριν. LSJ cites the verse for “slit-nosed.” At 21:20 ἔφηλος describes a white spot in the eye. ADLXX πτίλλος and Athens πτίλος refer to inflamed eyelids, and λειχήν describes a skin eruption. [LSJ lexical entries](https://github.com/PerseusDL/lexica/tree/master/CTS_XML_TEI/perseus/pdllex/grc/lsj)

### Leviticus 22 and selected later passages

In 22:21 both editions now give ἤ as “or” between a vow and a voluntary offering. At 22:23 the animal may be used for private slaughter. ADLXX uses ποιήσεις (“you shall make”) and Athens uses ἀποθήσεις (“you shall set aside”). Both distinguish this use from an animal acceptable for a vow.

The later corrections include ADLXX 23:32, which specifies the ninth day of the month, and 23:43, where God says he made Israel dwell in booths. At ADLXX 26:16, ἴκτερα denotes jaundice. LSJ records this accusative under ἴκτηρ. Athens reads ἴκτερον and already gave the same English sense. The latter check concerns distinct Greek forms and is outside the single-word ABP decision count. [LSJ lexical entries](https://github.com/PerseusDL/lexica/tree/master/CTS_XML_TEI/perseus/pdllex/grc/lsj)

### Leviticus 23–27

At 23:38 πλήν occurs four times. The festival offerings are **in addition to** sabbaths, gifts, vows, and voluntary offerings. Both interlinears now give “besides” at each occurrence. At 24:11 φυλή identifies the **tribe** of Dan. At 25:36 παρά with the genitive identifies the person **from** whom interest may not be taken. At 27:12 and 14 the contrast is between **good and bad condition** in the valuation of an animal or a house.

ADLXX 26:41 requires an editorial judgment. The cached publisher text prints ἀπολῷ. Athens has ἀπολῶ, the regular first-person future, and both ABP and NETS give a future in this clause. ADLXX retains its printed spelling and now glosses it “I will destroy,” with the morphological interpretation marked in the database. [NETS Leviticus](https://ccat.sas.upenn.edu/nets/edition/03-leu-nets.pdf)

### Numbers 1

The census formula is inclusive. Both editions now gloss ἐπάνω as “upward” in the age requirement beginning at twenty (1:3 and the tribal enumerations). At 1:50 σκεύη refers to the tent’s equipment. At 1:53 the Levites are to camp around the tent. At 1:54 the ADLXX publisher prints ᾿Αραρών where Athens has Ἀαρών. Moses and Aaron receive the command in both editions. ADLXX now identifies Aaron, and this spelling difference is outside the direct ABP word count.

### Numbers 2

At 2:2 ADLXX’s παρεμβαλλέτωσαν directs Israel to camp by ancestral house. At 2:3 κατά places Judah toward the east. Both editions identify Ephraim’s position at 2:18 as westward, the sense of the sea as a compass direction. At 2:27 both now identify Asher, the same tribe named again in the clause about its leader. These corrections concern the English glosses for matching Greek words.

### Numbers 3

The census counts Levites from one month old and upward (3:15, 22, 28, 34, 39). The same lower bound governs the count of Israel’s firstborn (3:40, 43). Both editions now give ἐπάνω its inclusive sense in all seven places. At 3:8 and 3:31 the Levites have charge of the tent’s equipment. ADLXX 3:27 names Izhar, one of Kohath’s sons in 3:19. The former gloss “Issachar” identified the wrong ancestor. At 3:47 and 3:50 the adjective “holy” or “sacred” qualifies the monetary unit used for redeeming the excess firstborn.

At 3:3 ADLXX uses an active verb in the expression for consecrating the priests’ hands. At 3:32 Eleazar is placed over the Levite chiefs. At 3:40 and 3:43 both editions give “by” in the expression for counting the firstborn by name.

### Numbers 4

At 4:23, 30, 35, 39, 43 and 47 both editions give the service ages as twenty-five to fifty. The lower limit combines πέντε (“five”) with εἰκοσαετοῦς (“twenty years old”). At 4:3 the local Greek texts differ. ADLXX has εἴκοσι καὶ πέντε, twenty-five, while Athens has εἰκοσαετοῦς alone, twenty. Both give fifty as the upper limit.

At 4:12 the service takes place in the sanctuary. At 4:15 Aaron and his sons cover the sacred things for transport. Both editions now distinguish the place from the objects. At 4:27 the second-person future directs the addressee to enumerate the Gershonites by name. ADLXX 4:48 uses a passive participle for those counted in the total.

At 4:44 and 4:48 the verb introduces a census total. Both editions now read “amounted to” at 4:48, where “were born” previously treated the number enrolled as a number of births.

### Numbers 5

At 5:6 ADLXX’s “man or woman” applies the restitution law regardless of marital status. At 5:7 both editions identify the principal to be repaid to the wronged person, with a fifth added. Verse 8 distinguishes that payment from the ram of atonement. At 5:19 both editions identify the woman’s own husband.

At 5:27 the ADLXX database has λάθη in the clause about escaping the husband’s notice. Athens has λάθῃ. The context supports λανθάνω in both editions, and ADLXX’s earlier “stones” arose from an incorrect noun analysis. At 5:30 both editions now identify the husband as the person who presents his wife before the Lord.

### Numbers 6

The head marked by the vow is the person’s head, which must be shaved after defilement. The sudden-death clause appears at ADLXX 6:9 and Athens 6:8. Both editions refer to the defiled head again at 6:12.

At 6:5 the person under the vow lets the hair grow. At 6:20 the foreleg is a priestly portion of the ram.

### Numbers 7

At 7:3 ADLXX joins the numeral and noun for “six wagons” in one Greek token. The next word describes the wagons as covered. The earlier English “lamps” misidentified this adjective. Athens separates the numeral and noun and also reads “covered.” At 7:24 ADLXX identifies Zebulun’s leader as Eliab. At 7:14 and the eleven parallel offerings, each incense vessel accounts for ten units of gold, giving the total of 120 in 7:86.

### Numbers 8–10

At 8:24 both editions give twenty-five as the age of entry into service, with five and twenty written separately. At 8:25 the Levite withdraws from that service at fifty.

At 9:6, 7 and 10 the phrase ψυχῇ ἀνθρώπου refers to the dead body of a person. Contact with the body explains why the ordinary Passover date cannot be kept.

At ADLXX 10:13, 14, 18 and 28, ἐξῇραν describes the camps setting out. At 10:28 the previous gloss “they plundered” incorrectly introduced an act of pillage. At 10:21 both editions identify the sacred things carried by the Kohathites. At the close of the chapter, the prayer as the ark sets out appears at ADLXX 10:34 and Athens 10:35. The prayer at rest follows at ADLXX 10:35 and Athens 10:36.

### Numbers 11–13

At ADLXX 11:5 σικύους means cucumbers. Garlic appears separately at the end of the food list. At 12:8 both editions now give “mouth to mouth” for στόμα κατὰ στόμα. The following αὐτῷ refers to Moses as the person to whom the Lord speaks. At ADLXX 12:10 the cloud withdraws from the tent.

At ADLXX 13:24 the scouts bring pomegranates as well as grapes and figs. The earlier reading “streams” came from a mistaken analysis of ροῶν. The English and lemma now identify the fruit.

### Numbers 14–16

At 14:11 ADLXX now assigns the negation to οὐ only. The question asks how long the people will fail to trust the Lord. At 14:18–20 Moses appeals to the Lord’s mercy. The negative before καθαριεῖ governs acquittal of the guilty. Both editions retain “forgive” in the plea and “merciful” in the reply.

At 15:31 ἐκτρίψει is a dative noun paired with a passive verb from the same root. The former reading “shall scour” introduced an action that was absent from the clause. Both databases now identify the noun and its emphatic function.

At ADLXX 16:1 and 16:12 the Greek identifies Dathan and Abiram as sons of Eliab. “Heliah” and “Eliezer” have been corrected. At 16:31–34 the ground opens beneath the rebels and closes over them.

### Numbers 17–19

Aaron’s staff blossoms at ADLXX 17:23, corresponding to Athens and ABP 17:8. The plague in ADLXX 17:12–15 corresponds to Athens and ABP 16:47–50.

At 18:21 the ADLXX publisher’s chapter text and the ADLXX database have δώδεκα (“twelve”) immediately before “every tithe.” Athens has δέδωκα (“I have given”), and the ABP Greek agrees with Athens. The ADLXX wording leaves the clause without the expected finite verb. This is a discrepancy in the published Greek, outside the matching-word comparison. The available evidence does not establish a manuscript origin. At 18:21 and 18:31 the tithe is given in return for the Levites’ service.

At ADLXX 19:4 the verb ρανεῖ directs Eleazar to sprinkle the heifer’s blood. The former gloss “he will seal” misidentified the action. At 19:16 and 19:18 both editions identify one slain as a source of corpse impurity.

### Numbers 20–22

In 20:8 the Lord tells Moses and Aaron to speak to the rock and bring forth water. At 20:12 both editions address Moses and Aaron in the plural and give their failure to trust the Lord as the reason they will not bring the congregation into the land. The plural verb at 20:24 also addresses both men.

ADLXX 21:18–19 repeats Manthanaein at the end of one leg of the journey and the start of the next. Both English glosses now identify the same place. The next destination after Bamoth is Ἰανήν (Janen) in ADLXX 21:19 and Νάπην in Athens 21:20. These are different Greek readings at corresponding points in the itinerary.

At 22:29 Balaam says that if he had a sword he would have pierced the donkey. At 22:34 he offers to turn back.

### Numbers 23–25

At 23:5 God puts a word in Balaam’s mouth. At 23:20 the emphatic negative makes Balaam’s refusal to reverse the blessing a declaration. At 24:13 he likewise declares that he will say what God tells him.

At 25:12 both editions give a covenant of peace to Phinehas. Athens also explicitly calls it “my covenant.” At 25:13 the local Greek texts differ in the ending of the adjective for “perpetual.” ADLXX’s nominative αἰωνία qualifies the covenant; Athens’s genitive αἰωνίας qualifies the priesthood. The different grammatical attachments should be preserved in English.

The rare passive infinitive at 23:19 remains an open lexical question. The local provisional gloss is “to be deceived”; ABP gives “to waver.” The agreement of the two editions on the Greek does not settle the sense.

Liddell–Scott–Jones, s.v. διαρτάω, records the active sense “mislead, deceive” and cites Menander. This independently supports the passive “to be deceived” as a possible reading. The entry does not determine which sense the translator intended in Numbers. [Perseus LSJ](https://logeion.uchicago.edu/διαρτάω)

### Numbers 26–28

At 26:2 and 26:4 the military census begins at twenty years of age; the separate Levite count at 26:62 begins at one month. Both editions now give ἐπάνω as “upward” in these formulas. ADLXX 26:9 identifies Dathan and Abiram as sons of Eliab.

At 27:17 the requested successor is to lead the congregation out and lead it in. The paired verbs express his responsibility for the people, described in the next clause as sheep needing a shepherd.

At 28:13, 21 and 29 the repeated δέκατον distributes one tenth to each lamb. At 28:15 the local Greek uses a passive verb for presenting the offering.

At Numbers 29:14–15 the flour measures apply to each animal. Each bull receives three tenths, each ram two and each lamb one. In ADLXX 29:11 the article before ὁλοκαύτωσις had been glossed “He.”

At Numbers 30:15 (ABP 30:14), both editions now gloss the two occurrences of στήσει as “he confirms.” The husband’s silence confirms the woman’s vows and obligations.

At Numbers 31:49 the officers report that “not even one” man is missing. At 31:50–51 both editions now use “article” for σκεῦος. The inventory includes gold bracelets and rings, which “vessel” would exclude.

At 2 Kings 8:13 (4 Kingdoms 8:13), Elisha tells Hazael that he will reign over Syria. Both interlinears now render ἐπὶ Συρίαν as “over Syria.” The singular place name identifies his realm.

At Numbers 31:23 both occurrences of διά govern a genitive and mean “through,” first through fire, then through water. Athens has an additional οὐ before the final verb where ADLXX and the aligned ABP text have no negative. The preposition correction applies to both editions. The difference in the final clause belongs to the Greek witnesses.

At Numbers 31:28 the assessed unit, μίαν ψυχήν, is one living being in five hundred. The list includes people, cattle, sheep and donkeys. Both editions previously glossed ψυχήν too narrowly as “a person.”

At Numbers 31:17–18 both editions previously gave “company” for ἀπαρτία. The context includes people counted among the property taken. Both editions now give “chattel,” the sense also found in ABP and Peter Flint’s translation in [NETS Numbers](https://ccat.sas.upenn.edu/nets/edition/04-num-nets.pdf).

At Numbers 32:17 the promised destination is the other Israelites’ own place. Both editions previously read “our own” for ἑαυτῶν. At 32:36 the structures are sheepfolds, while at 32:41 the same noun denotes settlements. ADLXX 32:42 names the captured town Καὰθ (Kaath), corresponding to Athens Κανὰθ (Kenath). The former ADLXX gloss “of Kohath” mistook the town for a person and made the direct object a genitive.

In the itinerary of Numbers 33, ἀπῇραν marks departure from a station and παρενέβαλον marks the next encampment. For εἰς immediately following the latter verb, “camped at” conveys the relationship to the named station in English.

Three ADLXX itinerary glosses confused place names with unrelated words or people. Numbers 33:7 locates the camp opposite Baal-zephon. At 33:15 the Israelites depart from Raphidim, the station named in 33:14. At 33:42 they arrive at Phinō (ABP Punon), the station they leave in 33:43. The previous glosses were “of Beelzebub,” “of the reeds,” and “Phinehas,” respectively.

Numbers 33:53–54 specifies distribution by lot. In 33:55 ADLXX καταλίπητε is from καταλείπω, “leave behind.” Its previous lemma and gloss (“you may seize”) reversed the condition in the warning. At 34:4–5 Azmon marks the southern boundary, distinct from Hashmonah in the earlier itinerary. At 34:8 ADLXX Ἐμάθ identifies Hamath on the northern boundary.

At Numbers 35:30 the shared preposition διά introduces witness testimony. Athens reads διὰ στόματος μαρτύρων (“by the mouth of witnesses”); ADLXX reads διὰ μαρτύρων (“by witnesses”). Athens also has third-person φονεύσει, where ADLXX has second-person φονεύσεις. The cached ABP interlinear pairs the third-person Greek with second-person English. The local glosses follow each edition’s verb.

At Numbers 36:5 Moses addresses Israel and then affirms the claim of Joseph’s descendants. The cached ABP page correctly prints the second name as Ἰωσήφ but labels it “of Israel” in English. Both local editions retain Joseph and now mark the relationship as “of Joseph.”

Deuteronomy 1:1 names Pharan (Paran) among the places where Moses addresses Israel. ADLXX formerly read “Pharao.” At 1:7 the geographic list includes the Arabah, formerly glossed “the Arabs” in ADLXX. At 1:38 the land is the object of κατακληρονομήσει and Israel the recipient. Joshua “will allot” the land to Israel.

Athens 1:38 uses a different verb, κατακληροδοτήσει, for causing Israel to inherit. Both clauses make Israel the recipient.

In Deuteronomy 2:5, 9 and 19, ἐν κλήρῳ describes land given as an inheritance. At 2:19 σοι marks the would-be recipient in the negative clause: the Lord will not give the Ammonites’ land “to you.” At 2:20 ADLXX has the same indeclinable name twice. The territory is “of the Rephaim,” and “the Rephaim” are the people who formerly lived there.

At Deuteronomy 3:11 πλήν restricts the statement about Og: “only” Og remained of the Rephaim. At 3:17 ADLXX twice names the Arabah in the description of the Jordan boundary. “Arabia” previously obscured the geographic reference.

At Deuteronomy 4:31 ADLXX οὐδὲ μὴ ἐκτρίψῃ is an emphatic negative assurance: the Lord will not destroy Israel. The old gloss “may he crush” obscured the force of the clause. At 4:35 ADLXX has ἔτι (“else” here) and Athens ἄλλος (“another”). Both deny that there is any other God besides the Lord. At 4:39 both editions use ἔτι.

At Deuteronomy 5:4 πρόσωπον κατὰ πρόσωπον means “face to face.” At 5:11 both occurrences of ἐπὶ ματαίῳ now give “in vain.” At 5:22 πᾶσαν describes the whole assembly that heard the commandments.

At 6:7 ADLXX διανιστάμενος means “rising,” paired with lying down. The prior gloss “leading” obscured the daily sequence. At 6:16 the repeated verb concerns putting the Lord to the test.

At Deuteronomy 7:7 ADLXX προείλετο means “he chose for himself.” The identical form in 7:6 already carried that sense. The old 7:7 gloss “he foretold” obscured the argument: the Lord chose Israel out of love and fidelity to his oath, despite Israel’s small numbers. Athens has the corresponding προείλατο in both verses.

At Deuteronomy 8:3 both halves use ἐπί to identify what sustains human life: “by bread” and “by every word.” At 8:8 the ADLXX list of produce had “flow” between figs and olives. The noun ροαί here means “pomegranates.”

Deuteronomy 9:4 in ADLXX ends with the warning against claiming Israel’s righteousness as the reason for the gift of land. Athens continues in the same verse with a clause about the nations’ impiety. Both editions make that point in 9:5. At 9:28 ADLXX αὐτούς is the object of the final infinitive in the accusation Moses fears the Egyptians might make. The gloss now reads “them.”

At Deuteronomy 10:11 ADLXX βάδιζε is the Lord’s command to Moses, “go.” The former gloss “I said” changed the speaker and removed the command. At 10:15 the object of ἀγαπᾶν is αὐτούς, “them,” referring to the fathers. The former ADLXX “himself” reversed the relationship.

At Deuteronomy 11:6 the local editions identify Eliab as the father of Dathan and Abiram. ADLXX had glossed the name Ἑλιάβ as “Eliasab.” At 11:10 σπόρον is the seed being sown in Egypt; the former ADLXX “sowing time” gave the object a temporal sense.

At Deuteronomy 12:1 and 14:23, both editions now gloss ἡμέρας as “days” in πάσας τὰς ἡμέρας, “all the days.” The ADLXX correction at 12:1 follows its own Greek and is outside the direct ABP decision count. At 1 Samuel 29:3, both editions retain singular “day.” There ἀφ᾽ ἧς ἡμέρας means “from the day when,” and the singular relative fixes the number despite the same noun spelling.

Deuteronomy 12:3 gives two ways of describing the removal of the gods’ name. ADLXX reads ἀπολεῖται, “will perish,” with “the name” as subject. Athens reads ἀπολεῖτε, “you shall destroy,” with “the name” as object. The cached ABP alignment pairs the ADLXX form with second-person English. Each interlinear retains the person and voice of its own Greek. At 12:2 the gloss “mountains” for ὀρέων preserves the distinction from the hills listed later in the verse.

Deuteronomy 12:6 and 12:11 repeat ἀπαρχὰς in the lists of gifts. Both interlinears now use “first offerings” in both verses. The former “heave offerings” introduced a lifting motion that the Greek noun does not specify. At 12:10, καταπαύσει has Israel as its direct object. “Shall give rest” preserves what God does for the people when he settles them in the land.

At Deuteronomy 12:14, αὐτόν refers to the place the Lord chooses. The masculine pronoun agrees with τόπον and takes “it” in English. At 12:18, the Lord chooses the place “for himself.” In 12:21, ὃν τρόπον introduces the manner in which Moses commanded the people to act. At 12:26, ADLXX γένηταί σοι refers to sacred things that come to be in the hearer's possession. The old gloss “is born” suggested a restriction to offspring absent from the Greek.

ADLXX Deuteronomy 13:15 opens the inquiry into a reported act of apostasy. The verb ἐτάσεις, followed by “you shall ask” and “you shall search,” means “you shall investigate.” The former “you will stretch” lost the first instruction. Athens 13:14 has the longer form ἐξετάσεις at the same point. At ADLXX 13:18 (ABP 13:17), the Lord remains the subject throughout the prayer that he turn from anger and grant mercy. The gloss of δώσῃ now reads “he may give.” The earlier reference to the hearer’s hand belongs to a different clause.

Deuteronomy 14:6–8 distinguishes divided hooves and chewing the cud. The gloss “claws” for ὀνυχιστῆρας obscured the hoof test. At 14:5, LSJ identifies πύγαργος as the name of a white-rumped antelope and explicitly cites this verse. At 14:12 it gives “sea-eagle” for ἁλιάετος and qualifies the identification with the osprey as probable. The local gloss retains that broader identification. The animal decisions record the specific lexical grounds at each position. [Liddell–Scott–Jones, Perseus digital edition](https://github.com/PerseusDL/lexica/tree/master/CTS_XML_TEI/perseus/pdllex/grc/lsj)

At ADLXX 14:22, the field produces a crop each year. The gloss for γένημα now reads “produce.” At 14:25, the masculine pronoun αὐτόν refers to the chosen place, a masculine noun in Greek. Both English interlinears now read “it.”

Deuteronomy 15:1 sets the interval for release: δι᾽ ἑπτὰ ἐτῶν means “every seven years.” In 15:9 the needy brother who has been refused help may cry to the Lord κατὰ σοῦ, “against you.” The old “according to” obscured whom the complaint concerns. Both editions now preserve that relationship. At 15:21 πονηρός qualifies a physical defect in an animal offered for sacrifice. “Serious” gives the sense of the defect in this context.

Deuteronomy 16:6 fixes the hour of the Passover sacrifice. ADLXX δυσμάς and Athens δυσμαῖς both refer to the setting of the sun here. The former “the west” suggested a direction. The ADLXX word has a direct ABP match. The Athens correction follows its own Greek form. At 16:19 the genitives σοφῶν and δικαίων identify whose eyes bribes blind and whose words they take away: the eyes “of the wise” and the words “of the righteous.”

At Deuteronomy 17:7 and 17:12 both editions have τὸν πονηρόν. The masculine article identifies the person who committed the offense, and the gloss now reads “evildoer.” Compare the neuter τὸ πονηρόν at ADLXX 13:6 and Athens 13:5, where the object is “evil.” At 17:20 the warning concerns the king raising his heart “above” his brothers. The comparison defines the relationship the law is intended to prevent.

At Deuteronomy 18:16, Moses recalls what Israel asked of the Lord at Horeb. ADLXX word 4, ἠτήσῳ, was tagged as an adjective and glossed “all,” although πάντα already expresses “all” at word 2. The revised gloss “you asked” restores the verb. The ADLXX surface spelling is preserved. Athens reads ᾐτήσω at the same position. At 18:20 προσέταξα, “I commanded,” makes the Lord the speaker in the test of prophetic authority.

At 18:22 the closing clauses differ. Athens reads οὐκ ἀφέξεσθε ἀπ᾽ αὐτοῦ. ADLXX reads οὐκ ἐφέξεσθε αὐτοῦ, with a different verb form and no intervening preposition. The ADLXX pronoun refers to the prophet and now reads “him.” The pronoun and the negative have direct ABP matches in ADLXX. The differing ADLXX verb falls outside the matching-word comparison.

At Deuteronomy 19:5 τύχῃ marks the accidental blow when the iron comes off the wooden handle. “Happens to strike” preserves the chance event that makes this a case for refuge. At 19:11 the assailant lies in wait and rises against the victim. At 19:19 the two editions use the same adjective with different articles. Athens τὸν πονηρόν identifies the evildoer. ADLXX τὸ πονηρόν identifies the evil. The matching adjective alone cannot settle the English choice.

In Deuteronomy 20:5–9 γραμματεῖς recurs for the scribes who address the people about returning home. The consistent gloss “scribes” distinguishes them from the leaders mentioned after their speech in 20:9. At 20:11 εἰρηνικά describes how the town replies: “peaceably.” ADLXX then has ἐν αὐτῇ, “in it,” referring to people found in the town. The former gloss “for it” misplaced the force of the dative after ἐν.

At Deuteronomy 21:4 and 21:6 both editions use forms of νευροκοπέω for the heifer. The former glosses referred to breaking its neck. ABP and LSJ support “hamstring” for the Greek verb, which occurs first as a command and then as a description of the same animal. At 21:8 the elders ask the Lord to be merciful to the people he redeemed. The concluding passive ἐξιλασθήσεται refers to atonement for the bloodshed. At 21:17 τούτῳ marks the firstborn as the one to whom the birthright belongs. [Liddell–Scott–Jones, Perseus digital edition](https://github.com/PerseusDL/lexica/tree/master/CTS_XML_TEI/perseus/pdllex/grc/lsj)

At Deuteronomy 22:8 the final pronoun refers to the roof from which someone might fall. At 22:9 γένημα is agricultural produce. At 22:26 the woman bears no guilt warranting death. The analogy compares the assailant’s act to murdering a neighbor. In ADLXX 22:27 the English entry for οὐκ previously contained the placeholder “(with the verb),” while the verb itself was glossed “was.” Restoring “not” makes explicit that no one was there to help her. This last correction was made from the local Greek outside the direct ABP comparison.

At ADLXX Deuteronomy 23:6 and Athens 23:5, the Lord refuses to heed Balaam, turns the curses into a blessing, and loves Israel. At the last Κύριος in the verse, the cached ABP English field contains a formatting fragment. Both interlinears retain “the Lord” on the evidence of their Greek. The ledger marks this specific ABP gloss as unusable.

At ADLXX 23:15 (Athens and ABP 23:14), the Lord is present “to rescue” Israel. The next infinitive in ADLXX is παραδοῦναι, “to hand over,” with the enemy as object. Both ADLXX infinitives previously read “to deliver,” obscuring the change of object and sense.

At Deuteronomy 24:11 ADLXX writes τὸδάνειόν as one token. The former gloss “the giving” and its participle analysis obscured the loan. The entry now reads “the loan” and identifies the noun δάνειον. Athens prints the article and noun separately. This correction comes from the local Greek outside the one-word ABP alignment.

At 24:13 the creditor returns the debtor’s pledged garment. At 24:15 the same form ἀποδώσεις takes a different object, the laborer’s wage. Both editions now gloss it “shall pay” there. If the wage is withheld, the laborer can cry to the Lord κατὰ σοῦ, “against you.”

At Deuteronomy 25:1 the object of the verdict differs by one letter in the article. Athens τὸν δίκαιον identifies the person in the right. ADLXX τὸ δίκαιον identifies what is right. At 25:6 the editions again differ in grammar: ADLXX τέκῃ describes the woman bearing the child, and Athens τεχθῇ describes the child being born. The direct-word comparison records the shared παιδίον as “child” in both editions. At 25:13–15 the Greek distinguishes a weight kept in a bag from a measure kept in a house and calls each one true and just.

At Deuteronomy 26:8 both interlinears formerly glossed ὁράμασι as “terrors.” The noun means “visions” and is distinct from the signs and wonders that follow. At 26:14 the worshiper says ἐποίησα, “I have done,” and addresses the Lord with ἐνετείλω, “you commanded.” The cached ABP English assigns this last verb a third-person subject, although the aligned Greek form is second person in both editions. At 26:18 περιούσιον describes Israel as the Lord’s treasured people, as in 14:2.

At Deuteronomy 27:15 Athens τεχνίτου and the matching ABP entry refer to the hands of a single craftsman. ADLXX τεχνιτῶν is plural, “of craftsmen.” The latter correction follows the local Greek outside the one-word ABP match. At 27:16 both editions retain “be it so” for the people’s γένοιτο. Its optative expresses their assent to the declaration. At 27:24 the dative δόλῳ describes how a neighbor is struck, “by deceit.”

Deuteronomy 28:12 illustrates a limit of accent-insensitive matching. In the blessing of the work of Israel’s hands, ADLXX εὐλογήσαι is accented as a wish, “may he bless.” Athens εὐλογῆσαι has the infinitive accent, “to bless,” agreeing with the cached ABP English. At the end of the verse both editions have σοῦ as the complement of “they shall rule.” Both now read “over you.” An earlier review had confirmed the identity of the pronoun without accounting for its role in that clause.

At Deuteronomy 28:20 ἐκλιμία denotes the sufferer’s extreme hunger. At 28:22 both editions retain “mildew” for ὤχρα. LSJ cites these very verses for the respective senses. Athens also lists φόνῳ, “slaughter,” between inflammation and wind blight. ADLXX proceeds directly from inflammation to wind blight. This difference in the list belongs to the Greek texts. [Liddell–Scott–Jones, Perseus digital edition](https://github.com/PerseusDL/lexica/tree/master/CTS_XML_TEI/perseus/pdllex/grc/lsj)

At Deuteronomy 28:44 the resident foreigner lends to Israel. ADLXX repeats the clause denying that Israel will lend to him. Athens states it once. At 28:45 both editions read ἐνετείλατο, “he commanded,” referring to the Lord. The cached ABP English gives the first person for the matching form. At 28:59 θαυμαστάς describes the blows as astonishing. The earlier “wonderful” could suggest that the speaker welcomed them.

At Athens Deuteronomy 29:4 and ADLXX 29:3, both editions give the heart εἰδέναι (“to know”) and the eyes βλέπειν (“to see”). Keep that distinction when checking the English against ABP. At Athens 29:6 the demonstrative οὗτος points to the Lord. ADLXX 29:5 instead closes with the explicit first-person pronoun ἐγώ. Each interlinear follows its own Greek wording.

At Athens Deuteronomy 29:19 and ADLXX 29:18, ὅσιά μοι γένοιτο is a wish uttered by the person who hears the curse. Both interlinears now give ὅσια the contextual gloss “blessings.” The closing verb συναπολέσῃ is active, with the sinner as subject and the sinless person as object. At Athens 29:26, διένειμεν retains “allotted.” It concerns the allocation of the other gods, while the preceding verb ἠπίσταντο already expresses knowing.

At Deuteronomy 30:9, both editions have πολυωρήσει σε. The Lord will care for Israel in its work, children, livestock and crops. The earlier gloss “shall multiply” obscured the verb’s sense in a verse about prosperity. At 30:19, γῆν is “earth” in the pair “heaven and earth” called as witnesses. In 30:18 the same noun refers to the land Israel is crossing the Jordan to possess.

At Deuteronomy 31:7 both editions distinguish two imperatives in the charge to Joshua. The glosses “take courage” (ἀνδρίζου) and “be strong” (ἴσχυε) preserve both. At 31:16 the Lord addresses Moses directly about sleeping with his fathers. The second-person gloss “you are going to sleep” keeps Moses distinct from the people whose future conduct the Lord then describes. At 31:19 ADLXX has the future ἐμβαλεῖτε, while Athens has the imperative ἐμβάλετε in the charge to put the song in the people’s mouths.

At ADLXX Deuteronomy 32:1, ΠΡΟΣΕΧΕ addresses heaven directly. The earlier “he looks” gave the verb a third-person subject. The corrected “give heed” restores the opening imperative. At 32:10 both editions now gloss κόρην ὀφθαλμοῦ as “pupil of an eye.” At ADLXX 32:11, ἐπεπόθησε describes the eagle yearning for its young. The next phrases supply the physical movements of spreading its wings and lifting the young.

At Deuteronomy 32:33 the preceding verse’s bitter grapes supply the setting for the wine compared to serpent venom. Both occurrences of θυμός in each edition now read “venom.” At 32:39 the doubled command to see introduces a declaration with ὅτι. Rendering the conjunction “that” makes what follows the substance of the command.

At ADLXX Deuteronomy 33:7, εἰσέλθοισαν is a third-person plural optative. “May they enter” restores the petition in the blessing of Judah. Athens reads εἰσέλθοις ἄν, with a second-person singular verb. At 34:6 both editions use ἔθαψαν, third-person plural, for the burial of Moses. “They buried” preserves the number while leaving the agents unnamed.

At ADLXX Joshua 1:6, ἀποδιελεῖς is a future verb with the land as its object. Joshua “shall divide” the land among the people. The previous gloss “you investigated” missed both the action and its tense. At 1:7 both editions name Moses as the subject of ἐνετείλατο, so the English keeps the third person even where the aligned ABP gloss supplies a first-person subject. At 1:18, ἀποθανέτω is a third-person imperative in both editions.

At Joshua 2:1 and 3:1, ADLXX spells the departure point Σαττίν. Both entries now read “Sattin,” replacing “Sychar” in the scouts’ departure and “of Satta” in Israel’s departure. Athens consistently renders its spelling Σαττείν as “Sattein.” At 2:19, γένωνται concerns the people who are with Rahab inside her house when the city is taken. The earlier gloss “are born” introduced a condition absent from the oath.

At Joshua 4:7, ἐξέλιπεν describes what happened to the river when the ark crossed. “Ceased flowing” gives the sense of the earlier gloss “failed.” At 5:12, τὴν χώραν τῶν Φοινίκων identifies the country by its inhabitants. The interlinear now gives Φοινίκων as “of the Phoenicians.” The preceding clauses explain why manna ceased when Israel began eating the grain of the land.

At Athens Joshua 6:16 and ADLXX 6:17, περιποιήσασθε is followed by αὐτήν, referring to Rahab. The command is to spare her, and it extends to all who are in her house. The former gloss “keep yourselves” assigned the action to the wrong object. At Athens 6:18 and ADLXX 6:19, θησαυρόν designates the treasury where the metals dedicated to the Lord are to be brought.

At Joshua 7:12, ἐγενήθησαν ἀνάθεμα describes Israel’s changed standing after the theft. Both editions now gloss the verb “became.” At 7:25, Κύριος supplies the subject of ἐξολοθρεύσαι in Joshua’s address to the offender. The English now conveys the wish “may he utterly destroy,” with the Lord identified in the next word.

At Joshua 8:25, the subject of ἐγενήθησαν is “those who fell,” and the following numeral supplies their total. Both interlinears now read “numbered” where they previously read “were born.” At 8:1, the perfect δέδωκα retains “I have given” in the Lord’s address to Joshua. At 8:23 the Greek συνέλαβον has the captors as its grammatical subject, so the active “they seized” is appropriate even where the aligned ABP English uses a passive.

At ADLXX Joshua 9:5, εὐρωτιῶν describes the condition of the Gibeonites’ bread. “Moldy” replaces “pleasant.” Athens 9:5 describes the loaves as dry and eaten away and has no corresponding word for mold. At 9:13, the wineskins are the subject of ἐρρώγασι, a perfect form of ῥήγνυμι. ADLXX now reads “have burst,” agreeing with Athens. The earlier “they water” obscured the evidence the visitors offered for their supposed journey. ADLXX’s lettered passage at 9:2 also aligns with ABP 8:30–35, the altar and the reading of the law. The ledger keeps the separate addresses.

At Joshua 10:13 both editions twice read ἔστη with the sun as subject. “Stood still” replaces “was established” in both clauses. The surrounding Greek differs: Athens has ἔθνος as the subject of ἠμύνατο and includes a question about what is written in the book of the upright. ADLXX has ὁ Θεός as the subject and proceeds directly to the repeated statement about the sun. The shared verb can be checked across editions without adding the book reference to ADLXX.

At Joshua 10:23 both editions name the fifth king’s city Ὀδολλάμ (Odollam). The aligned ABP English gives Eglon. At 10:36 Athens explicitly names Eglon as the departure point for Hebron, while ADLXX simply says that Joshua and Israel went to Hebron. At 10:34 both editions name Odollam as the destination but use different closing verbs: ADLXX has ἐξεπολιόρκησεν (“he took by siege”), and Athens has the imperfect ἐπολιόρκει (“he was besieging”). Each gloss follows the form in its own edition.

At Joshua 11:10 the repeated ADLXX place name Ἀσώρ is Hazor in both clauses. The second occurrence, formerly “Assyr.,” identifies Hazor as the leading city of those kingdoms. At 11:20 the Lord is identified as the source of the kings’ resolve. Both interlinears now use “to strengthen” for κατισχῦσαι or κατισχύσαι, with “their heart” as its object. At ADLXX 12:13, Δαβίρ identifies the city of the king being listed. “Of Debir” replaces “David.” The totals in 12:24 differ in the Greek itself: ADLXX reads twenty-nine and Athens thirty-one.

At ADLXX Joshua 13:5, Ἐμάθ identifies Hamath in the boundary phrase “the entrance of Hamath.” At 13:21, Ροκόμ is Rekem, one of the named Midianite leaders. The earlier “Rock” and its nominative parsing obscured the personal name. Athens already identifies Rekem at the corresponding position. At 14:8, ADLXX reads καρδίαν (“heart”), while Athens reads διάνοιαν (“mind”) in Caleb’s description of the other scouts’ effect on the people.

At Joshua 15:63, the verb ἀπολέσαι means “to destroy.” Both editions say that the sons of Judah were unable to do this and that the Jebusites lived with them in Jerusalem. At 16:3 and 16:8 the sea supplies both a compass direction and a physical endpoint. “West” describes the boundary’s course, while “sea” identifies where it ends.

At ADLXX Joshua 17:15, ἐκκάθαρον is the command to clear the woodland. The next word, σεαυτῷ, supplies “for yourself.” The earlier gloss “decide for yourself” also assigned the verb to the wrong lemma. Athens has a related imperative, ἐκκαθάρισον, already glossed “clear out.” At 18:4, ADLXX διελθέτωσαν and Athens διελθάτωσαν are third-person plural imperatives. Joshua directs the representatives to go through the land and map it for the allotment.

At Joshua 20:2, δότε governs “the cities of refuge.” The command designates particular cities for that purpose. At 20:3, ψυχήν is the person struck, and ἀκουσίως states that the act was unintentional. At 20:4, “take him in” fits the assembly’s action: the fugitive receives a place in the city and lives there with them.

At Joshua 21:45, ADLXX διέπεσεν is from διαπίπτω, “fail.” With the preceding negative, the verse says that none of the Lord’s good words failed. The earlier “he ruled” lost the point of the sentence. Athens already had “failed” and explicitly supplies ῥῆμα (“a word”) as the subject. Both editions close by affirming that everything came to pass.

At ADLXX Joshua 22:31, Phinehas tells the eastern tribes “you have rescued” the sons of Israel. The verb ἐρρύσασθε is a second-person plural aorist middle indicative of ῥύομαι. The earlier command “deliver!” reversed the timing of Phinehas’s acknowledgment. Athens already reads “you have rescued.” In 23:10 both editions use the past ἐξεπολέμει for the Lord fighting for Israel; the aligned ABP English uses the present.

At Joshua 24:6 Athens reads ἐξήγαγον. Both “I led out” and “they led out” are possible in isolation. Verse 5 begins with the Lord saying “I sent Moses and Aaron,” then shifts to third-person singular verbs with the Lord as subject. A return to the divine speaker in verse 6 fits the recital. The alternative would make Moses and Aaron the implied agents. Athens now reads “I led out your fathers.” ADLXX reads ἐξήγαγε, an unambiguous third-person singular, and retains “he brought out.” The Athens correction follows its own Greek and is outside the exact-word ABP count.

In Joshua 24:26–27, the stone is large (μέγαν) and hears the covenant words as a witness. ADLXX τερέμινθον in 24:26 denotes the tree under which Joshua sets the stone. In the ADLXX ending at 24:33, Phinehas both dies and is buried. The second verb, κατωρύγη, previously duplicated the death notice. Both corrections come from the local Greek context.

Judges 1:11 uses ἔμπροσθεν of Debir’s former name. Both editions now read “formerly” where “ahead” had suggested a direction. At ADLXX Judges 1:36, ᾿Ακραβὶν names the ascent of Akrabbin. The Rock is a separate landmark (Πέτρας) later in the same verse. The ADLXX context review also restored Ashdod at 1:18, Anak at 1:20, and “drove out” for ἐξῇρε at 1:27. The last correction restores the sense of the negative clause about Manasseh’s failure to expel the inhabitants.

Judges 2:1 preserves a difference in how the messenger recounts the exodus. ADLXX has ἀνεβίβασα and εἰσήγαγον in the Lord’s speech, “I brought you up” and “I brought you in.” The earlier glosses suggested an offering and introduced plural agents. Athens has third-person singular ἀνεβίβασεν and εἰσήγαγεν at those positions and keeps “he brought up” and “he brought in.” These two ADLXX corrections follow its local Greek. At 2:19 both editions now read “acted corruptly” for διέφθειραν, with ὑπέρ introducing the comparison with the preceding generation.

Judges 3:15 identifies the deliverer as Ehud (Ἀώδ). Both editions had used “Ohad,” the name of a different biblical figure. The same correction applies to subsequent occurrences in the chapter. In ADLXX 3:22 the hilt follows the φλόγος and the fat closes over it. Both occurrences refer to the blade. In 3:26, εἰς Σετειρωθά gives Ehud’s destination. The old gloss “he was scattered” had turned the place name into a verb.

In ADLXX Judges 4:9, Deborah is the subject of both verbs in “Deborah rose and went with Barak.” The second gloss now reads “she went.” At 4:21 κροτάφῳ means the temple of Sisera’s head, as the same word does when Barak sees him in 4:22. The peg is the subject of “it passed through.” At 4:23 God “routed” Jabin. The latter two verse corrections follow the ADLXX wording and context.

At Judges 5:15 ADLXX κοιλάσιν is the dative plural of κοιλάς, “valleys.” The earlier gloss “bellys” had assigned it to κοιλία. At 5:21 the Kishon is one torrent repeated three times in each edition. The singular verb for sweeping away the enemy confirms the number. At ADLXX 5:26 the paired words σφῦραν and ἐσφυροκόπησε give Jael a hammer and describe her striking Sisera with it, as in 4:21. Both previous glosses referred to a jaw. In 5:30 βάμματα denotes dyed fabrics in the list of spoils.

The opening of the song requires separate treatment. ADLXX prints ἦσαν with λέγοντες later in the clause. Athens prints εἶπεν and expressly mentions the song. ABP’s English “sang” alone cannot establish a manuscript reading or justify changing either local Greek text.

At Judges 6:13 Gideon asks where the Lord’s wonders are and recalls the exodus. ADLXX ἀνήγαγεν means “brought up,” replacing “levied.” In both editions the last ἐν in that verse introduces Midian’s hand. At 6:15 Gideon’s initial ἐν ἐμοί introduces a plea, but the subsequent occurrences of ἐν ask by what means he can save Israel and locate his clan in Manasseh and himself in his father’s house.

ADLXX 6:28 describes Baal’s altar as already torn down (καθῄρητο). The previous gloss “was purified” lost the action that prompts the investigation. At 6:32 ADLXX names Jerubbaal, while Athens prints δικαστήριον τοῦ Βάαλ, “judgment seat of Baal.” At ADLXX 6:37–38 the fleece is made of wool and Gideon squeezes it. The previous glosses “of love” and “he cleansed” obscured the sign. These corrections follow the local Greek.

At Judges 7:13–15 the dream and its interpretation are distinct. In ADLXX 7:13 the loaf overturns the tent. At 7:15 Gideon hears the telling (ἐξήγησιν) of the dream and then its interpretation (σύγκρισιν). At 7:16 both editions use ἀρχάς for the three companies into which Gideon divides his men. At ADLXX 7:20 λαμπάδας denotes the torches the men hold, the same objects placed in jars at 7:16. The previous “flashes of lightning” had changed the scene.

At ADLXX Judges 8:22 the Israelites ask Gideon, “Rule over us.” The previous “begin!” for ἄρξον missed the request for hereditary rule. Gideon uses the same verb three times in his answer at 8:23, reserving rule for the Lord. Athens reads ἄρχε ἐν ἡμῖν, “rule among us.” The constructions differ, but both use the governing sense of ἄρχω. At ADLXX 8:26 μηνίσκων denotes crescent ornaments among the spoils, as the reference to the camels’ ornaments at 8:21 helps confirm.

At Judges 9:15 the speaker is the bramble in both editions. The old ADLXX gloss “stream” obscured Jotham’s warning that fire could come from the very plant offering the other trees shade. At 9:26 ADLXX calls Gaal the son of Jobel (᾿Ιωβὴλ), while Athens calls him the son of Abed (Ἀβέδ). The former ADLXX gloss “jubilee” mistook his father’s name for a common noun. At ADLXX 9:53 the woman breaks Abimelech’s skull: ἔκλασε is from κλάω. “She wept” had assigned the verb the wrong meaning.

At Judges 10:1–2, ADLXX names Shamir (Σαμίρ) as Tola’s residence and burial place. Its earlier English “Samaria” obscured a difference between the editions. Athens explicitly reads Σαμαρείᾳ at 10:1, supporting “Samaria” there. At ADLXX 10:4 the sons are riding colts, and the plural subject of ἐκάλουν gives “they called” the towns Jair’s settlements. The earlier first-person gloss introduced a speaker into the narrative.

In Judges 11:2 the brothers tell Jephthah he will have no inheritance in their father’s house. Both editions had glossed ἐν as “please.” The preposition takes the dative and means “in” here. In 11:11, by contrast, εἰς introduces the office to which the people appoint him. “As head” gives the sense of εἰς κεφαλήν. Both corrections concern the English gloss.

At Judges 11:20 Athens has διὰ τῶν ὁρίων αὐτοῦ. Sihon refuses passage *through* his territory. The previous gloss “from” reversed the sense of the route. At 11:24 Athens uses κατεκληρονόμησε twice, with the recipients σοι and ἡμῖν. “Allotted” preserves the parallel between what each people receives. ADLXX uses different verbs in that verse and needs its own reading.

Judges 11:26 locates the cities beside the Jordan. Both editions read παρὰ with the accusative, and the earlier gloss “from” suggested a point of departure. At 11:33 πληγὴν describes the blow struck in battle. The old gloss “plague” suggested disease. In Jephthah’s vow (11:31), Athens has plural θυρῶν and ADLXX singular θύρας. The Athens gloss now preserves “doors.”

At ADLXX Judges 12:4, συνέστρεψεν takes “all the men of Gilead” as its object. Jephthah gathered the men. The earlier “conspired” obscured the action. At 12:6 the guards seize and slaughter a fugitive at the Jordan crossings. The old gloss “they sacrificed” for ἔθυσαν introduced a ritual sense unsupported by the scene. These two corrections came from reading the AD clause. At 12:12 AD uses Αἰλὼμ twice, first for the judge (Elon), then after ἐν for the burial place (Aijalon). The Greek spelling is preserved at both positions.

In ADLXX Judges 13:3, συλλήψῃ υἱόν promises conception to the woman just described as barren. The earlier “you will take” missed the announcement. At 13:8, Manoah asks that the visitor return and instruct the parents. The third-person singular imperative συμβιβασάτω had been glossed “let us join.” At 13:10 the wife runs, then reports that the man has appeared to her. These corrections came from the local clauses. At 13:19, Athens reads θαυμαστὰ ποιοῦντι, whereas AD reads διεχώρισε ποιῆσαι. An English rendering based on the Athens participle cannot settle the sense of the AD expression.

At ADLXX Judges 14:13, the wager specifies thirty ὀθόνια, linen garments. The draft’s “shekels” turned clothing into money. The challenge in 14:12 and the reply in 14:13 repeat the verb for posing a riddle. At 14:14 AD opens with τί βρωτόν, asking what edible thing came out of the eater. Athens repeats ἐξῆλθε in the two halves of its riddle. The repeated verb is explicit in Athens and understood in the second half in AD.

ADLXX Judges 15:3 had glossed ἠθώωμαι as “I wish.” Samson claims to be blameless in what he is about to do to the Philistines. At 15:8 and 15:11 τρυμαλιά describes the cleft of the rock of Etam. Treating it as a second place name in verse 11 obscured the return to the same spot. At 15:17 both editions give the place name Ἀναίρεσις σιαγόνος. We chose “removal of the jawbone” in light of Samson throwing it from his hand. The former “slaying” connected the name with the preceding combat.

At ADLXX Judges 16:3, Samson carries away the gate with its two doorposts. The draft’s “guards” for σταθμοῖς changed what he carried. At 16:13–14 the same noun, διάσματι, describes the warp both when Samson gives the instructions and when Delilah weaves his locks. The earlier glosses “the fleece” and “of the partition” hid that repetition. At 16:25 AD uses ἐρράπιζον for striking Samson. Athens uses ἐνέπαιζον for mocking him. The AD gloss “they were slapping” preserves that difference.

In ADLXX Judges 17:2, Micah recalls the curse his mother uttered about the missing silver. The draft’s “you deceived” missed the sense of ἠράσω. At 17:5 Micah makes an ephod and teraphim. Reading ἐφὼδ as “a courtyard” had introduced a building feature into the list of objects. In both editions of 18:6 the priest first tells the travelers to go in peace, then speaks of the road they are traveling. The second πορεύεσθε describes their journey.

In ADLXX Judges 18:14, 18, and 20 the same two terms recur as the scouts identify the objects, the men take them, and the priest carries them away. The draft variously rendered ἐφώδ as “house,” “the wall,” and “the entrance,” and θεραφίν as “servants,” “the servant,” and “the healing.” All three lists now name the ephod and teraphim, as in 17:5. At 18:30 AD prints Γηρσὼν (Gershon) and Athens prints Γερσὼμ (Gershom). The difference in the final consonant belongs to the Greek editions.

At Judges 19:11 the servant addresses his human master, and at 19:23 the speaker is the master of the house. Both interlinears previously used the divine-style “Lord” in these positions. ADLXX 19:21 also had “they slept” for ἐνίψαντο, although the next two words name the direct object, their feet. At 19:9 AD prints ἠσθένησενἡμέρα as one token. Its two components give “the day has waned,” the father’s reason for urging the travelers to stay. The release preserves the printed token.

At Judges 20:4 the Levite begins his testimony with ἦλθον ἐγώ. The explicit pronoun resolves the verb as “I came” in both editions. At 20:7 AD reads ἑαυτοῖς (“for yourselves”), while Athens prints αὐτοῖς (“to them”). The ABP comparison is insufficient reason to impose the reflexive on Athens. At 20:10 AD’s joined token καὶχιλίους counts a thousand men per ten thousand, continuing the preceding ratios of ten per hundred and a hundred per thousand.

At ADLXX Judges 20:16, ἐξαμαρτάνοντες describes the slingers’ accuracy. The older “offending” gave a moral sense to a statement about missing a target. The separate negative remains on its own Greek token.

Judges 20:30 begins differently in the two editions. AD has ἀνέβησαν, “they went up,” while Athens has ἔταξαν, “they drew up.” The Athens draft had given the AD sense to its own verb. In Athens 20:34 disaster has already taken hold of the Benjaminites. The former gloss “has caught fire” introduced a fire into this clause before the signal appears in the narrative. In AD 20:45 Γεδᾶν marks the limit of the pursuit, “as far as Gedan.” The earlier “of Gideon” mistook the place for a person.

For Athens 20:34 the corrected lemma ἀφάπτω inherits the existing no-number entry in the Strong’s lemma table. The former occurrence override assigned 681 under ἅπτω. At 20:26 Athens prints σωτηρίου in the genitive singular after “whole burnt offerings.” Its gloss now reads “of deliverance.” AD has a conjunction and a second plural form, καὶ τελείας.

At ADLXX Judges 21:7 and 21:16, τοῖς περισσοῖς refers to the remaining men of Benjamin who lack wives. The earlier “superfluous things” lost the human referent. At 21:10 the destination is Jabesh in Gilead. “Jabbok” had substituted a river name. At 21:11 AD prints the irregular εὐδυῖαν before κοίτην ἄρσενος. The working gloss “who has known” interprets this as probable εἰδυῖαν in light of the object and the contrast with virgins. Athens has γινώσκουσαν. This AD interpretation remains provisional pending comparison with the printed AD edition.

At Ruth 1:5, the AD gloss “cheeks” for Χελαιών missed the personal name Chilion, already introduced in 1:2. At 1:21 Naomi asks why the townspeople call her Naomi after she has asked to be called Bitter. “November” had obscured the contrast. At 1:9 the online AD verse has κα’Ι where Athens has καὶ. AD tokenizes the iota separately. We read the two AD tokens together as “and” and removed the unsupported gloss “Jesus” from the iota. Both source positions remain in the database.

At Ruth 2:1–2 the AD forms Νωεμὶν and Νωεμίν both name Naomi. The former had been glossed “to Noah” and the latter “Noe'm.” Athens already identified her in both verses. At 2:2, οὗ ἐὰν introduces an indefinite relative. The paired glosses “whom” and “-ever” express Ruth’s willingness to follow whoever shows her favor. At 2:3, περιέπεσε with περιπτώσει describes Ruth coming upon Boaz’s field by chance. The existing “came upon” fits the clause.

At Ruth 2:9, Boaz has forbidden the young men to touch Ruth. AD’s gloss “to touch yourself” assigned the action to the wrong person. The middle infinitive takes σου as its object. At 2:13, Ruth addresses Boaz. The AD gloss is now “sir.” At 2:6, 2:20 (twice), and 2:22, the AD name is Naomi throughout.

Two readings affect the comparison. At 2:16, AD has φάγεται (“she will eat”) where Athens has ἄφετε (“leave”). At 2:21, AD names the young women (κορασίων) and Athens the young workers (παιδαρίων). Each gloss follows its edition. These readings establish a difference between the two printed texts. They do not establish which manuscript supplied either reading.

At Ruth 3:3 Naomi tells Ruth to put on her clothing. The AD gloss “transfer” missed the sense of περιθήσεις with clothing as its object. At 3:10 Boaz calls Ruth blessed by the Lord, and at 3:13 he promises to act as next of kin for her if the nearer relative declines. At 3:16 Athens includes τίς εἶ, “who are you?” AD has θύγατερ, “daughter,” without the question.

At Ruth 4:3 AD’s ἀγχιστεῖ names the next of kin and Νωεμίν names Naomi as the recipient of the field. The draft had “the most distinguished” and “to Ruth.” At 4:7 the sandal goes to the relative exercising the right of redemption. The commercial and family context rules out the draft’s “avenger.” At 4:10 Μωαβῖτιν describes Ruth as a Moabite woman. At 4:19 AD names Aran twice in successive generations, where Athens names Aram twice. Each genealogy retains its own spelling.

At 1 Samuel 1:2, Peninnah has children (παιδία, plural), while Hannah has no child (παιδίον, singular). Both editions retain that distinction. At 1:6 AD prints ἀθυμίαντῆς as one token. The gloss now covers both the noun “dejection” and the article introducing “distress.” At 1:8 and 1:15 the AD vocative κύριε addresses a man and is glossed “sir.” At 1:11, when Hannah addresses God, the vocative retains “Lord.” The vow’s σίδηρος is glossed “an iron razor” in both editions. At 1:17 the optative expresses Eli’s wish that God grant Hannah’s petition. At 1:20 the AD gloss “it came to belong” misread the narrative verb ἐγενήθη, now “it came to pass.”

At 1 Samuel 2:1 the subject of ἐστερεώθη is Hannah’s heart. AD’s “I was established” gave the verb the wrong person and obscured the parallel with her horn and mouth. At 2:18 AD prints βάρ where Athens has Βάδ. The ephod gives the context for “linen.” The AD gloss is contextual and its former lexical analysis as βίος (“food”) was unsupported. At 2:34 the sign is that Eli’s sons will die on one day, and at 2:36 the coin is an obol. At 2:35 AD has a singular anointed one and Athens a plural.

At 1 Samuel 3:14 both editions have ὤμοσα (“I swore”) followed by εἰ and a future passive. This is a negative oath. Both drafts had left the particle blank and glossed the verb “shall be atoned for.” The gloss now reads “shall never be atoned for,” with the particle marked as introducing the oath. At 3:21 πονηρά describes the sons’ way as evil. Its feminine singular form agrees with ὁδός.

At 1 Samuel 4:10 AD’s “wound” for πληγή understated the scale of the defeat. The clause counts thirty thousand fallen, and the gloss is now “slaughter.” At 4:15 AD gives Eli’s age as ninety, while Athens gives ninety-eight. At 4:19 AD has Phinehas’s wife weeping and Athens has her crouching. At 4:21 AD prints Οὐαὶ Βαρχαβώθ in two words, while Athens has Οὐαιχαβώθ. The child is Ichabod. The former AD gloss “Barabbas” introduced a different person.

At 1 Samuel 5:4 AD’s ῥάχις denotes Dagon’s back, and the unfamiliar term ἀμαφέθ is read contextually as the threshold. At 5:6 AD prints τὰς ναῦς, “the ships,” while Athens describes the affliction on the inhabitants’ bodies. The wording of the surrounding AD clause is difficult, but the plural form is clear. At 5:7 the speakers call Dagon their “god.” Both interlinears now distinguish that reference from the God of Israel earlier in the verse.

At 1 Samuel 6:8, 11 and 15, the unusual AD terms βερσεχθάν and ἐργάβ accompany the container holding the gold objects. Their contextual gloss is “chest.” At 6:16, AD names Ashkelon (Ἀσκάλωνα) as the rulers’ destination. The former English “Asclepius” misidentified the name. Athens reads Ekron. At 6:17 the fused AD token τῆςΓάζης supplies the Gaza entry in the list, distinct from Gath later in the verse. At 6:14 and 18, AD names the field owner Hoshea and Athens names him Joshua. AD’s Βαιθσαμυσίτου in verse 18 identifies him as a man of Beth-shemesh.

At 1 Samuel 7:2, the AD phrase ἀφ᾿ ἦς ἡμέρας ἧν describes the time elapsed from the day when the ark was at Kiriath-jearim. The glosses follow the syntax despite the printed accents. At 7:4 περιεῖλον has the Israelites as its plural subject. They removed the Baals in response to Samuel’s command. At 7:14 ἀφείλοντο describes the recovery of territory from the Philistines.

At 1 Samuel 8:3 the last verb takes “judgments” as its object. The sons accept bribes and pervert judgments. At 8:7 the people are the subject of both instances of “they have rejected.” Samuel is the first object and the Lord the second. At 8:11 the fused AD token ὃςβασιλεύσει includes the relative pronoun as well as the verb, hence “who will reign.” At 8:12 AD names commanders of hundreds first, while Athens names commanders of thousands first.

At 1 Samuel 9:3 the first occurrence of Kish identifies the owner of the donkeys. The second names the father who speaks to Saul. At 9:9 the people are the subject of the active verb ἐκάλει: they formerly called the prophet “the seer.” At 9:24 AD reads ἥψησεν, describing the cook cooking the thigh. Athens reads ὕψωσεν, describing him lifting it. The two English verbs reflect the respective Greek readings.

At 1 Samuel 10:1–2 the two AD forms of χρίω refer to the Lord anointing Saul. The glosses “has appointed” and “you anoint” obscured the anointing and, in verse 2, reversed the roles of Saul and the Lord. The sign is to take place near Rachel’s tombs (τάφοις). At 10:19 ἐξουδενήκατε describes Israel rejecting the God who saved them. The draft’s “ye have made powerless” misrepresented the accusation. At 10:27 the dissenters’ question has “you” (ὑμᾶς) in AD and “us” in Athens.

At 1 Samuel 11:1, 3, 5, 9 and 10, the indeclinable AD place name Ἰαβίς identifies Jabesh throughout the siege and relief. “Jabbok,” “Jabez” and “Jabin” introduced unrelated names. The construction “men of Jabesh” occurs both when the townsmen ask Nahash for time and when they receive the messengers’ promise of help.

At 1 Samuel 12:9 the genitive after “forgot” supplies the English direct object: Israel forgot the Lord their God. Sisera is named as commander of Jabin, king of Hazor. At 12:11–12 AD speaks of God delivering “us” and calls him “our king”; Athens addresses the people with second-person pronouns. At 12:16 the “great thing” is the sign that follows, thunder and rain at wheat harvest. At 12:25 the verb “you shall be added” ends the Greek sentence. The complement supplied in the ABP English is an interpretation.

Athens includes a regnal notice at 1 Samuel 13:1; the AD chapter begins at verse 2. At 13:15 the pronoun and participle together mean “when they arrived.” At 13:18 AD’s Σαβίμ is a place name, formerly glossed “Sabbath.” At 13:20 θέριστρον is a reaping implement in the list of tools taken to the Philistines for metalwork. The AD draft’s “veil” missed that agricultural sense.

At 1 Samuel 14:2 Saul sits under a pomegranate tree; AD’s gloss “stream” gave the wrong sense of ροάν. At 14:14 κόχλαξι denotes pebbles of the plain. At 14:18 Saul asks for the ephod in both texts, but the explanation that follows mentions the ephod in AD and the ark of God in Athens. At 14:29 the eyes are the plural subject of εἶδον: Jonathan describes how his sight returned after he tasted honey.

At 14:45 the people invoke the living Lord and swear that no hair of Jonathan’s head will fall. The second εἰ introduces the negative oath, as at 3:14. Both English drafts had left that particle blank and glossed πεσεῖται as “will fall.” At 14:49, the AD forms Ἰεσσιού and Μελχισά name Saul’s sons Ishvi and Malchishua. The former glosses “Jesse” and “Mephibosheth” identified different men.

At 1 Samuel 15:4 the AD form Ἰούδαν names the contingent of Judah in Saul’s muster; the former gloss “Joab” introduced David’s later commander. AD numbers four hundred thousand and thirty thousand of Judah, Athens two hundred thousand and ten thousand. At 15:8 AD’s Ἱερίμ, glossed “Jerim” as in verse 3, had been rendered “Jeremiah.” At 15:10 the AD formula ἐγενήθη ῥῆμα Κυρίου introduces the Lord’s word to Samuel, not a “thing.” At 15:11 παρακέκλημαι expresses the Lord’s regret over Saul’s kingship, matching μετεμελήθη in verse 35. At 15:23 AD’s θεραφίν names the teraphim paired with divination; the former gloss “therapeutic” read it as a Greek adjective. At 15:31 AD has Samuel worship the Lord and Athens has Saul.

At 1 Samuel 16:1 ὅτι gives the reason the Lord sends Samuel to Jesse: he has seen a king among Jesse’s sons. At 16:8 and 17:13 Jesse’s second son is Abinadab; both drafts had “Aminadab,” the name of Nahshon’s father. At 16:10 τούτοις refers to the seven sons, not “these things.” At 16:20 AD sends “a gomor” of bread.

At 1 Samuel 17:1 AD’s Ἐφερμέμ is Ephes-dammim, formerly “Ephraim.” AD gives Goliath’s height as four cubits and a span (17:4), Athens as six. At 17:36 David’s οὐχί asks “shall I not go,” and at 17:39 οὐ μὴ δύνωμαι states that he cannot walk in Saul’s armor; the drafts had lost the negation in the first and turned the second into a question. At 17:40 λείους describes the smooth stones. At 17:43 AD’s χείρων is “worse” (than a dog); the former gloss “bear” confused it with χείρ. At 17:49 AD’s misprinted διέθυ stands for διέδυ: the stone went through the helmet. At 17:58 AD’s misprinted Δυαίδ is David answering Saul, not “Jonathan.”

At 1 Samuel 18:22 λάθρᾳ means in secret, not “truthfully.” At 18:26 ηὐθύνθη says the proposal seemed right to David; the draft’s “was immediately done” derived it from εὐθύς. At 18:19 AD names Merab’s husband Ἰσραήλ where Athens has Adriel; each edition keeps its own reading.

At 1 Samuel 19:6 Saul swears by the living Lord that David will not die. As at 3:14 and 14:45, εἰ introduces a negative oath; both drafts had glossed the verb “he shall die.” At 19:2 Jonathan delights in David (ᾑρεῖτο), formerly “was taking.” At 19:19–23 AD’s Ναυάθ is Naioth throughout, replacing “Naphtath,” “Naphthe” and “Na'ath,” and Σεφί at 19:22 is a place name, not the Shephelah.

At 1 Samuel 20:20 and 20:36–37 Jonathan’s signal is archery: AD’s τρισσεύσω is shooting three times at the mark (ἀματταρί), and ἠκόντιζε is “shot,” not “sharpened” or “thrusting.” At 20:30 Saul says “I know” that Jonathan sides with the son of Jesse. At 20:34 Saul had decided on harm against David; “had made an end” implied David was already dead. At 20:41 David rises from beside the Ergab of verse 19, not Argob.

At 1 Samuel 21:2 and 22:9, 19 AD’s Νομβά is Nob, formerly “law,” “district” and “Nebam.” At 21:3 Φελλανὶ Ἀλεμωνί transliterates the Hebrew for an unnamed place; the draft had read it as loaves and leavened bread. At 21:4 the priest asks whether the young men have kept themselves from women, not whether they are “kept in store.” At 21:9 Goliath’s sword was wrapped in a garment in the valley of Elah. At 21:11 the servants ask “did not” the dancers sing of David. At 22:1 David goes to the cave of Adullam; AD’s draft had “Oholibah.” At 22:4 David entreats the king of Moab rather than summoning him.

At 1 Samuel 23 AD’s Κεϊλά is Keilah throughout, and at 23:19, 23:24 and 26:1, 3 AD’s Ἰεσσαιμοῦν is the wilderness of Jeshimon, not Jesse. At 23:24–25 AD’s Μαάν is the wilderness of Maon. At 24:9 David addresses Saul as “lord,” not “O Lord.”

At 1 Samuel 25:2 AD’s Μαάν is Maon in Judah, formerly “in the Gaulanitis.” At 25:11 Nabal’s future verbs form a scornful question, “shall I take … shall I give,” which the drafts had stated as agreement. At 25:28 the Lord fights the wars of David. At 25:30 ἐντελεῖταί σοι εἰς ἡγούμενον is appointing David leader, not commanding him. At 25:35 ᾑρέτισα τὸ πρόσωπον is accepting Abigail’s request. AD names Ahinoam (25:43, 27:3) with corrupt spellings, formerly “Achinos” and “Achinnach,” and Palti’s home Ῥομμά (25:44), formerly “Roman”; Athens reads Gallim.

At 1 Samuel 26:19 AD’s misprinted ὀσφανθείη is the optative of ὀσφραίνομαι, “may he smell” the offering, not “offer.” At 26:21 Saul promises he will “not” harm David again; “by no means” belongs to οὐ μή, and ἠγνόηκα is “I have been ignorant” without a negation. At 26:24 σκεπάσαι is optative in David’s wish. At 27:6 AD’s Σεκελάκ is Ziklag, formerly “Sheckel,” and at 27:12 Ἀγχοῦς is Achish, formerly “in the anguish”: AD says David was trusted by Achish, and Athens says Achish trusted David. At 27:9 Athens lacks the οὐκ of AD and says David kept the people alive; each edition keeps its own reading.

At 1 Samuel 28:10 Saul swears by the living Lord that no guilt will come upon the woman of Endor: εἰ introduces a negative oath, as at 19:6, and both drafts had stated that guilt would come. At 28:2 AD’s Ἀγχοῦς is Achish, formerly “anxiety,” and at 28:4 AD’s Σωμάν is Shunem, formerly “Socoh.” At 28:25 the meal is served to Saul’s servants, not “children.” At 29:1 Israel camps at Endor in Jezreel; the AD draft had “Israel.” At 29:6 κατὰ σοῦ is “against you,” not “according to.”

At 1 Samuel 30:1 the Amalekites attack the south (ἐπέθετο), formerly “committed herself.” At 30:17 οὐκ ἐσώθη had lost its negation under the label “(with the verb)”: none escaped except four hundred young men. At 30:24 οὐχ ἧττον ἡμῶν (Athens ὑμῶν) is a genitive of comparison, “no less than us,” and the man who stays “by” the baggage receives an equal share. At 31:2 Saul’s sons are Jonathan, Abinadab and Malchishua; the AD draft had “Melchizedek,” and both editions’ Ἀμιναδ- spelling is glossed Abinadab as at 16:8. At 31:12 the bodies are brought to Jabesh, not the river Jabbok.

At 2 Samuel 1:6, 21 Γελβουέ is Mount Gilboa, formerly “Gelboue.” At 1:9 ἐπάνω is “over”: Saul asks the man to stand over him; the AD draft had “Upper.” At 1:22 Jonathan’s bow never returned “empty”; “nothing” with the negated verb made a double negative. At 2:5 and 2:4 AD’s Ἰαβίς is Jabesh, formerly “Jabbath” and “Iabish,” and AD’s Μαναέμ is Mahanaim (2:8, 12), formerly “Manahaim” and “of Manasseh.” At 2:26 Abner asks whether the sword must devour forever; μή marks the question. At 2:30 AD prints ἐπεσκέπησαν τῶν as one token: nineteen of David’s servants were missing, not “having guarded.”

At 2 Samuel 3:17 βασιλεύειν is “to reign,” and at 3:21 Abner promises that David “will reign.” At 3:39 σκληρότεροί μου is “harsher than I.” At 4:2, 5, 9 AD’s Ῥεμμών is Rimmon the Beerothite, and at 4:4 the news came from Jezreel; the draft had “Israel.” At 4:5, 7 Ishbosheth was sleeping, not lying down, when he was killed, and at 4:11 he is a righteous man, not a “husband.”

At 2 Samuel 5:12 David’s kingdom “was exalted,” and at 5:13 sons and daughters “were born” to him; the drafts had “he was taken” and “amounted to.” At 6:2 the Lord sits enthroned “upon” the cherubim, not “in charge of” them, and at 6:3–8 AD’s Ὀζά is Uzzah, formerly “Oza” and “Ozi.” At 7:7 εἰ λαλῶν ἐλάλησα asks whether the Lord ever spoke to any tribe of Israel. At 8:2 David kept the rest of Moab alive (ἐζώγρησε), not “freed” them. Σουβά is Zobah throughout chapter 8, and AD’s Θοού and Ἰεδδουράν are Toi and his son Joram, formerly “of Tohu,” “Thou” and “Jeduthun.” At 8:13 AD reads Γεβελέμ, not the Phoenician Gebal.

At 2 Samuel 9:7 David promises that he “will restore” Saul’s land (ἀποκαταστήσω), not that he “may.” In chapter 10 AD’s Ῥοώβ is Rehob, not “Rob,” and τὸν βασιλέα Μααχά is the king of Maacah. At 11:10 a plain οὐ is “not,” not “by no means,” and Uriah does not “go down” to his house (verses 9–10, formerly “came down”). At 11:26 ἡ γυνὴ Οὐρίου is Uriah’s wife. At 12:8 the Lord “would add” more to David; “I will again” had dropped the verb. Ραββάθ is Rabbah of the Ammonites in both editions. At 13:14 Amnon “was stronger than” Tamar (AD ἐκραταίωσεν) or “prevailed over” her (Athens ἐκραταιώθη). At 13:32 μὴ εἰπάτω is a prohibition, “let not my lord say,” not “lest.” At 13:36 the king’s sons “lifted up” their voices; AD had “he struck.” At 14:21 the king acts “according to” Joab’s word, not “against” it, and tells him to “bring back” Absalom.

In 2 Samuel 15–17 Χουσί is Hushai the Archite, David’s friend, in both editions; the drafts had “Chousi,” “Chousei” and “Cushi.” At 18:21–32 the same Greek name is the Cushite messenger, and AD 18:31 now reads “Cushi.” At 15:7–8 Absalom pays the vows he “vowed” (ηὐξάμην, ηὔξατο), not prayers. At 15:16 δέκα γυναῖκας τῶν παλλακῶν are ten concubines, not “wives.” At 15:25 David tells Zadok to “take back” the ark (ἀπόστρεψον), and the Lord “will bring back” David. At 17:28 φακός is “lentils” among the foods brought to David, not a “flask.” At 18:4 the king “stood” by the gate; “was established” misread ἔστη. At 18:8 the forest “exceeded” the sword in devouring.

In 2 Samuel 19–20 the names are brought to their identity spellings in both editions: Ἀμεσσαΐ is Amasa (AD had glossed it “Ammon” at 20:6 and 20:8, and elsewhere “Amessai,” “Amesai,” “Amassai,” “Amessaios”), Βοχορί is “of Bichri” (formerly “Bochor,” “Bokhor,” “Bochur,” “Bochori,” “Bochorei”), Χερεθί and Φελεθί are the Cherethites and Pelethites (AD “Chereb,” “Phaleth”), and Βερζελλί is Barzillai. At 20:6 AD has David speak to Amasa where Athens reads Abishai (Ἀβισαεί); each edition keeps its own reading. At 19:13 David offers Amasa command “of the army” (ἄρχων δυνάμεως). At 19:35 μὴ γνώσομαι and εἰ γεύσεται are Barzillai’s questions, now “[marks a question].” At 20:8 Joab’s μάχαιρα is a sword, not a “knife,” and at 20:10 Amasa “did not guard against” it.

## Name harmonization pass

Proper names now take the familiar English form of the person or place in both editions: Gilead rather than Galaad, Boaz rather than Booz, Abner rather than Abenner, Shechem rather than Sychem. Earlier passes had sometimes retained transliterations of the Greek. AD gave Gilead 80 times and Galaad 33.

The pass changed 3,756 tokens (1,706 in ADLXX, 2,050 in Athens). Where ABP aligns one-to-one with the same Greek word, its name gave the familiar form. A spelling ABP itself uses at least twice for that lemma was left alone, so Samuel did not become Shemuel and Joseph kept its form. Forms derived from the name (Egyptian, Samarian, Levites) were not taken as new names. Where ABP has no one-to-one match, a token changed only when every aligned token of the same lemma and spelling in that book mapped to the same name. Each changed position that already had a decision was rewritten with the decision “harmonize name spelling.” Open positions received new rows.

Corrupted or Hellenized Greek spellings of the same person or place take the familiar name. Examples are Βαλλά as Bera at Genesis 14:2, Γαιδάδ as Irad at 4:18, Ἀρμαθαίμ as Ramah in 1 Samuel, and Ἠλιού as Elijah in 1–2 Kings. Where the Greek names a different place than the Hebrew, the gloss follows the Greek. At Joshua 10, Ὀδολλάμ is Adullam, although ABP gives Eglon from the Hebrew, and at Isaiah 66:19 Φούδ is Put rather than Pul. A gloss that translates a name was kept: “Life” for Eve’s name at Genesis 3:20 and “Burning” at Numbers 11:3.

A name that ABP spells only once yields to its usual spelling for that lemma. That rule never overrides a token whose own ABP word already matches ours. A first draft without this guard would have changed Bered to Bedad at Genesis 16:14 and Tirzah to Tizrah at 1 Kings 16:9; the corrected pass left those 18 positions unchanged. The verifier checked all 184,820 decisions against both releases, and Greek surfaces and word order are unchanged.

A second run widened the test to every token whose grammar calls it a proper noun or name, not only those labeled as a personal or place name, and changed 799 more tokens (569 in ADLXX, 230 in Athens). This run caught identity errors as well as spellings. AD had glossed Hezekiah as “Ezekiel” (Isaiah 38:5, 9; Jeremiah 15:4), Johanan as “John” (Jeremiah 47–50), Merib-baal as “Meribah” (1 Chronicles 8:34; 9:40), Shaphan as “Sappho” (2 Kings 22), Ahaz as “Azariah” (Isaiah 7:10), Amram as “Abram” (1 Chronicles 5:29) and Jeduthun as “Igal” (1 Chronicles 25:1). Glosses that translate a name stay, as do the English choices Judeans, Sabaoth, Cushites and Arabs, and vocatives such as “O Lord.”

## Construction batches

Three constructions that the 1–2 Samuel review kept correcting were searched across both editions. Each hit was read in its clause before any change.

- **ὅτι after knowing, hearing, seeing, saying or swearing** (328 hits, 214 changed). Examples are “they heard that Jonathan was prepared” (1 Maccabees 12:28), “remember that death will not delay” (Sirach 14:12), and the oath “as the Lord lives, that…” (2 Samuel 2:27). With τί, as in “why is it that you repaid evil for good” (Genesis 44:4), ὅτι also became “that.” “Because” was kept where the clause gives a reason, even after a verb of speaking: “Because I was afraid” (Genesis 31:31), “speak, for your servant is listening” (1 Samuel 3:9–10), and “here I am, for you called me” (3:5–8).
- **ἐπί with an office or charge** (216 hits, 51 changed). The officer “over the forced labor” (1 Kings 12:18), the Levites “over the treasures” (1 Chronicles 26:20–26), Amasa “over the army” (2 Samuel 17:25) and Jehu anointed king “over the people of the Lord” (2 Kings 9:6) now read “over.” Where the Greek speaks of judgment, blessing or an army coming upon a people or house, the gloss stays “on” or “upon.”
- **ἕως with a time** (190 hits, 131 changed). “Until this day,” “until evening” and ἕως τοῦ with an infinitive now read “until.” “As far as” stays for distance (“from Adasa as far as Gazera,” 1 Maccabees 7:45), for degree (“sick unto death”), and before αἰών, where the following gloss already carries “for ever.”

The batches changed 396 tokens, most of them positions where ABP's English agreed with ours or had no one-to-one match. The verifier checked all 184,975 decisions, and Greek surfaces and word order are unchanged.

In 2 Samuel 21–24, at 21:1 the Lord says guilt lies “upon” Saul and his house (ἐπὶ Σαοὺλ … ἀδικία); “over” had made it a rule. At 21:8–10 Ρεσφά is Rizpah daughter of Aiah, and she kept watch “until” the rain fell, driving off the birds “by day” (ἡμέρας). At 21:12 AD's ᾿Ιαβὶς Γαλαάδ is Jabesh Gilead, not “Jabin.” At 21:20–22 Ραφά is Rapha, ancestor of the giants. AD had glossed it “of David” at 21:22, and Athens repeated “to” after τῷ. At 21:21 Jonathan is the son of David's brother Shimeah (Σεμεΐ; Σαμαά at 13:3). In the song of chapter 22, AD's ἐξείλετο at 22:1 and 22:20 is the Lord who “rescued” David, not one who “chose” him. At 22:16 the blast is “of the breath” of his anger. At 23:1 David is anointed “of God” (Θεοῦ) of Jacob. At 23:20–22 ᾿Ιωδαέ is Jehoiada, Benaiah's father, formerly “Jotham” and “Iodas,” and Benaiah “went down” into the pit and against the Egyptian. At 24:9 Israel is the subject of the census total. At 24:13–15 θάνατος is the “pestilence” of three days, which runs to the “hour” of the meal, and the seventy thousand “died.” At 24:16 the angel is told to “relax” his hand (ἄνες). The Gibeonites, Beersheba and Gilboa now take their familiar forms in both editions.

AD spells both Bathsheba and Beersheba Βηρσαβεέ. Athens writes Βηθσαβεέ for Bathsheba in 2 Samuel 11–12 and 1 Kings 1–2, but Βηρσαβεέ at 1 Chronicles 3:5 and in the title of Psalm 50. The glosses had mixed the two: AD gave “Bersabee” for Bathsheba in 1 Kings 1–2, “Bersabee~Beersheba” for her at 2 Samuel 11:3 and 12:24, and “Bithiah” at 1 Kings 1:11. Each of the 37 differing tokens now follows the person or place its verse names: the mother of Solomon, or the town at the southern limit “from Dan to Beersheba.”

In 1 Kings 1, at 1:13 David “swore” (ὤμοσας, aorist) that Solomon would reign. At 1:30 ὅτι οὕτω ποιήσω gives his sworn assurance, “that so I will do,” not a reason. At 1:35 Solomon is leader over Israel and “Judah” (accusative). The royal guard of 1:38 and 1:44 are the Cherethites and Pelethites in both editions, as in 2 Samuel, and Adonijah is the son “of Haggith.”

Two more construction batches, each hit read in its clause. After a kin, house, land, city or tribe noun, a genitive name now takes “of” (“son of Gideoni”, “house of Jacob”, “king of Babylon”); 646 of 670 hits were applied, leaving out names already in the possessive and appositions such as “King Jehoshaphat.” After ἐν, an article glossed “to the” is now “the” (59 of 60 hits; the articular infinitive at Leviticus 26:26 was left out). At Jeremiah 33:1 AD's “Joseph's” for ᾿Ιωσία is now “of Josiah.”

A stricter prompt for the gemma3:12b screener scored 10% precision on the 2 Samuel trial verses, and 6% once flags that only repeat ABP were dropped. Gemma is no longer used for screening.

From 1 Kings 2 the chapter review was done by parallel Claude reviewers under one written brief, each reading every open position against the Greek clause and the verse's full gloss line, with the coordinator validating, applying and verifying book by book. A calibration chapter (1 Kings 2) reviewed independently by the coordinator and a reviewer agreed on every correction the coordinator made; the reviewer also caught errors outside the open queue. 1 Kings 2–22 and all of 2 Kings were reviewed this way: about 3,400 edits, chiefly lost “of” and “to” on genitive and dative articles, doubled words across neighbouring glosses (“you you asked”, “the the house”), and wrong senses or names (δαβίρ “the pillar” → Debir, the pillars Jachin and Boaz, ῥοαί “streams” → pomegranates, Ζαμβρί “Omri” → Zimri, Sabaoth for “Sabbath”). Obvious AD misprints are glossed as the intended word Athens prints (λέγων for λέων “lion” at 1 Kings 13:24, ρήσεται for ῥύσεται at 2 Kings 18:32). Positions fixed outside the queue that then differ from ABP get their own ledger rows.

## 1 Chronicles to Daniel

The same parallel review finished the rest of the canonical Old Testament: 1–2 Chronicles, Ezra, Nehemiah, Greek Esther, Job, Psalms, Proverbs, Ecclesiastes, Song of Songs, the Twelve, Isaiah, Jeremiah, Lamentations, Ezekiel and Daniel. Each reviewer read every open position in its clause and the full gloss line of each verse, so it also fixed errors outside the queue. After every book, the coordinator validated, applied, rebuilt and verified the release. Both editions now have a decision for every position that ABP aligns. Every verify run reported Greek surfaces and word order unchanged. The verifier checked 308,421 decisions.

The change rate varied by book. Psalms, with glosses already close, ran at 1–4% of open positions. Proverbs, the Prophets and Ezekiel ran at 20–40%. Most changes fall into a few classes:
- a genitive or dative that lost its “of” or “to”;
- a pronoun or article doubled across neighbouring glosses (“I · I will”, “the · the land”);
- an optative glossed as a past tense;
- ἢ after a comparative read as “or” rather than “than.”

Words misread as a similar-looking word were corrected:
- ῥύομαι read as “flow” (rescue);
- ῥοά read as “stream” or “rose” (pomegranate);
- σῦρον read as “Syrian” (sweeping);
- στόμα glossed “beak.”

Glosses that followed the Hebrew rather than the Greek were also corrected:
- σχοίνισμα: “Bond” became “Cord” (Zechariah 11);
- ἐνθυμήματα: “idols” became “devices” (Ezekiel 44:10);
- φῶς: “opening” became “light” (Ezekiel 42).

Name glosses follow the identity rule. A variant or garbled spelling of the person's own name takes the KJV form:
- Ἀμώς for Isaiah's father is Amoz, and for the king it is Amon;
- Ἰάζερ for Azur becomes Azur (Ezekiel 11:1).

A Greek spelling of a different real name keeps that name:
- Ζαμβρί is Zimri at Micah 6:16;
- Σαρουΐας is Zeruiah at Jeremiah 44:13 (the Hebrew has Irijah);
- Ἰωακείμ is Jehoiakim at Jeremiah 52:31, as at 2 Kings 24:6.

Other names and glosses settled here:
- σαβαώθ is glossed Sabaoth throughout, because the Greek transliterates it and the KJV writes Sabaoth where the Greek has σαβαώθ.
- The sisters of Ezekiel 23 are Aholah and Aholibah.
- Transliterations that the Greek keeps stay as transliterations: Ubal (Daniel 8), ailammo (Ezekiel 40), Sabei (Daniel 11).

Some constructions recur in every book, including books reviewed before the reviewers saw full gloss lines. These are left for corpus-wide batches, each hit read in its clause:
- the psalm superscriptions;
- οὐ μή;
- interrogative μή glossed “surely not”;
- the vocative “the · O God”;
- the article doubled before a participle;
- ἐνώπιον with a following “of”;
- ἕως αἰῶνος;
- ἀλλ᾿ ἤ and πρὶν ἤ;
- “Highest” for “Most High”;
- spatial κατά in Ezekiel 40–45;
- about 200 doubled articles left in Exodus.

## Corpus-wide batches after the book review

Some constructions recurred in every book, so they were set across both editions in one pass. Each hit was read in its clause.

Checked against Boyd's updated Brenton and against Asser:
- **οὐ μή → "not · at all."** About 1,200 tokens changed. Both translations read οὐ μή as one strong negative, most often "shall not", sometimes "by no means" or "never", and never double it. Our "not · not" read as a double negative.
- **Psalm titles.** εἰς τὸ τέλος became "for the end", ψαλμός "a psalm", τῷ/τοῦ Δαυίδ "of David" (it had been "to the · David"), ᾠδή "a song" (the AD had "O"), and διάψαλμα "pause", as in Boyd and the 2015 Asser. Only title words changed: where verse 1 runs into the psalm text, as at 131:1, that text was left alone.

Two batches had a rule propose a fix for every hit, then reviewers read each hit and confirmed or overrode it:
- **Doubled words** ("the · the land", "I · I will go", "put on · on"): 3,222 hits. 120 remain where the Greek itself repeats the word (σε σύ, με ἐπικαλέσομαι, γὰρ εἰς).
- **Article with a substantival participle.** The article now carries the noun with its case: "the one · who lives", "of those · who fear", "to the one · who …". An attributive article after a noun or pronoun of the same case is "—", and an article after a preposition takes no extra "of". 2,104 hits.

Smaller batches:
- ἐνώπιον / ἐναντίον no longer add "of" to the genitive after them (145).
- ἀλλ᾿ ἤ is "but · —" and πρὶν ἤ is "before · —".
- Interrogative μή and ἦ are "[marks a question]".
- ἕως αἰῶνος is "until · eternity".
- θυσία is "sacrifice", not "grain offering", which followed the Hebrew (207).
- Κύριος is "Lord", not "LORD".
- The title ὁ Ὕψιστος is "the Most High".
- Spatial κατά in Ezekiel 40–48 is "toward", "at" or "by".
- The title of Psalm 137 names Haggai, not an angel.

Together these changed about 8,500 tokens. The verifier checked all 308,639 decisions, and Greek surfaces and word order are unchanged.

## Books outside ABP

ABP does not cover Tobit, Judith, 1 Esdras, Wisdom, Sirach, Baruch, the Letter of Jeremiah, Susanna, Bel, the Song of
the Three, 1–4 Maccabees or the Odes, so there is no aligned gloss to compare against. These books were read in full
instead: every gloss in both editions, verse by verse, against its own Greek, with Boyd's updated Brenton beside it only
to find the sense quickly. A gloss was changed only when it was wrong in its clause. None of Brenton's wording was
copied.

- **Scope.** 32 reviewer batches of one to ten chapters each. They covered every verse of every book that has neither
  an ABP decision ledger nor a previous full read. That includes the eleven Sirach verses Athens prints a second time
  after a section heading.
- **Result.** About 8,950 AD and 8,000 Athens glosses corrected, with no gloss left empty. The commonest faults were
  the same as in the ABP books:
  - lost genitive and dative relations;
  - "of" added after a preposition;
  - words doubled across neighbouring glosses;
  - substantival and attributive articles;
  - ὅτι as "because" where it means "that";
  - glosses holding alternatives or notes.

  Many senses were wrong, often a look-alike word (ῥώμῃ as "Rome", ἀρά as a name, ρύσεται as "flow"). Where one
  edition misprints a word one letter off what the other prints and the context needs, the gloss gives the intended
  word.
- **Names.** People and places that also appear in the canonical books take the canonical form: Josiah, Zerubbabel,
  Ezra, Nebuchadnezzar, Ashdod, Beth-horon, Mizpah, Hananiah, Azariah. Those found only in these books take the KJV
  Apocrypha form: Tobias, Holofernes, Ozias, Judas Maccabeus, Alcimus, Assideans, Modin, Susanna, Joacim. Every
  Ptolemy in 1–3 Maccabees is "Ptolemee". Each book's variants were aligned after its batches were applied.

The verifier still passes on all 308,639 ABP decisions, and Greek surfaces and word order are unchanged.

## Style choices settled from the translations

Four open style questions were settled by how Michael Asser's translation of the Apostoliki Diakonia text renders the
Greek, and by Boyd's updated Brenton where Asser does not decide:
- **Untranslated articles.** Neither translation renders the article of an articular infinitive, or an article before
  a name or an attributive adjective. Those articles are now "—" (about 2,340 tokens). Glosses such as "(marks the
  infinitive)", "(marks the name)" and "[introduces the adjective]" are gone, and so is "the" before an infinitive
  glossed "to …". Interrogative εἰ glossed "(marks question)" is now "[marks a question]".
- **The rivers of Eden.** Asser writes Pison in Genesis and Pishon in Sirach, so Boyd's Pishon decides; both write Gihon.
  Genesis 2:11–13 now agrees with Sirach 24 and Jeremiah 2:18.
- **Ἰουδαῖοι.** Asser calls the nation Judeans in 1–3 Maccabees and Jews in Esther, Ezra, Nehemiah, Daniel, 1 Esdras,
  2 Kings and 4 Maccabees; a single convert or confessor is a Jew. Where Asser has neither, Boyd gives Jews. The 179
  tokens that differed now follow that usage. The land of Judea keeps "Judean".
- **An article with a bare participle** ("the · fearing", "the · one carrying") takes the house form "the one" /
  "those", as in the article + participle batch. A rule proposed a fix for 3,477 hits and reviewers read each one. They
  overrode it often: an attributive participle after its noun is "—"; a participle already glossed as a noun ("the ·
  inhabitants", "the · dead") keeps "the"; after a preposition the article takes no extra "of" or "to"; a predicate
  adjective before the article (μακάριος ὁ …) leaves the article substantival. After πάντες, "all · — · who …" stays,
  and a bare participle takes "all · those · dwelling". About 3,100 tokens changed; those in Exodus to 2 Samuel wait for
  that book's full read.

## Spot-check and the grammar of names

A random 100 of the changes made since the Leviticus pass was drawn, 50 per edition, and each was read in its verse. Athens had no errors. AD had six, all in rows the review had appended from the base corpus:
- Sheba son of Bichri marked as a place;
- Μωυσῆ marked "vocative/dative" after ἐν χειρί;
- Jephunneh marked nominative after υἱός;
- μηρυκᾶται parsed as a future;
- λαλήσετε parsed as an aorist subjunctive;
- ἐπί at Jeremiah 36:21 (29:21 in the Hebrew numbering) glossed "on" beside a second ἐπί glossed "against".

Most of these are names, and the grammar audit leaves names out (31,584 AD words), because Morpheus guesses the declension of biblical names. So every name's stated case was compared with its gloss: "of X" should be genitive, "to X" dative.
- **Indeclinable names** in the house form ("indeclinable personal name, nominative in context") take the case of the article in front of them, or else the case the gloss shows. The automatic changes were sampled and read in their verses (60, all right), and the 133 doubtful ones were read in full. Kept as they stand:
  - dative possessives with τῷ (1 Chronicles 11:10);
  - "the way to Ophrah", which is a genitive (1 Samuel 13:17–18);
  - "did to Ai", which is an accusative (Joshua 8:2).
- **Names with base-corpus analyses** ("nominative singular masculine proper noun" on "of Reuben") were given the house form, wherever the same lemma has one elsewhere in the edition. Judas, the genitive of declined Ἰούδας, is a personal name, not the tribe.
- **Μωυσῆ** is genitive, dative or vocative. Its case was set from the word that governs it (ἐναντίον, διά, ἐν χειρί, μετά: genitive; τῷ, εἰσήκουσαν: dative). "Of Moses" was added after χειρί, γαμβρός, νόμον and ῥῆμα.

In all, 1,561 grammar strings were corrected (AD 848, Athens 713), all but six of them names, along with 9 AD lemmas. 29 glosses were corrected, among them two plain errors: Γεθσών at 1 Chronicles 6:28 was glossed "of Gethsemane" (it is Gershon), and Ματθανία and Ματθαναΐ in Ezra 10 and Nehemiah 12 were glossed "Matthew" (Mattaniah and Mattenai). That check left 219 name rows whose stated case their gloss does not show (AD 187, Athens 32), and each was then read in its verse. 196 grammar strings were corrected (AD 176, Athens 20), mostly AD base-corpus analyses of names with no house form to copy, such as υἱὸς Αδερ "son of Hadad" parsed as a nominative ten times in 1 Kings 21. With them, 24 AD lemmas that named a different word were corrected (Χιράμ had Χείρ, ᾿Αράθ had Ἄρης, ᾿Ωφίρ had Ὄψωρ), along with 9 AD glosses. 1 Chronicles 1:7 read "with Tarshish stones · of the Kotians · Rydians" for Θαρσίς Κίτιοι Ρόδιοι, now "Tarshish · Kittim · Rhodians" as at Genesis 10:4, and 1 Chronicles 1:15 read "of Aruka", "of Asenna" for the Arkite and the Sinite. The other 23 rows are right as they stand: printed datives (ἐν γῇ Αἰγύπτῳ, "in the land of Egypt"), gentilic adjectives (σειρήνειοι, ᾿Αβραμιαῖος, Θεκωῖτις, ῾Ιεροσολυμίτης), and accusatives of motion (Κυρήνην, Δαμασκόν).

AD's name lemmas were then made consistent. Before, AD spelled many of them several ways: Rehoboam had about ten, with grave accents, missing breathings and lookalike names such as Βοβοάμ, and a few Ishbosheth rows had the lemma Ἰεβουσαῖος. 4,092 AD lemmas were corrected in three steps.

1. **Form.** Each lemma was put in its dictionary form, using Athens's spelling of the same name where Athens has one: a grave became an acute, a spacing breathing mark became a real one, and a missing breathing was supplied. AD keeps ρρ where Athens writes ῤῥ.
2. **One lemma per printed name.** Every printed form of a name now has a single lemma. The 292 groups whose lemmas differed by more than accents were read one by one. Declined names take their nominative (Μανασσῆς, Ἔσδρας, not the verb-like Ἐσδράω), and so do gentilics (Εὐαῖος, not Εὐαῖον). The -ία names follow their nominative in -ίας (Ζαχαρίας, Οὐρίας, Σαμαίας). Indeclinable names take the name as printed. Where one spelling is shared by two people, each keeps its own lemma: Γαδδί for Gadi at 2 Kings 15:14 and 15:17, and Γάδ for Gad elsewhere.
3. **Lemmas that named another word.** About 40 single rows were corrected, such as Γολιάθ on Γωλάμ and Ἰησοῦς on ᾿Ιεσρί. Two other groups turned up along the way. In 7 rows the word ἀλλοφύλων carried the lemma Φυλιστιείμ and the grammar "indeclinable ethnonym"; it is now ἀλλόφυλος, parsed like its other 110 uses. In all-capitals title words, ᾨδή had the lemma ὦ or ἰδού in 9 psalm titles, and Psalm 6:6 ᾅδῃ ("Hades") had ᾠδή.

Along the way, 112 lemmas of ordinary words with a grave accent or a garbled form were corrected (καί, ἱερεύς; προσφέρω for πρὸςφέρω), along with 36 grammar strings and 3 glosses. At Nehemiah 10:22 the names Hanan and Anaiah had been glossed "to the upper" and "high", and at 1 Chronicles 8:11 Ὡσίν was "from the Os" (now Hushim). Two slips joined the AD errata list: Γάβερκαὶ at Deuteronomy 2:8 (Γάβερ καί run together) and συναντὴν at 2 Kings 2:15 (for συνάντησιν). The only lemmas still carrying a grave are phrase lemmas such as ἀνὰ μέσον, where the grave is correct.

## The last style calls, with Brenton–Boyd first

Five calls left open by the book reviews were settled across both editions (125 tokens):
- **θυσία** is "sacrifice" everywhere, as Brenton renders it: the 91 remaining "offering" glosses, mostly θυσία σωτηρίου and the evening θυσία (Ezra 9:4, Daniel 9:21), now read "sacrifice".
- **ἕως αἰῶνος** stays "until · eternity". Anarthrous αἰῶνος is "eternity" elsewhere in the corpus, and Brenton's "for ever" would make ἕως "for".
- **ἦ** opening a question is "[marks a question]" (1 Samuel 10:11–12, 2 Samuel 3:25, 2 Chronicles 13:9, seven places in Job). ἦ μήν is "surely · indeed" everywhere. Where ἦ joins the second half of a question it is "or" (Job 12:2), as Brenton reads.
- **δή** stays "please" in requests, including the future of a polite request ("let me pass, please"). It is "now" after ἰδού, εἰ and δεῦρο and in Judith's consent at 12:18, and "indeed" after καί and διό.
- **Ἰωράμ** is Joram for every bearer, as Brenton writes it, including the priest at 2 Chronicles 17:8.

## Genesis to 2 Samuel: words outside the ABP comparison

The ABP review of Genesis to 1 Kings 1 reached only the words ABP aligns one-to-one with ours. Words inside an ABP grouped
phrase, words where the Greek differs, and verses ABP could not align were never read: about 24,500 AD and 27,700 Athens
positions in 4,948 and 6,192 verses. Reviewers now read every such verse in full, against its own Greek, with the
never-reviewed words marked and Boyd's updated Brenton beside it only to find the sense. Plainly wrong glosses
elsewhere in those verses were fixed too.

- **Genesis.** 1,156 fixes in both editions. Most are lost “of” and “to” on genitive and dative articles, words doubled
  across neighbouring glosses, glosses holding alternatives or notes, and names left in Greek form (Pathrusim, Anamim,
  Calah, Jokshan, Zaphnath-paaneah, the sons in Genesis 46). Indefinite ἐάν after a relative is “ever”. Each name
  then takes one spelling throughout the book (Adah, Milcah, Nebajoth, Timna). Σάρα before Genesis 17:15 is Sarai,
  as Αβραμ is Abram.
- **Leviticus.** 1,037 fixes. The same classes recur, most often a lost “of” in the sacrificial and purity formulas
  (“the young bull of the sin offering”, “a lesion of scaly disease”) and “of” invented after a preposition (“from
  of the blood”). Indefinite ἐάν after a relative is “ever”. Athens numbers Leviticus 5:20–26 as 6:1–7, and its
  fixes follow its own numbering.
- **Exodus, Numbers and Deuteronomy.** 4,007, 1,716 and 1,132 fixes. Exodus still held about 750 glosses with
  alternatives or notes (“on/upon”, “tent/tabernacle”, “bases/sockets”), mostly in the tabernacle chapters; each is now
  one gloss for its clause. Numbers' census and station lists, and the clan names of Numbers 26, take their KJV forms
  (Shedeur, Helon, Ahira, Ammihud, Nemuel, Zerah, Hahiroth, Bene-jaakan). μή after verbs of watching is “lest”, and
  ὑψηλῷ with the arm in Deuteronomy is “uplifted”. Each name then takes one spelling across the book.
- **Joshua, Judges, Ruth, 1–2 Samuel and 1 Kings 1.** 1,653, 1,383, 72, 303, 1,342 and 20 fixes. Joshua's boundary
  and town lists account for most of its total: garbled names read as ordinary words (“grave” for Tappuah, “Hermes”
  for Hormah) and towns left in Greek form now take their KJV names where the Greek and the list identify them; towns
  that cannot be identified keep a transliteration. The mighty-men list of 2 Samuel 23 held wrong words in AD
  (“Samaria”, “Elijah”, “Kishon”). Interrogative μή, εἰ and ἦ are “[marks a question]”, and ὁ κύριός μου said to the
  king is “lord”. Names then take one familiar spelling across each book: Absalom, Mephibosheth and Abishai replace
  Abessalom, Memphibosthe and Abisai in every book, and Mizpeh, Ramah, Ophrah, Ish-tob, Beth-shemesh and Ira replace
  their Greek forms in Joshua to 2 Samuel. Ramathaim stays at 1 Samuel 1:1, as in the KJV.

With this, every verse of Genesis to 1 Kings 1 has been read in full in both editions.

## Notes left in glosses, settled corpus-wide

About 700 glosses in each edition were notes rather than English: “[modal particle]”, “(marks indefinite/conditional
time)”, “(with ἀνά)”, “(with κατά)”, “[part of 'because']” and their kin. Each is now the house gloss for its pair:

- ἄν after a relative is “ever” (“who · ever”), as ἐάν there already was; elsewhere ἄν is “—”, the verb's own gloss
  carrying “would” or “may”.
- A word whose sense its partner carries is “—”: μέσον after ἀνά “between”, ὧν after ἀνθ᾽ “because”, πρόσωπον after
  κατά “before”, τρόπον after ὅν “as”, οὗ after ἕως “until”, τί or ἵνα in “why”, ἤ after ἀλλά. μή in οὐ μή is
  “at all”, the corpus form. The same holds for the 200 places that glossed ἀνὰ μέσον “between · midst”.
- εἰ in a negative oath is “—” where the verb already carries the negative; εἰ opening a question is “[marks a
  question]”.
- The article of an articular infinitive glossed “in order” is “—”; the infinitive's “to” carries the purpose.

## The sanctuary: tabernacle and witness

σκηνή for the sanctuary is “tabernacle” and μαρτύριον is “witness”, as in the 2015 revised Asser (in Exodus to Numbers it
has tabernacle 259 times, and witness 156 times against testimony 17). Each σκηνή glossed “tent” and each μαρτύριον
glossed “testimony” took the word the 2015 Asser uses in that verse, or, where it uses neither or both, Boyd's
Brenton; the rest were read by hand. About 870 glosses changed. An ordinary tent (“his tent”, the people's tents,
the booths of Nehemiah 8) stays “tent”, and “the ark of the testimony” and “before the testimony” stay, as Asser has
them.

## One gloss per word

About 520 glosses still offered alternatives (“on/upon”, “bases/sockets”, “you shall offer/do”), most in the
tabernacle chapters of Exodus, and about 650 carried a note in parentheses or brackets (“you (plural)”, “river
(Nile)”, “[completes 'most holy']”, “will [marks a question]”). Each is now one gloss. Where the alternatives were
content words, the one the 2015 Asser, then Boyd's Brenton, uses in that verse was kept; function words take the
house form (“on”, “from”, “with”), βάσις is “bases” and λογεῖον “breastpiece” throughout, and the rest were chosen
by hand for their clause. Notes in parentheses were dropped where the word's own gloss stands without them; ὁ τοῦ
Ναυή is “the son · — · of Nun”. Athens' stray ᾶ at Joshua 17:4 keeps its “[unclear Greek form]” marker.

## The Odes

Only Athens prints the Odes. Each canticle was aligned with the same passage in its source book, and the 282 words with
the same Greek but different English were read. 43 Ode glosses and 3 source glosses were corrected, among them the
vocatives of Deuteronomy 32 (“O heaven”, “O nations”), ἐπί as “with” in “provoked me to jealousy with what is no god”,
θυμός as the “venom” of serpents, and σκηνή as “a tent” in Hezekiah's song.

The songs themselves were then read against their Greek in both editions. About 70 glosses in Exodus 15 and
Deuteronomy 32 were corrected: lost genitives (“of rams”, “of kidneys”, “of destruction”), first persons (“I said”,
“I shall strike”), attributive articles before participles (“— · who begot”), and μή as “lest” in 32:27.

## Articles and genitives

The article was checked against the word it belongs to, corpus-wide.

- A genitive article glossed “the” between its head noun and a genitive noun now carries the relation: “the words ·
  of the · law”, “the fruit · of the · earth” (about 630 glosses). It was left alone after Κύριος and Θεός, after a
  genitive-governing preposition or adverb, and where the verb takes the genitive.
- Where the article was “the” and the next word was already glossed “of the X”, the article is now “—”; where the next
  word was “of X”, the relation moved to the article (“the · of the · people”, not “the · of the people”); after
  ἀπό, ἐκ, ἐπί and similar the noun's stray “of” was dropped. Before a name the article is “—” (“Mesopotamia · — · of
  Syria”), and the article of an articular infinitive is “—”. About 1,700 glosses.
- ὁ δέ before a finite verb is the pronoun: “he · and · said”, “she · and · said”; where the verb's gloss already says
  “they said”, the article is “—” (68 glosses).
- About 470 genitive nouns that follow their head noun gained “of”: “lesion · of scaly disease”, “nakedness · of sister
  · of father”, “by houses · of ancestral houses”, “book · of words”. Every hit was read; counts and measures
  (“twelve thousand horsemen”, “breadth · cubits”), genitive objects, same-word pairs (“blood · blood” in
  Deuteronomy 17:8) and the displaced genitives of the literary books were left as they were.

πᾶς with an article and participle reads “every · one · who touches”, “every · one who is · touching” and “all · — · that had befallen them” (110 glosses, each read in its verse; πᾶς itself is “every” or “any”, not “everyone · one who is”).

Ἑνώχ son of Reuben and son of Midian is “Hanoch”; Ἀμμάν at Genesis 19:38 is “Ammon”, as in Brenton (the Greek has no “Ben-” for the Hebrew form Benammi) and Genesis 14:7 names “Hazazon-tamar”, as at 2 Chronicles 20:2; Cain's and Jared's sons stay “Enoch”.

## Loose ends after the review

Every edit of the article pass above was reread in its verse, and three smaller patterns were settled the same way.

- Rereading the “the · of the X” edits found about 160 wrong ones, now corrected. Names had wrongly taken the relation
  onto the article (“of the · Cyrus” is now “— · of Cyrus”). A preposition had been doubled (“outside · of the · veil”
  is now “outside · the · veil”, and the same after ἀπό, ἐκ, περί, διά and the other genitive prepositions). A noun had
  kept “a” after an article that already says “the” (“for the · lamb”). Split phrases now read “the · of Noah · ark”;
  in regnal dates (“year · — · of Joash · king”) the name stays in apposition.
- The dative article before a name carries the relation: “bowed down · to · David”, “the ninth · to · Jeshua”. It is
  “—” after a preposition (“in · — · Judea”), where a preceding word already gives the relation (“for all · — ·
  Israel”), with verbs that take the dative as their object (“served · — · Baal”, “commanded · — · Moses”) and in
  apposition (“your servant · — · David”). Psalm titles read “a psalm · of · Asaph”, as in the other titles. Peoples
  keep “the” (“to the · Levites”). About 680 glosses, each read in its verse, including Amram and Izhar for Abraham and
  Isaac at 1 Chronicles 26:23.
- A participle glossed “what …” no longer follows an article glossed “the” (“— · what had happened”); predicative
  γεγραμμένον is “written” (“found · written”); 71 glosses.
- The reviewers' open calls were settled. ὅτι ἀλλ᾿ ἤ is “— · but · —” (“but only”), and ἀλλ᾿ ἤ no longer reads
  “but · or”, “but · than” or “but · rather”. The AD misprint ᾿Ισραήλ at 1 Samuel 18:19 is “Adriel”, as Athens has
  it. Athens Ἱερείμ at 1 Samuel 15:3 is “Jerim”, as in AD and Brenton. About 50 glosses.

## Lemma review trial: Job

The ABP review could check a gloss only where ABP has the same Greek word. Job 21:22 shows what slips through: ABP
reads σοφούς where AD and Athens read φόνους, so the gloss “bloodshed” was never compared, though the plural means
“murders”. As a trial, every content word in Job without an ABP partner (563 in AD, 2,206 in Athens) was compared
with how the rest of the corpus glosses its lemma. The 760 that differ from the usual glosses were each read in
their verse.

- Most stand. They are contextual senses (θαυμάζειν πρόσωπον “show regard to”, στόματι μαχαίρας “edge”), Job's own
  vocabulary (ἱκανός “the Mighty One”) or forms of εἰμί and γίνομαι.
- 38 were corrected: 13 in AD, 23 in Athens, and φόνους in both. Examples: σταθμός “doorpost” for the weight of
  the winds (28:25), δράκων “a snake” beside the sea (7:12), ἀληθινός “faithful” for “true” (1:1), neuter
  ἐκλεκτόν “the chosen one” (37:11), ἐποίησεν “did” for “made” (28:24, 26), and first-person glosses on the
  second-person ἐξείλω (36:21) and ἥμαρτον “offended” for “I sinned” (33:9).
- That is about one correction for every 75 unchecked content words. The same review is worth running on the other
  books, starting from 1 Kings 2.
- AD spellings to check for the errata list: κώμην for κόμην (1:20), παυσώμαθε for παυσώμεθα (37:19), ἐμπρήσεις
  where Athens has ἐμπλήσεις (38:39), and ἔχετε where Athens has ἔχεται (2:3). Athens has ἀπῆλθεν where AD has
  ἐπῆλθεν (15:19). The glosses follow the sense in each case.

## Lemma review: 1 Kings 2 to Malachi, with Esther and Daniel

`scripts/adlxx/lemma_outliers.py` flagged 12,264 unchecked words in the remaining protocanonical books, Esther and Daniel. Eight reviewer agents each took one group of books and read every flag in its verse. None of them saw ABP or Asser. They proposed 266 changes, raised 45 questions and noted where a neighbouring word, flagged or not, was also wrong. Every proposal was then reread in its verse before it was applied. Two pointed to the wrong word and were moved to the right one (γῆς at 2 Kings 21:8). Sixteen were reworded: ἐν τῷ βασιλεῦσαι αὐτόν is “to become king”, not “becoming”; διεσκέδασε τὴν βουλήν is “set aside”; ἐνέπεσον πρός is “they fell away”, as in the KJV; θεραπεία is “service”, not “worship”; an article already glossed is not repeated in its noun. Twenty-eight questions were settled from the Greek. Examples: κλήρῳ is “by lot” in 1 Chronicles 6; ἐξοδίου σκηνῆς is “of the closing assembly of the tabernacle” in the Psalm 28 title; ναθινίμ are the Nethinim, not “the Nazarenes”. The other seventeen were left as they stand.

In all, 300 glosses were corrected (AD 177, Athens 123), about one in 41 flags:

| 1KI | 2KI | 1CH | 2CH | EZR | NEH | ESG | PSA | PRO | ECC | LAM | ISA | JER | EZK | DAG | Twelve |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 43 | 27 | 50 | 35 | 9 | 4 | 12 | 20 | 22 | 1 | 1 | 8 | 30 | 29 | 3 | 6 |

The yield is lower than Job’s, because Job had the most unmatched poetry. The commonest faults: ἐγένετο/ἐγενήθη glossed “became” where it is “it came to pass”, “came” or “was”; ποιέω with “did” and “made” swapped; πᾶς ὁ glossed “every”; γῆ glossed “earth” for the land; and names glossed as common words (᾿Αμαρία “sin”, ᾿Ορνά “bird”, Βαρέα “hard”, ρώμῃ “Rome”).

The review also found AD and Athens spellings that are probably misprints. Each is glossed by its sense, and the Greek is unchanged; they go to the errata list:

| Where | Printed | Probably |
|---|---|---|
| AD 1 Kings 13:24 | λέγων | λέων |
| Athens 1 Chronicles 17:22 | ἐγεννήθης | ἐγενήθης |
| Athens Lamentations 4:10 | ἐγεννήθησαν | ἐγενήθησαν |
| Athens Daniel 9:2 | ἐγεννήθη | ἐγενήθη |
| Athens Isaiah 43:19 | κενά | καινά |
| AD Ecclesiastes 1:10 | κενόν | καινόν |
| Athens Isaiah 51:23 | κόψον | κύψον |
| AD Isaiah 31:4 | θύρᾳ | θήρᾳ |
| AD Isaiah 33:18 | στρεφομένους | τρεφομένους |
| AD Isaiah 43:6 | ἅγιε | ἄγε |
| AD Ecclesiastes 4:8 | πειρασμός | περασμός |
| Athens Ezekiel 47:22 | κύκλῳ | κλήρῳ |
| Athens Psalm 108:24 | ἔλεον | ἔλαιον |
| AD 2 Chronicles 18:2 | ἠγάπα | ἠπάτα, in other witnesses |

Lemma or grammar errors for the grammar audit: ρήσεται tagged λέγω (2 Kings 18:32), ᾿Ιάβις tagged Ἰούδας (1 Chronicles 2:55), Athens ταπεινώσει parsed as a noun where it is the verb (Isaiah 25:5), and διατάξεις parsed as a noun where it is the verb “you shall appoint” (Ezekiel 21:20; its gloss is still “paths”).

## Lemma review: the deuterocanon

`scripts/adlxx/lemma_outliers.py` flagged 28,140 unchecked words in 1 Esdras, Tobit, Judith, 1–4 Maccabees, Wisdom, Sirach, Baruch, the Letter of Jeremiah, Susanna, Bel and the Song of the Three. Twenty reviewer agents each read about 1,450 flags in their verses, in book order; none saw ABP or Asser. All 305 proposals matched the release and were read in their verses. One was reworded (ὑάκινθος at Sirach 40:4 is "violet", as the corpus glosses it, not "blue"), one parallel was added for AD alone (τὸν αἰώνιον at Baruch 4:20 is "the Eternal One"; Athens adds ὕψιστον, so its "eternal" stands), and 305 were applied (AD 147, Athens 158), about 1 in 92 flags. 54 questions were left for a later pass and then settled one by one, with Brenton–Boyd as the check. That gave 66 glosses and 14 lemma or grammar changes. Examples: ὧν χάριν had its two glosses swapped (Judith 8:19); κάθημαι of a land is "will lie waste" (8:21); πλήθει δυνάμεως is "multitude of an army" (1 Maccabees 3:19). Where Athens prints a slip (λαοῦ for ναοῦ at 1 Maccabees 4:57, ἡτίμασας for ἡτοίμασας at Wisdom 16:2), its lemma now follows the intended word, as its gloss already did. Where AD's word is shared with Brenton's Greek and Brenton's English reads it as the near word (φάραγξιν "ranks" at 1 Maccabees 6:38, μέλι "melody" at Sirach 40:21), the gloss follows Brenton. Substantival πολλοί, glossed "numerous" 126 times across the two editions, is now "many". The glosses of both editions now use American spelling throughout, as Boyd does: 461 changes, mostly neighbour, favour and honour, with travelling, worshipped, mould and storey.

| Book | Corrected | Book | Corrected |
|---|---|---|---|
| 1 Esdras | 20 | Wisdom | 5 |
| Tobit | 27 | Sirach | 66 |
| Judith | 32 | Baruch | 12 |
| 1 Maccabees | 60 | Letter of Jeremiah | 2 |
| 2 Maccabees | 49 | Susanna | 2 |
| 3 Maccabees | 14 | Song of the Three | 2 |
| 4 Maccabees | 14 | | |

The commonest corrections: πᾶς with an article or a mass noun glossed "every" for "all" (and the reverse without the article); ἐγένετο/ἐγενήθη "became" or "it came to pass" where a noun follows as subject ("there was a great famine"); σκεῦος "belongings" for the temple vessels; "made" for "did" with evil or good; γῆ "earth" for the land; lost plurals (λογισμῶν "reasonings"); British spellings left from the source glosses (honours, favour, travelling); and swapped glosses of neighbouring words (ὧν χάριν at 3 Maccabees 5:41; τέλος and δοκῶν at 3 Maccabees 1:26).

## Grammar audit against Morpheus

`scripts/adlxx/grammar_audit.py` parses every surface with Morpheus (perseids-tools/morpheus, built locally in `build/ext/morpheus`). It lists each word where no Morpheus analysis fits the case, number, gender, tense, voice, mood and person our grammar column states. Proper names and indeclinables are not compared, because Morpheus guesses their declension. The script knows the Koine and Septuagint forms Morpheus misses: aorists of αἴρω compounds printed with an iota subscript (ἐπῇρε), accusative plurals in -εις (πήχεις), κάθημαι, ἠδύναντο, the second aorist passive ἀπηγγέλη, the imperative ἀνάστα, and aorist passive imperatives identical to unaugmented indicatives (πορεύθητε). Fixes are applied with `scripts/adlxx/apply_grammar.py`, which checks each edit against the release's current value.

The first passes corrected 681 analyses (AD 321, Athens 360):

| Class | Words | Example |
|---|---|---|
| Participles labelled “imperative” | 435 | βλέπων, “present active imperative, nominative masculine singular” |
| θη-aorists labelled “middle” | 96 | ἐγενήθη, which the corpus elsewhere calls aorist passive |
| Futures labelled “aorist subjunctive” | 41 | ἀποθανῇ, “you shall die” |
| Imperfects labelled “aorist” | 51 | ἐξέλειπον, κατέλειπε, ἐμαστίγου |
| Optatives labelled “infinitive” | 20 | μεγαλύναι, “may he magnify” |
| Genders confirmed by the article | 37 | τὰ χρυσᾶ (neuter), ὁ νῶτος (masculine) |
| Other single words | 1 | Song 5:2 ἄνοιξον, a second-singular imperative |

Fourteen apparent futures were left as they stand. In each, the context points to a subjunctive or a third-person subject, which conflicts with the printed form (δώσῃ, ἀφελῇ, ἐξαποστελῇ, ἐκβαλῶ after ὅταν, πληθυνῶ after ἵνα, ἀπολῆται); they belong with the errata. About 3,565 disagreements remain (AD 1,744, Athens 1,821). By the feature that differs: case 736, gender 511, tense 481, mood 353, voice 327, number 314, two or more 561. Each needs its verse read, since the remainder mixes real errors with accent and Koine forms Morpheus does not know (θλίψις, θυΐσκαι).

### The single mismatches

Eight reviewer agents then read all 3,565 remaining mismatches in their verses and proposed 2,946 corrections (grammar 2,632, lemma 314; AD 1,600, Athens 1,346). Each proposal was checked against the release. 2,854 now agree with Morpheus, or name a lemma the corpus already uses; a random 100 of these were read in their verses and all stood. The other 92 were read one by one. Eight carried the wrong word position, and four new strings were respelled in the corpus style. Typical corrections: second aorists parsed as imperfects (εἶδε, ἦλθον); neuter plurals parsed as singular (σκεύη); middle imperatives parsed as active (σπάσαι); Attic contracted futures parsed as presents (ἐργᾶται, καταχαροῦμαι); feminine nouns of the second declension (αἱ ἄρκοι); vocatives after ὦ; and lemmas that held an inflected form (κάνθων for κανθός, ἦρεν for αἴρω). Three Athens Strong’s decisions moved with their lemma. 58 questions and 99 apparent misprints were set aside for the errata list.

The 58 questions were then settled one by one, with 100 grammar or lemma changes and 8 glosses. Salt: ἁλί and ἅλα are forms of masculine ἅλς, not neuter ἅλας. Sapphire and emerald are feminine. The -σοι(το) optatives are futures by form (ἀγαλλιάσοιντο), while πέσοι stays a second aorist. ἐργῶνται is the contracted future throughout. At Ezekiel 9:5 μὴ φείδεσθε is 'do not spare' (AD had φεύγω, 'flee'). At Isaiah 17:11 κληρώσῃ is second-person middle, 'you will inherit for your sons', as Brenton reads it. Athens's ἐξέλεξεν at 3 Maccabees 6:29 is glossed as ἔλεξεν, 'said'. Seven accent slips joined the errata list. AD's iota-subscript aorists (ᾖρε, about 200) turned out to be a spelling habit, not slips. The last, Athens 1 Kings 6:20 περιεπίλητε, stands in a clause Brenton's text lacks (Solomon overlaid the house within with gold); Swete's apparatus records the clause with an aorist of περιπιλέω, so περιεπίλητε is printed for περιεπίλησε, and it is now parsed and glossed as "overlaid".

The audit no longer counts AD words listed as slips, whose grammar follows the intended word. 921 mismatches remain (AD 358, Athens 563); the reviewers judged Morpheus wrong in these (Septuagint feminines such as ληνός and ἄρκος, aorist infinitives it reads as optatives from the accent). The audit is closed.
