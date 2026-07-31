# R25 Model Bank Scan Report (Phase 1 — Reconnaissance)

Source: `C:\R25` (local R25 Model Bank install, read-only reference — not copied
into this repo, same pattern as `jar/`, `T24.javadoc/`, `docs/`).
Scan date: 2026-07-31.

This is a **live installed environment**, not a source archive: `INSTALL-GUIDE.md`
documents login (`http://localhost:8090/transact-explorer-wa`, `INPUTT`/`AUTHOR`,
pwd `123456`) and `Fix-R25-JDK21-Compilation.ps1` is a real troubleshooting script
for a JDK21/`tools.jar` compiler bug someone already hit and fixed on this box.
Both are genuinely valuable curated content, not noise.

## Top-level map

| Path | Nature | Verdict |
|---|---|---|
| `bnk/T24_BP` | ~hundreds of real `.b` Infobasic routines (AA calculations etc.) | **Extract** — real source examples |
| `bnk/ESBProjects` (28 pkgs) | Payment-scheme integration packages, each with `ESB_SOURCE/` | **Extract** (structure + a few samples) |
| `bnk/NonESBProjects` (11 pkgs) | Same pattern, non-ESB integrations | **Extract** (structure) |
| `bnk/Extensions` (17 svc modules) | `EB_*`/`IF_*` service extension modules (Auth, OFSConnector, IntegrationFlow, Sms...) | **Extract** — names + purpose |
| `bnk/UD` | Live runtime working directories (`&HOLD&`, `&TEMP&`, upload archives) | **Exclude** — runtime data, not reference material |
| `bnk/local` | Empty | **Exclude** |
| `bnk/t24lib` | ~650MB compiled per-module JARs (`AA_*.jar`, etc.) | **Exclude** — binary, superseded by existing `jar/` + `extract.py` pipeline |
| `bnk/t24wars` | One deployable `.war` | **Exclude** — build artefact |
| `bnk/Transact_L3_Javadoc` | Single `T24.javadoc.jar` (26MB) | **Compare** — likely same/overlapping content as `T24.javadoc/` already indexed; not clearly newer. Skip unless diffing shows new classes. |
| `TAFJ/conf` | Real runtime config: `tafj.properties` (+ versioned `.bak` incl. a `pre-v8.4.1.bak` showing an actual upgrade), `TAFJDBComparer.default`, `TAFJDBImport.default` | **Extract** — config key reference + upgrade evidence |
| `TAFJ/dbdrivers` | 12 driver dirs: db2, h2 (×3 versions), mongodb, mssql, nuodb, oracle, postgresql, sqljdbc, weblogic, yugabyte | **Extract** — supported-DB matrix |
| `TAFJ/dbscripts` | Per-DB script dirs (oracle/postgresql/ms-sql/db2/h2/nuodb/basic) + `BasicFunctions.java`/`.cs` | **Extract** — DB provisioning reference |
| `TAFJ/doc` | **53 official Temenos PDFs**: install guides per DB and per app server (WebLogic, JBoss v7/v8, WebSphere Liberty), `TAFJ-Upgrade.pdf`, `TAFJ-MultiTenant.pdf`, `TAFJ-Secure-Authentication-Using-Keycloak.pdf`, `TAFJ-Kerberos_setup.pdf`, IBM MQ/JMS install, `TAFJ-Lock-Manager`, `TAFJ-Logging`, `TAFJ-JBC-Precompiler-Rules`, `TAFJ-JBC-Remote-Debugger`, `TAFJ-UnitTestFramework`, `TAFJ-Maven-Plugin`, GIT/RTC ChangeSet Installation, `T24-Componentisation(-RESTful-WS)`, `TAFJ-DSPackageInstaller`, `TAFJ-Supported-Commands`, `TAFJ-Read-Only-Database`, `TAFJ-DeprecationMechanism` | **This is the single richest source in the scan** — official admin/install/upgrade/security manual set |
| `TAFJ/javadoc` | `TAFJClient-javadoc.jar` — TAFJ framework client API (distinct from business-layer javadoc) | **Extract** if a temenos-admin/integration skill needs client API calls |
| `TAFJ/ofsml` | `ofsml.jar`, `tcommon.jar`, `propertybag.jar` + 3rd-party libs | **Low priority** — binary, OFS message-layer plumbing |
| `TAFJ/PROC` | Effectively empty (15-byte readme) | **Exclude** |
| `TAFJ/RulesEngine` | `RulesEngine.jar` + antlr + **`doc/Rules Engine User Guide.doc`** (2.5MB) + `Test.java`/`testcallj.b` samples | **Extract** — real user guide + working sample |
| `TAFJ/Regression` | `SeatInject` scripts + bin/lib | **Low priority** — seat/license injection tooling, not test content |
| `TAFJ/samples/basic` | Real minimal Infobasic samples (`HELLO`, `LOGGER.b`, `MAIN.PRG.b`, `TEST.SUB*.b`) + a `CBI/` subfolder | **Extract** — good for `temenos-infobasic` skill enrichment |
| `TAFJ/T24Email`, `TAFJ/T24Sms` | `config/docs/lib/template` each — real notification integration modules | **Extract** — temenos-integration material |
| `TAFJ/TemnMonitor` | Full observability stack: elasticsearch, grafana, helm, influxdb, jaeger, logstash, opentelemetry, prometheus, pushgateway, splunk, `docker-compose-monitoring.yml`, `README.txt` | **Extract** — real ops/monitoring stack, strong admin material |
| `TAFJ/TemnXACML` | `authz-decision-adapter`, `transact-authz`, `SMS2XACML_Generator` (zips) | **Extract structure only** — entitlements/XACML security integration, zips not worth unpacking wholesale |
| `TAFJ/RELEASE`, `TAFJ/Patch.xml` | Release manifest + patch installer script (lists exactly which dirs a patch touches: `bin, dbdrivers, dbscripts, lib, libMonitor, libValidation, TemnMonitor, ext, appserver, JMSInjector, TAFJSessionMonitor, eclipse, ofsml`) | **Extract** — direct migration/patch procedure evidence |
| `DesignStudioT24-R25.2` | Eclipse-based IDE binaries + empty workspace | **Skip deep extraction** — it's the IDE itself, not T24 content; maybe one short "how Design Studio maps to skill artefacts" note at most |
| `jboss-eap-8.1` | Standard JBoss EAP 8.1 distribution | **Skip** — third-party app server, just record "R25 runs on JBoss EAP 8.1, port 8090" as a fact |
| `3rdParty/Database` | **8.7GB `MBR25.bak`** (full SQL Server backup of the model bank DB) + `R25_Data`/`R25_log` | **Exclude entirely** — huge binary, not reference material. Worth one line noting a restorable seed DB backup exists, for temenos-migration context only. |
| `3rdParty/Java` | JDK 21 installer | **Exclude** — confirms JDK 21 is the required runtime (ties to the JDK21 fix script) |
| `3rdParty/Node` | Node v24 runtime | **Exclude** — confirms Node is bundled, purpose not yet clear (likely Design Studio or ESB tooling) |

## Root-level curated files (already read in full)

- `INSTALL-GUIDE.md` — login/access instructions for this specific install (Transact Explorer URL, port 8090, `INPUTT`/`AUTHOR` creds, start via `jboss-eap-8.1\startjboss.bat`)
- `Fix-R25-JDK21-Compilation.ps1` — real fix for a documented bug: JDK 21 removed `lib\tools.jar`; five TAFJ compiler launchers (`tCompile.bat`, `tComponentBuild.bat`, `tComponentBuildProcess.bat`, `tComponentReport.bat`, `tJavadocMerge.bat`) still reference it in `TAFJ_CLASSPATH`, causing a "Could not find or load main class ...tools.jar" error. This is exactly the kind of concrete, non-inventable admin knowledge CLAUDE.md wants captured with a source citation.

## Cross-check: bnk/Transact_L3_Javadoc vs. existing java-api.md / class-index.md

Not yet diffed — `T24.javadoc.jar` (26MB) needs to be unzipped and compared against
`skills/temenos-dev/references/apis/java-api.md` (157 classes) and `class-index.md`
(77,762 classes) before deciding whether it adds anything. Flagging as an open
item for Phase 2, not resolved here.

## Skill mapping proposal (revised from the original hypothesis)

- **temenos-admin** — `TAFJ/doc` (install/upgrade/security/DB PDFs),
  `TAFJ/conf`, `TAFJ/dbdrivers`, `TAFJ/dbscripts`, `TAFJ/TemnMonitor`,
  `TAFJ/TemnXACML`, `jboss-eap-8.1` (as a fact, not deep-extracted),
  `INSTALL-GUIDE.md`, `Fix-R25-JDK21-Compilation.ps1`. This is the best-supported
  new skill in the scan — strong primary sources throughout.
- **temenos-migration** — `TAFJ/RELEASE`, `TAFJ/Patch.xml`, `TAFJ-Upgrade.pdf`,
  `TAFJ-GIT-ChangeSet-Installation.pdf`, `TAFJ-RTC-ChangeSet-Installation.pdf`,
  `tafj.properties.pre-v8.4.1.bak` (real evidence of a version jump), the
  DB-specific install PDFs (Oracle/Postgres/MSSQL/DB2/MongoDB/H2). Well-supported.
- **temenos-integration** — `bnk/ESBProjects` (28 payment-scheme packages),
  `bnk/NonESBProjects`, `bnk/Extensions` (`EB_OFSConnectorService`,
  `IF_IntegrationFlowService`, `IF_IntegrationFrameworkService`,
  `IF_IntegrationLandscapeService`, `EB_Sms`, `EB_AuthenticationService`,
  `EB_AuthorizationService`), `TAFJ/T24Email`, `TAFJ/T24Sms`, `TAFJ/ofsml`,
  `T24-Componentisation-RESTful-WS.pdf`, `TAFJ-IBM-MQ-with-WEBLOGIC.pdf`,
  `TAFJ-JMS-MQ-Install-8.0.pdf`. Well-supported, and payment-scheme package names
  (BACS, BECS, CHAPS-style codes) give it real specificity.
- **temenos-architect** — weakest-supported of the four original candidates.
  `bnk/T24_BP` is real source but is really routine-level, not architecture-level;
  `bnk/Extensions` and `bnk/UD` are runtime/packaging, not design docs. Recommend
  narrowing scope to "package/extension structure and componentisation patterns"
  (backed by `T24-Componentisation.pdf`) rather than a broad "architect" skill —
  or folding it into `temenos-jbc` as an enrichment instead of a new skill.
- **New candidate: temenos-devsecops** (not in original hypothesis) —
  `TAFJ-JBC-Precompiler-Rules.pdf`, `TAFJ-JBC-Remote-Debugger.pdf`,
  `TAFJ-UnitTestFramework.pdf`, `TAFJ-Maven-Plugin.pdf`, `TAFJ/RulesEngine`
  (+ its User Guide), `TAFJ-MultiTenant.pdf`, `TAFJ-Secure-Authentication-Using-Keycloak.pdf`,
  `TAFJ-Kerberos_setup.pdf`, `TAFJ/TemnMonitor` (observability stack),
  `CodeCoverageReceiver.pdf`, `JBC-SonarQube-Plugin.pdf`. This is a distinct,
  well-supported cluster (build/test/debug/observability/security tooling) that
  doesn't fit cleanly into admin, migration, or integration. Proposing it as a
  fifth candidate rather than force-fitting into the other four.
- Not recommending a dedicated skill for: `TAFJ/Regression` (SeatInject is
  license-seat tooling, not test content), `DesignStudioT24` internals (it's the
  IDE, not T24 knowledge), `jboss-eap-8.1` internals (generic JBoss, not
  T24-specific).

## Recommendation

Proceed to Phase 2 for **temenos-admin**, **temenos-migration**,
**temenos-integration**, and **temenos-devsecops** — all four have concrete,
citable primary sources. Downgrade **temenos-architect** to either a narrower
"componentisation & packaging" scope or skip it as a standalone skill and instead
enrich `temenos-jbc` with the `T24-Componentisation*.pdf` material.

## Outcome (Phase 2 — completed 2026-07-31)

User decisions on the two open scope questions:
- `temenos-architect`: build as a **standalone skill** (user overrode the
  fold-into-`temenos-jbc` recommendation), scoped narrowly per the
  "weakly supported" finding above — componentisation architecture +
  package/routine naming-convention structure only, with explicit
  cross-references to `temenos-jbc` and `temenos-integration` rather than
  duplicating their content.
- `temenos-devsecops`: added as proposed.

Built:
- `skills/temenos-admin/` — SKILL.md + 3 references (install-and-runtime,
  database-and-config, observability-and-security)
- `skills/temenos-migration/` — SKILL.md + 2 references (patch-and-release,
  changeset-and-upgrade)
- `skills/temenos-integration/` — SKILL.md + 2 references (esb-packages,
  service-extensions-and-messaging)
- `skills/temenos-devsecops/` — SKILL.md + 2 references (build-test-debug,
  security-multitenancy-rules)
- `skills/temenos-architect/` — SKILL.md + 2 references (componentisation-model,
  package-and-routine-structure)
- 53 PDFs copied from `C:\R25\TAFJ\doc` into `docs/{TAFJ-Admin,TAFJ-Migration,
  TAFJ-Integration,TAFJ-DevSecOps,T24-Componentisation}/` and re-embedded into
  the existing Layer B vectordb via `pipeline/pdf_extract.py` (additive —
  original ~3,127 cached PDFs untouched).
- `CLAUDE.md` updated: repository layout tree, Layer B contents note, Next
  tasks P6.

Corrected during the scan: initial ESBProjects count of "28 packages" (from a
`head -30`-truncated listing) was wrong — the full, untruncated list is
**72 packages**. `esb-packages.md` uses the corrected count.

Not done in this pass (flagged as open items in the relevant reference files,
not silently skipped):
- `bnk/Transact_L3_Javadoc/T24.javadoc.jar` vs. existing `java-api.md`/
  `class-index.md` diff — not resolved.
- `TAFJ/RulesEngine/doc/Rules Engine User Guide.doc` — Word format, not
  ingested by the PDF-only `pdf_extract.py` pipeline; noted, not indexed.
- Per-ESB-package content survey (`ESB_SOURCE/` internals) — package
  *existence* captured, not package *purpose*.
