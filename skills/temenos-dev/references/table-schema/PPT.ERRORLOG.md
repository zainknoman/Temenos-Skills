# PPT.ERRORLOG — Table Schema

> Source: `INSERTS/I_F.PPT.ERRORLOG` in `PP_PaymentFrameworkService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPERL.CompanyID` | `PptErrorlog_Companyid` |  |  |  |
| 2 | `PPERL.Date` | `PptErrorlog_Date` |  |  |  |
| 3 | `PPERL.Timestamp` | `PptErrorlog_Timestamp` |  |  |  |
| 4 | `PPERL.JobName` | `PptErrorlog_Jobname` |  |  |  |
| 5 | `PPERL.ProgramName` | `PptErrorlog_Programname` |  |  |  |
| 6 | `PPERL.EventType` | `PptErrorlog_Eventtype` |  |  |  |
| 7 | `PPERL.EventDescription` | `PptErrorlog_Eventdescription` |  |  |  |
| 8 | `PPERL.ErrorCode` | `PptErrorlog_Errorcode` |  |  |  |
| 9 | `PPERL.AdditionalInformation` | `PptErrorlog_Additionalinformation` |  |  |  |
