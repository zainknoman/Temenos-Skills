# TNFCOP.BATCH.EXTRACT.LOGGING — Table Schema

> Source: `INSERTS/I_F.TNFCOP.BATCH.EXTRACT.LOGGING` in `TNFCOP_AVA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.BE.LOG.ERROR.DESC` | `TnfcopBatchExtractLogging_ErrorDesc` |  |  |  |
| 2 | `TNFCOP.BE.LOG.STATUS` | `TnfcopBatchExtractLogging_Status` | TField |  | This field denotes the status of error (Failed or Fixed). |
| 3 | `TNFCOP.BE.LOG.REPORTING.PERIOD` | `TnfcopBatchExtractLogging_ReportingPeriod` | TField |  | Reporting Period in 'mmyyyy' format. |
| 4 | `TNFCOP.BE.LOG.RESERVED.8` | `TnfcopBatchExtractLogging_Reserved8` | TField |  | Reserved field for future use |
| 5 | `TNFCOP.BE.LOG.RESERVED.7` | `TnfcopBatchExtractLogging_Reserved7` | TField |  | Reserved field for future use |
| 6 | `TNFCOP.BE.LOG.RESERVED.6` | `TnfcopBatchExtractLogging_Reserved6` | TField |  | Reserved field for future use |
| 7 | `TNFCOP.BE.LOG.RESERVED.5` | `TnfcopBatchExtractLogging_Reserved5` | TField |  | Reserved field for future use |
| 8 | `TNFCOP.BE.LOG.RESERVED.4` | `TnfcopBatchExtractLogging_Reserved4` | TField |  | Reserved field for future use |
| 9 | `TNFCOP.BE.LOG.RESERVED.3` | `TnfcopBatchExtractLogging_Reserved3` | TField |  | Reserved field for future use |
| 10 | `TNFCOP.BE.LOG.RESERVED.2` | `TnfcopBatchExtractLogging_Reserved2` | TField |  | Reserved field for future use |
| 11 | `TNFCOP.BE.LOG.RESERVED.1` | `TnfcopBatchExtractLogging_Reserved1` | TField |  | Reserved field for future use |
| 12 | `TNFCOP.BE.LOG.LOCAL.REF` | `TnfcopBatchExtractLogging_LocalRef` |  |  |  |
| 13 | `TNFCOP.BE.LOG.OVERRIDE` | `TnfcopBatchExtractLogging_Override` |  |  |  |
| 14 | `TNFCOP.BE.LOG.RECORD.STATUS` | `TnfcopBatchExtractLogging_RecordStatus` | String |  |  |
| 15 | `TNFCOP.BE.LOG.CURR.NO` | `TnfcopBatchExtractLogging_CurrNo` | String |  |  |
| 16 | `TNFCOP.BE.LOG.INPUTTER` | `TnfcopBatchExtractLogging_Inputter` |  |  |  |
| 17 | `TNFCOP.BE.LOG.DATE.TIME` | `TnfcopBatchExtractLogging_DateTime` |  |  |  |
| 18 | `TNFCOP.BE.LOG.AUTHORISER` | `TnfcopBatchExtractLogging_Authoriser` | String |  |  |
| 19 | `TNFCOP.BE.LOG.CO.CODE` | `TnfcopBatchExtractLogging_CoCode` | String |  |  |
| 20 | `TNFCOP.BE.LOG.DEPT.CODE` | `TnfcopBatchExtractLogging_DeptCode` | String |  |  |
| 21 | `TNFCOP.BE.LOG.AUDITOR.CODE` | `TnfcopBatchExtractLogging_AuditorCode` | String |  |  |
| 22 | `TNFCOP.BE.LOG.AUDIT.DATE.TIME` | `TnfcopBatchExtractLogging_AuditDateTime` | String |  |  |
