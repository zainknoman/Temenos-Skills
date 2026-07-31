# Security, Multi-Tenancy & Rules Engine Reference

Source: `TAFJ_HOME/RulesEngine`, `docs/TAFJ-DevSecOps/`, verified 2026-07-31.

## Rules Engine

`TAFJ_HOME/RulesEngine/` contains `RulesEngine.jar`, `antlr.jar` (ANTLR —
confirms the rules language is grammar/parser-driven, not a simple
key-value config), `commons-codec.jar`, `commons-io.jar`,
`istack-commons-runtime.jar`, and a `doc/` subfolder with:
- `Rules Engine User Guide.doc` (2.5MB, Word format — **not** a PDF, so it is
  *not* covered by the `pipeline/pdf_extract.py` → vectordb pipeline; read it
  directly if deep Rules Engine detail is needed, it hasn't been indexed into
  Layer B).
- `Test.java`, `testcallj.b` — a real working sample pairing a Java rule test
  with a `CALLJ`-invoking Infobasic routine, useful as a template for how
  Infobasic invokes the Rules Engine via `CALLJ`.

## Multi-tenancy

`TAFJ-MultiTenant.pdf` documents TAFJ's multi-tenant deployment model. Read
this before assuming a single-tenant deployment pattern applies — don't
default to single-tenant assumptions in generated admin guidance without
checking whether the target environment is multi-tenant.

## Secure authentication

- `TAFJ-Secure-Authentication-Using-Keycloak.pdf` — Keycloak-based SSO/auth
  integration for TAFJ.
- `TAFJ-Kerberos_setup.pdf` — Kerberos-based authentication setup.

These are TAFJ-level authentication mechanisms — distinct from
`bnk/Extensions/EB_AuthenticationService` (a service-extension module, see
`temenos-integration`) and from `TemnXACML` (entitlements policy translation,
see `temenos-admin`). Three different layers of "security" exist in
this stack; don't conflate them when answering a security question — clarify
which layer (TAFJ-level auth, service-extension auth, or XACML entitlements)
the question is actually about.

## Message integrity & lightweight runtime

- `TAFJ-MessageIntegrity.pdf` — message integrity mechanism
  (`TAFJ_HOME/MessageIntegrity/` is a real directory in this install).
- `TAFJ-MicroEE.pdf` — MicroEE, a lighter-weight Java EE profile option for
  TAFJ; relevant when a deployment target can't or shouldn't run a full app
  server stack.
