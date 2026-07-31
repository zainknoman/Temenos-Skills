# LC.SCHEDULES — Table Schema

> Source: `INSERTS/I_F.LC.SCHEDULES` in `LC_Schedules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LC.SCH.PAY.SCH` | `LcSchedules_PaySch` | TField |  | Flag to process payment on instalment due date. |
| 2 | `LC.SCH.COMM.SCH` | `LcSchedules_CommSch` | TField |  | Flag to process commission on scheduled frequency date. |
| 3 | `LC.SCH.MSG.SCH` | `LcSchedules_MsgSch` | TField |  | Flag to process delivery messages on message scheduled date. |
| 4 | `LC.SCH.RESERVED.3` | `LcSchedules_Reserved3` |  |  |  |
| 5 | `LC.SCH.RESERVED.2` | `LcSchedules_Reserved2` | TField |  |  |
| 6 | `LC.SCH.RESERVED.1` | `LcSchedules_Reserved1` | TField |  |  |
