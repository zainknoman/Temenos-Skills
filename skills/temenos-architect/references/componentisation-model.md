# Componentisation Model Reference

Source: `docs/T24-Componentisation/` (official Temenos PDFs, copied from a real
`TAFJ_HOME/doc` on 2026-07-31). This file has not deep-parsed the PDFs line by
line — query them directly for procedural/API-level detail:

```
python pipeline/query_docs.py "<question>" --topic T24-Componentisation -n 5
```

## Documents available

| PDF | Covers |
|---|---|
| `T24-Componentisation.pdf` | The core componentisation model — how T24 functionality is packaged as jBC components |
| `T24-Componentisation-RESTful-WS.pdf` | Exposing componentised functionality as RESTful web services |
| `Component-Framework-Deploying-Component-Service.pdf` | Deployment of a component service within the component framework |

## Relationship to `temenos-jbc`

This skill covers the **architectural model** (what a component is, how the
framework deploys it, how REST exposure fits in). The `temenos-jbc`
skill covers **writing the actual code** (methods, validation hooks,
template definitions, `@GET`/`@POST`/`@Path` annotations, `metamodelVersion`,
`$PACKAGE`/`$USING`). When a request is "explain how componentisation works"
route here; when it's "write/review a component file" route to
`temenos-jbc`.

## Open item

Full architectural detail (component lifecycle, framework internals, exact
deployment sequence) has not been transcribed into markdown here — per the
Layer A/B/C split in this repo's `CLAUDE.md`, that level of detail belongs in
Layer B (searchable via `query_docs.py`), not duplicated into Layer C
reference files.
