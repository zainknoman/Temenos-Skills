# SL.LOAN.PART.BALANCES — Table Schema

> Source: `INSERTS/I_F.SL.LOAN.PART.BALANCES` in `SL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SLP.LOAN.CURRENCY` | `SlLoanPartBalances_LoanCurrency` | TField |  | Currency of the loan contract is updated in this field |
| 2 | `SLP.PART.INIT.LO.AMT` | `SlLoanPartBalances_PartInitLoAmt` | TField |  | This field is updated with the participant's share of the initial loan amount |
| 3 | `SLP.PR.OUTS.AMT` | `SlLoanPartBalances_PrOutsAmt` |  |  |  |
| 4 | `SLP.PR.AMT.MOVED` | `SlLoanPartBalances_PrAmtMoved` |  |  |  |
| 5 | `SLP.PR.AMT.INCR` | `SlLoanPartBalances_PrAmtIncr` |  |  |  |
| 6 | `SLP.PR.AMT.DECR` | `SlLoanPartBalances_PrAmtDecr` |  |  |  |
| 7 | `SLP.MVT.TYPE` | `SlLoanPartBalances_MvtType` |  |  |  |
| 8 | `SLP.MVT.AMT` | `SlLoanPartBalances_MvtAmt` |  |  |  |
| 9 | `SLP.PR.AMT.EFF.DATE` | `SlLoanPartBalances_PrAmtEffDate` |  |  |  |
| 10 | `SLP.STRT.PRD.INT` | `SlLoanPartBalances_StrtPrdInt` |  |  |  |
| 11 | `SLP.END.PRD.INT` | `SlLoanPartBalances_EndPrdInt` |  |  |  |
| 12 | `SLP.TOT.INT.AMT` | `SlLoanPartBalances_TotIntAmt` |  |  |  |
| 13 | `SLP.FLT.INT.AMT` | `SlLoanPartBalances_FltIntAmt` |  |  |  |
| 14 | `SLP.PRD.INT.AMT` | `SlLoanPartBalances_PrdIntAmt` |  |  |  |
| 15 | `SLP.INT.ON.RPY.AMT` | `SlLoanPartBalances_IntOnRpyAmt` |  |  |  |
| 16 | `SLP.BS.INT.AMT` | `SlLoanPartBalances_BsIntAmt` |  |  |  |
| 17 | `SLP.CAP.INT.AMT` | `SlLoanPartBalances_CapIntAmt` |  |  |  |
| 18 | `SLP.TAX.AMOUNT` | `SlLoanPartBalances_TaxAmount` |  |  |  |
| 19 | `SLP.OUTS.ACCR.INT` | `SlLoanPartBalances_OutsAccrInt` |  |  |  |
| 20 | `SLP.INT.RATE` | `SlLoanPartBalances_IntRate` |  |  |  |
| 21 | `SLP.CAP.RATE` | `SlLoanPartBalances_CapRate` |  |  |  |
| 22 | `SLP.INT.SPREAD` | `SlLoanPartBalances_IntSpread` |  |  |  |
| 23 | `SLP.INT.CAP.SPREAD` | `SlLoanPartBalances_IntCapSpread` |  |  |  |
| 24 | `SLP.SPL.INT.SPREAD` | `SlLoanPartBalances_SplIntSpread` |  |  |  |
| 25 | `SLP.SPL.INT.CAP.SPR` | `SlLoanPartBalances_SplIntCapSpr` |  |  |  |
| 26 | `SLP.INT.BASIS` | `SlLoanPartBalances_IntBasis` |  |  |  |
| 27 | `SLP.INT.RATE.TYPE` | `SlLoanPartBalances_IntRateType` |  |  |  |
| 28 | `SLP.RATE.EFF.DT` | `SlLoanPartBalances_RateEffDt` |  |  |  |
| 29 | `SLP.RET.INT.AMT` | `SlLoanPartBalances_RetIntAmt` |  |  |  |
| 30 | `SLP.RET.AC.OR.PL` | `SlLoanPartBalances_RetAcOrPl` |  |  |  |
| 31 | `SLP.RET.INT.DATE` | `SlLoanPartBalances_RetIntDate` |  |  |  |
| 32 | `SLP.PIK.REFERENCE` | `SlLoanPartBalances_PikReference` |  |  |  |
| 33 | `SLP.PIK.ST.DATE` | `SlLoanPartBalances_PikStDate` |  |  |  |
| 34 | `SLP.PIK.END.DATE` | `SlLoanPartBalances_PikEndDate` |  |  |  |
| 35 | `SLP.PIK.INT` | `SlLoanPartBalances_PikInt` |  |  |  |
| 36 | `SLP.PIK.CAP.INT.AMT` | `SlLoanPartBalances_PikCapIntAmt` |  |  |  |
| 37 | `SLP.PIK.RATE` | `SlLoanPartBalances_PikRate` |  |  |  |
| 38 | `SLP.PIK.RATE.EFF.DT` | `SlLoanPartBalances_PikRateEffDt` |  |  |  |
