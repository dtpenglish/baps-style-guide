# 7.1 EPUB Accessibility
Standards for producing accessible EPUBs from our InDesign source files. Accessibility is editorial, not technical: alt text is writing, reading order is structure, and both belong in the production conversation from the start.

## 7.1.1 Pages in This Section
- [Alt Text Guidelines](alt-text.md) — writing useful alternative text for images
- [Reading Order](reading-order.md) — the Articles panel and structural sequencing

## 7.1.2 Why This Matters
Our EPUBs are read on assistive technologies. A screen reader user encountering a photograph with no alt text experiences a silence where the rest of us see a face, a place, an event. Reading order determines whether the screen reader narrates content in the sequence we intended or jumps around the page erratically. These are not edge cases — they are the experience of every reader using assistive tech.

Beyond accessibility, well-formed EPUBs:

- Pass automated validation (DAISY Ace, EPUBCheck) without warnings.
- Index and search correctly in reader applications.
- Display reliably across reading software.

## 7.1.3 Tooling
The `ArticleBuilder.jsx` script (current version v4.39) automates Articles-panel sequencing for EPUB export. The `AddAltText.jsx` script (current version v17) handles batch alt-text application with caption pre-population. See [Scripts & Tools](../scripts/index.md) for details.
