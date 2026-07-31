# AA.PRODUCT — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT` in `AA_ProductManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PDT.DESCRIPTION` | `AaProduct_Description` |  |  |  |
| 2 | `AA.PDT.PRODUCT.GROUP` | `AaProduct_ProductGroup` | TField |  | This field denotes the name of product group to which the product belongs to.Should be a valid product group id. |
| 3 | `AA.PDT.PRODUCT.STATUS` | `AaProduct_ProductStatus` | TField |  | This field denotes the current status of the product. If the product was proofed lately it will hold the value &quot;PROOFED&quot;, similarly if the product was published lately it will hold the value &quot;PUBLISHED&quot; |
| 4 | `AA.PDT.PRODUCT.INTEGRITY` | `AaProduct_ProductIntegrity` | TField |  | Does not serve any purpose currently and is reserved for future use. |
| 5 | `AA.PDT.PRF.PROPERTY` | `AaProduct_PrfProperty` |  |  |  |
| 6 | `AA.PDT.PRF.AVAILABLE.DATE` | `AaProduct_PrfAvailableDate` | TField |  | This field denotes the available date when the product was last proofed |
| 7 | `AA.PDT.PRF.EXPIRY.DATE` | `AaProduct_PrfExpiryDate` | TField |  | This field denotes the expiry date when the product was last proofed |
| 8 | `AA.PDT.PRF.PROP.CONTROL.PROPERTY` | `AaProduct_PrfPropControlProperty` |  |  |  |
| 9 | `AA.PDT.RESERVED.3` | `AaProduct_Reserved3` | TField |  |  |
| 10 | `AA.PDT.CAT.PROPERTY` | `AaProduct_CatProperty` |  |  |  |
| 11 | `AA.PDT.PRODUCT.ERROR` | `AaProduct_ProductError` |  |  |  |
| 12 | `AA.PDT.REMEDY` | `AaProduct_Remedy` |  |  |  |
| 13 | `AA.PDT.CAT.AVAILABLE.DATE` | `AaProduct_CatAvailableDate` | TField |  | This field denotes the available date when the product was last cataloged. |
| 14 | `AA.PDT.CAT.EXPIRY.DATE` | `AaProduct_CatExpiryDate` | TField |  | This field denotes the expiry date when the product was last cataloged. |
| 15 | `AA.PDT.LAST.PUBLISHED` | `AaProduct_LastPublished` | TField |  | This field denotes the date when the record was last published. |
| 16 | `AA.PDT.AVAILABLE.DATE` | `AaProduct_AvailableDate` |  |  |  |
| 17 | `AA.PDT.AVAILABLE.COMPANY` | `AaProduct_AvailableCompany` |  |  |  |
| 18 | `AA.PDT.OWNING.COMPANY` | `AaProduct_OwningCompany` |  |  |  |
| 19 | `AA.PDT.CAT.PROP.CONTROL.PROPERTY` | `AaProduct_CatPropControlProperty` |  |  |  |
| 20 | `AA.PDT.GROUP.LEVEL` | `AaProduct_GroupLevel` | TField |  | This field is to differentiate between the FACILITY and DEAL Product. |
| 21 | `AA.PDT.AVAILABLE.COUNTRY` | `AaProduct_AvailableCountry` |  |  |  |
| 22 | `AA.PDT.AVAILABLE.REGION` | `AaProduct_AvailableRegion` |  |  |  |
| 23 | `AA.PDT.EPP.PRODUCT.GROUP` | `AaProduct_EppProductGroup` | TField | Yes | This field is allowed for a product group which begins with EPP to be specified. Only used when PRODUCT.GROUP is EPP.Mandatory when PRODUCT.GROUP is EPP. |
| 24 | `AA.PDT.EPP.PRODUCT.LINE` | `AaProduct_EppProductLine` | TField |  |  |
