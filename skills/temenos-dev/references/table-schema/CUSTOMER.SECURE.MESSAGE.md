# CUSTOMER.SECURE.MESSAGE — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.SECURE.MESSAGE` in `EB_ARC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUS.SEC.MSG.SECURE.MESSAGE.ID` | `CustomerSecureMessage_SecureMessageId` | TField |  | Specifies the secure message ids belonging to this Customer The number of secure message ids of this Customer are held one per field |
