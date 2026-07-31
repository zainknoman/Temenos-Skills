# FS.GA.FORWARD.RATES — Table Schema

> Source: `INSERTS/I_F.FS.GA.FORWARD.RATES` in `FS_Forex.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FORWARD.RATES.PARENT.REF.ID` | `FsGaForwardRates_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FORWARD.RATES.ORA.ROWID` | `FsGaForwardRates_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FORWARD.RATES.FUND.ID` | `FsGaForwardRates_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FORWARD.RATES.FUND.ACCOUNTING.DATE` | `FsGaForwardRates_FundAccountingDate` | TField |  | FAD of the fund Multifonds DB Column is DCTA_PTF. |
| 5 | `FS.GA.FORWARD.RATES.LOT.NUMBER` | `FsGaForwardRates_LotNumber` | TField |  | Contract number of deal Multifonds DB Column is NCONTRAT. |
| 6 | `FS.GA.FORWARD.RATES.IFRS.CATEGORY` | `FsGaForwardRates_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 7 | `FS.GA.FORWARD.RATES.MANAGER.CODE` | `FsGaForwardRates_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 8 | `FS.GA.FORWARD.RATES.SETTLE.DATE` | `FsGaForwardRates_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 9 | `FS.GA.FORWARD.RATES.PAY.DATE` | `FsGaForwardRates_PayDate` | TField |  | Pay Date Multifonds DB Column is DVAL. |
| 10 | `FS.GA.FORWARD.RATES.CURRENCY.BOUGHT` | `FsGaForwardRates_CurrencyBought` | TField |  | Purchased Currency Multifonds DB Column is CDEV_ACHAT. |
| 11 | `FS.GA.FORWARD.RATES.SOLD.CURRENCY` | `FsGaForwardRates_SoldCurrency` | TField |  | Sold Currency Multifonds DB Column is CDEV_VENTE. |
| 12 | `FS.GA.FORWARD.RATES.FORWARD.RATE.D.MINUS.1` | `FsGaForwardRates_ForwardRateDMinus1` | TField |  | Forward Rate D-1 Multifonds DB Column is NBT_COURSVAL_PRED. |
| 13 | `FS.GA.FORWARD.RATES.FORWARD.RATE.D` | `FsGaForwardRates_ForwardRateD` | TField |  | Forward Rate D Multifonds DB Column is NBT_COURS_VAL. |
| 14 | `FS.GA.FORWARD.RATES.UNREALISED` | `FsGaForwardRates_Unrealised` | TField |  | GPTF amount Multifonds DB Column is MNT_GPTF. |
| 15 | `FS.GA.FORWARD.RATES.PERCENTAGE.VAR` | `FsGaForwardRates_PercentageVar` | TField |  | Percentage Var Multifonds DB Column is PC_VAR. |
| 16 | `FS.GA.FORWARD.RATES.SPOT.RATE.BOUGHT.LEG.DATE` | `FsGaForwardRates_SpotRateBoughtLegDate` | TField |  | Spot Rate Bought leg Date Multifonds DB Column is DCTA_TCOURS_BOUGHT. |
| 17 | `FS.GA.FORWARD.RATES.SPOT.RATE.BOUGHT.LEG.RATE` | `FsGaForwardRates_SpotRateBoughtLegRate` | TField |  | Spot Rate Bought leg Rate Multifonds DB Column is TCOURS_BOUGHT. |
| 18 | `FS.GA.FORWARD.RATES.SPOT.RATE.SELL.LEG.DATE` | `FsGaForwardRates_SpotRateSellLegDate` | TField |  | Spot Rate Sell leg Date Multifonds DB Column is DCTA_TCOURS_SELL. |
| 19 | `FS.GA.FORWARD.RATES.SPOT.RATE.SELL.LEG.RATE` | `FsGaForwardRates_SpotRateSellLegRate` | TField |  | Spot Rate Sell leg Rate Multifonds DB Column is TCOURS_SELL. |
| 20 | `FS.GA.FORWARD.RATES.LOWER.TENOR.BOUGHT.LEG.DETAILS` | `FsGaForwardRates_LowerTenorBoughtLegDetails` | TField |  | Lower Tenor Bought Leg details Multifonds DB Column is CODE_MOIS_LOW_TENOR_BOUGHT. |
| 21 | `FS.GA.FORWARD.RATES.LOWER.TENOR.BOUGHT.LEG.DATE` | `FsGaForwardRates_LowerTenorBoughtLegDate` | TField |  | Lower Tenor Bought Leg details Date Multifonds DB Column is DCTA_TCHG_LOW_TENOR_BOUGHT. |
| 22 | `FS.GA.FORWARD.RATES.LOWER.TENOR.BOUGHT.LEG.RATE` | `FsGaForwardRates_LowerTenorBoughtLegRate` | TField |  | Lower Tenor Bought Leg details Rate Multifonds DB Column is COURS_LOW_TENOR_BOUGHT. |
| 23 | `FS.GA.FORWARD.RATES.UPPER.TENOR.BOUGHT.LEG.DETAILS` | `FsGaForwardRates_UpperTenorBoughtLegDetails` | TField |  | Upper Tenor Bought Leg details Multifonds DB Column is CODE_MOIS_UTENOR_BOUGHT. |
| 24 | `FS.GA.FORWARD.RATES.UPPER.TENOR.BOUGHT.LEG.DATE` | `FsGaForwardRates_UpperTenorBoughtLegDate` | TField |  | Upper Tenor Bought Leg details Date Multifonds DB Column is DCTA_TCHG_UTENOR_BOUGHT. |
| 25 | `FS.GA.FORWARD.RATES.UPPER.TENOR.BOUGHT.LEG.RATE` | `FsGaForwardRates_UpperTenorBoughtLegRate` | TField |  | Upper Tenor Bought Leg details Rate Multifonds DB Column is COURS_UTENOR_BOUGHT. |
| 26 | `FS.GA.FORWARD.RATES.LOWER.TENOR.SELL.LEG.DETAILS` | `FsGaForwardRates_LowerTenorSellLegDetails` | TField |  | Lower Tenor Sell Leg details Multifonds DB Column is CODE_MOIS_LOW_TENOR_SELL. |
| 27 | `FS.GA.FORWARD.RATES.LOWER.TENOR.SELL.LEG.DATE` | `FsGaForwardRates_LowerTenorSellLegDate` | TField |  | Lower Tenor Sell Leg details Date Multifonds DB Column is DCTA_TCHG_LOW_TENOR_SELL. |
| 28 | `FS.GA.FORWARD.RATES.LOWER.TENOR.SELL.LEG.RATE` | `FsGaForwardRates_LowerTenorSellLegRate` | TField |  | Lower Tenor Sell Leg details Rate Multifonds DB Column is COURS_LOW_TENOR_SELL. |
| 29 | `FS.GA.FORWARD.RATES.UPPER.TENOR.SELL.LEG.DETAILS` | `FsGaForwardRates_UpperTenorSellLegDetails` | TField |  | Upper Tenor Sell Leg details Multifonds DB Column is CODE_MOIS_UTENOR_SELL. |
| 30 | `FS.GA.FORWARD.RATES.UPPER.TENOR.SELL.LEG.DATE` | `FsGaForwardRates_UpperTenorSellLegDate` | TField |  | Upper Tenor Sell Leg details Date Multifonds DB Column is DCTA_TCHG_UTENOR_SELL. |
| 31 | `FS.GA.FORWARD.RATES.UPPER.TENOR.SELL.LEG.RATE` | `FsGaForwardRates_UpperTenorSellLegRate` | TField |  | Upper Tenor Sell Leg details Rate Multifonds DB Column is COURS_UTENOR_SELL. |
| 32 | `FS.GA.FORWARD.RATES.OPERATION.CODE` | `FsGaForwardRates_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 33 | `FS.GA.FORWARD.RATES.SERVICE.CODE` | `FsGaForwardRates_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 34 | `FS.GA.FORWARD.RATES.RESERVED10` | `FsGaForwardRates_Reserved10` | TField |  |  |
| 35 | `FS.GA.FORWARD.RATES.RESERVED9` | `FsGaForwardRates_Reserved9` | TField |  |  |
| 36 | `FS.GA.FORWARD.RATES.RESERVED8` | `FsGaForwardRates_Reserved8` | TField |  |  |
| 37 | `FS.GA.FORWARD.RATES.RESERVED7` | `FsGaForwardRates_Reserved7` | TField |  |  |
| 38 | `FS.GA.FORWARD.RATES.RESERVED6` | `FsGaForwardRates_Reserved6` | TField |  |  |
| 39 | `FS.GA.FORWARD.RATES.RESERVED5` | `FsGaForwardRates_Reserved5` | TField |  |  |
| 40 | `FS.GA.FORWARD.RATES.RESERVED4` | `FsGaForwardRates_Reserved4` | TField |  |  |
| 41 | `FS.GA.FORWARD.RATES.RESERVED3` | `FsGaForwardRates_Reserved3` | TField |  |  |
| 42 | `FS.GA.FORWARD.RATES.RESERVED2` | `FsGaForwardRates_Reserved2` | TField |  |  |
| 43 | `FS.GA.FORWARD.RATES.RESERVED1` | `FsGaForwardRates_Reserved1` | TField |  |  |
| 44 | `FS.GA.FORWARD.RATES.LOCAL.REF` | `FsGaForwardRates_LocalRef` |  |  |  |
| 45 | `FS.GA.FORWARD.RATES.OVERRIDE` | `FsGaForwardRates_Override` |  |  |  |
| 46 | `FS.GA.FORWARD.RATES.RECORD.STATUS` | `FsGaForwardRates_RecordStatus` | String |  |  |
| 47 | `FS.GA.FORWARD.RATES.CURR.NO` | `FsGaForwardRates_CurrNo` | String |  |  |
| 48 | `FS.GA.FORWARD.RATES.INPUTTER` | `FsGaForwardRates_Inputter` |  |  |  |
| 49 | `FS.GA.FORWARD.RATES.DATE.TIME` | `FsGaForwardRates_DateTime` |  |  |  |
| 50 | `FS.GA.FORWARD.RATES.AUTHORISER` | `FsGaForwardRates_Authoriser` | String |  |  |
| 51 | `FS.GA.FORWARD.RATES.CO.CODE` | `FsGaForwardRates_CoCode` | String |  |  |
| 52 | `FS.GA.FORWARD.RATES.DEPT.CODE` | `FsGaForwardRates_DeptCode` | String |  |  |
| 53 | `FS.GA.FORWARD.RATES.AUDITOR.CODE` | `FsGaForwardRates_AuditorCode` | String |  |  |
| 54 | `FS.GA.FORWARD.RATES.AUDIT.DATE.TIME` | `FsGaForwardRates_AuditDateTime` | String |  |  |
