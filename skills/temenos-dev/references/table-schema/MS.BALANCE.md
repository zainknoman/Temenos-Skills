# MS.BALANCE — Table Schema

> Source: `INSERTS/I_F.MS.BALANCE` in `SE_MSBalActApi.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MSBAL.FIELD.NAME` | `MsBalance_FieldName` |  |  |  |
| 2 | `MSBAL.FIELD.VALUE` | `MsBalance_FieldValue` |  |  |  |
| 3 | `MSBAL.RECORD.STATUS` | `MsBalance_RecordStatus` | String |  |  |
| 4 | `MSBAL.CURR.NO` | `MsBalance_CurrNo` | String |  |  |
| 5 | `MSBAL.INPUTTER` | `MsBalance_Inputter` |  |  |  |
| 6 | `MSBAL.DATE.TIME` | `MsBalance_DateTime` |  |  |  |
| 7 | `MSBAL.AUTHORISER` | `MsBalance_Authoriser` | String |  |  |
| 8 | `MSBAL.CO.CODE` | `MsBalance_CoCode` | String |  |  |
| 9 | `MSBAL.DEPT.CODE` | `MsBalance_DeptCode` | String |  |  |
| 10 | `MSBAL.AUDITOR.CODE` | `MsBalance_AuditorCode` | String |  |  |
| 11 | `MSBAL.AUDIT.DATE.TIME` | `MsBalance_AuditDateTime` | String |  |  |
