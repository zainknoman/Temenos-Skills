# CAMB.H.CUST.CHECK.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAMB.H.CUST.CHECK.DETAILS` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.CHECK.NUMBER` | `CambHCustCheckDetails_CheckNumber` |  |  |  |
| 2 | `CAMB.ACCOUNT.NUMBER` | `CambHCustCheckDetails_AccountNumber` |  |  |  |
| 3 | `CAMB.ISSUE.DATE` | `CambHCustCheckDetails_IssueDate` |  |  |  |
| 4 | `CAMB.AMOUNT` | `CambHCustCheckDetails_Amount` |  |  |  |
| 5 | `CAMB.CURRENCY` | `CambHCustCheckDetails_Currency` |  |  |  |
| 6 | `CAMB.PAYEE.NAME` | `CambHCustCheckDetails_PayeeName` |  |  |  |
| 7 | `CAMB.CUSTOMER.NO` | `CambHCustCheckDetails_CustomerNo` |  |  |  |
| 8 | `CAMB.TRANSACTION.STATUS` | `CambHCustCheckDetails_TransactionStatus` |  |  |  |
| 9 | `CAMB.DATE` | `CambHCustCheckDetails_Date` |  |  |  |
| 10 | `CAMB.FT.REFERENCE` | `CambHCustCheckDetails_FtReference` |  |  |  |
| 11 | `CAMB.ERROR.MSG` | `CambHCustCheckDetails_ErrorMsg` |  |  |  |
| 12 | `CAMB.EMAIL.ADDR` | `CambHCustCheckDetails_EmailAddr` |  |  |  |
| 13 | `CAMB.CHANGE.COMMENTS` | `CambHCustCheckDetails_ChangeComments` |  |  |  |
| 14 | `CAMB.CUSTOMER.NAME` | `CambHCustCheckDetails_CustomerName` |  |  |  |
| 15 | `CAMB.RECORD.STATUS` | `CambHCustCheckDetails_RecordStatus` |  |  |  |
| 16 | `CAMB.CURR.NO` | `CambHCustCheckDetails_CurrNo` |  |  |  |
| 17 | `CAMB.INPUTTER` | `CambHCustCheckDetails_Inputter` |  |  |  |
| 18 | `CAMB.DATE.TIME` | `CambHCustCheckDetails_DateTime` |  |  |  |
| 19 | `CAMB.AUTHORISER` | `CambHCustCheckDetails_Authoriser` |  |  |  |
| 20 | `CAMB.CO.CODE` | `CambHCustCheckDetails_CoCode` |  |  |  |
| 21 | `CAMB.DEPT.CODE` | `CambHCustCheckDetails_DeptCode` |  |  |  |
| 22 | `CAMB.AUDITOR.CODE` | `CambHCustCheckDetails_AuditorCode` |  |  |  |
| 23 | `CAMB.AUDIT.DATE.TIME` | `CambHCustCheckDetails_AuditDateTime` |  |  |  |
