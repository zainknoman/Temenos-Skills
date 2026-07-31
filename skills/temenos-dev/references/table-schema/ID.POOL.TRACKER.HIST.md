# ID.POOL.TRACKER.HIST — Table Schema

> Source: `INSERTS/I_F.ID.POOL.TRACKER.HIST` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.PTH.OPENING.DATE` | `IdPoolTrackerHist_OpeningDate` | TField |  |  |
| 2 | `ID.PTH.CURRENT.POOL` | `IdPoolTrackerHist_CurrentPool` | TField |  |  |
| 3 | `ID.PTH.POOL.CHANGE.DATE` | `IdPoolTrackerHist_PoolChangeDate` | TField |  |  |
| 4 | `ID.PTH.PREVIOUS.POOL` | `IdPoolTrackerHist_PreviousPool` |  |  |  |
| 5 | `ID.PTH.POOL.START.DATE` | `IdPoolTrackerHist_PoolStartDate` |  |  |  |
| 6 | `ID.PTH.POOL.END.DATE` | `IdPoolTrackerHist_PoolEndDate` |  |  |  |
| 7 | `ID.PTH.RESERVED.5` | `IdPoolTrackerHist_Reserved5` |  |  |  |
| 8 | `ID.PTH.RESERVED.4` | `IdPoolTrackerHist_Reserved4` |  |  |  |
| 9 | `ID.PTH.RESERVED.3` | `IdPoolTrackerHist_Reserved3` |  |  |  |
| 10 | `ID.PTH.RESERVED.2` | `IdPoolTrackerHist_Reserved2` |  |  |  |
| 11 | `ID.PTH.RESERVED.1` | `IdPoolTrackerHist_Reserved1` |  |  |  |
