# OA.CONDITIONAL.FORMLET.DETAILS — Table Schema

> Source: `INSERTS/I_F.OA.CONDITIONAL.FORMLET.DETAILS` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.CFD.FORM` | `OaConditionalFormletDetails_Form` |  |  |  |
| 2 | `OA.CFD.FORMLET` | `OaConditionalFormletDetails_Formlet` |  |  |  |
| 3 | `OA.CFD.STATUS.CODES` | `OaConditionalFormletDetails_StatusCodes` |  |  |  |
| 4 | `OA.CFD.RESERVED.5` | `OaConditionalFormletDetails_Reserved5` | TField |  |  |
| 5 | `OA.CFD.RESERVED.4` | `OaConditionalFormletDetails_Reserved4` | TField |  |  |
| 6 | `OA.CFD.RESERVED.3` | `OaConditionalFormletDetails_Reserved3` | TField |  |  |
| 7 | `OA.CFD.RESERVED.2` | `OaConditionalFormletDetails_Reserved2` | TField |  |  |
| 8 | `OA.CFD.RESERVED.1` | `OaConditionalFormletDetails_Reserved1` | TField |  |  |
