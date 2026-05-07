# Changelog

A record of substantial changes to the conventions in this guide. Routine edits (typos, formatting tweaks, examples) are tracked in the Git history but not here.

The format follows [Keep a Changelog](https://keepachangelog.com/). Versions are dated.

---

## [1.1] — 2026-05-07

### Added
- New **Concepts** section ([concepts/index.md](concepts/index.md)) — definitions of romanization, anglicization, translation, and transliteration, taken from the SAP Writing Guidelines (v1).
- New **Translation & Transliteration** section ([translation/index.md](translation/index.md), [translation-rules.md](translation/translation-rules.md)) — when to translate, when to transliterate, and when to use the OED spelling.
- New editorial pages: [Italics](editorial/italics.md), [Plurals](editorial/plurals.md), and [Quotation Marks](editorial/quotation-marks.md), all reproducing rules from the SAP Writing Guidelines (v1).
- New [SAP Diacritics Policy](diacritics/sap-policy.md) page documenting the official SAP rule: no diacritics in headings, body text, or legends; diacritics permitted in transliterations of verses.
- New **Open Discussions** section preserving the SAP Writing Guidelines' "Conventions to Discuss" — [Sanstha & Mandirs](discussions/sanstha-and-mandirs.md), [Gurus & Honorifics](discussions/gurus-and-honorifics.md), [Shastras](discussions/shastras.md), [Indic Words](discussions/indic-words.md), [Transliteration](discussions/transliteration.md), [Web — BrE or AmE?](discussions/web.md), [Base Style Manual](discussions/base-style-manual.md).

### Changed
- [Editorial — Capitalisation](editorial/capitalisation.md) rewritten to follow the SAP Writing Guidelines' rules; the previous draft is superseded.
- [Editorial — index](editorial/index.md) updated to include the three new pages and to surface the BrE/AmE question.
- [Diacritics — index](diacritics/index.md) now flags the **two-policy** situation: the official SAP rule (no diacritics in general text) vs the in-house macron-only convention (used in glossary and reference work). The two are scoped differently rather than contradictory.
- [Macron-Only Convention](diacritics/macron-convention.md) prefaced with a scope note clarifying that it applies to glossary and reference work, not to general-reader publications (which follow the SAP rule).
- [Home page](index.md) cards updated to include Concepts, Translation, and Open Discussions.

### Notes
- The two diacritic policies (SAP "no diacritics" vs in-house "macron-only") are presented as scoped-differently rather than reconciled into one rule. Whether the macron-only convention should ever appear in a finished general-reader publication is logged as an open question in [Open Discussions: Transliteration](discussions/transliteration.md).
- All new content reproducing SAP rules cites the source as "SAP Writing Guidelines (v1)" so the lineage is clear.

---

## [1.0] — 2026-05-07

### Added
- Initial scaffold of the style guide site.
- Editorial section with placeholders for tone, capitalisation, and punctuation.
- Diacritics section documenting the macron-only convention (carried over from the BAPS Glossary project, April 2026).
- InDesign section with placeholders for paragraph styles and master pages.
- EPUB Accessibility section drawing on the Bliss Jan–Feb 2026 alt-text work.
- Scripts & Tools section indexing `ArticleBuilder`, `AddAltText`, `SplitVachanamrut`, and `ExportToWord_Generic`.
- Workflows section with file versioning rules and naming conventions.
- Contributing guide explaining the pencil-icon edit flow.

### Established
- File versioning rule documented as non-negotiable: every output gets an incremented version (e.g. `v1.0` → `v1.1`), never overwritten. See [versioning rules](workflows/versioning.md).

---

<!--
Template for future entries — copy this above when adding a new release.

## [X.Y] — YYYY-MM-DD

### Added
-

### Changed
-

### Deprecated
-

### Removed
-
-->
