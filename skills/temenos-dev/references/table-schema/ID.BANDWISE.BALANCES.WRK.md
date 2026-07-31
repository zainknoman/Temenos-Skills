# ID.BANDWISE.BALANCES.WRK — Table Schema

> Source: `INSERTS/I_F.ID.BANDWISE.BALANCES.WRK` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IBB.ACTION.ID` | `IdBandwiseBalancesWrk_ActionId` | TField |  |  |
| 2 | `ID.IBB.POOL.REF` | `IdBandwiseBalancesWrk_PoolRef` | TField |  |  |
| 3 | `ID.IBB.CATEGORY` | `IdBandwiseBalancesWrk_Category` | TField |  |  |
| 4 | `ID.IBB.CURRENCY` | `IdBandwiseBalancesWrk_Currency` | TField |  |  |
| 5 | `ID.IBB.DIST.FREQUENCY` | `IdBandwiseBalancesWrk_DistFrequency` | TField |  |  |
| 6 | `ID.IBB.AMOUNT.FROM` | `IdBandwiseBalancesWrk_AmountFrom` | TField |  |  |
| 7 | `ID.IBB.AMOUNT.TO` | `IdBandwiseBalancesWrk_AmountTo` | TField |  |  |
| 8 | `ID.IBB.TOTAL.AVG.BAL` | `IdBandwiseBalancesWrk_TotalAvgBal` | TField |  |  |
| 9 | `ID.IBB.TOTAL.WEIGHTED.AVG.BAL` | `IdBandwiseBalancesWrk_TotalWeightedAvgBal` | TField |  |  |
| 10 | `ID.IBB.TOTAL.AFTER.PER.BAL` | `IdBandwiseBalancesWrk_TotalAfterPerBal` | TField |  |  |
| 11 | `ID.IBB.TOTAL.AFTER.MUD.BAL` | `IdBandwiseBalancesWrk_TotalAfterMudBal` | TField |  |  |
| 12 | `ID.IBB.TOTAL.AFTER.IRR.BAL` | `IdBandwiseBalancesWrk_TotalAfterIrrBal` | TField |  |  |
| 13 | `ID.IBB.RTN.ALTERED.PROFIT` | `IdBandwiseBalancesWrk_RtnAlteredProfit` | TField |  |  |
| 14 | `ID.IBB.DEPOSIT.TYPE` | `IdBandwiseBalancesWrk_DepositType` | TField |  |  |
| 15 | `ID.IBB.CALCULATED.PROFIT` | `IdBandwiseBalancesWrk_CalculatedProfit` | TField |  |  |
| 16 | `ID.IBB.RESERVED13` | `IdBandwiseBalancesWrk_Reserved13` | TField |  |  |
| 17 | `ID.IBB.RESERVED12` | `IdBandwiseBalancesWrk_Reserved12` | TField |  |  |
| 18 | `ID.IBB.RESERVED11` | `IdBandwiseBalancesWrk_Reserved11` | TField |  |  |
| 19 | `ID.IBB.NET.PROFIT.PAYABLE` | `IdBandwiseBalancesWrk_NetProfitPayable` | TField |  |  |
| 20 | `ID.IBB.MUD.EXPECTED.PROFIT` | `IdBandwiseBalancesWrk_MudExpectedProfit` | TField |  |  |
| 21 | `ID.IBB.MUD.PDS.PROFIT` | `IdBandwiseBalancesWrk_MudPdsProfit` | TField |  |  |
| 22 | `ID.IBB.RESERVED.8` | `IdBandwiseBalancesWrk_Reserved8` | TField |  |  |
| 23 | `ID.IBB.RESERVED.7` | `IdBandwiseBalancesWrk_Reserved7` | TField |  |  |
| 24 | `ID.IBB.RESERVED.6` | `IdBandwiseBalancesWrk_Reserved6` | TField |  |  |
| 25 | `ID.IBB.RESERVED.5` | `IdBandwiseBalancesWrk_Reserved5` | TField |  |  |
| 26 | `ID.IBB.RESERVED.4` | `IdBandwiseBalancesWrk_Reserved4` |  |  |  |
| 27 | `ID.IBB.RESERVED.3` | `IdBandwiseBalancesWrk_Reserved3` |  |  |  |
| 28 | `ID.IBB.RESERVED.2` | `IdBandwiseBalancesWrk_Reserved2` |  |  |  |
| 29 | `ID.IBB.RESERVED.1` | `IdBandwiseBalancesWrk_Reserved1` |  |  |  |
