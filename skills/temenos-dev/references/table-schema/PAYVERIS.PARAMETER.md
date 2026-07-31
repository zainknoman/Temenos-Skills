# PAYVERIS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PAYVERIS.PARAMETER` in `NAPVPT_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVP.FILE.ID.START.INDEX` | `PayverisParameter_FileIdStartIndex` | TField |  | Start index of Payveris File Identifier in the File Header record. |
| 2 | `PVP.FILE.ID.LENGTH` | `PayverisParameter_FileIdLength` | TField |  | Length of Payveris File Identifier in the File Header record. The File Identifier begins at the start Index and extends upto string length. |
| 3 | `PVP.IN.PATH` | `PayverisParameter_InPath` | TField |  | The UD file path where Payveris files are placed for processing. |
| 4 | `PVP.ARCHIVE.PATH` | `PayverisParameter_ArchivePath` | TField |  | The UD file path where Payveris files will be moved/archived to once processed. |
| 5 | `PVP.ERROR.FILE.PATH` | `PayverisParameter_ErrorFilePath` | TField |  | The UD file path where duplicate Payveris file with same File Identifier will be moved/archived. |
| 6 | `PVP.RESPONSE.PATH` | `PayverisParameter_ResponsePath` | TField |  | Core banking processor consuming the file |
| 7 | `PVP.FILE.ENCODING` | `PayverisParameter_FileEncoding` | TField |  | Default file encoding is UTF-8. File with different encoding such as " |
| 8 | `PVP.PROCESSOR.NAME` | `PayverisParameter_ProcessorName` | TField |  | FI Processor Name. |
| 9 | `PVP.PROCESSOR.ID` | `PayverisParameter_ProcessorId` | TField |  | Assigned by Payveris |
| 10 | `PVP.BULKING.PARAMETER` | `PayverisParameter_BulkingParameter` | TField |  | Number of records to load from file in a single sequential iteration |
| 11 | `PVP.ACCOUNTS.FILE.PATH` | `PayverisParameter_AccountsFilePath` | TField |  | The UD file path where Payveris accounts extract file will be placed. |
| 12 | `PVP.ORIGINATOR.ID` | `PayverisParameter_OriginatorId` | TField |  | Originator Identifier assigned by Payveris |
| 13 | `PVP.FI.ID` | `PayverisParameter_FiId` | TField |  | Financial Institution Identifier assigned by Payveris |
| 14 | `PVP.FI.NAME` | `PayverisParameter_FiName` | TField |  | Financial Institution Name |
| 15 | `PVP.RECORD.STATUS` | `PayverisParameter_RecordStatus` | String |  |  |
| 16 | `PVP.CURR.NO` | `PayverisParameter_CurrNo` | String |  |  |
| 17 | `PVP.INPUTTER` | `PayverisParameter_Inputter` |  |  |  |
| 18 | `PVP.DATE.TIME` | `PayverisParameter_DateTime` |  |  |  |
| 19 | `PVP.AUTHORISER` | `PayverisParameter_Authoriser` | String |  |  |
| 20 | `PVP.CO.CODE` | `PayverisParameter_CoCode` | String |  |  |
| 21 | `PVP.DEPT.CODE` | `PayverisParameter_DeptCode` | String |  |  |
| 22 | `PVP.AUDITOR.CODE` | `PayverisParameter_AuditorCode` | String |  |  |
| 23 | `PVP.AUDIT.DATE.TIME` | `PayverisParameter_AuditDateTime` | String |  |  |
