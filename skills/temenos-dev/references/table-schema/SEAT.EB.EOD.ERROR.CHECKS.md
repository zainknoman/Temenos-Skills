# SEAT.EB.EOD.ERROR.CHECKS — Table Schema

> Source: `INSERTS/I_F.SEAT.EB.EOD.ERROR.CHECKS` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.ERR.CHK.ERROR.MSG` | `SeatEbEodErrorChecks_ErrorMsg` | TField |  |  |
| 2 | `SE.ERR.CHK.SCRIPT.REFERENCE` | `SeatEbEodErrorChecks_ScriptReference` | TField |  |  |
| 3 | `SE.ERR.CHK.RESERVED.9` | `SeatEbEodErrorChecks_Reserved9` | TField |  |  |
| 4 | `SE.ERR.CHK.RESERVED.8` | `SeatEbEodErrorChecks_Reserved8` | TField |  |  |
| 5 | `SE.ERR.CHK.RESERVED.7` | `SeatEbEodErrorChecks_Reserved7` | TField |  |  |
| 6 | `SE.ERR.CHK.RESERVED.6` | `SeatEbEodErrorChecks_Reserved6` | TField |  |  |
| 7 | `SE.ERR.CHK.RESERVED.5` | `SeatEbEodErrorChecks_Reserved5` | TField |  |  |
| 8 | `SE.ERR.CHK.RESERVED.4` | `SeatEbEodErrorChecks_Reserved4` | TField |  |  |
| 9 | `SE.ERR.CHK.RESERVED.3` | `SeatEbEodErrorChecks_Reserved3` | TField |  |  |
| 10 | `SE.ERR.CHK.RESERVED.2` | `SeatEbEodErrorChecks_Reserved2` | TField |  |  |
| 11 | `SE.ERR.CHK.RESERVED.1` | `SeatEbEodErrorChecks_Reserved1` | TField |  |  |
| 12 | `SE.ERR.CHK.RECORD.STATUS` | `SeatEbEodErrorChecks_RecordStatus` | String |  |  |
| 13 | `SE.ERR.CHK.CURR.NO` | `SeatEbEodErrorChecks_CurrNo` | String |  |  |
| 14 | `SE.ERR.CHK.INPUTTER` | `SeatEbEodErrorChecks_Inputter` |  |  |  |
| 15 | `SE.ERR.CHK.DATE.TIME` | `SeatEbEodErrorChecks_DateTime` |  |  |  |
| 16 | `SE.ERR.CHK.AUTHORISER` | `SeatEbEodErrorChecks_Authoriser` | String |  |  |
| 17 | `SE.ERR.CHK.CO.CODE` | `SeatEbEodErrorChecks_CoCode` | String |  |  |
| 18 | `SE.ERR.CHK.DEPT.CODE` | `SeatEbEodErrorChecks_DeptCode` | String |  |  |
| 19 | `SE.ERR.CHK.AUDITOR.CODE` | `SeatEbEodErrorChecks_AuditorCode` | String |  |  |
| 20 | `SE.ERR.CHK.AUDIT.DATE.TIME` | `SeatEbEodErrorChecks_AuditDateTime` | String |  |  |
