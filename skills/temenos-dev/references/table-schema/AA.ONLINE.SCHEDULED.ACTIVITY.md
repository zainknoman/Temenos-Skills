# AA.ONLINE.SCHEDULED.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.AA.ONLINE.SCHEDULED.ACTIVITY` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.OSCH.ACTIVITY.NAME` | `AaOnlineScheduledActivity_ActivityName` |  |  |  |
| 2 | `AA.OSCH.LAST.DATE` | `AaOnlineScheduledActivity_LastDate` |  |  |  |
| 3 | `AA.OSCH.EVENT.DATE` | `AaOnlineScheduledActivity_EventDate` |  |  |  |
| 4 | `AA.OSCH.NEXT.DATE` | `AaOnlineScheduledActivity_NextDate` |  |  |  |
| 5 | `AA.OSCH.NEXT.RUN.DATE` | `AaOnlineScheduledActivity_NextRunDate` | TField |  |  |
| 6 | `AA.OSCH.EARLY.END.DATE` | `AaOnlineScheduledActivity_EarlyEndDate` | TField |  |  |
