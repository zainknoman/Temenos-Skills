# SEAT.COMP.SCENARIO — Table Schema

> Source: `INSERTS/I_F.SEAT.COMP.SCENARIO` in `SE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SCEN.DESCRIPTION` | `SeatCompScenario_Description` |  |  |  |
| 2 | `SCEN.MASTER.SEAT.COMP` | `SeatCompScenario_MasterSeatComp` | TField |  | Name of the SEAT.COMPONENT to be tested initially. Must be a valid SEAT.COMPONENT. |
| 3 | `SCEN.LINK.SEAT.COMP` | `SeatCompScenario_LinkSeatComp` |  |  |  |
| 4 | `SCEN.RESERVED.10` | `SeatCompScenario_Reserved10` | TField |  |  |
| 5 | `SCEN.RESERVED.9` | `SeatCompScenario_Reserved9` | TField |  |  |
| 6 | `SCEN.RESERVED.8` | `SeatCompScenario_Reserved8` | TField |  |  |
| 7 | `SCEN.RESERVED.7` | `SeatCompScenario_Reserved7` | TField |  |  |
| 8 | `SCEN.RESERVED.6` | `SeatCompScenario_Reserved6` | TField |  |  |
| 9 | `SCEN.RESERVED.5` | `SeatCompScenario_Reserved5` | TField |  |  |
| 10 | `SCEN.RESERVED.4` | `SeatCompScenario_Reserved4` | TField |  |  |
| 11 | `SCEN.RESERVED.3` | `SeatCompScenario_Reserved3` | TField |  |  |
| 12 | `SCEN.RESERVED.2` | `SeatCompScenario_Reserved2` | TField |  |  |
| 13 | `SCEN.RESERVED.1` | `SeatCompScenario_Reserved1` | TField |  |  |
| 14 | `SCEN.RECORD.STATUS` | `SeatCompScenario_RecordStatus` | String |  |  |
| 15 | `SCEN.CURR.NO` | `SeatCompScenario_CurrNo` | String |  |  |
| 16 | `SCEN.INPUTTER` | `SeatCompScenario_Inputter` |  |  |  |
| 17 | `SCEN.DATE.TIME` | `SeatCompScenario_DateTime` |  |  |  |
| 18 | `SCEN.AUTHORISER` | `SeatCompScenario_Authoriser` | String |  |  |
| 19 | `SCEN.CO.CODE` | `SeatCompScenario_CoCode` | String |  |  |
| 20 | `SCEN.DEPT.CODE` | `SeatCompScenario_DeptCode` | String |  |  |
| 21 | `SCEN.AUDITOR.CODE` | `SeatCompScenario_AuditorCode` | String |  |  |
| 22 | `SCEN.AUDIT.DATE.TIME` | `SeatCompScenario_AuditDateTime` | String |  |  |
