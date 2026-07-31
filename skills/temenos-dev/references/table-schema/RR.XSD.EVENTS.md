# RR.XSD.EVENTS — Table Schema

> Source: `INSERTS/I_F.RR.XSD.EVENTS` in `EB_Streaming.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RR.XSD.TRANSACTION.TIME` | `RrXsdEvents_TransactionTime` | TField |  | Contains the event creation time. |
| 2 | `RR.XSD.PROCESSED.TIME` | `RrXsdEvents_ProcessedTime` | TField |  | Its for later use to update the time once the event is polled. |
| 3 | `RR.XSD.APPLICATION.ID` | `RrXsdEvents_ApplicationId` | TField |  | Contains the application name for the which the event is generated. |
| 4 | `RR.XSD.XSD` | `RrXsdEvents_Xsd` | TField |  | Contains the generated XSD of the application. If a table disabled from RR.PARAM this field will be updated with 'ADDED/REMOVED/DELISTED' message. |
| 5 | `RR.XSD.COMPANY` | `RrXsdEvents_Company` |  |  |  |
| 6 | `RR.XSD.FILE.SUFFIX` | `RrXsdEvents_FileSuffix` |  |  |  |
| 7 | `RR.XSD.ORCL.FILE.NAME` | `RrXsdEvents_OrclFileName` |  |  |  |
