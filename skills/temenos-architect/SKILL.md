---
name: temenos-architect
description: >
  Expert assistant for Temenos T24/Transact componentisation architecture, package
  structure, and routine-naming conventions. Covers the T24 componentisation model
  (jBC components, REST exposure), how package/extension modules are structured
  (bnk/Extensions, bnk/ESBProjects layout), and how the base T24_BP routine
  repository is organised by naming prefix (CONV.*, E.*, V.*, OC.*, application
  codes). Triggers: 'T24 architecture', 'package structure', 'componentisation
  architecture', 'routine naming convention', 'T24_BP', 'application layering',
  'component deployment architecture', 'how is T24 organised'.
---

# Temenos Architect Skill

**Scope note (read this first):** this skill is deliberately narrower than a general
"enterprise architect" skill. A scan of a real R25 Model Bank install found strong
primary sources for *componentisation architecture and naming/packaging conventions*,
but not for broader topics like target-state solution architecture, capacity planning,
or integration topology design (that material lives in `temenos-integration` and
`temenos-admin` instead — see cross-references below). Don't overstate this
skill's authority beyond what its references actually cover.

## Reference Files

| File | When to read |
|------|-------------|
| [componentisation-model.md](references/componentisation-model.md) | How T24 componentisation works (jBC components, REST exposure, deployment) |
| [package-and-routine-structure.md](references/package-and-routine-structure.md) | How package/extension modules and the base routine repository are organised |

For deeper componentisation detail:
```
python pipeline/query_docs.py "<question>" --topic T24-Componentisation -n 5
```
`docs/T24-Componentisation/` holds `T24-Componentisation.pdf`,
`T24-Componentisation-RESTful-WS.pdf`,
`Component-Framework-Deploying-Component-Service.pdf` — copied from a real
`TAFJ_HOME/doc` on 2026-07-31.

## Cross-references — don't duplicate, route instead

- Writing or reviewing actual jBC component code → `temenos-jbc` skill.
- ESB/non-ESB integration package inventory and service-extension modules →
  `temenos-integration` skill (`bnk/Extensions`, `bnk/ESBProjects`).
- Application-server / deployment-runtime questions → `temenos-admin` skill.
