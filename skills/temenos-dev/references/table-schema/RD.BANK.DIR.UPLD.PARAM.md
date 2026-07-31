# RD.BANK.DIR.UPLD.PARAM — Table Schema

> Source: `INSERTS/I_F.RD.BANK.DIR.UPLD.PARAM` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RD.UPLD.DESCRIPTION` | `RdBankDirUpldParam_Description` |  |  |  |
| 2 | `RD.UPLD.ACTION` | `RdBankDirUpldParam_Action` | TField | Yes | The type of action to be performed on the existing records in the Centralised Bank Directory. Validation Rules: This is a mandatory field. Allowed values are UPDATE/OVERWRITE. |
| 3 | `RD.UPLD.UPLOAD.TYPE` | `RdBankDirUpldParam_UploadType` | TField | Yes | Indicates if the uploaded file is the one indicated by the user or the process picks the file(s) automatically based on the upload rules. Validation Rules: This is a mandatory field. Allowed values are AUTOMATED/MANUAL. AUTOMATED : The system will check the available files and will start to upload them according to the upload rules. Either the FILE.NAME.FORMAT or FILE.NAME.FORMAT.API or FILE.NAME is mandatory when this option is chosen. MANUAL: The system will only upload the file indicated by the user. The FILE.NAME is mandatory for this option. |
| 4 | `RD.UPLD.FILE.TYPE` | `RdBankDirUpldParam_FileType` | TField |  | Indicates the type of file to upload. Applicable for automatic uploads. Validation Rules: Allowed values are DAILY.DELTA, MONTHLY.DELTA, MONTHLY.FULL. |
| 5 | `RD.UPLD.FILE.LOCATION` | `RdBankDirUpldParam_FileLocation` | TField | Yes | The folder from where the files will be picked. Validation Rules: This is a mandatory field. Should be valid location. |
| 6 | `RD.UPLD.FILE.NAME` | `RdBankDirUpldParam_FileName` | TField | Yes | The file name which will be picked. Validation Rules: This is a mandatory field. when UPLOAD.TYPE is MANUAL. |
| 7 | `RD.UPLD.DELIMITER` | `RdBankDirUpldParam_Delimiter` | TField |  | SWIFTRef Bank Directory Plus file field delimiter character. Validation Rules: Allowed values are TAB and COMMA. |
| 8 | `RD.UPLD.ACT.ON.MISS.FILE` | `RdBankDirUpldParam_ActOnMissFile` | TField |  | Will indicate what actions will take the process when a file is missing. Validation Rules: Allowed values are STOP and SKIP. STOP : if the next file is not found the process will stop. SKIP : if the next file is not found the process will continue with the next available file. |
| 9 | `RD.UPLD.FILE.NAME.FORMAT` | `RdBankDirUpldParam_FileNameFormat` | TField |  | Should be in line with the option in the File Type and match with pattern provided by Swift to identify Publication DateNaming convention of the file/file(s) which must be uploaded. Example : BANKDIRECTORYPLUS_V3_DELTA_&lt;yyyymmdd&gt;.txt BANKDIRECTORYPLUS*DELTA_&lt;yyyymmdd&gt;* IBANPLUS_V3_FULL_&lt;yyyymmdd&gt;.txt Where * represents any character, &lt;yyyymmdd&gt; represents a date. |
| 10 | `RD.UPLD.FILE.NAME.FORMAT.API` | `RdBankDirUpldParam_FileNameFormatApi` | TField |  | Local API to determine which file should be picked. This API should contains 4 arguments as below Argument1 :IN - RD.BANK.DIR.UPLD.PARAM record ID. Argument2(1) :OUT - FileName. Argument2(2) :OUT - FileNameFormat. Argument3, Argument4 - Reserved for future use. |
| 11 | `RD.UPLD.LAST.PUBLICATION.DATE` | `RdBankDirUpldParam_LastPublicationDate` | TField |  | Date of the last publication file which has been uploaded. Only files after this date will be considered for automatic upload. Validation Rules: Input not allowed.Updated by system for automated upload. |
| 12 | `RD.UPLD.ARCHIVE.FILE.LOCATION` | `RdBankDirUpldParam_ArchiveFileLocation` | TField |  | This field defines the Archive location to where the uploaded file has to be moved post processing. If no path is specified, file will be deleted. |
| 13 | `RD.UPLD.LOCAL.MAPPING.API` | `RdBankDirUpldParam_LocalMappingApi` | TField |  | Local API to indicate the mapping logic to be used to map the details from the uploaded file in the directory. This API should contains 4 arguments as below. Argument1(1) :IN -RD.CENTRAL.BANK.DIR record ID Argument2 :INOUT = RD.CENTRAL.BANK.DIR Record as input and output to send modified record. Argument3, Argument4 - Reserved for future use. |
| 14 | `RD.UPLD.STORE.AS.UPCASE` | `RdBankDirUpldParam_StoreAsUpcase` | TField |  | To capture the set up to store Institution name in upper case. |
| 15 | `RD.UPLD.RESERVED.4` | `RdBankDirUpldParam_Reserved4` | TField |  |  |
| 16 | `RD.UPLD.RESERVED.3` | `RdBankDirUpldParam_Reserved3` | TField |  |  |
| 17 | `RD.UPLD.RESERVED.2` | `RdBankDirUpldParam_Reserved2` | TField |  |  |
| 18 | `RD.UPLD.RESERVED.1` | `RdBankDirUpldParam_Reserved1` | TField |  |  |
| 19 | `RD.UPLD.LOCAL.REF` | `RdBankDirUpldParam_LocalRef` |  |  |  |
| 20 | `RD.UPLD.OVERRIDE` | `RdBankDirUpldParam_Override` |  |  |  |
| 21 | `RD.UPLD.RECORD.STATUS` | `RdBankDirUpldParam_RecordStatus` | String |  |  |
| 22 | `RD.UPLD.CURR.NO` | `RdBankDirUpldParam_CurrNo` | String |  |  |
| 23 | `RD.UPLD.INPUTTER` | `RdBankDirUpldParam_Inputter` |  |  |  |
| 24 | `RD.UPLD.DATE.TIME` | `RdBankDirUpldParam_DateTime` |  |  |  |
| 25 | `RD.UPLD.AUTHORISER` | `RdBankDirUpldParam_Authoriser` | String |  |  |
| 26 | `RD.UPLD.CO.CODE` | `RdBankDirUpldParam_CoCode` | String |  |  |
| 27 | `RD.UPLD.DEPT.CODE` | `RdBankDirUpldParam_DeptCode` | String |  |  |
| 28 | `RD.UPLD.AUDITOR.CODE` | `RdBankDirUpldParam_AuditorCode` | String |  |  |
| 29 | `RD.UPLD.AUDIT.DATE.TIME` | `RdBankDirUpldParam_AuditDateTime` | String |  |  |
