# MD.PART.CSN.BALANCES — Table Schema

> Source: `INSERTS/I_F.MD.PART.CSN.BALANCES` in `MD_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.PART.CURRENCY` | `MdPartCsnBalances_Currency` | TField |  | Currency in which commission is calculated. Validation Rules: System maintained. |
| 2 | `MD.PART.PRIN.EFF.DATE` | `MdPartCsnBalances_PrinEffDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `MD.PART.PRIN.BALANCE` | `MdPartCsnBalances_PrinBalance` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `MD.PART.TOTAL.COMM.AMT` | `MdPartCsnBalances_TotalCommAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `MD.PART.CSN.RATE` | `MdPartCsnBalances_CsnRate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `MD.PART.PART.CUST` | `MdPartCsnBalances_PartCust` |  |  |  |
| 7 | `MD.PART.CSN.START` | `MdPartCsnBalances_CsnStart` |  |  |  |
| 8 | `MD.PART.CSN.END` | `MdPartCsnBalances_CsnEnd` |  |  |  |
| 9 | `MD.PART.PART.CSN.AMT` | `MdPartCsnBalances_PartCsnAmt` |  |  |  |
| 10 | `MD.PART.CSN.AMT` | `MdPartCsnBalances_CsnAmt` |  |  |  |
| 11 | `MD.PART.TAX.AMT` | `MdPartCsnBalances_TaxAmt` |  |  |  |
| 12 | `MD.PART.PAST.CSN.ST` | `MdPartCsnBalances_PastCsnSt` |  |  |  |
| 13 | `MD.PART.PAST.CSN.END` | `MdPartCsnBalances_PastCsnEnd` |  |  |  |
| 14 | `MD.PART.PAST.CSN.AMT` | `MdPartCsnBalances_PastCsnAmt` |  |  |  |
| 15 | `MD.PART.PAST.CSN.TAX` | `MdPartCsnBalances_PastCsnTax` |  |  |  |
