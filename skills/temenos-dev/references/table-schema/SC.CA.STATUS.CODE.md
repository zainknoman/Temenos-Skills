# SC.CA.STATUS.CODE — Table Schema

> Source: `INSERTS/I_F.SC.CA.STATUS.CODE` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ST.DESCRIPTION` | `ScCaStatusCode_Description` |  |  |  |
| 2 | `SC.ST.RESERVED1` | `ScCaStatusCode_Reserved1` | TField |  |  |
| 3 | `SC.ST.RESERVED2` | `ScCaStatusCode_Reserved2` | TField |  |  |
| 4 | `SC.ST.RESERVED3` | `ScCaStatusCode_Reserved3` | TField |  |  |
| 5 | `SC.ST.RESERVED4` | `ScCaStatusCode_Reserved4` | TField |  |  |
| 6 | `SC.ST.RESERVED5` | `ScCaStatusCode_Reserved5` | TField |  |  |
| 7 | `SC.ST.RECORD.STATUS` | `ScCaStatusCode_RecordStatus` | String |  |  |
| 8 | `SC.ST.CURR.NO` | `ScCaStatusCode_CurrNo` | String |  |  |
| 9 | `SC.ST.INPUTTER` | `ScCaStatusCode_Inputter` |  |  |  |
| 10 | `SC.ST.DATE.TIME` | `ScCaStatusCode_DateTime` |  |  |  |
| 11 | `SC.ST.AUTHORISER` | `ScCaStatusCode_Authoriser` | String |  |  |
| 12 | `SC.ST.CO.CODE` | `ScCaStatusCode_CoCode` | String |  |  |
| 13 | `SC.ST.DEPT.CODE` | `ScCaStatusCode_DeptCode` | String |  |  |
| 14 | `SC.ST.AUDITOR.CODE` | `ScCaStatusCode_AuditorCode` | String |  |  |
| 15 | `SC.ST.AUDIT.DATE.TIME` | `ScCaStatusCode_AuditDateTime` | String |  |  |
