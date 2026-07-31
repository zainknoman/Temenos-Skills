# OA.POLICY.DEVIATION — Table Schema

> Source: `INSERTS/I_F.OA.POLICY.DEVIATION` in `OA_PolicyRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.PDE.POLICY.ITEM` | `OaPolicyDeviation_PolicyItem` |  |  |  |
| 2 | `OA.PDE.REFERENCE.DATA` | `OaPolicyDeviation_ReferenceData` |  |  |  |
| 3 | `OA.PDE.APPLICATION.DATA` | `OaPolicyDeviation_ApplicationData` |  |  |  |
| 4 | `OA.PDE.RULE.OUTCOME` | `OaPolicyDeviation_RuleOutcome` |  |  |  |
| 5 | `OA.PDE.DEVIATION` | `OaPolicyDeviation_Deviation` |  |  |  |
| 6 | `OA.PDE.RESERVED.2` | `OaPolicyDeviation_Reserved2` |  |  |  |
| 7 | `OA.PDE.RESERVED.1` | `OaPolicyDeviation_Reserved1` |  |  |  |
| 8 | `OA.PDE.RESERVED.3` | `OaPolicyDeviation_Reserved3` |  |  |  |
