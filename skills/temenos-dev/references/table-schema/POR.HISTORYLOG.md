# POR.HISTORYLOG — Table Schema

> Source: `INSERTS/I_F.POR.HISTORYLOG` in `PP_PaymentFrameworkService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPHI.CompanyID` | `PorHistorylog_Companyid` |  |  |  |
| 2 | `PPPHI.FTNumber` | `PorHistorylog_Ftnumber` |  |  |  |
| 3 | `PPPHI.HistoryTimestamp` | `PorHistorylog_Historytimestamp` |  |  |  |
| 4 | `PPPHI.EventType` | `PorHistorylog_Eventtype` |  |  |  |
| 5 | `PPPHI.EventDescription` | `PorHistorylog_Eventdescription` |  |  |  |
| 6 | `PPPHI.ErrorCode` | `PorHistorylog_Errorcode` |  |  |  |
| 7 | `PPPHI.AdditionalInformation` | `PorHistorylog_Additionalinformation` |  |  |  |
