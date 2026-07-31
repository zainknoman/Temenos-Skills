# PR.CUSTOMER.BALANCE — Table Schema

> Source: `INSERTS/I_F.PR.CUSTOMER.BALANCE` in `RE_ConBalanceUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PR.CUSTOMER` | `PrCustomerBalance_Customer` | TField |  | The customer to which the PR.CUSTOMER.BALANCE record belongs Third Party Customer id, who is not holding any account. |
| 2 | `PR.CURRENCY` | `PrCustomerBalance_Currency` | TField |  | Indicates the currency of the transaction. Validation Rules: 3 Alpha-numeric Currency code. Internal file, no input |
| 3 | `PR.CATEGORY` | `PrCustomerBalance_Category` | TField |  | Category that will be applied to the Payable / Receivable movements for the underlying transaction. For SEC.TRADE it will be set to '22000'. Validation Rules: 1 - 5 Character Category Code. (Internal System field.) Internal file, no input |
| 4 | `PR.PRODUCT` | `PrCustomerBalance_Product` | TField |  | Product for PR.CUSTOMER.BALANCE is 'PR' which is PAYABLE / RECEIVABLE |
| 5 | `PR.TXN.SUB.ASST.TYP` | `PrCustomerBalance_TxnSubAsstTyp` | TField |  |  |
| 6 | `PR.CRF.TYPES` | `PrCustomerBalance_CrfTypes` |  |  |  |
| 7 | `PR.MATURITY.DATE` | `PrCustomerBalance_MaturityDate` | TField |  | Maturity date is the value date of the transaction. Records in PR.CUSTOMER.BALANCE will be held upto the maturity date and no balance left for Payable / Receivable asset types Validation Rules: Standard Date Format Internal file, no input |
| 8 | `PR.LAST.AMEND.DATE` | `PrCustomerBalance_LastAmendDate` | TField |  | Date when the PR.CUSTOMER.BALANCE table is last updated with a change in CRF.TYPE or MATURITY.DATE fields. Validation Rules: Standard Date Format Internal file, no input |
| 9 | `PR.RESERVED.10` | `PrCustomerBalance_Reserved10` | TField |  |  |
| 10 | `PR.RESERVED.09` | `PrCustomerBalance_Reserved09` | TField |  |  |
| 11 | `PR.RESERVED.08` | `PrCustomerBalance_Reserved08` | TField |  |  |
| 12 | `PR.RESERVED.07` | `PrCustomerBalance_Reserved07` | TField |  |  |
| 13 | `PR.RESERVED.06` | `PrCustomerBalance_Reserved06` | TField |  |  |
| 14 | `PR.RESERVED.05` | `PrCustomerBalance_Reserved05` | TField |  |  |
| 15 | `PR.RESERVED.04` | `PrCustomerBalance_Reserved04` | TField |  |  |
| 16 | `PR.RESERVED.03` | `PrCustomerBalance_Reserved03` | TField |  |  |
| 17 | `PR.RESERVED.02` | `PrCustomerBalance_Reserved02` | TField |  |  |
| 18 | `PR.RESERVED.01` | `PrCustomerBalance_Reserved01` | TField |  |  |
