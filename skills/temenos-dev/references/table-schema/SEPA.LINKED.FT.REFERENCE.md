# SEPA.LINKED.FT.REFERENCE — Table Schema

> Source: `INSERTS/I_F.SEPA.LINKED.FT.REFERENCE` in `EP_InwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEPA.LINK.SEPA.APP.REF` | `SepaLinkedFtReference_SepaAppRef` | TField |  | This field holds the ID of SEPA.INWARD record to which the FT is linked The value is updated from SEPA.EXEC.INWARD.CB Validation Rules: Value upto 70 type ANY(Any Character) |
