# TZ.TRANSACTION.STOP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TZ.TRANSACTION.STOP.PARAMETER` in `TZ_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TZ.TSP.DEFAULT.EXPIRY.DAYS` | `TzTransactionStopParameter_DefaultExpiryDays` | TField | No | A number of working/calendars days after which the TRANSACTION.STOP.INSTRUCTION will be marked as EXPIRED. Validation Rule: This is an optional field. Allowed values are 1C - 999C and 1W - 999W. Maximum allowed number of digits is '3'. If only number of days is provided, systems defaults as calender days |
| 2 | `TZ.TSP.DAYS.TO.HISTORY` | `TzTransactionStopParameter_DaysToHistory` | TField | Yes | A number of working days which the TRANSACTION.STOP.INSTRUCTION will be moved to history. Validation Rule: This is a mandatory field. Allowed values are 1C - 99C and 1W - 99W. Maximum allowed number of digits is '2'. If only number of days is provided, systems defaults as calender days. |
| 3 | `TZ.TSP.DUP.STOP.CRITERIA` | `TzTransactionStopParameter_DupStopCriteria` | TField | No | Will define the duplicate criteria which will be used if the Transaction Stop Instruction has been already captured. Input to this field must be a valid record id from the EB.DUPLICATE.TYPE file Validation Rule: Optional Input. Input to this field must be a valid record id from the EB.DUPLICATE.TYPE file,, when the APPLICATION is set to 'TZ.TRANSACTION.STOP.INSTRUCTION' |
| 4 | `TZ.TSP.RESERVED.5` | `TzTransactionStopParameter_Reserved5` | TField |  |  |
| 5 | `TZ.TSP.RESERVED.4` | `TzTransactionStopParameter_Reserved4` | TField |  |  |
| 6 | `TZ.TSP.RESERVED.3` | `TzTransactionStopParameter_Reserved3` | TField |  |  |
| 7 | `TZ.TSP.RESERVED.2` | `TzTransactionStopParameter_Reserved2` | TField |  |  |
| 8 | `TZ.TSP.RESERVED.1` | `TzTransactionStopParameter_Reserved1` | TField |  |  |
| 9 | `TZ.TSP.LOCAL.REF` | `TzTransactionStopParameter_LocalRef` |  |  |  |
| 10 | `TZ.TSP.OVERRIDE` | `TzTransactionStopParameter_Override` |  |  |  |
| 11 | `TZ.TSP.RECORD.STATUS` | `TzTransactionStopParameter_RecordStatus` | String |  |  |
| 12 | `TZ.TSP.CURR.NO` | `TzTransactionStopParameter_CurrNo` | String |  |  |
| 13 | `TZ.TSP.INPUTTER` | `TzTransactionStopParameter_Inputter` |  |  |  |
| 14 | `TZ.TSP.DATE.TIME` | `TzTransactionStopParameter_DateTime` |  |  |  |
| 15 | `TZ.TSP.AUTHORISER` | `TzTransactionStopParameter_Authoriser` | String |  |  |
| 16 | `TZ.TSP.CO.CODE` | `TzTransactionStopParameter_CoCode` | String |  |  |
| 17 | `TZ.TSP.DEPT.CODE` | `TzTransactionStopParameter_DeptCode` | String |  |  |
| 18 | `TZ.TSP.AUDITOR.CODE` | `TzTransactionStopParameter_AuditorCode` | String |  |  |
| 19 | `TZ.TSP.AUDIT.DATE.TIME` | `TzTransactionStopParameter_AuditDateTime` | String |  |  |
