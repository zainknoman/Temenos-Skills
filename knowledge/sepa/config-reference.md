# SEPA / TPH — Configuration Reference

Field names here are exact, from `INSERTS/I_F.<APP>` inside the JARs `[SCHEMA]`.
Full field lists: `skills/temenos-dev/references/table-schema/<APP>.md`.
Verify mechanically before use:

```
python pipeline/validate_fields.py --app PP.CLEARING --fields "PP.CG.SchemeCompliance,PP.CG.ClearingType"
```

---

## Corrections to the working brief

The Phase 0 §0.2 summary in the agent brief attributes several fields to the wrong
application. The real placement, verified against `INSERTS/I_F.*`:

| Field the brief places on `PP.CLEARING.SETTING` | Actually on | Real field name |
|---|---|---|
| Out Message Format API | `PP.CLEARING` | `PP.CG.OutMessageFormatAPI` (pos 14) |
| Out Msg Generation API | `PP.CLEARING` | `PP.CG.OutboundMsgGenerationAPI` (pos 21) |
| Bulking Criteria API | `PP.CLEARING` | `PP.CG.BulkingCriteriaAPI` (pos 12) |
| Bulking API | `PP.CLEARING` | `PP.CG.BulkingAPI` (pos 53) |
| Bulking Mode (ESB/NonESB) | `PP.CLEARING` | `PP.CG.BulkingMode` (pos 48) |
| Schema Folder | `PP.CLEARING` | `PP.CG.SchemaFolder` (pos 50) |
| StyleSheet Folder | `PP.CLEARING` | `PP.CG.StyleSheetFolder` (pos 51) |
| OutFolderName | `PP.CLEARING` | `PP.CG.OutFolderName` (pos 49) |
| BulkFileRefAPI | `PP.CLEARING` | `PP.CG.BulkFileRefAPI` (pos 17) |
| PhysicalFileNameAPI | `PP.CLEARING` | `PP.CG.PhysicalFileNameAPI` (pos 18) |
| MandateValidationAPI | `PP.CLEARING` | `PP.CG.MandateValidationAPI` (pos 19) |
| EnrichOutMessageAPI | `PP.CLEARING` | `PP.CG.EnrichOutMessageAPI` (pos 57) |
| CriteriaConfigurationAPI | `PP.CLEARING` | `PP.CG.CriteriaConfigurationAPI` (pos 76) |
| Allow Partial Return | `PP.CLEARING` | `PP.CG.AllowPartialReturn` (pos 101) |
| Allowed ROI Response | `PP.CLEARING` | `PP.CG.AllowedROIResponse` (pos 100) |

**Practical consequence:** these are *clearing-level*, not per-message-type. You
cannot vary the schema folder, bulking criteria or outward format API per
currency/nature-code/direction by editing `PP.CLEARING.SETTING` — those knobs are
one-per-clearing. `PP.CLEARING.SETTING` carries account, settlement, return,
mandate and validation behaviour only.

Two more corrections:

- The brief lists `Max Inst Time Out` and `Mandate Verification Indicator` on
  `PP.CLEARING.SETTING` — correct: `PP.CGS.MaxInstTimeOut` (39),
  `PP.CGS.MandateVerificationIndicator` (34). But it also lists a
  `Manual Verification Indicator` separately; the real record has both
  `PP.CGS.ManualVerificationIndicator` (15) **and**
  `PP.CGS.MandateVerificationIndicator` (34) — different fields, easy to confuse.
- `PP.CLEARING.SETTING` has **no** `Allow Partial Return` or `Allowed ROI Response`
  field. Its cancellation-response controls are
  `PP.CGS.AutoNegativeCancelReqResponse` (40),
  `PP.CGS.AcceptanceDaysCustInitCanclReq` (46) and
  `PP.CGS.CancellationOverdueDays` (47).

---

## `PP.CLEARING` — 101 fields

One record per clearing scheme. Key fields with confirmed valid values:

### Identity and type

| Pos | Field | Values / meaning |
|-----|-------|------------------|
| 1 | `PP.CG.CompanyID` | FTD company; NoInput, auto-populated on validation |
| 2 | `PP.CG.ClearingCurrency` | |
| 3 | `PP.CG.ClearingCountryCode` | **Mandatory.** 2 alphanumeric; links to `COUNTRY.COUNTRY.CODE` |
| 4 | `PP.CG.ClearingName` | 128 alphanumeric |
| 5 | `PP.CG.ClearingFileTransactionInd` | `F` = file based, `T` = transaction based |
| 6 | `PP.CG.RTGSSystem` | `Y` = RTGS (needs RTGS framework licence), `N`/blank = not RTGS (needs ACH framework licence), `I` = channel supports Instant Payments send/receive |
| 97 | `PP.CG.ClearingType` | |
| 54 | `PP.CG.SettlementType` | |
| 7 | `PP.CG.SendingBIC` | 35 alphanumeric; links to `PPT.BICTABLE.BICCode` |
| 15 | `PP.CG.ClearingBIC` | Receiving-institution code used in the file header; links to `PPT.BICTABLE.BICCode` |
| 45 | `PP.CG.ClearingNCC` / 47 `PP.CG.SendingNcc` | National clearing codes |
| 55 | `PP.CG.ClearingSystemIdCode` | |
| 25 | `PP.CG.ParticipantType` | blank = clearing house, `DP` = direct participant, `IP` = indirect participant. *PH module only.* |

### SEPA / EPC compliance

| Pos | Field | Values |
|-----|-------|--------|
| 98 | `PP.CG.SchemeCompliance` | `EPC` or blank. **This is the SEPA switch.** Verbatim: *"If it is defined as 'EPC' then while validating a system generated CR or ROI or CA message for a SEPA or SEPA instant payment, EPC message format validations and Clearing Specific format validations (if routine is present) are applicable."* Applies to system-generated **C**ancellation **R**equest, **R**esolution **O**f **I**nvestigation and **C**laim messages in EBQA. Blank (default) = non-EPC-compliant. |

Note the scope: as documented, `SchemeCompliance` governs the CR/ROI/CA
(camt.056 / camt.029 / camt.027) validation path — *not* pacs.008 field
validation, which comes from the schema and `ValidateAPI`. The description adds
"In future, this field can be used for scheme specific processing/validation at
various stages of the payment life cycle." `[SCHEMA]`

### File generation and bulking

| Pos | Field | Values |
|-----|-------|--------|
| 13 | `PP.CG.FileGenerationRequired` | `Y` = system generates the clearing file. `N` = not supported (settlement only). blank = generate a null file to the clearing. `NR` = not supported and move status to **999** (settlement only). |
| 9 | `PP.CG.MaxTransPerBulk` | 7 numeric, default 999 |
| 10 | `PP.CG.MaxBulksPerFile` | 4 numeric, default 1 |
| 11 | `PP.CG.MaxFilesPerCycle` | 4 numeric, default 1 |
| 12 | `PP.CG.BulkingCriteriaAPI` | → `PaymentLifecycle.getGroupingCriteria()` |
| 53 | `PP.CG.BulkingAPI` | |
| 48 | `PP.CG.BulkingMode` | ESB / NonESB |
| 17 | `PP.CG.BulkFileRefAPI` | → `PaymentLifecycle.getBulkPaymentReference()` |
| 18 | `PP.CG.PhysicalFileNameAPI` | → `PP.CLEARING.PhyFileNameAPI.HOOK` |
| 76 | `PP.CG.CriteriaConfigurationAPI` | → `PaymentLifecycle.getCustomGroupingValues()` |

Both status values are correct and apply to different settings, confirmed by the
vendor guide: `N` → *"Temenos Payments Hub does not create the clearing file but
parks the payment in **990** status. The external system can update the payment
status to Temenos Payments Hub through OFS message or Provider API exposed by
Temenos Payments Hub."*
`[PDF TPH-Clearing/TPH Configuring Clearing.pdf p.2]`; `NR` → status **999**
`[SCHEMA]`.

### Message format, schema and transport

| Pos | Field | Notes |
|-----|-------|-------|
| 14 | `PP.CG.OutMessageFormatAPI` | Determines the outgoing message type (format) |
| 21 | `PP.CG.OutboundMsgGenerationAPI` | Overrides the configured outgoing message type |
| 46 | `PP.CG.OutMsgEmitFormat` | |
| 50 | `PP.CG.SchemaFolder` / 51 `PP.CG.StyleSheetFolder` | XSD and XSLT locations |
| 33 | `PP.CG.XsltVersionNumber` | |
| 49 | `PP.CG.OutFolderName` | |
| 75 | `PP.CG.ErrorFolder` | |
| 52 | `PP.CG.OutValidateAPI` / 62 `PP.CG.FileOutValidateAPI` | Pre-send validation |
| 57 | `PP.CG.EnrichOutMessageAPI` | → `PaymentLifecycle.updateOutgoingPaymentRecords()` |
| 63 | `PP.CG.InterfaceAPI` | |
| 96 | `PP.CG.MessageInterface` | **The DE-vs-direct branch point flagged in the brief §0.35.** Check this value on the target clearing before deciding where custom outward-message code goes. |
| 44 | `PP.CG.SwiftBased` | |
| 30–32 | `PP.CG.ClearingTransactionType` / `PP.CG.OutgoingMessageType` / `PP.CG.IncomingMessageType` | The txn-type ↔ message-type registration triple |

### Instant payments

| Pos | Field | Values |
|-----|-------|--------|
| 23 | `PP.CG.TimeZone` | *"EBA INST requires all payment initiations to the Clearing House to be time stamped with UTC time zone as the base."* |
| 26 | `PP.CG.PostingMethod` | `DebitNow` = reserve, book, send; on confirmation complete or reverse. `DebitOnPayConfirmation` = reserve and send; on confirmation book or cancel reservation. |
| 27 | `PP.CG.InstPayRejectBooking` | `Reverse` = mark rejected, reverse debit/credit, no new charge. `ReverseAndCharge` = mark rejected, create a new reversing transaction, apply its configured charges. Charges on the original stay. |
| 24 | `PP.CG.InvestigationTimeOut` | Seconds. If `now >= InstAcceptDateTime + InvestigationTimeOut`, the system auto-sends the message type in `PP.CG.ClearingInvestigationMsgType`. Empty = no automated investigation. *PH module only.* |
| 42 | `PP.CG.ClearingInvestigationMsgType` | |
| 39/40 | `PP.CG.InvestigationRetryTime` / `...RetryCount` | |
| 41 | `PP.CG.InstAllowPendingConfirmation` | |
| 43 | `PP.CG.AckTypeForBeneBank` / 95 `PP.CG.AckTypeForDebtorBank` | |
| 29 | `PP.CG.24By7Channel` | |
| 77/78 | `PP.CG.InstOriginationCancelTimeOut` / `PP.CG.NRInstOriginationCancelTimeOut` | |
| 87 | `PP.CG.NRInstOriginationTimeOutAction` | |
| 90–94 | `PP.CG.TimeOutTransactionType`, `PP.CG.InstantOrNRInstant`, `PP.CG.TimeOutActionRetryTime`, `...RetryCount`, `...MessageType` | |

### Screening, reachability, characters

| Pos | Field | Values |
|-----|-------|--------|
| 28 | `PP.CG.ScreeningResponseAction` | On a *Possible Hit* from the filtering engine: `SendPendingConfirmation` (sends the message type in `PP.CLEARINGSETTING.ClearingStatusMessageType`), `Reject` (negative confirmation to clearing), blank (no action). |
| 22 | `PP.CG.SkipReachability` | `Y` = skip, `N`/blank = check against `PP.CLEARING.DIRECTORY` |
| 8 | `PP.CG.RMACheck` | `Y`/`N` |
| 16 | `PP.CG.AllowUTF8Characters` | `Y` = validate per `PP.BANK.CONDITIONS.Allowspecialcharacterset` (which, if `Y`, uses the configured code-page set; if `N`, uses the `STANDARD.SW` record; if blank, falls back to `PP.COMPANY.PROPERTIES.Allowspecialcharacterset`). `N` = validate against `STANDARD.SW`. blank = no validation, character retained as-is. Valid values come from `ASCII.VAL.TABLE`. |

### Returns / recall

| Pos | Field |
|-----|-------|
| 89 | `PP.CG.RecallPossibleMsgs` |
| 100 | `PP.CG.AllowedROIResponse` |
| 101 | `PP.CG.AllowPartialReturn` |
| 58/59 | `PP.CG.PostingMethodforReturnsSent` / `...Recvd` |
| 99 | `PP.CG.DDPostingMethod` |
| 80 | `PP.CG.SWIFTReturnCodeWord` |

---

## `PP.CLEARING.SETTING` — 67 fields

Key: clearing + currency + nature code + message payment type + direction.

| Pos | Field | Confirmed values |
|-----|-------|------------------|
| 2 | `PP.CGS.ClearingID` | |
| 3 | `PP.CGS.ClearingCurrency` | |
| 4 | `PP.CGS.ClearingNatureCode` | **Mandatory.** Links to `PPT.CLEARINGNATURECODE.ClearingNatureCode` |
| 5 | `PP.CGS.MessageDirection` | `R` = Received, `S` = Sent |
| 6 | `PP.CGS.MessagePaymentType` | **Mandatory.** Links to `PPT.MSGPAYMENTTYPE.MessagePaymentType` |
| 8–13 | `PP.CGS.ClearingAccount{Company,Number,Currency}`, `PP.CGS.SuspenseAccount{Company,Number,Currency}` | |
| 14 | `PP.CGS.SettlementBookingIndicator` | `Y` = clearing-file total is pre-settled; create the settlement transaction at de-bulking time (an extra transaction on top of the individual payments). `N` = not pre-settled, or pre-settled but the bank creates the settlement transaction later for successful payments only. **The description also references `IF`** (file-level) — the truncated text confirms more than the Y/N pair; read the full description in the schema file before choosing. Example given: UK BACS Direct Debit → `N`. |
| 15 | `PP.CGS.ManualVerificationIndicator` | |
| 16 | `PP.CGS.SettlementShift` | |
| 17 | `PP.CGS.ScheduledForReleaseIndicator` | |
| 19–21 | `PP.CGS.ValidationRequired`, `PP.CGS.Ranking`, `PP.CGS.ValidateAPI` | Ranked pre-send validation |
| 22 | `PP.CGS.AutomatedReturnIndicator` | `Y` = return automatically. `N` = park in repair queue for manual return. **NOINPUT unless the SEPA products `PPSPDD`/`PPSPCT` are installed on PP, and unless PH is installed on PP.** *PH module only.* |
| 23/24 | `PP.CGS.CreateReturnBookingIndicator`, `PP.CGS.CreateReturnMessageIndicator` | |
| 25–27 | `PP.CGS.ReturnSuspenseAccount{Company,Number,Currency}` | |
| 28 | `PP.CGS.CreateRejectMessageIndicator` | |
| 29 | `PP.CGS.AcceptanceDays` | Window for accepting an inward cancellation request / sending an outward one, and for initiating a return on incoming payments. `N` = TPH-initiated recall not allowed. Suffix `C` = calendar days (`30C`), `W` = processing-company working days per `HOLIDAY`, `CW` = clearing working days per `PP.CLEARING.NONWORKINGDAY` (max 99). |
| 30 | `PP.CGS.ClearingTransactionType` | |
| 31/32 | `PP.CGS.AuthRefundAllowedDays`, `PP.CGS.UnAuthRefundAllowedDays` | |
| 33 | `PP.CGS.ImposeReturnValueDate` | `Y` = the return uses the original value date (DD return: original debtor credited with the original debit value date; CT return: original creditor debited with the original credit value date). `N` / blank. *PH module only.* |
| 34–38 | `PP.CGS.MandateVerificationIndicator`, `PP.CGS.AutoRegisterMandateIndicator`, `PP.CGS.MandateAmendmentIndicator`, `PP.CGS.MandateLimitCheckIndicator`, `PP.CGS.CrdRestrictionCheckIndicator` | |
| 39 | `PP.CGS.MaxInstTimeOut` | |
| 40 | `PP.CGS.AutoNegativeCancelReqResponse` | `Y` = auto-process a negative response to an incoming cancellation request (original not found, or request beyond allowed days). `N`/blank |
| 41 | `PP.CGS.OriginalTrnLookUpCriteriaAPI` | API used to retrieve the original transaction for an incoming message. 50 numeric characters. |
| 45 | `PP.CGS.ChequesAutoClear` | |
| 46/47 | `PP.CGS.AcceptanceDaysCustInitCanclReq`, `PP.CGS.CancellationOverdueDays` | |

`PPSPDD` / `PPSPCT` are the SEPA Direct Debit and SEPA Credit Transfer product
licences on PP — their presence is what enables the automated-return behaviour.
`[SCHEMA]`

`PPRTGF` (RTGS framework) and `PPACHF` (ACH framework) are also real, confirmed
by the vendor guide as prerequisites for `Clearing Type = Y` and `= N`/blank
respectively. They appear in the PDF, not in any field description.
`[PDF TPH-Clearing/TPH Configuring Clearing.pdf p.4, p.6]`

---

## `PP.MSGMAPPINGPARAMETER` — 23 fields

Inbound mapping. Complete non-audit field list:

| Pos | Field | Notes |
|-----|-------|-------|
| 1 | `PP.MMP.DebulkAPI` | |
| 2 | `PP.MMP.MappingAPI` | e.g. `InwardMappingFramework.mapCreditTransfer` — **a compiled jBC component method, not a Java class.** See [`mapping-frameworks.md`](mapping-frameworks.md). |
| 3 | `PP.MMP.SourceTypeAPI` | → `PaymentLifecycle.getSource()` |
| 4 | `PP.MMP.ClearingTransactionType` | |
| 5 | `PP.MMP.ClearingNatureCode` | |
| 6 | `PP.MMP.EnrichAPI` | → `Message.updateInformationLine()` |
| 7 | `PP.MMP.BulkDuplicateCheckID` | |
| 8 | `PP.MMP.AgreementValidationCriteriaAPI` | |
| 20 | `PP.MMP.InstantLocalInstrumentCode` | |
| 21 | `PP.MMP.InstantPaymentMethod` | |
| 22 | `PP.MMP.OriginalPmtIDAPI` | |
| 23 | `PP.MMP.SkipFileBulkUpdate` | |

---

## `PP.CLEARING.COMPANY` — 19 fields

| Pos | Field |
|-----|-------|
| 1–3 | `PP.CCM.CompanyID`, `PP.CCM.ClearingName`, `PP.CCM.ClearingID` |
| 4–6 | `PP.CCM.ClearingAccount{Company,Currency,Number}` |
| 7 | `PP.CCM.AlternateIdentifier` |
| 19 | `PP.CCM.ClearingTransactionType` |

---

## `PP.COMPONENT.API.HOOK` — the jBC hook registry

Two functional fields only: `[SCHEMA]`

| Pos | Field |
|-----|-------|
| 1 | `PP.CAH.HookAPIName` |
| 2 | `PP.CAH.InvokeCall` |

A record here binds a named component hook (e.g. `CreditPartyDetermination`) to a
routine. A real production example is analysed in
[`routines/component-api-hooks.md`](routines/component-api-hooks.md). `[CLIENT]`

---

## Related applications present in this JAR set

`PP.MSG.ACCEPTANCE.PARAM`, `PP.RETURN.MAPPING.PARAM`, `PP.CLEARING.DIRECTORY`,
`PP.CLEARING.NATURE.CODE`, `PP.CLEARING.RETURNCODE`, `PP.CLEARING.FREQUENCY`,
`PP.CLEARING.NONWORKINGDAY`, `PP.CLEARING.STATUS.REPORT`, `PP.CHAR.CONVERSION`,
`PP.COMPANY.PROPERTIES`, `PP.BANK.CONDITIONS`, `PP.BIC.TABLE`,
`PP.COUNTRYIBANSTRUCTURE`, `PP.PROCESSING.SEQUENCE`, `PP.STATUS.ACTION`,
`PP.FEETYPE`, `PP.CHANNEL`, `PP.CHANNEL.CUTOFF`, `PP.CURRENCY.NONWORKINGDAY`.
Full list with field counts in [`applications.md`](applications.md). `[SCHEMA]`
