# CA.CLEARING.DIRECTORY.PARAM — Table Schema

> Source: `INSERTS/I_F.CA.CLEARING.DIRECTORY.PARAM` in `CA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CA.CDP.REACHABILITY.KEY.FIELDS` | `CaClearingDirectoryParam_ReachabilityKeyFields` |  |  |  |
| 2 | `CA.CDP.MAX.DAYS.IN.ADVANCE` | `CaClearingDirectoryParam_MaxDaysInAdvance` | TField |  | This field is used to store the max number of days that is added to the creation date in order to determine the effective month of the directory. Additional logic is used to determine the effective date within that month. For a clearing this will apply to the creation date to determine the effective month and then ultimately the effective date EX: 9W - 9 Working Days or 9C - 9 Calendar days |
| 3 | `CA.CDP.REACHABILITY.API` | `CaClearingDirectoryParam_ReachabilityApi` | TField |  | This field is used to store the name of Reachability API for the Clearing Directory provider. |
| 4 | `CA.CDP.VALIDATION.API` | `CaClearingDirectoryParam_ValidationApi` | TField |  | This field is used to store the name of the Validation API, which is used to perform any local validations. |
| 5 | `CA.CDP.LAST.UPLOAD.DATE` | `CaClearingDirectoryParam_LastUploadDate` | TField |  | This field is used to store the T24 current business date at the time when the most recent upload started. This will be updated at the end of the upload process. |
| 6 | `CA.CDP.LAST.EFFECTIVE.DATE` | `CaClearingDirectoryParam_LastEffectiveDate` | TField |  | This field is used to store the effective date of the most recent uploaded file. This will be updated at the end of the upload process. |
| 7 | `CA.CDP.LAST.SOURCE.FILE.NAME` | `CaClearingDirectoryParam_LastSourceFileName` | TField |  | This field is used to store the name of the most recent uploaded file. This will be updated at the end of the upload process. |
| 8 | `CA.CDP.LOCAL.REF` | `CaClearingDirectoryParam_LocalRef` |  |  |  |
| 9 | `CA.CDP.REQUEST.SOURCE` | `CaClearingDirectoryParam_RequestSource` |  |  |  |
| 10 | `CA.CDP.APPLICATION.TABLE` | `CaClearingDirectoryParam_ApplicationTable` |  |  |  |
| 11 | `CA.CDP.FIELD.NAME` | `CaClearingDirectoryParam_FieldName` |  |  |  |
| 12 | `CA.CDP.ROUTINE` | `CaClearingDirectoryParam_Routine` |  |  |  |
| 13 | `CA.CDP.DIRECTORY.FIELD` | `CaClearingDirectoryParam_DirectoryField` |  |  |  |
| 14 | `CA.CDP.VALIDITY.OFFSET.DAYS` | `CaClearingDirectoryParam_ValidityOffsetDays` | TField |  | Number of days to be offset (added) to start date of the directory record to arrive at end date. Usage of this parameter (in the respective upload API) is purely determined by specific requirement for the given clearing. |
| 15 | `CA.CDP.RESERVED.4` | `CaClearingDirectoryParam_Reserved4` |  |  |  |
| 16 | `CA.CDP.RESERVED.3` | `CaClearingDirectoryParam_Reserved3` | TField |  |  |
| 17 | `CA.CDP.RESERVED.2` | `CaClearingDirectoryParam_Reserved2` | TField |  |  |
| 18 | `CA.CDP.RESERVED.1` | `CaClearingDirectoryParam_Reserved1` | TField |  |  |
| 19 | `CA.CDP.OVERRIDE` | `CaClearingDirectoryParam_Override` |  |  |  |
| 20 | `CA.CDP.RECORD.STATUS` | `CaClearingDirectoryParam_RecordStatus` | String |  |  |
| 21 | `CA.CDP.CURR.NO` | `CaClearingDirectoryParam_CurrNo` | String |  |  |
| 22 | `CA.CDP.INPUTTER` | `CaClearingDirectoryParam_Inputter` |  |  |  |
| 23 | `CA.CDP.DATE.TIME` | `CaClearingDirectoryParam_DateTime` |  |  |  |
| 24 | `CA.CDP.AUTHORISER` | `CaClearingDirectoryParam_Authoriser` | String |  |  |
| 25 | `CA.CDP.CO.CODE` | `CaClearingDirectoryParam_CoCode` | String |  |  |
| 26 | `CA.CDP.DEPT.CODE` | `CaClearingDirectoryParam_DeptCode` | String |  |  |
| 27 | `CA.CDP.AUDITOR.CODE` | `CaClearingDirectoryParam_AuditorCode` | String |  |  |
| 28 | `CA.CDP.AUDIT.DATE.TIME` | `CaClearingDirectoryParam_AuditDateTime` | String |  |  |
| 29 | `CA.CDP.OPERAND` | `CaClearingDirectoryParam_Operand` |  |  |  |
