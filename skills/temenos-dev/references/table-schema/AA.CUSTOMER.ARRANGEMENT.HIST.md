# AA.CUSTOMER.ARRANGEMENT.HIST — Table Schema

> Source: `INSERTS/I_F.AA.CUSTOMER.ARRANGEMENT.HIST` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CUSARR.HIST.PRODUCT.LINE` | `AaCustomerArrangementHist_ProductLine` |  |  |  |
| 2 | `AA.CUSARR.HIST.RESERVED5` | `AaCustomerArrangementHist_Reserved5` |  |  |  |
| 3 | `AA.CUSARR.HIST.RESERVED4` | `AaCustomerArrangementHist_Reserved4` |  |  |  |
| 4 | `AA.CUSARR.HIST.ARRANGEMENT` | `AaCustomerArrangementHist_Arrangement` |  |  |  |
| 5 | `AA.CUSARR.HIST.CUSTOMER.ROLE` | `AaCustomerArrangementHist_CustomerRole` |  |  |  |
| 6 | `AA.CUSARR.HIST.CURRENCY` | `AaCustomerArrangementHist_Currency` |  |  |  |
| 7 | `AA.CUSARR.HIST.PRODUCT.GROUP` | `AaCustomerArrangementHist_ProductGroup` |  |  |  |
| 8 | `AA.CUSARR.HIST.MASS.CUSTOMER.UPDATE` | `AaCustomerArrangementHist_MassCustomerUpdate` | TField |  | Indicates the flag whether any one of the customer arrangement information was updated on AA.MASS.CUSTOMER.ARRANGEMENT.HIST. This flag will not be reversed even though the last customer arrangement was archived or deleted. |
