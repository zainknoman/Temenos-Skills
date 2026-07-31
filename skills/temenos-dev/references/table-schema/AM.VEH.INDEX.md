# AM.VEH.INDEX — Table Schema

> Source: `INSERTS/I_F.AM.VEH.INDEX` in `AM_ValuationHistorical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.VEH.IND.VEH.CONTAINER` | `AmVehIndex_VehContainer` | TField |  | This field identifies the container(file) in which the historical data is stored. |
| 2 | `AM.VEH.IND.STATUS` | `AmVehIndex_Status` | TField |  | This field indicates the availability of historical data. it can have two values.Active : This indicates that historical data for that month is currently available. Stale : This indicates that historical data is no longer available. |
| 3 | `AM.VEH.IND.RESERVED.03` | `AmVehIndex_Reserved03` | TField |  |  |
| 4 | `AM.VEH.IND.RESERVED.02` | `AmVehIndex_Reserved02` | TField |  |  |
| 5 | `AM.VEH.IND.RESERVED.01` | `AmVehIndex_Reserved01` | TField |  |  |
