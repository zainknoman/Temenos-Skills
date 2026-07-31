# AA.ARR.TRACKER.LIST — Table Schema

> Source: `INSERTS/I_F.AA.ARR.TRACKER.LIST` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ATL.TARGET.ARRANGEMENT` | `AaArrTrackerList_TargetArrangement` |  |  |  |
| 2 | `AA.ATL.CHANGED.PROPERTY` | `AaArrTrackerList_ChangedProperty` |  |  |  |
| 3 | `AA.ATL.RESERVED1` | `AaArrTrackerList_Reserved1` |  |  |  |
| 4 | `AA.ATL.RESERVED2` | `AaArrTrackerList_Reserved2` |  |  |  |
| 5 | `AA.ATL.RESERVED3` | `AaArrTrackerList_Reserved3` |  |  |  |
| 6 | `AA.ATL.RESERVED4` | `AaArrTrackerList_Reserved4` |  |  |  |
| 7 | `AA.ATL.RESERVED5` | `AaArrTrackerList_Reserved5` |  |  |  |
