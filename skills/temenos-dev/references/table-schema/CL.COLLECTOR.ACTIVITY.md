# CL.COLLECTOR.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.CL.COLLECTOR.ACTIVITY` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.COLLACT.ACTION` | `ClCollectorActivity_Action` |  |  |  |
| 2 | `CL.COLLACT.NO.ACTIONS` | `ClCollectorActivity_NoActions` |  |  |  |
| 3 | `CL.COLLACT.OUTCOME.CODE` | `ClCollectorActivity_OutcomeCode` |  |  |  |
| 4 | `CL.COLLACT.NO.OUTCOMES` | `ClCollectorActivity_NoOutcomes` |  |  |  |
| 5 | `CL.COLLACT.TOTOC.DUEAMT` | `ClCollectorActivity_TotocDueamt` |  |  |  |
| 6 | `CL.COLLACT.TOT.INCENTIVE.PTS` | `ClCollectorActivity_TotIncentivePts` | TField |  | This field will hold the total of incentive points allocated to the collector during the month. |
| 7 | `CL.COLLACT.COLLECTOR.ID` | `ClCollectorActivity_CollectorId` | TField |  | First component of the ID. |
| 8 | `CL.COLLACT.RESERVED.5` | `ClCollectorActivity_Reserved5` | TField |  |  |
| 9 | `CL.COLLACT.RESERVED.4` | `ClCollectorActivity_Reserved4` | TField |  |  |
| 10 | `CL.COLLACT.RESERVED.3` | `ClCollectorActivity_Reserved3` | TField |  |  |
| 11 | `CL.COLLACT.RESERVED.2` | `ClCollectorActivity_Reserved2` | TField |  |  |
| 12 | `CL.COLLACT.RESERVED.1` | `ClCollectorActivity_Reserved1` | TField |  |  |
