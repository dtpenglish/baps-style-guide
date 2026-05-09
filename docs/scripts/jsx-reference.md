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
A handful of issues that have caught us out and are worth knowing before writing or extending InDesign JSX scripts:

### `item.pageItems` vs `item.allPageItems`
- **What's the difference.** `pageItems` returns only the *direct* children of a container as generic `PageItem` objects. `allPageItems` recursively walks all descendants and returns each as its **proper type** — `Image`, `TextFrame`, `Group`, `Rectangle`, etc.
- **Why it matters.** If a script needs to ask *what kind of thing is this?* (e.g. "is this an image?"), `pageItems` will give back generic page items that lose their type info. `allPageItems` preserves the type.
- **Rule of thumb.** Use `allPageItems` whenever the script needs to branch on object type, walk into groups, or count specific kinds of items. Use `pageItems` only when you just need direct children and don't care about types.

### Finding anchored images
- **What goes wrong.** Anchored images (images attached to a text-flow position) don't appear when you enumerate `spread.pageItems` — the spread-level collection doesn't surface anchored objects, only those positioned freely on the page.
- **Fix.** Walk `page.allPageItems` across **every page** in the document instead. Anchored objects appear there.
- **Why this matters for us.** `ArticleBuilder.jsx` relies on this — the script's job is to build the EPUB reading order, and anchored images would be missed if we only checked spread-level enumeration.

### Track changes — InDesign 2025 API
- **What changed.** The track-changes API was rewritten in InDesign 2025. The older `story.trackChangesPreferences` and related properties are deprecated and behave inconsistently in the new version.
- **What to use instead.**
    - `story.changes.count()` — number of change records on the story.
    - `story.changes.item(i)` — the *i*-th change record (0-indexed).
    - `ChangeTypes.INSERTED_TEXT` (and other `ChangeTypes.*` constants) — to filter by change type.
- **Why this matters for us.** `ExportToWord_Generic.jsx` exports tracked changes into the Word document — it had to be rewritten against the new API for InDesign 2025 compatibility.

### ScriptUI scrolling is broken in long lists
- **What goes wrong.** ScriptUI (the JavaScript-based dialog framework InDesign uses) has a long-standing bug where `listbox` and `treeview` controls don't scroll reliably once the list grows beyond a screen-full — the scrollbar stops responding, the highlight jumps, or items above the viewport become unreachable.
- **Workaround.** When the script needs to show a scrollable list of more than ~20 rows (e.g. previewing the article order before applying), generate an HTML page on disk and open it in the system browser instead. The browser's scrolling Just Works.
- **Why this matters for us.** `ArticleBuilder.jsx` previously crashed or stalled on long Articles-panel previews; replacing the ScriptUI list with an HTML preview fixed it.

### Pre-compute everything before `pd.show()`
- **What `pd` is.** A common script idiom — `pd` for "progress dialog" — a ScriptUI window opened to show progress/feedback while the script does work.
- **What goes wrong.** If long-running DOM operations (looping over hundreds of page items, modifying many styles, etc.) run **after** `pd.show()` is called, InDesign frequently crashes or hangs. The ScriptUI event loop and the scripting DOM compete for the main thread.
- **Pattern that works.** Do *all* the heavy work first — walk the document, gather what's needed, build result arrays — then show the dialog with the pre-computed data. The dialog should only be displaying or applying simple decisions, not doing the analysis.

```javascript
// Bad: dialog opens, then the slow walk runs while it's open.
pd.show();
for (var i = 0; i < doc.allPageItems.length; i++) { /* … */ }

// Good: walk first, store, then show.
var items = [];
for (var i = 0; i < doc.allPageItems.length; i++) { items.push(/* … */); }
pd.show();   // dialog only displays / applies the results.
```

## 8.2.5 Related
- [Versioning Rules](../workflows/versioning.md) – every script edit produces a new versioned file
- [Reading Order](../epub/reading-order.md) – what `ArticleBuilder.jsx` actually produces
- [Alt Text Guidelines](../epub/alt-text.md) – what `AddAltText.jsx` actually applies
