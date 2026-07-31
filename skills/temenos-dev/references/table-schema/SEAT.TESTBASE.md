# SEAT.TESTBASE — Table Schema

> Source: `INSERTS/I_F.SEAT.TESTBASE` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.TB.DESCRIPTION` | `SeatTestbase_Description` |  |  |  |
| 2 | `SE.TB.START.DATE` | `SeatTestbase_StartDate` | TField |  |  |
| 3 | `SE.TB.END.DATE` | `SeatTestbase_EndDate` | TField |  |  |
| 4 | `SE.TB.MODEL.BANK` | `SeatTestbase_ModelBank` | TField |  |  |
| 5 | `SE.TB.NO.OF.COMPANY` | `SeatTestbase_NoOfCompany` | TField |  |  |
| 6 | `SE.TB.OTHER.SQUADS` | `SeatTestbase_OtherSquads` |  |  |  |
| 7 | `SE.TB.RESERVED.5` | `SeatTestbase_Reserved5` | TField |  |  |
| 8 | `SE.TB.RESERVED.4` | `SeatTestbase_Reserved4` | TField |  |  |
| 9 | `SE.TB.RESERVED.3` | `SeatTestbase_Reserved3` | TField |  |  |
| 10 | `SE.TB.RESERVED.2` | `SeatTestbase_Reserved2` | TField |  |  |
| 11 | `SE.TB.RESERVED.1` | `SeatTestbase_Reserved1` | TField |  |  |
| 12 | `SE.TB.RECORD.STATUS` | `SeatTestbase_RecordStatus` | String |  |  |
| 13 | `SE.TB.CURR.NO` | `SeatTestbase_CurrNo` | String |  |  |
| 14 | `SE.TB.INPUTTER` | `SeatTestbase_Inputter` |  |  |  |
| 15 | `SE.TB.DATE.TIME` | `SeatTestbase_DateTime` |  |  |  |
| 16 | `SE.TB.AUTHORISER` | `SeatTestbase_Authoriser` | String |  |  |
| 17 | `SE.TB.CO.CODE` | `SeatTestbase_CoCode` | String |  |  |
| 18 | `SE.TB.DEPT.CODE` | `SeatTestbase_DeptCode` | String |  |  |
| 19 | `SE.TB.AUDITOR.CODE` | `SeatTestbase_AuditorCode` | String |  |  |
| 20 | `SE.TB.AUDIT.DATE.TIME` | `SeatTestbase_AuditDateTime` | String |  |  |
