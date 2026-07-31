# WR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.WR.PARAMETER` in `WR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WR.PAR.T24.REPORTING.FILE` | `WrParameter_T24ReportingFile` | TField |  | This is the filename for the path to which the reports will be written for extraction to T24 Client Reporting. If the 'Retain Hardcopy' option has not been taken, the data in this directory will be deleted up to the day previous to the report run, each time the reports are run. However, note that if the output path is changed, the data in the old directory will need to be manually deleted.Alternatively a valid path can be given.Do not use relative paths. |
| 2 | `WR.PAR.T24.REPORTING.PATH` | `WrParameter_T24ReportingPath` | TField |  | This is the path (or table name) to which the reports will be written for extraction to T24 Client Reporting. If the 'Retain Hardcopy' option has not been taken, the data in this directory will be deleted up to the day previous to the report run, each time the reports are run. However, note that if the output path is changed, the data in the old directory will need to be manually deleted. Defaulted as absolute path from T24 Reporting File. |
| 3 | `WR.PAR.T24.REPORTING.DIR` | `WrParameter_T24ReportingDir` | TField |  | This is the samba name for the location pointed to by the T24 Reporting Path. |
| 4 | `WR.PAR.RETAIN.HARDCOPY` | `WrParameter_RetainHardcopy` | TField |  | Denotes whether the 'hardcopy' report details in the HOLD file should be kept after production of .csv formatted output. If this field is set to 'Y' they are retained until manually removed. This field also controls deletion of report details in WR.ENQUIRY.WORKFILE and removes historic data in the directory detailed in 'Output Path'. |
| 5 | `WR.PAR.TIMESTAMP.STYLE` | `WrParameter_TimestampStyle` | TField |  | Style of timestamp used within the records being communicated between T24 and T24 Client Reporting. |
| 6 | `WR.PAR.CR.ADDRESS` | `WrParameter_CrAddress` | TField |  | This is the ip adress or hostname/fully qualified domain name for the T24 Client Reporting listener |
| 7 | `WR.PAR.CR.PORT` | `WrParameter_CrPort` | TField |  | This is the port for the T24 Client Reporting listener |
| 8 | `WR.PAR.CR.TIMEOUT` | `WrParameter_CrTimeout` | TField |  | This is the timeout in milliseconds for the socket connection to the T24 Client Reporting listener |
| 9 | `WR.PAR.REP.DOCUMENT.FILE` | `WrParameter_RepDocumentFile` | TField |  | This is the filename for the path to which the report documents will be delivered. Alternatively a valid path can be given.Do not use relative paths. |
| 10 | `WR.PAR.REP.DOCUMENT.PATH` | `WrParameter_RepDocumentPath` | TField |  | This is the path to which the report documents will be delivered. Defaulted as absolute path from Rep Document File. |
| 11 | `WR.PAR.REP.DOCUMENT.DIR` | `WrParameter_RepDocumentDir` | TField |  | This is the samba name for the location pointed to by the Report Document Path. If an Image Type is specified in the 'Image Type' field, and the samba name given in this field does not match the contents of the 'Path' field, and override message will be displayed warning that the path will be updated in IM.IMAGE.TYPE. On accepting the override, the path will be reset in the IM.IMAGE.TYPE record. |
| 12 | `WR.PAR.ERROR.LOG.FILE` | `WrParameter_ErrorLogFile` | TField |  | This is the filename for the path to which any errors found during production of reports should be logged. Alternatively a valid path can be given.Do not use relative paths. |
| 13 | `WR.PAR.ERROR.LOG.PATH` | `WrParameter_ErrorLogPath` | TField |  | This is the path to which any errors found during production of reports should be logged. Defaulted as absolute path from Error Log File. |
| 14 | `WR.PAR.ERROR.LOG.DIR` | `WrParameter_ErrorLogDir` | TField |  | This is the samba name for the location pointed to by the Error Log Path. |
| 15 | `WR.PAR.IMAGE.TYPE` | `WrParameter_ImageType` | TField |  | This is the T24 image type we should use to store the report documents. This should be a valid record in IM.IMAGE.TYPE. |
| 16 | `WR.PAR.DATA.ARCHIVING` | `WrParameter_DataArchiving` | TField |  | Determines whether the to delete or archive the communications history between T24 and T24 Client Reporting. |
| 17 | `WR.PAR.DATA.ARCHIVE.FILE` | `WrParameter_DataArchiveFile` | TField |  | This is the filename for the path to which archived communications history will be posted (if Data Archiving is set to 'Archive'). Alternatively a valid path can be given.Do not use relative paths. |
| 18 | `WR.PAR.DATA.ARCHIVE.PATH` | `WrParameter_DataArchivePath` | TField |  | This is the path to which archived communications history will be posted (if Data Archiving is set to 'Archive'). Defaulted as absolute path from Data Archive File. |
| 19 | `WR.PAR.DATA.ARCHIVE.DIR` | `WrParameter_DataArchiveDir` | TField |  | This is the samba name for the location pointed to by the Data Archive Path. |
| 20 | `WR.PAR.REPORTING.ACTIVE` | `WrParameter_ReportingActive` | TField |  | Determines whether automated periodic reporting as run during the WR.REPORTING COB process is active or not. Unless this checkbox is populated, there will be no production of WR reports nor any initialisation signal to T24 Private Wealth Management Client Reporting module. However, historic report records will still be cleared unless the 'Retain Hardcopy' checkbox has been selected. |
| 21 | `WR.PAR.PROCESS.IDENTIFIER` | `WrParameter_ProcessIdentifier` | TField |  | This is the Process Identifier to send to the T24 Client Reporting listener as part of the initialisation message.The value in this field should match exactly with the value shown against the corresponding procedure in the T24 Client Reporting module. |
| 22 | `WR.PAR.REP.TIME` | `WrParameter_RepTime` | TField |  | This field is for internal use only, and temporarily holds the time at which the WR COB report generation started. |
| 23 | `WR.PAR.CSV.COL.DELIMITER` | `WrParameter_CsvColDelimiter` | TField |  | The delimiter to use between columns in the CSV output.Standard CSV tables use a comma (,) as the separator, however this is not recommended, as some data in T24 that will be reported upon (for example descriptive fields) may contain commas.Therefore, the default separator for T24 Client Reporting is the pipe symbol (\|). This is set as default when first amending this record.If a different separator is required, the T24 Client Reporting module will need to be configured accordingly.This field can not be changed once set. |
| 24 | `WR.PAR.CSV.ROW.DELIMITER` | `WrParameter_CsvRowDelimiter` | TField |  | The delimiter to use between rows in the CSV output.Standard CSV tables use a line feed as the separator. The default row delimiter is a line feed. If left blank, a line feed is used as the separator.If a different separator is required, the T24 Client Reporting module will need to be configured accordingly.This field can not be changed once set. |
| 25 | `WR.PAR.DFLT.REPORT` | `WrParameter_DfltReport` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 26 | `WR.PAR.DFLT.RPT.STYLE` | `WrParameter_DfltRptStyle` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 27 | `WR.PAR.GET.CUS.LOCAL` | `WrParameter_GetCusLocal` |  |  |  |
| 28 | `WR.PAR.RESERVED.02` | `WrParameter_Reserved02` | TField |  |  |
| 29 | `WR.PAR.RESERVED.01` | `WrParameter_Reserved01` | TField |  |  |
| 30 | `WR.PAR.LOCAL.REF` | `WrParameter_LocalRef` |  |  |  |
| 31 | `WR.PAR.OVERRIDE` | `WrParameter_Override` |  |  |  |
| 32 | `WR.PAR.RECORD.STATUS` | `WrParameter_RecordStatus` | String |  |  |
| 33 | `WR.PAR.CURR.NO` | `WrParameter_CurrNo` | String |  |  |
| 34 | `WR.PAR.INPUTTER` | `WrParameter_Inputter` |  |  |  |
| 35 | `WR.PAR.DATE.TIME` | `WrParameter_DateTime` |  |  |  |
| 36 | `WR.PAR.AUTHORISER` | `WrParameter_Authoriser` | String |  |  |
| 37 | `WR.PAR.CO.CODE` | `WrParameter_CoCode` | String |  |  |
| 38 | `WR.PAR.DEPT.CODE` | `WrParameter_DeptCode` | String |  |  |
| 39 | `WR.PAR.AUDITOR.CODE` | `WrParameter_AuditorCode` | String |  |  |
| 40 | `WR.PAR.AUDIT.DATE.TIME` | `WrParameter_AuditDateTime` | String |  |  |
