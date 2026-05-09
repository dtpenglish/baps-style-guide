# 6.4 Object Styles
!!! info "Draft page"
    Document the object-style conventions used across our standard publication templates. Add screenshots from the Object Styles panel where helpful.

## 6.4.1 Why We Standardise
Object styles apply formatting to **frames and other page items** — text frames, image frames, sidebars, callout boxes, decorative ornaments, footnote frames. Standardised object styles:

- Make global changes to spacing, stroke, fill, corner options, text-wrap, and frame-fitting take seconds instead of hours.
- Drive correct EPUB export — object styles control whether an item is *included*, *decorative*, or *anchored*, which directly affects the Articles panel and the screen-reader narration order.
- Keep recurring page elements (callout boxes, sidebars, image-with-caption blocks) visually consistent across publications.

## 6.4.2 Suggested Naming Pattern
A common convention is `Element.Variant`:

| Style name | Use |
|---|---|
| `TextFrame.Body` | Default body text frame |
| `TextFrame.Caption` | Photo-caption frame |
| `TextFrame.Sidebar` | Sidebar / pull-quote frame |
| `Image.Default` | Image frame with default fitting and stroke |
| `Image.FullBleed` | Full-bleed image frame (no stroke, edge-to-edge fit) |
| `Image.Decorative` | Decorative ornament — **marked decorative for EPUB**, no alt text |
| `Callout.Default` | Callout box with stroke, fill, and corner options |
| `Footnote.Frame` | Footnote-text frame |

The dot-separated naming sorts cleanly in the Object Styles panel and groups related styles visually.

## 6.4.3 Object Styles and EPUB Accessibility
The most consequential object-style choice for EPUBs is the **Object Export Options** setting — *Default*, *Custom*, or *Tagged Element*. When this is set on an object style (rather than per-instance), every frame using the style inherits the correct EPUB behaviour.

For images:

- Content images use `Image.Default` (or similar) with Object Export Options → Alt Text → *Custom* or *From Structure*. The `AddAltText.jsx` script (see [Scripts & Tools](../scripts/index.md)) populates these.
- Decorative images use `Image.Decorative` with Object Export Options → Alt Text → *Empty alt attribute*. These are excluded from the screen-reader narration.

See [7.2 Alt Text Guidelines](../epub/alt-text.md) and [7.3 Reading Order](../epub/reading-order.md) for the underlying rules that the object styles encode.

## 6.4.4 To Document for Our Publications
- The full object-style hierarchy for each long-form publication template.
- Cross-publication reusable object styles (e.g. a shared callout-box style).
- Object-style → EPUB-export-tag mapping.

Contributions welcome — see [Feedback](../feedback.md) to suggest naming changes before they're applied.

## 6.4.5 See Also
- [Paragraph Styles](paragraph-styles.md) – paragraph-level style hierarchy.
- [Character Styles](character-styles.md) – inline character-level styles.
- [7.2 Alt Text Guidelines](../epub/alt-text.md) – the alt-text rules object styles encode.
- [7.3 Reading Order](../epub/reading-order.md) – Articles-panel sequencing for EPUB export.
