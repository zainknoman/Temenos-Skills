# ST.DEL.MESSAGE — Table Schema

> Source: `INSERTS/I_F.ST.DEL.MESSAGE` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.MSG.DESCRIPTION` | `StDelMessage_Description` | TField |  | This will represent the description of the Message. |
| 2 | `ST.MSG.RESERVED.5` | `StDelMessage_Reserved5` | TField |  |  |
| 3 | `ST.MSG.RESERVED.4` | `StDelMessage_Reserved4` | TField |  |  |
| 4 | `ST.MSG.RESERVED.3` | `StDelMessage_Reserved3` | TField |  |  |
| 5 | `ST.MSG.RESERVED.2` | `StDelMessage_Reserved2` | TField |  |  |
| 6 | `ST.MSG.RESERVED.1` | `StDelMessage_Reserved1` | TField |  |  |
| 7 | `ST.MSG.LOCAL.REF` | `StDelMessage_LocalRef` |  |  |  |
| 8 | `ST.MSG.OVERRIDE` | `StDelMessage_Override` |  |  |  |
| 9 | `ST.MSG.RECORD.STATUS` | `StDelMessage_RecordStatus` | String |  |  |
| 10 | `ST.MSG.CURR.NO` | `StDelMessage_CurrNo` | String |  |  |
| 11 | `ST.MSG.INPUTTER` | `StDelMessage_Inputter` |  |  |  |
| 12 | `ST.MSG.DATE.TIME` | `StDelMessage_DateTime` |  |  |  |
| 13 | `ST.MSG.AUTHORISER` | `StDelMessage_Authoriser` | String |  |  |
| 14 | `ST.MSG.CO.CODE` | `StDelMessage_CoCode` | String |  |  |
| 15 | `ST.MSG.DEPT.CODE` | `StDelMessage_DeptCode` | String |  |  |
| 16 | `ST.MSG.AUDITOR.CODE` | `StDelMessage_AuditorCode` | String |  |  |
| 17 | `ST.MSG.AUDIT.DATE.TIME` | `StDelMessage_AuditDateTime` | String |  |  |
