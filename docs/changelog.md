# Changelog
A record of substantial changes to the conventions in this guide. Routine edits (typos, formatting tweaks, examples) are tracked in the Git history but not here.

The format follows [Keep a Changelog](https://keepachangelog.com/). Versions are dated.

---

## [1.21] – 2026-05-08

### Changed
- **Em dash dropped; spaced en dash takes its role.** SAP convention is now: hyphen for simple compounds, **unspaced en dash** (`–`) for ranges, place pairs, and complex compounds, and **spaced en dash** (` – `) for parenthetical breaks. The em dash (`—`) is **not used**.
- All 471 existing spaced em dashes across 41 files (the entire site, plus `READ_ME.md` and `CLAUDE.md`) replaced with spaced en dashes. Done by bulk substitution (` — ` → ` – `).
- **3.9.2 Dashes** rewritten: table now lists hyphen and en dash only; en dash has four rows (ranges, place pairs, complex compounds, parenthetical breaks) showing the unspaced-vs-spaced distinction.
- **3.9.5 Spacing** reworded: "one space on each side of an en dash used for a parenthetical break" replaces the old em-dash spacing note.
- **3.9.11 Open Questions** – the open question 'Spaced or unspaced em dashes in print?' removed (resolved by the new rule).
- **CLAUDE.md** locked-in punctuation rule updated.

---

## [1.20] – 2026-05-08

### Changed
- **Site-wide quote sweep.** Double-quoted highlights converted to single quotes per the new 3.9.1 rule (single curly = primary mark for highlighting; double curly = speech only). Affected files: `epub/alt-text.md` (table examples + UI labels), `editorial/italics.md` (Decision Summary table), `editorial/tone-and-voice.md` (example sentences), `editorial/capitalization.md` (counter-examples), `editorial/punctuation.md` (vitamin-C example sentences), `tithis/index.md` (CMS quotations), `discussions/shastras.md` ('Shri' heading), `discussions/base-style-manual.md` ('Adopt a Base' heading + interpretation), `workflows/file-naming.md` (bad filename examples), and the changelog itself (where section names were quoted as text).
- **Speech examples kept double** in [3.8.1.3 Quoted Speech](editorial/quotation-marks.md#3813-quoted-speech-double-quotes) per the new rule. MkDocs admonition titles (`!!! tip "..."`) also unchanged – that's MkDocs syntax, not content quotation.
- **BrE spelling sweep.** Two AmE spellings updated to BrE forms:
  - `dialog` → `dialogue` (4 occurrences in `scripts/jsx-reference.md`).
  - `catalog-style` → `catalogue-style` (`editorial/punctuation.md`).
- The Oxford -ize rule (already locked in) is preserved; words covered by it (*emphasize*, *italicize*, *organize*, etc.) are not affected.

### Notes
- A few apostrophe-as-elision cases (e.g. `'60s`, `'80s`) may render with the wrong direction via smarty's heuristic – flag any you spot and they'll get explicit Unicode.

---

## [1.19] – 2026-05-08

### Changed
- **Quotation-mark convention flipped.** SAP now uses **single curly quotes ' '** as the **primary** mark – for highlighting a term in special sense, mottoes presented as phrases, glosses of Indic terms, titles of short works, and quoted excerpts of authoritative text. **Double curly quotes " " are reserved for direct speech / dialogue only.** Previously double was the primary mark (CMS / AmE-style); the new convention is BrE-style.
- **Typographers' (curly) quotes throughout the site.** The `smarty` markdown extension is now enabled in `mkdocs.yml`, so straight `'` and `"` in source files render as the curly forms ' ' " " automatically. Smart-dashes and smart-ellipses are disabled – those continue to use real Unicode characters typed directly.
- **3.9.1 Quotation Marks** rule rewritten with the new single-primary / double-for-speech convention.
- **3.8 Quotation Marks for Indic Terms** updated to apply the new convention:
  - 3.8.1.2 *Translation Clarified* – single quotes around the gloss (was double).
  - 3.8.1.3 *Quoted Speech* – double quotes for actual speech, single for any nested gloss inside.
  - 3.8.1.4 *Mottoes / Slogans* – split into two cases: motto presented as a phrase = single; motto spoken aloud in narrative = double (speech rule).
  - 3.8.4 *Terms Used in a Special Sense* – *'soft launch'* now in single quotes (was double).
- **CLAUDE.md locked-in rules** updated.

### Fixed
- Stale link in changelog 1.8 entry pointing to `contributing.md` (now `feedback.md`) repaired.

### Notes
- Existing site content with double-quoted highlights (e.g. quoting a rule, scare quotes) will still render – the rendered marks become curly. Per the new rule, those should gradually shift to single quotes. Speech examples are unchanged.

---

## [1.18] – 2026-05-08

### Removed
- **GitHub Issues references removed site-wide.** Feedback now routes exclusively through the [Feedback](feedback.md) mailto channel. Affected:
  - `feedback.md` – secondary 'Open a GitHub Issue' button removed; section 12.2 collapsed.
  - All 7 discussion pages with a *Have an opinion?* line – the "or open a GitHub Issue" option dropped; replaced with subject-line guidance for the Feedback email (e.g. *Subject: Translit: jn vs gn*).
  - `discussions/index.md` – "or open a GitHub Issue" removed.
  - `diacritics/index.md` – open-question link to GitHub Issues replaced with Feedback.
  - `macron-convention.md` – issue-tracker link replaced with Feedback.
  - `tone-and-voice.md` – both GitHub Issue references replaced with Feedback.
  - `READ_ME.md` – alternative-GitHub-Issue clause removed; Feedback is now the sole channel.
  - `CLAUDE.md` – open-question routing updated to Feedback.
- **"Made a decision in a meeting?" reframed** in `discussions/index.md` to "Decision reached?" – meetings aren't the documented path; the maintainer simply records the decision when it's made.

### Why
The team's feedback flow is centralized on the email-to-maintainer channel. Multiple channels (mailto + GitHub Issues + meetings) created ambiguity about where suggestions should go. One channel = one inbox to track.

---

## [1.17] – 2026-05-08

### Changed
- **Diacritics scope clarified site-wide.** The macron-only convention is now framed explicitly as applying in **two contexts only**: (a) the [BAPS master glossary](diacritics/glossary-reference.md), where the `diacriticSpelling` column is recorded **for reference**, and (b) **bhajan and scripture-verse transliterations** (*shlokas*, *padas*) within publications. **Diacritics are not preferred in prose text** – body, headings, captions, footnotes, names, titles all stay plain-Roman per the [SAP Diacritics Policy](diacritics/sap-policy.md).
- **5.4 Glossary Reference** rewritten with explicit guidance: use the `term` (plain-Roman) column for prose; use `diacriticSpelling` (macron-only) only when transliterating a verse. Names use the plain form even within verses.
- **5.3 Macron-Only Convention** scope intro tightened. 5.3.8 (Italicization) reframed and now warns explicitly that names never carry diacritics, in either prose or verse contexts.
- **5.2 SAP Diacritics Policy** wording tightened: verses called out specifically as "bhajan and scripture-verse transliterations (*shlokas*, *padas*)". Notes that the BAPS in-house default for verse transliterations is the macron-only convention. Cross-references to the glossary's prose vs verse columns added.
- **5.1 Diacritics & Transliteration** index – Quick Decision table reorganized; bhajan/verse row added separately from glossary row; "names never carry diacritics, even in verses" stated explicitly.
- **3.5.4 Shlokas, Padas, and Other Quoted Verses** in [Italics](editorial/italics.md): now points to the macron-only convention as the BAPS default for verse transliterations and to the glossary as the source of each verse term's spelling.

---

## [1.16] – 2026-05-08

### Changed
- **Site is read-only for visitors.** The edit-pencil icon (`content.action.edit`) has been disabled in `mkdocs.yml`. Visitors no longer see an "edit this page" affordance.
- **Contributing renamed to Feedback** ([docs/contributing.md](feedback.md) → [docs/feedback.md](feedback.md)). The page is now a one-click mailto-the-maintainer flow rather than a how-to-edit-via-pencil walkthrough. Pre-fills subject and a structured body for the email; provides a secondary GitHub Issue option for users with accounts.
- **Pencil-icon mentions removed across the site** – 16 occurrences across the home page, downloads, all 8 discussion pages, tone-and-voice (3.2), paragraph-styles (6.2), and the repo READ_ME. Each replaced with a pointer to the new Feedback page (mailto link), keeping the existing GitHub Issue option as a secondary path.
- READ_ME.md updated to reflect the read-only model and to list the maintainer's edit paths (GitHub web editor, github.dev, local clone, Claude Code).

### Why
Edit access is restricted to the maintainer, so visible "edit" affordances were misleading: clicking the pencil routed visitors through GitHub's fork-and-PR flow, which only collaborators could merge. Replacing the affordance with a mailto-feedback link means every team member – with or without a GitHub account – has a clear way to suggest changes.

---

## [1.15] – 2026-05-08

### Removed
- **Resolved discussion topics removed from the discussions pages.** Each topic below has been settled and is now documented in the relevant editorial section; keeping a parallel 'Resolved' entry under [10.x](discussions/index.md) was duplicative.
  - **10.3.1** – *Supreme* / *Sarvopari* and the resolved tip removed (rule lives at [3.3.2.10](editorial/capitalization.md#33210-the-definite-article-with-unique-theological-designations) and [3.4.1.1](editorial/doctrinal-titles.md#3411-rule-1-proper-nouns-and-formal-doctrinal-titles-capitalize-everything)).
  - **10.3.6** – *Sant* / *Satpurush* (full section) removed (rule lives at [3.4.1.1](editorial/doctrinal-titles.md#3411-rule-1-proper-nouns-and-formal-doctrinal-titles-capitalize-everything) and [3.4.1.2](editorial/doctrinal-titles.md#3412-rule-2-generic-descriptions-of-qualities-or-states-all-lowercase)).
  - **10.6.11** – Italicizing mixed phrases (full section) removed (rule lives at [3.5.1.5](editorial/italics.md#3515-multiword-sanskrit-and-indic-phrases-italicize-the-whole-phrase)).
  - **10.6.13** – Capitalization / italicization of tithis (full section) removed (rule lives at [Tithis Part 4](tithis/index.md)).

### Changed
- **10.3.x renumbered** after 10.3.6 was removed: Anglophone Honorifics 10.3.7 → 10.3.6; Sadhus 10.3.8 → 10.3.7; Have an Opinion 10.3.9 → 10.3.8.
- **10.6.x renumbered** after 10.6.11 and 10.6.13 were removed: 10.6.12 → 10.6.11; 10.6.14 → 10.6.12; 10.6.15 → 10.6.13; 10.6.16 → 10.6.14; 10.6.17 → 10.6.15; 10.6.18 → 10.6.16; 10.6.19 → 10.6.17; 10.6.20 → 10.6.18; 10.6.21 → 10.6.19.
- 4.7 in [Tithis](tithis/index.md): removed the line pointing back to discussions §10.6.13 (now obsolete).

---

## [1.14] – 2026-05-07

### Added
- **Part 11 [Downloads](downloads/index.md)** – new top-level section where the team can place JSX scripts, InDesign templates, glossary downloads, and other working files for users to download. Files are placed in `docs/downloads/files/`; a table on the page describes each entry.

### Changed
- **Contributing renumbered from Part 11 to Part 12** to make room for the new Downloads section.
- **InDesign 6.1**, **Scripts 8.1**, **Scripts 8.2**, **Workflows 9.2**, **Workflows 9.3** – removed references to the Sidekick MCP plugin, Cowork, the local `E:\AVDWork\` drive paths, and specific working-file names that were tied to one team member's environment. The pages now describe the InDesign / Scripts environment in portable, environment-neutral terms, and point to Downloads for the latest script versions.

---

## [1.13] – 2026-05-07

### Added
- **3.9.6.1 Footnote Numbers with Colons and Semicolons** – superscript goes *before* a colon or semicolon (BrE convention); commas and full stops still take the superscript after.
- **3.9.6.2 Footnote Numbers with Quoted Material** – handling for the three cases: footnote referring to quoted material (after closing quote), to a specific word inside the quote (immediately after that word), and to the whole sentence ending with a quotation (after final punctuation).
- **10.6.4 dental vs. retroflex *t* / *d*** – added as another open transliteration variant. South-Indian convention distinguishes *t* (retroflex ट) from *th* (dental त) and *d* / *dh* similarly; SAP follows the North-Indian / Hunterian convention (*t* and *d* for both), accepting the dental/retroflex ambiguity. Mostly relevant for Sanskrit/Hindi material.

### Notes
- The basic CMS-aligned footnote rule (3.9.6) is preserved unchanged: after punctuation when the note refers to the whole sentence; before punctuation when it refers to a specific word.

---

## [1.12] – 2026-05-07

### Added
- **[3.9.10 Commas with *such as* and *like*](editorial/punctuation.md#3910-commas-with-such-as-and-like)** – new section with four subsections covering the restrictive/nonrestrictive comma rule (*Citrus fruits, such as oranges, are high in vitamin C* vs *Trees such as oaks and elms don't grow at this altitude*); the *such as* (inclusion) vs *like* (comparison) distinction; the no-colon-after-*such as* rule; and a guideline that 1–3 examples is the comfortable range, longer lists should become vertical lists.

### Changed
- **3.9.9.6** enriched with degree-abbreviation forms – no-periods style (*BA*, *BSc*, *MA*, *MSc*, *PhD*, *MBA*, *MD*, *EdD*) cross-referencing the existing rule in 3.9.7.1, and a SAP BrE-default note (*MSc* not *MS*; *MA* not *M.A.*; *PhD* fine in either variety).
- 3.9.10 Open Questions renumbered to 3.9.11 to make room for "Commas with *such as* and *like*".

---

## [1.11] – 2026-05-07

### Added
- **[3.9.9 Apostrophes](editorial/punctuation.md#399-apostrophes)** – new section with seven subsections covering possessives of singular nouns (Chicago/Oxford rule: *'s* even on names ending in *s* – *Dickens's*, *Hopkins's*); plurals (apostrophe-only on *s*-ending plurals; *'s* on plurals not ending in *s* like *children's*); plural-form names and uninflected nouns (*the United States'*, *politics'*); plurals of single letters (*p's and q's*) vs multi-letter abbreviations; possessive vs attributive in names (*Mother's Day* vs *Veterans Day*); apostrophes in degrees (*bachelor's degree* but *Bachelor of Arts*) and omitted-year forms (*the '60s*, *the class of '75*); and what an apostrophe doesn't do (no *apple's for sale*).
- **[3.9.7.7 Commas with *i.e.*, *e.g.*, and *etc.*](editorial/punctuation.md#3977-commas-with-ie-eg-and-etc)** – new subsection: comma before and after *i.e.* / *e.g.* (Oxford-aligned, retained for formal and devotional clarity); *etc.* takes a comma before it after a list of 3+ items, comma after it only when the sentence continues; never *and etc.*
- **[3.5.2 exception](editorial/italics.md#352-punctuation-adjacent-to-italicized-phrases)** – punctuation that is part of an italicized title (e.g. *Who's Afraid of Virginia Woolf?*, *Help!*) should be italicized along with the title. Default rule (punctuation in surrounding-text font) is unchanged.

### Changed
- 3.9.9 Open Questions renumbered to 3.9.10 to make room for 'Apostrophes'.
- CLAUDE.md locked-in rules: added apostrophe rule, comma-with-Latin-abbreviations rule.

---

## [1.10] – 2026-05-07

### Added
- **[3.9.8 Vertical Lists](editorial/punctuation.md#398-vertical-lists)** – new section covering bullets vs numbers vs letters, parallel construction, and three punctuation/capitalization styles (continuation lists with lowercase + commas + final period; full-sentence lists with caps + periods + no *and*/*or*; standalone catalog-style lists with caps + no end punctuation, the SAP default). Plus the colon-vs-no-punctuation rule for introducing a list.
- **[3.3.3 Title Case in Detail](editorial/capitalization.md#333-title-case-in-detail)** – new section covering what to capitalize and lowercase in titles; hyphenated words in titles (*High-Quality Web Services*, *Anti-inflammatory Dieting*); the first word after a colon; prepositions in phrasal verbs (*Back Up*, *Turn Down*); open compounds; and the sentence-case vs title-case distinction.
- **3.3.2.13 Terms of Address** – direct address (*Sergeant*, *Your Honor*) and family relationships (*Father*, *Mom*) capitalized when standing in for a name; lowercase when preceded by an article or possessive.
- **3.3.2.14 Ages and Time Periods** – capitalize established names (*the Bronze Age*, *the Renaissance*, *the Vedic Period*); lowercase descriptive periods (*ancient Greece*, *the colonial period*).
- **3.3.2.15 Adjectives before Capitalized Nouns** – general English rule that descriptive adjectives are not capitalized just because the noun is (*the big Apple*, *the tall Eiffel Tower*); the exception for adjectives that are part of an established proper noun, formal title, or epithet.
- **3.3.2.16 Definitions Use Sentence Case** – the term being defined uses title case; the definition itself uses sentence case (*Param-Bhagvat Sant – Ideal sadhu of God, referring to the Satpurush.*).

### Changed
- 3.3.3 Open Questions renumbered to 3.3.4 to make room for new 'Title Case in Detail' section.
- 3.3.4 See Also renumbered to 3.3.5.
- 3.9.8 Open Questions renumbered to 3.9.9 to make room for 'Vertical Lists'.

---

## [1.9] – 2026-05-07

### Added
- **[3.7.5 Compound Modifiers and Unit Spacing](editorial/numbers.md#375-compound-modifiers-and-unit-spacing)** – seven new subsections covering hyphenation of written-out compound numerals (*twenty-nine*), hyphenation in compound adjectives (*two-car family*, *five-kilometre trek*, *18th-century novel*), no-hyphen rule before symbols and metric units (*30% increase*, *5 km trail*, *100 °C thermometer*), singular form in compound modifiers (*10-foot tree*, not *10-feet*), no-hyphen rule with possessive nouns (*one week's pay*), space between number and unit (*5 km*, *32 °C*) with the plane-angle exception (*30° 22′ 8″*), and the rule for when the written-out number is itself a compound (*250 ml flask* over *two hundred and fifty millilitre flask*).
- **[3.9.7 Abbreviations and Acronyms](editorial/punctuation.md#397-abbreviations-and-acronyms)** – significantly expanded with six subsections: truncations vs contractions (period rule), acronyms vs initialisms, capitalization by length (≤5 letters all-caps; ≥6 initial-cap), articles before acronyms (*the BBC*, no article for *NATO*), first-mention spell-out convention, and plurals (*MEPs* not *MEP's*; *1920s*, *747s*).

### Notes
- Personal name initials follow the BrE convention: *TS Eliot*, *RK Narayan* – no spaces, no periods. The older *T. S. Eliot* form is acceptable.

---

## [1.8] – 2026-05-07

### Added
- **Home page** ([index.md](index.md)) – framing context: SAP work composition (most English work is Gujarati→English; Sanskrit/Hindi material typically embedded in those projects; significant English-original work) and a scope statement clarifying the guide doesn't cover general English grammar.
- **Translation index** ([translation/index.md](translation/index.md)) – same composition note in the section intro.
- **Contributing** (now [feedback.md](feedback.md), renamed in 1.16) – 'About the team' admonition acknowledging that most contributors learn on the job, framing the guide as a support tool rather than a gatekeeper.

---

## [1.7] – 2026-05-07

### Changed
- **Numbers rule shortened from 1–100 to 1–10.** [§3.7](editorial/numbers.md) now spells out whole numbers from *one* through *ten*; numerals from **11** onwards. Always numerals for measurements, ages, dates, percentages, currency, times, and statistics. The previous CMS-aligned rule (spell out 1–100) is superseded; AP-style is closer to current SAP practice.
- 3.7.4.2 (mixing words and numerals in a passage) now references the 11-threshold.

---

## [1.6] – 2026-05-07

### Changed
- **Rule 3 in [Doctrinal Titles](editorial/doctrinal-titles.md) flipped to cap-cap roman.** Previously, an adjective + reverential noun for the Satpurush set the adjective italic lowercase and the noun cap roman (e.g. *brahmaswarup* **Sadhu**, *gunatit* **Guru**). The rule is now: capitalize **both** the adjective and the noun, set roman – *Brahmaswarup Sadhu*, *Gunatit Guru*, *Pragat Guru*, *Divya Sadhu*. The qualifying adjective is treated as part of the doctrinal designation, not a quality descriptor.
- Distinction from Rule 2 (lowercase descriptive) now keys off the **noun**: reverential nouns for the Satpurush (Sadhu, Guru, Satpurush, Sant) take Rule 3; abstract nouns (state, devotion, understanding, lifestyle) take Rule 2.

### Added
- Eleven new editorial subsections covering proper adjectives (Hindu, Vedic, Puranic, Upanishadic, Gandhian, Socratic), *Yogic* vs *Yoga*, *Sampradaya*, historical titles (*the King of Kutch*), the definite article with unique theological designations (*the Supreme God*), *Satsang* as a doctrinal term, multiword Sanskrit phrases italicized as a unit (*ekantik dharma*, *murti puja*), *Swami* as a substitute for a specific name, descriptive sadhu phrases (*the God-realized sadhu*, *the true sadhu*) lowercase, and usage notes (*at* vs *in* with places, *detachment from*).

### Resolved
- **10.3.1** *Supreme* / *Sarvopari* – capitalized when functioning as a formal theological designation; lowercase when descriptive.
- **10.3.6** *Param Ekantik Sadhu / Sant* – capitalized as a formal designation (Rule 1).
- **10.3.6** *the Satpurush* vs *a satpurush* – cap when doctrinal designation, lowercase italic when descriptive common-noun usage.
- **10.6.11** Italicizing mixed phrases – italicize the entire phrase as a single foreign lexical unit.

---

## [1.5] – 2026-05-07

### Changed
- **Switched from flat to hierarchical section numbering** for stability when new pages are added. Top-level 'Parts' are now numbered 1–11; pages inside a Part take *Part.Chapter* (e.g. *3.3 Capitalization* under Editorial). H2s are *Part.Chapter.Section* (*3.3.1 Core Rules*); H3s are *Part.Chapter.Section.Sub* (*3.3.1.1*).
- Single-page Parts (Concepts = 1, Tithis = 4, Contributing = 11) keep two-level references: *1.1*, *1.1.1*.
- **Adding a new page in one Part no longer shifts numbers in other Parts** – references like *3.3.1* stay valid even if *Diacritics* (Part 5) gains new pages later. Previously, every chapter from 6 through 37 was at risk of shifting.

### Migration impact
- Any external citations to the old flat scheme (e.g. *6.4*) are now invalid. The site is days old and these were not yet in circulation, so the trade-off is acceptable.
- Numbering is regenerated by `number_sections.py`, which is now hierarchical and idempotent.

---

## [1.4] – 2026-05-07

### Added
- **CMS-style hierarchical section numbering** across the whole guide. Every page is now a numbered chapter (1–38), every H2 within is a numbered section (e.g. *6.1*, *6.2*), and every H3 is a numbered sub-section (e.g. *6.1.1*). Reference any rule precisely as *"see 6.1"* or *"per 13.4"*.
- Numbered nav labels for sub-pages within multi-page sections (e.g. *5. Tone & Voice*, *6. Capitalization*, *15. SAP Diacritics Policy*). Top-level tabs and single-page tabs (Concepts, Tithis, Contributing, Changelog) keep clean unprefixed labels – the chapter number is shown in the page H1.
- The changelog itself is **not** numbered (release versions like *1.4* are the natural anchor here).

### Notes
- If a page is added, removed, or reordered later, chapter numbers downstream of the change will shift. The numbering is regenerated by a script (`number_sections.py`) and is idempotent – running it strips and re-applies based on current nav order.

---

## [1.3] – 2026-05-07

### Changed
- **All headings** converted from sentence case to **Title Case** (CMS rules: capitalize the first/last word and all major words; lowercase articles, coordinating conjunctions, prepositions, and *to*).
- **All -ise / -isation / -ised / -ising** spellings converted to **-ize / -ization / -ized / -izing** (Oxford -ize style). Protected words (*advise*, *exercise*, *comprise*, *devise*, *supervise*, *surprise*, etc.) keep -ise. *Analyse* keeps -se per Oxford guidance (the only common -ise word that does not derive from Greek -izō).
- The *Capitalisation* nav label and page H1 are now *Capitalization*. The page filename (`capitalisation.md`) is unchanged to preserve URLs.

### Notes
- Spelling change applies to body prose, headings, and table cells across all 39 markdown files in `docs/`.
- A few headings preserve italic-lowercase mid-word – for example *Earth* / *earth*, *sud* and *vad*, *not* – because those italics are themselves the subject of the heading or carry intentional emphasis.

---

## [1.2] – 2026-05-07
### Added
- New **Tithis** section ([tithis/index.md](tithis/index.md)) – capitalization and italicization rule for the 16 tithis of the lunar fortnight, with CMS, Hart's, and OED references. Resolves the previously open question.
- New **Doctrinal Titles & Reverential Capitalization** page ([editorial/doctrinal-titles.md](editorial/doctrinal-titles.md)) – the four-rule system for adjective+noun phrases in BAPS English (e.g. *brahmaswarup Sadhu* vs *Pragat Brahmaswarup Mahant Swami Maharaj*).
- New **Numbers** page ([editorial/numbers.md](editorial/numbers.md)) – CMS rule: spell out one through one hundred and round multiples; numerals for measurements, statistics, ages, dates, percentages.

### Changed
- [Capitalization](editorial/capitalization.md) – added rules for *Earth* / *earth* and the preferred wording *cycles of birth and death*. Cross-link to the new doctrinal-titles page.
- [Punctuation](editorial/punctuation.md) – added footnote superscript placement (after sentence punctuation vs after a specific word), spacing rules (one space after a period; no space before a footnote superscript), abbreviation conventions (no periods in *BAPS*, *CMS*, *EPUB*; periods in *V.S.*, *e.g.*, *i.e.*). Removed the 'Draft page' banner. Refined dash table to mention complex compounds.
- [Italics](editorial/italics.md) – added 'Italics for English emphasis' (use sparingly) and 'Shlokas, padas, and other quoted verses' (italic transliteration + roman translation).
- [Quotation Marks](editorial/quotation-marks.md) – added rule for terms used in a special sense (double quotes on first use only; roman thereafter).
- [Tithis](tithis/index.md) – added documented CMS allowance: CMS itself permits the chosen capitalization as a religious-context style choice.

### Notes
- Items not incorporated because already settled or in conflict with existing rules: title capitalization, Oxford comma, religious-term capitalization, British English spellings, glossary formatting, and IAST diacritics in general text (conflicts with the SAP "no diacritics in general body text" rule).

---

## [1.1] – 2026-05-07
### Added
- New **Concepts** section ([concepts/index.md](concepts/index.md)) – definitions of romanization, anglicization, translation, and transliteration.
- New **Translation & Transliteration** section ([translation/index.md](translation/index.md), [translation-rules.md](translation/translation-rules.md)) – when to translate, when to transliterate, and when to use the OED spelling.
- New editorial pages: [Italics](editorial/italics.md), [Plurals](editorial/plurals.md), and [Quotation Marks](editorial/quotation-marks.md).
- New [SAP Diacritics Policy](diacritics/sap-policy.md) page documenting the official SAP rule: no diacritics in headings, body text, or legends; diacritics permitted in transliterations of verses.
- New **Open Discussions** section – [Sanstha & Mandirs](discussions/sanstha-and-mandirs.md), [Gurus & Honorifics](discussions/gurus-and-honorifics.md), [Shastras](discussions/shastras.md), [Indic Words](discussions/indic-words.md), [Transliteration](discussions/transliteration.md), [Base Style Manual](discussions/base-style-manual.md).

### Changed
- [Editorial – Capitalization](editorial/capitalization.md) rewritten; the previous draft is superseded.
- [Editorial – index](editorial/index.md) updated to include the three new pages and to surface the BrE/AmE question.
- [Diacritics – index](diacritics/index.md) now flags the **two-policy** situation: the official SAP rule (no diacritics in general text) vs the in-house macron-only convention (used in glossary and reference work). The two are scoped differently rather than contradictory.
- [Macron-Only Convention](diacritics/macron-convention.md) prefaced with a scope note clarifying that it applies to glossary and reference work, not to general-reader publications (which follow the SAP rule).
- [Home page](index.md) cards updated to include Concepts, Translation, and Open Discussions.

### Notes
- The two diacritic policies (SAP "no diacritics" vs in-house "macron-only") are presented as scoped-differently rather than reconciled into one rule. Whether the macron-only convention should ever appear in a finished general-reader publication is logged as an open question in [Open Discussions: Transliteration](discussions/transliteration.md).

---

## [1.0] – 2026-05-07
### Added
- Initial scaffold of the style guide site.
- Editorial section with placeholders for tone, capitalization, and punctuation.
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
Template for future entries – copy this above when adding a new release.

## [X.Y] – YYYY-MM-DD
### Added
-

### Changed
-

### Deprecated
-

### Removed
-
-->
