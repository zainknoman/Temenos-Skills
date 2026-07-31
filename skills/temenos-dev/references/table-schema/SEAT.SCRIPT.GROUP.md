# SEAT.SCRIPT.GROUP — Table Schema

> Source: `INSERTS/I_F.SEAT.SCRIPT.GROUP` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SEAT.GRP.DESCRIPTION` | `SeatScriptGroup_Description` |  |  |  |
| 2 | `EB.SEAT.GRP.RESERVED.5` | `SeatScriptGroup_Reserved5` | TField |  |  |
| 3 | `EB.SEAT.GRP.RESERVED.4` | `SeatScriptGroup_Reserved4` | TField |  |  |
| 4 | `EB.SEAT.GRP.RESERVED.3` | `SeatScriptGroup_Reserved3` | TField |  |  |
| 5 | `EB.SEAT.GRP.RESERVED.2` | `SeatScriptGroup_Reserved2` | TField |  |  |
| 6 | `EB.SEAT.GRP.RESERVED.1` | `SeatScriptGroup_Reserved1` | TField |  |  |
| 7 | `EB.SEAT.GRP.LOCAL.REF` | `SeatScriptGroup_LocalRef` |  |  |  |
| 8 | `EB.SEAT.GRP.RECORD.STATUS` | `SeatScriptGroup_RecordStatus` | String |  |  |
| 9 | `EB.SEAT.GRP.CURR.NO` | `SeatScriptGroup_CurrNo` | String |  |  |
| 10 | `EB.SEAT.GRP.INPUTTER` | `SeatScriptGroup_Inputter` |  |  |  |
| 11 | `EB.SEAT.GRP.DATE.TIME` | `SeatScriptGroup_DateTime` |  |  |  |
| 12 | `EB.SEAT.GRP.AUTHORISER` | `SeatScriptGroup_Authoriser` | String |  |  |
| 13 | `EB.SEAT.GRP.CO.CODE` | `SeatScriptGroup_CoCode` | String |  |  |
| 14 | `EB.SEAT.GRP.DEPT.CODE` | `SeatScriptGroup_DeptCode` | String |  |  |
| 15 | `EB.SEAT.GRP.AUDITOR.CODE` | `SeatScriptGroup_AuditorCode` | String |  |  |
| 16 | `EB.SEAT.GRP.AUDIT.DATE.TIME` | `SeatScriptGroup_AuditDateTime` | String |  |  |
