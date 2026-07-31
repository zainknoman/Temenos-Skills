# PP.TRANSACTION.TABLES — Table Schema

> Source: `INSERTS/I_F.PP.TRANSACTION.TABLES` in `PP_OutwardMappingFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTTS.ApplicationName` | `PpTransactionTables_Applicationname` |  |  |  |
| 2 | `PPTTS.RECORD.STATUS` | `PpTransactionTables_RecordStatus` | String |  |  |
| 3 | `PPTTS.CURR.NO` | `PpTransactionTables_CurrNo` | String |  |  |
| 4 | `PPTTS.INPUTTER` | `PpTransactionTables_Inputter` |  |  |  |
| 5 | `PPTTS.DATE.TIME` | `PpTransactionTables_DateTime` |  |  |  |
| 6 | `PPTTS.AUTHORISER` | `PpTransactionTables_Authoriser` | String |  |  |
| 7 | `PPTTS.CO.CODE` | `PpTransactionTables_CoCode` | String |  |  |
| 8 | `PPTTS.DEPT.CODE` | `PpTransactionTables_DeptCode` | String |  |  |
| 9 | `PPTTS.AUDITOR.CODE` | `PpTransactionTables_AuditorCode` | String |  |  |
| 10 | `PPTTS.AUDIT.DATE.TIME` | `PpTransactionTables_AuditDateTime` | String |  |  |
