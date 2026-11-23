---
name: temenos-admin
description: >
  Expert assistant for Temenos T24/Transact (TAFJ) installation, runtime configuration,
  application-server administration, database provisioning, and operational troubleshooting.
  Covers TAFJ.HOME layout (conf, dbdrivers, dbscripts, appserver), supported application
  servers (JBoss EAP, WebLogic, WebSphere Liberty), supported databases (Oracle, DB2, MS SQL,
  PostgreSQL, MongoDB, H2, NuoDB, Yugabyte), tafj.properties keys, TemnMonitor observability
  stack (Grafana/Prometheus/Jaeger/ELK/OpenTelemetry), TemnXACML entitlements, known
  install/runtime bugs, and COB (Close of Business) operations: stages, BATCH/PGM.FILE/TSA.SERVICE/
  TSA.PARAMETER setup, tSM/tSA agents, running and monitoring COB, EB.EOD.ERROR and crash recovery,
  multi-threaded job internals, and COB performance features. Triggers: 'TAFJ install', 'T24 admin', 'tafj.properties',
  'application server config', 'JBoss EAP', 'WebLogic install', 'DB driver', 'dbscripts',
  'TemnMonitor', 'observability stack', 'XACML', 'entitlements', 'startjboss', 'Transact
  Explorer', 'tools.jar error', 'TAFJ_CLASSPATH', 'JDK21 compilation error', 'DB tuning',
  'lock manager', 'read-only database', 'multi-tenant install', 'COB', 'close of business',
  'end of day', 'EOD', 'BATCH record', 'batch stage', 'TSA.SERVICE', 'TSA.PARAMETER',
  'TSA.WORKLOAD.PROFILE', 'tSM', 'tSA', 'START.TSM', 'EB.EOD.ERROR', 'COB crash', 'COMO',
  'AGENT.STATUS', 'JOB.TIMES', 'JT.ANALYSE', 'business stage COB', 'TS2024', 'ONLINE.SERVICE',
  'EB.EXTERNALISE.REPORT', 'BATCH.JOB.CONTROL', 'LIST file', 'bulking', 'elastic scaling',
  'EXIT.API', 'queue processing', 'Redis cache'.
---

# Temenos Administrator Skill

Administration/operations knowledge for a running Temenos T24/Transact (TAFJ) estate —
not code generation. For customisation code, route to `temenos-dev` and its sub-skills instead.

**Ground truth for this skill comes from an actual installed R25 Model Bank
(`TAFJ_HOME`), not invented values.** Any config key, script name, path, or version
number given here traces back to a real file — if asked something this skill's
references don't cover, say so and point at the relevant `docs/TAFJ-Admin/*.pdf`
rather than guessing.

## Reference Files

| File | When to read |
|------|-------------|
| [install-and-runtime.md](references/install-and-runtime.md) | First-time install, starting/stopping the environment, app-server choice, known install/compile bugs |
| [database-and-config.md](references/database-and-config.md) | Supported DBs, `dbdrivers`/`dbscripts` layout, `tafj.properties` and other `TAFJ_HOME/conf` files |
| [observability-and-security.md](references/observability-and-security.md) | TemnMonitor stack, TemnXACML entitlements/authorisation |
| [cob.md](references/cob.md) | Anything COB: stages and TS2024, BATCH/PGM.FILE/TSA.* setup, running COB, tSM/tSA internals, LIST files and bulking, errors and crash recovery, monitoring, performance features (select-ahead, elastic agents, queue processing, Redis) |

For anything deeper than these summaries — installation walkthroughs, tuning
parameters, exact config syntax — search the source PDFs directly:

```
py -3 pipeline/query_docs.py "<question>" --topic TAFJ-Admin -n 5
```

`docs/TAFJ-Admin/` holds 28 official Temenos PDFs covering install (per DB, per
app server), DB Tools, DB Performance, Logging, Lock Manager, Supported Commands,
Read-Only Database, Deprecation Mechanism, Default Properties, Eclipse setup,
and the TAFJ Updater — copied from a real `TAFJ_HOME/doc` on 2026-07-31.

`docs/COB/` holds the two Temenos COB courses (**COB Foundation**, then **COB Implementation**),
OCR'd from slide screenshots by `pipeline/docx_extract.py` on 2026-11-23. PDF page N is slide N:

```
py -3 pipeline/query_docs.py "<question>" --topic COB -n 5
```

## COB rules that matter most

Full detail is in [cob.md](references/cob.md). Before answering any COB question:

- **COB is operations, not code.** For writing a COB job routine (`.LOAD`/`.SELECT`/record routine,
  `BATCH.BUILD.LIST`), route the code to `temenos-infobasic` or `temenos-jbc`, using cob.md §6 for the
  framework contract.
- **Clear EB.EOD.ERROR first.** COB will not start while errors needing a fix are unresolved.
- **Never add batches or jobs under TS2024.** New clients cannot add batches or jobs to any COB stage.
  Use services, TSA.SERVICES.COB or exit APIs instead.
- **Business-stage COB is one-way.** TSA.PARAMETER BUSINESS.STAGE.COB=YES cannot be undone.
- **Check the release.** TSA.SERVICE PRE.COB.CHECK, TSA.PARAMETER LIST.JOBS and BATCH ASSOCIATED.JOBS
  exist in R25 but not R23.
- **Flag unverified names.** DATES, EB.EOD.ERROR, TSA.WORKLOAD.PROFILE and JOB.TIMES have no schema in
  Layer A, so their field names come only from the course screenshots.

## TAFJ_HOME layout (verified, R25)

```
TAFJ_HOME/
├── conf/             tafj.properties, TAFJTrace.properties, TAFJ.policy, .key, clientAPI.mapping
├── dbdrivers/         per-DB JDBC driver jars (db2, h2, mongodb, mssql, nuodb, oracle, postgresql, weblogic, yugabyte)
├── dbscripts/         per-DB provisioning scripts + BasicFunctions.java/.cs (shared T24 basic-function emulation layer)
├── appserver/         app-server integration layer
├── bin/                compiler launchers: tCompile.bat, tComponentBuild.bat, tComponentBuildProcess.bat, tComponentReport.bat, tJavadocMerge.bat
├── ext/, lib/, libMonitor/, libValidation/   runtime + monitoring + validation libraries
├── TemnMonitor/        bundled observability stack (see observability-and-security.md)
├── TemnXACML/          entitlements/authorisation modules (see observability-and-security.md)
├── RulesEngine/        business rules engine (see temenos-devsecops skill)
├── RELEASE, Patch.xml  version manifest + patch installer (see temenos-migration skill)
└── doc/                the 28 PDFs mirrored into docs/TAFJ-Admin/
```

## Quick facts (verified against the live install)

- Application server confirmed in use: **JBoss EAP 8.1** (`TAFJ_HOME/../jboss-eap-8.1`),
  started via `jboss-eap-8.1\startjboss.bat`. WebLogic and WebSphere Liberty are
  also officially supported (see `TAFJ-AS-*Install*.pdf`) but not what this
  particular environment runs.
- Default access (this install, per `INSTALL-GUIDE.md`): Transact Explorer at
  `http://localhost:8090/transact-explorer-wa`, Conventional Browser at
  `http://localhost:8090/BrowserWeb`, credentials `INPUTT`/`AUTHOR` (password
  `123456`). Treat these as environment-specific, not a universal default —
  don't assume they apply outside this install.
- Required JDK: **21** (`3rdParty/Java/jdk-21.0.6_windows-x64_bin.exe`).
