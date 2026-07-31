# DW.EXPORT.PARAM — Table Schema

> Source: `INSERTS/I_F.DW.EXPORT.PARAM` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.EP.DESCRIPTION` | `DwExportParam_Description` |  |  |  |
| 2 | `DW.EP.FILE.PATHNAME` | `DwExportParam_FilePathname` | TField |  | This is the path in which the data will be extracted to for the particular COMPANY record Different paths should be given for different company extracts. |
| 3 | `DW.EP.UNICODE.STD` | `DwExportParam_UnicodeStd` | TField |  | This is the format in which the data will be extracted in. This is a NOINPUT field, it will be defaulted to UTF-16BE |
| 4 | `DW.EP.FLD.DELIMITER` | `DwExportParam_FldDelimiter` | TField |  | This is the delimiter with which the data will be delimited in the extract This is a NOINPUT field, it will be defaulted to '~' |
| 5 | `DW.EP.FILE.NAME` | `DwExportParam_FileName` |  |  |  |
| 6 | `DW.EP.TRANSFER.RTN` | `DwExportParam_TransferRtn` | TField |  | A routine or a Java method implementing the super class DataExporter can be attached in this field. A user defined routine/class which has the logic to move the extracted data from the T24 server to Insightserver. * 1. BASIC Implementation The routine should have a valid entry in EB.API with SOURCE.TYPE as BASIC. A sample routine DW.TRANSFER.ROUTINE is provided by Temenos. * 2. JAVA Implementation The class should have a valid entry in EB.API with SOURCE.TYPE as METHOD which implements an interface defined inthe EB.API record DW.EXPORT.PARAM.TRANSFER.RTN.HOOK. This field supports the transferDataExtract method from the super class DataExporter which is available in thecom.temenos.t24.api.hook.system package under DW_DataExportHook.jar shipped with Transact. A sample Java implementation SampleTransferHookImpl.java is provided by Temenos. |
| 7 | `DW.EP.DW.ONLINE.UPDATE` | `DwExportParam_DwOnlineUpdate` | TField |  | This field will control in which format data's will be extracted It has 3 options, ONLINE, INCREMENTAL, BOTH |
| 8 | `DW.EP.MERGE.COMPANY` | `DwExportParam_MergeCompany` |  |  |  |
| 9 | `DW.EP.PRODUCT` | `DwExportParam_Product` |  |  |  |
| 10 | `DW.EP.FREQUENCY` | `DwExportParam_Frequency` |  |  |  |
| 11 | `DW.EP.OL.TARGET.DATABASE` | `DwExportParam_OlTargetDatabase` | TField |  | This field will be used when the TAKEOVER field is specified as 'ONLINE'. The value in this field is the database that will be updated when a record of the current. DW.EXPORT record is modified or created. The table information will be obtained from the OL.TARGET.TABLE field. |
| 12 | `DW.EP.NO.OF.RETRY` | `DwExportParam_NoOfRetry` | TField |  | Input field, should accept only numbers. This is to specify how many times system should re-try to push the transaction from T24 to 3rd party database, incase of network failure or database failure. |
| 13 | `DW.EP.ACTUAL.RETRY` | `DwExportParam_ActualRetry` | TField |  | No input field. This will be updated for the online extraction. This is to note how many times the system re-tried to push the transaction from T24 to 3rd party database, incase of network failure or database failure. |
| 14 | `DW.EP.BULK.NO` | `DwExportParam_BulkNo` | TField |  |  |
| 15 | `DW.EP.BBL.CALL` | `DwExportParam_BblCall` | TField |  |  |
| 16 | `DW.EP.TYPE.OF.EXTRACT` | `DwExportParam_TypeOfExtract` | TField |  | This field determines the type of offline extraction - delimited, fixed, data stream and store in local table |
| 17 | `DW.EP.FILE.SUFFIX` | `DwExportParam_FileSuffix` | TField |  |  |
| 18 | `DW.EP.RECON` | `DwExportParam_Recon` | TField |  | This field is used to enable or disable the reconciliation process for DW.EXPORT This field will accept only YES or NO or Null(" "),Both NULL and NO are same and default value is NULL. |
| 19 | `DW.EP.ENABLE.DW.LITE` | `DwExportParam_EnableDwLite` | TField |  | This field will activate the DW.LITE version This field will accept only YES and ''(NULL), Null is equalent NO Set this field to 'YES' to enable DW.LITE |
| 20 | `DW.EP.ONE.TIME.EXTRACT` | `DwExportParam_OneTimeExtract` |  |  |  |
| 21 | `DW.EP.ONLINE.BULK.NO` | `DwExportParam_OnlineBulkNo` | TField |  | This field will be used by ONLINE service to execute a batch of SQL Queries matching the Bulk number which willbe executed in single established SQL connection |
| 22 | `DW.EP.OL.DATA.PIPELINE.MODE` | `DwExportParam_OlDataPipelineMode` | TField | Yes | This field is used to determine the data pipeline mode for streaming of DW events to the online database It can be left blank or the options CALLJ or IF-PIPELINE can be set CALLJ option can be used as a push request to stream data to online database using DWUtils package IF-PIPELINE option can be used as a pull request to stream DW data to the external data store using DWUtilspackage STORE.IN.LOCAL.TABLE option can be used to store data in Transact tables This field is mandatory if DW.ONLINE.UPDATE is set |
| 23 | `DW.EP.CACHE.REFRESH.TIME` | `DwExportParam_CacheRefreshTime` | TField |  | Refresh DW cache based on the value set in this field |
| 24 | `DW.EP.CREATE.MISSING.OL.TOPICS` | `DwExportParam_CreateMissingOLTopics` |  |  |  |
| 25 | `DW.EP.CREATE.MISSING.ILP.TOPICS` | `DwExportParam_CreateMissingIlpTopics` | TField |  | This field creates missing topics for streaming data via initial load processing when enabled |
| 26 | `DW.EP.RESERVED.5` | `DwExportParam_Reserved5` |  |  |  |
| 27 | `DW.EP.RESERVED.4` | `DwExportParam_Reserved4` | TField |  |  |
| 28 | `DW.EP.RESERVED.3` | `DwExportParam_Reserved3` | TField |  |  |
| 29 | `DW.EP.RESERVED.2` | `DwExportParam_Reserved2` | TField |  |  |
| 30 | `DW.EP.RESERVED.1` | `DwExportParam_Reserved1` | TField |  |  |
| 31 | `DW.EP.RECORD.STATUS` | `DwExportParam_RecordStatus` | String |  |  |
| 32 | `DW.EP.CURR.NO` | `DwExportParam_CurrNo` | String |  |  |
| 33 | `DW.EP.INPUTTER` | `DwExportParam_Inputter` |  |  |  |
| 34 | `DW.EP.DATE.TIME` | `DwExportParam_DateTime` |  |  |  |
| 35 | `DW.EP.AUTHORISER` | `DwExportParam_Authoriser` | String |  |  |
| 36 | `DW.EP.CO.CODE` | `DwExportParam_CoCode` | String |  |  |
| 37 | `DW.EP.DEPT.CODE` | `DwExportParam_DeptCode` | String |  |  |
| 38 | `DW.EP.AUDITOR.CODE` | `DwExportParam_AuditorCode` | String |  |  |
| 39 | `DW.EP.AUDIT.DATE.TIME` | `DwExportParam_AuditDateTime` | String |  |  |
