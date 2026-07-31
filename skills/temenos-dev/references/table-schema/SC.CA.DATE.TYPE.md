# SC.CA.DATE.TYPE — Table Schema

> Source: `INSERTS/I_F.SC.CA.DATE.TYPE` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.DT.DESCRIPTION` | `ScCaDateType_Description` |  |  |  |
| 2 | `SC.DT.RESERVED1` | `ScCaDateType_Reserved1` | TField |  |  |
| 3 | `SC.DT.RESERVED2` | `ScCaDateType_Reserved2` | TField |  |  |
| 4 | `SC.DT.RESERVED3` | `ScCaDateType_Reserved3` | TField |  |  |
| 5 | `SC.DT.RESERVED4` | `ScCaDateType_Reserved4` | TField |  |  |
| 6 | `SC.DT.RESERVED5` | `ScCaDateType_Reserved5` | TField |  |  |
| 7 | `SC.DT.RECORD.STATUS` | `ScCaDateType_RecordStatus` | String |  |  |
| 8 | `SC.DT.CURR.NO` | `ScCaDateType_CurrNo` | String |  |  |
| 9 | `SC.DT.INPUTTER` | `ScCaDateType_Inputter` |  |  |  |
| 10 | `SC.DT.DATE.TIME` | `ScCaDateType_DateTime` |  |  |  |
| 11 | `SC.DT.AUTHORISER` | `ScCaDateType_Authoriser` | String |  |  |
| 12 | `SC.DT.CO.CODE` | `ScCaDateType_CoCode` | String |  |  |
| 13 | `SC.DT.DEPT.CODE` | `ScCaDateType_DeptCode` | String |  |  |
| 14 | `SC.DT.AUDITOR.CODE` | `ScCaDateType_AuditorCode` | String |  |  |
| 15 | `SC.DT.AUDIT.DATE.TIME` | `ScCaDateType_AuditDateTime` | String |  |  |
