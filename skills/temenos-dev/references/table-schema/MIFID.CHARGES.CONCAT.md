# MIFID.CHARGES.CONCAT — Table Schema

> Source: `INSERTS/I_F.MIFID.CHARGES.CONCAT` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFID.CHG.CONCAT.MIFID.CHARGES` | `MifidChargesConcat_MifidCharges` | TField |  | Specifies an MIFID.CHARGES belonging to the SEC.ACC.MASTER or AM.GROUP.PORT specified in field 0.The numbers of all MIFID.CHARGES belonging to the SEC.ACC.MASTER or AM.GROUP.PORT specified in Field 0 are held in fields 1 onwards, one MIFID.CHARGES per field.Validation Rules:Standard MIFID.CHARGES id format.Internal field. This is a NOINPUT field. |
