# MIFDII.GROUP.CONCAT — Table Schema

> Source: `INSERTS/I_F.MIFDII.GROUP.CONCAT` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFDII.CONCAT.MIFDII.QUESTION.GROUP` | `MifdiiGroupConcat_MifdiiQuestionGroup` | TField |  | Specifies an MIFDII.QUESTION.GROUP belonging to the Company specified in field 0.The numbers of all MIFDII.QUESTION.GROUP belonging to the Company specified in Field 0 are held in fields 1 onwards, one MIFDII.QUESTION.GROUP per field.Validation Rules:Standard MIFDII.QUESTION.GROUP id format.Internal field. This is a NOINPUT field. |
