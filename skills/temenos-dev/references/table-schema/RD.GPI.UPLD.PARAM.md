# RD.GPI.UPLD.PARAM — Table Schema

> Source: `INSERTS/I_F.RD.GPI.UPLD.PARAM` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RD.GPIPAR.DESCRIPTION` | `RdGpiUpldParam_Description` |  |  |  |
| 2 | `RD.GPIPAR.ACTION` | `RdGpiUpldParam_Action` | TField |  | Field to decide what needs to be done while uploading Swift file. When the action is 'OVERWRITE' - We clear all the records. When the action is 'UPDATE' - We dont clear any records. Just update the records. |
| 3 | `RD.GPIPAR.UPLOAD.TYPE` | `RdGpiUpldParam_UploadType` | TField | Yes | Indicates if the uploaded file is the one indicated by the user or the process picks the file(s) automatically based on the upload rules. If Automated, the system will check the available files and will start to upload them according to the upload rules. Either the File Name Format or File Name Format API is mandatory when this option is chosen. If Manual, the system will only upload the file indicated by the user. The File Name is mandatory for this option. |
| 4 | `RD.GPIPAR.FILE.TYPE` | `RdGpiUpldParam_FileType` | TField |  | This field will indicate the type of file which is going to be uploaded. It will include three options 1) Daily Delta 2) Monthly Delta 3) Monthly Full |
| 5 | `RD.GPIPAR.FILE.LOCATION` | `RdGpiUpldParam_FileLocation` | TField | Yes | A Mandatory field to specify the location of GPI file. Validation Rules: A maximum of 255 characters can be entered. |
| 6 | `RD.GPIPAR.FILE.NAME` | `RdGpiUpldParam_FileName` | TField |  | Holds the file name of GPI that is downloaded from swift. Validation Rules: A maximum of 255 characters can be entered. |
| 7 | `RD.GPIPAR.DELIMITER` | `RdGpiUpldParam_Delimiter` | TField | Yes | A Mandatory field to indicate the delimiter option available in Swift file. Options available are 'Comma' and 'Tab'. |
| 8 | `RD.GPIPAR.ACT.ON.MISS.FILE` | `RdGpiUpldParam_ActOnMissFile` | TField |  | Will indicate what actions to take when a file is missing - Stop - if the current file is not found the process will stop Skip - if the current file is not found the process will continue with the next available file |
| 9 | `RD.GPIPAR.FILE.NAME.PATTERN` | `RdGpiUpldParam_FileNamePattern` | TField |  | This field defines the naming convention of the file(s) that will be uploaded. Should be in line with the option in the File Type and match with pattern provided by Swift to identify Publication Date. Examples: GPI_V1_DAILY_DELTA_&lt;yyyymmdd&gt;.txt GPI_V1_MONTHLY_DELTA_&lt;yyyymmdd&gt;.txt GPI_V1_MONTHLY_FULL_&lt;yyyymmdd&gt;.txt GPI*DELTA_&lt;yyyymmdd&gt;* Where * represents any character, yyyymmdd represents a date |
| 10 | `RD.GPIPAR.FILE.NAME.PTRN.API` | `RdGpiUpldParam_FileNamePtrnApi` | TField |  | Local API to determine which file(s) should be picked for processing. This API should contains 4 arguments as below - Argument1 :IN - RD.SWIFT.GPI.DIR record ID Argument2(1) :OUT - FileName Argument2(2) :OUT - FileNameFormat Argument3, Argument4 - Reserved for future use |
| 11 | `RD.GPIPAR.LST.PUBLICATION.DATE` | `RdGpiUpldParam_LstPublicationDate` | TField |  | Date of the last publication file which has been uploaded. Only files after this date will be considered for automatic upload. |
| 12 | `RD.GPIPAR.ARCHIVE.FILE.LOCATION` | `RdGpiUpldParam_ArchiveFileLocation` | TField |  | This field defines the Archive location to where the uploaded file has to be moved post processing. If no path is specified, file will be deleted. |
| 13 | `RD.GPIPAR.LCL.VALIDATION.API` | `RdGpiUpldParam_LclValidationApi` | TField |  | This field allow the local API to add additional validation to decide if a record/line in the file should be uploaded in the directory, basically to include additional validation. This API should contain 5 arguments as below - Argument1 :IN - RD.SWIFT.GPI.DIR record ID Argument2 :IN - RD.SWIFT.GPI.DIR Record Argument3 :OUT = 1/0 . 1 to include the record. 0 to skip the record Argument4, Argument5 - Reserved for future use |
| 14 | `RD.GPIPAR.MAPPING.API` | `RdGpiUpldParam_MappingApi` | TField |  | Local API to indicate the mapping logic to be used to map the details from the uploaded file in the directory. This field is used when Bank is using different sources for reference data than the SWIFTRef GPI directory. This API should contain 4 arguments as below - Argument1 :IN - RD.SWIFT.GPI.DIR record ID Argument2 :INOUT = RD.SWIFT.GPI.DIR Record as input and output to send modified record Argument3, Argument4 - Reserved for future use |
| 15 | `RD.GPIPAR.RESERVED.10` | `RdGpiUpldParam_Reserved10` | TField |  |  |
| 16 | `RD.GPIPAR.RESERVED.9` | `RdGpiUpldParam_Reserved9` | TField |  |  |
| 17 | `RD.GPIPAR.RESERVED.8` | `RdGpiUpldParam_Reserved8` | TField |  |  |
| 18 | `RD.GPIPAR.RESERVED.7` | `RdGpiUpldParam_Reserved7` | TField |  |  |
| 19 | `RD.GPIPAR.RESERVED.6` | `RdGpiUpldParam_Reserved6` | TField |  |  |
| 20 | `RD.GPIPAR.RESERVED.5` | `RdGpiUpldParam_Reserved5` | TField |  |  |
| 21 | `RD.GPIPAR.RESERVED.4` | `RdGpiUpldParam_Reserved4` | TField |  |  |
| 22 | `RD.GPIPAR.RESERVED.3` | `RdGpiUpldParam_Reserved3` | TField |  |  |
| 23 | `RD.GPIPAR.RESERVED.2` | `RdGpiUpldParam_Reserved2` | TField |  |  |
| 24 | `RD.GPIPAR.RESERVED.1` | `RdGpiUpldParam_Reserved1` | TField |  |  |
| 25 | `RD.GPIPAR.LOCAL.REF` | `RdGpiUpldParam_LocalRef` |  |  |  |
| 26 | `RD.GPIPAR.OVERRIDE` | `RdGpiUpldParam_Override` |  |  |  |
| 27 | `RD.GPIPAR.RECORD.STATUS` | `RdGpiUpldParam_RecordStatus` | String |  |  |
| 28 | `RD.GPIPAR.CURR.NO` | `RdGpiUpldParam_CurrNo` | String |  |  |
| 29 | `RD.GPIPAR.INPUTTER` | `RdGpiUpldParam_Inputter` |  |  |  |
| 30 | `RD.GPIPAR.DATE.TIME` | `RdGpiUpldParam_DateTime` |  |  |  |
| 31 | `RD.GPIPAR.AUTHORISER` | `RdGpiUpldParam_Authoriser` | String |  |  |
| 32 | `RD.GPIPAR.CO.CODE` | `RdGpiUpldParam_CoCode` | String |  |  |
| 33 | `RD.GPIPAR.DEPT.CODE` | `RdGpiUpldParam_DeptCode` | String |  |  |
| 34 | `RD.GPIPAR.AUDITOR.CODE` | `RdGpiUpldParam_AuditorCode` | String |  |  |
| 35 | `RD.GPIPAR.AUDIT.DATE.TIME` | `RdGpiUpldParam_AuditDateTime` | String |  |  |
