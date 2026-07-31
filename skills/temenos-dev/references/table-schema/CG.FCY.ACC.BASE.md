# CG.FCY.ACC.BASE — Table Schema

> Source: `INSERTS/I_F.CG.FCY.ACC.BASE` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.FAB.PORTFOLIO.NO` | `CgFcyAccBase_PortfolioNo` | TField |  |  |
| 2 | `CG.FAB.ACCOUNT.NO` | `CgFcyAccBase_AccountNo` | TField |  |  |
| 3 | `CG.FAB.CURRENCY` | `CgFcyAccBase_Currency` | TField |  |  |
| 4 | `CG.FAB.PARCEL.ID` | `CgFcyAccBase_ParcelId` |  |  |  |
| 5 | `CG.FAB.TXN.ID` | `CgFcyAccBase_TxnId` |  |  |  |
| 6 | `CG.FAB.BUY.SELL` | `CgFcyAccBase_BuySell` |  |  |  |
| 7 | `CG.FAB.TRADE.DATE.TIME` | `CgFcyAccBase_TradeDateTime` |  |  |  |
| 8 | `CG.FAB.SETTLEMENT.DATE` | `CgFcyAccBase_SettlementDate` |  |  |  |
| 9 | `CG.FAB.FCY.AMT.TXN` | `CgFcyAccBase_FcyAmtTxn` |  |  |  |
| 10 | `CG.FAB.CG.FCY.AMT.TXN` | `CgFcyAccBase_CgFcyAmtTxn` |  |  |  |
| 11 | `CG.FAB.EXCH.RATE.TXN` | `CgFcyAccBase_ExchRateTxn` |  |  |  |
| 12 | `CG.FAB.LCY.AMT.TXN` | `CgFcyAccBase_LcyAmtTxn` |  |  |  |
| 13 | `CG.FAB.EXCH.RATE.TRD.DATE` | `CgFcyAccBase_ExchRateTrdDate` |  |  |  |
| 14 | `CG.FAB.EXCH.RATE.SETT.DATE` | `CgFcyAccBase_ExchRateSettDate` |  |  |  |
| 15 | `CG.FAB.ACQ.COST.LCY` | `CgFcyAccBase_AcqCostLcy` |  |  |  |
| 16 | `CG.FAB.LCY.AMT.SETT` | `CgFcyAccBase_LcyAmtSett` |  |  |  |
| 17 | `CG.FAB.DISP.AMT.LCY` | `CgFcyAccBase_DispAmtLcy` |  |  |  |
| 18 | `CG.FAB.FX.GAIN` | `CgFcyAccBase_FxGain` |  |  |  |
| 19 | `CG.FAB.PUR.PARCEL.ID` | `CgFcyAccBase_PurParcelId` |  |  |  |
| 20 | `CG.FAB.PUR.FCY.ACQ.AMT` | `CgFcyAccBase_PurFcyAcqAmt` |  |  |  |
| 21 | `CG.FAB.PUR.LCY.ACQ.AMT` | `CgFcyAccBase_PurLcyAcqAmt` |  |  |  |
| 22 | `CG.FAB.PUR.PARCEL.FX.GAIN` | `CgFcyAccBase_PurParcelFxGain` |  |  |  |
| 23 | `CG.FAB.RESERVED.25` | `CgFcyAccBase_Reserved25` | TField |  |  |
| 24 | `CG.FAB.RESERVED.24` | `CgFcyAccBase_Reserved24` | TField |  |  |
| 25 | `CG.FAB.RESERVED.23` | `CgFcyAccBase_Reserved23` | TField |  |  |
| 26 | `CG.FAB.RESERVED.22` | `CgFcyAccBase_Reserved22` | TField |  |  |
| 27 | `CG.FAB.RESERVED.21` | `CgFcyAccBase_Reserved21` | TField |  |  |
| 28 | `CG.FAB.RESERVED.20` | `CgFcyAccBase_Reserved20` | TField |  |  |
| 29 | `CG.FAB.RESERVED.19` | `CgFcyAccBase_Reserved19` | TField |  |  |
| 30 | `CG.FAB.RESERVED.18` | `CgFcyAccBase_Reserved18` | TField |  |  |
| 31 | `CG.FAB.RESERVED.17` | `CgFcyAccBase_Reserved17` | TField |  |  |
| 32 | `CG.FAB.RESERVED.16` | `CgFcyAccBase_Reserved16` | TField |  |  |
| 33 | `CG.FAB.RESERVED.15` | `CgFcyAccBase_Reserved15` | TField |  |  |
| 34 | `CG.FAB.RESERVED.14` | `CgFcyAccBase_Reserved14` | TField |  |  |
| 35 | `CG.FAB.RESERVED.13` | `CgFcyAccBase_Reserved13` | TField |  |  |
| 36 | `CG.FAB.RESERVED.12` | `CgFcyAccBase_Reserved12` | TField |  |  |
| 37 | `CG.FAB.RESERVED.11` | `CgFcyAccBase_Reserved11` | TField |  |  |
| 38 | `CG.FAB.RESERVED.10` | `CgFcyAccBase_Reserved10` | TField |  |  |
| 39 | `CG.FAB.RESERVED.9` | `CgFcyAccBase_Reserved9` | TField |  |  |
| 40 | `CG.FAB.RESERVED.8` | `CgFcyAccBase_Reserved8` | TField |  |  |
| 41 | `CG.FAB.RESERVED.7` | `CgFcyAccBase_Reserved7` | TField |  |  |
| 42 | `CG.FAB.RESERVED.6` | `CgFcyAccBase_Reserved6` | TField |  |  |
| 43 | `CG.FAB.RESERVED.5` | `CgFcyAccBase_Reserved5` | TField |  |  |
| 44 | `CG.FAB.RESERVED.4` | `CgFcyAccBase_Reserved4` | TField |  |  |
| 45 | `CG.FAB.RESERVED.3` | `CgFcyAccBase_Reserved3` | TField |  |  |
| 46 | `CG.FAB.RESERVED.2` | `CgFcyAccBase_Reserved2` | TField |  |  |
| 47 | `CG.FAB.RESERVED.1` | `CgFcyAccBase_Reserved1` | TField |  |  |
| 48 | `CG.FAB.RECORD.STATUS` | `CgFcyAccBase_RecordStatus` | String |  |  |
| 49 | `CG.FAB.CURR.NO` | `CgFcyAccBase_CurrNo` | String |  |  |
| 50 | `CG.FAB.INPUTTER` | `CgFcyAccBase_Inputter` |  |  |  |
| 51 | `CG.FAB.DATE.TIME` | `CgFcyAccBase_DateTime` |  |  |  |
| 52 | `CG.FAB.AUTHORISER` | `CgFcyAccBase_Authoriser` | String |  |  |
| 53 | `CG.FAB.CO.CODE` | `CgFcyAccBase_CoCode` | String |  |  |
| 54 | `CG.FAB.DEPT.CODE` | `CgFcyAccBase_DeptCode` | String |  |  |
| 55 | `CG.FAB.AUDITOR.CODE` | `CgFcyAccBase_AuditorCode` | String |  |  |
| 56 | `CG.FAB.AUDIT.DATE.TIME` | `CgFcyAccBase_AuditDateTime` | String |  |  |
