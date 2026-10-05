# JAR Viewer, Markdown Viewer and Application Viewer — design

Date: 2026-10-05 · Repos: Temenos-Skills (export) + T24Tools (viewers) · Status: approved in chat, pending spec review

## Goal

Answer "which JAR (and package) holds class X?" — e.g. `RecordLifecycle` → `EB_TemplateHook.jar`,
`com.temenos.t24.api.hook.system` — from T24Tools, for R23 and R25, the same way the JSON Viewer
answers "which fields does application X have?". In the same round, bring RepoMind's Markdown
Viewer into T24Tools and give the JSON Viewer a meaningful name.

## Decisions (made in brainstorming)

| # | Decision |
|---|----------|
| D1 | Temenos-Skills exports a per-release `classes.json`; T24Tools reads it. No in-browser JAR scanning. |
| D2 | `classes.json` is **published with the T24Tools site** like `fields.json` (`docs/t24tools/<R>/`), loadable in-tool. |
| D3 | **No download links in the T24Tools header** — for `classes.json` and also the existing `fields.json` links. Files load from inside the tools. |
| D4 | Content: JAR + package for every class; superclass, interfaces, type and interface/abstract flags for every class; full public method signatures only for types `hook`, `public-api`, `batch`, `service`, `integration`. ~7 MB per release. |
| D5 | R23 ↔ R25 movement is computed in the browser when both releases are loaded — not stored in the file. |
| D6 | Separate tabs, merge maybe later: JSON Viewer renamed **Application Viewer** (id `json` kept); new **JAR Viewer** (id `jar`); new **Markdown Viewer** (id `md`). |
| D7 | Markdown Viewer = RepoMind's MDViewer (paste, marked + DOMPurify, mermaid) **plus** MDFV-style upload/drop of `.md` files and MDFV manuscript styling. Mermaid lazy-loaded, `securityLevel: 'strict'`. |

## Part 1 — Temenos-Skills: `classes.json` export

### Data source
- **R23:** existing extraction cache `cache/*.json` (2,050 JARs, 92,912 classes, 5,925 packages), written by `pipeline/extract.py`.
- **R25:** run `pipeline/extract.py` over `C:\R25\bnk\t24lib` (2,136 JARs), cache in `build/releases/R25/class-cache/`. Read-only on `C:\R25` (see the `c-r25-read-only` rule); nothing is written under it.

### Tool
`pipeline/class_export.py --release <R> [--cache <dir>] [--out build/t24tools/<R>/classes.json]`,
called by `pipeline/release_t24tools.py` after `fields.json`. It also adds `classes.json` (bytes +
sha256) to `build/t24tools/<R>/manifest.json`. Export still only happens when every golden case passes,
as today.

### Format (`schemaVersion` 1)
```json
{
  "kind": "t24-classes",
  "schemaVersion": 1,
  "release": "R23",
  "generated": "2026-10-05T10:00:00Z",
  "jars":     ["EB_TemplateHook.jar"],
  "packages": ["com.temenos.t24.api.hook.system"],
  "types":    ["hook"],
  "classes": [
    ["RecordLifecycle", 0, 0, 0, 0,
     "com.temenos.tafj.api.client.impl.T24Context", [],
     [["validateRecord", "com.temenos.api.TValidationResponse",
       ["java.lang.String", "java.lang.String", "com.temenos.api.TStructure", "com.temenos.api.TStructure",
        "com.temenos.api.TStructure", "com.temenos.t24.api.complex.eb.templatehook.TransactionContext"]]]]
  ]
}
```
Class tuple: `[name, packageIdx, jarIdx, typeIdx, flags, superclass, interfaces, methods?]`
- `flags` bit 1 = interface, bit 2 = abstract.
- `superclass` is the fully-qualified name or `""`; `interfaces` is a list of fully-qualified names.
- `methods` (public only, `[name, returnType, [paramTypes]]`, fully-qualified types) is present only for types in D4; otherwise the tuple has 7 elements.
- A class present in more than one JAR appears once per JAR (split package — real information, not deduplicated).
- Classes sorted by name, then package, then JAR, so the file is deterministic for identical input.

### Tests (`tests/pipeline/test_class_export.py`)
- Round-trip on a small fixture cache: decode → `RecordLifecycle` → `EB_TemplateHook.jar` / package / superclass.
- Methods present only for the D4 types; tuple length 7 vs 8.
- Duplicate class in two JARs → two entries.
- Manifest entry bytes/sha256 match the written file.

### Docs
Update CLAUDE.md: the "never commit it to the public T24Tools repo" note on the T24Tools export is
replaced by the D2/D3 rule (published, loadable in-tool, no header download). Add the `class_export.py`
command to "Running the extraction pipeline".

## Part 2 — T24Tools

### Navigation and header
- `src/navigation.js` `NAV_TABS`: `json` → label "Application Viewer"; add `['jar', 'JAR Viewer']` and `['md', 'Markdown Viewer']`. Ids are permanent (`?tool=` deep links).
- `src/App.jsx`: remove the R23/R25 `fields.json` download links from the header.
- `src/build/knowledgeFiles.js`: publish `classes.json` alongside `fields.json` and `manifest.json` under `knowledge/<R>/`.
- README: tool table (Application Viewer, JAR Viewer, Markdown Viewer), `?tool=jar` / `?tool=md`, knowledge files paragraph (no header download). The disclaimer's "contains no Temenos data" sentence is replaced with a statement that the only Temenos-derived data T24Tools uses is application field names (`fields.json`) and Java class and JAR names (`classes.json`); the not-affiliated / trademark sentences stay as they are.

### Application Viewer
The existing JSON Viewer, renamed in the tab, its heading and docs. No behaviour change.

### JAR Viewer (`src/features/jarViewer/`)
- `classIndex.js` (pure): `isClassIndex(doc)`, `decodeClassIndex(doc)` (validates `kind`/`schemaVersion`), `searchClasses(index, query, { types, limit })`, `classesInJar(index, jar)`, `findClass(index, qualified)`, `compareReleases(a, b)` → per qualified name `same | moved(fromJar, toJar) | onlyA | onlyB`.
- `JarViewer.jsx`:
  - **Load:** "Load R23 / R25 from this site" + drop/upload `classes.json`; both releases may be loaded. Session-only (not written to storage — two ~7 MB files would fill most of the browser's storage).
  - **Search** one box over class name, qualified name, package, JAR. Type filter defaults to all types except `internal` and `test`. Results ranked: exact simple name, prefix, contains. Virtual list for large result sets.
  - **Class detail:** JAR, package, type, flags, superclass (link when it is in the index), interfaces, method signatures when present, **Copy** button for `import <qualified>;`.
  - **JAR mode:** query matching a JAR name lists its classes grouped by package.
  - **Release badges** when both releases are loaded: same JAR / moved A → B / R25 only / R23 only.

### Markdown Viewer (`src/features/markdownViewer/`)
- Ported from RepoMind: `src/lib/markdown.js` (`renderMarkdown`: marked → DOMPurify, mermaid fences → `<div class="mermaid">`), `src/services/diagram.js` (`renderMermaidBlocks`, dynamic `import('mermaid')`, `securityLevel: 'strict'`), `MarkdownViewer.jsx`.
- Inputs: paste (textarea) or drop/upload one or more `.md` files with a file list (switch/remove), session-only.
- Output: MDFV manuscript sheet with filename tab, light and dark theme.
- Dependencies (exact versions, like the rest of `package.json`): `marked`, `dompurify`, `mermaid`. Mermaid is a separate lazy chunk served from the site; the CSP is unchanged.

### Error handling
- Wrong file in JAR Viewer → "This isn't a classes.json (expected kind t24-classes)", with a pointer to Application Viewer for `fields.json`. Unsupported `schemaVersion` → message naming the found and supported versions.
- Site file missing → Load button shows the HTTP status; upload still works.
- Bad mermaid block → error and source shown for that block only; rest of the document renders.
- HTML in markdown → sanitised by DOMPurify (no scripts, no event handlers).

### Tests
- Vitest: `classIndex.test.js` (decode, validation errors, ranking, type filter, superclass lookup, JAR mode, release comparison), `markdown.test.js` (ported: sanitising, mermaid fence), `navigation.test.js` (new ids, `json` label), `knowledgeFiles.test.js` (classes.json published).
- Playwright E2E: JAR Viewer loads R23 from the site, search `RecordLifecycle` → `EB_TemplateHook.jar`; Markdown Viewer renders a pasted document with a mermaid block; header has no knowledge download links.
- Manual browser check before reporting done.

## Build order (each step shippable)
1. Temenos-Skills: `class_export.py`, R23 + R25 `classes.json`, manifest, tests, CLAUDE.md.
2. T24Tools: rename to Application Viewer, remove header download links, README.
3. T24Tools: JAR Viewer + publish `classes.json`.
4. T24Tools: Markdown Viewer.

## Out of scope
- Merging Application Viewer and JAR Viewer (possible later).
- Method signatures for `internal`, `framework`, `custom`, `test`, `data`, `tooling` classes (~190 MB in total).
- Searching by method name across all classes.
- Releases other than R23 and R25.
