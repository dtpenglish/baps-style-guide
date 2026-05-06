# File Versioning Rules

!!! danger "Non-negotiable"
    Every file output — script, Word document, Excel file, PDF, or any other deliverable — must carry an incremented version number in **both** the filename and an internal version string. **Never overwrite a previous version.** Each new file is the next version.

## The rule

When you produce a new revision of any file:

1. Increment the version number in the filename (`v1.0` → `v1.1`).
2. Update any internal version string inside the file to match.
3. Save as a new file. Do not overwrite the previous version.
4. The previous version stays where it is.

## Versioning scheme

| Change type | Version bump |
|---|---|
| Minor edit, fix, refinement | Patch: `v4.28` → `v4.29` |
| Substantive revision, new feature, new section | Minor: `v4.39` → `v5.0`, or `v1.2` → `v1.3` |
| Complete restructure, breaking change | Major: `v1.x` → `v2.0` |

For most day-to-day work, increment the patch number. Reserve minor and major bumps for genuinely substantial changes.

## Filename pattern

Place the version near the end of the filename, before the extension:

```
glossary-all-2026-04-15_v1.2.xlsx
ArticleBuilder_v4.39.jsx
ClaudeBrief_Vachanamrut_v3.docx
MSM_Vicharan_2016-23_v2.xlsx
```

For dated files, the date stays the date it was first created or the snapshot date; the version increments independently.

## Internal version strings

Where the file format allows, store the version inside the file too:

| File type | Where to put the version |
|---|---|
| JSX / Python script | A `// VERSION = "v4.39"` or `# VERSION = "v1.2"` line near the top |
| Excel | A `Version` cell in a metadata sheet, or in cell A1 of the first sheet |
| Word | The footer, or a metadata table on the cover page |
| PDF | The footer of every page |
| HTML | A `<meta name="version" content="v1.2">` tag |

The internal version must match the filename version. Mismatches are confusing and worse than absent.

## Why this rule exists

We have lost real work — and worse, lost the ability to *prove* what changed when — by overwriting files. The cost of an extra few KB on disk is trivial. The cost of not being able to roll back to last week's version of a script that used to work is enormous.

Beyond rollback, versioning gives us:

- **Audit:** a clear trail of what changed, when, and by whom.
- **Diffing:** the ability to compare two versions to understand a change.
- **Collaboration:** colleagues can refer to "the v4.38 behaviour" unambiguously.
- **Confidence:** you can experiment knowing the previous version is intact.

## What to do with old versions

Keep them. Disk is cheap, lost work is expensive. If a folder is getting cluttered, archive older versions into an `_archive/` subfolder rather than deleting them.

## Apply this rule automatically

This rule should be applied to every file output **without being asked**. If you're producing a file and you didn't bump the version, stop and bump it. If a tool or script generates output, the tool's version-bumping behaviour should be built in.

For Claude-assisted work, the rule is encoded in the team's working memory: every Claude session producing a file output is expected to apply versioning without being prompted.

## Related

- [File Naming](file-naming.md) — broader filename conventions
