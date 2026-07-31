# EB.LOGGING — Table Schema

> Source: `INSERTS/I_F.EB.LOGGING` in `EB_Logging.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.LOG.APPLICATION` | `EbLogging_Application` | TField |  | Standard T24 alphanumeric field.The underlying T24 application for which the TEC log was triggered. Validation Rules: A maximum of 35 characters allowed. |
| 2 | `EB.LOG.ROUTINE` | `EbLogging_Routine` | TField |  | Standard T24 alphanumeric field.The actual TEC routine which has invoked this log update. Validation Rules: A maximum of 35 characters allowed. |
| 3 | `EB.LOG.MODULE` | `EbLogging_Module` | TField |  | Standard T24 alphanumeric field.The T24 product module to which the APPLICATION belongs to. Validation Rules: A maximum of 35 characters allowed. |
| 4 | `EB.LOG.FILE.NAME` | `EbLogging_FileName` | TField |  | Standard T24 alphanumeric field.The T24 file name for which the TEC log was updated. This will usually be the same as APPLICATION. Validation Rules: A maximum of 35 characters allowed. |
| 5 | `EB.LOG.RECORD.KEY` | `EbLogging_RecordKey` | TField |  | Standard T24 alphanumeric field.The Record ID in the application which triggered this log update. Validation Rules: A maximum of 35 characters allowed. |
| 6 | `EB.LOG.OPERATOR` | `EbLogging_Operator` | TField |  | Standard T24 alphanumeric field.The user who performed the transaction which triggered this log update. Validation Rules: A maximum of 35 characters allowed. |
| 7 | `EB.LOG.DATE` | `EbLogging_Date` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters allowed. |
| 8 | `EB.LOG.TIME` | `EbLogging_Time` | TField |  | Standard T24 time field. Validation Rules: A maximum of 5 characters allowed. |
| 9 | `EB.LOG.COMP.CODE` | `EbLogging_CompCode` | TField |  | Standard T24 alphanumeric field.The company in which the transaction was performed. Validation Rules: A maximum of 11 characters allowed. |
| 10 | `EB.LOG.LOG.PARAMETER` | `EbLogging_LogParameter` | TField |  | EB.LOGGING.PARAMETER file based on which the log is recorded. Validation Rules: A maximum of 35 characters allowed. |
| 11 | `EB.LOG.LOG.LEVEL` | `EbLogging_LogLevel` | TField |  | Level of log message that is recorded. Validation Rules: A maximum of 35 characters allowed. |
| 12 | `EB.LOG.LOG.DESCRIPTION` | `EbLogging_LogDescription` | TField |  | Gives a brief description about the log. Validation Rules: A maximum of 35 characters allowed. |
| 13 | `EB.LOG.LOG.DETAILS` | `EbLogging_LogDetails` | TField |  | Gives a detailed description about the log recorded. Validation Rules: A maximum of 35 characters allowed. |
