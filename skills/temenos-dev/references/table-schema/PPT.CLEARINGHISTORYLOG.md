# PPT.CLEARINGHISTORYLOG — Table Schema

> Source: `INSERTS/I_F.PPT.CLEARINGHISTORYLOG` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCHL.CompanyID` | `PptClearinghistorylog_Companyid` |  |  |  |
| 2 | `PPCHL.Timestamp` | `PptClearinghistorylog_Timestamp` |  |  |  |
| 3 | `PPCHL.JobName` | `PptClearinghistorylog_Jobname` |  |  |  |
| 4 | `PPCHL.ProgramName` | `PptClearinghistorylog_Programname` |  |  |  |
| 5 | `PPCHL.EventType` | `PptClearinghistorylog_Eventtype` |  |  |  |
| 6 | `PPCHL.EventDescription` | `PptClearinghistorylog_Eventdescription` |  |  |  |
| 7 | `PPCHL.ErrorCode` | `PptClearinghistorylog_Errorcode` |  |  |  |
| 8 | `PPCHL.AdditionalInformation` | `PptClearinghistorylog_Additionalinformation` |  |  |  |
