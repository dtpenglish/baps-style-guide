# BAPS DTP Style Guide

> Internal editorial, design, and production conventions for BAPS Swaminarayan Sanstha publishing.

**Live site:** https://dtpenglish.github.io/baps-style-guide/

This is an in-house style guide built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). It covers conventions for our work across Sanskrit, Gujarati, Hindi, and English materials — including editorial style, diacritic handling, InDesign production, EPUB accessibility, and our scripts and workflows.

## Quick links

- 📖 [Read the style guide](https://dtpenglish.github.io/baps-style-guide/)
- ✏️ [How to contribute](docs/contributing.md)
- 📝 [Changelog](docs/changelog.md)

## How editing works

Every page on the live site has a **pencil icon** in the top-right. Click it to open the page directly in GitHub's web editor — no local setup required. Make your edits in Markdown, write a brief description, and submit a pull request. Once reviewed and merged, the change is live within about a minute.

For more detail, see [CONTRIBUTING.md](docs/contributing.md).

## Local preview (optional)

If you want to preview changes before pushing — useful for larger edits — set up locally:

```bash
# One-time setup
git clone https://github.com/dtpenglish/baps-style-guide.git
cd baps-style-guide
pip install -r requirements.txt

# Preview (rebuilds automatically as you edit)
mkdocs serve
# Open http://127.0.0.1:8000 in your browser
```

## Repository structure

```
baps-style-guide/
├── docs/                       # All content (Markdown)
│   ├── index.md                # Home page
│   ├── editorial/              # Tone, capitalisation, punctuation
│   ├── diacritics/             # Sanskrit/Gujarati/Hindi conventions
│   ├── indesign/               # Paragraph styles, master pages
│   ├── epub/                   # Alt text, reading order
│   ├── scripts/                # JSX scripts reference
│   ├── workflows/              # Versioning, file naming
│   ├── contributing.md
│   └── changelog.md
├── mkdocs.yml                  # Site configuration
├── requirements.txt            # Python dependencies
└── .github/workflows/          # Auto-deployment
    └── deploy.yml
```

## Maintainer

[@dtpenglish](https://github.com/dtpenglish)

## Version

Style guide site scaffold **v1.0** — established May 2026.
