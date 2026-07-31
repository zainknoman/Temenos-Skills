# IN.EXCLUSION.LIST.LOAD — Table Schema

> Source: `INSERTS/I_F.IN.EXCLUSION.LIST.LOAD` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.EX.LI.LOAD.DESCRIPTION` | `InExclusionListLoad_Description` |  |  |  |
| 2 | `IN.EX.LI.LOAD.FILE.NAME` | `InExclusionListLoad_FileName` | TField |  | Holds the file name of EXCLUSION LIST that is downloaded from swift. Validation Rules: A maximum of 35 characters can be entered. |
| 3 | `IN.EX.LI.LOAD.FILE.PATH` | `InExclusionListLoad_FilePath` | TField |  | Specifies the location of EXCLUSION LIST file. Validation Rules: A maximum of 35 characters can be entered. |
| 4 | `IN.EX.LI.LOAD.DELIMITER` | `InExclusionListLoad_Delimiter` | TField | Yes | A Mandatory field to indicate the delimiter option available in Swift file. Options available are 'Comma' and 'Tab'. |
| 5 | `IN.EX.LI.LOAD.ACTION` | `InExclusionListLoad_Action` | TField |  | Field to decide what needs to be done while uploading Swift file. When the action is 'OVERWRITE' - We clear all the records. When the action is 'UPDATE' - We dont clear any records. Just update the records. |
| 6 | `IN.EX.LI.LOAD.UPLOAD.TYPE` | `InExclusionListLoad_UploadType` | TField | Yes | Indicates if the uploaded file is the one indicated by the user or the process picks the file(s) automatically based on the upload rules. If Automated, the system will check the available files and will start to upload them according to the upload rules. Either the File Name Format or File Name Format API is mandatory when this option is chosen. If Manual, the system will only upload the file indicated by the user. The File Name is mandatory for this option. |
| 7 | `IN.EX.LI.LOAD.FILE.TYPE` | `InExclusionListLoad_FileType` | TField |  | This field will indicate the type of file which is going to be uploaded. It will include three options- 1) Daily Delta 2) Monthly Delta 3) Monthly Full |
| 8 | `IN.EX.LI.LOAD.ACT.ON.MISS.FILE` | `InExclusionListLoad_ActOnMissFile` | TField |  | Will indicate what actions will take the process when a file is missing - Stop - if the next file is not found the process will stop Skip - if the next file is not found the process will continue with the next available file |
| 9 | `IN.EX.LI.LOAD.LAST.PUBLICATION.DATE` | `InExclusionListLoad_LastPublicationDate` | TField |  | Date of the last publication file which has been uploaded. Only files after this date will be considered for automatic upload. For the manual uploads this can be manually updated. |
| 10 | `IN.EX.LI.LOAD.FILE.NAME.FORMAT` | `InExclusionListLoad_FileNameFormat` | TField |  | This field defines the naming convention of the file(s) that will be uploaded. Should be in line with the option in the File Type and match with pattern provided by Swift to identify Publication Date. E.g. IBANPLUS_V3_FULL_yyyymmdd.txt |
| 11 | `IN.EX.LI.LOAD.FILE.NAME.FORMAT.API` | `InExclusionListLoad_FileNameFormatApi` | TField |  | Local API to determine which file(s) should be picked for processing. This API should contains 4 arguments as below - Argument1 :IN - IN.IBAN.PLUS.LOAD/IN.EXCLUSION.LIST.LOAD record ID Argument2(1) :OUT - FileName Argument2(2) :OUT - FileNameFormat Argument3, Argument4 - Reserved for future use |
| 12 | `IN.EX.LI.LOAD.ARCHIVE.FILE.LOCATION` | `InExclusionListLoad_ArchiveFileLocation` | TField |  | This field defines the Archive location to where the uploaded file has to be moved post processing. If no path is specified, file will be deleted. |
| 13 | `IN.EX.LI.LOAD.LOCAL.VALIDATION.API` | `InExclusionListLoad_LocalValidationApi` | TField |  | This field allow the local API to add additional validation to decide if a record/line in the file should be uploaded in the directory, basically to include additional validation. This API should contains 4 arguments as below - Argument1(1) :IN - IN.IBAN.PLUS record ID Argument2 :IN - IN.IBAN.PLUS Record Argument3(1) :OUT = 1/0 . 1 to include the record. 0 to skip the record Argument4, Argument5 - Reserved for future use |
| 14 | `IN.EX.LI.LOAD.LOCAL.MAPPING.API` | `InExclusionListLoad_LocalMappingApi` | TField |  | Local API to indicate the mapping logic to be used to map the details from the uploaded file in the directory. This field is used when Bank is using different sources for reference data than the SWIFTRef IBAN Plus. This API should contains 4 arguments as below - Argument1(1) :IN - IN.IBAN.PLUS record ID Argument2 :INOUT = IN.IBAN.PLUS Record as input and output to send modified record Argument3, Argument4 - Reserved for future use |
| 15 | `IN.EX.LI.LOAD.RECORD.STATUS` | `InExclusionListLoad_RecordStatus` | String |  |  |
| 16 | `IN.EX.LI.LOAD.CURR.NO` | `InExclusionListLoad_CurrNo` | String |  |  |
| 17 | `IN.EX.LI.LOAD.INPUTTER` | `InExclusionListLoad_Inputter` |  |  |  |
| 18 | `IN.EX.LI.LOAD.DATE.TIME` | `InExclusionListLoad_DateTime` |  |  |  |
| 19 | `IN.EX.LI.LOAD.AUTHORISER` | `InExclusionListLoad_Authoriser` | String |  |  |
| 20 | `IN.EX.LI.LOAD.CO.CODE` | `InExclusionListLoad_CoCode` | String |  |  |
| 21 | `IN.EX.LI.LOAD.DEPT.CODE` | `InExclusionListLoad_DeptCode` | String |  |  |
| 22 | `IN.EX.LI.LOAD.AUDITOR.CODE` | `InExclusionListLoad_AuditorCode` | String |  |  |
| 23 | `IN.EX.LI.LOAD.AUDIT.DATE.TIME` | `InExclusionListLoad_AuditDateTime` | String |  |  |
