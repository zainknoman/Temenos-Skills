# CO.ASSET.DETAILS — Table Schema

> Source: `INSERTS/I_F.CO.ASSET.DETAILS` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COASD.COLLATERAL.ID` | `CoAssetDetails_CollateralId` |  |  |  |
| 2 | `COASD.COLLATERAL.CCY` | `CoAssetDetails_CollateralCcy` |  |  |  |
| 3 | `COASD.COLL.TYPE` | `CoAssetDetails_CollType` |  |  |  |
| 4 | `COASD.COLL.COUNTRY` | `CoAssetDetails_CollCountry` |  |  |  |
| 5 | `COASD.HIGH.ADV.RATIO` | `CoAssetDetails_HighAdvRatio` |  |  |  |
| 6 | `COASD.LOW.ADV.RATIO` | `CoAssetDetails_LowAdvRatio` |  |  |  |
| 7 | `COASD.MARGIN.VALUE` | `CoAssetDetails_MarginValue` |  |  |  |
| 8 | `COASD.CONTRACT.ID` | `CoAssetDetails_ContractId` |  |  |  |
| 9 | `COASD.ASSET.TYPE` | `CoAssetDetails_AssetType` |  |  |  |
| 10 | `COASD.SUB.ASSET.TYPE` | `CoAssetDetails_SubAssetType` |  |  |  |
| 11 | `COASD.SC.INDUSTRY` | `CoAssetDetails_ScIndustry` |  |  |  |
| 12 | `COASD.CONCENTRATION.CAP` | `CoAssetDetails_ConcentrationCap` |  |  |  |
| 13 | `COASD.NO.CONC.CAP` | `CoAssetDetails_NoConcCap` |  |  |  |
| 14 | `COASD.HAR.LEVEL` | `CoAssetDetails_HarLevel` |  |  |  |
| 15 | `COASD.LAR.LEVEL` | `CoAssetDetails_LarLevel` |  |  |  |
| 16 | `COASD.ACTUAL.VALUE` | `CoAssetDetails_ActualValue` |  |  |  |
| 17 | `COASD.COLL.VALUE` | `CoAssetDetails_CollValue` |  |  |  |
| 18 | `COASD.EXCH.RATE` | `CoAssetDetails_ExchRate` |  |  |  |
| 19 | `COASD.TOTAL.CUST.COLL` | `CoAssetDetails_TotalCustColl` | TField |  | Total value of the collaterals of a customer in local currency. Validation Rules: 1. Standard T24 amount field. 2. No input field. |
| 20 | `COASD.TOT.COLL.AFT.GRP.CAP` | `CoAssetDetails_TotCollAftGrpCap` | TField |  | Total Collateral Value of the customer in local currency after applying group concentration cap. Validation Rules: 1. Standard T24 amount field. 2. No input field. |
| 21 | `COASD.LTMV` | `CoAssetDetails_Ltmv` | TField |  | Loan To Market Value Ratio is the ratio of loans against the market value of the assets held by the customer. The formula for the calculation of Loan to Market Value Ratio (LTMV) is : LTMV = (Total Outstanding Liabilities / Total Market Value of the portfolio) Where, Total Outstanding Liabilities is the total amount of loans and other liabilities held by the customer Total Market Value of the portfolio is the value of the portfolio before the application of Advance Ratio and Concentration Caps (Total Nominal value of collaterals) This calculation will take place whenever the services "CO.CALC.CUST.COLL.SERVICE" and "CO.RECALC.CUST.COLLATERAL" are triggered. |
| 22 | `COASD.LTCV` | `CoAssetDetails_Ltcv` | TField |  | Loan To Collateral Value Ratio is the ratio of loans against the collateral value of the assets held by the customer. The formula for the calculation of Loan to Collateral Value Ratio (LTCV) is : LTCV = (Total Outstanding Liabilities / Total Collateral Value of the portfolio) Where, Total Outstanding Liabilities is the total amount of loans and other liabilities held by the customer Total Collateral Value of the portfolio is the value of the portfolio after the application of Advance Ratio and Concentration Caps have been applied This calculation will take place whenever the services "CO.CALC.CUST.COLL.SERVICE" and "CO.RECALC.CUST.COLLATERAL" are triggered. |
| 23 | `COASD.RESERVED.5` | `CoAssetDetails_Reserved5` | TField |  |  |
| 24 | `COASD.RESERVED.4` | `CoAssetDetails_Reserved4` | TField |  |  |
| 25 | `COASD.RESERVED.3` | `CoAssetDetails_Reserved3` | TField |  |  |
| 26 | `COASD.RESERVED.2` | `CoAssetDetails_Reserved2` | TField |  |  |
| 27 | `COASD.UPDATED.DATE.TIME` | `CoAssetDetails_UpdatedDateTime` |  |  |  |
| 28 | `COASD.ASSET.CCY` | `CoAssetDetails_AssetCcy` |  |  |  |
| 29 | `COASD.LIAB.CCY` | `CoAssetDetails_LiabCcy` |  |  |  |
| 30 | `COASD.CCY.PAIR.PERC` | `CoAssetDetails_CcyPairPerc` |  |  |  |
| 31 | `COASD.HAR.LEVEL.ID` | `CoAssetDetails_HarLevelId` |  |  |  |
| 32 | `COASD.LAR.LEVEL.ID` | `CoAssetDetails_LarLevelId` |  |  |  |
| 33 | `COASD.MV.AFTER.HAR` | `CoAssetDetails_MvAfterHar` |  |  |  |
| 34 | `COASD.MV.AFT.SINGLE.CAP` | `CoAssetDetails_MvAftSingleCap` |  |  |  |
| 35 | `COASD.SAME.CCY.ALLOCATED` | `CoAssetDetails_SameCcyAllocated` |  |  |  |
| 36 | `COASD.MV.AFT.SAME.CCY.ALLOC` | `CoAssetDetails_MvAftSameCcyAlloc` |  |  |  |
| 37 | `COASD.MV.AFTER.LAR` | `CoAssetDetails_MvAfterLar` |  |  |  |
| 38 | `COASD.CROSS.CCY.ALLOCATED` | `CoAssetDetails_CrossCcyAllocated` |  |  |  |
| 39 | `COASD.MV.UNALLOC` | `CoAssetDetails_MvUnalloc` |  |  |  |
| 40 | `COASD.TOTAL.COLL.CONC.POOL` | `CoAssetDetails_TotalCollConcPool` | TField |  |  |
