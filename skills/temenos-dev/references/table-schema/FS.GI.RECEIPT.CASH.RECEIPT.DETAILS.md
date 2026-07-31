# FS.GI.RECEIPT.CASH.RECEIPT.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.RECEIPT.CASH.RECEIPT.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.FILE.REFERENCE` | `FsGiReceiptCashReceiptDetails_FileReference` |  |  |  |
| 2 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.TYPE` | `FsGiReceiptCashReceiptDetails_ReceiptType` |  |  |  |
| 3 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.ID` | `FsGiReceiptCashReceiptDetails_ReceiptId` |  |  |  |
| 4 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.ACCOUNT.NUMBER` | `FsGiReceiptCashReceiptDetails_ReceiptAccountNumber` |  |  |  |
| 5 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.COLLECTION.ACCOUNT.GROUP` | `FsGiReceiptCashReceiptDetails_CollectionAccountGroup` |  |  |  |
| 6 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.VALUE.DATE` | `FsGiReceiptCashReceiptDetails_ReceiptValueDate` |  |  |  |
| 7 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.AMOUNT` | `FsGiReceiptCashReceiptDetails_Amount` |  |  |  |
| 8 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.CURRENCY` | `FsGiReceiptCashReceiptDetails_ReceiptCurrency` |  |  |  |
| 9 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.REMITTER.ID` | `FsGiReceiptCashReceiptDetails_RemitterId` |  |  |  |
| 10 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.REMITTER.TYPE` | `FsGiReceiptCashReceiptDetails_RemitterType` |  |  |  |
| 11 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.REMITTER.NAME` | `FsGiReceiptCashReceiptDetails_RemitterName` |  |  |  |
| 12 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.REMITTER.BANK.ACCOUNT` | `FsGiReceiptCashReceiptDetails_RemitterBankAccount` |  |  |  |
| 13 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.REMITTER.ROUTING.CODE` | `FsGiReceiptCashReceiptDetails_RemitterRoutingCode` |  |  |  |
| 14 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.BANK.REFERENCE` | `FsGiReceiptCashReceiptDetails_ReceiptBankReference` |  |  |  |
| 15 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.NARRATIVE` | `FsGiReceiptCashReceiptDetails_ReceiptNarrative` |  |  |  |
| 16 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.COUNTRY.OF.ORIGIN` | `FsGiReceiptCashReceiptDetails_CountryOfOrigin` |  |  |  |
| 17 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.CUSTOMER.REFERENCE` | `FsGiReceiptCashReceiptDetails_CustomerReference` |  |  |  |
| 18 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.SOURCE.SYSTEM` | `FsGiReceiptCashReceiptDetails_ReceiptSourceSystem` |  |  |  |
| 19 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.IMPORT.CONFIRMATION.INDICATOR` | `FsGiReceiptCashReceiptDetails_ImportConfirmationIndicator` |  |  |  |
| 20 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.TIME.STAMP` | `FsGiReceiptCashReceiptDetails_ReceiptTimeStamp` |  |  |  |
| 21 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.AGEING` | `FsGiReceiptCashReceiptDetails_Ageing` |  |  |  |
| 22 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECEIPT.STATUS` | `FsGiReceiptCashReceiptDetails_ReceiptStatus` |  |  |  |
| 23 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.SOF.STATUS` | `FsGiReceiptCashReceiptDetails_SofStatus` |  |  |  |
| 24 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MEMO` | `FsGiReceiptCashReceiptDetails_Memo` |  |  |  |
| 25 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.EXEMPT.REASON.CODE` | `FsGiReceiptCashReceiptDetails_ExemptReasonCode` |  |  |  |
| 26 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GROUP.ID` | `FsGiReceiptCashReceiptDetails_MatchGroupId` |  |  |  |
| 27 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.PREVIOUS.MATCH.ID` | `FsGiReceiptCashReceiptDetails_PreviousMatchId` |  |  |  |
| 28 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.CHILD.RECEIPT.MATCH.GROUP.ID` | `FsGiReceiptCashReceiptDetails_ChildReceiptMatchGroupId` |  |  |  |
| 29 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.CHILD.RECEIPT.DEAL.REFERENCE` | `FsGiReceiptCashReceiptDetails_ChildReceiptDealReference` |  |  |  |
| 30 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.FUND.PROMOTER.ID` | `FsGiReceiptCashReceiptDetails_FundPromoterId` |  |  |  |
| 31 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.UNIQUE.PAYMENT.REFERENCE` | `FsGiReceiptCashReceiptDetails_UniquePaymentReference` |  |  |  |
| 32 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.EXTERNAL.PAYMENT.REFERENCE` | `FsGiReceiptCashReceiptDetails_ExternalPaymentReference` |  |  |  |
| 33 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.GROUP.CODE` | `FsGiReceiptCashReceiptDetails_GroupCode` |  |  |  |
| 34 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GROUP.STATUS` | `FsGiReceiptCashReceiptDetails_MatchGroupStatus` |  |  |  |
| 35 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.DATE.OF.MATCHING` | `FsGiReceiptCashReceiptDetails_DateOfMatching` |  |  |  |
| 36 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCHING.METHOD` | `FsGiReceiptCashReceiptDetails_MatchingMethod` |  |  |  |
| 37 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GROUP.MAKER` | `FsGiReceiptCashReceiptDetails_MatchGroupMaker` |  |  |  |
| 38 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GROUP.CHECKER` | `FsGiReceiptCashReceiptDetails_MatchGroupChecker` |  |  |  |
| 39 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.REMITTER.CHECK.STATUS` | `FsGiReceiptCashReceiptDetails_RemitterCheckStatus` |  |  |  |
| 40 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GROUP.SETTLEMENT.METHOD` | `FsGiReceiptCashReceiptDetails_MatchGroupSettlementMethod` |  |  |  |
| 41 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.SETTLEMENT.DATE` | `FsGiReceiptCashReceiptDetails_SettlementDate` |  |  |  |
| 42 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.FORCED.TRADE.DATE` | `FsGiReceiptCashReceiptDetails_ForcedTradeDate` |  |  |  |
| 43 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.TOLERANCE.AMOUNT` | `FsGiReceiptCashReceiptDetails_ToleranceAmount` |  |  |  |
| 44 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GROUP.MAKER.DATE` | `FsGiReceiptCashReceiptDetails_MatchGroupMakerDate` |  |  |  |
| 45 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GROUP.CHECKER.DATE` | `FsGiReceiptCashReceiptDetails_MatchGroupCheckerDate` |  |  |  |
| 46 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GRP.APPROVAL.CHECKER1` | `FsGiReceiptCashReceiptDetails_MatchGrpApprovalChecker1` |  |  |  |
| 47 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MATCH.GRP.APPROV.CHECKER1.DATE` | `FsGiReceiptCashReceiptDetails_MatchGrpApprovChecker1Date` |  |  |  |
| 48 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.FUND.ID` | `FsGiReceiptCashReceiptDetails_FundId` |  |  |  |
| 49 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.PREVIOUS.RECEIPT.STATUS` | `FsGiReceiptCashReceiptDetails_PreviousReceiptStatus` |  |  |  |
| 50 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.AMOUNT.APPLICATION.CURRENCY` | `FsGiReceiptCashReceiptDetails_AmountApplicationCurrency` |  |  |  |
| 51 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.APPLICATION.CURRENCY` | `FsGiReceiptCashReceiptDetails_ApplicationCurrency` |  |  |  |
| 52 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.NOTIONAL.FX` | `FsGiReceiptCashReceiptDetails_NotionalFx` |  |  |  |
| 53 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.FINAL.PAYMENT.ID` | `FsGiReceiptCashReceiptDetails_FinalPaymentId` |  |  |  |
| 54 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.PAYMENT.FILE.ID` | `FsGiReceiptCashReceiptDetails_PaymentFileId` |  |  |  |
| 55 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.MIGRATED.FLAG` | `FsGiReceiptCashReceiptDetails_MigratedFlag` |  |  |  |
| 56 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED10` | `FsGiReceiptCashReceiptDetails_Reserved10` |  |  |  |
| 57 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED9` | `FsGiReceiptCashReceiptDetails_Reserved9` |  |  |  |
| 58 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED8` | `FsGiReceiptCashReceiptDetails_Reserved8` |  |  |  |
| 59 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED7` | `FsGiReceiptCashReceiptDetails_Reserved7` |  |  |  |
| 60 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED6` | `FsGiReceiptCashReceiptDetails_Reserved6` |  |  |  |
| 61 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED5` | `FsGiReceiptCashReceiptDetails_Reserved5` |  |  |  |
| 62 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED4` | `FsGiReceiptCashReceiptDetails_Reserved4` |  |  |  |
| 63 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED3` | `FsGiReceiptCashReceiptDetails_Reserved3` |  |  |  |
| 64 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED2` | `FsGiReceiptCashReceiptDetails_Reserved2` |  |  |  |
| 65 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RESERVED1` | `FsGiReceiptCashReceiptDetails_Reserved1` |  |  |  |
| 66 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.LOCAL.REF` | `FsGiReceiptCashReceiptDetails_LocalRef` |  |  |  |
| 67 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.OVERRIDE` | `FsGiReceiptCashReceiptDetails_Override` |  |  |  |
| 68 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.RECORD.STATUS` | `FsGiReceiptCashReceiptDetails_RecordStatus` |  |  |  |
| 69 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.CURR.NO` | `FsGiReceiptCashReceiptDetails_CurrNo` |  |  |  |
| 70 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.INPUTTER` | `FsGiReceiptCashReceiptDetails_Inputter` |  |  |  |
| 71 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.DATE.TIME` | `FsGiReceiptCashReceiptDetails_DateTime` |  |  |  |
| 72 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.AUTHORISER` | `FsGiReceiptCashReceiptDetails_Authoriser` |  |  |  |
| 73 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.CO.CODE` | `FsGiReceiptCashReceiptDetails_CoCode` |  |  |  |
| 74 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.DEPT.CODE` | `FsGiReceiptCashReceiptDetails_DeptCode` |  |  |  |
| 75 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.AUDITOR.CODE` | `FsGiReceiptCashReceiptDetails_AuditorCode` |  |  |  |
| 76 | `GI.RECEIPT.CASH.RECEIPT.DETAILS.AUDIT.DATE.TIME` | `FsGiReceiptCashReceiptDetails_AuditDateTime` |  |  |  |
