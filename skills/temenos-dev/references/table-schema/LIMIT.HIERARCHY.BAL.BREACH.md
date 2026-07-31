# LIMIT.HIERARCHY.BAL.BREACH — Table Schema

> Source: `INSERTS/I_F.LIMIT.HIERARCHY.BAL.BREACH` in `LI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.LHBB.VALIDATION.CCY` | `LimitHierarchyBalBreach_ValidationCcy` | TField |  | Contains the currency of the breached validation limit |
| 2 | `LI.LHBB.UTILISATION.TOTAL` | `LimitHierarchyBalBreach_UtilisationTotal` | TField |  | Contains the sum of all underlying utilisation limits' internal amount in VALIDATION.CCY |
| 3 | `LI.LHBB.BREACHED.AMOUNT` | `LimitHierarchyBalBreach_BreachedAmount` | TField |  | Contains the breach to the validation limit in VALIDATION.CCY which is the difference between the UTILISATION.TOTAL and validation limit's internal amount |
| 4 | `LI.LHBB.UPDATED.DATE.TIME` | `LimitHierarchyBalBreach_UpdatedDateTime` |  |  |  |
| 5 | `LI.LHBB.RESERVED.10` | `LimitHierarchyBalBreach_Reserved10` | TField |  |  |
| 6 | `LI.LHBB.RESERVED.9` | `LimitHierarchyBalBreach_Reserved9` | TField |  |  |
| 7 | `LI.LHBB.RESERVED.8` | `LimitHierarchyBalBreach_Reserved8` | TField |  |  |
| 8 | `LI.LHBB.RESERVED.7` | `LimitHierarchyBalBreach_Reserved7` | TField |  |  |
| 9 | `LI.LHBB.RESERVED.6` | `LimitHierarchyBalBreach_Reserved6` | TField |  |  |
| 10 | `LI.LHBB.RESERVED.5` | `LimitHierarchyBalBreach_Reserved5` | TField |  |  |
| 11 | `LI.LHBB.RESERVED.4` | `LimitHierarchyBalBreach_Reserved4` | TField |  |  |
| 12 | `LI.LHBB.RESERVED.3` | `LimitHierarchyBalBreach_Reserved3` | TField |  |  |
| 13 | `LI.LHBB.RESERVED.2` | `LimitHierarchyBalBreach_Reserved2` | TField |  |  |
| 14 | `LI.LHBB.RESERVED.1` | `LimitHierarchyBalBreach_Reserved1` | TField |  |  |
