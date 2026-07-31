---
name: temenos-migration
description: >
  Expert assistant for Temenos T24/Transact (TAFJ) version upgrades, patch application,
  and change-set-based deployment. Covers the TAFJ.Patch.xml patch-installer contract
  (which directories a patch touches), RELEASE manifest interpretation, GIT/RTC ChangeSet
  installation workflows, the DSPackageInstaller, and reading real upgrade evidence out of
  an installed environment (versioned config backups). Triggers: 'T24 upgrade', 'TAFJ
  upgrade', 'migration', 'patch install', 'Patch.xml', 'RELEASE notes', 'ChangeSet
  installation', 'GIT ChangeSet', 'RTC ChangeSet', 'DSPackageInstaller', 'version upgrade',
  'upgrade path', 'apply a patch', 'TAFJ version'.
---

# Migration Expert Skill

Version-upgrade and patch-deployment knowledge for Temenos T24/Transact (TAFJ) — not
code generation. For customisation code, route to `temenos-dev` and its sub-skills; for
observability/security config, route to `temenos-admin`.

**This skill's authority comes from a real patch installer and real upgrade evidence
found in an installed R25 environment — not from general T24 knowledge.** Cite the
source file when giving procedural detail; if a question needs detail this skill's
references don't have, say so and point at the relevant `docs/TAFJ-Migration/*.pdf`.

## Reference Files

| File | When to read |
|------|-------------|
| [patch-and-release.md](references/patch-and-release.md) | Understanding what a TAFJ patch touches, reading a RELEASE manifest, or planning a patch application |
| [changeset-and-upgrade.md](references/changeset-and-upgrade.md) | GIT/RTC ChangeSet installation workflow, DSPackageInstaller, or a full version upgrade |

For install-guide-level detail (exact upgrade steps, prerequisite checks):
```
python pipeline/query_docs.py "<question>" --topic TAFJ-Migration -n 5
```
`docs/TAFJ-Migration/` holds `TAFJ-Upgrade.pdf`, `TAFJ-GIT-ChangeSet-Installation.pdf`,
`TAFJ-RTC-ChangeSet-Installation.pdf`, `TAFJ-DSPackageInstaller.pdf` — copied from a
real `TAFJ_HOME/doc` on 2026-07-31.

## Core principle

A TAFJ patch is **directory-scoped, not full-reinstall**. `Patch.xml` (found at the
root of `TAFJ_HOME` in a patched environment) declares exactly which subdirectories
get overwritten:

```
bin, dbdrivers, dbscripts, lib, libMonitor, libValidation, TemnMonitor, ext,
appserver, JMSInjector, TAFJSessionMonitor, eclipse, ofsml
```

Anything outside this list is explicitly untouched by a patch installer. This is the
first thing to check when asked "will patching break my customisations?" — if the
customisation lives outside those directories (e.g. in `bnk/` package source), a TAFJ
core patch does not touch it directly, though the application server EAR still needs
redeploying after merging changes. See
[patch-and-release.md](references/patch-and-release.md) for the full contract.
