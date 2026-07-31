# EV.SCHEDULED.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.EV.SCHEDULED.ACTIVITY` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVSA.EVIDENCE.ACTIVITY` | `EvScheduledActivity_EvidenceActivity` |  |  |  |
| 2 | `EV.EVSA.LAST.DATE` | `EvScheduledActivity_LastDate` |  |  |  |
| 3 | `EV.EVSA.NEXT.DATE` | `EvScheduledActivity_NextDate` |  |  |  |
| 4 | `EV.EVSA.NEXT.RUN.DATE` | `EvScheduledActivity_NextRunDate` | TField |  | This is the nearest date on which a activity is scheduled to run for this evidence. This is the lowest date among the NEXT.DATE fields. |
