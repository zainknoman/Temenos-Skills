# SEPA in Temenos Transact — Architecture

Provenance tags are defined in [`provenance.md`](provenance.md).

---

## The single most important structural fact

**This JAR set contains two entirely separate SEPA implementations.** They do not
share applications, tables, routines or hooks. Answering a SEPA question without
first establishing which one the bank runs produces guidance that is wrong in
every detail. `[JAR]`

| | **EP — European Payments** | **PP — Temenos Payments / TPH** |
|---|---|---|
| JAR prefix | `EP_` (14 JARs) | `PP_` (108 JARs) + `PI_` (8) + `PW_` |
| Core tables | `SEPA.*` (29 applications: `SEPA.PARAMETER`, `SEPA.OUTWARD`, `SEPA.INWARD`, `SEPA.MANDATE`, `SEPA.PEACH`, `SEPA.REASONS`, `SEPA.LAYOUT`, `SEPA.HEADER`, `SEPA.REFUSAL`, …) | `PP.*` (167 applications) + `POR.*` (the neutral payment object) + `PAYMENT.ORDER` |
| Message definition | `UNIFI.XML.FORMAT` / `UNIFI.XML.MESSAGE` / `UNIFI.XML.TAG` — a table-driven ISO 20022 schema engine. `UNIFI.XML.TAG` even carries a `UsedBySepa` multivalue field. | XSD + XSLT on the file system, referenced from `PP.CLEARING` (`PP.CG.SchemaFolder`, `PP.CG.StyleSheetFolder`) |
| Mapping implementation | ~1,900 compiled jBC routines named `SEPA_*` (e.g. `SEPA_SET_ULTMT_CRED_NAME`, `SEPA_UPDATE_REASON_CODE_CAMT29_ISO`, `SEPA_RVSD_INSTD_AMT_MAP`) | Mapping *APIs* named in configuration fields, implemented as `EB.API` METHOD records over Java hooks, or as jBC subroutines |
| Java customisation surface | **None.** No `EP_*Hook.jar` exists. | 16 hook classes — see [`java-api.md`](java-api.md) |
| Character handling | `SepaUtf8Process_convertCharacters`, `SepaUtf8Process_convertGermanAlphabets` `[JAR]` | `PP.CG.AllowUTF8Characters` → `PP.BANK.CONDITIONS` → `PP.COMPANY.PROPERTIES`; `PP.CHAR.CONVERSION` `[SCHEMA]` |
| Vendor position | Rulebook maintenance documents are published separately for EP. On the 2019 camt.087 workflow: *"System does not support generation of camt.087 or receipt of camt.029.001.008 as the originator bank and the automatic response to camt.087. **Temenos suggests upgrade to TPH to support this workflow.**"* `[PDF SEPA_Rulebook_Changes_2019_European Payments (EP).pdf p.10]` | The strategic product; receives the full rulebook change set. |

**Practical rule:** if the bank's SEPA tables are `SEPA.OUTWARD` / `SEPA.INWARD`,
it is EP and all customisation is Infobasic/jBC. If they are `POR.TRANSACTION` /
`PP.CLEARING`, it is TPH and Java L3 hooks are available.

---

## TPH — component map

Confirmed application inventory (382 payment-domain applications with exact field
lists in [`applications.md`](applications.md)). The ones that matter for a SEPA
clearing implementation:

### Initiation and order management

| Application | Role | Source |
|---|---|---|
| `PAYMENT.ORDER` | Order capture: channel intake, validation, storage until processing date, manual repair/release, routing decision | `[SCHEMA]` `PI_Contract.jar` |
| `PAYMENT.ORDER.PARAMETER` | Company-level PO configuration | `[SCHEMA]` |
| `PAYMENT.ORDER.COUNTRY.RULES` | Country rules for outward payments — IBAN/BIC allowed, clearing code format, allowed currencies | `[SCHEMA]` |
| `PAYMENT.ORDER.PRODUCT` | Product-level features: calendar, IBAN/BIC usage, FX, warehousing, charging, reachability | `[SCHEMA]` |
| `PAYMENT.ORDER.HIST`, `PAYMENT.ORDER.NOTIFICATION` | History and notification | `[SCHEMA]` |
| `PI.PS.MAPPING.RULE` | Payment Order → source-system status update mapping | `[SCHEMA]` |
| `PI.ERROR.REASON.CODE`, `PI.ISO.EXTERNAL.CODE`, `PI.GPI.TRACKER` | Reason-code and ISO external-code registries; SWIFT gpi tracking | `[SCHEMA]` |
| `PAYMENT.CATEG.PURPOSE`, `PAYMENT.PURPOSE.CODE` | Category-purpose and purpose-code static data | `[SCHEMA]` |

Setup order documented as: `PAYMENT.ORDER.PARAMETER` → `PAYMENT.ORDER.COUNTRY.RULES`
→ `PAYMENT.ORDER.PRODUCT`. `[PDF TPH - Copy/Payment Order Application/PAYMENT ORDER.pdf p.2]`

### The neutral payment object — `POR.*`

TPH maps every inbound clearing message into "internal POR tables (TPH neutral
payment object)" before any processing.
`[PDF TPH - Copy/Messaging Framework/Introduction to Messaging Framework.pdf p.16]`

Principal tables: `POR.TRANSACTION` (the payment itself), `POR.SUPPLEMENTARY.INFO`
(extended / ISO 20022 elements not modelled on `POR.TRANSACTION`),
`POR.AGREEMENT.AND.ADVICE`, `POR.POSTING.AND.CONFIRMATION`, `POR.AUDIT.TRAIL`,
`POR.PARTYCREDIT` / `POR.PARTYDEBIT`, `POR.REMITTANCEINFSTRUCTURED`,
`POR.PAYMENTSTATUSCODE`, `POR.PAYMENTCURRENTSTATUS`, `POR.SCREENINGREQUESTS`,
`POR.DUPLICATECHECK`, `POR.CLG.IN.SETTLEMENT.PENDING` /
`POR.CLG.OUT.SETTLEMENT.PENDING`, `POR.STATEMENTLINE`. `[SCHEMA]`

Those five record types — `PorTransactionRecord`, `PorSupplementaryInfoRecord`,
`PorAgreementAndAdviceRecord`, `PorPostingAndConfirmationRecord`,
`PorAuditTrailRecord` — are the exact parameter set passed to
`PaymentLifecycle.postUpdateRequest` and `postRequestToExternalSystem`. `[JAR]`

### Clearing configuration

`PP.CLEARING` → `PP.CLEARING.SETTING` → `PP.MSGMAPPINGPARAMETER` →
`PP.CLEARING.COMPANY` → `PP.RETURN.MAPPING.PARAM`, plus `PP.CLEARING.DIRECTORY`,
`PP.CLEARING.NATURE.CODE`, `PP.CLEARING.RETURNCODE`, `PP.CLEARING.FREQUENCY`,
`PP.CLEARING.NONWORKINGDAY`, `PP.CLEARING.STATUS.REPORT`. Field-level detail in
[`config-reference.md`](config-reference.md). `[SCHEMA]`

Menu path and the grouping of these records is confirmed as
*Clearing / Clearing Company / Clearing Nature Code / Clearing Setting / Clearing
Return Code / Clearing Frequency / Clearing Transaction Tables / Return Mapping
Param* under **Admin menu > Payments Hub > Local Clearing**.
`[PDF Core/PAYMENT HUB/PAYMENT HUB/2 Parameters/Local Clearing.pdf p.1, p.8]`

### Inward message acceptance

`PP.MSG.ACCEPTANCE.PARAM` is the queue-level entry point. The documented
`INWARD.MAPPING` service sequence is:

1. Receive the file.
2. Read `PP.MSG.ACCEPTANCE.PARAM` for the queue; invoke **Validate API** and
   **Debulk API** to validate and debulk the message.
3. On success, map the message to the internal POR tables.

`[PDF TPH - Copy/Messaging Framework/Introduction to Messaging Framework.pdf p.16]`

`PP.MSG.ACCEPTANCE.PARAM` fields configure `InFolder Name`, `Queue Name`,
`Backup Folder`, `Schema Folder`, `Stylesheet Folder`, `Generic Folder`,
`Error Folder`; Schema/Stylesheet/Generic are explicitly *not* configured for
non-XML input. `[PDF ibid.]`

Named integration flow property files (ESB/non-ESB):
`PP_InwardXML_InwardIntegrity` / `PP_InwardXML_T24Inward` (non-instant),
`PPINST_InstantInward_InwardIntegrity` / `PPINST_InstantInward_T24Inward`
(instant), `PI_POInstantInward_InwardIntegrity` / `PI_POInstantInward_T24Inward`
(payment order inward), `PPIPCL_CreditTransferIP_OutwardIntegrity` /
`PPIPCL_CreditTransferIP_T24Outward` (agent banking).
`[PDF TPH - Copy/Messaging Framework/Introduction to Messaging Framework.pdf p.7]`

### SEPA participation type

*"TPH bank can be a direct or an indirect participant of SEPA. The channel through
which it routes payment determines the participation type in TPH."* Configured at
**Admin Menu > Payments Hub > Local Clearing > Clearing** (i.e. on `PP.CLEARING`,
field `PP.CG.ParticipantType`).
`[PDF TPH-R21/SEPA/Configuring SEPA Credit Transfer.pdf p.1]`

For indirect participants: *"Each IP of the output channel is considered as a
clearing correspondent in the `PP.CLEARINGCORRESPONDENTS` and identified by the
Clearing ID (output channel), Currency BIC or NCC,"* with the IP's Vostro account
derived from that record. `[PDF ibid. p.9]` `PP.CLEARINGCORRESPONDENTS` is present
in this JAR set. `[SCHEMA]`

### Reachability

`PP_ClearingFrameworkService.jar` contains four distinct reachability checks as
separate compiled component methods — including one named specifically for SEPA:

- `ClearingFrameworkService.checkSEPAReachability`
- `ClearingFrameworkService.checkACHReachability`
- `ClearingFrameworkService.checkRTGSReachability`
- `ClearingFrameworkService.checkReachability`

plus `validateOutputChannel`, `validateCrPtyQueue`, and
`ClearingFrameworkDASService.hashTheBIC`. `[JAR]`

Reachability is switched by `PP.CG.SkipReachability` (`Y` = skip, `N`/blank = check)
against the uploaded `PP.CLEARING.DIRECTORY`. `[SCHEMA]`

---

## Java customisation surface (TPH only)

16 hook classes, exact signatures in [`java-api.md`](java-api.md). `[JAR]`

| Hook | JAR | What it governs |
|---|---|---|
| `com.temenos.t24.api.hook.payments.PaymentLifecycle` | `PP_PaymentLifecycleHook.jar` | The main surface — 26 overridable methods covering party validation, account derivation, dates, charges, transaction code, routing product, bulking/grouping, file naming, clearing validation, external-core-system integration |
| `com.temenos.t24.api.hook.payments.PaymentOrderLifecycle` | `PI_PaymentOrderLifecycleHook.jar` | `PAYMENT.ORDER` record events: `handleValidationEvent`, `validatePaymentOrderRecord`, `applyChargeType`, `setProductId`, `getPaymentSystemType` |
| `com.temenos.t24.api.hook.PaymentOrderHook` | `PI_PaymentOrderHook.jar` | `PAYMENT.ORDER.PRODUCT` product-determination and conditional-fee APIs |
| `com.temenos.t24.api.hook.payments.Message` | `PP_MessageHook.jar` | Message-level mapping: `updatePaymentObject`, `updateFieldValue`, `updateInformationLine`, `updateMessageStatus` |
| `com.temenos.t24.api.hook.ComponentApiHook` | `PP_ComponentApiHook.jar` | Party/account/date component APIs shared across services |
| `com.temenos.t24.api.hook.MessageAcceptanceParamHook` | `PP_MessageAcceptanceParamHook.jar` | Inbound acceptance: validate, ACK, debulk, message-forward APIs |
| `com.temenos.t24.api.hook.FeeDeterminationHook` | `PP_FeeDeterminationHook.jar` | Fee determination |
| `com.temenos.t24.api.hook.BalanceCheckApiHook` | `PP_BalanceCheckApiHook.jar` | Balance check / recycler / manual-auth-required |
| `com.temenos.t24.api.hook.PostingSchemeAPIHook` | `PP_PostingSchemeAPIHook.jar` | Posting scheme |
| `com.temenos.t24.api.payments.DataAccess` | `PP_DataAccessApi.jar` | **Called, not extended.** `getPaymentRecord(String) → PorTransactionRecord`, `getActiveId(String, String) → String` |
| `com.temenos.t24.api.hook.foundation.Process` | `PW_ProcessHook.jar` | Payment workflow `getActivity` |
| `com.temenos.t24.api.hook.contract.DirectDebit` | `DD_ContractHook.jar` | Direct Debit contract |
| `com.temenos.t24.api.hook.DebitCollectionOrderHook` | `DB_DebitCollectionOrderHook.jar` | Debit collection order |
| `com.temenos.t24.api.hook.clearing.InwardEntry` | `FT_ClearingHook.jar` | FT local-clearing inward entry |
| `com.temenos.t24.api.hook.accounting.ClearingService` | `AC_ClearingServiceHook.jar` | Accounting clearing service |
| `com.temenos.t24.api.hook.countrymodelbank.usa.Clearing` | `ACHFRM_ClearingHouseHook.jar` | US ACH country model bank |

### How a hook is wired in

The pattern is documented inside the field descriptions themselves. Quoting
`PP.CLEARING` `PP.CG.BulkingCriteriaAPI` verbatim:

> "Specify either a jBC subroutine name … For java implementations: An `EB.API`
> record of type `METHOD` which implements an interface defined in the `EB.API`
> record `PP.CLEARING.BulkingCriteriaAPI.HOOK`. This field supports the
> `PaymentLifecycle.getGroupingCriteria()` method. The `PaymentLifecycle` class is
> in the `com.temenos.t24.api.hook.payments` package which is in
> `PP_PaymentLifecycleHook.jar` shipped with T24."

`[SCHEMA table-schema/PP.CLEARING.md field 12]`

So: **configuration field → `EB.API` METHOD record → your subclass of the hook →
overridden method.** Same shape for `PP.CG.BulkFileRefAPI` →
`PP.CLEARING.bulkRefAPI.HOOK` → `PaymentLifecycle.getBulkPaymentReference()`, and
`PP.CG.PhysicalFileNameAPI` → `PP.CLEARING.PhyFileNameAPI.HOOK`. `[SCHEMA]`

---

## Payment lifecycle

Stage sequence, with the artefact that owns each stage. Stages marked `[PUBLIC]`
are the standard TPH flow described in vendor overview material but not pinned to
a specific routine in these artifacts.

| # | Stage | Owner in this JAR set |
|---|---|---|
| 1 | Channel intake / order capture | `PAYMENT.ORDER` (`PI_Contract.jar`) `[SCHEMA]` |
| 2 | Order validation, product determination, charging | `PaymentOrderLifecycle.validatePaymentOrderRecord` / `.setProductId` / `.applyChargeType`; `PaymentOrderHook` product APIs `[JAR]` |
| 3 | Routing / payment-system determination | `PaymentOrderLifecycle.getPaymentSystemType`; `PaymentLifecycle.getRoutingProductId` / `.updateProduct` `[JAR]` |
| 4 | Map to neutral payment object | `POR.*` tables `[PDF Messaging Framework p.16]` |
| 5 | Party validation and account derivation | `PaymentLifecycle.validateDebitParty` / `.validateCreditParty` / `.getDebitAccount` / `.getCreditAccount` / `.getAccountLocation` / `.getPostingRestriction` `[JAR]` |
| 6 | Date determination | `PaymentLifecycle.getPaymentDate`; `PP_DateDeterminationService.jar` `[JAR]` |
| 7 | Sanctions / AML filtering | `PP_FilteringService.jar`, `PP_RiskFilterService.jar`, `POR.SCREENINGREQUESTS`; `PP.CG.ScreeningResponseAction` governs behaviour on a *Possible Hit* (`SendPendingConfirmation` / `Reject` / blank) `[JAR]` `[SCHEMA]` |
| 8 | Duplicate check | `PP_DuplicateCheckService.jar`, `POR.DUPLICATECHECK`, `POR.DUPLICATECRITERIA` `[JAR]` |
| 9 | Fee determination | `FeeDeterminationHook`, `PaymentLifecycle.getChargeResponse` `[JAR]` |
| 10 | Balance check / fund reservation | `BalanceCheckApiHook`, `PP_BalanceCheckService.jar` `[JAR]` |
| 11 | Repair | `PP_AutomatedRepairToolService.jar`, `POR.REPAIR.AUDIT`, `POR.AUTOREPAIR.AUDIT.LOG` `[JAR]` |
| 12 | Clearing validation | `PaymentLifecycle.validatePaymentForClearing`; `PP.CG.OutValidateAPI`, `PP.CGS.ValidateAPI` `[JAR]` `[SCHEMA]` |
| 13 | Posting | `PostingSchemeAPIHook`, `PP_PostingSchemeService.jar`, `POR.POSTINGLINE`, `PAYMENT.ORDER.ENTRY` `[JAR]` |
| 14 | Bulking and outward message generation | `PaymentLifecycle.getGroupingCriteria` / `.getCustomGroupingValues` / `.getBulkPaymentReference` / `.getFileName`; `PP_OutwardMappingFramework.jar` staging tables `PP.OUT.CT.TRANSACTION` / `PP.OUT.DD.TRANSACTION` / `PP.OUT.CC.TRANSACTION` `[JAR]` |
| 15 | Transmission to clearing | `PP.CG.InterfaceAPI`, `PP.CG.OutFolderName`; `PP_OutwardInterfaceService.jar` `[JAR]` `[SCHEMA]` |
| 16 | Inward ACK/NACK and status update | `PP_InwardMappingFramework.jar` — `PP_MX_ACK_NACK_PROCESSING`, `PP_SWIFTMX_ACK_NACK_PROCESSING`; `MessageAcceptanceParamHook`; `POR.PAYMENTSTATUSCODE` `[JAR]` |
| 17 | Returns / R-transactions | `PP.CGS.AutomatedReturnIndicator` and the return block on `PP.CLEARING.SETTING`; `PP.CLEARING.RETURNCODE`; `PP.RETURN.MAPPING.PARAM`; `PP_InwardMappingFramework` `PP_DETERMINE_ORIGINAL_TXN_FOR_NCR` `[JAR]` `[SCHEMA]` |
| 18 | Reconciliation / reporting | `PP_ClearingStatusReport.jar`, `PP_CustomerPaymentStatusReport.jar`, `PAYRCN.*` applications `[JAR]` |
