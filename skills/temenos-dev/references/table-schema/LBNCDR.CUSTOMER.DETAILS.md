# LBNCDR.CUSTOMER.DETAILS — Table Schema

> Source: `INSERTS/I_F.LBNCDR.CUSTOMER.DETAILS` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDR.CUST.DETAIL.CONSOL.KEY` | `LbncdrCustomerDetails_ConsolKey` |  |  |  |
| 2 | `CDR.CUST.DETAIL.RESERVED.1` | `LbncdrCustomerDetails_Reserved1` | TField |  | Validation Rules |
| 3 | `CDR.CUST.DETAIL.RESERVED.2` | `LbncdrCustomerDetails_Reserved2` | TField |  | Validation Rules |
| 4 | `CDR.CUST.DETAIL.RESERVED.3` | `LbncdrCustomerDetails_Reserved3` | TField |  | Validation Rules |
| 5 | `CDR.CUST.DETAIL.RESERVED.4` | `LbncdrCustomerDetails_Reserved4` | TField |  | Validation Rules |
| 6 | `CDR.CUST.DETAIL.RESERVED.5` | `LbncdrCustomerDetails_Reserved5` | TField |  | Validation Rules |
| 7 | `CDR.CUST.DETAIL.RESERVED.6` | `LbncdrCustomerDetails_Reserved6` | TField |  | Validation Rules |
| 8 | `CDR.CUST.DETAIL.RESERVED.7` | `LbncdrCustomerDetails_Reserved7` | TField |  | Validation Rules |
| 9 | `CDR.CUST.DETAIL.RESERVED.8` | `LbncdrCustomerDetails_Reserved8` | TField |  | Validation Rules |
| 10 | `CDR.CUST.DETAIL.LOCAL.REF` | `LbncdrCustomerDetails_LocalRef` |  |  |  |
| 11 | `CDR.CUST.DETAIL.OVERRIDE` | `LbncdrCustomerDetails_Override` |  |  |  |
