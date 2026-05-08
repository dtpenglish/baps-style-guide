# 5.3 The Macron-Only Convention
!!! info "Scope"
    The macron-only convention applies in **two contexts**:

    1. **The [BAPS master glossary](glossary-reference.md)** – the `diacriticSpelling` column records the macron-only form of each term as a reference.
    2. **Bhajan and scripture-verse transliterations** within publications – where pronunciation cues matter for recitation and prosody.

    It is **not** used in **prose text**. In body paragraphs, headings, photo captions, footnotes, and titles, terms are set in plain Roman with no diacritics. For the prose rule, see the [SAP Diacritics Policy](sap-policy.md). For the larger discussion, see [Diacritics & Transliteration](index.md).

## 5.3.1 The Rule
Long *a* vowels in transliterated Sanskrit, Gujarati, and Hindi terms are marked with a macron: **ā**. No other diacritical marks are used.

## 5.3.2 Why Macron-Only?
Full IAST (International Alphabet of Sanskrit Transliteration) marks every vowel length and every retroflex, palatal, and sibilant distinction – *Akṣharabrahman*, *Vacanāmṛta*, *Svāminārāyaṇa*. This is precise but visually demanding for the general reader, and difficult to typeset consistently across our four-language workflow.

The single most common loss in plain-Roman BAPS transliteration is the long *a* – the difference between *sadhu* (which an English reader pronounces with a short *a*) and *sādhu* (the actual Sanskrit pronunciation). Marking only that one distinction:

- Captures the most common pronunciation error, restoring the long *a* that English readers otherwise miss.
- Keeps text readable for general audiences who are not Sanskrit students.
- Is easy to typeset (a single Unicode character: <kbd>U+0101</kbd>) and easy to search.
- Stays consistent with how BAPS publications have rendered names like *Swāminārāyan* and *Aksharbrahman* in recent decades.

## 5.3.3 How to Apply It
Mark a macron on every long *a*. A long *a* is the vowel sound in *father*, not the short *a* in *cat*.

| Term | Plain Roman | Macron-only |
|---|---|---|
| Sadhu | sadhu | **sādhu** |
| Maharaj | maharaj | **mahārāj** |
| Bhagwan | bhagwan | **bhagwān** |
| Aksharbrahman | aksharbrahman | **aksharbrahman** *(no long-a vowels)* |
| Swaminarayan | swaminarayan | **swāminārāyan** |
| Vachanamrut | vachanamrut | **vachanāmrut** |
| Pramukh | pramukh | **pramukh** *(no long-a vowels)* |
| Akshardham | akshardham | **aksharadhām** |
| Gunatitanand | gunatitanand | **guṇātītānand** → **gunātītānand** → **gunatītanand**? |

!!! warning "Edge case under review"
    The last entry illustrates a known ambiguity: when a name contains both long *a* and long *i*, the macron-only rule marks only the *a*. *Gunatitanand* becomes *Gunatītanand* in some sources, but our rule strictly marks only long *a*: **Gunātitānand**. The team should agree on whether to mark long *i* in proper names or leave them plain – send your view via [Feedback](../feedback.md).

## 5.3.4 What We Do Not Mark
We do **not** use the following IAST diacritics, even when the source term contains them:

| IAST mark | Examples we leave plain |
|---|---|
| ṣ, ś (sibilants) | *Akshar* not *Akṣhara*; *Shikshapatri* not *Śikṣāpatrī* |
| ṭ, ḍ, ṇ (retroflexes) | *Pramukh* not *Pramukha*; *Pratishtha* not *Pratiṣṭhā* |
| ṛ (vocalic r) | *Krishna* not *Kṛṣṇa* |
| ī, ū (long i, long u) | *Bhakti* not *Bhaktī*; *Guru* not *Gurū* |
| ṃ, ḥ (anusvara, visarga) | *Aum* not *Auṃ*; *Namah* not *Namaḥ* |

## 5.3.5 Typing the Macron
| Tool | How |
|---|---|
| Windows | <kbd>Alt</kbd> + <kbd>0257</kbd> on the numeric keypad → ā |
| InDesign | Glyphs panel → search "0101" → double-click |
| HTML/Markdown | Type `ā` directly, or use the entity `&#257;` |
| Excel/Word | Insert → Symbol → Latin Extended-A → ā |

For high-volume entry, set up an autocorrect rule (Word) or text-replacement (macOS) that converts a typed sequence (e.g. `aaa`) to `ā`.

## 5.3.6 Capital Macron-A
The capital form is **Ā** (<kbd>U+0100</kbd>). Use it at the start of sentences and in proper nouns: *Ādi*, *Ārti*, *Ākash*.

## 5.3.7 Source-Language Considerations
This convention is for **transliteration into English-language editorial contexts**. Our Gujarati and Hindi publications use the appropriate native script and follow language-team conventions for any embedded Roman text.

When transliterating from a Gujarati source, use the Gujarati pronunciation (often closer to *Bhagwān*); from a Sanskrit source, use the Sanskrit pronunciation (often closer to *Bhagavān*). Record the chosen form in the [glossary](glossary-reference.md) and use it consistently.

## 5.3.8 Italicization in Macron-Only Contexts
Within a verse transliteration, the entire verse is italicized as a block (see [Italics §3.5.4](../editorial/italics.md#354-shlokas-padas-and-other-quoted-verses)) – individual term italicization doesn't come up.

Within an editorial / glossary-reference context (this site, the spreadsheet's example column), an untranslated transliterated term is italicized on first appearance and explained briefly: *bhakti* (devotion). Subsequent appearances of the same term are set in roman without italics. Proper nouns (names, titles, place names) are not italicized.

!!! warning "Names – no diacritics, regardless of context"
    Personal names, place names, organization names, and titles of works are spelled **without diacritics** in both prose and verse – *Bhagwan Swaminarayan*, *Sarangpur*, *the Vachanamrut*. The macron-only convention does not apply to names. See [§5.2.2](sap-policy.md#522-names-never-with-diacritics).

!!! tip "When in doubt, check the glossary"
    The [master glossary](glossary-reference.md) records the agreed spelling for ~1,500 BAPS terms. If a term you need isn't there, add it – that's how the glossary grows.
