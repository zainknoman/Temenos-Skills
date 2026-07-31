# CAPL.PLAN.ENTRIES — Table Schema

> Source: `INSERTS/I_F.CAPL.PLAN.ENTRIES` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PE.TXN.ENTRY` | `CaplPlanEntries_TxnEntry` |  |  |  |
| 2 | `CAPL.PE.RESERVED.10` | `CaplPlanEntries_Reserved10` |  |  |  |
| 3 | `CAPL.PE.RESERVED.9` | `CaplPlanEntries_Reserved9` | TField |  |  |
| 4 | `CAPL.PE.RESERVED.8` | `CaplPlanEntries_Reserved8` | TField |  |  |
| 5 | `CAPL.PE.RESERVED.7` | `CaplPlanEntries_Reserved7` | TField |  |  |
| 6 | `CAPL.PE.RESERVED.6` | `CaplPlanEntries_Reserved6` | TField |  |  |
| 7 | `CAPL.PE.RESERVED.5` | `CaplPlanEntries_Reserved5` | TField |  |  |
| 8 | `CAPL.PE.RESERVED.4` | `CaplPlanEntries_Reserved4` | TField |  |  |
| 9 | `CAPL.PE.RESERVED.3` | `CaplPlanEntries_Reserved3` | TField |  |  |
| 10 | `CAPL.PE.RESERVED.2` | `CaplPlanEntries_Reserved2` | TField |  |  |
| 11 | `CAPL.PE.RESERVED.1` | `CaplPlanEntries_Reserved1` | TField |  |  |
| 12 | `CAPL.PE.LOCAL.REF` | `CaplPlanEntries_LocalRef` |  |  |  |
| 13 | `CAPL.PE.OVERRIDE` | `CaplPlanEntries_Override` |  |  |  |
