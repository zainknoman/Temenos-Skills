# ISO 20022 Message Reference — IQ ACH (SEPA-style `pacs` family)

Source: `D:\Prema\Development\RasheedBank\review\Client Doc - IQ ACH.docx`, read in
full (2,390 extracted lines). `[CLIENT]`

---

## Scope warning — read before using anything here for SEPA

This is a **national ACH for Iraq**, not EU SEPA. Its own Overview states the
formats are based on *"ISO 20022 standards, SEPA payment schemes as defined in the
SEPA Credit Transfer (SCT) and SEPA Direct Debit (SDD) Rulebooks (maintained by
European Payment Council (EPC)) … proprietary standards and customizations
following the business requirements of the IPS project."*

Transfers to a SEPA build: message structure, the `pacs` family shape, the status
vocabulary, the build checklist.

Does **not** transfer: currencies (IQD/USD, not EUR), IBAN validation (this scheme
explicitly does not validate — *"Since Iraq does not use IBAN standard yet, ACH
does not use yet international standards to validate the account format and allows
a less strict format"*), decimal places, BIC values, proprietary reason codes
(`IQ01`–`IQ04`), cheque handling (`pacs.005` is not a SEPA message at all).

Participants named: ACH itself is `IACHIQBA`; participants `RAFBIQB1` (Rafidain
Bank), `RDBAIQB1` / `RDBAIQB1223` (Rasheed Bank).

---

## Version ambiguity in the source — resolve before writing an XSD

The document names three different `pacs.002` versions and they disagree:

| Location | Version |
|---|---|
| Overview catalogue table (§1) | `pacs.002.001.002` |
| Section 6 heading | `pacs.002.001.003` |
| `OrgnlMsgNmId` allowed-values table (§6.3.2.2) | `pacs.002.001.003` |
| Namespace in the worked XML examples (§6.4.x) | `urn:iso:std:iso:20022:tech:xsd:pacs.002.001.03` |

Two further inconsistencies in the same document:

- The Overview table gives **Cheque Validation** the XML type
  `FIToFIPmtStsRpt (pacs.003.001.002)`. `pacs.003` is Direct Debit; every other
  status message in the table is `pacs.002`. Almost certainly a typo.
- The Overview table lists the system messages as **System Information Message**
  and **Table Notification Message**. Section 7 actually documents **Calendar
  Information Message**, **Timetable Information Message** and **Participant
  Information Message**. The two lists do not intersect.

**Do not pick one silently.** Get the authoritative version and system-message
list from the ACH operator before registering a schema in `PP.CG.SchemaFolder`.
`[GAP]`

---

## Message catalogue

| Category | Message | XML root (type) | Direction | Inbound file name | Outbound file name |
|---|---|---|---|---|---|
| Credit | Credit Transfer | `FIToFICstmrCdtTrf` (`pacs.008.001.002`) | In / Out | `<BIC8><Ref>.i` | `Credit.SCF.<BIC8><Ref>.xml` |
| Cheque | Cheque | `BlkChq` (`pacs.005.001.02`) | In / Out | `<BIC8><Ref>.zip` | `Cheque.QNF.<BIC8><Ref>.zip` |
| Cheque | VIP Cheque | `BlkChq` (`pacs.005.001.02`) | In / Out | `<BIC8><Ref>.zip` | `VIP Cheque.QNF.<BIC8><Ref>.zip` |
| Cheque | Refusal / Suspension / Acceptance | `FIToFIPmtStsRpt` | In / Out | `<BIC8><Ref>.c` | `Cheque.QNF.<BIC8><Ref>.xml` |
| Debit | Direct Debit | `FIToFICstmrDrctDbt` (`pacs.003.001.002`) | In / Out | `<BIC8><Ref>.i` | `Debit.DNF.<BIC8><Ref>.xml` |
| Debit | Debit Refusal | `FIToFIPmtStsRpt` | In / Out | `<BIC8><Ref>.i` | `Debit.DNF.<BIC8><Ref>.xml` |
| Status | Credit / Cheque / Debit **Validation** | `FIToFIPmtStsRpt` | Out | — | `Credit.CVF.` / `Cheque.QVF.` / `Debit.DVF.<BIC8><Ref>.xml` |
| Status | Credit / Cheque / Debit **Clearing** | `FIToFIPmtStsRpt` | Out | — | `*.RCF.<BIC8><Ref>.xml` |
| Status | Credit / Cheque / Debit **Settlement** | `FIToFIPmtStsRpt` | Out | — | `Credit.CCF.` and `Credit.RSF.` / `Cheque.RSF.` / `Debit.RSF.<BIC8><Ref>.xml` |
| System | System Information | `SystemInformationMessage` | Out only | — | `<BIC8>_SYSTEM_INFORMATION_<Ref>.xml` |
| System | Table Notification | `TableNotificationMessage` | Out only | — | `<BIC8>_TABLE_NOTIFICATION_<Ref>.xml` |

**Hard constraint the brief omits:** *"the total file name length (including
extension) must be less or equal than 24 characters."* Example given:
`RAFBIQB10000012345.i` (20 chars). With an 8-character BIC and a 2-character
extension that leaves **14 characters for `<Ref>`**. This is a real design
constraint on any `PhysicalFileNameAPI` implementation. `[CLIENT]`

### File envelope

- Non-cheque types: the XML message *is* the file; only the extension varies.
- Cheque types: a **zip** containing `<reference>.xml` (the `pacs.005` batch) plus
  two TIFFs per item, named
  `<BlkChq/Chq/CdtrAgt/FinInstnId/BIC>.<BlkChq/Chq/PmtId/TxId>.front.tiff` and
  `….rear.tiff`. Worked example: `cheque00001.xml`,
  `RAFBIQB1778.1_57650356294.front.tiff`, `RAFBIQB1778.1_57650356294.rear.tiff`, …
- A VIP cheque XML may contain only a single payment.

---

## `pacs.008.001.002` Credit Transfer — structure

Root `<FIToFICstmrCdtTrf>` → `<GrpHdr>` [1..1] + `<CdtTrfTxInf>` [1..*].

**Group Header**: `MsgId` [1..1] Max35Text · `CreDtTm` [1..1] ISODateTime ·
`NbOfTxs` [1..1] Max35Text · `TtlIntrBkSttlmAmt` [1..1] Amount ·
`IntrBkSttlmDt` [1..1] ISODate · `SttlmInf/SttlmMtd` [1..1] Code ·
`InstgAgt/FinInstnId/BIC` [0..1] · `InstdAgt/FinInstnId/BIC` [0..1].

**Transaction**: `PmtId/EndToEndId` + `PmtId/TxId` · `PmtTpInf/CtgyPurp/Cd` [0..1] ·
`IntrBkSttlmAmt` · `ChrgBr` · `Dbtr/Nm` (+ optional `PstlAdr/AdrLine`) ·
`DbtrAcct/Id/IBAN` · `DbtrAgt/FinInstnId/BIC` · `CdtrAgt/FinInstnId/BIC` ·
`Cdtr/Nm` (+ optional `PstlAdr/AdrLine`) · `CdtrAcct/Id/IBAN` ·
`RmtInf/Ustrd` [1..1].

### Rules confirmed verbatim

| Element | Rule |
|---|---|
| `SttlmMtd` | **Only `CLRG` is allowed.** |
| `ChrgBr` | **Only `SLEV` is allowed.** |
| `EndToEndId` | *"In case there is no value to generate, use `NOTPROVIDED`."* |
| `IntrBkSttlmDt` | Usually the current date; the ACH also accepts a future settlement date for credits, within a window configurable by the ACH administrator. |
| `InstgAgt` | Mandatory participant→ACH, optional ACH→participant. |
| `InstdAgt` | Optional participant→ACH, mandatory ACH→participant. |
| `InstgAgt`/`InstdAgt` BIC | *"Normally the batch group header should use BIC8 identifiers, for head office."* |
| `CtgyPurp/Cd` | `SALA` (private payroll) and `GOVT` (government payroll) **are charged differently by the ACH**. |

Note the document's `<InstdAgt>` row in the structure table is written as
`<InstgAgt>` (index 1.11 in both `pacs.008` and `pacs.002`); the narrative text
uses `<InstdAgt>`. Another source typo. `[CLIENT]`

---

## `pacs.002` Payment Status Report — the status engine

Root `<FIToFIPmtStsRpt>` → `<GrpHdr>` [1..1] + `<OrgnlGrpInfAndSts>` [1..1] +
`<TxInfAndSts>` [0..*].

Used for two different things, with different `Orgtr` semantics:

1. **Status Update** — ACH → participant, for Accepted / Rejected / Cleared /
   Settled. `Orgtr/…/BICOrBEI` = `IACHIQBA`.
2. **Reply** — participant → ACH (then forwarded): Cheque Refusal, Cheque
   Suspension, Cheque Acceptance, Direct Debit Refusal. `Orgtr/…/BICOrBEI` = the
   reply originator's **branch BIC11**, e.g. `RDBAIQB1223`.

### `GrpSts` — group-level status codes

| Code | Name |
|---|---|
| `ACCP` | AcceptedCustomerProfile |
| `ACSC` | AcceptedSettlementCompleted |
| `CLRD` | Cleared |
| **`PART`** | **PartiallyAccepted** |
| `RJCT` | Rejected |

**`PART` is missing from the working brief's status list (§5.2.3).** It is the
code for the "partially accepted batch" scenario the brief's own testing checklist
requires. `[CLIENT]`

### `TxSts` — transaction-level status codes

| Code | Name | Note |
|---|---|---|
| `ACCP` | AcceptedCustomerProfile | |
| `ACPT` | Accepted | a **suspended cheque** accepted to continue clearing |
| `ACSC` | AcceptedSettlementCompleted | |
| `CLRD` | Cleared | |
| `RJCT` | Rejected | |
| `SPND` | Suspended | cheque item suspended from clearing |

`PART` is group-level only; `ACPT` and `SPND` are transaction-level only.

### `StsRsnInf` presence

| Message | Group level | Transaction level |
|---|---|---|
| ACH status report, rejected payments | **required** | **required** |
| Participant reply messages | *not* required | **required** |

`[CLIENT]`

### Group-level reason codes (`OrgnlGrpInfAndSts/StsRsnInf/Rsn/Cd`)

`AGNT` IncorrectAgent · `AM05` Duplication (duplicate batch) · `B00` Accepted (all
items accepted) · `B01` Partial · `B09` AllRejected · `CURR` IncorrectCurrency ·
`ED05` SettlementFailed · `FF01` InvalidFileFormat.

`FF01` is heavily overloaded — the same code covers BulkTooLarge, BulkBadCount,
BadTotalAmount, BulkBadInstructing, BulkBadInstructed, BulkZeroAmount,
BulkBadSettlementDate and BulkBadOriginalMessageId. Any reject-handling logic must
read `AddtlInf` (Max105Text), not just `Cd`. `[CLIENT]`

### Transaction-level reason codes

`AC01` · `AG01` · `AG02` (three distinct meanings: invalid Local Instrument Code,
invalid Category Purpose Code, invalid Service Level Code) · `AM01` ZeroAmount ·
`AM02` NotAllowedAmount · `AM03` NotAllowedCurrency · `AM04` SettlementFailed
(insufficient funds) · `AM05` Duplication · `CUST` RequestedByCustomer · `DT01`
InvalidDate · `FF01` (invalid `OrgnlMsgNmId` / invalid item format) ·
**`IQ01`–`IQ04`** (proprietary: cheque acceptance/refusal timing, invalid Service
Level Proprietary) · `MD01` NoMandate · `MD03` (four distinct proprietary
meanings) · `MD05` CollectionNotDue · `MS02` · `RC01` BankIdentifierIncorrect
(also used when *the participant is disabled*) · `RR01` (item cannot be mapped to
an existing product) · `SUSP` ItemSuspicios (matches the AML rules) · `UNCO`
Unconfirmed (auto-rejected, not confirmed before cut-off).

`IQ01`–`IQ04` are **scheme-proprietary and will not exist in SEPA.** `[CLIENT]`

### Participant reply reason codes — numeric, not ISO

Cheque Refusal uses codes **1–13** (insufficient funds, not completed properly,
courtesy/legal amount differ, post-dated, stopped, mental capacity, bankruptcy
petition, signature mismatch, uncountersigned correction, stale > 6 months 10 days,
illegible date, certified-cheque error, other).

Direct Debit Refusal uses codes **1, 2, 3, 4, 6, 7, 8, 9, 13, 17, 18, 19** (no
mandate, complete lack of funds, partial lack of funds, incorrect date per mandate,
drawer banned, bankruptcy, missing authorised signature, stopped after due period,
mandate cancelled, name mismatch, account closed, details not recognisable).
Note the gaps — 5, 10, 11, 12, 14, 15, 16 are not defined. `[CLIENT]`

---

## Common item types

| Type | Format |
|---|---|
| `BIC` (`FinInstnId/BIC`, `BICIdentifier`) | `[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}` — 8 or 11 characters |
| `BICOrBEI` (`AnyBICIdentifier`) | same pattern |
| `Amount` (`ActiveCurrencyAndAmount`) | `totalDigits 17`, `fractionDigits 3`, `minInclusive 0`, pattern `[0-9]{0,14}([\.]([0-9]{0,3})){0,1}`; `Ccy` attribute `[A-Z]{3,3}`. **Decimal separator is a dot.** Allowed: **IQD (max 3 decimals), USD (max 2 decimals)**. Batch total must equal the sum of the items. |
| `IBAN` (`IBAN2007Identifier`) | declared as `[a-zA-Z0-9]{1,35}` — **deliberately looser than ISO**, no checksum validation |
| `Nm` / `AdrLine` | Max35Text |
| `AddtlInf` | Max105Text |
| `Ustrd` | Max140Text |
| `CtgyPurp/Cd` (`ExternalCategoryPurpose1Code`) | the full 27-code ISO list: BONU CASH CBLK CCRD CORT DCRD DIVI EPAY FCOL GOVT HEDG ICCP IDCP INTC INTE LOAN OTHR PENS SALA SECU SSBE SUPP TAXS TRAD TREA VATX WHLD |

**For real SEPA these change:** EUR only, 2 decimals, IBAN checksum enforced per
the EPC rulebook, and the category-purpose subset is scheme-restricted.

---

## Cheque (`pacs.005.001.02`) — note the reversed party roles

In the worked cheque example the **`Cdtr` is the sender** and the **`Dbtr` is the
receiver** — the opposite of the credit-transfer convention, because a cheque is a
collection. `PmtTpInf/SvcLvl/Prtry` carries the cheque subtype (`CH` in the
example); an unrecognised value is rejected with `IQ04`
InvalidServiceLevelProprietary. `[CLIENT]`

`pacs.005` has no SEPA equivalent. Nothing in this section transfers.

---

## Worked examples available in the source

Ten, all with full XML: accepted batch · partially accepted batch · rejected batch
(batch error) · rejected batch (item errors) · cleared · settled · cancelled ·
participant cheque refusal · cheque suspension · cheque acceptance · DD refusal.
Use them as the regression corpus required by the brief's §5.2 item 11 — they are
the only authoritative test fixtures in the artifacts. `[CLIENT]`

---

## Mapping these onto TPH

| Spec concept | TPH artefact |
|---|---|
| Message type registration | `PP.CG.ClearingTransactionType` ↔ `PP.CG.IncomingMessageType` / `PP.CG.OutgoingMessageType` `[SCHEMA]` |
| XSD location | `PP.CG.SchemaFolder`; XSLT `PP.CG.StyleSheetFolder` `[SCHEMA]` |
| File name convention (≤ 24 chars) | `PP.CG.PhysicalFileNameAPI` → `PP.CLEARING.PhyFileNameAPI.HOOK`; delivered examples `OutwardMappingFramework.generatePhysicalFileName*` `[JAR]` |
| Batch/bulk limits | `PP.CG.MaxTransPerBulk`, `PP.CG.MaxBulksPerFile`, `PP.CG.MaxFilesPerCycle` `[SCHEMA]` |
| Bulking rule | `PP.CG.BulkingCriteriaAPI` → `PaymentLifecycle.getGroupingCriteria()` `[SCHEMA]` `[JAR]` |
| Inbound parse + map | `PP.MMP.DebulkAPI` / `PP.MMP.MappingAPI` → `InwardMappingFramework.parse*` / `.map*` `[JAR]` |
| Status report generation | `OutwardMappingFramework.generatePacs002` `[JAR]` |
| Return / refusal window | `PP.CGS.AcceptanceDays`, `PP.CGS.AuthRefundAllowedDays`, `PP.CGS.UnAuthRefundAllowedDays`, `PP.CGS.AutomatedReturnIndicator` `[SCHEMA]` |
| Reason-code registry | `PP.CLEARING.RETURNCODE`, `PI.ERROR.REASON.CODE`, `PI.ISO.EXTERNAL.CODE` `[SCHEMA]` |
| Category purpose | `PAYMENT.CATEG.PURPOSE`, `PAYMENT.PURPOSE.CODE`; EP module: `SEPA.CATEG.PURPOSE` `[SCHEMA]` |
| Character set | `PP.CG.AllowUTF8Characters` → `PP.BANK.CONDITIONS` → `PP.COMPANY.PROPERTIES`; `PP.CHAR.CONVERSION` `[SCHEMA]` |
| Cheque zip envelope | **No TPH artefact found.** Image packing/unpacking is not represented in any class, routine or configuration field in this JAR set. `[GAP]` |
