# File Naming

How we name files, folders, and revisions across the DTP workflow.

## General principles

- **Use lowercase and hyphens** for new files where possible: `master-glossary-2026-04-15_v1.2.xlsx`. Underscores and mixed case are fine for files inheriting from existing conventions.
- **No spaces** in filenames for anything that will pass through scripts or be referenced in a URL.
- **Date-stamp** files where the snapshot date matters (glossaries, exports, batch outputs). Use ISO dates: `YYYY-MM-DD`.
- **Version-stamp** every file output. See [versioning rules](versioning.md).

## Patterns we use

| Type | Pattern | Example |
|---|---|---|
| Versioned glossary | `name-YYYY-MM-DD_vX.Y.xlsx` | `glossary-all-2026-04-15_v1.2.xlsx` |
| Script | `Name_vX.Y.jsx` | `ArticleBuilder_v4.39.jsx` |
| Brief / spec doc | `ClaudeBrief_Topic_vX.docx` | `ClaudeBrief_Vachanamrut_v3.docx` |
| Project export | `Project_Description_vX.ext` | `MSM_Vicharan_2016-23_v2.xlsx` |

## Folder organisation

Active work lives under `E:\AVDWork\AVD_Current\`, organised by publication:

```
E:\AVDWork\
├── AVD_Current\
│   ├── Vach_SnV\
│   │   └── Vach Text\
│   │       └── 2025_4E\          # Vachanamrut 4th Edition working files
│   └── Bliss\                    # Bliss magazine working files
├── Scripts\                      # Canonical scripts location
└── BAPS-Timeline-Tools\          # Timeline deployment toolchain
```

Keep working files in their publication folder. Move reusable assets (scripts, shared glossaries, templates) to the appropriate shared location.

## What not to do

- Don't put dates in folder names if the folder's contents are continuously updated. Date the *files*, not the *folder*.
- Don't use "final," "FINAL," "really-final," "USE-THIS-ONE," or similar markers. Use the version number — that's what it's for.
- Don't bury versioning inside the filename: `v1.2-glossary.xlsx` sorts unhelpfully. Put the version near the end: `glossary_v1.2.xlsx`.

## Related

- [Versioning Rules](versioning.md) — the version-number rule itself
