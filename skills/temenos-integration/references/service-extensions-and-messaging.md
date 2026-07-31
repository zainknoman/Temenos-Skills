# Service Extensions & Messaging Reference

Source: `bnk/Extensions/`, `TAFJ_HOME/T24Email`, `TAFJ_HOME/T24Sms`,
`TAFJ_HOME/ofsml`, `docs/TAFJ-Integration/`, verified 2026-07-31.

## `bnk/Extensions/` — 17 service-extension modules

These are packaged as installable services (naming convention:
`<Prefix>_<ServiceName>`):

| Module | Likely area (by name — not independently verified beyond the folder existing) |
|---|---|
| `AC_DDAService` | Account / DDA (Demand Deposit Account) service |
| `DF_DfMappingService` | Data-Field mapping service |
| `DS_DesignStudioInstallerService` | Design Studio installer service |
| `EB_AuthenticationService` | Authentication |
| `EB_AuthorizationService` | Authorization — see also `temenos-admin`'s TemnXACML note; this is a *service extension*, TemnXACML is the *policy-translation layer*, they are different mechanisms |
| `EB_AutomationService` | Automation |
| `EB_CatalogService` | Catalog |
| `EB_EntitlementService` | Entitlements |
| `EB_OFSConnectorService` | OFS connector — the most directly relevant module for external-system-to-T24 OFS integration work |
| `EB_ResourceProviderService` | Resource provider |
| `EB_Sms` | SMS (Security Management System, not text messaging — don't confuse with `T24Sms` below, which *is* the text-message notification module) |
| `IF_InboundSecurityService` | Inbound security |
| `IF_InflowService` | Inflow |
| `IF_IntegrationFlowService` | Integration flow |
| `IF_IntegrationFrameworkService` | Integration framework |
| `IF_IntegrationLandscapeService` | Integration landscape |
| `PP_TraFixService` | Payments — TraFix |

None of these module internals have been opened/surveyed yet — this table
records what exists, not implementation detail. Open the module directly for
implementation questions.

## Notification integration: T24Email / T24Sms

`TAFJ_HOME/T24Email/` — `config/`, `docs/`, `lib/`, `pdfTemplate/`, `template/`.
`TAFJ_HOME/T24Sms/` — `config/`, `docs/`, `lib/`.

Both are real, documented integration modules (each ships its own `docs/`
subfolder) for outbound email and SMS notification from T24. `T24Email`
additionally has a `pdfTemplate/` — implies PDF-generation capability for
emailed documents (e.g. statements), consistent with the Docupilot-adjacent
print/document-delivery pattern already covered by the `temenos-de` skill.

## OFS message layer: `ofsml`

`TAFJ_HOME/ofsml/` — `ofsml.jar`, `tcommon.jar`, `propertybag.jar`, plus
third-party support libs (`log4j-core`, `log4j-api`, `log4j-1.2-api`,
`commons-pool2`). This is the binary OFS-XML/message-layer library set — for
API-level detail, decompile/inspect the jars or consult
`Synopsis-of-T24-Java-documentations.pdf`, not this reference.

## MQ / JMS connectivity

`docs/TAFJ-Integration/` includes:
- `TAFJ-IBM-MQ-with-WEBLOGIC-using-SSL-connectivity.pdf` — IBM MQ integration
  specifically under WebLogic with SSL.
- `TAFJ-JMS-MQ-Install-8.0.pdf` — general JMS/MQ install for TAFJ 8.0.

Both are WebLogic/JMS-specific in their exact steps — if the target
environment runs JBoss EAP instead (as this R25 install does, per
`temenos-admin`), treat these as MQ *concept* references and verify
JBoss-specific messaging setup separately rather than following the WebLogic
steps literally.

## CALLJEE

`TAFJ-CALLJEE.pdf` — the CALLJEE mechanism for invoking Java/JEE code from
Infobasic. Query
`python pipeline/query_docs.py "CALLJEE" --topic TAFJ-Integration` for usage
detail rather than guessing syntax.
