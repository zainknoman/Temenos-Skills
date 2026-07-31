# FS.GA.DUPLICATE.RECORDS.CHECK — Table Schema

> Source: `INSERTS/I_F.FS.GA.DUPLICATE.RECORDS.CHECK` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DUPLICATE.RECORDS.CHECK.OBJECT.NAME` | `FsGaDuplicateRecordsCheck_ObjectName` | TField |  | Object Name Multifonds DB Column is OBJ_NAME. |
| 2 | `DUPLICATE.RECORDS.CHECK.COLUMN.NAME` | `FsGaDuplicateRecordsCheck_ColumnName` | TField |  | Column Name Multifonds DB Column is COL_NAME. |
| 3 | `DUPLICATE.RECORDS.CHECK.COLUMN.CODE` | `FsGaDuplicateRecordsCheck_ColumnCode` | TField |  | Column code Multifonds DB Column is CELEM. |
| 4 | `DUPLICATE.RECORDS.CHECK.CTYPE.CHECK` | `FsGaDuplicateRecordsCheck_CtypeCheck` | TField |  | Ctype check Multifonds DB Column is CTYP_CHECK. |
| 5 | `DUPLICATE.RECORDS.CHECK.RECORD.STATUS` | `FsGaDuplicateRecordsCheck_RecordStatus` | String |  |  |
| 6 | `DUPLICATE.RECORDS.CHECK.CURR.NO` | `FsGaDuplicateRecordsCheck_CurrNo` | String |  |  |
| 7 | `DUPLICATE.RECORDS.CHECK.INPUTTER` | `FsGaDuplicateRecordsCheck_Inputter` |  |  |  |
| 8 | `DUPLICATE.RECORDS.CHECK.DATE.TIME` | `FsGaDuplicateRecordsCheck_DateTime` |  |  |  |
| 9 | `DUPLICATE.RECORDS.CHECK.AUTHORISER` | `FsGaDuplicateRecordsCheck_Authoriser` | String |  |  |
| 10 | `DUPLICATE.RECORDS.CHECK.CO.CODE` | `FsGaDuplicateRecordsCheck_CoCode` | String |  |  |
| 11 | `DUPLICATE.RECORDS.CHECK.DEPT.CODE` | `FsGaDuplicateRecordsCheck_DeptCode` | String |  |  |
| 12 | `DUPLICATE.RECORDS.CHECK.AUDITOR.CODE` | `FsGaDuplicateRecordsCheck_AuditorCode` | String |  |  |
| 13 | `DUPLICATE.RECORDS.CHECK.AUDIT.DATE.TIME` | `FsGaDuplicateRecordsCheck_AuditDateTime` | String |  |  |
