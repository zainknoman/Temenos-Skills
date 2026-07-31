# AA.SCHEDULED.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.AA.SCHEDULED.ACTIVITY` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SCH.ACTIVITY.NAME` | `AaScheduledActivity_ActivityName` |  |  |  |
| 2 | `AA.SCH.LAST.DATE` | `AaScheduledActivity_LastDate` |  |  |  |
| 3 | `AA.SCH.EVENT.DATE` | `AaScheduledActivity_EventDate` |  |  |  |
| 4 | `AA.SCH.NEXT.DATE` | `AaScheduledActivity_NextDate` |  |  |  |
| 5 | `AA.SCH.NEXT.RUN.DATE` | `AaScheduledActivity_NextRunDate` | TField |  | This is the nearest date on which a activity is scheduled to run for this arrangement. This is the lowest date among the NEXT.DATE fields. |
| 6 | `AA.SCH.EARLY.END.DATE` | `AaScheduledActivity_EarlyEndDate` | TField |  | Field contains the last processed scheduled date as part of early schedule processing(AA.INTRADAY.PROCESS). This field only be updated for early processing contracts. |
