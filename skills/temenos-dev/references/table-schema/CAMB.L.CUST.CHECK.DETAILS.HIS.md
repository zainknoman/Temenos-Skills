# CAMB.L.CUST.CHECK.DETAILS.HIS — Table Schema

> Source: `INSERTS/I_F.CAMB.L.CUST.CHECK.DETAILS.HIS` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.CHECK.NUMBER` | `CambLCustCheckDetailsHis_CheckNumber` |  |  |  |
| 2 | `CAMB.ACCOUNT.NUMBER` | `CambLCustCheckDetailsHis_AccountNumber` |  |  |  |
| 3 | `CAMB.ISSUE.DATE` | `CambLCustCheckDetailsHis_IssueDate` |  |  |  |
| 4 | `CAMB.AMOUNT` | `CambLCustCheckDetailsHis_Amount` |  |  |  |
| 5 | `CAMB.CURRENCY` | `CambLCustCheckDetailsHis_Currency` |  |  |  |
| 6 | `CAMB.PAYEE.NAME` | `CambLCustCheckDetailsHis_PayeeName` |  |  |  |
| 7 | `CAMB.CUSTOMER.NO` | `CambLCustCheckDetailsHis_CustomerNo` |  |  |  |
| 8 | `CAMB.TRANSACTION.STATUS` | `CambLCustCheckDetailsHis_TransactionStatus` |  |  |  |
| 9 | `CAMB.DATE` | `CambLCustCheckDetailsHis_Date` |  |  |  |
| 10 | `CAMB.FT.REFERENCE` | `CambLCustCheckDetailsHis_FtReference` |  |  |  |
| 11 | `CAMB.ERROR.MSG` | `CambLCustCheckDetailsHis_ErrorMsg` |  |  |  |
| 12 | `CAMB.EMAIL.ADDR` | `CambLCustCheckDetailsHis_EmailAddr` |  |  |  |
| 13 | `CAMB.CHANGE.COMMENTS` | `CambLCustCheckDetailsHis_ChangeComments` |  |  |  |
