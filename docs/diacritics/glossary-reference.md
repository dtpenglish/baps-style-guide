# 5.4 Glossary Reference
The master glossary is a **reference repository** that records, for each BAPS term:

- the **plain-Roman** spelling (used in prose, headings, captions),
- the **macron-only diacritic** spelling, where appropriate, for use in **bhajan and scripture-verse transliterations** only,
- the word class, definition, source language, and any usage notes.

Before introducing or correcting a term in any publication, check the glossary first.

!!! tip "Diacritic spellings are for verses, not prose"
    The `diacriticSpelling` column is what to use when transliterating a *bhajan*, *shloka*, *pada*, or other verse content where the macron helps the reader pronounce the term. **In prose text** – body paragraphs, headings, photo captions, footnotes, titles – use the plain-Roman headword. Diacritics are not preferred in prose. See [SAP Diacritics Policy](sap-policy.md).

## 5.4.1 Where It Lives
The current master file is:

```
glossary-all-2026-04-15_v1.2.xlsx
```

It contains 1,586 rows covering Sanskrit, Gujarati, and Hindi terms used across BAPS publications. Columns:

| Column | Contents | When to use |
|---|---|---|
| `term` | The plain-Roman headword (e.g. *sadhu*) | **Prose, headings, captions** – the default in every general-reader publication |
| `wordClass` | Part of speech (noun, proper noun, verb, etc.) | Reference |
| `diacriticSpelling` | Macron-only spelling, where applicable (e.g. *sādhu*) | **Bhajan and scripture-verse transliterations only** |
| `definition` | Brief gloss for editorial reference | Reference |
| `sourceLanguage` | Sanskrit / Gujarati / Hindi | Reference |
| `notes` | Usage notes, alternative spellings, cross-references | Reference |

!!! note "Path"
    The file path is internal to the DTP team's working drives. Ask the maintainer for the current location if you need direct access. The glossary itself is not stored in this site's repository – only this reference page is.

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
4. See [Italics §3.5.4 Shlokas, Padas, and Other Quoted Verses](../editorial/italics.md#354-shlokas-padas-and-other-quoted-verses) for the typographic treatment.

**Names – never with diacritics, in either context:**

Personal names, place names, organization names, and titles of works are spelled in plain Roman both in prose and in verse transliterations. See [SAP Diacritics Policy §5.2.2](sap-policy.md#522-names-never-with-diacritics).

**For new terms not in the glossary:**

1. Check that it isn't a variant spelling of an existing entry. *Sadguru*, *Sadgurū*, and *Satguru* should not all become separate rows.
2. Propose an addition via [Feedback](../feedback.md).
3. Apply the [macron-only convention](macron-convention.md) when writing the diacritic-spelling field for the new entry.

## 5.4.3 Updating the Glossary
The glossary is versioned separately from this style guide. The current scheme (as of April 2026):

- Filename pattern: `glossary-all-YYYY-MM-DD_vX.Y.xlsx`
- Each substantive update bumps the version (`v1.2` → `v1.3`).
- Major restructures (column changes, scope changes) bump the major version (`v1.x` → `v2.0`).
- Old versions are retained – never overwritten. See [versioning rules](../workflows/versioning.md).

Changes to conventions that the glossary embodies – for instance, a decision to start marking long *i* – should be documented in this style guide's [changelog](../changelog.md) before being applied to the glossary file.

## 5.4.4 Related
- [SAP Diacritics Policy](sap-policy.md) – the rule for prose: no diacritics in body text, headings, captions, names.
- [Macron-Only Convention](macron-convention.md) – the rule the `diacriticSpelling` column applies, for use in verse transliterations.
- [Italics §3.5.4 Shlokas, Padas, and Other Quoted Verses](../editorial/italics.md#354-shlokas-padas-and-other-quoted-verses) – typographic treatment of verses.
- [Versioning Rules](../workflows/versioning.md) – why the glossary filename always carries a version.
