# ESLEND.MORTGAGE.APR.CASHFLOW — Table Schema

> Source: `INSERTS/I_F.ESLEND.MORTGAGE.APR.CASHFLOW` in `ESLEND_AprCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESLEND.CUSTOMER` | `EslendMortgageAprCashflow_Customer` | TField |  | This field denotes the customer related to the account |
| 2 | `ESLEND.INTEREST.BASIS` | `EslendMortgageAprCashflow_InterestBasis` | TField |  | This field denotes the Interest Basis of the underlying account |
| 3 | `ESLEND.APR.REQUIRED` | `EslendMortgageAprCashflow_AprRequired` | TField |  | This field holds Yes if APR calculation is required else it will have No |
| 4 | `ESLEND.CASH.FLOW.DATE` | `EslendMortgageAprCashflow_CashFlowDate` |  |  |  |
| 5 | `ESLEND.CASH.FLOW.TYPE` | `EslendMortgageAprCashflow_CashFlowType` |  |  |  |
| 6 | `ESLEND.CASH.FLOW.AMT` | `EslendMortgageAprCashflow_CashFlowAmt` |  |  |  |
