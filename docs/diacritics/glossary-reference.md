# 5.4 Glossary Reference
The master glossary is a **reference repository** that records, for each BAPS term:

- the **plain-Roman** spelling (used in prose, headings, captions),
- the **macron-only diacritic** spelling, where appropriate, for use in **bhajan and scripture-verse transliterations** only,
- the word class, definition, source language, and any usage notes.

Before introducing or correcting a term in any publication, check the glossary first.

!!! tip "Diacritic spellings are for verses, not prose"
    The `diacriticSpelling` column is what to use when transliterating a *bhajan*, *shloka*, *pada*, or other verse content where the macron helps the reader pronounce the term. **In prose text** – body paragraphs, headings, photo captions, footnotes, titles – use the plain-Roman headword. Diacritics are not preferred in prose. See [SAP Diacritics Policy](sap-policy.md).

## 5.4.1 Where It Lives
The glossary covers Sanskrit, Gujarati, and Hindi terms used across BAPS publications. A link to the current version will be provided here once it is ready.

Columns:

| Column | Contents | When to use |
|---|---|---|
| `term` | The plain-Roman headword (e.g. *sadhu*) | **Prose, headings, captions** – the default in every general-reader publication |
| `wordClass` | Part of speech (noun, proper noun, verb, etc.) | Reference |
| `diacriticSpelling` | Macron-only spelling, where applicable (e.g. *sādhu*) | **Bhajan and scripture-verse transliterations only** |
| `definition` | Brief gloss for editorial reference | Reference |
| `sourceLanguage` | Sanskrit / Gujarati / Hindi | Reference |
| `notes` | Usage notes, alternative spellings, cross-references | Reference |

## 5.4.2 How to Use It
**For routine prose editorial work (the typical case):**

1. Encounter a term in your text – say, *gunatitanand*.
2. Search the glossary for the headword.
3. Use the spelling from the **`term`** column (plain Roman, no diacritics) in body text, headings, captions, footnotes, and titles.
4. If the term has a usage note, follow it.

**When transliterating a bhajan or scripture verse:**

1. For each transliterated term within the verse, look up the headword in the glossary.
2. Use the **`diacriticSpelling`** column – the macron-only form – for the verse text.
3. The English translation alongside the verse stays in prose form (no diacritics).
4. See [Italics §3.6.4 Shlokas, Padas, and Other Quoted Verses](../editorial/italics.md#364-shlokas-padas-and-other-quoted-verses) for the typographic treatment.

**Names – never with diacritics, in either context:**

Personal names, place names, organization names, and titles of works are spelled in plain Roman both in prose and in verse transliterations. See [SAP Diacritics Policy §5.2.2](sap-policy.md#522-names-never-with-diacritics).

**For new terms not in the glossary:**

1. Check that it isn't a variant spelling of an existing entry. *Sadguru*, *Sadgurū*, and *Satguru* should not all become separate rows.
2. Propose an addition via [Feedback](../feedback.md).
3. Apply the [macron-only convention](macron-convention.md) when writing the diacritic-spelling field for the new entry.

## 5.4.3 Related
- [SAP Diacritics Policy](sap-policy.md) – the rule for prose: no diacritics in body text, headings, captions, names.
- [Macron-Only Convention](macron-convention.md) – the rule the `diacriticSpelling` column applies, for use in verse transliterations.
- [Italics §3.6.4 Shlokas, Padas, and Other Quoted Verses](../editorial/italics.md#364-shlokas-padas-and-other-quoted-verses) – typographic treatment of verses.
