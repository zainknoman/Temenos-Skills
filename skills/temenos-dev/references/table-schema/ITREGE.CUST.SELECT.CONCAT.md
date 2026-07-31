# ITREGE.CUST.SELECT.CONCAT — Table Schema

> Source: `INSERTS/I_F.ITREGE.CUST.SELECT.CONCAT` in `ITREGE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ITREGE.CUST.CONCAT.CUSTOMER.NUMBER` | `ItregeCustSelectConcat_CustomerNumber` | TField |  | The id of the customer |
| 2 | `ITREGE.CUST.CONCAT.ACCOUNT.NUMBER` | `ItregeCustSelectConcat_AccountNumber` | TField |  | The id for the account |
| 3 | `ITREGE.CUST.CONCAT.RELATED.CUSTOMER` | `ItregeCustSelectConcat_RelatedCustomer` | TField |  |  |
| 4 | `ITREGE.CUST.CONCAT.CARD.ISSUE.DATE` | `ItregeCustSelectConcat_CardIssueDate` | TField |  | Defines the date of issue of cards |
| 5 | `ITREGE.CUST.CONCAT.CARD.EXPIRY.DATE` | `ItregeCustSelectConcat_CardExpiryDate` | TField |  | Specifies the expiry date of the card being issued |
