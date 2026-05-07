# Glossary Reference
The master glossary is the authoritative source for spelling, diacritics, and word class of BAPS terminology in Roman script. Before introducing or correcting a term in any publication, check the glossary first.

## Where It Lives
The current master file is:

```
glossary-all-2026-04-15_v1.2.xlsx
```

This contains 1,586 rows covering Sanskrit, Gujarati, and Hindi terms used across BAPS publications. Columns include:

| Column | Contents |
|---|---|
| `term` | The plain-Roman headword |
| `wordClass` | Part of speech (noun, proper noun, verb, etc.) |
| `diacriticSpelling` | Macron-only spelling (e.g. *sādhu*) |
| `definition` | Brief gloss for editorial reference |
| `sourceLanguage` | Sanskrit / Gujarati / Hindi |
| `notes` | Usage notes, alternative spellings, cross-references |

!!! note "Path"
    The file path is internal to the DTP team's working drives. Ask a maintainer for the current location if you need direct access. The glossary itself is not stored in this site's repository — only this reference page is.

## How to Use It
**For routine editorial work:**

1. Encounter a term in your text — say, *gunatitanand*.
2. Search the glossary for the headword.
3. Use the spelling from the `diacriticSpelling` column in your publication.
4. If the term has a usage note, follow it.

**For new terms not in the glossary:**

1. Check that it isn't a variant spelling of an existing entry. *Sadguru*, *Sadgurū*, and *Satguru* should not all become separate rows.
2. Propose an addition via the team's glossary update process.
3. Apply the [macron-only convention](macron-convention.md) when writing the diacritic spelling.

## Updating the Glossary
The glossary is versioned separately from this style guide. The current scheme (as of April 2026):

- Filename pattern: `glossary-all-YYYY-MM-DD_vX.Y.xlsx`
- Each substantive update bumps the version (`v1.2` → `v1.3`).
- Major restructures (column changes, scope changes) bump the major version (`v1.x` → `v2.0`).
- Old versions are retained — never overwritten. See [versioning rules](../workflows/versioning.md).

Changes to conventions that the glossary embodies — for instance, a decision to start marking long *i* — should be documented in this style guide's [changelog](../changelog.md) before being applied to the glossary file.

## Related
- [Macron-Only Convention](macron-convention.md) — the rule the `diacriticSpelling` column applies
- [Versioning Rules](../workflows/versioning.md) — why the glossary filename always carries a version
