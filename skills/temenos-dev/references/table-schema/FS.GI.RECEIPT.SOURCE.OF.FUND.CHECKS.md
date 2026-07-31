# FS.GI.RECEIPT.SOURCE.OF.FUND.CHECKS — Table Schema

> Source: `INSERTS/I_F.FS.GI.RECEIPT.SOURCE.OF.FUND.CHECKS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.REC.SOURCE.FUND.CHECKS.FUND.PROMOTER.ID` | `FsGiReceiptSourceOfFundChecks_FundPromoterId` |  |  |  |
| 2 | `GI.REC.SOURCE.FUND.CHECKS.COLLECTION.ACCOUNT.GROUP` | `FsGiReceiptSourceOfFundChecks_CollectionAccountGroup` |  |  |  |
| 3 | `GI.REC.SOURCE.FUND.CHECKS.AML.JURISDICTION` | `FsGiReceiptSourceOfFundChecks_AmlJurisdiction` |  |  |  |
| 4 | `GI.REC.SOURCE.FUND.CHECKS.AML.RISK.GROUP` | `FsGiReceiptSourceOfFundChecks_AmlRiskGroup` |  |  |  |
| 5 | `GI.REC.SOURCE.FUND.CHECKS.APPROVAL.METHOD` | `FsGiReceiptSourceOfFundChecks_ApprovalMethod` |  |  |  |
| 6 | `GI.REC.SOURCE.FUND.CHECKS.PENDING.FLAG` | `FsGiReceiptSourceOfFundChecks_PendingFlag` |  |  |  |
| 7 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED10` | `FsGiReceiptSourceOfFundChecks_Reserved10` |  |  |  |
| 8 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED9` | `FsGiReceiptSourceOfFundChecks_Reserved9` |  |  |  |
| 9 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED8` | `FsGiReceiptSourceOfFundChecks_Reserved8` |  |  |  |
| 10 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED7` | `FsGiReceiptSourceOfFundChecks_Reserved7` |  |  |  |
| 11 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED6` | `FsGiReceiptSourceOfFundChecks_Reserved6` |  |  |  |
| 12 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED5` | `FsGiReceiptSourceOfFundChecks_Reserved5` |  |  |  |
| 13 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED4` | `FsGiReceiptSourceOfFundChecks_Reserved4` |  |  |  |
| 14 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED3` | `FsGiReceiptSourceOfFundChecks_Reserved3` |  |  |  |
| 15 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED2` | `FsGiReceiptSourceOfFundChecks_Reserved2` |  |  |  |
| 16 | `GI.REC.SOURCE.FUND.CHECKS.RESERVED1` | `FsGiReceiptSourceOfFundChecks_Reserved1` |  |  |  |
| 17 | `GI.REC.SOURCE.FUND.CHECKS.LOCAL.REF` | `FsGiReceiptSourceOfFundChecks_LocalRef` |  |  |  |
| 18 | `GI.REC.SOURCE.FUND.CHECKS.OVERRIDE` | `FsGiReceiptSourceOfFundChecks_Override` |  |  |  |
| 19 | `GI.REC.SOURCE.FUND.CHECKS.RECORD.STATUS` | `FsGiReceiptSourceOfFundChecks_RecordStatus` |  |  |  |
| 20 | `GI.REC.SOURCE.FUND.CHECKS.CURR.NO` | `FsGiReceiptSourceOfFundChecks_CurrNo` |  |  |  |
| 21 | `GI.REC.SOURCE.FUND.CHECKS.INPUTTER` | `FsGiReceiptSourceOfFundChecks_Inputter` |  |  |  |
| 22 | `GI.REC.SOURCE.FUND.CHECKS.DATE.TIME` | `FsGiReceiptSourceOfFundChecks_DateTime` |  |  |  |
| 23 | `GI.REC.SOURCE.FUND.CHECKS.AUTHORISER` | `FsGiReceiptSourceOfFundChecks_Authoriser` |  |  |  |
| 24 | `GI.REC.SOURCE.FUND.CHECKS.CO.CODE` | `FsGiReceiptSourceOfFundChecks_CoCode` |  |  |  |
| 25 | `GI.REC.SOURCE.FUND.CHECKS.DEPT.CODE` | `FsGiReceiptSourceOfFundChecks_DeptCode` |  |  |  |
| 26 | `GI.REC.SOURCE.FUND.CHECKS.AUDITOR.CODE` | `FsGiReceiptSourceOfFundChecks_AuditorCode` |  |  |  |
| 27 | `GI.REC.SOURCE.FUND.CHECKS.AUDIT.DATE.TIME` | `FsGiReceiptSourceOfFundChecks_AuditDateTime` |  |  |  |
