# SEAT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SEAT.PARAMETER` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.PAR.SEAT.OPTION` | `SeatParameter_SeatOption` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `SE.PAR.DEFAULT.THRESHOLD` | `SeatParameter_DefaultThreshold` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `SE.PAR.IMAGE.TRACE` | `SeatParameter_ImageTrace` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `SE.PAR.PARAMETER.NAME` | `SeatParameter_ParameterName` |  |  |  |
| 5 | `SE.PAR.PARAMETER.VALUE` | `SeatParameter_ParameterValue` |  |  |  |
| 6 | `SE.PAR.DYNAMIC.REG.DATES` | `SeatParameter_DynamicRegDates` | TField |  |  |
| 7 | `SE.PAR.REGRESSION.DAY` | `SeatParameter_RegressionDay` |  |  |  |
| 8 | `SE.PAR.REGRESSION.DATE` | `SeatParameter_RegressionDate` |  |  |  |
| 9 | `SE.PAR.RESERVED.5` | `SeatParameter_Reserved5` |  |  |  |
| 10 | `SE.PAR.RESERVED.4` | `SeatParameter_Reserved4` |  |  |  |
| 11 | `SE.PAR.RESERVED.3` | `SeatParameter_Reserved3` |  |  |  |
| 12 | `SE.PAR.RESERVED.2` | `SeatParameter_Reserved2` |  |  |  |
| 13 | `SE.PAR.RESERVED.1` | `SeatParameter_Reserved1` |  |  |  |
| 14 | `SE.PAR.RECORD.STATUS` | `SeatParameter_RecordStatus` | String |  |  |
| 15 | `SE.PAR.CURR.NO` | `SeatParameter_CurrNo` | String |  |  |
| 16 | `SE.PAR.INPUTTER` | `SeatParameter_Inputter` |  |  |  |
| 17 | `SE.PAR.DATE.TIME` | `SeatParameter_DateTime` |  |  |  |
| 18 | `SE.PAR.AUTHORISER` | `SeatParameter_Authoriser` | String |  |  |
| 19 | `SE.PAR.CO.CODE` | `SeatParameter_CoCode` | String |  |  |
| 20 | `SE.PAR.DEPT.CODE` | `SeatParameter_DeptCode` | String |  |  |
| 21 | `SE.PAR.AUDITOR.CODE` | `SeatParameter_AuditorCode` | String |  |  |
| 22 | `SE.PAR.AUDIT.DATE.TIME` | `SeatParameter_AuditDateTime` | String |  |  |
