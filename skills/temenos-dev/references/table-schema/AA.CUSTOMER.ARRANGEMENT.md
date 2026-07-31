# AA.CUSTOMER.ARRANGEMENT — Table Schema

> Source: `INSERTS/I_F.AA.CUSTOMER.ARRANGEMENT` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CUSARR.PRODUCT.LINE` | `AaCustomerArrangement_ProductLine` |  |  |  |
| 2 | `AA.CUSARR.RESERVED5` | `AaCustomerArrangement_Reserved5` |  |  |  |
| 3 | `AA.CUSARR.RESERVED4` | `AaCustomerArrangement_Reserved4` |  |  |  |
| 4 | `AA.CUSARR.ARRANGEMENT` | `AaCustomerArrangement_Arrangement` |  |  |  |
| 5 | `AA.CUSARR.CUSTOMER.ROLE` | `AaCustomerArrangement_CustomerRole` |  |  |  |
| 6 | `AA.CUSARR.CURRENCY` | `AaCustomerArrangement_Currency` |  |  |  |
| 7 | `AA.CUSARR.PRODUCT.GROUP` | `AaCustomerArrangement_ProductGroup` |  |  |  |
| 8 | `AA.CUSARR.MASS.CUSTOMER.UPDATE` | `AaCustomerArrangement_MassCustomerUpdate` | TField |  | Indicates the flag whether any one of the customer arrangement information was updated on AA.MASS.CUSTOMER.ARRANGEMENT. This flag will not be reversed even though the last customer arrangement was reversed or deleted. |
