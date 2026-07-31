# SC.SAFEKEEP.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.SC.SAFEKEEP.ACTIVITY` in `SC_ScfSafekeepingFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SSA.DAY.NO` | `ScSafekeepActivity_DayNo` |  |  |  |
| 2 | `SSA.CLOSING.NOM` | `ScSafekeepActivity_ClosingNom` |  |  |  |
| 3 | `SSA.CLOSING.NOM.LCY` | `ScSafekeepActivity_ClosingNomLcy` |  |  |  |
| 4 | `SSA.ASSET.BAL.LCY` | `ScSafekeepActivity_AssetBalLcy` |  |  |  |
| 5 | `SSA.AVG.CL.NOM.LCY` | `ScSafekeepActivity_AvgClNomLcy` |  |  |  |
| 6 | `SSA.AVG.CLOSING.NOM` | `ScSafekeepActivity_AvgClosingNom` |  |  |  |
| 7 | `SSA.AVG.AST.BAL.LCY` | `ScSafekeepActivity_AvgAstBalLcy` |  |  |  |
| 8 | `SSA.ASSET.BAL.SCY` | `ScSafekeepActivity_AssetBalScy` |  |  |  |
| 9 | `SSA.AVG.AST.BAL.SCY` | `ScSafekeepActivity_AvgAstBalScy` |  |  |  |
| 10 | `SSA.MV.RES.7` | `ScSafekeepActivity_MvRes7` |  |  |  |
| 11 | `SSA.MV.RES.6` | `ScSafekeepActivity_MvRes6` |  |  |  |
| 12 | `SSA.MV.RES.5` | `ScSafekeepActivity_MvRes5` |  |  |  |
| 13 | `SSA.MV.RES.4` | `ScSafekeepActivity_MvRes4` |  |  |  |
| 14 | `SSA.MV.RES.3` | `ScSafekeepActivity_MvRes3` |  |  |  |
| 15 | `SSA.MV.RES.2` | `ScSafekeepActivity_MvRes2` |  |  |  |
| 16 | `SSA.MV.RES.1` | `ScSafekeepActivity_MvRes1` |  |  |  |
| 17 | `SSA.SECURITY.CCY` | `ScSafekeepActivity_SecurityCcy` | TField |  | Security currency, for securities data this will be security currency, for other assets this will be obtainedfrom the associated SC.POS.ASSET record. |
| 18 | `SSA.PRODUCT` | `ScSafekeepActivity_Product` | TField |  | Product to which the asset belongs, for Securities data this will be SC, for other assets this will be obtainedfrom the associated SC.POS.ASSET record. |
| 19 | `SSA.SECURITY.CODE` | `ScSafekeepActivity_SecurityCode` | TField |  | Security code or asset id |
| 20 | `SSA.FEE.EST.DAY` | `ScSafekeepActivity_FeeEstDay` |  |  |  |
| 21 | `SSA.DAILY.FEE.EST.LCY` | `ScSafekeepActivity_DailyFeeEstLcy` |  |  |  |
| 22 | `SSA.CUM.FEE.EST.LCY` | `ScSafekeepActivity_CumFeeEstLcy` |  |  |  |
| 23 | `SSA.DAILY.MIN.AMT.LCY` | `ScSafekeepActivity_DailyMinAmtLcy` |  |  |  |
| 24 | `SSA.CUM.MIN.AMT.LCY` | `ScSafekeepActivity_CumMinAmtLcy` |  |  |  |
| 25 | `SSA.DAILY.MAX.AMT.LCY` | `ScSafekeepActivity_DailyMaxAmtLcy` |  |  |  |
| 26 | `SSA.CUM.MAX.AMT.LCY` | `ScSafekeepActivity_CumMaxAmtLcy` |  |  |  |
| 27 | `SSA.TOT.DAYS.FEE.EST.LCY` | `ScSafekeepActivity_TotDaysFeeEstLcy` |  |  |  |
| 28 | `SSA.DAYS.FEE.AMT.LCY` | `ScSafekeepActivity_DaysFeeAmtLcy` |  |  |  |
| 29 | `SSA.TOT.EST.FEE.LCY` | `ScSafekeepActivity_TotEstFeeLcy` | TField |  | This field will hold the total Fee amount which will be charged from the customer till date. The total fee is calculated in local currency. Validation Rules: NoInput Field |
| 30 | `SSA.TOT.CHRGD.AMT.LCY` | `ScSafekeepActivity_TotChrgdAmtLcy` | TField |  |  |
| 31 | `SSA.PL.RECOG.SAFE.LCY` | `ScSafekeepActivity_PlRecogSafeLcy` | TField |  | This field will hold the total fees that are credited directly to the PL account due to sale or transfer of thesecurity or due to a corporate action events that has caused reduction in customer position as on date. Part of EXT.DATE multi-value set |
| 32 | `SSA.PORTFOLIO` | `ScSafekeepActivity_Portfolio` | TField |  | Portfolio Id |
| 33 | `SSA.DEPOSITORY` | `ScSafekeepActivity_Depository` | TField |  |  |
| 34 | `SSA.CONTRACT.CODE` | `ScSafekeepActivity_ContractCode` | TField |  |  |
| 35 | `SSA.MATURITY.DATE` | `ScSafekeepActivity_MaturityDate` | TField |  |  |
| 36 | `SSA.STRIKE.PRICE` | `ScSafekeepActivity_StrikePrice` | TField |  |  |
| 37 | `SSA.CALL.PUT` | `ScSafekeepActivity_CallPut` | TField |  |  |
| 38 | `SSA.DELIVERY.CCY` | `ScSafekeepActivity_DeliveryCcy` | TField |  |  |
| 39 | `SSA.UNDLYING.MAT.DATE` | `ScSafekeepActivity_UndlyingMatDate` | TField |  |  |
| 40 | `SSA.FEES.CHRGD.DATE` | `ScSafekeepActivity_FeesChrgdDate` |  |  |  |
| 41 | `SSA.FEES.CHRGD.AMT.LCY` | `ScSafekeepActivity_FeesChrgdAmtLcy` |  |  |  |
| 42 | `SSA.DX.TRADE.ID` | `ScSafekeepActivity_DxTradeId` | TField |  |  |
| 43 | `SSA.RECORD.STATUS` | `ScSafekeepActivity_RecordStatus` | String |  |  |
| 44 | `SSA.CURR.NO` | `ScSafekeepActivity_CurrNo` | String |  |  |
| 45 | `SSA.INPUTTER` | `ScSafekeepActivity_Inputter` |  |  |  |
| 46 | `SSA.DATE.TIME` | `ScSafekeepActivity_DateTime` |  |  |  |
| 47 | `SSA.AUTHORISER` | `ScSafekeepActivity_Authoriser` | String |  |  |
| 48 | `SSA.CO.CODE` | `ScSafekeepActivity_CoCode` | String |  |  |
| 49 | `SSA.DEPT.CODE` | `ScSafekeepActivity_DeptCode` | String |  |  |
| 50 | `SSA.AUDITOR.CODE` | `ScSafekeepActivity_AuditorCode` | String |  |  |
| 51 | `SSA.AUDIT.DATE.TIME` | `ScSafekeepActivity_AuditDateTime` | String |  |  |
