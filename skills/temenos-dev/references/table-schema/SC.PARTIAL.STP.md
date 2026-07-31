# SC.PARTIAL.STP — Table Schema

> Source: `INSERTS/I_F.SC.PARTIAL.STP` in `SC_SccConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PSTP.TYPE` | `ScPartialStp_Type` |  |  |  |
| 2 | `SC.PSTP.RESERVED.5` | `ScPartialStp_Reserved5` | TField |  |  |
| 3 | `SC.PSTP.RESERVED.4` | `ScPartialStp_Reserved4` | TField |  |  |
| 4 | `SC.PSTP.RESERVED.3` | `ScPartialStp_Reserved3` | TField |  |  |
| 5 | `SC.PSTP.RESERVED.2` | `ScPartialStp_Reserved2` | TField |  |  |
| 6 | `SC.PSTP.RESERVED.1` | `ScPartialStp_Reserved1` | TField |  |  |
| 7 | `SC.PSTP.LOCAL.REF` | `ScPartialStp_LocalRef` |  |  |  |
| 8 | `SC.PSTP.OVERRIDE` | `ScPartialStp_Override` |  |  |  |
| 9 | `SC.PSTP.RECORD.STATUS` | `ScPartialStp_RecordStatus` | String |  |  |
| 10 | `SC.PSTP.CURR.NO` | `ScPartialStp_CurrNo` | String |  |  |
| 11 | `SC.PSTP.INPUTTER` | `ScPartialStp_Inputter` |  |  |  |
| 12 | `SC.PSTP.DATE.TIME` | `ScPartialStp_DateTime` |  |  |  |
| 13 | `SC.PSTP.AUTHORISER` | `ScPartialStp_Authoriser` | String |  |  |
| 14 | `SC.PSTP.CO.CODE` | `ScPartialStp_CoCode` | String |  |  |
| 15 | `SC.PSTP.DEPT.CODE` | `ScPartialStp_DeptCode` | String |  |  |
| 16 | `SC.PSTP.AUDITOR.CODE` | `ScPartialStp_AuditorCode` | String |  |  |
| 17 | `SC.PSTP.AUDIT.DATE.TIME` | `ScPartialStp_AuditDateTime` | String |  |  |
