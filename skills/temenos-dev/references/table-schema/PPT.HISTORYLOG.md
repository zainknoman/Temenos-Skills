# PPT.HISTORYLOG — Table Schema

> Source: `INSERTS/I_F.PPT.HISTORYLOG` in `PP_PaymentFrameworkService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPHIS.CompanyID` | `PptHistorylog_Companyid` |  |  |  |
| 2 | `PPHIS.Timestamp` | `PptHistorylog_Timestamp` |  |  |  |
| 3 | `PPHIS.JobName` | `PptHistorylog_Jobname` |  |  |  |
| 4 | `PPHIS.ProgramName` | `PptHistorylog_Programname` |  |  |  |
| 5 | `PPHIS.EventType` | `PptHistorylog_Eventtype` |  |  |  |
| 6 | `PPHIS.EventDescription` | `PptHistorylog_Eventdescription` |  |  |  |
| 7 | `PPHIS.ErrorCode` | `PptHistorylog_Errorcode` |  |  |  |
| 8 | `PPHIS.AdditionalInformation` | `PptHistorylog_Additionalinformation` |  |  |  |
