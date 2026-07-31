# LKWHTX.ARRANGEMENT.MONTHLY.TAX — Table Schema

> Source: `INSERTS/I_F.LKWHTX.ARRANGEMENT.MONTHLY.TAX` in `LKWHTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAX.PRODUCT.TYPE` | `LkwhtxArrangementMonthlyTax_ProductType` | TField |  | Defines the Product type of the arrangement. It should be a valid ID on AA.PRODUCT.GROUP application. |
| 2 | `TAX.ACCOUNT.OWNERSHIP` | `LkwhtxArrangementMonthlyTax_AccountOwnership` | TField |  | Defines whether the account has single or joint ownership. |
| 3 | `TAX.ARRANGEMENT.CURRENCY` | `LkwhtxArrangementMonthlyTax_ArrangementCurrency` | TField |  | Defines the currency of the arrangement. It should be a valid ID on CURRENCY application. |
| 4 | `TAX.TOTAL.INTEREST` | `LkwhtxArrangementMonthlyTax_TotalInterest` | TField |  | Defines the total interest value for the arrangement. |
| 5 | `TAX.CUSTOMER` | `LkwhtxArrangementMonthlyTax_Customer` |  |  |  |
| 6 | `TAX.INTEREST.JOINT.HOLDER` | `LkwhtxArrangementMonthlyTax_InterestJointHolder` |  |  |  |
| 7 | `TAX.WHT.RATE` | `LkwhtxArrangementMonthlyTax_WhtRate` |  |  |  |
| 8 | `TAX.WHT.DEDUCTED` | `LkwhtxArrangementMonthlyTax_WhtDeducted` |  |  |  |
| 9 | `TAX.PAYMENT.DATE` | `LkwhtxArrangementMonthlyTax_PaymentDate` |  |  |  |
| 10 | `TAX.LOCAL.REF` | `LkwhtxArrangementMonthlyTax_LocalRef` |  |  |  |
