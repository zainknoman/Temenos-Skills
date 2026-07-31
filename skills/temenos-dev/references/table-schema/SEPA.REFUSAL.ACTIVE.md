# SEPA.REFUSAL.ACTIVE — Table Schema

> Source: `INSERTS/I_F.SEPA.REFUSAL.ACTIVE` in `EP_Refusal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.RACT.SEPA.REFUSAL.ID` | `SepaRefusalActive_SepaRefusalId` | TField |  | This field holds the value of Active SEPA.REFUSAL record ID's for the corresponding Account Validation Rules: Value upto 35 type ANY(Any Character) and Value must exists in SEPA.REFUSAL |
