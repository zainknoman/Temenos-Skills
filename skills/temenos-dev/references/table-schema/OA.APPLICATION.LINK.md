# OA.APPLICATION.LINK — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.LINK` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.AL.OA.APPLICATION` | `OaApplicationLink_OaApplication` |  |  |  |
| 2 | `OA.AL.CUSTOMER.ROLE` | `OaApplicationLink_CustomerRole` |  |  |  |
| 3 | `OA.AL.FORM.PURPOSE` | `OaApplicationLink_FormPurpose` |  |  |  |
| 4 | `OA.AL.FORM` | `OaApplicationLink_Form` |  |  |  |
| 5 | `OA.AL.FORM.REFERENCES` | `OaApplicationLink_FormReferences` |  |  |  |
