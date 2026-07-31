# CL.QUEUE.COLL — Table Schema

> Source: `INSERTS/I_F.CL.QUEUE.COLL` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.QC.COLLECTOR` | `ClQueueColl_Collector` |  |  |  |
| 2 | `CL.QC.LAST.ASSIGNED` | `ClQueueColl_LastAssigned` | TField |  | This field hold Collector who last assigned to collection item's |
| 3 | `CL.QC.RESERVED.5` | `ClQueueColl_Reserved5` | TField |  |  |
| 4 | `CL.QC.RESERVED.4` | `ClQueueColl_Reserved4` | TField |  |  |
| 5 | `CL.QC.RESERVED.3` | `ClQueueColl_Reserved3` | TField |  |  |
| 6 | `CL.QC.RESERVED.2` | `ClQueueColl_Reserved2` | TField |  |  |
| 7 | `CL.QC.RESERVED.1` | `ClQueueColl_Reserved1` | TField |  |  |
