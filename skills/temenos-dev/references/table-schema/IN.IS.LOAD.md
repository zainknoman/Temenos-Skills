# IN.IS.LOAD — Table Schema

> Source: `INSERTS/I_F.IN.IS.LOAD` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.IS.LOAD.DESCRIPTION` | `InIsLoad_Description` |  |  |  |
| 2 | `IN.IS.LOAD.FILE.NAME` | `InIsLoad_FileName` | TField |  | Holds the file name of IBAN structure that is downloaded from swift. Validation Rules: A maximum of 35 characters can be entered. |
| 3 | `IN.IS.LOAD.FILE.PATH` | `InIsLoad_FilePath` | TField |  | Specifies the location of IBAN structure file. Validation Rules: A maximum of 35 characters can be entered. |
| 4 | `IN.IS.LOAD.DELIMITER` | `InIsLoad_Delimiter` | TField | Yes | A Mandatory field to indicate the delimiter option available in Swift file. Options available are 'Comma' and 'Tab'. |
| 5 | `IN.IS.LOAD.ACTION` | `InIsLoad_Action` | TField |  | Field to decide what needs to be done while uploading Swift file. When the action is 'OVERWRITE' - We clear all the existing records from both live and history tables as well. When the action is 'UPDATE' - We dont clear any records. Just update the records. |
| 6 | `IN.IS.LOAD.LAST.PUBLICATION.DATE` | `InIsLoad_LastPublicationDate` | TField |  | Field to hold date when ,the swift file has been uploaded successfully. To upload records field should be null, and after successful upload it will be defaulted to respective date. |
| 7 | `IN.IS.LOAD.RESERVED.3` | `InIsLoad_Reserved3` | TField |  |  |
| 8 | `IN.IS.LOAD.RESERVED.2` | `InIsLoad_Reserved2` | TField |  |  |
| 9 | `IN.IS.LOAD.RESERVED.1` | `InIsLoad_Reserved1` | TField |  |  |
| 10 | `IN.IS.LOAD.RECORD.STATUS` | `InIsLoad_RecordStatus` | String |  |  |
| 11 | `IN.IS.LOAD.CURR.NO` | `InIsLoad_CurrNo` | String |  |  |
| 12 | `IN.IS.LOAD.INPUTTER` | `InIsLoad_Inputter` |  |  |  |
| 13 | `IN.IS.LOAD.DATE.TIME` | `InIsLoad_DateTime` |  |  |  |
| 14 | `IN.IS.LOAD.AUTHORISER` | `InIsLoad_Authoriser` | String |  |  |
| 15 | `IN.IS.LOAD.CO.CODE` | `InIsLoad_CoCode` | String |  |  |
| 16 | `IN.IS.LOAD.DEPT.CODE` | `InIsLoad_DeptCode` | String |  |  |
| 17 | `IN.IS.LOAD.AUDITOR.CODE` | `InIsLoad_AuditorCode` | String |  |  |
| 18 | `IN.IS.LOAD.AUDIT.DATE.TIME` | `InIsLoad_AuditDateTime` | String |  |  |
