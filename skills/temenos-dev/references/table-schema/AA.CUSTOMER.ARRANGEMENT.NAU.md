# AA.CUSTOMER.ARRANGEMENT.NAU — Table Schema

> Source: `INSERTS/I_F.AA.CUSTOMER.ARRANGEMENT.NAU` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CUSARR.NAU.PRODUCT.LINE` | `AaCustomerArrangementNau_ProductLine` |  |  |  |
| 2 | `AA.CUSARR.NAU.RESERVED5` | `AaCustomerArrangementNau_Reserved5` |  |  |  |
| 3 | `AA.CUSARR.NAU.RESERVED4` | `AaCustomerArrangementNau_Reserved4` |  |  |  |
| 4 | `AA.CUSARR.NAU.ARRANGEMENT` | `AaCustomerArrangementNau_Arrangement` |  |  |  |
| 5 | `AA.CUSARR.NAU.CUSTOMER.ROLE` | `AaCustomerArrangementNau_CustomerRole` |  |  |  |
| 6 | `AA.CUSARR.NAU.CURRENCY` | `AaCustomerArrangementNau_Currency` |  |  |  |
| 7 | `AA.CUSARR.NAU.PRODUCT.GROUP` | `AaCustomerArrangementNau_ProductGroup` |  |  |  |
| 8 | `AA.CUSARR.NAU.MASS.CUSTOMER.UPDATE` | `AaCustomerArrangementNau_MassCustomerUpdate` | TField |  |  |
