# SE.DW.TEST.CUSTOMER.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.SE.DW.TEST.CUSTOMER.ACCOUNT` in `SE_TestOtherApplication.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.CAC.ACCOUNT.NUMBER` | `SeDwTestCustomerAccount_AccountNumber` | TField |  | Specifies an Account belonging to the Customer specified in field 0. The numbers of all Accounts belonging to the Customer specified in Field 0 are held in fields 1 onwards, one Account Number per field. Validation Rules: Standard Account Number format. Internal field. This is a NOINPUT field. |
| 2 | `DW.CAC.RECORD.STATUS` | `SeDwTestCustomerAccount_RecordStatus` | String |  |  |
| 3 | `DW.CAC.CURR.NO` | `SeDwTestCustomerAccount_CurrNo` | String |  |  |
| 4 | `DW.CAC.INPUTTER` | `SeDwTestCustomerAccount_Inputter` |  |  |  |
| 5 | `DW.CAC.DATE.TIME` | `SeDwTestCustomerAccount_DateTime` |  |  |  |
| 6 | `DW.CAC.AUTHORISER` | `SeDwTestCustomerAccount_Authoriser` | String |  |  |
| 7 | `DW.CAC.CO.CODE` | `SeDwTestCustomerAccount_CoCode` | String |  |  |
| 8 | `DW.CAC.DEPT.CODE` | `SeDwTestCustomerAccount_DeptCode` | String |  |  |
| 9 | `DW.CAC.AUDITOR.CODE` | `SeDwTestCustomerAccount_AuditorCode` | String |  |  |
| 10 | `DW.CAC.AUDIT.DATE.TIME` | `SeDwTestCustomerAccount_AuditDateTime` | String |  |  |
