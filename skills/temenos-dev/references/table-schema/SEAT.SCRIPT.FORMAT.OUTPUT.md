# SEAT.SCRIPT.FORMAT.OUTPUT — Table Schema

> Source: `INSERTS/I_F.SEAT.SCRIPT.FORMAT.OUTPUT` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.SFO.DESCRIPT` | `SeatScriptFormatOutput_Descript` |  |  |  |
| 2 | `SE.SFO.APPLICATION` | `SeatScriptFormatOutput_Application` | TField | Yes | The Application to which input is done by the script. This value is also obtained from SEAT.SCRIPTS record for that particular script id which is also the Format Output record ID.Its an mandatory field. This field can have any Alphanumeric characters. |
| 3 | `SE.SFO.REFERENCE` | `SeatScriptFormatOutput_Reference` | TField |  | This field holds the Transaction id(Enquiry Report Name) for that particular script which is obtained from that SEAT.SCRIPTS record.For Deal Slip messgaes this will be the Script ID itself. This field can have any Alphanumeric characters. |
| 4 | `SE.SFO.FIELD.DETAILS` | `SeatScriptFormatOutput_FieldDetails` | TField |  | This field holds the fields names from the ENQUIRIES that are displayed in the report (when we launch the enquiry)as its value. This values are obtained from OFS.OUT.MSG has the values for this Enquiry reports. This field can have any Alphabetic characters. |
| 5 | `SE.SFO.LINE.AND.COLMN` | `SeatScriptFormatOutput_LineAndColmn` |  |  |  |
| 6 | `SE.SFO.ACTUAL.VALUE` | `SeatScriptFormatOutput_ActualValue` |  |  |  |
| 7 | `SE.SFO.EXPECTED.VALUE` | `SeatScriptFormatOutput_ExpectedValue` |  |  |  |
| 8 | `SE.SFO.RESULT` | `SeatScriptFormatOutput_Result` |  |  |  |
| 9 | `SE.SFO.RESERVED.4` | `SeatScriptFormatOutput_Reserved4` |  |  |  |
| 10 | `SE.SFO.DEFAULT.VALUE` | `SeatScriptFormatOutput_DefaultValue` | TField |  | This field can have the value as 'Y' or null. When the value is set to 'Y' the values in the field EXPECTED.VALUE are copied to the value of ACTUAL.VALUE field. This field can have only 'Y' or 'N'. |
| 11 | `SE.SFO.OVERALL.RESULT` | `SeatScriptFormatOutput_OverallResult` | TField |  | This field is populated with 'ERROR', when any of the RESULTS field in the multi value set is populated as 'ERROR'.Based on this field we can conclude whether there is any mismatch in the EXPECTED.VALUE and ACTUAL.VALUE fields which is updated during the 'RECORD' and 'TEST' options. This is an NOINPUT field.This field can have any Alphanumeric characters. |
| 12 | `SE.SFO.UPLOAD.TAG` | `SeatScriptFormatOutput_UploadTag` |  |  |  |
| 13 | `SE.SFO.CREATED.DATE` | `SeatScriptFormatOutput_CreatedDate` | TField |  | This field will get updated with the Date on which the SEAT.SCRIPT.FORMAT.OUTPUT record was created and uploaded to the master. This is an NOINPUT field. Only Dates can be defined as value for this field |
| 14 | `SE.SFO.LAST.MODIFIED.DATE` | `SeatScriptFormatOutput_LastModifiedDate` | TField |  | This field will get updated with the Date on which the SEAT.SCRIPT.FORMAT.OUTPUT reocrd was modified and uploaded to the master. This is an NOINPUT field. Only Dates can be defined as value for this field |
| 15 | `SE.SFO.LOCAL.REF` | `SeatScriptFormatOutput_LocalRef` |  |  |  |
| 16 | `SE.SFO.OVERRIDE` | `SeatScriptFormatOutput_Override` |  |  |  |
| 17 | `SE.SFO.RECORD.STATUS` | `SeatScriptFormatOutput_RecordStatus` | String |  |  |
| 18 | `SE.SFO.CURR.NO` | `SeatScriptFormatOutput_CurrNo` | String |  |  |
| 19 | `SE.SFO.INPUTTER` | `SeatScriptFormatOutput_Inputter` |  |  |  |
| 20 | `SE.SFO.DATE.TIME` | `SeatScriptFormatOutput_DateTime` |  |  |  |
| 21 | `SE.SFO.AUTHORISER` | `SeatScriptFormatOutput_Authoriser` | String |  |  |
| 22 | `SE.SFO.CO.CODE` | `SeatScriptFormatOutput_CoCode` | String |  |  |
| 23 | `SE.SFO.DEPT.CODE` | `SeatScriptFormatOutput_DeptCode` | String |  |  |
| 24 | `SE.SFO.AUDITOR.CODE` | `SeatScriptFormatOutput_AuditorCode` | String |  |  |
| 25 | `SE.SFO.AUDIT.DATE.TIME` | `SeatScriptFormatOutput_AuditDateTime` | String |  |  |
