# Reading Order

Reading order is the sequence in which a screen reader narrates the content of a page. In a print book, the reader's eye establishes order through layout convention; in an EPUB, **we** have to declare it explicitly.

## The Articles panel

InDesign's **Articles panel** (Window → Articles) is where reading order is defined for EPUB export. Every content element on every page should be a member of an article, in the order it should be read.

## Common problems we encounter

| Problem | Symptom | Fix |
|---|---|---|
| Stale members | Articles panel has 303 entries when the spread has 254 | Remove deleted/replaced items; deduplicate |
| Decorative items in articles | Page ornaments narrated as content | Remove from Articles panel; mark Object Export Options as decorative |
| Anchored images in wrong sequence | Image narrated before its caption | Reorder within the article |
| Multi-column flow | Right column narrated before left finishes | Confirm article order matches intended reading sequence |

## Cleaning the Articles panel

The Bliss Jan–Feb 2026 cleanup pattern:

1. Open Articles panel and the affected document.
2. For each spread, compare panel members to actual content. Remove stragglers (deleted images that left their entries behind).
3. Remove decorative ornaments that crept in from the InDesign auto-add.
4. Verify each content image is present exactly once.
5. Verify the within-article order matches reading flow.

This is tedious by hand. The `ArticleBuilder.jsx` script automates much of it — see [Scripts & Tools](../scripts/index.md).

## Anchored images

Anchored images (images anchored to a text frame) need special attention. Their position in the reading order is determined by the anchor location, not the visual position on the page. If an image visually appears at the bottom of a column but its anchor is mid-paragraph, it will be narrated mid-paragraph — usually disrupting the flow.

`ArticleBuilder.jsx` handles anchored images explicitly. From v4.39, it walks `page.allPageItems` (across all pages) to find anchored objects and inserts them into the article at sensible positions.

## ExtendScript notes

For team members writing or extending JSX scripts that touch reading order:

- Use `item.allPageItems`, not `item.pageItems`, to get typed objects (groups, images within groups, etc.).
- Use `page.allPageItems` to find anchored objects across all pages.
- Use `story.changes.count()` (InDesign 2025 API) to detect track-changes entries.

These quirks are documented in greater detail in the [Scripts reference](../scripts/jsx-reference.md).

## Verifying reading order

Before EPUB export:

1. **Window → Articles** — visually scan each article's member list.
2. **File → Export → EPUB** with the option *Use → Articles panel* selected for content order.
3. Open the exported EPUB in a screen reader (NVDA on Windows, VoiceOver on macOS) and listen to a few pages.
4. Run DAISY Ace for an automated reading-order report.

A few minutes of listening to the actual narration catches problems that visual scanning misses every time.

## Related

- [Alt Text Guidelines](alt-text.md) — how to write the text screen readers will narrate for images
- [Scripts & Tools](../scripts/index.md) — `ArticleBuilder.jsx` reference
