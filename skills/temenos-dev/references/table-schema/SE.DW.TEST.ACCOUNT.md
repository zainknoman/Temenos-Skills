# SE.DW.TEST.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.SE.DW.TEST.ACCOUNT` in `SE_TestOtherApplication.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.AC.CUSTOMER.ID` | `SeDwTestAccount_CustomerId` | TField | Yes | Identifies the Customer to whom the Account belongs. This field maintains a link between the Customer and their Accounts. This field must contain a valid Customer Id from SE.DW.TEST.CUSTOMER application. This is a mandatory field. |
| 2 | `DW.AC.CURRENCY` | `SeDwTestAccount_Currency` | TField | Yes | Identifies the Currency of the Account. This field must contain a valid Currency Id from CURRENCY application. This is a mandatory field. |
| 3 | `DW.AC.BALANCE` | `SeDwTestAccount_Balance` | TField | Yes | Identifies the Balance of the Account. This is a mandatory field. |
| 4 | `DW.AC.RECORD.STATUS` | `SeDwTestAccount_RecordStatus` | String |  |  |
| 5 | `DW.AC.CURR.NO` | `SeDwTestAccount_CurrNo` | String |  |  |
| 6 | `DW.AC.INPUTTER` | `SeDwTestAccount_Inputter` |  |  |  |
| 7 | `DW.AC.DATE.TIME` | `SeDwTestAccount_DateTime` |  |  |  |
| 8 | `DW.AC.AUTHORISER` | `SeDwTestAccount_Authoriser` | String |  |  |
| 9 | `DW.AC.CO.CODE` | `SeDwTestAccount_CoCode` | String |  |  |
| 10 | `DW.AC.DEPT.CODE` | `SeDwTestAccount_DeptCode` | String |  |  |
| 11 | `DW.AC.AUDITOR.CODE` | `SeDwTestAccount_AuditorCode` | String |  |  |
| 12 | `DW.AC.AUDIT.DATE.TIME` | `SeDwTestAccount_AuditDateTime` | String |  |  |
