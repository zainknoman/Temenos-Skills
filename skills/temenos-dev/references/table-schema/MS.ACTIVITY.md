# MS.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.MS.ACTIVITY` in `SE_MSBalActApi.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MSACT.FIELD.NAME` | `MsActivity_FieldName` |  |  |  |
| 2 | `MSACT.FIELD.VALUE` | `MsActivity_FieldValue` |  |  |  |
| 3 | `MSACT.RECORD.STATUS` | `MsActivity_RecordStatus` | String |  |  |
| 4 | `MSACT.CURR.NO` | `MsActivity_CurrNo` | String |  |  |
| 5 | `MSACT.INPUTTER` | `MsActivity_Inputter` |  |  |  |
| 6 | `MSACT.DATE.TIME` | `MsActivity_DateTime` |  |  |  |
| 7 | `MSACT.AUTHORISER` | `MsActivity_Authoriser` | String |  |  |
| 8 | `MSACT.CO.CODE` | `MsActivity_CoCode` | String |  |  |
| 9 | `MSACT.DEPT.CODE` | `MsActivity_DeptCode` | String |  |  |
| 10 | `MSACT.AUDITOR.CODE` | `MsActivity_AuditorCode` | String |  |  |
| 11 | `MSACT.AUDIT.DATE.TIME` | `MsActivity_AuditDateTime` | String |  |  |
