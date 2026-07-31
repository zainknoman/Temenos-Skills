# SL.LOAN.BALANCES — Table Schema

> Source: `INSERTS/I_F.SL.LOAN.BALANCES` in `SL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SLB.SL.CURRENCY` | `SlLoanBalances_SlCurrency` | TField |  | Holds the currency of the loan contract . |
| 2 | `SLB.SL.LOAN.INIT.AMT` | `SlLoanBalances_SlLoanInitAmt` | TField |  | Holds the initial loan amount from SL.LOAN record |
| 3 | `SLB.OUTS.CURR.AMT` | `SlLoanBalances_OutsCurrAmt` |  |  |  |
| 4 | `SLB.AMT.MOVED` | `SlLoanBalances_AmtMoved` |  |  |  |
| 5 | `SLB.INCR.AMT` | `SlLoanBalances_IncrAmt` |  |  |  |
| 6 | `SLB.DECR.AMT` | `SlLoanBalances_DecrAmt` |  |  |  |
| 7 | `SLB.MVT.TYPE` | `SlLoanBalances_MvtType` |  |  |  |
| 8 | `SLB.MVT.AMT` | `SlLoanBalances_MvtAmt` |  |  |  |
| 9 | `SLB.AMT.EFF.DATE` | `SlLoanBalances_AmtEffDate` |  |  |  |
| 10 | `SLB.OUTS.AMT.B.CCY` | `SlLoanBalances_OutsAmtBCcy` |  |  |  |
| 11 | `SLB.STRT.PRD.INT` | `SlLoanBalances_StrtPrdInt` |  |  |  |
| 12 | `SLB.END.PRD.INT` | `SlLoanBalances_EndPrdInt` |  |  |  |
| 13 | `SLB.TAX.AMOUNT` | `SlLoanBalances_TaxAmount` |  |  |  |
| 14 | `SLB.BS.INT.AMT` | `SlLoanBalances_BsIntAmt` |  |  |  |
| 15 | `SLB.COMMITED.INT` | `SlLoanBalances_CommitedInt` |  |  |  |
| 16 | `SLB.FLT.INT.AMT` | `SlLoanBalances_FltIntAmt` |  |  |  |
| 17 | `SLB.PRD.INT.AMT` | `SlLoanBalances_PrdIntAmt` |  |  |  |
| 18 | `SLB.INT.ON.RPY.AMT` | `SlLoanBalances_IntOnRpyAmt` |  |  |  |
| 19 | `SLB.CAP.INT.AMT` | `SlLoanBalances_CapIntAmt` |  |  |  |
| 20 | `SLB.INT.RATE` | `SlLoanBalances_IntRate` |  |  |  |
| 21 | `SLB.CAP.RATE` | `SlLoanBalances_CapRate` |  |  |  |
| 22 | `SLB.INT.SPREAD` | `SlLoanBalances_IntSpread` |  |  |  |
| 23 | `SLB.INT.CAP.SPREAD` | `SlLoanBalances_IntCapSpread` |  |  |  |
| 24 | `SLB.SPL.INT.SPREAD` | `SlLoanBalances_SplIntSpread` |  |  |  |
| 25 | `SLB.SPL.INT.CAP.SPR` | `SlLoanBalances_SplIntCapSpr` |  |  |  |
| 26 | `SLB.INT.BASIS` | `SlLoanBalances_IntBasis` |  |  |  |
| 27 | `SLB.INT.RATE.TYPE` | `SlLoanBalances_IntRateType` |  |  |  |
| 28 | `SLB.RATE.EFF.DT` | `SlLoanBalances_RateEffDt` |  |  |  |
| 29 | `SLB.RET.INT.AMT` | `SlLoanBalances_RetIntAmt` |  |  |  |
| 30 | `SLB.RET.AC.OR.PL` | `SlLoanBalances_RetAcOrPl` |  |  |  |
| 31 | `SLB.RET.INT.DATE` | `SlLoanBalances_RetIntDate` |  |  |  |
| 32 | `SLB.LAST.BS.DATE` | `SlLoanBalances_LastBsDate` | TField |  | This field is updated with the last BUY/SELL movement date for validation purposes |
| 33 | `SLB.NEXT.INT.REV.DT` | `SlLoanBalances_NextIntRevDt` | TField |  | This field defines the date on which next interest revision is scheduled |
| 34 | `SLB.LAST.INT.REV.DT` | `SlLoanBalances_LastIntRevDt` | TField |  | This field holds the date on which the last interest revision took place |
| 35 | `SLB.INT.BASE.DT` | `SlLoanBalances_IntBaseDt` | TField |  | In SL.REPAYMENT.SCHEDULES, if BASE.DATE is 'BASE', then the INTEREST base date is stored in this field based on the values in INT.DUE.FQY |
| 36 | `SLB.PRIN.BASE.DT` | `SlLoanBalances_PrinBaseDt` | TField |  | In SL.REPAYMENT.SCHEDULES, if BASE.DATE is 'BASE', then the Principal base date is stored in this field based on the values in NXT.RPT.DATE. |
| 37 | `SLB.RATE.BASE.DT` | `SlLoanBalances_RateBaseDt` | TField |  | In SL.REPAYMENT.SCHEDULES, if BASE.DATE is 'BASE', then the Rate schedule base date is stored in this field based on the values in R.SCH.FQU field |
| 38 | `SLB.PIK.REFERENCE` | `SlLoanBalances_PikReference` |  |  |  |
| 39 | `SLB.PIK.ST.DATE` | `SlLoanBalances_PikStDate` |  |  |  |
| 40 | `SLB.PIK.END.DATE` | `SlLoanBalances_PikEndDate` |  |  |  |
| 41 | `SLB.PIK.INT` | `SlLoanBalances_PikInt` |  |  |  |
| 42 | `SLB.PIK.INT.CAP.AMT` | `SlLoanBalances_PikIntCapAmt` |  |  |  |
| 43 | `SLB.PIK.RATE` | `SlLoanBalances_PikRate` |  |  |  |
| 44 | `SLB.PIK.RATE.EFF.DT` | `SlLoanBalances_PikRateEffDt` |  |  |  |
| 45 | `SLB.INT.START.DATE` | `SlLoanBalances_IntStartDate` | TField |  |  |
