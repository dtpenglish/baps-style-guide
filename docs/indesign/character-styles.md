# 6.3 Character Styles
!!! info "Draft page"
    Document the character-style conventions used across our standard publication templates. Add screenshots from the Character Styles panel where helpful.

## 6.3.1 Why We Standardise
Character styles apply formatting to **runs of text within a paragraph** — italics for transliterations, small caps for V.S. dates, bold for emphasis, run-in heads at the start of a paragraph, drop caps, footnote references, and similar inline treatments.

Standardised character styles:

- Make global formatting changes (italic font, small-cap design, emphasis colour) take seconds instead of hours.
- Drive correct EPUB export — every character style maps to an HTML inline element (`em`, `strong`, `span` with class) and contributes to semantic markup.
- Keep typographic treatment of recurring elements (Indic transliterations, scripture references, *V.S.* dates) consistent across publications.

## 6.3.2 Suggested Naming Pattern
A common convention is `Element.Variant`:

| Style name | Use |
|---|---|
| `Italic.Indic` | Italicised Indic terms (*sadhu*, *darshan*) |
| `Italic.Title` | Italicised titles of works (*Vachanamrut*, *Shikshapatri*) |
| `Italic.Emphasis` | English emphasis (use sparingly) |
| `Bold.Term` | Bolded term being defined |
| `SmallCaps.VS` | Small-cap *V.S.* before a Vikram Samvat year |
| `RunInHead.Default` | Run-in heading that opens a paragraph |
| `DropCap.Default` | Drop cap at the start of a section |
| `Footnote.Ref` | Footnote-reference superscript |

The dot-separated naming sorts cleanly in the Character Styles panel and groups related styles visually.

## 6.3.3 Italic.Indic — the Workhorse Style
The most-used character style in BAPS publications is the one that italicises non-anglicised Indic terms in the body text. The rule that determines what gets italicised lives at [3.6 Italics](../editorial/italics.md); the character style is what applies it consistently.

Apply `Italic.Indic` to non-OED Indic terms (*dandvat*, *kothari*, *patshala*) and the fortnight designators *sud* / *vad*. Don't apply it to anglicized Indic terms (*dharma*, *guru*, *yoga*) or to proper nouns (names, places, festivals, tithis).

## 6.3.4 To Document for Our Publications
- The full character-style hierarchy for each long-form publication template.
- Cross-publication reusable styles.
- Style mapping for EPUB export (which character styles map to which HTML inline elements).

Contributions welcome — see [Feedback](../feedback.md) to suggest naming changes before they're applied.

## 6.3.5 See Also
- [Paragraph Styles](paragraph-styles.md) – paragraph-level style hierarchy.
- [3.6 Italics](../editorial/italics.md) – when to italicise (the rule that `Italic.Indic` mechanically applies).
