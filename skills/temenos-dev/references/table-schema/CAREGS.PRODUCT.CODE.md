# CAREGS.PRODUCT.CODE — Table Schema

> Source: `INSERTS/I_F.CAREGS.PRODUCT.CODE` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.PRD.CODE.PRODUCT.CODE` | `CaregsProductCode_ProductCode` | TField |  | This field will be updated based on the field PRODUCT.TYPE.START.SEQ and based on the number defined, fetch the subsequent running sequence and incremented by 1.Note: if PRODUCT.TYPE.START.SEQ is not 1, then there must be some default codes, use the DEFAULT.PRODUCT.CODE and DESCRIPTION field to update the CAREGS.PRODUCT.CODE table. |
| 2 | `CDIC.PRD.CODE.PRODUCT.DESC` | `CaregsProductCode_ProductDesc` | TField |  |  |
| 3 | `CDIC.PRD.CODE.PRODUCT.GROUP.CODE` | `CaregsProductCode_ProductGroupCode` | TField |  | This field used to hold product group code. The product group code will be derived based on below.AA.PRODUCT.CATALOG&gt;PRD.GROUP.CODECATEGORY&gt;PRD.GROUP.CODE(or)APPL.GEN.CONDITION setup |
