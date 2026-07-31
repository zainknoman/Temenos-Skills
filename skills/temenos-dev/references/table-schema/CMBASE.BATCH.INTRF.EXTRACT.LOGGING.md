# CMBASE.BATCH.INTRF.EXTRACT.LOGGING — Table Schema

> Source: `INSERTS/I_F.CMBASE.BATCH.INTRF.EXTRACT.LOGGING` in `CMBASE_InterfaceBatchExtract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMBASE.INTRF.LOG.BATCH.INTRF.ID` | `CmbaseBatchIntrfExtractLogging_BatchIntrfId` | TField |  | Lookup of CMBASE.BATCH.INTRf.PARAM>@ID |
| 2 | `CMBASE.INTRF.LOG.FILE.NAME` | `CmbaseBatchIntrfExtractLogging_FileName` | TField |  | Name of the extracted file for which the log is created, generally the file name is configured in theCMBASE.BATCH.INTF.PARAM |
| 3 | `CMBASE.INTRF.LOG.PROCESS.DATE` | `CmbaseBatchIntrfExtractLogging_ProcessDate` | TField |  | File extraction date |
| 4 | `CMBASE.INTRF.LOG.PROCESS.TIME` | `CmbaseBatchIntrfExtractLogging_ProcessTime` | TField |  | File extraction time |
| 5 | `CMBASE.INTRF.LOG.STATUS` | `CmbaseBatchIntrfExtractLogging_Status` | TField |  | File extraction status, Possible values Success, Failure, Pending |
| 6 | `CMBASE.INTRF.LOG.ERROR.CODE` | `CmbaseBatchIntrfExtractLogging_ErrorCode` |  |  |  |
| 7 | `CMBASE.INTRF.LOG.ERROR.DESC` | `CmbaseBatchIntrfExtractLogging_ErrorDesc` |  |  |  |
| 8 | `CMBASE.INTRF.LOG.ERROR.RECORD` | `CmbaseBatchIntrfExtractLogging_ErrorRecord` |  |  |  |
| 9 | `CMBASE.INTRF.LOG.ERROR.FIELD` | `CmbaseBatchIntrfExtractLogging_ErrorField` |  |  |  |
| 10 | `CMBASE.INTRF.LOG.ERROR.LINE.NO` | `CmbaseBatchIntrfExtractLogging_ErrorLineNo` |  |  |  |
| 11 | `CMBASE.INTRF.LOG.RESERVED.10` | `CmbaseBatchIntrfExtractLogging_Reserved10` |  |  |  |
| 12 | `CMBASE.INTRF.LOG.RESERVED.9` | `CmbaseBatchIntrfExtractLogging_Reserved9` |  |  |  |
| 13 | `CMBASE.INTRF.LOG.RESERVED.8` | `CmbaseBatchIntrfExtractLogging_Reserved8` | TField |  | This field is reserved for future use |
| 14 | `CMBASE.INTRF.LOG.RESERVED.7` | `CmbaseBatchIntrfExtractLogging_Reserved7` | TField |  | This field is reserved for future use |
| 15 | `CMBASE.INTRF.LOG.RESERVED.6` | `CmbaseBatchIntrfExtractLogging_Reserved6` | TField |  | This field is reserved for future use |
| 16 | `CMBASE.INTRF.LOG.RESERVED.5` | `CmbaseBatchIntrfExtractLogging_Reserved5` | TField |  | This field is reserved for future use |
| 17 | `CMBASE.INTRF.LOG.RESERVED.4` | `CmbaseBatchIntrfExtractLogging_Reserved4` | TField |  | This field is reserved for future use |
| 18 | `CMBASE.INTRF.LOG.RESERVED.3` | `CmbaseBatchIntrfExtractLogging_Reserved3` | TField |  | This field is reserved for future use |
| 19 | `CMBASE.INTRF.LOG.RESERVED.2` | `CmbaseBatchIntrfExtractLogging_Reserved2` | TField |  | This field is reserved for future use |
| 20 | `CMBASE.INTRF.LOG.RESERVED.1` | `CmbaseBatchIntrfExtractLogging_Reserved1` | TField |  | This field is reserved for future use |
| 21 | `CMBASE.INTRF.LOG.LOCAL.REF` | `CmbaseBatchIntrfExtractLogging_LocalRef` |  |  |  |
| 22 | `CMBASE.INTRF.LOG.OVERRIDE` | `CmbaseBatchIntrfExtractLogging_Override` |  |  |  |
| 23 | `CMBASE.INTRF.LOG.RECORD.STATUS` | `CmbaseBatchIntrfExtractLogging_RecordStatus` | String |  |  |
| 24 | `CMBASE.INTRF.LOG.CURR.NO` | `CmbaseBatchIntrfExtractLogging_CurrNo` | String |  |  |
| 25 | `CMBASE.INTRF.LOG.INPUTTER` | `CmbaseBatchIntrfExtractLogging_Inputter` |  |  |  |
| 26 | `CMBASE.INTRF.LOG.DATE.TIME` | `CmbaseBatchIntrfExtractLogging_DateTime` |  |  |  |
| 27 | `CMBASE.INTRF.LOG.AUTHORISER` | `CmbaseBatchIntrfExtractLogging_Authoriser` | String |  |  |
| 28 | `CMBASE.INTRF.LOG.CO.CODE` | `CmbaseBatchIntrfExtractLogging_CoCode` | String |  |  |
| 29 | `CMBASE.INTRF.LOG.DEPT.CODE` | `CmbaseBatchIntrfExtractLogging_DeptCode` | String |  |  |
| 30 | `CMBASE.INTRF.LOG.AUDITOR.CODE` | `CmbaseBatchIntrfExtractLogging_AuditorCode` | String |  |  |
| 31 | `CMBASE.INTRF.LOG.AUDIT.DATE.TIME` | `CmbaseBatchIntrfExtractLogging_AuditDateTime` | String |  |  |
