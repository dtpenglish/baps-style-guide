# BAPS SAP Style Guide
Welcome to the in-house style guide for the BAPS Swaminarayan Aksharpith (SAP) publishing team. SAP publishes books, magazines, newsletters, and other literature predominantly in Gujarati, English, and Hindi for a general *satsangi* readership.

Most of our English-language work consists of **translations from Gujarati source texts**. Smaller proportions involve Sanskrit material (typically scriptural verses and commentaries embedded in larger Gujarati→English projects) and Hindi material (similarly embedded). A significant body of work is also written **originally in English**.

This site documents the editorial, design, and production conventions for all of that – across Sanskrit, Gujarati, Hindi, and English material. It does **not** cover general English grammar (Garner / Fowler / CMS handle that), but the recurrent patterns SAP editors fix in BAPS manuscripts — Indian-English usages, Gujarati-translation calques, devotional-register issues — are documented in [Part 11 Common Editorial Pitfalls](pitfalls/index.md).

!!! tip "How to use this guide"
    Use the search bar (top right, or press <kbd>/</kbd>) to find a rule or term quickly. Browse the navigation tabs above to read sections in order. Found something out of date or unclear? See [Feedback](feedback.md) – one click sends an email to the maintainer.

## I Need To…
Common entry points organized by task, not topic:

- **… decide whether to italicize a term** → [3.6 Italics](editorial/italics.md) (with decision tree)
- **… decide whether to capitalize a term** → [3.3 Capitalization](editorial/capitalization.md) (with decision tree)
- **… decide whether to use diacritics** → [5 Diacritics](diacritics/index.md) (with decision tree)
- **… check the comma rule for *i.e.* / *e.g.* / *etc.*** → [3.12.7](editorial/abbreviations.md#3127-commas-with-ie-eg-and-etc)
- **… place a footnote superscript correctly** → [3.11 Footnotes](editorial/footnotes.md)
- **… cite a book, article, website, or scripture** → [3.15 Citations & References](editorial/citations.md)
- **… set the title of a book or chapter** → [3.4 Title Case in Detail](editorial/title-case.md)
- **… look up a specific topic A–Z** → [Quick Find](quick-find.md)
- **… set up an InDesign character style** → [6.3 Character Styles](indesign/character-styles.md)
- **… draft alt text for an image** → [7.2 Alt Text](epub/alt-text.md)
- **… version a script file or Word document** → [9.2 File Versioning](workflows/versioning.md)
- **… run one of our JSX scripts** → [8.2 JSX Scripts Reference](scripts/jsx-reference.md)
- **… send a correction to the maintainer** → [Feedback](feedback.md)

## Recently Updated
Hand-curated; full history in the [Changelog](changelog.md).

- **2026-05-13** – Quick Find A–Z index added; long chapters split into focused pages (Editorial now 14 chapters instead of 9).
- **2026-05-13** – Left sidebar now shows every numbered subsection (`toc.integrate` enabled).
- **2026-05-13** – Reversed the *i.e.* / *e.g.* trailing-comma rule to follow BrE convention (see [3.12.7](editorial/abbreviations.md#3127-commas-with-ie-eg-and-etc)).
- **2026-05-13** – Footnote dash exception clarified for the spaced en dash (see [3.11.2](editorial/footnotes.md#3112-footnote-numbers-with-colons-semicolons-and-other-punctuation)).
- **2026-05-13** – *Earth* / *earth* expanded with theological-context examples (see [3.3.2.3](editorial/capitalization.md#3323-earth-earth)).

## Sections at a Glance
<div class="grid cards" markdown>

-   :material-school-outline: __Foundational Concepts__

    ---

    Romanization, anglicization, translation, and transliteration – the four terms the rest of this guide depends on.

    [:octicons-arrow-right-24: Concepts](concepts/index.md)

-   :material-translate: __Translation & Transliteration__

    ---

    When to translate, when to transliterate, and when to use the OED.

    [:octicons-arrow-right-24: Translation rules](translation/index.md)

-   :material-pencil-outline: __Editorial__

    ---

    Tone, capitalization, italics, plurals, quotation marks, and punctuation for prose across our publications.

    [:octicons-arrow-right-24: Editorial conventions](editorial/index.md)

-   :material-moon-waxing-crescent: __Tithis__

    ---

    The 16 named days of the lunar fortnight – *Padvo*, *Bij*, *Ekadashi*, *Punam*, *Amas* – and the *sud* / *vad* fortnight designators. Roman, capitalized, no italics, no diacritics.

    [:octicons-arrow-right-24: Tithis rule](tithis/index.md)

-   :material-format-letter-matches: __Diacritics__

    ---

    The SAP rule (no diacritics in general text) and the in-house macron-only convention for glossary work.

    [:octicons-arrow-right-24: Diacritic rules](diacritics/index.md)

-   :material-file-document-outline: __InDesign__

    ---

    Paragraph styles, master pages, and production patterns for our long-form publications.

    [:octicons-arrow-right-24: InDesign conventions](indesign/index.md)

-   :material-book-open-page-variant: __EPUB Accessibility__

    ---

    Alt text writing, Articles panel hygiene, and reading-order standards for accessible EPUBs.

    [:octicons-arrow-right-24: EPUB guidelines](epub/index.md)

-   :material-code-tags: __Scripts & Tools__

    ---

    Reference for our JSX scripts (`ArticleBuilder`, `AddAltText`, `ExportToWord_Generic`).

    [:octicons-arrow-right-24: Scripts reference](scripts/index.md)

-   :material-folder-cog-outline: __Workflows__

    ---

    File versioning rules, naming conventions, and production handoff patterns.

    [:octicons-arrow-right-24: Workflow conventions](workflows/index.md)

-   :material-comment-question-outline: __Open Discussions__

    ---

    Conventions the team has not yet settled – Sanstha names, mandir names, gurus, transliteration choices, and more.

    [:octicons-arrow-right-24: Open questions](discussions/index.md)

-   :material-alert-circle-outline: __Common Editorial Pitfalls__

    ---

    Indian-English usages, Gujarati-translation calques, and devotional-register issues SAP editors fix recurrently in BAPS manuscripts.

    [:octicons-arrow-right-24: Pitfalls](pitfalls/index.md)

</div>

## Core Principles
Three rules underpin everything else in this guide:

1. **Consistency over cleverness.** A reader should encounter the same term, the same diacritic, the same heading style every time. Where this guide and instinct disagree, follow the guide and propose an edit if it's wrong.
2. **Versioning is non-negotiable.** Every file output – script, Word doc, Excel, PDF – gets an incremented version number in the filename and an internal version string. Never overwrite. See [versioning rules](workflows/versioning.md).
3. **Accessibility is editorial.** Alt text, reading order, and structural markup are not technical afterthoughts – they are part of the writing. See [EPUB accessibility](epub/index.md).

## Recently Updated
The "last updated" date at the bottom of every page reflects the most recent commit. Major changes to conventions are recorded in the [changelog](changelog.md).

## Contributing
This guide is maintained collaboratively by the BAPS DTP team. Anyone on the team can suggest changes – see [Feedback](feedback.md) to send a note to the maintainer.
