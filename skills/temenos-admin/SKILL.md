---
name: temenos-admin
description: >
  Expert assistant for Temenos T24/Transact (TAFJ) installation, runtime configuration,
  application-server administration, database provisioning, and operational troubleshooting.
  Covers TAFJ.HOME layout (conf, dbdrivers, dbscripts, appserver), supported application
  servers (JBoss EAP, WebLogic, WebSphere Liberty), supported databases (Oracle, DB2, MS SQL,
  PostgreSQL, MongoDB, H2, NuoDB, Yugabyte), tafj.properties keys, TemnMonitor observability
  stack (Grafana/Prometheus/Jaeger/ELK/OpenTelemetry), TemnXACML entitlements, and known
  install/runtime bugs. Triggers: 'TAFJ install', 'T24 admin', 'tafj.properties',
  'application server config', 'JBoss EAP', 'WebLogic install', 'DB driver', 'dbscripts',
  'TemnMonitor', 'observability stack', 'XACML', 'entitlements', 'startjboss', 'Transact
  Explorer', 'tools.jar error', 'TAFJ_CLASSPATH', 'JDK21 compilation error', 'DB tuning',
  'lock manager', 'read-only database', 'multi-tenant install'.
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

For anything deeper than these summaries — installation walkthroughs, tuning
parameters, exact config syntax — search the source PDFs directly:

```
python pipeline/query_docs.py "<question>" --topic TAFJ-Admin -n 5
```

`docs/TAFJ-Admin/` holds 28 official Temenos PDFs covering install (per DB, per
app server), DB Tools, DB Performance, Logging, Lock Manager, Supported Commands,
Read-Only Database, Deprecation Mechanism, Default Properties, Eclipse setup,
and the TAFJ Updater — copied from a real `TAFJ_HOME/doc` on 2026-07-31.

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
