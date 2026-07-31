# DLM.IS.CONFIG — Table Schema

> Source: `INSERTS/I_F.DLM.IS.CONFIG` in `DL_Separation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DLM.IS.RESTRICTED.COMPANIES` | `DlmIsConfig_RestrictedCompanies` |  |  |  |
| 2 | `DLM.IS.RESTRICTED.FILES` | `DlmIsConfig_RestrictedFiles` |  |  |  |
| 3 | `DLM.IS.EXCLUDED.COMPANIES` | `DlmIsConfig_ExcludedCompanies` |  |  |  |
| 4 | `DLM.IS.EXCLUDED.FILES` | `DlmIsConfig_ExcludedFiles` |  |  |  |
| 5 | `DLM.IS.DATE.FIELD.FILES` | `DlmIsConfig_DateFieldFiles` |  |  |  |
| 6 | `DLM.IS.DATE.FIELD.VAL` | `DlmIsConfig_DateFieldVal` |  |  |  |
| 7 | `DLM.IS.LIVE.DB.NAME` | `DlmIsConfig_LiveDbName` | TField |  | Name of the T24 database. |
| 8 | `DLM.IS.LIVE.DB.SCHEMA` | `DlmIsConfig_LiveDbSchema` | TField |  | Name of the schema owner in T24 database. |
| 9 | `DLM.IS.LIVE.DATA.TABLESPACE` | `DlmIsConfig_LiveDataTablespace` | TField |  | Name of the tablespace in T24 database used for T24 data. |
| 10 | `DLM.IS.LIVE.INDEX.TABLESPACE` | `DlmIsConfig_LiveIndexTablespace` | TField |  | Name of the tablespace in T24 database used for T24 indexes. |
| 11 | `DLM.IS.RO.DB.NAME` | `DlmIsConfig_RoDbName` | TField |  | Name of the READ ONLY database. |
| 12 | `DLM.IS.RO.DB.SCHEMA` | `DlmIsConfig_RoDbSchema` | TField |  | Name of the schema owner in READ ONLY database. |
| 13 | `DLM.IS.RO.VOID.DATE` | `DlmIsConfig_RoVoidDate` | TField |  | Date to be added as PDATE value for records which doesn't have value in the actual PDATE field and the recordswill not be copied. |
| 14 | `DLM.IS.RO.COPY.START.DATE` | `DlmIsConfig_RoCopyStartDate` | TField |  | Date defines the start of the READ ONLY data retention period. All data greater than or equal to this date will be copied to the READ ONLY tables. |
| 15 | `DLM.IS.RO.COPY.END.DATE` | `DlmIsConfig_RoCopyEndDate` | TField |  | Date defines the end of the READ ONLY data retention period. All data less than this date will be copied to the READ ONLY tables. |
| 16 | `DLM.IS.RETENTION.PERIOD` | `DlmIsConfig_RetentionPeriod` | TField |  | Number of years required to store READ ONLY data before it is archived. |
| 17 | `DLM.IS.SKIP.KEY.FIELD.COPY` | `DlmIsConfig_SkipKeyFieldCopy` | TField |  | Flag to skip the copy script generation for tables defined with @ID or @DATE as purge date field. |
| 18 | `DLM.IS.OFFSET.APP.NAME` | `DlmIsConfig_OffsetAppName` |  |  |  |
| 19 | `DLM.IS.OFFSET.MONTHS` | `DlmIsConfig_OffsetMonths` |  |  |  |
| 20 | `DLM.IS.ARC.SCHEMA` | `DlmIsConfig_ArcSchema` | TField |  | Name of the schema owner in READ ONLY database to hold the ARC tables. |
| 21 | `DLM.IS.FIN.DATA.TABLESPACE` | `DlmIsConfig_FinDataTablespace` | TField |  | Prefix name for the READ ONLY database DATA tablespaces which will be appended to a number. Example: RODATA1,RODATA2,... |
| 22 | `DLM.IS.FIN.INDEX.TABLESPACE` | `DlmIsConfig_FinIndexTablespace` | TField |  | Name of the READ ONLY database INDEX tablespace. |
| 23 | `DLM.IS.ARC.DATA.TABLESPACE` | `DlmIsConfig_ArcDataTablespace` | TField |  |  |
| 24 | `DLM.IS.ARC.INDEX.TABLESPACE` | `DlmIsConfig_ArcIndexTablespace` | TField |  |  |
| 25 | `DLM.IS.ORCL.RO.PARALLEL.VALUE` | `DlmIsConfig_OrclRoParallelValue` | TField |  | Oracle parallel script execution value. |
| 26 | `DLM.IS.ORCL.FIN.DISK.GROUPNAME` | `DlmIsConfig_OrclFinDiskGroupname` | TField |  | Name of the disk group to be used to store the READ ONLY database DATA tablespaces. |
| 27 | `DLM.IS.ORCL.FIN.DISK.FILEPATH` | `DlmIsConfig_OrclFinDiskFilepath` | TField |  | Disk filepath location to be used to store the READ ONLY database DATA tablespaces. |
| 28 | `DLM.IS.ORCL.FIN.TS.SIZE` | `DlmIsConfig_OrclFinTsSize` | TField |  | Initial size of the READ ONLY database DATA tablespaces. |
| 29 | `DLM.IS.ORCL.FIN.TS.AUTOEXTENT` | `DlmIsConfig_OrclFinTsAutoextent` | TField |  | Specifies how much each DATA tablespace can extend by when auto extending. |
| 30 | `DLM.IS.ORCL.FIN.INDEX.TS.SIZE` | `DlmIsConfig_OrclFinIndexTsSize` | TField |  | Initial size of the READ ONLY database INDEX tablespaces. |
| 31 | `DLM.IS.ORCL.FIN.INDEX.TS.AUTOEXTENT` | `DlmIsConfig_OrclFinIndexTsAutoextent` | TField |  | Specifies how much each INDEX tablespace can extend by when auto extending. |
| 32 | `DLM.IS.ORCL.LOB.COMPRESS.TYPE` | `DlmIsConfig_OrclLobCompressType` | TField |  | Oracle advanced compression option. (LOW, MEDIUM or HIGH) Requires oracles advanced compression license before implementation. |
| 33 | `DLM.IS.ORCL.FIN.PART.INTERVAL.NUM` | `DlmIsConfig_OrclFinPartIntervalNum` | TField |  | Specifies the interval number for the table partitions. Example: 1 for 1 MONTH, 3 for 3 months,... |
| 34 | `DLM.IS.ORCL.FIN.PART.INTERVAL.PERIOD` | `DlmIsConfig_OrclFinPartIntervalPeriod` | TField |  | Specifies the interval period for the table partitions. Example: MONTH or YEAR |
| 35 | `DLM.IS.ARC.RET.END.DATE` | `DlmIsConfig_ArcRetEndDate` | TField |  | The earliest date that the ARCHIVE data is required to be retained. |
| 36 | `DLM.IS.ORCL.ARC.DISK.GROUPNAME` | `DlmIsConfig_OrclArcDiskGroupname` | TField |  | Name of the disk group to be used to store the READ ONLY database ARCHIVE tablespaces. |
| 37 | `DLM.IS.ORCL.ARC.DISK.FILEPATH` | `DlmIsConfig_OrclArcDiskFilepath` | TField |  | Disk filepath location to be used to store the READ ONLY database ARCHIVE tablespaces. |
| 38 | `DLM.IS.ORCL.ARC.TS.SIZE` | `DlmIsConfig_OrclArcTsSize` | TField |  | Initial size of the READ ONLY database ARCHIVE DATA tablespaces. |
| 39 | `DLM.IS.ORCL.ARC.TS.AUTOEXTENT` | `DlmIsConfig_OrclArcTsAutoextent` | TField |  | Specifies how much each ARCHIVE DATA tablespace can extend by when auto extending. |
| 40 | `DLM.IS.ORCL.ARC.INDEX.TS.SIZE` | `DlmIsConfig_OrclArcIndexTsSize` | TField |  | Initial size of the READ ONLY database ARCHIVE INDEX tablespaces. |
| 41 | `DLM.IS.ORCL.ARC.INDEX.TS.AUTOEXTENT` | `DlmIsConfig_OrclArcIndexTsAutoextent` | TField |  | Specifies how much each ARCHIVE INDEX tablespace can extend by when auto extending. |
| 42 | `DLM.IS.ORCL.LIVE.DB.PWD` | `DlmIsConfig_OrclLiveDbPwd` | TField |  | Password of the schema owner for the T24 database. |
| 43 | `DLM.IS.ORCL.RO.DB.PWD` | `DlmIsConfig_OrclRoDbPwd` | TField |  | Password of the schema owner for the READ ONLY database. |
| 44 | `DLM.IS.ORCL.RO.SCHEMA.NAMES` | `DlmIsConfig_OrclRoSchemaNames` |  |  |  |
| 45 | `DLM.IS.MSSQL.FIN.FILEPATH` | `DlmIsConfig_MssqlFinFilepath` | TField |  | Specifies the location to hold physical files for READ ONLY data. |
| 46 | `DLM.IS.MSSQL.FIN.FILEGROUP` | `DlmIsConfig_MssqlFinFilegroup` | TField |  | Prefix name for the READ ONLY database FILEGROUP name which will be appended to a number. Example: ROFG1,ROFG2,... |
| 47 | `DLM.IS.MSSQL.FIN.FILENAME` | `DlmIsConfig_MssqlFinFilename` | TField |  | Prefix name for the READ ONLY database FILE name which will be appended to a number. Example: ROFN1, ROFN2,... |
| 48 | `DLM.IS.MSSQL.FIN.PARTITION.FUNCTION` | `DlmIsConfig_MssqlFinPartitionFunction` | TField |  | Specifies the READ ONLY database 'partition function' name to be created. |
| 49 | `DLM.IS.MSSQL.FIN.PARTITION.SCHEME` | `DlmIsConfig_MssqlFinPartitionScheme` | TField |  | Specifies the READ ONLY database 'partition scheme' name to be created. |
| 50 | `DLM.IS.MSSQL.ARC.FILEPATH` | `DlmIsConfig_MssqlArcFilepath` | TField |  | Specifies the location to hold physical files for READ ONLY Archive data. |
| 51 | `DLM.IS.MSSQL.ARC.FILEGROUP` | `DlmIsConfig_MssqlArcFilegroup` | TField |  | Prefix name for the READ ONLY database Archive FILEGROUP name which will be appended to a number. Example:ARCFG1, ARCFG2,... |
| 52 | `DLM.IS.MSSQL.ARC.FILENAME` | `DlmIsConfig_MssqlArcFilename` | TField |  | Prefix name for the READ ONLY database Archive FILE name which will be appended to a number. Example: ARCFN1,ARCFN2,... |
| 53 | `DLM.IS.DB2.FIN.BUFFER` | `DlmIsConfig_Db2FinBuffer` | TField |  | Specifies the READ ONLY database buffer pool name for data. |
| 54 | `DLM.IS.DB2.FIN.INDEX.BUFFER` | `DlmIsConfig_Db2FinIndexBuffer` | TField |  | Specifies the READ ONLY database buffer pool name for index. |
| 55 | `DLM.IS.DB2.FIN.LOB.BUFFER` | `DlmIsConfig_Db2FinLobBuffer` | TField |  | Specifies the READ ONLY database buffer pool name for LOB data. |
| 56 | `DLM.IS.DB2.FIN.LOB.TABLESPACE` | `DlmIsConfig_Db2FinLobTablespace` | TField |  | Prefix name for the READ ONLY database LOB DATA tablespaces which will be appended to a number. Example:ROFINLOB1 |
| 57 | `DLM.IS.DB2.FIN.NUM.TABLESPACE` | `DlmIsConfig_Db2FinNumTablespace` | TField |  | Specifies the number of READ ONLY database INDEX and LOB tablespaces to be created. |
| 58 | `DLM.IS.DB2.ARC.BUFFER` | `DlmIsConfig_Db2ArcBuffer` | TField |  | Specifies the READ ONLY database buffer pool name for Archive data. |
| 59 | `DLM.IS.DB2.ARC.INDEX.BUFFER` | `DlmIsConfig_Db2ArcIndexBuffer` | TField |  | Specifies the READ ONLY database buffer pool name for Archive index. |
| 60 | `DLM.IS.DB2.ARC.LOB.BUFFER` | `DlmIsConfig_Db2ArcLobBuffer` | TField |  | Specifies the READ ONLY database buffer pool name for Archive LOB data. |
| 61 | `DLM.IS.DB2.ARC.LOB.TABLESPACE` | `DlmIsConfig_Db2ArcLobTablespace` | TField |  | Prefix name for the READ ONLY database Archive LOB DATA tablespaces which will be appended to a number. Example:ARCLOB1 |
| 62 | `DLM.IS.DB2.ARC.NUM.TABLESPACE` | `DlmIsConfig_Db2ArcNumTablespace` | TField |  | Specifies the number of READ ONLY database Archive DATA, INDEX and LOB tablespaces to be created. |
| 63 | `DLM.IS.DB2.LIVE.SERVER.NAME` | `DlmIsConfig_Db2LiveServerName` | TField |  | SERVER name of the T24 database to be created. |
| 64 | `DLM.IS.DB2.LIVE.DB.AUTH.NAME` | `DlmIsConfig_Db2LiveDbAuthName` | TField |  | Name of the authenticated user to login DB2 for T24 database. |
| 65 | `DLM.IS.DB2.LIVE.DB.AUTH.PWD` | `DlmIsConfig_Db2LiveDbAuthPwd` | TField |  | Password of the authenticated user to login DB2 for T24 database. |
| 66 | `DLM.IS.DB2.LIVE.TCPIP.NODE.NAME` | `DlmIsConfig_Db2LiveTcpipNodeName` | TField |  | TCPIP node number to connect with T24 database. |
| 67 | `DLM.IS.DB2.LIVE.CATALOGUED.DB.NAME` | `DlmIsConfig_Db2LiveCataloguedDbName` | TField |  | T24 Cataloged database name. |
| 68 | `DLM.IS.DB2.RO.SERVER.NAME` | `DlmIsConfig_Db2RoServerName` | TField |  | SERVER name of the READ ONLY database to be created. |
| 69 | `DLM.IS.DB2.RO.DB.AUTH.NAME` | `DlmIsConfig_Db2RoDbAuthName` | TField |  | Name of the authenticated user to login DB2 for READ ONLY database. |
| 70 | `DLM.IS.DB2.RO.DB.AUTH.PWD` | `DlmIsConfig_Db2RoDbAuthPwd` | TField |  | Password of the authenticated user to login DB2 for READ ONLY database. |
| 71 | `DLM.IS.DB2.RO.TCPIP.NODE.NAME` | `DlmIsConfig_Db2RoTcpipNodeName` | TField |  | TCPIP node number to connect with READ ONLY database. |
| 72 | `DLM.IS.DB2.RO.CATALOGUED.DB.NAME` | `DlmIsConfig_Db2RoCataloguedDbName` | TField |  | READ ONLY Cataloged database name. |
| 73 | `DLM.IS.DB2.VERSION` | `DlmIsConfig_Db2Version` | TField |  | Specifies the version of DB2. |
| 74 | `DLM.IS.TEMP.PWD` | `DlmIsConfig_TempPwd` |  |  |  |
| 75 | `DLM.IS.NUO.HOST.NAME` | `DlmIsConfig_NuoHostName` | TField |  | NUODB host server which will be used in storagegroup scripts. |
| 76 | `DLM.IS.NUO.RO.STORAGE.GROUP` | `DlmIsConfig_NuoRoStorageGroup` | TField |  | Prefix name for the READ ONLY database storagegroup name which will be appended to a number. Example: ROSG1,ROSG2,... |
| 77 | `DLM.IS.NUO.ARC.STORAGE.GROUP` | `DlmIsConfig_NuoArcStorageGroup` | TField |  | Prefix name for the READ ONLY database ARCHIVE DATA storagegroup name which will be appended to a number. Example: ARCSG1,ARCSG2,... |
| 78 | `DLM.IS.NUO.SM.PROCESS.ID` | `DlmIsConfig_NuoSmProcessId` | TField |  |  |
| 79 | `DLM.IS.PSQL.HOST.NAME` | `DlmIsConfig_PsqlHostName` |  |  |  |
| 80 | `DLM.IS.PSQL.LIVE.DB.USER` | `DlmIsConfig_PsqlLiveDbUser` | TField |  | User name for the T24 database. |
| 81 | `DLM.IS.PSQL.RO.DB.USER` | `DlmIsConfig_PsqlRoDbUser` | TField |  | User name for the READ ONLY database |
| 82 | `DLM.IS.PSQL.LIVE.DB.PWD` | `DlmIsConfig_PsqlLiveDbPwd` | TField |  | Password of the schema owner for the T24 database. |
| 83 | `DLM.IS.PSQL.RO.DB.PWD` | `DlmIsConfig_PsqlRoDbPwd` | TField |  | Password of the schema owner for the READ ONLY database. |
| 84 | `DLM.IS.PSQL.FIN.PART.INTERVAL.NUM` | `DlmIsConfig_PsqlFinPartIntervalNum` | TField |  | Specifies the interval number for the table partitions. Example: 1 for 1 YEAR, 3 for 3 YEAR,.... |
| 85 | `DLM.IS.PSQL.FIN.PART.INTERVAL.PERIOD` | `DlmIsConfig_PsqlFinPartIntervalPeriod` | TField |  |  |
| 86 | `DLM.IS.PSQL.FIN.DISK.FILEPATH` | `DlmIsConfig_PsqlFinDiskFilepath` |  |  |  |
| 87 | `DLM.IS.MSSQL.AZURE.SQL` | `DlmIsConfig_MssqlIsAzureSql` | TField |  |  |
| 88 | `DLM.IS.RESERVED.7` | `DlmIsConfig_Reserved7` |  |  |  |
| 89 | `DLM.IS.RESERVED.6` | `DlmIsConfig_Reserved6` |  |  |  |
| 90 | `DLM.IS.RESERVED.5` | `DlmIsConfig_Reserved5` |  |  |  |
| 91 | `DLM.IS.RESERVED.4` | `DlmIsConfig_Reserved4` | TField |  |  |
| 92 | `DLM.IS.RESERVED.3` | `DlmIsConfig_Reserved3` | TField |  |  |
| 93 | `DLM.IS.RESERVED.2` | `DlmIsConfig_Reserved2` | TField |  |  |
| 94 | `DLM.IS.RESERVED.1` | `DlmIsConfig_Reserved1` | TField |  |  |
| 95 | `DLM.IS.OVERRIDE` | `DlmIsConfig_Override` |  |  |  |
| 96 | `DLM.IS.RECORD.STATUS` | `DlmIsConfig_RecordStatus` | String |  |  |
| 97 | `DLM.IS.CURR.NO` | `DlmIsConfig_CurrNo` | String |  |  |
| 98 | `DLM.IS.INPUTTER` | `DlmIsConfig_Inputter` |  |  |  |
| 99 | `DLM.IS.DATE.TIME` | `DlmIsConfig_DateTime` |  |  |  |
| 100 | `DLM.IS.AUTHORISER` | `DlmIsConfig_Authoriser` | String |  |  |
| 101 | `DLM.IS.CO.CODE` | `DlmIsConfig_CoCode` | String |  |  |
| 102 | `DLM.IS.DEPT.CODE` | `DlmIsConfig_DeptCode` | String |  |  |
| 103 | `DLM.IS.AUDITOR.CODE` | `DlmIsConfig_AuditorCode` | String |  |  |
| 104 | `DLM.IS.AUDIT.DATE.TIME` | `DlmIsConfig_AuditDateTime` | String |  |  |
