# SC.TRAIL.FEES.EXTRACT — Table Schema

> Source: `INSERTS/I_F.SC.TRAIL.FEES.EXTRACT` in `SC_ScfTrailerFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TFE.SECURITY.NO` | `ScTrailFeesExtract_SecurityNo` | TField |  | Specifies the SECURITY.NO for which the extract was built |
| 2 | `SC.TFE.CUSTOMER` | `ScTrailFeesExtract_Customer` | TField |  | Specifies the Customer for whom the extract was built. |
| 3 | `SC.TFE.ISSUER` | `ScTrailFeesExtract_Issuer` | TField |  | Specifies the ISSUER for whom the EXTRACT is been created. |
| 4 | `SC.TFE.CALC.CCY` | `ScTrailFeesExtract_CalcCcy` | TField |  | Specifies the currency in which calculation is been made. It is updated by the system with the CALC.CCY set in corresponding SC.TRAIL.FEES.ARRANGEMENT record. |
| 5 | `SC.TFE.EXTRACT.DATE` | `ScTrailFeesExtract_ExtractDate` |  |  |  |
| 6 | `SC.TFE.NO.NOMINAL` | `ScTrailFeesExtract_NoNominal` |  |  |  |
| 7 | `SC.TFE.V.DATE.NOMINAL` | `ScTrailFeesExtract_VDateNominal` |  |  |  |
| 8 | `SC.TFE.PRICE` | `ScTrailFeesExtract_Price` |  |  |  |
| 9 | `SC.TFE.INDEX` | `ScTrailFeesExtract_Index` |  |  |  |
| 10 | `SC.TFE.TRAIL.REF.LEVEL` | `ScTrailFeesExtract_TrailRefLevel` |  |  |  |
| 11 | `SC.TFE.INIT.REF.LEVEL` | `ScTrailFeesExtract_InitRefLevel` |  |  |  |
| 12 | `SC.TFE.EXT.ACCR.AMT` | `ScTrailFeesExtract_ExtAccrAmt` |  |  |  |
| 13 | `SC.TFE.TR.FEE.RATE` | `ScTrailFeesExtract_TrFeeRate` |  |  |  |
| 14 | `SC.TFE.EX.RATE.CALC.LCY` | `ScTrailFeesExtract_ExRateCalcLcy` |  |  |  |
| 15 | `SC.TFE.ACCR.AMT.PAY.CCY` | `ScTrailFeesExtract_AccrAmtPayCcy` |  |  |  |
| 16 | `SC.TFE.EX.RATE.CALC.PAY` | `ScTrailFeesExtract_ExRateCalcPay` |  |  |  |
| 17 | `SC.TFE.BV.NO.NOMINAL` | `ScTrailFeesExtract_BvNoNominal` |  |  |  |
| 18 | `SC.TFE.BV.V.DATE.NOMINAL` | `ScTrailFeesExtract_BvVDateNominal` |  |  |  |
| 19 | `SC.TFE.BV.T.NO.NOMINAL` | `ScTrailFeesExtract_BvTNoNominal` |  |  |  |
| 20 | `SC.TFE.BV.T.V.DATE.NOMINAL` | `ScTrailFeesExtract_BvTVDateNominal` |  |  |  |
| 21 | `SC.TFE.BV.PRICE` | `ScTrailFeesExtract_BvPrice` |  |  |  |
| 22 | `SC.TFE.BV.INDEX` | `ScTrailFeesExtract_BvIndex` |  |  |  |
| 23 | `SC.TFE.BV.TRAIL.REF.LEVEL` | `ScTrailFeesExtract_BvTrailRefLevel` |  |  |  |
| 24 | `SC.TFE.BV.INIT.REF.LEVEL` | `ScTrailFeesExtract_BvInitRefLevel` |  |  |  |
| 25 | `SC.TFE.BV.EXT.ACCR.AMT` | `ScTrailFeesExtract_BvExtAccrAmt` |  |  |  |
| 26 | `SC.TFE.BV.TR.FEE.RATE` | `ScTrailFeesExtract_BvTrFeeRate` |  |  |  |
| 27 | `SC.TFE.BV.ACCR.AMT.PAY.CCY` | `ScTrailFeesExtract_BvAccrAmtPayCcy` |  |  |  |
| 28 | `SC.TFE.BV.MGMT.FEE.RATE` | `ScTrailFeesExtract_BvMgmtFeeRate` |  |  |  |
| 29 | `SC.TFE.RESERVED.6` | `ScTrailFeesExtract_Reserved6` |  |  |  |
| 30 | `SC.TFE.RESERVED.5` | `ScTrailFeesExtract_Reserved5` |  |  |  |
| 31 | `SC.TFE.MGMT.FEE.RATE` | `ScTrailFeesExtract_MgmtFeeRate` |  |  |  |
| 32 | `SC.TFE.RESERVED.3` | `ScTrailFeesExtract_Reserved3` |  |  |  |
| 33 | `SC.TFE.RESERVED.2` | `ScTrailFeesExtract_Reserved2` |  |  |  |
| 34 | `SC.TFE.RESERVED.1` | `ScTrailFeesExtract_Reserved1` |  |  |  |
| 35 | `SC.TFE.CALC.DATE` | `ScTrailFeesExtract_CalcDate` |  |  |  |
| 36 | `SC.TFE.TOT.ACCR.AMT.CALC.CCY` | `ScTrailFeesExtract_TotAccrAmtCalcCcy` | TField |  | Specifies the total accrual amount in calculation currency that is accrued till date |
| 37 | `SC.TFE.TOT.ACCR.AMT.PAY.CCY` | `ScTrailFeesExtract_TotAccrAmtPayCcy` | TField |  | Specifies the total accrual amount in equivalent payment currency that is accrued till date |
| 38 | `SC.TFE.BV.CALC.DATE` | `ScTrailFeesExtract_BvCalcDate` |  |  |  |
| 39 | `SC.TFE.BV.TOT.ACCR.AMT.CALC.CCY` | `ScTrailFeesExtract_BvTotAccrAmtCalcCcy` | TField |  | Specifies the total recalculated accrual amount in calculation currency that is accrued till date. EXAMPLE:- (The Back valuation process is Triggered After the Creation of the Payment record) :- CALC DATE \| EXTR.ACC.AMT 10-JAN-2008 \| 100 15-JAN-2008 \| 100 16-JAN-2008 \| 100 TOT.ACCR.AMT.CALC.CCY = 300 If the SECURITY price is changed on 15-JAN-2008 then the Back valuation process is triggered and Recalculation is done for the 15-JAN-2008, 16-JAN-2008 and it will Update in the BV.EXTR.ACC.AMT with the new recalculated values. The BV.CAL.DATE is updated with the value as 15-JAN-2008 and 16-JAN-2008. The sum of Recalculated price is stored in the BV.TOT.ACCR.AMT.CALC.CCY After Back valuation service:- CALC DATE \|EXTR.ACC.AMT\| BV.CALC.DATE \| BV.EXTR.ACC.AMT 10-JAN-2008 \| 100 \| \| 15-JAN-2008 \| 100 \| 15-JAN-2008 \| 110 16-JAN-2008 \| 100 \| 16-JAN-2008 \| 100 BV.TOT.ACCR.AMT.CALC.CCY = 310 |
| 40 | `SC.TFE.BV.TOT.ACCR.AMT.PAY.CCY` | `ScTrailFeesExtract_BvTotAccrAmtPayCcy` | TField |  | Specifies the total recalculated accrual amount in equivalent payment currency that is accrued till date. |
| 41 | `SC.TFE.DIFF.AMT` | `ScTrailFeesExtract_DiffAmt` | TField |  | Specifies the difference amount in payment currency that is prorated against the individual client level |
| 42 | `SC.TFE.DEPOSITORY` | `ScTrailFeesExtract_Depository` | TField |  | Specifies the Depository for whom the extract was built. |
| 43 | `SC.TFE.REIMBURSE.TR.FEE` | `ScTrailFeesExtract_ReimburseTrFee` | TField |  |  |
| 44 | `SC.TFE.TAX.CODE` | `ScTrailFeesExtract_TaxCode` |  |  |  |
| 45 | `SC.TFE.EST.TAX.CALC.CCY` | `ScTrailFeesExtract_EstTaxCalcCcy` |  |  |  |
| 46 | `SC.TFE.EST.TAX.PAY.CCY` | `ScTrailFeesExtract_EstTaxPayCcy` |  |  |  |
| 47 | `SC.TFE.DIFF.TAX` | `ScTrailFeesExtract_DiffTax` |  |  |  |
| 48 | `SC.TFE.FINAL.AMT.CALC.CCY` | `ScTrailFeesExtract_FinalAmtCalcCcy` | TField |  | This field will hold the accrued fees plus tax amount in calculation currency if the tax is INCLUSIVE This field will hold only the accrued fees in calculation currency if the tax is EXCLUSIVE |
| 49 | `SC.TFE.FINAL.AMT.PAY.CCY` | `ScTrailFeesExtract_FinalAmtPayCcy` | TField |  | This field will hold the accrued fees plus tax amount in payment currency if the tax is INCLUSIVE This field will hold only the accrued fees in payment currency if the tax is EXCLUSIVE |
| 50 | `SC.TFE.HOLDING.ID` | `ScTrailFeesExtract_HoldingId` | TField |  |  |
| 51 | `SC.TFE.PORTFOLIO.ID` | `ScTrailFeesExtract_PortfolioId` | TField |  | This field will hold the SEC.ACC.MASTER id which corresponds to the current extract record |
