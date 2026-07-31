# AA.PURPOSE.PRODUCTS — Table Schema

> Source: `INSERTS/I_F.AA.PURPOSE.PRODUCTS` in `AA_ProductFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PP.PRODUCT` | `AaPurposeProducts_Product` | TField |  | This field will holds the list of products belongs to the current purpose. When user creates the marketing catalogue for this purpose then all the products that exist in this field would be displayed in the output of the marketing catalogue. |
