# INACCT.PART.WITHDRAW.INT.CALC — Table Schema

> Source: `INSERTS/I_F.INACCT.PART.WITHDRAW.INT.CALC` in `INACCT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INACCT.PART.WITHDRAW.ARRANGEMENT.CCY` | `InacctPartWithdrawIntCalc_ArrangementCcy` | TField |  | The currency of deposit arrangement |
| 2 | `INACCT.PART.WITHDRAW.PARTIAL.WD.DATE` | `InacctPartWithdrawIntCalc_PartialWdDate` |  |  |  |
| 3 | `INACCT.PART.WITHDRAW.PARTIAL.WD.AMOUNT` | `InacctPartWithdrawIntCalc_PartialWdAmount` |  |  |  |
| 4 | `INACCT.PART.WITHDRAW.PART.WITHDRAW.AMOUNT` | `InacctPartWithdrawIntCalc_PartWithdrawAmount` |  |  |  |
| 5 | `INACCT.PART.WITHDRAW.FROM.DATE` | `InacctPartWithdrawIntCalc_FromDate` |  |  |  |
| 6 | `INACCT.PART.WITHDRAW.TO.DATE` | `InacctPartWithdrawIntCalc_ToDate` |  |  |  |
| 7 | `INACCT.PART.WITHDRAW.DAYS` | `InacctPartWithdrawIntCalc_Days` |  |  |  |
| 8 | `INACCT.PART.WITHDRAW.BALANCE` | `InacctPartWithdrawIntCalc_Balance` |  |  |  |
| 9 | `INACCT.PART.WITHDRAW.RUN.RATE.INTEREST.RATE` | `InacctPartWithdrawIntCalc_RunRateInterestRate` |  |  |  |
| 10 | `INACCT.PART.WITHDRAW.RUN.RATE.INTEREST.AMOUNT` | `InacctPartWithdrawIntCalc_RunRateInterestAmount` |  |  |  |
| 11 | `INACCT.PART.WITHDRAW.PART.WD.BALANCE` | `InacctPartWithdrawIntCalc_PartWdBalance` |  |  |  |
| 12 | `INACCT.PART.WITHDRAW.PART.WD.PAID.INTEREST.AMOUNT` | `InacctPartWithdrawIntCalc_PartWdPaidInterestAmount` |  |  |  |
| 13 | `INACCT.PART.WITHDRAW.PI.BI.KEY` | `InacctPartWithdrawIntCalc_PiBiKey` |  |  |  |
| 14 | `INACCT.PART.WITHDRAW.PART.WD.INTEREST.RATE` | `InacctPartWithdrawIntCalc_PartWdInterestRate` |  |  |  |
| 15 | `INACCT.PART.WITHDRAW.TOT.PART.WD.PAID.INT.AMOUNT` | `InacctPartWithdrawIntCalc_TotPartWdPaidIntAmount` |  |  |  |
| 16 | `INACCT.PART.WITHDRAW.TOT.RUN.RATE.INTEREST.AMOUNT` | `InacctPartWithdrawIntCalc_TotRunRateInterestAmount` |  |  |  |
| 17 | `INACCT.PART.WITHDRAW.PENALTY.INTEREST.RATE` | `InacctPartWithdrawIntCalc_PenaltyInterestRate` |  |  |  |
| 18 | `INACCT.PART.WITHDRAW.TOT.PENALTY.INTEREST.AMOUNT` | `InacctPartWithdrawIntCalc_TotPenaltyInterestAmount` |  |  |  |
| 19 | `INACCT.PART.WITHDRAW.CALC.EXCESS.INT.PAID.AMOUNT` | `InacctPartWithdrawIntCalc_CalcExcessIntPaidAmount` |  |  |  |
| 20 | `INACCT.PART.WITHDRAW.EXCESS.INT.PAID.DATE` | `InacctPartWithdrawIntCalc_ExcessIntPaidDate` |  |  |  |
| 21 | `INACCT.PART.WITHDRAW.EXCESS.INT.PAID.FLAG` | `InacctPartWithdrawIntCalc_ExcessIntPaidFlag` |  |  |  |
| 22 | `INACCT.PART.WITHDRAW.DATE` | `InacctPartWithdrawIntCalc_Date` |  |  |  |
| 23 | `INACCT.PART.WITHDRAW.LATEST.EXCESS.INT.PAID.AMOUNT` | `InacctPartWithdrawIntCalc_LatestExcessIntPaidAmount` |  |  |  |
| 24 | `INACCT.PART.WITHDRAW.LATEST.EXCESS.INT.PAID.DATE` | `InacctPartWithdrawIntCalc_LatestExcessIntPaidDate` |  |  |  |
| 25 | `INACCT.PART.WITHDRAW.BALANCE.INT.PAID.AMOUNT` | `InacctPartWithdrawIntCalc_BalanceIntPaidAmount` |  |  |  |
