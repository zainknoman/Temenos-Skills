# SC.CA.REASON.CODE — Table Schema

> Source: `INSERTS/I_F.SC.CA.REASON.CODE` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.RC.DESCRIPTION` | `ScCaReasonCode_Description` |  |  |  |
| 2 | `SC.RC.RESERVED1` | `ScCaReasonCode_Reserved1` | TField |  |  |
| 3 | `SC.RC.RESERVED2` | `ScCaReasonCode_Reserved2` | TField |  |  |
| 4 | `SC.RC.RESERVED3` | `ScCaReasonCode_Reserved3` | TField |  |  |
| 5 | `SC.RC.RESERVED4` | `ScCaReasonCode_Reserved4` | TField |  |  |
| 6 | `SC.RC.RESERVED5` | `ScCaReasonCode_Reserved5` | TField |  |  |
| 7 | `SC.RC.RECORD.STATUS` | `ScCaReasonCode_RecordStatus` | String |  |  |
| 8 | `SC.RC.CURR.NO` | `ScCaReasonCode_CurrNo` | String |  |  |
| 9 | `SC.RC.INPUTTER` | `ScCaReasonCode_Inputter` |  |  |  |
| 10 | `SC.RC.DATE.TIME` | `ScCaReasonCode_DateTime` |  |  |  |
| 11 | `SC.RC.AUTHORISER` | `ScCaReasonCode_Authoriser` | String |  |  |
| 12 | `SC.RC.CO.CODE` | `ScCaReasonCode_CoCode` | String |  |  |
| 13 | `SC.RC.DEPT.CODE` | `ScCaReasonCode_DeptCode` | String |  |  |
| 14 | `SC.RC.AUDITOR.CODE` | `ScCaReasonCode_AuditorCode` | String |  |  |
| 15 | `SC.RC.AUDIT.DATE.TIME` | `ScCaReasonCode_AuditDateTime` | String |  |  |
