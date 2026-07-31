# SEAT.SERVICE.RESULTS.PARAM — Table Schema

> Source: `INSERTS/I_F.SEAT.SERVICE.RESULTS.PARAM` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.SRP.DESCRIPTION` | `SeatServiceResultsParam_Description` |  |  |  |
| 2 | `SE.SRP.FILE.NAME` | `SeatServiceResultsParam_FileName` |  |  |  |
| 3 | `SE.SRP.INC.PROCESS.NAME` | `SeatServiceResultsParam_IncProcessName` |  |  |  |
| 4 | `SE.SRP.EXC.PROCESS.NAME` | `SeatServiceResultsParam_ExcProcessName` |  |  |  |
| 5 | `SE.SRP.KEY.FIELDS` | `SeatServiceResultsParam_KeyFields` |  |  |  |
| 6 | `SE.SRP.SEAT.APPLN.MGR.ID` | `SeatServiceResultsParam_SeatApplnMgrId` | TField |  | This field holds value which is the record ID in the SEAT.APPLICATION.MANAGER file.This field can have any alpabetic characters |
| 7 | `SE.SRP.RESERVED.10` | `SeatServiceResultsParam_Reserved10` | TField |  |  |
| 8 | `SE.SRP.RESERVED.9` | `SeatServiceResultsParam_Reserved9` | TField |  |  |
| 9 | `SE.SRP.RESERVED.8` | `SeatServiceResultsParam_Reserved8` | TField |  |  |
| 10 | `SE.SRP.RESERVED.7` | `SeatServiceResultsParam_Reserved7` | TField |  |  |
| 11 | `SE.SRP.RESERVED.6` | `SeatServiceResultsParam_Reserved6` | TField |  |  |
| 12 | `SE.SRP.RESERVED.5` | `SeatServiceResultsParam_Reserved5` | TField |  |  |
| 13 | `SE.SRP.RESERVED.4` | `SeatServiceResultsParam_Reserved4` | TField |  |  |
| 14 | `SE.SRP.RESERVED.3` | `SeatServiceResultsParam_Reserved3` | TField |  |  |
| 15 | `SE.SRP.RESERVED.2` | `SeatServiceResultsParam_Reserved2` | TField |  |  |
| 16 | `SE.SRP.RESERVED.1` | `SeatServiceResultsParam_Reserved1` | TField |  |  |
| 17 | `SE.SRP.LOCAL.REF` | `SeatServiceResultsParam_LocalRef` |  |  |  |
| 18 | `SE.SRP.OVERRIDE` | `SeatServiceResultsParam_Override` |  |  |  |
| 19 | `SE.SRP.RECORD.STATUS` | `SeatServiceResultsParam_RecordStatus` | String |  |  |
| 20 | `SE.SRP.CURR.NO` | `SeatServiceResultsParam_CurrNo` | String |  |  |
| 21 | `SE.SRP.INPUTTER` | `SeatServiceResultsParam_Inputter` |  |  |  |
| 22 | `SE.SRP.DATE.TIME` | `SeatServiceResultsParam_DateTime` |  |  |  |
| 23 | `SE.SRP.AUTHORISER` | `SeatServiceResultsParam_Authoriser` | String |  |  |
| 24 | `SE.SRP.CO.CODE` | `SeatServiceResultsParam_CoCode` | String |  |  |
| 25 | `SE.SRP.DEPT.CODE` | `SeatServiceResultsParam_DeptCode` | String |  |  |
| 26 | `SE.SRP.AUDITOR.CODE` | `SeatServiceResultsParam_AuditorCode` | String |  |  |
| 27 | `SE.SRP.AUDIT.DATE.TIME` | `SeatServiceResultsParam_AuditDateTime` | String |  |  |
