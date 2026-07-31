# ID.BANDWISE.BALANCES — Table Schema

> Source: `INSERTS/I_F.ID.BANDWISE.BALANCES` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IBL.ACTION.ID` | `IdBandwiseBalances_ActionId` | TField |  |  |
| 2 | `ID.IBL.POOL.REF` | `IdBandwiseBalances_PoolRef` | TField |  |  |
| 3 | `ID.IBL.CATEGORY` | `IdBandwiseBalances_Category` | TField |  |  |
| 4 | `ID.IBL.CURRENCY` | `IdBandwiseBalances_Currency` | TField |  |  |
| 5 | `ID.IBL.DIST.FREQUENCY` | `IdBandwiseBalances_DistFrequency` | TField |  |  |
| 6 | `ID.IBL.AMOUNT.FROM` | `IdBandwiseBalances_AmountFrom` | TField |  |  |
| 7 | `ID.IBL.AMOUNT.TO` | `IdBandwiseBalances_AmountTo` | TField |  |  |
| 8 | `ID.IBL.TOTAL.AVG.BAL` | `IdBandwiseBalances_TotalAvgBal` | TField |  |  |
| 9 | `ID.IBL.TOTAL.AVG.PRFT.RATE` | `IdBandwiseBalances_TotalAvgPrftRate` | TField |  |  |
| 10 | `ID.IBL.TOTAL.WEIGHTED.AVG.BAL` | `IdBandwiseBalances_TotalWeightedAvgBal` | TField |  |  |
| 11 | `ID.IBL.WEIGHTED.AVG.PRFT.RATE` | `IdBandwiseBalances_WeightedAvgPrftRate` | TField |  |  |
| 12 | `ID.IBL.TOTAL.AFTER.PER.BAL` | `IdBandwiseBalances_TotalAfterPerBal` | TField |  |  |
| 13 | `ID.IBL.PRFT.RATE.AFTER.PER` | `IdBandwiseBalances_PrftRateAfterPer` | TField |  |  |
| 14 | `ID.IBL.TOTAL.AFTER.MUD.BAL` | `IdBandwiseBalances_TotalAfterMudBal` | TField |  |  |
| 15 | `ID.IBL.PRFT.RATE.AFTER.MUD` | `IdBandwiseBalances_PrftRateAfterMud` | TField |  |  |
| 16 | `ID.IBL.TOTAL.AFTER.IRR.BAL` | `IdBandwiseBalances_TotalAfterIrrBal` | TField |  |  |
| 17 | `ID.IBL.PRFT.RATE.AFTER.IRR` | `IdBandwiseBalances_PrftRateAfterIrr` | TField |  |  |
| 18 | `ID.IBL.RTN.ALTERED.PROFIT` | `IdBandwiseBalances_RtnAlteredProfit` | TField |  |  |
| 19 | `ID.IBL.DEPOSIT.TYPE` | `IdBandwiseBalances_DepositType` | TField |  |  |
| 20 | `ID.IBL.CALCULATED.PROFIT` | `IdBandwiseBalances_CalculatedProfit` | TField |  |  |
| 21 | `ID.IBL.TOT.AVG.BAL.UNROUND` | `IdBandwiseBalances_TotAvgBalUnround` | TField |  |  |
| 22 | `ID.IBL.TOT.WEIGH.BAL.UNROUND` | `IdBandwiseBalances_TotWeighBalUnround` | TField |  |  |
| 23 | `ID.IBL.RESERVED11` | `IdBandwiseBalances_Reserved11` | TField |  |  |
| 24 | `ID.IBL.NET.PROFIT.PAYABLE` | `IdBandwiseBalances_NetProfitPayable` | TField |  |  |
| 25 | `ID.IBL.NET.PROFIT.RATE` | `IdBandwiseBalances_NetProfitRate` | TField |  |  |
| 26 | `ID.IBL.WAKALA.PROFIT.RATE` | `IdBandwiseBalances_WakalaProfitRate` | TField |  |  |
| 27 | `ID.IBL.SPREAD.RATE` | `IdBandwiseBalances_SpreadRate` | TField |  |  |
| 28 | `ID.IBL.SPL.SPREAD.RATE` | `IdBandwiseBalances_SplSpreadRate` | TField |  |  |
| 29 | `ID.IBL.TARGET.RATE` | `IdBandwiseBalances_TargetRate` | TField |  |  |
| 30 | `ID.IBL.NET.TRGT.AMT.PAYABLE` | `IdBandwiseBalances_NetTrgtAmtPayable` | TField |  |  |
| 31 | `ID.IBL.HIBA.AMOUNT` | `IdBandwiseBalances_HibaAmount` | TField |  |  |
| 32 | `ID.IBL.STATUS` | `IdBandwiseBalances_Status` | TField |  |  |
| 33 | `ID.IBL.MUD.EXPECTED.PROFIT` | `IdBandwiseBalances_MudExpectedProfit` | TField |  |  |
| 34 | `ID.IBL.MUD.PDS.PROFIT` | `IdBandwiseBalances_MudPdsProfit` | TField |  |  |
| 35 | `ID.IBL.BROKEN.DEPOSIT.RATE` | `IdBandwiseBalances_BrokenDepositRate` | TField |  |  |
| 36 | `ID.IBL.RESERVED.5` | `IdBandwiseBalances_Reserved5` | TField |  |  |
| 37 | `ID.IBL.RESERVED.4` | `IdBandwiseBalances_Reserved4` |  |  |  |
| 38 | `ID.IBL.RESERVED.3` | `IdBandwiseBalances_Reserved3` |  |  |  |
| 39 | `ID.IBL.RESERVED.2` | `IdBandwiseBalances_Reserved2` |  |  |  |
| 40 | `ID.IBL.RESERVED.1` | `IdBandwiseBalances_Reserved1` |  |  |  |
| 41 | `ID.IBL.RECORD.STATUS` | `IdBandwiseBalances_RecordStatus` | String |  |  |
| 42 | `ID.IBL.CURR.NO` | `IdBandwiseBalances_CurrNo` | String |  |  |
| 43 | `ID.IBL.INPUTTER` | `IdBandwiseBalances_Inputter` |  |  |  |
| 44 | `ID.IBL.DATE.TIME` | `IdBandwiseBalances_DateTime` |  |  |  |
| 45 | `ID.IBL.AUTHORISER` | `IdBandwiseBalances_Authoriser` | String |  |  |
| 46 | `ID.IBL.CO.CODE` | `IdBandwiseBalances_CoCode` | String |  |  |
| 47 | `ID.IBL.DEPT.CODE` | `IdBandwiseBalances_DeptCode` | String |  |  |
| 48 | `ID.IBL.AUDITOR.CODE` | `IdBandwiseBalances_AuditorCode` | String |  |  |
| 49 | `ID.IBL.AUDIT.DATE.TIME` | `IdBandwiseBalances_AuditDateTime` | String |  |  |
