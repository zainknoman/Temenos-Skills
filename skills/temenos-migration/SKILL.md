---
name: temenos-migration
description: >
  Expert assistant for Temenos T24/Transact (TAFJ) version upgrades, patch application,
  and change-set-based deployment. Covers the TAFJ.Patch.xml patch-installer contract
  (which directories a patch touches), RELEASE manifest interpretation, GIT/RTC ChangeSet
  installation workflows, the DSPackageInstaller, reading real upgrade evidence out of
  an installed environment (versioned config backups), and Temenos Packager (DSF Packager,
  TMNPACK): data packages of Transact configuration as JSON, Web/CLI/IDE creation, deployment
  via dsf-iris API/Maven/Workbench (full, incremental hash/file, single vs no transaction,
  multi-package, async), field-level updates, data structures, pre/post actions, user/system
  variables, package dependencies, sync, and the Code Packager for L3 jBC/Java JARs.
  Triggers: 'T24 upgrade', 'TAFJ upgrade', 'migration', 'patch install', 'Patch.xml',
  'RELEASE notes', 'ChangeSet installation', 'GIT ChangeSet', 'RTC ChangeSet',
  'DSPackageInstaller', 'version upgrade', 'upgrade path', 'apply a patch', 'TAFJ version',
  'Temenos Packager', 'DSF Packager', 'dsf-iris', 'dsf-transact', 'TMNPACK', 'T3TTP',
  'data package', 'deploy package', 'package manager', 'Temenos Workbench', 't-package.json',
  'DS.DSF.PACKAGE', 'field level update', 'FLU', 'data structure', 'filterOnlyLocal',
  'pre post action', 'incremental hash', 'multiPackageDeploy', 'dsf-multi-package-archetype',
  'Code Packager', 'dsf-code-jbc-package-archetype', 'promote configuration', 'DEV to UAT'.
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
| [temenos-packager.md](references/temenos-packager.md) | Anything Temenos Packager: packaging configuration records or L3 code, deploying packages to SIT/UAT/PROD, dsf-iris APIs and properties, FLU, data structures, pre/post actions, variables, multi-package and async deployment |

For install-guide-level detail (exact upgrade steps, prerequisite checks):
```
python pipeline/query_docs.py "<question>" --topic TAFJ-Migration -n 5
```
`docs/TAFJ-Migration/` holds `TAFJ-Upgrade.pdf`, `TAFJ-GIT-ChangeSet-Installation.pdf`,
`TAFJ-RTC-ChangeSet-Installation.pdf`, `TAFJ-DSPackageInstaller.pdf` — copied from a
real `TAFJ_HOME/doc` on 2026-07-31.

`docs/T3TTP/` holds the two Temenos Packager courses (**Part 1 Foundation**, **Part 2 Advanced**,
certification T3TTP), OCR'd from slide screenshots by `pipeline/docx_extract.py` on 2026-11-23.
PDF page N is slide N:
```
py -3 pipeline/query_docs.py "<question>" --topic T3TTP -n 5
```

## Temenos Packager rules that matter most

Full detail is in [temenos-packager.md](references/temenos-packager.md). Before answering:

- **Three different things are called "package".** A TAFJ patch (`Patch.xml`), a GIT/RTC change set,
  and a Temenos Packager data or code package. Ask which one when it is unclear.
- **Check what is installed.** `C:\R25` runs Packager 25.0.2 (`dsf-iris.war`, `dsf-transact.war`)
  but has no Workbench web UI (`dsf-uxp.war`). Offer API, CLI or IDE steps there.
- **Never deploy from Workbench in PROD.** Use the dsf-iris API or Maven CLI. Prefer no-transaction
  mode. Pass `transactionMode` explicitly, because the course gives different defaults for API and CLI.
- **One record, one package.** Deployment fails when a record already came from another package.
  `dsf.package.skipPackageDuplicateCheck` is false in R25. Turn it on only in test areas.
- **Automate, don't document.** Use pre/post actions (D, R, H, HLD, PR, PB, PP) and user/system
  variables instead of manual post-deployment steps.
- **Field names in package JSON are screen names** (`FIXED.SELECTION`). Layer A holds the
  prefixed EQU names (`ENQ.FIXED.SELECTION`). VERSION, DS.DSF.PACKAGE and DATES have no schema,
  so flag any field of theirs as unverified.

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
