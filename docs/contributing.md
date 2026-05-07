# 12 Contributing to the Style Guide
This guide is yours. Anyone on the BAPS DTP team can propose edits — from fixing a typo to adding an entire new section. This page explains how.

!!! note "About the team"
    Most of our authors and editors don't have formal writing or publishing training — we learn on the job, drawing on the SAP glossary, this guide, and one another. The guide is meant to **support** that learning, not to gatekeep. If a rule is unclear, propose an edit, ask a question in [GitHub Issues](https://github.com/dtpenglish/baps-style-guide/issues), or raise it in a meeting. The goal is shared, evolving conventions — not formal expertise.

## 12.1 Three Ways to Contribute
Pick whichever matches your comfort level. All three result in the same outcome: a reviewed, versioned change to the live site.

### 12.1.1 1. the Pencil Icon (easiest)
Every page on this site has a **pencil icon** in the top-right corner. This is the fastest way to fix a typo, clarify a sentence, or update a small detail.

**Steps:**

1. Click the :material-pencil: pencil icon on the page you want to edit.
2. GitHub opens the page's Markdown source in its web editor. Sign in if prompted.
3. Make your edits directly in the browser.
4. Scroll down. Under **Commit changes**, write a one-line description of what you changed (e.g. "Fix typo in macron convention example").
5. Select **Create a new branch for this commit and start a pull request**.
6. Click **Propose changes**, then **Create pull request**.
7. Done. A maintainer will review and merge — usually within a day.

!!! tip "No Git knowledge needed"
    The pencil-icon flow handles all the Git steps for you. You're just editing text in a browser.

### 12.1.2 2. New Page or Larger Edit
For adding a whole new page or restructuring an existing one, the same web flow works — but you'll need to create a new file.

1. In the GitHub repository, navigate to the appropriate folder under `docs/` (e.g. `docs/editorial/`).
2. Click **Add file → Create new file**.
3. Name the file using lowercase and hyphens, ending in `.md` (e.g. `quotation-marks.md`).
4. Write your content in Markdown (see [Markdown basics](#markdown-basics) below).
5. Commit and create a pull request as in the previous flow.
6. **Important:** Also propose an edit to `mkdocs.yml` to add your new page to the navigation. If you're not sure how, mention this in the pull request description and a maintainer will help.

### 12.1.3 3. Local Preview (for Substantial Work)
If you're writing a long section or want to see exactly how it'll render, set up MkDocs locally.

```bash
# One-Time Setup
git clone https://github.com/dtpenglish/baps-style-guide.git
cd baps-style-guide
pip install -r requirements.txt

# Start the Live Preview Server
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) — the site rebuilds automatically as you edit. When you're done, commit your branch and push, then open a pull request on GitHub.

## 12.2 What Makes a Good Edit
A good edit:

- **Has one clear purpose.** Fix one typo, clarify one rule, or add one section per pull request. Don't bundle unrelated changes.
- **Cites a real example.** When proposing a new convention, point to where it came up — a publication, a script, a recurring question.
- **Considers our four languages.** Conventions that apply only to English should say so. Rules for transliteration should specify which source language.
- **Doesn't duplicate.** Search the site first. If a topic already exists, edit the existing page rather than creating a new one.

## 12.3 Reviewing Pull Requests
If you have maintainer access, here's the review checklist:

- [ ] The change matches an actual practice — not an aspiration we don't follow yet.
- [ ] Examples are concrete and accurate.
- [ ] Diacritics use the macron-only convention (where applicable).
- [ ] No file paths reference personal drives or unshared resources.
- [ ] Links work; navigation entries are added if a new page was created.
- [ ] The change has been previewed (locally or via the GitHub Actions preview build).

For substantial conventions changes — anything that would alter how we work — also add an entry to the [changelog](changelog.md) before merging.

## 12.4 Markdown Basics
This site uses standard Markdown plus some MkDocs Material extensions. The essentials:

| Goal | Syntax |
|---|---|
| Heading | `## Heading 2`, `### Heading 3` |
| Bold | `**bold**` |
| Italic | `*italic*` |
| Inline code | `` `code` `` |
| Link | `[text](path/to/page.md)` |
| Bullet list | `- item` |
| Numbered list | `1. item` |
| Table | See below |

**Tables:**

```markdown
| Term | Diacritic spelling |
|---|---|
| Aksharbrahman | Akṣharbrahman |
| Sadhu | Sādhu |
```

**Callouts** (admonitions):

```markdown
!!! note "Optional title"
    The body of the callout goes here.

!!! warning
    Use this for things people should not do.

!!! tip
    Use this for helpful suggestions.
```

**Linking between pages:** Use relative paths from the current file. From `docs/editorial/tone.md` to `docs/diacritics/macron-convention.md`, write `[link text](../diacritics/macron-convention.md)`.

## 12.5 Asking Questions without Editing
If you've spotted something that needs work but aren't sure how to fix it — or you want to discuss a convention before drafting — open a [GitHub Issue](https://github.com/dtpenglish/baps-style-guide/issues/new) instead of a pull request. Issues are for conversations; pull requests are for changes.

## 12.6 Who Reviews and Merges
The current maintainer is [@dtpenglish](https://github.com/dtpenglish). All pull requests are reviewed before merging. For routine fixes (typos, formatting), expect same-day turnaround. For substantive conventions changes, allow a few days for discussion.
