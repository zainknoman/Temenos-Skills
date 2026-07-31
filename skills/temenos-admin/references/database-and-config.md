# Database & Configuration Reference

Source: `TAFJ_HOME/conf`, `TAFJ_HOME/dbdrivers`, `TAFJ_HOME/dbscripts`, verified 2026-07-31.

## Supported databases (JDBC drivers bundled)

`TAFJ_HOME/dbdrivers/` contains one directory per supported database — this is
the authoritative list of what R25 TAFJ ships driver support for:

| Directory | Database |
|---|---|
| `oracle-12c` | Oracle |
| `db2_v11.1` | IBM DB2 |
| `mssql-jdbc-12`, `sqljdbc_6.0` | Microsoft SQL Server (two driver generations) |
| `postgresql` | PostgreSQL |
| `mongodb_4.10.1` | MongoDB |
| `h2-1.3.161`, `h2-1.4.200`, `h2-2.3.232` | H2 (three versions — pick per target TAFJ version, don't assume the newest is always correct) |
| `nuodb-jdbc-21.0.0` | NuoDB |
| `yugabyte` | YugabyteDB |
| `weblogic-12.2.1.2` | WebLogic-specific JDBC integration |

`TAFJ_HOME/dbscripts/` mirrors this with per-DB provisioning script
directories: `oracle/`, `postgresql/`, `ms-sql/`, `db2/`, `h2/`, `nuodb/`,
`basic/`. Also at this level:
- `BasicFunctions.java` / `BasicFunctions.cs` / `BasicFunctionsSingle.java` —
  the shared T24 BASIC-function emulation layer used across DB backends.
- `Functions.java`, `StringUtils.java` — supporting utility classes.

For install steps per database, read the matching PDF in `docs/TAFJ-Admin/`
(`TAFJ-Oracle-Install.pdf`, `TAFJ-DB2-Install.pdf`, `TAFJ-MSSQLInstall.pdf`,
`TAFJ-PostgresSQLInstall.pdf`, `TAFJ-MongoDB-Install.pdf`,
`TAFJ-H2-Install.pdf`) or query:
```
python pipeline/query_docs.py "<question>" --topic TAFJ-Admin
```
Also see `TAFJ-DB Tools.pdf`, `TAFJ-DB-Performance.pdf`, `TAFJ-DB-Setup.pdf`,
`TAFJ-Read-Only-Database.pdf`, `TAFJ-Lock-Manager.pdf` for tuning and
DB-tooling specifics — do not invent tuning parameter names, look them up.

## `TAFJ_HOME/conf` — key files

| File | Purpose |
|---|---|
| `tafj.properties` | Main TAFJ runtime configuration (36KB — hundreds of keys; don't invent a key name, grep the actual file or the `TAFJ-Default Properties.pdf` reference) |
| `TAFJTrace.properties` | Tracing/diagnostics configuration |
| `TAFJ.policy` | Java security policy |
| `.key` | License/activation key |
| `.properties` | Additional install-time properties |
| `clientAPI.mapping` | TAFJ client API mapping |
| `TAFJDBComparer.default` | Default config for the DB-comparison tool |
| `TAFJDBImport.default` | Default config for the DB-import tool |
| `tafj.link` | Install linkage marker |

**Evidence of a real upgrade on this install:** `tafj.properties.bak` and
`tafj.properties.pre-v8.4.1.bak` both exist alongside the live
`tafj.properties` — this environment was upgraded across a TAFJ 8.4.1
boundary at some point. See the `temenos-migration` skill for upgrade
procedure; this file is cross-referenced there too, not duplicated.

## Deprecation & versioning

- `TAFJ-DeprecationMechanism.pdf` — how TAFJ signals deprecated APIs/config.
- `TAFJ-Supported-Commands.pdf` — the authoritative command reference; don't
  assume a CLI command exists without checking this.
