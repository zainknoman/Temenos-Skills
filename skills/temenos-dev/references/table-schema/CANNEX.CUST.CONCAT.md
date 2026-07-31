# CANNEX.CUST.CONCAT — Table Schema

> Source: `INSERTS/I_F.CANNEX.CUST.CONCAT` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.CUS.CANNEX.CUSTOMER` | `CannexCustConcat_CannexCustomer` | TField |  | This field is used to define the Existing CIF or New CIF will be recorded to use for creating CANNEX Term Deposits. |
| 2 | `CANNEX.CUS.BENEFICIARY.ID` | `CannexCustConcat_BeneficiaryId` | TField |  |  |
| 3 | `CANNEX.CUS.RESERVED.2` | `CannexCustConcat_Reserved2` | TField |  |  |
| 4 | `CANNEX.CUS.RESERVED.3` | `CannexCustConcat_Reserved3` | TField |  |  |
| 5 | `CANNEX.CUS.RESERVED.4` | `CannexCustConcat_Reserved4` | TField |  |  |
| 6 | `CANNEX.CUS.RESERVED.5` | `CannexCustConcat_Reserved5` | TField |  |  |
| 7 | `CANNEX.CUS.RESERVED.6` | `CannexCustConcat_Reserved6` | TField |  |  |
| 8 | `CANNEX.CUS.RESERVED.7` | `CannexCustConcat_Reserved7` | TField |  |  |
| 9 | `CANNEX.CUS.RESERVED.8` | `CannexCustConcat_Reserved8` | TField |  |  |
| 10 | `CANNEX.CUS.RESERVED.9` | `CannexCustConcat_Reserved9` | TField |  |  |
| 11 | `CANNEX.CUS.RESERVED.10` | `CannexCustConcat_Reserved10` | TField |  |  |
| 12 | `CANNEX.CUS.LOCAL.REF` | `CannexCustConcat_LocalRef` |  |  |  |
| 13 | `CANNEX.CUS.OVERRIDE` | `CannexCustConcat_Override` |  |  |  |
