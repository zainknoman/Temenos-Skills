# Patch & Release Reference

Source: `TAFJ_HOME/Patch.xml`, `TAFJ_HOME/RELEASE`, `TAFJ_HOME/conf/*.bak`,
verified 2026-07-31 against a real R25 install.

## `Patch.xml` — the patch installer contract

`Patch.xml` at the root of `TAFJ_HOME` is a self-installer descriptor
(consumed by Temenos's install tooling) with these sections:

- **`<Welcome>`** — states the patch deploys onto an existing installation
  *without creating backup files* and *cannot be reverted* — take your own
  backup before applying. It explicitly warns this only updates files inside
  the directories you specify; nothing outside `TAFJ_HOME` is touched.
- **`<Questions>`** — a single `install-directory` question (the target
  `TAFJ_HOME`), must already exist.
- **`<FilesToEdit>`** — empty in this patch (no in-place text edits).
- **`<FilesToDelete>`** — this patch removes:
  - `/lib/TemnLogger.jar`
  - `/lib/TemnMeter.jar`
  - `/lib/TemnTracer.jar`
  (superseded by newer equivalents shipped in the same patch — check the
  patch's `lib/` payload for replacements before assuming logging/metrics/
  tracing are simply gone).
- **`<Thanks>`** — confirms success and tells you to verify component
  versions via `'path_to_TAFJ_HOME'/bin tVersion`.

**Directories a patch overwrites** (declared in the `<Welcome>` text):
```
TAFJ_HOME/bin
TAFJ_HOME/dbdrivers
TAFJ_HOME/dbscripts
TAFJ_HOME/lib
TAFJ_HOME/libMonitor
TAFJ_HOME/libValidation
TAFJ_HOME/TemnMonitor
TAFJ_HOME/ext
TAFJ_HOME/appserver
TAFJ_HOME/JMSInjector
TAFJ_HOME/TAFJSessionMonitor
TAFJ_HOME/eclipse
TAFJ_HOME/ofsml
```

**Post-patch action required:** the application server EAR must be manually
rebuilt/redeployed after merging the patch's changes with the current
deployment, and any new libs added to the app-server classpath — a TAFJ
patch does not auto-redeploy the running app server.

**Verification:** run `tVersion` from `TAFJ_HOME/bin` after any patch to
confirm component versions actually changed.

## `RELEASE` manifest

`TAFJ_HOME/RELEASE` (a ~300KB text file) is the authoritative version/
component manifest for the installed TAFJ build. When asked "what version is
this / what's included in this release", read this file directly rather than
inferring from folder names or `pom.xml`/`pomEE8.xml` version strings — those
describe the build tooling, not necessarily the deployed release identity.

## Real upgrade evidence on this install

`TAFJ_HOME/conf/` contains, alongside the live `tafj.properties`:
- `tafj.properties.bak` — most recent pre-change backup
- `tafj.properties.pre-v8.4.1.bak` — explicitly named backup from before a
  TAFJ 8.4.1-boundary change

This is a directly observable example of the standard TAFJ upgrade pattern:
**config files get versioned `.bak` copies before an upgrade touches them,
named with the version being crossed.** When planning or reviewing an
upgrade, check for this naming pattern to understand what's already been
attempted on a given environment before assuming a clean baseline.
