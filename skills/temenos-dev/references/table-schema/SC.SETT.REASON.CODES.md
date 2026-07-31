# SC.SETT.REASON.CODES — Table Schema

> Source: `INSERTS/I_F.SC.SETT.REASON.CODES` in `SC_STP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.RCD.SHORT.NAME` | `ScSettReasonCodes_ShortName` | TField | Yes | This field will hold the short name of this code. Validation Rules: Single value field. Mandatory field. |
| 2 | `SC.RCD.DESCRIPTION` | `ScSettReasonCodes_Description` |  |  |  |
| 3 | `SC.RCD.OUT.NARRATIVE` | `ScSettReasonCodes_OutNarrative` | TField |  |  |
| 4 | `SC.RCD.RESERVED4` | `ScSettReasonCodes_Reserved4` | TField |  |  |
| 5 | `SC.RCD.RESERVED3` | `ScSettReasonCodes_Reserved3` | TField |  |  |
| 6 | `SC.RCD.RESERVED2` | `ScSettReasonCodes_Reserved2` | TField |  |  |
| 7 | `SC.RCD.RESERVED1` | `ScSettReasonCodes_Reserved1` | TField |  |  |
| 8 | `SC.RCD.LOCAL.REF` | `ScSettReasonCodes_LocalRef` |  |  |  |
| 9 | `SC.RCD.OVERRIDE` | `ScSettReasonCodes_Override` | TField |  |  |
| 10 | `SC.RCD.RECORD.STATUS` | `ScSettReasonCodes_RecordStatus` | String |  |  |
| 11 | `SC.RCD.CURR.NO` | `ScSettReasonCodes_CurrNo` | String |  |  |
| 12 | `SC.RCD.INPUTTER` | `ScSettReasonCodes_Inputter` |  |  |  |
| 13 | `SC.RCD.DATE.TIME` | `ScSettReasonCodes_DateTime` |  |  |  |
| 14 | `SC.RCD.AUTHORISER` | `ScSettReasonCodes_Authoriser` | String |  |  |
| 15 | `SC.RCD.CO.CODE` | `ScSettReasonCodes_CoCode` | String |  |  |
| 16 | `SC.RCD.DEPT.CODE` | `ScSettReasonCodes_DeptCode` | String |  |  |
| 17 | `SC.RCD.AUDITOR.CODE` | `ScSettReasonCodes_AuditorCode` | String |  |  |
| 18 | `SC.RCD.AUDIT.DATE.TIME` | `ScSettReasonCodes_AuditDateTime` | String |  |  |
