# SC.ENT.INCOME.SUPP — Table Schema

> Source: `INSERTS/I_F.SC.ENT.INCOME.SUPP` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.EIP.EFFECTIVE.DATE` | `ScEntIncomeSupp_EffectiveDate` |  |  |  |
| 2 | `SC.EIP.INCOME.TYPE` | `ScEntIncomeSupp_IncomeType` |  |  |  |
| 3 | `SC.EIP.CASH.NON.CASH` | `ScEntIncomeSupp_CashNonCash` |  |  |  |
| 4 | `SC.EIP.COST.ADJUSTED` | `ScEntIncomeSupp_CostAdjusted` |  |  |  |
| 5 | `SC.EIP.INCOME.CCY` | `ScEntIncomeSupp_IncomeCcy` |  |  |  |
| 6 | `SC.EIP.INCOME.AMT` | `ScEntIncomeSupp_IncomeAmt` |  |  |  |
| 7 | `SC.EIP.TOT.INCOME` | `ScEntIncomeSupp_TotIncome` | TField |  | Sum of INCOME.AMT from all multi-value groups is updated. |
