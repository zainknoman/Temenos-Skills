# SEAT.SCRIPT.FIELD.VALUES — Table Schema

> Source: `INSERTS/I_F.SEAT.SCRIPT.FIELD.VALUES` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SFV.DESCRIPT` | `SeatScriptFieldValues_Descript` |  |  |  |
| 2 | `EB.SFV.RECORD.ID` | `SeatScriptFieldValues_RecordId` | TField |  | Stores the RECORD ID during the upload. It is Automatically updated. No input field. |
| 3 | `EB.SFV.FIELD.NAME` | `SeatScriptFieldValues_FieldName` |  |  |  |
| 4 | `EB.SFV.FLD.BASE.REL` | `SeatScriptFieldValues_FldBaseRel` |  |  |  |
| 5 | `EB.SFV.ACTUAL.VALUE` | `SeatScriptFieldValues_ActualValue` |  |  |  |
| 6 | `EB.SFV.EXPECTED.VALUE` | `SeatScriptFieldValues_ExpectedValue` |  |  |  |
| 7 | `EB.SFV.INDEX.FIELD` | `SeatScriptFieldValues_IndexField` |  |  |  |
| 8 | `EB.SFV.NO.OF.RECORDS` | `SeatScriptFieldValues_NoOfRecords` | TField |  | This field holds the number of instances of this record in the file that are similar to the field values defined. This field can have any Alphanumeric characters. |
| 9 | `EB.SFV.CONCAT.FILE` | `SeatScriptFieldValues_ConcatFile` | TField |  | This field can be set to 'Y', when we needs to check the TABLE type files,such that we can ignore the checks for standard selection Table type template files. This field can be set to 'Y' or 'N' as value. |
| 10 | `EB.SFV.DEFAULT.VALUE` | `SeatScriptFieldValues_DefaultValue` | TField |  | Value can be "Y" or null. Once "Y" is entered while cross validation stage if the EXPECTED.VALUE field is blank it will copy the ACTUAL.VALUE to EXPECTED.VALUE field. Up to 16 characters of input will be accepted, leading spaces, trailing spaces and duplicated embedded spaces will be removed. |
| 11 | `EB.SFV.RESULT` | `SeatScriptFieldValues_Result` | TField |  | This is a no input field. Incase of any error this field will be populated. |
| 12 | `EB.SFV.FILE.MNEMONIC` | `SeatScriptFieldValues_FileMnemonic` | TField |  | This field defines the mnemonic of the file with a maximum of 16 characters. |
| 13 | `EB.SFV.UPLOAD.TAG` | `SeatScriptFieldValues_UploadTag` |  |  |  |
| 14 | `EB.SFV.FILE.CHECK.TYPE` | `SeatScriptFieldValues_FileCheckType` | TField |  |  |
| 15 | `EB.SFV.LAST.MODIFIED.DATE` | `SeatScriptFieldValues_LastModifiedDate` |  |  |  |
| 16 | `EB.SFV.RESULT.FILE.ID` | `SeatScriptFieldValues_ResultFileId` | TField |  | To update RF id associated with FV automatically. No input Field Length upto 29 characters are allowed. |
| 17 | `EB.SFV.LOCAL.REF` | `SeatScriptFieldValues_LocalRef` |  |  |  |
| 18 | `EB.SFV.OVERRIDE` | `SeatScriptFieldValues_Override` |  |  |  |
| 19 | `EB.SFV.RECORD.STATUS` | `SeatScriptFieldValues_RecordStatus` | String |  |  |
| 20 | `EB.SFV.CURR.NO` | `SeatScriptFieldValues_CurrNo` | String |  |  |
| 21 | `EB.SFV.INPUTTER` | `SeatScriptFieldValues_Inputter` |  |  |  |
| 22 | `EB.SFV.DATE.TIME` | `SeatScriptFieldValues_DateTime` |  |  |  |
| 23 | `EB.SFV.AUTHORISER` | `SeatScriptFieldValues_Authoriser` | String |  |  |
| 24 | `EB.SFV.CO.CODE` | `SeatScriptFieldValues_CoCode` | String |  |  |
| 25 | `EB.SFV.DEPT.CODE` | `SeatScriptFieldValues_DeptCode` | String |  |  |
| 26 | `EB.SFV.AUDITOR.CODE` | `SeatScriptFieldValues_AuditorCode` | String |  |  |
| 27 | `EB.SFV.AUDIT.DATE.TIME` | `SeatScriptFieldValues_AuditDateTime` | String |  |  |
| 28 | `EB.SFV.FIELD.VALUES.TYPE` | `SeatScriptFieldValues_FieldValuesType` | TField |  |  |
