# Package & Routine Structure Reference

Source: `bnk/T24_BP/`, `bnk/Extensions/`, `bnk/ESBProjects/`, verified 2026-07-31
against a real R25 install.

## The base routine repository is a flat, naming-convention-organised tree

`bnk/T24_BP/` holds **2,955 `.b` Infobasic routines** in a single flat
directory — there is no folder-per-application structure. The organising
principle is the routine **name prefix**, not directory placement. Prefix
frequency on this install:

| Prefix | Count | Likely role |
|---|---|---|
| `CONV.*` | 943 | Conversion routines (upgrade/data-conversion) |
| `E.*` | 805 | Enquiry routines |
| `OC.*` | 132 | OFS conversion routines |
| `AA.*` | 114 | Arrangement Architecture (lending/deposits) routines |
| `V.*` | 64 | Version routines |
| `SCDX.*` | 62 | — not decoded, verify per-routine before asserting purpose |
| `DE.*` | 62 | Delivery Engine (see `temenos-de` skill) |
| `FT.*` | 41 | Funds Transfer |
| `PP.*` | 22 | Payments |
| `DAS.*` | 22 | — not decoded |
| `SC.*` | 21 | — not decoded (note: distinct from the `SC` ESB package in `temenos-integration`) |

**Practical implication:** when asked "where does routine X live" or "what
pattern should a new routine follow," the answer is governed by naming
convention + application-code prefix, not directory architecture. Don't
invent a folder-based mental model for this codebase — verify by grepping
the actual prefix distribution before asserting where something belongs.

## Extension-module packaging pattern

`bnk/Extensions/` packages functionality as one directory per service,
named `<ShortPrefix>_<ServiceName>` (e.g. `EB_OFSConnectorService`,
`IF_IntegrationFlowService`) — 17 such modules exist on this install. Full
list and per-module notes live in `temenos-integration`'s
`service-extensions-and-messaging.md` (not duplicated here — that skill owns
the module inventory since they're primarily integration-purposed).

## Integration-package structure

`bnk/ESBProjects/` and `bnk/NonESBProjects/` each package one integration
target per top-level directory, with source under an `ESB_SOURCE/`
subfolder (e.g. `bnk/ESBProjects/PPBACS/ESB_SOURCE/`). Full package
inventory lives in `temenos-integration`'s `esb-packages.md` — this file only
notes the *structural pattern* (one dir per integration target, source
nested under `ESB_SOURCE/`), not the full list, to avoid maintaining the
same inventory in two places.
