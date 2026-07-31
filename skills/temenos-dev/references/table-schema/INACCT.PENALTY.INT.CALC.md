# INACCT.PENALTY.INT.CALC — Table Schema

> Source: `INSERTS/I_F.INACCT.PENALTY.INT.CALC` in `INACCT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INACCT.PENALTY.INT.FROM.DATE` | `InacctPenaltyIntCalc_FromDate` |  |  |  |
| 2 | `INACCT.PENALTY.INT.TO.DATE` | `InacctPenaltyIntCalc_ToDate` |  |  |  |
| 3 | `INACCT.PENALTY.INT.DAYS` | `InacctPenaltyIntCalc_Days` |  |  |  |
| 4 | `INACCT.PENALTY.INT.ARRANGEMENT.CCY` | `InacctPenaltyIntCalc_ArrangementCcy` |  |  |  |
| 5 | `INACCT.PENALTY.INT.BALANCE` | `InacctPenaltyIntCalc_Balance` |  |  |  |
| 6 | `INACCT.PENALTY.INT.INTEREST.RATE` | `InacctPenaltyIntCalc_InterestRate` |  |  |  |
| 7 | `INACCT.PENALTY.INT.INTEREST.AMOUNT` | `InacctPenaltyIntCalc_InterestAmount` |  |  |  |
| 8 | `INACCT.PENALTY.INT.PI.BI.KEY` | `InacctPenaltyIntCalc_PiBiKey` | TField |  | Periodic Key or Basic Interest Key that was used for deriving interest rate |
| 9 | `INACCT.PENALTY.INT.CALC.PENALTY.AMOUNT` | `InacctPenaltyIntCalc_CalcPenaltyAmount` | TField |  | Total Penalty Amount, which need to be recovered From the Customer |
| 10 | `INACCT.PENALTY.INT.DATE` | `InacctPenaltyIntCalc_Date` | TField |  | Date of penalty interest recovered. |
| 11 | `INACCT.PENALTY.INT.BUCKET.RATE` | `InacctPenaltyIntCalc_BucketRate` | TField |  | Actual Interest rate based on the run tenure, actual rate applied while processing redeem deposits. |
| 12 | `INACCT.PENALTY.INT.ACTUAL.INT.AMOUNT` | `InacctPenaltyIntCalc_ActualIntAmount` | TField |  | Actual Interest amount calculated based on the above bucketed rate and holds the latest Interest capitalisation amount. This amount will be used for TDS tax calculation. |
