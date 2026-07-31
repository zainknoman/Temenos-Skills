# SE.DW.TEST.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.SE.DW.TEST.CUSTOMER` in `SE_TestOtherApplication.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.CUS.CUSTOMER.NAME` | `SeDwTestCustomer_CustomerName` | TField |  | Identifies the Name of the Customer. |
| 2 | `DW.CUS.CUSTOMER.MNEMONIC` | `SeDwTestCustomer_CustomerMnemonic` | TField |  | Identifies the Mnemonic of the Customer. |
| 3 | `DW.CUS.CUSTOMER.ADDRESS` | `SeDwTestCustomer_CustomerAddress` | TField |  | Identifies the Address of the Customer. |
| 4 | `DW.CUS.RECORD.STATUS` | `SeDwTestCustomer_RecordStatus` | String |  |  |
| 5 | `DW.CUS.CURR.NO` | `SeDwTestCustomer_CurrNo` | String |  |  |
| 6 | `DW.CUS.INPUTTER` | `SeDwTestCustomer_Inputter` |  |  |  |
| 7 | `DW.CUS.DATE.TIME` | `SeDwTestCustomer_DateTime` |  |  |  |
| 8 | `DW.CUS.AUTHORISER` | `SeDwTestCustomer_Authoriser` | String |  |  |
| 9 | `DW.CUS.CO.CODE` | `SeDwTestCustomer_CoCode` | String |  |  |
| 10 | `DW.CUS.DEPT.CODE` | `SeDwTestCustomer_DeptCode` | String |  |  |
| 11 | `DW.CUS.AUDITOR.CODE` | `SeDwTestCustomer_AuditorCode` | String |  |  |
| 12 | `DW.CUS.AUDIT.DATE.TIME` | `SeDwTestCustomer_AuditDateTime` | String |  |  |
