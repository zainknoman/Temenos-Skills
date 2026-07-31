# INGAAP.SC.TRADING.POSITION — Table Schema

> Source: `INSERTS/I_F.INGAAP.SC.TRADING.POSITION` in `INGAAP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INGAAP.PORTFOLIO.NO` | `IngaapScTradingPosition_PortfolioNo` | TField |  |  |
| 2 | `INGAAP.PORTFOLIO.TYPE` | `IngaapScTradingPosition_PortfolioType` | TField |  |  |
| 3 | `INGAAP.SECURITY.CODE` | `IngaapScTradingPosition_SecurityCode` | TField |  |  |
| 4 | `INGAAP.SEC.CCY` | `IngaapScTradingPosition_SecCcy` | TField |  |  |
| 5 | `INGAAP.SUB.ASSET.TYPE` | `IngaapScTradingPosition_SubAssetType` | TField |  |  |
| 6 | `INGAAP.USGAAP.SUB.ASSET` | `IngaapScTradingPosition_UsgaapSubAsset` | TField |  |  |
| 7 | `INGAAP.TIME.BAND` | `IngaapScTradingPosition_TimeBand` | TField |  |  |
| 8 | `INGAAP.LEVEL` | `IngaapScTradingPosition_Level` | TField |  |  |
| 9 | `INGAAP.MATURITY.DATE` | `IngaapScTradingPosition_MaturityDate` | TField |  |  |
| 10 | `INGAAP.ISSUE.DATE` | `IngaapScTradingPosition_IssueDate` | TField |  |  |
| 11 | `INGAAP.RESERVED.24` | `IngaapScTradingPosition_Reserved24` | TField |  |  |
| 12 | `INGAAP.RESERVED.23` | `IngaapScTradingPosition_Reserved23` | TField |  |  |
| 13 | `INGAAP.RESERVED.22` | `IngaapScTradingPosition_Reserved22` | TField |  |  |
| 14 | `INGAAP.RESERVED.21` | `IngaapScTradingPosition_Reserved21` | TField |  |  |
| 15 | `INGAAP.RESERVED.20` | `IngaapScTradingPosition_Reserved20` | TField |  |  |
| 16 | `INGAAP.RESERVED.19` | `IngaapScTradingPosition_Reserved19` | TField |  |  |
| 17 | `INGAAP.STP.DATE` | `IngaapScTradingPosition_StpDate` |  |  |  |
| 18 | `INGAAP.CURRENT.POSITION` | `IngaapScTradingPosition_CurrentPosition` |  |  |  |
| 19 | `INGAAP.CUR.COST.OF.POSN` | `IngaapScTradingPosition_CurCostOfPosn` |  |  |  |
| 20 | `INGAAP.V.D.NOMINAL` | `IngaapScTradingPosition_VDNominal` |  |  |  |
| 21 | `INGAAP.V.D.COST` | `IngaapScTradingPosition_VDCost` |  |  |  |
| 22 | `INGAAP.AMORTIZED.COST` | `IngaapScTradingPosition_AmortizedCost` |  |  |  |
| 23 | `INGAAP.UNREAL.PROFIT.LOSS` | `IngaapScTradingPosition_UnrealProfitLoss` |  |  |  |
| 24 | `INGAAP.REALISED.PL` | `IngaapScTradingPosition_RealisedPl` |  |  |  |
| 25 | `INGAAP.REVALUATION.COST` | `IngaapScTradingPosition_RevaluationCost` |  |  |  |
| 26 | `INGAAP.LOSS.DATE` | `IngaapScTradingPosition_LossDate` |  |  |  |
| 27 | `INGAAP.REPO.NOMINAL` | `IngaapScTradingPosition_RepoNominal` |  |  |  |
| 28 | `INGAAP.RESO.NOMINAL` | `IngaapScTradingPosition_ResoNominal` |  |  |  |
| 29 | `INGAAP.LAST.PRIICE` | `IngaapScTradingPosition_LastPriice` |  |  |  |
| 30 | `INGAAP.ESTIMATION` | `IngaapScTradingPosition_Estimation` |  |  |  |
| 31 | `INGAAP.UNREAL.PL.TAX` | `IngaapScTradingPosition_UnrealPlTax` |  |  |  |
| 32 | `INGAAP.NOMINAL.SOLD` | `IngaapScTradingPosition_NominalSold` |  |  |  |
| 33 | `INGAAP.AMOUNT.SOLD` | `IngaapScTradingPosition_AmountSold` |  |  |  |
| 34 | `INGAAP.INT.AMT` | `IngaapScTradingPosition_IntAmt` | TField |  |  |
| 35 | `INGAAP.MAX.MTD.BAL` | `IngaapScTradingPosition_MaxMtdBal` | TField |  |  |
| 36 | `INGAAP.PLEDGE.PURPOSE` | `IngaapScTradingPosition_PledgePurpose` | TField |  |  |
| 37 | `INGAAP.CUR.POSN` | `IngaapScTradingPosition_CurPosn` | TField |  |  |
| 38 | `INGAAP.CUR.AMORT.COST` | `IngaapScTradingPosition_CurAmortCost` | TField |  |  |
| 39 | `INGAAP.CUR.ESTIMATION` | `IngaapScTradingPosition_CurEstimation` | TField |  |  |
| 40 | `INGAAP.RESERVED.15` | `IngaapScTradingPosition_Reserved15` | TField |  |  |
| 41 | `INGAAP.RESERVED.14` | `IngaapScTradingPosition_Reserved14` | TField |  |  |
| 42 | `INGAAP.RESERVED.13` | `IngaapScTradingPosition_Reserved13` | TField |  |  |
| 43 | `INGAAP.RESERVED.12` | `IngaapScTradingPosition_Reserved12` | TField |  |  |
| 44 | `INGAAP.RESERVED.11` | `IngaapScTradingPosition_Reserved11` | TField |  |  |
| 45 | `INGAAP.RESERVED.10` | `IngaapScTradingPosition_Reserved10` | TField |  |  |
| 46 | `INGAAP.RESERVED.9` | `IngaapScTradingPosition_Reserved9` | TField |  |  |
| 47 | `INGAAP.RESERVED.8` | `IngaapScTradingPosition_Reserved8` | TField |  |  |
| 48 | `INGAAP.RESERVED.7` | `IngaapScTradingPosition_Reserved7` | TField |  |  |
| 49 | `INGAAP.RESERVED.6` | `IngaapScTradingPosition_Reserved6` | TField |  |  |
| 50 | `INGAAP.RESERVED.5` | `IngaapScTradingPosition_Reserved5` | TField |  |  |
| 51 | `INGAAP.RESERVED.4` | `IngaapScTradingPosition_Reserved4` | TField |  |  |
| 52 | `INGAAP.RESERVED.3` | `IngaapScTradingPosition_Reserved3` | TField |  |  |
| 53 | `INGAAP.RESERVED.2` | `IngaapScTradingPosition_Reserved2` | TField |  |  |
| 54 | `INGAAP.RESERVED.1` | `IngaapScTradingPosition_Reserved1` | TField |  |  |
