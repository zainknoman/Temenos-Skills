# SEAT.SCRIPT.RESULT.FILES — Table Schema

> Source: `INSERTS/I_F.SEAT.SCRIPT.RESULT.FILES` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SRF.DESCRIPT` | `SeatScriptResultFiles_Descript` |  |  |  |
| 2 | `EB.SRF.APPLICATION` | `SeatScriptResultFiles_Application` | TField |  | A valid Application name. Up to 35 characters of input will be accepted, leading spaces, trailing spaces and duplicated embedded spaces will be removed. |
| 3 | `EB.SRF.TRANSACTION.ID` | `SeatScriptResultFiles_TransactionId` | TField |  | A valid transaction ID of the above application. This is a no input field. |
| 4 | `EB.SRF.TRANSACTION.COMPANY` | `SeatScriptResultFiles_TransactionCompany` | TField |  | Valid company ID.This is a NOINPUT field |
| 5 | `EB.SRF.SCRIPT.FUNCTION` | `SeatScriptResultFiles_ScriptFunction` |  |  |  |
| 6 | `EB.SRF.COB.DATE` | `SeatScriptResultFiles_CobDate` |  |  |  |
| 7 | `EB.SRF.FUNC.DESCRIPTION` | `SeatScriptResultFiles_FuncDescription` |  |  |  |
| 8 | `EB.SRF.RESULT` | `SeatScriptResultFiles_Result` |  |  |  |
| 9 | `EB.SRF.FILE.NAME` | `SeatScriptResultFiles_FileName` |  |  |  |
| 10 | `EB.SRF.REC.ID.MAP` | `SeatScriptResultFiles_RecIdMap` |  |  |  |
| 11 | `EB.SRF.FLD.DEFN.ID` | `SeatScriptResultFiles_FldDefnId` |  |  |  |
| 12 | `EB.SRF.UPDATE.TYPE` | `SeatScriptResultFiles_UpdateType` |  |  |  |
| 13 | `EB.SRF.FILE.BASE.RELEASE` | `SeatScriptResultFiles_FileBaseRelease` |  |  |  |
| 14 | `EB.SRF.JOB.NAME.ID` | `SeatScriptResultFiles_JobNameId` |  |  |  |
| 15 | `EB.SRF.FORMAT.OUTPUT` | `SeatScriptResultFiles_FormatOutput` |  |  |  |
| 16 | `EB.SRF.FORMAT.RESULT` | `SeatScriptResultFiles_FormatResult` |  |  |  |
| 17 | `EB.SRF.OVERALL.RESULT` | `SeatScriptResultFiles_OverallResult` | TField |  | Stores the overall result of the script. This is a noinput field. |
| 18 | `EB.SRF.UPLOAD.TAG` | `SeatScriptResultFiles_UploadTag` |  |  |  |
| 19 | `EB.SRF.CREATED.DATE` | `SeatScriptResultFiles_CreatedDate` | TField |  | This field will get updated with the Date on which the SEAT.SCRIPT.RESULT.FILES record was created and uploaded to the master. This is an NOINPUT field. Only Dates can be defined as value for this field |
| 20 | `EB.SRF.LAST.MODIFIED.DATE` | `SeatScriptResultFiles_LastModifiedDate` | TField |  | This field will get populated with the Date on which the SEAT.SCRIPT.RESULT.FILES reocrd was modified and uploaded to the master. This is an NOINPUT field. Only Dates can be defined as value for this field |
| 21 | `EB.SRF.SCRIPT.ACTIVITY.ID` | `SeatScriptResultFiles_ScriptActivityId` | TField |  | This field stores the associated SSA id and is a NOINPUT field |
| 22 | `EB.SRF.RESERVED.4` | `SeatScriptResultFiles_Reserved4` | TField |  |  |
| 23 | `EB.SRF.RESERVED.3` | `SeatScriptResultFiles_Reserved3` | TField |  |  |
| 24 | `EB.SRF.RESERVED.2` | `SeatScriptResultFiles_Reserved2` | TField |  |  |
| 25 | `EB.SRF.RESERVED.1` | `SeatScriptResultFiles_Reserved1` | TField |  |  |
| 26 | `EB.SRF.LOCAL.REF` | `SeatScriptResultFiles_LocalRef` |  |  |  |
| 27 | `EB.SRF.OVERRIDE` | `SeatScriptResultFiles_Override` |  |  |  |
| 28 | `EB.SRF.RECORD.STATUS` | `SeatScriptResultFiles_RecordStatus` | String |  |  |
| 29 | `EB.SRF.CURR.NO` | `SeatScriptResultFiles_CurrNo` | String |  |  |
| 30 | `EB.SRF.INPUTTER` | `SeatScriptResultFiles_Inputter` |  |  |  |
| 31 | `EB.SRF.DATE.TIME` | `SeatScriptResultFiles_DateTime` |  |  |  |
| 32 | `EB.SRF.AUTHORISER` | `SeatScriptResultFiles_Authoriser` | String |  |  |
| 33 | `EB.SRF.CO.CODE` | `SeatScriptResultFiles_CoCode` | String |  |  |
| 34 | `EB.SRF.DEPT.CODE` | `SeatScriptResultFiles_DeptCode` | String |  |  |
| 35 | `EB.SRF.AUDITOR.CODE` | `SeatScriptResultFiles_AuditorCode` | String |  |  |
| 36 | `EB.SRF.AUDIT.DATE.TIME` | `SeatScriptResultFiles_AuditDateTime` | String |  |  |
| 37 | `EB.SRF.REGRESSION.DAY` | `SeatScriptResultFiles_RegressionDay` |  |  |  |
