# SC.TRADE.POS.HISTORY — Table Schema

> Source: `INSERTS/I_F.SC.TRADE.POS.HISTORY` in `SC_SctDealerBookPosition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TPH.DAY` | `ScTradePosHistory_Day` |  |  |  |
| 2 | `SC.TPH.POSITION` | `ScTradePosHistory_Position` |  |  |  |
| 3 | `SC.TPH.COST.OF.POSN` | `ScTradePosHistory_CostOfPosn` |  |  |  |
| 4 | `SC.TPH.CPN.ACCR.POSTED` | `ScTradePosHistory_CpnAccrPosted` |  |  |  |
| 5 | `SC.TPH.TAX.BALANCE` | `ScTradePosHistory_TaxBalance` |  |  |  |
| 6 | `SC.TPH.DISC.ACCRUED` | `ScTradePosHistory_DiscAccrued` |  |  |  |
| 7 | `SC.TPH.CONSOL.TRD.BAL` | `ScTradePosHistory_ConsolTrdBal` |  |  |  |
| 8 | `SC.TPH.CONTINGENT.B.CR` | `ScTradePosHistory_ContingentBCr` |  |  |  |
| 9 | `SC.TPH.CONTINGENT.B.DB` | `ScTradePosHistory_ContingentBDb` |  |  |  |
| 10 | `SC.TPH.AVERAGE.PRICE` | `ScTradePosHistory_AveragePrice` |  |  |  |
| 11 | `SC.TPH.REALIZED.PL` | `ScTradePosHistory_RealizedPl` |  |  |  |
| 12 | `SC.TPH.VAL.DATED.POSN` | `ScTradePosHistory_ValDatedPosn` |  |  |  |
| 13 | `SC.TPH.V.D.COST.OF.POS` | `ScTradePosHistory_VDCostOfPos` |  |  |  |
| 14 | `SC.TPH.V.D.CPN.ACCRUED` | `ScTradePosHistory_VDCpnAccrued` |  |  |  |
| 15 | `SC.TPH.V.D.REAL.PROFIT` | `ScTradePosHistory_VDRealProfit` |  |  |  |
| 16 | `SC.TPH.V.D.DISC.ACCR` | `ScTradePosHistory_VDDiscAccr` |  |  |  |
| 17 | `SC.TPH.DATE` | `ScTradePosHistory_Date` |  |  |  |
| 18 | `SC.TPH.CPN.ACCR` | `ScTradePosHistory_CpnAccr` |  |  |  |
| 19 | `SC.TPH.CPN.DATE` | `ScTradePosHistory_CpnDate` |  |  |  |
| 20 | `SC.TPH.CPN.AMOUNT` | `ScTradePosHistory_CpnAmount` |  |  |  |
| 21 | `SC.TPH.DIFF.AMOUNT` | `ScTradePosHistory_DiffAmount` |  |  |  |
| 22 | `SC.TPH.SETTLED.POSN` | `ScTradePosHistory_SettledPosn` |  |  |  |
| 23 | `SC.TPH.COST.OF.SET.POS` | `ScTradePosHistory_CostOfSetPos` |  |  |  |
| 24 | `SC.TPH.FUNDING.AMOUNT` | `ScTradePosHistory_FundingAmount` |  |  |  |
| 25 | `SC.TPH.MTD.REALISED.PL` | `ScTradePosHistory_MtdRealisedPl` |  |  |  |
| 26 | `SC.TPH.YTD.REALISED.PL` | `ScTradePosHistory_YtdRealisedPl` |  |  |  |
| 27 | `SC.TPH.MTD.COUPON.ACCR` | `ScTradePosHistory_MtdCouponAccr` |  |  |  |
| 28 | `SC.TPH.YTD.COUPON.ACCR` | `ScTradePosHistory_YtdCouponAccr` |  |  |  |
| 29 | `SC.TPH.V.D.DISC.SOLD` | `ScTradePosHistory_VDDiscSold` |  |  |  |
| 30 | `SC.TPH.AVERAGE.YIELD` | `ScTradePosHistory_AverageYield` |  |  |  |
| 31 | `SC.TPH.CAP.INT.AMT` | `ScTradePosHistory_CapIntAmt` |  |  |  |
| 32 | `SC.TPH.CONT.INT.PAID` | `ScTradePosHistory_ContIntPaid` |  |  |  |
| 33 | `SC.TPH.CONT.INT.RECD` | `ScTradePosHistory_ContIntRecd` |  |  |  |
| 34 | `SC.TPH.CONT.DISCOUNT` | `ScTradePosHistory_ContDiscount` |  |  |  |
| 35 | `SC.TPH.CONT.CAP.INT.PAID` | `ScTradePosHistory_ContCapIntPaid` |  |  |  |
| 36 | `SC.TPH.CONT.CAP.INT.RECD` | `ScTradePosHistory_ContCapIntRecd` |  |  |  |
| 37 | `SC.TPH.CONT.BELG.TAX` | `ScTradePosHistory_ContBelgTax` |  |  |  |
| 38 | `SC.TPH.CON.TRD.BAL.LCY` | `ScTradePosHistory_ConTrdBalLcy` |  |  |  |
| 39 | `SC.TPH.EFF.INT.RATE` | `ScTradePosHistory_EffIntRate` |  |  |  |
