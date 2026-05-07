# Scripts & Tools
Reference for the JSX scripts and automation tools used by the BAPS DTP team.

## Pages in This Section
- [JSX Scripts Reference](jsx-reference.md) — usage notes for our InDesign scripts

## Where Scripts Live
All canonical scripts are stored in:

```
E:\AVDWork\Scripts\
```

Project-specific scripts may live alongside their working files. If you write a script that's reusable across publications, move it to the canonical location and add an entry to the [JSX reference](jsx-reference.md).

## Running Scripts
InDesign's **Scripts panel** (Window → Utilities → Scripts) is the standard execution path. Scripts placed in the User Scripts folder appear in the panel and run with a double-click.

For Sidekick-driven workflows that route through Claude Desktop's MCP connection, the pattern is:

```javascript
app.doScript(script, 1246973031);
```

Where `1246973031` is the JavaScript script language ID.

## Versioning
Every script revision gets a version number in both the filename and the internal version string. Never overwrite an earlier version. See [versioning rules](../workflows/versioning.md).

Current versions of the major scripts (May 2026):

| Script | Current version |
|---|---|
| `ArticleBuilder.jsx` | v4.39 |
| `AddAltText.jsx` | v17 |
| `ExportToWord_Generic.jsx` | v11g |
| `SplitVachanamrut.jsx` | (record current version) |
