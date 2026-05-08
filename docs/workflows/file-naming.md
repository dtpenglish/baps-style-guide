# 9.3 File Naming
How we name files, folders, and revisions across the DTP workflow.

## 9.3.1 General Principles
- **Use lowercase and hyphens** for new files where possible: `master-glossary-2026-04-15_v1.2.xlsx`. Underscores and mixed case are fine for files inheriting from existing conventions.
- **No spaces** in filenames for anything that will pass through scripts or be referenced in a URL.
- **Date-stamp** files where the snapshot date matters (glossaries, exports, batch outputs). Use ISO dates: `YYYY-MM-DD`.
- **Version-stamp** every file output. See [versioning rules](versioning.md).

## 9.3.2 Patterns We Use
| Type | Pattern | Example |
|---|---|---|
| Versioned glossary | `name-YYYY-MM-DD_vX.Y.xlsx` | `glossary-all-2026-04-15_v1.2.xlsx` |
| Script | `Name_vX.Y.jsx` | `ArticleBuilder_v4.39.jsx` |
| Brief / spec doc | `Brief_Topic_vX.docx` | `Brief_Vachanamrut_v3.docx` |
| Project export | `Project_Description_vX.ext` | `MSM_Vicharan_2016-23_v2.xlsx` |

## 9.3.3 Folder Organization
Organize active work by publication, with shared resources (scripts, glossaries, templates) in their own top-level folders. A typical layout:

```
DTP-root/
├── Current/
│   ├── <Publication-A>/
│   │   └── <Edition-or-Year>/   # working files for one edition
│   └── <Publication-B>/         # working files for another publication
├── Scripts/                     # canonical scripts location
└── <Toolchain>/                 # other shared toolchains
```

Keep working files in their publication folder. Move reusable assets (scripts, shared glossaries, templates) to the appropriate shared location.

## 9.3.4 What Not to Do
- Don't put dates in folder names if the folder's contents are continuously updated. Date the *files*, not the *folder*.
- Don't use 'final', 'FINAL', 'really-final', 'USE-THIS-ONE', or similar markers. Use the version number — that's what it's for.
- Don't bury versioning inside the filename: `v1.2-glossary.xlsx` sorts unhelpfully. Put the version near the end: `glossary_v1.2.xlsx`.

## 9.3.5 Related
- [Versioning Rules](versioning.md) — the version-number rule itself
