# 8.2 JSX Scripts Reference
Quick reference for the InDesign JSX scripts used in BAPS DTP production. Each entry covers what the script does, how to run it, and notable behaviour.

---

## 8.2.1 ArticleBuilder.jsx
**Current version:** v4.39

**Purpose:** Automates Articles panel sequencing for EPUB export. Walks the document, identifies content elements, and produces a clean reading order.

**Run:** Double-click in the Scripts panel.

**Key behaviours:**

- Uses `item.allPageItems` (not `item.pageItems`) to surface typed objects from groups.
- Uses `page.allPageItems` across all pages to locate anchored objects.
- Pre-computes all DOM work before the dialogue (`pd.show()`) opens – this prevents InDesign crashes from long-running operations inside ScriptUI.
- Replaced the broken ScriptUI scrolling preview with an HTML-in-browser preview.

**Notable edge cases:**

- Anchored images are placed in the article based on the anchor's text position, not visual position on the page.
- Decorative items must be tagged via Object Export Options before running, or the script will include them.

---

## 8.2.2 AddAltText.jsx
**Current version:** v17

**Purpose:** Batch alt-text application for images in an InDesign document.

**Run:** Double-click in the Scripts panel.

**Key behaviours:**

- v17 introduced caption pre-population: the script reads the InDesign caption associated with each image and pre-fills the alt-text field, so the editor refines rather than drafts from scratch.
- Operates on selected pages or the whole document.
- Skips items already tagged decorative.

**Workflow:**

1. Ensure each image has an associated caption in InDesign.
2. Run the script.
3. Review and refine each pre-populated alt text in the dialogue.
4. Apply.

---

## 8.2.3 ExportToWord_Generic.jsx
**Current version:** v11g

**Purpose:** Exports an InDesign story or document to RTF/Word format with paragraph numbering and track changes preserved.

**Run:** Double-click in the Scripts panel.

**Key behaviours:**

- Injects paragraph numbering into the export.
- Wraps operations in `app.doScript` with undo, so the document can be reverted to its pre-export state non-destructively.
- Sorts content by reading order.
- Exports tracked changes as green-underlined text.
- Excludes master page items from the export.

**Required InDesign 2025 APIs:**

- `story.changes.item(i)` for iterating track changes.
- `ChangeTypes.INSERTED_TEXT` for filtering insertions.

---

## 8.2.4 ExtendScript Gotchas
A handful of issues that have caught us out and are worth knowing before writing or extending these scripts:

- **`item.pageItems` vs `item.allPageItems`:** the latter returns typed objects (groups, etc.); the former returns generic page items. Use `allPageItems` when you need to reason about types.
- **Anchored images:** to find them, walk `page.allPageItems` across all pages, not `spread.pageItems`. Anchor relationships are not surfaced by the spread-level enumeration.
- **Track changes (InDesign 2025):** use `story.changes.count()` and `story.changes.item(i)`. The earlier `story.trackChangesPreferences` API is deprecated.
- **ScriptUI scrolling:** broken in long lists. Replace with an HTML-in-browser preview when you need scrollable content.
- **Pre-compute before `pd.show()`:** any long-running DOM work after the dialogue opens risks crashing InDesign. Do all the heavy lifting first, store results in arrays, then show the dialogue.

## 8.2.5 Related
- [Versioning Rules](../workflows/versioning.md) – every script edit produces a new versioned file
- [Reading Order](../epub/reading-order.md) – what `ArticleBuilder.jsx` actually produces
- [Alt Text Guidelines](../epub/alt-text.md) – what `AddAltText.jsx` actually applies
