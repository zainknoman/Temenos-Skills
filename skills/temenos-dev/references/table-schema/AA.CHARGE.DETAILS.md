# AA.CHARGE.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.CHARGE.DETAILS` in `AA_ActivityCharges.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CHG.DET.PAYMENT.DATE` | `AaChargeDetails_PaymentDate` |  |  |  |
| 2 | `AA.CHG.DET.BILL.ID` | `AaChargeDetails_BillId` |  |  |  |
| 3 | `AA.CHG.DET.AMOUNT` | `AaChargeDetails_Amount` |  |  |  |
| 4 | `AA.CHG.DET.AMOUNT.LCY` | `AaChargeDetails_AmountLcy` |  |  |  |
| 5 | `AA.CHG.DET.DEFAULT.AMT` | `AaChargeDetails_DefaultAmt` |  |  |  |
| 6 | `AA.CHG.DET.DEFAULT.AMT.LCY` | `AaChargeDetails_DefaultAmtLcy` |  |  |  |
| 7 | `AA.CHG.DET.WAIVE.AMOUNT` | `AaChargeDetails_WaiveAmount` |  |  |  |
| 8 | `AA.CHG.DET.WAIVE.AMOUNT.LCY` | `AaChargeDetails_WaiveAmountLcy` |  |  |  |
| 9 | `AA.CHG.DET.WAIVE.REASON` | `AaChargeDetails_WaiveReason` |  |  |  |
| 10 | `AA.CHG.DET.ADJ.AMT.TOTAL` | `AaChargeDetails_AdjAmtTotal` |  |  |  |
| 11 | `AA.CHG.DET.ADJ.AMT.TOTAL.LCY` | `AaChargeDetails_AdjAmtTotalLcy` |  |  |  |
| 12 | `AA.CHG.DET.RESERVED.3` | `AaChargeDetails_Reserved3` |  |  |  |
| 13 | `AA.CHG.DET.RESERVED.2` | `AaChargeDetails_Reserved2` |  |  |  |
| 14 | `AA.CHG.DET.RESERVED.1` | `AaChargeDetails_Reserved1` |  |  |  |
| 15 | `AA.CHG.DET.ARR.ACTIVITY.ID` | `AaChargeDetails_ArrActivityId` |  |  |  |
| 16 | `AA.CHG.DET.BILL.TYPE` | `AaChargeDetails_BillType` |  |  |  |
| 17 | `AA.CHG.DET.PAY.DATE` | `AaChargeDetails_PayDate` |  |  |  |
| 18 | `AA.CHG.DET.BILL.AMT` | `AaChargeDetails_BillAmt` |  |  |  |
| 19 | `AA.CHG.DET.BILL.AMT.LCY` | `AaChargeDetails_BillAmtLcy` |  |  |  |
| 20 | `AA.CHG.DET.DEF.BILL.AMT` | `AaChargeDetails_DefBillAmt` |  |  |  |
| 21 | `AA.CHG.DET.DEF.BILL.AMT.LCY` | `AaChargeDetails_DefBillAmtLcy` |  |  |  |
| 22 | `AA.CHG.DET.APP.PERIOD` | `AaChargeDetails_AppPeriod` |  |  |  |
| 23 | `AA.CHG.DET.APP.METHOD` | `AaChargeDetails_AppMethod` |  |  |  |
| 24 | `AA.CHG.DET.ADJUST.AMT` | `AaChargeDetails_AdjustAmt` |  |  |  |
| 25 | `AA.CHG.DET.ADJUST.REASON` | `AaChargeDetails_AdjustReason` |  |  |  |
| 26 | `AA.CHG.DET.ACTIVITY.ID` | `AaChargeDetails_ActivityId` |  |  |  |
| 27 | `AA.CHG.DET.CHG.CALC.TYPE` | `AaChargeDetails_ChgCalcType` |  |  |  |
| 28 | `AA.CHG.DET.SOURCE.BALANCE` | `AaChargeDetails_SourceBalance` |  |  |  |
| 29 | `AA.CHG.DET.TIER.BALANCE` | `AaChargeDetails_TierBalance` |  |  |  |
| 30 | `AA.CHG.DET.TIER.CALC.VALUE` | `AaChargeDetails_TierCalcValue` |  |  |  |
| 31 | `AA.CHG.DET.CALC.AMT` | `AaChargeDetails_CalcAmt` |  |  |  |
| 32 | `AA.CHG.DET.TIER.MAX.AMT` | `AaChargeDetails_TierMaxAmt` |  |  |  |
| 33 | `AA.CHG.DET.TIER.MIN.AMT` | `AaChargeDetails_TierMinAmt` |  |  |  |
| 34 | `AA.CHG.DET.TIER.CALC.AMT` | `AaChargeDetails_TierCalcAmt` |  |  |  |
| 35 | `AA.CHG.DET.TOT.TIER.CALC.AMT` | `AaChargeDetails_TotTierCalcAmt` |  |  |  |
| 36 | `AA.CHG.DET.FREE.AMT` | `AaChargeDetails_FreeAmt` |  |  |  |
| 37 | `AA.CHG.DET.CHG.AMT` | `AaChargeDetails_ChgAmt` |  |  |  |
| 38 | `AA.CHG.DET.MIN.CHG.AMT` | `AaChargeDetails_MinChgAmt` |  |  |  |
| 39 | `AA.CHG.DET.WAIVE.AMT` | `AaChargeDetails_WaiveAmt` |  |  |  |
| 40 | `AA.CHG.DET.FINAL.CHG.AMT` | `AaChargeDetails_FinalChgAmt` |  |  |  |
| 41 | `AA.CHG.DET.CHARGE.TYPE` | `AaChargeDetails_ChargeType` |  |  |  |
| 42 | `AA.CHG.DET.PAYMENT.TYPE` | `AaChargeDetails_PaymentType` |  |  |  |
| 43 | `AA.CHG.DET.BENEFIT.TYPE` | `AaChargeDetails_BenefitType` |  |  |  |
| 44 | `AA.CHG.DET.ADJUSTMENT.REASON` | `AaChargeDetails_AdjustmentReason` |  |  |  |
| 45 | `AA.CHG.DET.ADJUSTMENT.AMOUNT` | `AaChargeDetails_AdjustmentAmount` |  |  |  |
| 46 | `AA.CHG.DET.SOURCE.PAY.DATE.INFO` | `AaChargeDetails_SourcePayDateInfo` |  |  |  |
| 47 | `AA.CHG.DET.SOURCE.PAY.METHOD.INFO` | `AaChargeDetails_SourcePayMethodInfo` |  |  |  |
| 48 | `AA.CHG.DET.SOURCE.DATE.INFO` | `AaChargeDetails_SourceDateInfo` |  |  |  |
| 49 | `AA.CHG.DET.SOURCE.ACTUAL.TIER.AMOUNT.INFO` | `AaChargeDetails_SourceActualTierAmountInfo` |  |  |  |
| 50 | `AA.CHG.DET.SOURCE.ACTUAL.RATE.INFO` | `AaChargeDetails_SourceActualRateInfo` |  |  |  |
| 51 | `AA.CHG.DET.SOURCE.ADJ.TIER.AMOUNT.INFO` | `AaChargeDetails_SourceAdjTierAmountInfo` |  |  |  |
| 52 | `AA.CHG.DET.SOURCE.ADJ.RATE.INFO` | `AaChargeDetails_SourceAdjRateInfo` |  |  |  |
| 53 | `AA.CHG.DET.SOURCE.ACTUAL.AMOUNT` | `AaChargeDetails_SourceActualAmount` |  |  |  |
| 54 | `AA.CHG.DET.SOURCE.ACTUAL.TAX` | `AaChargeDetails_SourceActualTax` |  |  |  |
| 55 | `AA.CHG.DET.SOURCE.ADJ.AMOUNT` | `AaChargeDetails_SourceAdjAmount` |  |  |  |
| 56 | `AA.CHG.DET.SOURCE.ADJ.TAX` | `AaChargeDetails_SourceAdjTax` |  |  |  |
| 57 | `AA.CHG.DET.PAYMENT.PERIOD` | `AaChargeDetails_PaymentPeriod` |  |  |  |
