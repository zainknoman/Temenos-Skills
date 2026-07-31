# ChangeSet Installation & Upgrade Reference

Source: `docs/TAFJ-Migration/` (official Temenos PDFs, copied from a real
`TAFJ_HOME/doc` on 2026-07-31). This skill has not deep-parsed these PDFs line
by line — for procedural detail, query them directly rather than relying on
this summary:

```
python pipeline/query_docs.py "<question>" --topic TAFJ-Migration -n 5
```

## Documents available

| PDF | Covers |
|---|---|
| `TAFJ-Upgrade.pdf` | The official TAFJ version-upgrade procedure |
| `TAFJ-GIT-ChangeSet-Installation.pdf` | Installing a change set sourced from a GIT-based development environment |
| `TAFJ-RTC-ChangeSet-Installation.pdf` | Installing a change set sourced from IBM RTC (Rational Team Concert) |
| `TAFJ-DSPackageInstaller.pdf` | The Design Studio package installer tool |

## What "ChangeSet installation" means in a TAFJ context

Two source-control-driven deployment paths are documented separately (GIT vs.
RTC) — they are not interchangeable procedures, and a migration plan should
name which one the target environment actually uses before generating steps.
Don't assume GIT tooling applies to an RTC-sourced change set or vice versa;
verify against the environment's actual VCS before proceeding.

## Relationship to `Patch.xml`-style patching

A **patch** (see [patch-and-release.md](patch-and-release.md)) is a
Temenos-issued, directory-scoped binary/lib update applied via the
`Patch.xml` self-installer. A **change set** is typically the mechanism for
deploying a project's own custom development (routines, components,
templates) sourced from GIT or RTC — a different concern from a core TAFJ
patch. When a developer asks about "migrating changes," clarify which of
these two they mean before answering, since the tooling and directory scope
differ.

## Open item

The exact step-by-step procedure inside `TAFJ-Upgrade.pdf` has not been
transcribed here — this file intentionally stays at the "what exists and
where to look" level per the Layer A/Layer C split in `CLAUDE.md`. Deep
procedural content belongs in Layer B (the vector-searchable PDF corpus),
queried via `pipeline/query_docs.py --topic TAFJ-Migration`, not duplicated
into markdown here.
