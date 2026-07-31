# ID.POOL.TRACKER — Table Schema

> Source: `INSERTS/I_F.ID.POOL.TRACKER` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPT.OPENING.DATE` | `IdPoolTracker_OpeningDate` | TField |  | The date from which the contract was linked to a Pool. Validation Rules: 1. Must be a standard T24 Date. |
| 2 | `ID.IPT.CURRENT.POOL` | `IdPoolTracker_CurrentPool` | TField |  | The Pool to which the contract was currently linked to. Validation Rules: 1. Must be a valid record from the table ID.POOL.PARAMETER. |
| 3 | `ID.IPT.POOL.CHANGE.DATE` | `IdPoolTracker_PoolChangeDate` | TField |  | Date on which the contract was linked to the current pool. Validation Rules: 1. Must be a standard T24 Date. |
| 4 | `ID.IPT.PREVIOUS.POOL` | `IdPoolTracker_PreviousPool` |  |  |  |
| 5 | `ID.IPT.POOL.START.DATE` | `IdPoolTracker_PoolStartDate` |  |  |  |
| 6 | `ID.IPT.POOL.END.DATE` | `IdPoolTracker_PoolEndDate` |  |  |  |
| 7 | `ID.IPT.RESERVED.5` | `IdPoolTracker_Reserved5` |  |  |  |
| 8 | `ID.IPT.RESERVED.4` | `IdPoolTracker_Reserved4` |  |  |  |
| 9 | `ID.IPT.RESERVED.3` | `IdPoolTracker_Reserved3` |  |  |  |
| 10 | `ID.IPT.RESERVED.2` | `IdPoolTracker_Reserved2` |  |  |  |
| 11 | `ID.IPT.RESERVED.1` | `IdPoolTracker_Reserved1` |  |  |  |
