# DEBA18.CREDIT.EXP.RESULT — Table Schema

> Source: `INSERTS/I_F.DEBA18.CREDIT.EXP.RESULT` in `DEBA18_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEBA18.RESULT.CUSTOMER.GROUP` | `Deba18CreditExpResult_CustomerGroup` | TField |  |  |
| 2 | `DEBA18.RESULT.CUSTOMER` | `Deba18CreditExpResult_Customer` | TField |  |  |
| 3 | `DEBA18.RESULT.SECTOR` | `Deba18CreditExpResult_Sector` | TField |  |  |
| 4 | `DEBA18.RESULT.ACCOUNT` | `Deba18CreditExpResult_Account` |  |  |  |
| 5 | `DEBA18.RESULT.CREDIT.VOLUME` | `Deba18CreditExpResult_CreditVolume` | TField |  |  |
| 6 | `DEBA18.RESULT.AVAILABLE.BALANCE` | `Deba18CreditExpResult_AvailableBalance` | TField |  |  |
| 7 | `DEBA18.RESULT.DUE.BALANCE` | `Deba18CreditExpResult_DueBalance` | TField |  |  |
| 8 | `DEBA18.RESULT.COLLATERAL` | `Deba18CreditExpResult_Collateral` | TField |  |  |
| 9 | `DEBA18.RESULT.CUSTOMER.TOTAL` | `Deba18CreditExpResult_CustomerTotal` | TField |  |  |
| 10 | `DEBA18.RESULT.CUST.GROUP.TOTAL` | `Deba18CreditExpResult_CustGroupTotal` | TField |  |  |
