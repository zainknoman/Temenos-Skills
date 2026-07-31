# NACUST.SCHEDULED.EVENTS — Table Schema

> Source: `INSERTS/I_F.NACUST.SCHEDULED.EVENTS` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NACUST.SCHEDULE.EVENT.NAME` | `NacustScheduledEvents_EventName` |  |  |  |
| 2 | `NACUST.SCHEDULE.LAST.DATE` | `NacustScheduledEvents_LastDate` |  |  |  |
| 3 | `NACUST.SCHEDULE.NEXT.DATE` | `NacustScheduledEvents_NextDate` |  |  |  |
| 4 | `NACUST.SCHEDULE.CONTEXT.NAME` | `NacustScheduledEvents_ContextName` |  |  |  |
| 5 | `NACUST.SCHEDULE.CONTEXT.VALUE` | `NacustScheduledEvents_ContextValue` |  |  |  |
| 6 | `NACUST.SCHEDULE.RESERVED.20` | `NacustScheduledEvents_Reserved20` |  |  |  |
| 7 | `NACUST.SCHEDULE.RESERVED.19` | `NacustScheduledEvents_Reserved19` |  |  |  |
| 8 | `NACUST.SCHEDULE.RESERVED.18` | `NacustScheduledEvents_Reserved18` |  |  |  |
| 9 | `NACUST.SCHEDULE.RESERVED.17` | `NacustScheduledEvents_Reserved17` |  |  |  |
| 10 | `NACUST.SCHEDULE.RESERVED.16` | `NacustScheduledEvents_Reserved16` |  |  |  |
| 11 | `NACUST.SCHEDULE.NEXT.RUN.DATE` | `NacustScheduledEvents_NextRunDate` | TField |  | Nearest NEXT.DATE from today. It would be the next run date for the event. Validation Rules Value should be in valid date format. |
| 12 | `NACUST.SCHEDULE.RESERVED.15` | `NacustScheduledEvents_Reserved15` | TField |  |  |
| 13 | `NACUST.SCHEDULE.RESERVED.14` | `NacustScheduledEvents_Reserved14` | TField |  |  |
| 14 | `NACUST.SCHEDULE.RESERVED.13` | `NacustScheduledEvents_Reserved13` | TField |  |  |
| 15 | `NACUST.SCHEDULE.RESERVED.12` | `NacustScheduledEvents_Reserved12` | TField |  |  |
| 16 | `NACUST.SCHEDULE.RESERVED.11` | `NacustScheduledEvents_Reserved11` | TField |  |  |
| 17 | `NACUST.SCHEDULE.RESERVED.10` | `NacustScheduledEvents_Reserved10` | TField |  |  |
| 18 | `NACUST.SCHEDULE.RESERVED.9` | `NacustScheduledEvents_Reserved9` | TField |  |  |
| 19 | `NACUST.SCHEDULE.RESERVED.8` | `NacustScheduledEvents_Reserved8` | TField |  |  |
| 20 | `NACUST.SCHEDULE.RESERVED.7` | `NacustScheduledEvents_Reserved7` | TField |  |  |
| 21 | `NACUST.SCHEDULE.RESERVED.6` | `NacustScheduledEvents_Reserved6` | TField |  |  |
| 22 | `NACUST.SCHEDULE.RESERVED.5` | `NacustScheduledEvents_Reserved5` | TField |  |  |
| 23 | `NACUST.SCHEDULE.RESERVED.4` | `NacustScheduledEvents_Reserved4` | TField |  |  |
| 24 | `NACUST.SCHEDULE.RESERVED.3` | `NacustScheduledEvents_Reserved3` | TField |  |  |
| 25 | `NACUST.SCHEDULE.RESERVED.2` | `NacustScheduledEvents_Reserved2` | TField |  |  |
| 26 | `NACUST.SCHEDULE.RESERVED.1` | `NacustScheduledEvents_Reserved1` | TField |  |  |
