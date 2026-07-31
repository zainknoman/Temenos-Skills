---
name: temenos-integration
description: >
  Expert assistant for Temenos T24/Transact integration: ESB/payment-scheme integration
  packages, service-extension modules (EB_*/IF_*/AC_*/DF_*/PP_*), OFS message layer
  (ofsml), Email/SMS notification integration, and MQ/JMS connectivity. Covers the
  bnk/ESBProjects and bnk/NonESBProjects package structure, bnk/Extensions service
  modules, T24Email/T24Sms integration modules, and CALLJEE. Triggers: 'ESB', 'ESB
  project', 'payment scheme', 'OFS integration', 'ofsml', 'IBM MQ', 'JMS', 'CALLJEE',
  'T24Email', 'T24Sms', 'integration flow', 'inflow service', 'OFSConnector',
  'entitlement service', 'catalog service', 'automation service', 'DFMapping',
  'inbound security', 'integration landscape', 'PPBACS', 'PPBECS', 'RTGS'.
---

# Integration Expert Skill

Integration/interface knowledge for Temenos T24/Transact — ESB and non-ESB payment
integration packages, service-extension modules, and messaging connectivity. Not code
generation — for writing OFS/DE/componentised integration routines, route to `temenos-dev`
(→ `temenos-infobasic`, `temenos-jbc`, or `temenos-de`) instead.

**This skill's package/module lists are read directly off a real installed
environment (`bnk/ESBProjects`, `bnk/NonESBProjects`, `bnk/Extensions`).** The
4–6 letter package codes below (`PPBACS`, `PPESIC`, etc.) are listed as
observed, not semantically decoded — several map to recognisable payment
schemes (BACS, RTGS) by naming convention, but don't assume a code's meaning
beyond what's verified inside its own `ESB_SOURCE/` folder.

## Reference Files

| File | When to read |
|------|-------------|
| [esb-packages.md](references/esb-packages.md) | Full list of ESB/non-ESB payment-integration packages found on this environment |
| [service-extensions-and-messaging.md](references/service-extensions-and-messaging.md) | `bnk/Extensions` service modules, T24Email/T24Sms, ofsml, MQ/JMS, CALLJEE |

For deeper procedural detail (MQ install/SSL config, CALLJEE usage,
Componentisation-RESTful specifics):
```
python pipeline/query_docs.py "<question>" --topic TAFJ-Integration -n 5
```
`docs/TAFJ-Integration/` holds `TAFJ-IBM-MQ-with-WEBLOGIC-using-SSL-connectivity.pdf`,
`TAFJ-JMS-MQ-Install-8.0.pdf`, `TAFJ-CALLJEE.pdf`,
`Synopsis-of-T24-Java-documentations.pdf` — copied from a real `TAFJ_HOME/doc` on
2026-07-31.

## Two integration project trees, not one

`bnk/ESBProjects/` (72 packages) and `bnk/NonESBProjects/` (11 packages) are
**separate trees** — a package name appearing in both (e.g. `PI`, `PP`,
`PPAUBD`, `PPAUDE`) has distinct ESB and non-ESB variants. When asked to
locate or modify an integration package, confirm which tree the developer
means before touching files — they are not interchangeable, and a fix applied
in one tree does not propagate to the other.
