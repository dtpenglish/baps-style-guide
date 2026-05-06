# Paragraph Styles

!!! info "Draft page"
    Document the paragraph-style hierarchy used in Vachanamrut, Bliss, and our standard publication templates. Add screenshots from the Paragraph Styles panel where helpful.

## Why we standardise

Paragraph styles are the single most important production tool we have. Consistent, well-named styles:

- Make global changes (font, spacing, leading) take seconds instead of hours.
- Drive correct EPUB export — every style maps to a CSS class and contributes to the document's structural semantics.
- Allow our scripts (`ArticleBuilder`, `AddAltText`) to reason about the document programmatically.

## Suggested naming pattern

A common convention is `Section.Element.Variant`:

| Style name | Use |
|---|---|
| `Body.Default` | Default body paragraph |
| `Body.FirstLine` | First paragraph of a section (no first-line indent) |
| `Heading.H1` | Section title |
| `Heading.H2` | Subsection title |
| `Caption.Image` | Photo caption |
| `Footnote.Default` | Footnote body |

The dot-separated naming sorts cleanly in the Paragraph Styles panel and groups related styles visually.

## To document for our publications

- The full Vachanamrut 4E style hierarchy
- The Bliss magazine style hierarchy
- Cross-publication reusable styles
- Style mapping for EPUB export (which paragraph styles map to which HTML tags)

Contributions welcome — use the pencil icon, or open an issue to discuss naming changes before applying them.
