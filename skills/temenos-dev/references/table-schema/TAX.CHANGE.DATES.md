# TAX.CHANGE.DATES — Table Schema

> Source: `INSERTS/I_F.TAX.CHANGE.DATES` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCD.EFF.DATE` | `TaxChangeDates_EffDate` | TField |  | Dates on which the tax rate changes. Multi value field. Validation Rules: This is a NoInput field. |
