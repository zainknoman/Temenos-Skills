# OA.CONDITIONAL.EVIDENCE.DETAILS — Table Schema

> Source: `INSERTS/I_F.OA.CONDITIONAL.EVIDENCE.DETAILS` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.CED.FORM` | `OaConditionalEvidenceDetails_Form` |  |  |  |
| 2 | `OA.CED.FORMLET` | `OaConditionalEvidenceDetails_Formlet` |  |  |  |
| 3 | `OA.CED.STATUS.CODES` | `OaConditionalEvidenceDetails_StatusCodes` |  |  |  |
| 4 | `OA.CED.ASSOC.FORMLET` | `OaConditionalEvidenceDetails_AssocFormlet` |  |  |  |
| 5 | `OA.CED.RESERVED.5` | `OaConditionalEvidenceDetails_Reserved5` | TField |  |  |
| 6 | `OA.CED.RESERVED.4` | `OaConditionalEvidenceDetails_Reserved4` | TField |  |  |
| 7 | `OA.CED.RESERVED.3` | `OaConditionalEvidenceDetails_Reserved3` | TField |  |  |
| 8 | `OA.CED.RESERVED.2` | `OaConditionalEvidenceDetails_Reserved2` | TField |  |  |
| 9 | `OA.CED.RESERVED.1` | `OaConditionalEvidenceDetails_Reserved1` | TField |  |  |
