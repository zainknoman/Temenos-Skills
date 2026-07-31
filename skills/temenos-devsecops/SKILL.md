---
name: temenos-devsecops
description: >
  Expert assistant for Temenos T24/Transact (TAFJ) build, test, debug, and security
  tooling: JBC precompiler rules, remote debugging, unit test framework, Maven plugin,
  SonarQube/code-coverage integration, the Rules Engine, multi-tenancy, and
  Keycloak/Kerberos secure authentication. This is tooling/process knowledge, distinct
  from both runtime administration and integration. Triggers: 'JBC precompiler',
  'remote debugger', 'unit test framework', 'TAFJ Maven plugin', 'SonarQube',
  'code coverage', 'Rules Engine', 'multi-tenant', 'multitenancy', 'Keycloak',
  'Kerberos', 'message integrity', 'MicroEE', 'TF Core', 'build pipeline',
  'CI for T24', 'testcallj', 'seat inject'.
---

# Temenos DevSecOps Skill

Build/test/debug/security-tooling knowledge for Temenos T24/Transact (TAFJ) — the
"how do I build, test, debug, and secure this properly" layer, distinct from
`temenos-admin` (runtime/install/DB), `temenos-migration` (versioning/patching),
and `temenos-integration` (ESB/messaging). For writing customisation code itself, route
to `temenos-dev` and its sub-skills.

## Reference Files

| File | When to read |
|------|-------------|
| [build-test-debug.md](references/build-test-debug.md) | Precompiler rules, remote debugging, unit testing, Maven plugin, SonarQube/code coverage |
| [security-multitenancy-rules.md](references/security-multitenancy-rules.md) | Keycloak/Kerberos auth, multi-tenancy, message integrity, the Rules Engine |

For procedural detail beyond these summaries:
```
python pipeline/query_docs.py "<question>" --topic TAFJ-DevSecOps -n 5
```
`docs/TAFJ-DevSecOps/` holds 14 official Temenos PDFs — copied from a real
`TAFJ_HOME/doc` on 2026-07-31.

## Working code samples on this environment

`TAFJ_HOME/samples/basic/` contains real, minimal Infobasic samples worth
using as a sanity-check baseline before debugging a more complex routine:
`HELLO` / `HELLO.FAILURE` / `HELLO.GR0`, `LOGGER.b`, `MAIN.PRG.b`,
`TEST.SUB.b`, `TEST.SUB1.b`, plus a `CBI/` subfolder. If a developer's
compile/runtime setup is suspect, compiling and running `HELLO` first isolates
tooling problems from routine-logic problems.
