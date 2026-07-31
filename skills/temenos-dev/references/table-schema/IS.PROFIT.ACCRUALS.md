# IS.PROFIT.ACCRUALS — Table Schema

> Source: `INSERTS/I_F.IS.PROFIT.ACCRUALS` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.IPA.FROM.DATE` | `IsProfitAccruals_FromDate` |  |  |  |
| 2 | `IS.IPA.TO.DATE` | `IsProfitAccruals_ToDate` |  |  |  |
| 3 | `IS.IPA.DAYS` | `IsProfitAccruals_Days` |  |  |  |
| 4 | `IS.IPA.BALANCE` | `IsProfitAccruals_Balance` |  |  |  |
| 5 | `IS.IPA.BASIS` | `IsProfitAccruals_Basis` |  |  |  |
| 6 | `IS.IPA.RATE` | `IsProfitAccruals_Rate` |  |  |  |
| 7 | `IS.IPA.ACCRUAL.AMT` | `IsProfitAccruals_AccrualAmt` |  |  |  |
| 8 | `IS.IPA.ACCT.ACC.AMT` | `IsProfitAccruals_AcctAccAmt` |  |  |  |
| 9 | `IS.IPA.RESERVED.9` | `IsProfitAccruals_Reserved9` |  |  |  |
| 10 | `IS.IPA.RESERVED.8` | `IsProfitAccruals_Reserved8` |  |  |  |
| 11 | `IS.IPA.PERIOD.START` | `IsProfitAccruals_PeriodStart` |  |  |  |
| 12 | `IS.IPA.PERIOD.END` | `IsProfitAccruals_PeriodEnd` |  |  |  |
| 13 | `IS.IPA.TOT.ACCRUAL.AMT` | `IsProfitAccruals_TotAccrualAmt` |  |  |  |
| 14 | `IS.IPA.TOT.DUE.AMT` | `IsProfitAccruals_TotDueAmt` |  |  |  |
| 15 | `IS.IPA.TOT.POS.ACCR.AMT` | `IsProfitAccruals_TotPosAccrAmt` |  |  |  |
| 16 | `IS.IPA.TOT.NEG.ACCR.AMT` | `IsProfitAccruals_TotNegAccrAmt` |  |  |  |
| 17 | `IS.IPA.RESERVED.7` | `IsProfitAccruals_Reserved7` |  |  |  |
| 18 | `IS.IPA.RESERVED.6` | `IsProfitAccruals_Reserved6` |  |  |  |
| 19 | `IS.IPA.RESERVED.5` | `IsProfitAccruals_Reserved5` |  |  |  |
| 20 | `IS.IPA.RESERVED.4` | `IsProfitAccruals_Reserved4` |  |  |  |
| 21 | `IS.IPA.RESERVED.3` | `IsProfitAccruals_Reserved3` | TField |  |  |
| 22 | `IS.IPA.RESERVED.2` | `IsProfitAccruals_Reserved2` | TField |  |  |
| 23 | `IS.IPA.RESERVED.1` | `IsProfitAccruals_Reserved1` | TField |  |  |
