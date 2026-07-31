# EB.TAABS.CAPTURE.TXNS — Table Schema

> Source: `INSERTS/I_F.EB.TAABS.CAPTURE.TXNS` in `EB_ProductConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TCTX.PACKAGE.NAME` | `EbTaabsCaptureTxns_PackageName` | TField |  | This field indicates the EB.TAABS.PACKAGE.DETAILS record to which the data has been captured for. |
| 2 | `EB.TCTX.COMPANY` | `EbTaabsCaptureTxns_Company` | TField |  | This field indicates the COMPANY record level at which the data has been captured for. In case the transaction was captured for a table classified as 'INT' then it would be the COMPANY code of the MASTER Company. |
| 3 | `EB.TCTX.APPLICATION` | `EbTaabsCaptureTxns_Application` | TField |  | This field indicates the T24 Application for which the data has been captured for. |
| 4 | `EB.TCTX.TXN.REF` | `EbTaabsCaptureTxns_TxnRef` | TField |  | This field indicates the transaction reference of Application that was captured. |
| 5 | `EB.TCTX.DATE` | `EbTaabsCaptureTxns_Date` |  |  |  |
| 6 | `EB.TCTX.VERSION` | `EbTaabsCaptureTxns_Version` |  |  |  |
| 7 | `EB.TCTX.USER` | `EbTaabsCaptureTxns_User` |  |  |  |
| 8 | `EB.TCTX.USER.ROLE` | `EbTaabsCaptureTxns_UserRole` |  |  |  |
| 9 | `EB.TCTX.USER.COMPANY` | `EbTaabsCaptureTxns_UserCompany` |  |  |  |
| 10 | `EB.TCTX.RESERVED.3` | `EbTaabsCaptureTxns_Reserved3` |  |  |  |
| 11 | `EB.TCTX.RESERVED.2` | `EbTaabsCaptureTxns_Reserved2` |  |  |  |
| 12 | `EB.TCTX.RESERVED.1` | `EbTaabsCaptureTxns_Reserved1` |  |  |  |
| 13 | `EB.TCTX.UNIQ.REF.ID` | `EbTaabsCaptureTxns_UniqRefId` |  |  |  |
| 14 | `EB.TCTX.FUNCTION` | `EbTaabsCaptureTxns_Function` |  |  |  |
| 15 | `EB.TCTX.REMARKS` | `EbTaabsCaptureTxns_Remarks` |  |  |  |
| 16 | `EB.TCTX.TXN.CURR.NO` | `EbTaabsCaptureTxns_TxnCurrNo` |  |  |  |
| 17 | `EB.TCTX.PACKAGE.REF` | `EbTaabsCaptureTxns_PackageRef` |  |  |  |
| 18 | `EB.TCTX.UNAUTHORISED` | `EbTaabsCaptureTxns_Unauthorised` | TField |  | This field indicates the authorisation status of the transaction due to the associated event. |
| 19 | `EB.TCTX.EXCLUDE.TXN` | `EbTaabsCaptureTxns_ExcludeTxn` | TField |  | This field indicates if this record has been excluded from releasing into the target system. |
| 20 | `EB.TCTX.RECORD.STATUS` | `EbTaabsCaptureTxns_RecordStatus` | String |  |  |
| 21 | `EB.TCTX.CURR.NO` | `EbTaabsCaptureTxns_CurrNo` | String |  |  |
| 22 | `EB.TCTX.INPUTTER` | `EbTaabsCaptureTxns_Inputter` |  |  |  |
| 23 | `EB.TCTX.DATE.TIME` | `EbTaabsCaptureTxns_DateTime` |  |  |  |
| 24 | `EB.TCTX.AUTHORISER` | `EbTaabsCaptureTxns_Authoriser` | String |  |  |
| 25 | `EB.TCTX.CO.CODE` | `EbTaabsCaptureTxns_CoCode` | String |  |  |
| 26 | `EB.TCTX.DEPT.CODE` | `EbTaabsCaptureTxns_DeptCode` | String |  |  |
| 27 | `EB.TCTX.AUDITOR.CODE` | `EbTaabsCaptureTxns_AuditorCode` | String |  |  |
| 28 | `EB.TCTX.AUDIT.DATE.TIME` | `EbTaabsCaptureTxns_AuditDateTime` | String |  |  |
