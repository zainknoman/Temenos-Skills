# FICOLL.PRINCIPAL.BAL — Table Schema

> Source: `INSERTS/I_F.FICOLL.PRINCIPAL.BAL` in `FICOLL_GuarantiaGuarantee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.PRIN.MINUM.GTEE.DECREASE.VALUE` | `FicollPrincipalBal_MinumGteeDecreaseValue` | TField |  | It stores the Minimum monthly Garantia decrease value to be calculated. |
| 2 | `FICOLL.PRIN.PREV.PRINCIPAL.BALANCE` | `FicollPrincipalBal_PrevPrincipalBalance` | TField |  | It stores the CURACCOUNT balance of the account before the payment frequency. |
| 3 | `FICOLL.PRIN.CURR.PRINCIPAL.BALANCE` | `FicollPrincipalBal_CurrPrincipalBalance` | TField |  | It stores the CURACCOUNT balance of the account after the payment frequency. |
| 4 | `FICOLL.PRIN.PRIN.REPAYMENT.PERC` | `FicollPrincipalBal_PrinRepaymentPerc` | TField |  | It stores the percentage of the principal decrease in a month. |
| 5 | `FICOLL.PRIN.GTEE.REDUCE.VALUE` | `FicollPrincipalBal_GteeReduceValue` | TField |  | It stores the value calculated from the decrease Garanita Guarantee amount with percentage arrived on PRIN.REPYAMENT.PERC field. |
| 6 | `FICOLL.PRIN.HALG.FEES` | `FicollPrincipalBal_HalgFees` | TField |  | This field will be 'Yes' when Guarnatia/Bank fees is already paid. |
