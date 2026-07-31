# OA.SCHEDULED.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.OA.SCHEDULED.ACTIVITY` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.SA.ACTIVITY.NAME` | `OaScheduledActivity_ActivityName` |  |  |  |
| 2 | `OA.SA.RESERVED.10` | `OaScheduledActivity_Reserved10` |  |  |  |
| 3 | `OA.SA.PURPOSE` | `OaScheduledActivity_Purpose` |  |  |  |
| 4 | `OA.SA.RESERVED.8` | `OaScheduledActivity_Reserved8` |  |  |  |
| 5 | `OA.SA.LAST.DATE` | `OaScheduledActivity_LastDate` |  |  |  |
| 6 | `OA.SA.RESERVED.7` | `OaScheduledActivity_Reserved7` |  |  |  |
| 7 | `OA.SA.RESERVED.6` | `OaScheduledActivity_Reserved6` |  |  |  |
| 8 | `OA.SA.NEXT.DATE` | `OaScheduledActivity_NextDate` |  |  |  |
| 9 | `OA.SA.RESERVED.5` | `OaScheduledActivity_Reserved5` | TField |  |  |
| 10 | `OA.SA.RESERVED.4` | `OaScheduledActivity_Reserved4` | TField |  |  |
| 11 | `OA.SA.NEXT.RUN.DATE` | `OaScheduledActivity_NextRunDate` | TField |  |  |
| 12 | `OA.SA.RESERVED.3` | `OaScheduledActivity_Reserved3` | TField |  |  |
| 13 | `OA.SA.RESERVED.2` | `OaScheduledActivity_Reserved2` | TField |  |  |
| 14 | `OA.SA.RESERVED.1` | `OaScheduledActivity_Reserved1` | TField |  |  |
