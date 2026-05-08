# BAPS DTP Style Guide

> Internal editorial, design, and production conventions for BAPS Swaminarayan Sanstha publishing.

**Live site:** https://dtpenglish.github.io/baps-style-guide/

This is a BAPS in-house style guide built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). It covers conventions for our work across Sanskrit, Gujarati, Hindi, and English materials – including editorial style, diacritic handling, InDesign production, EPUB accessibility, and our scripts and workflows.

## Quick links

- 📖 [Read the style guide](https://dtpenglish.github.io/baps-style-guide/)
- ✉️ [Send feedback](docs/feedback.md)
- 📝 [Changelog](docs/changelog.md)

## How feedback and editing work

The site is **read-only** for visitors. The edit-pencil icon has been removed from page headers.

If you'd like to suggest a fix, propose a new convention, or report a typo, see the [Feedback](docs/feedback.md) page – it's a one-click email to the maintainer.

The maintainer ([@dtpenglish](https://github.com/dtpenglish)) is the only person with direct push access. Edits are made via:

- GitHub's web editor (navigate to the file in the repo, click GitHub's own pencil)
- [github.dev](https://github.dev/dtpenglish/baps-style-guide) (press <kbd>.</kbd> on any GitHub page)
- A local clone + `mkdocs serve` for preview
- Claude Code for substantial work

## Local preview (maintainer only)

```bash
# One-time setup
git clone https://github.com/dtpenglish/baps-style-guide.git
cd baps-style-guide
pip install -r requirements.txt

# Preview (rebuilds automatically as you edit)
mkdocs serve --watch mkdocs.yml
# Open http://127.0.0.1:8000 in your browser
```

## Repository structure

```
baps-style-guide/
├── docs/                       # All content (Markdown)
│   ├── index.md                # Home page
│   ├── editorial/              # Tone, capitalization, punctuation
│   ├── diacritics/             # Sanskrit/Gujarati/Hindi conventions
│   ├── indesign/               # Paragraph styles, master pages
│   ├── epub/                   # Alt text, reading order
│   ├── scripts/                # JSX scripts reference
│   ├── workflows/              # Versioning, file naming
│   ├── downloads/              # Downloadable scripts and other files
│   ├── feedback.md             # How to send feedback
│   └── changelog.md
├── mkdocs.yml                  # Site configuration
├── requirements.txt            # Python dependencies
└── .github/workflows/          # Auto-deployment
    └── deploy.yml
```

## Maintainer

[@dtpenglish](https://github.com/dtpenglish)

## Version

Style guide site scaffold **v1.0** – established May 2026.
