# SEPA / TPH — Inward and Outward Mapping Frameworks

This file resolves the largest "unconfirmed" item in the working brief (§0.35,
*"Field-to-tag mapping logic is unconfirmed … their actual Java implementation …
is not in any artifact reviewed so far"*).

---

## Finding: the mapping frameworks are jBC components, not Java classes

`PP.MSGMAPPINGPARAMETER` `PP.MMP.MappingAPI` values such as
`InwardMappingFramework.mapCreditTransfer` resolve to **compiled jBC component
methods**, shipped as TAFJ-generated classes in the `com.temenos.t24` package:

```
PP_InwardMappingFramework.jar
  com.temenos.t24.InwardMappingFramework_mapCreditTransfer_<n>_cl
PP_OutwardMappingFramework.jar
  com.temenos.t24.OutwardMappingFramework_mapCreditTransfer_<n>_cl
```

`[JAR]`

There is **no** `com.temenos.t24.api.hook.*MappingFramework` class. Searching the
whole 2,053-JAR set for classes named `pacs`, `pain` or `camt` returns zero
results. `[JAR]` The consequence for customisation:

- `MappingAPI` / `DebulkAPI` / `EnrichAPI` values name **component methods**, and a
  custom replacement is a **jBC subroutine**, registered the same way.
- Java hooks exist alongside, for the specific extension points listed in
  [`config-hook-map.md`](config-hook-map.md) — not for message mapping wholesale.
- Message *structure* comes from the registered XSD (`PP.CG.SchemaFolder`) and
  XSLT (`PP.CG.StyleSheetFolder`). The framework has explicit XSLT and validation
  entry points: `OutwardMappingFramework.transformXMLWithXSLT`,
  `.transformXMLWithoutValidation`, `InwardMappingFramework.validateXMLwithXsd`,
  `.interpretXML`, `.interpretNonXML`. `[JAR]`

So the answer to *"is generation driven by Java, by XSD/XSLT, or both?"* is: the
jBC framework orchestrates, XSD validates, XSLT transforms, and configuration
selects which framework method runs. Java hooks intervene at named points only.

---

## Delivered SEPA / STEP2 coverage — check before writing anything

The outward framework ships **clearing-specific implementations by name**,
including for SEPA STEP2: `[JAR]`

| Method | Clearing |
|---|---|
| `OutwardMappingFramework.STEP2determineBulkingCriteria` | SEPA STEP2 |
| `OutwardMappingFramework.criteriaConfigurationForSTEP2` | SEPA STEP2 |
| `OutwardMappingFramework.determineBulkingCriteriaForBACS` / `.getBulkFileRefForBACS` / `.enrichOutMessageAPIForBACS` | UK BACS |
| `OutwardMappingFramework.determineBulkingCriteriaForCOELSA` / `.criteriaConfigurationForCOELSA` | COELSA (AR) |
| `OutwardMappingFramework.determineBulkingCriteriaForNCR` / `.generatePhysicalFileNameForNCR` / `.outwardNCRBulkingAPI` | NCR |
| `OutwardMappingFramework.IPdetermineBulkingCriteria` / `.criteriaConfigurationForIP` / `.enrichOutMessageAPIForIP` / `.generatePhysicalFileNameForIP` | Instant Payments |
| `OutwardMappingFramework.FPSdetermineBulkingCriteria` | UK Faster Payments |
| `InwardMappingFramework.validateEBQAforEPC` | **EPC / SEPA rulebook validation** — the counterpart of `PP.CG.SchemeCompliance = EPC` |
| `InwardMappingFramework.validateEBQAforGenericEBA` | EBA generic |
| `InwardMappingFramework.debulkBACSFile` / `.validateBACSFile` / `.enrichReturnPaymentFromBACS` | UK BACS |

**Default-before-custom rule (brief §0.35):** for a standard SEPA STEP2
`pacs.008` / `pacs.003` / `pacs.002` flow, point the configuration at the
delivered STEP2 methods first. Write a custom API only for a named local gap.

---

## Inward framework — `PP_InwardMappingFramework.jar` (181 methods)

Full list in [`routine-index.md`](routine-index.md); the functional groups:

**File / bulk lifecycle** — `processFile`, `processInward`, `processInwardInstNonESB`,
`executeFileLevel`, `executeBulkLevel`, `executeMessageLevel`, `checkBatch`,
`checkBulkValidation`, `checkBulkReversal`, `splitXMLIntoSmallFiles`,
`resubmitFileBulk`, `writeReceivedBulkDetails`, `setFileAsSuccess`/`setFileAsRepair`,
`setBulkAsSuccess`/`setBulkAsRepair`, `updateFileAsRejected`/`updateBulkAsRejected`,
`updateFileAsResubmitted`/`updateBulkAsResubmitted`.

**Parse (message → internal structure)** — `interpretXML`, `interpretNonXML`,
`validateXMLwithXsd`, `parseMessageByInEntryParam`, plus one `parse*` per message
family: `parseCreditTransfer`, `parseCreditTransferInit`, `parseDirectDebit`,
`parseDirectDebitInit`, `parseDirectDebitReversal`, `parseReturnTransaction`,
`parseReverseCredit`, `parseCancellationRequest`, `parseROI`,
`parseInvesgnRequest`, `parseInformationRequest`, `parseClearingStatusReport`,
`parseISOConfirmations`, `parseRFRD`, `parseLTA` — each with a `…NonXML` variant
where the scheme has a flat-file form.

**Map (internal structure → POR tables)** — `mapCreditTransfer`, `mapDirectDebit`,
`mapDirectDebitRefundReturn`, `mapDirectDebitReversal`, `mapInReturn`,
`mapReverseCredit`, `mapRecallResponse`, `mapROI`, `mapCancellationRequest`,
`mapClearingStatusReport`, `mapISOConfirmations`, `mapChequeCollection`,
`mapIncmgInvestigationRequest`, `mapInvestigationFromClearingToBen`,
`mapSwiftMxdetails`, `mapLocalRef`/`mapLocalRefAPI`.

Per-target-table mappers follow a `map<TxnType>to<PORTable>` convention:
`mapCTtoPORPartyCredit`, `mapCTtoPORPartyDebit`, `mapCTtoPORCoverInfo`,
`mapCTtoInformation`, `mapCTtoPORRemInfStruct`, `mapCTtoRelatedRemittanceinfo`;
the same shape for `DD`, `DDI`, `DDR`, `DDRDRF`, `RT`, `RC`, `RVI`, and
`mapChildTo*` for bulk children. `[JAR]`

**Company / party determination** — `determineCompanyId`,
`determineCompanyIdFromIBAN`, `determineCompanyIdFromISOClearingCode`,
`determineCompanyMnemonic`, `getRunningCompany`. These are the implementation of
the company/BIC precedence rules the brief describes in §0.2 point 6. `[JAR]`

**Agreement / indirect participant** — `determineAgreementCriteria`,
`determineAgreementCriteriaForIP`, `validateBulkAgreementForIP`,
`determineValidationReportForIP` — the implementation behind
`PP.MMP.AgreementValidationCriteriaAPI`. `[JAR]`

**Return / recall matching** — `determineActionType`,
`determineChequeCollectionIdForNCR`, `retrieveOriginalTxnInfoforClaims`,
`insertNewTxnInfoforClaims`, `processInstantRecallReqForReturn`,
`processBulkCustomerCancellation`, `validateCustomerCancellation`.
`PP_DETERMINE_ORIGINAL_TXN_FOR_NCR`, `PP_DETERMINE_ORIGINAL_FILE_FOR_NCR` and
`PP_DETERMINE_CLR_CCY_FOR_NCR` are standalone routines in the same JAR. `[JAR]`

**EBQA (enquiry/answer) workflow** — `createEBQA`, `processEBQA`,
`processEBQAForClaims`, `processEBQAforCustCancellation`, `validateEBQA`,
`validateEBQAFields`, **`validateEBQAforEPC`**, `validateEBQAforGenericEBA`,
`authoriseEBQA`, `authoriseEBQAForClaims`, `charConversionEBQA`,
`ebqaUpdatePmtDet`. `[JAR]`

**ACK/NACK** — the standalone routines `PP_MX_ACK_NACK_PROCESSING` and
`PP_SWIFTMX_ACK_NACK_PROCESSING`. `[JAR]`

---

## Outward framework — `PP_OutwardMappingFramework.jar` (102 methods)

**Pipeline stages, in order** — `processPreBulk` / `selectPreBulk`,
`createPreBulksList`, `insertGroupingCriteria`, `selectGroupingCriteriaAll`,
`getGroupedTxns`, `insertClgGroupedTxns`, `processBulk` / `selectBulk`,
`createFileBulkReferences`, `getBulkFileRef`, `insertClgFileBulkDets`,
`getClgFileBulkDets`, `processTransactionXML` / `selectTransactionXML`,
`transformXMLWithXSLT`, `generatePhysicalFileName`, `insertSentBulkDetails`,
`insertSentFileDetails`, `sendToQueue`, `bulkInterfaceAPI`,
`updatePPforOutwardFileGeneration`, `processFinalise`, `processCleanUp` /
`selectCleanUp`. `[JAR]`

**Settlement** — `createSettlementTransaction`, `insertClgSettlementPending`,
`getClgSettlementPending`, `selectAllSettlementPending`,
`selectAllSettlementPendingForDD`, `processSettlementPendingForDD`,
`processReleaseSettlement`, `processReleaseSettlementForFile`,
`selectReleaseSettlement`, `selectReleaseSettlementForDD`,
`selectReleaseSettlementForFile`, `submitForClearingSettelement`,
`updateClgOutSettlementPending`, `deleteClgPendingTxns`, `insertClgPendingTxns`,
`selectClgPendingTxns`. `[JAR]`

**Message building** — `mapCreditTransfer`, `mapDirectDebit`,
`mapChequeCollection`, `mapCancellationRequest`, `mapUnmatchedCancellation`,
`mapTechnicalHeader`, `generatePacs002`, `generateCCFile`,
`mapOutgoingForNoorReversal`, `mapOutgoingMsgForNOORCase`,
`mapToGenericTableForCT` / `…ForDD` / `…ForCC` / `…ForCancellation`,
`mapIFEventForCT` / `…ForDD` / `…ForCC` / `…ForCancellation` /
`…ForCancellationOriginalReq`, `enrichOutMessageDetails`. `[JAR]`

`generatePacs002` is the only method in either framework whose name contains an
ISO 20022 message identifier. `[JAR]`

**Confirmations / rejects** — `sendClearingConfirmationMsg`,
`emitNegativeConfirmationMsg`, `processConsolidateRejects`,
`selectConsolidateRejects`, `processPendingConsolidateRejects`,
`updateConsolidateRejectConcat`, `processAutoCancelForBatchChild`,
`processPendingAutoCancelPayment`, `selectAllPendingAutoCancelPayment`. `[JAR]`

**Characters** — `doCharConversion`. `[JAR]`

**Outward staging tables** (in the same JAR, as record models):
`PP.OUT.CT.TRANSACTION`, `PP.OUT.DD.TRANSACTION`, `PP.OUT.CC.TRANSACTION`,
`PP.TRANSACTION.TABLES`, `PPT.SENTBULKDETAILS`, `PPT.SENTFILEDETAILS`,
`POR.CLG.OUT.SETTLEMENT.PENDING`, `PP.UPDATE.IN.OUT.SETTLEMENT`. `[JAR]`

The `PP.OUT.DD.TRANSACTION` record class carries multivalue field groups whose
names are ISO 20022 remittance structures verbatim — `RefdocinftpcdorpropcdClass`,
`RefdocamdiscapplamtpcdClass`, `RefdocamtaxamtpcdClass`, `RefdocamadjamrsnamClass`,
`InvridorgidothidClass`, `InveidprvidothidClass` — i.e. the structured-remittance
tree is modelled as MV fields on the outward staging record. Treat every one of
those as multivalue (see the MV-detection rule in
`skills/temenos-dev/SKILL.md`). `[JAR]`

---

## Still unresolved

- **Parameter signatures of the jBC component methods** are not captured. The
  compiled wrappers expose `jVar`-typed positional arguments only; the real
  argument list comes from the component's `.component` declaration, which is not
  in the JAR set here. To write a drop-in replacement for a framework method you
  need either that declaration or a Temenos-supplied skeleton. `[GAP]`
- **Which framework method a given clearing actually uses** is data, not code —
  it is the value stored in `PP.MSGMAPPINGPARAMETER` / `PP.CLEARING` on the target
  environment. Read the live records; they are not in these artifacts. `[GAP]`
