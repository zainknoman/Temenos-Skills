# FS.GI.RECEIPT.CASH.MGMT.FILTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.RECEIPT.CASH.MGMT.FILTER` in `FS_Receipt.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.FILE.REFERENCE` | `FsGiReceiptCashMgmtFilter_FileReference` |  |  |  |
| 2 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.FUND.PROMOTER.ID` | `FsGiReceiptCashMgmtFilter_FundPromoterId` |  |  |  |
| 3 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.COLLECTION.ACCOUNT.GROUP` | `FsGiReceiptCashMgmtFilter_CollectionAccountGroup` |  |  |  |
| 4 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RECEIPT.ACCOUNT.NUMBER` | `FsGiReceiptCashMgmtFilter_ReceiptAccountNumber` |  |  |  |
| 5 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RECEIPT.CURRENCY` | `FsGiReceiptCashMgmtFilter_ReceiptCurrency` |  |  |  |
| 6 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.VALUE.DATE.FROM` | `FsGiReceiptCashMgmtFilter_ValueDateFrom` |  |  |  |
| 7 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.VALUE.DATE.TO` | `FsGiReceiptCashMgmtFilter_ValueDateTo` |  |  |  |
| 8 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.LATEST.FILE.IMPORT.DATE` | `FsGiReceiptCashMgmtFilter_LatestFileImportDate` |  |  |  |
| 9 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.MATCH.DATE.FROM` | `FsGiReceiptCashMgmtFilter_MatchDateFrom` |  |  |  |
| 10 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.MATCH.DATE.TO` | `FsGiReceiptCashMgmtFilter_MatchDateTo` |  |  |  |
| 11 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.PROCESS.ID` | `FsGiReceiptCashMgmtFilter_ProcessId` |  |  |  |
| 12 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RECEIPT.STATUS` | `FsGiReceiptCashMgmtFilter_ReceiptStatus` |  |  |  |
| 13 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.DEAL.TYPE` | `FsGiReceiptCashMgmtFilter_DealType` |  |  |  |
| 14 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED10` | `FsGiReceiptCashMgmtFilter_Reserved10` |  |  |  |
| 15 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED9` | `FsGiReceiptCashMgmtFilter_Reserved9` |  |  |  |
| 16 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED8` | `FsGiReceiptCashMgmtFilter_Reserved8` |  |  |  |
| 17 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED7` | `FsGiReceiptCashMgmtFilter_Reserved7` |  |  |  |
| 18 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED6` | `FsGiReceiptCashMgmtFilter_Reserved6` |  |  |  |
| 19 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED5` | `FsGiReceiptCashMgmtFilter_Reserved5` |  |  |  |
| 20 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED4` | `FsGiReceiptCashMgmtFilter_Reserved4` |  |  |  |
| 21 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED3` | `FsGiReceiptCashMgmtFilter_Reserved3` |  |  |  |
| 22 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED2` | `FsGiReceiptCashMgmtFilter_Reserved2` |  |  |  |
| 23 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RESERVED1` | `FsGiReceiptCashMgmtFilter_Reserved1` |  |  |  |
| 24 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.LOCAL.REF` | `FsGiReceiptCashMgmtFilter_LocalRef` |  |  |  |
| 25 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.OVERRIDE` | `FsGiReceiptCashMgmtFilter_Override` |  |  |  |
| 26 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.RECORD.STATUS` | `FsGiReceiptCashMgmtFilter_RecordStatus` |  |  |  |
| 27 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.CURR.NO` | `FsGiReceiptCashMgmtFilter_CurrNo` |  |  |  |
| 28 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.INPUTTER` | `FsGiReceiptCashMgmtFilter_Inputter` |  |  |  |
| 29 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.DATE.TIME` | `FsGiReceiptCashMgmtFilter_DateTime` |  |  |  |
| 30 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.AUTHORISER` | `FsGiReceiptCashMgmtFilter_Authoriser` |  |  |  |
| 31 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.CO.CODE` | `FsGiReceiptCashMgmtFilter_CoCode` |  |  |  |
| 32 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.DEPT.CODE` | `FsGiReceiptCashMgmtFilter_DeptCode` |  |  |  |
| 33 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.AUDITOR.CODE` | `FsGiReceiptCashMgmtFilter_AuditorCode` |  |  |  |
| 34 | `FS.GI.RECEIPT.CASH.MGMT.FILTER.AUDIT.DATE.TIME` | `FsGiReceiptCashMgmtFilter_AuditDateTime` |  |  |  |
