# MDA.REGISTRY — Table Schema

> Source: `INSERTS/I_F.MDA.REGISTRY` in `SE_MDARegistry.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDAR.FIELD.NAME` | `Mdar_FieldName` |  |  |  |
| 2 | `MDAR.FIELD.VALUE` | `Mdar_FieldValue` |  |  |  |
| 3 | `MDAR.RECORD.STATUS` | `Mdar_RecordStatus` |  |  |  |
| 4 | `MDAR.CURR.NO` | `Mdar_CurrNo` |  |  |  |
| 5 | `MDAR.INPUTTER` | `Mdar_Inputter` |  |  |  |
| 6 | `MDAR.DATE.TIME` | `Mdar_DateTime` |  |  |  |
| 7 | `MDAR.AUTHORISER` | `Mdar_Authoriser` |  |  |  |
| 8 | `MDAR.CO.CODE` | `Mdar_CoCode` |  |  |  |
| 9 | `MDAR.DEPT.CODE` | `Mdar_DeptCode` |  |  |  |
| 10 | `MDAR.AUDITOR.CODE` | `Mdar_AuditorCode` |  |  |  |
| 11 | `MDAR.AUDIT.DATE.TIME` | `Mdar_AuditDateTime` |  |  |  |
