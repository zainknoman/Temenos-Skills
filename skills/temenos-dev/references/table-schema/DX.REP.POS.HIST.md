# DX.REP.POS.HIST — Table Schema

> Source: `INSERTS/I_F.DX.REP.POS.HIST` in `DX_Position.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.RPH.CUSTOMER` | `DxRepPosHist_Customer` | TField |  | The customer holding the position |
| 2 | `DX.RPH.PORTFOLIO` | `DxRepPosHist_Portfolio` | TField |  | The T24 Portfolio holding the position |
| 3 | `DX.RPH.CONTRACT` | `DxRepPosHist_Contract` | TField |  | The contract that is being traded. This will be a valid DX.CONTRACT.MASTER id. |
| 4 | `DX.RPH.MATURITY.DATE` | `DxRepPosHist_MaturityDate` | TField |  | Maturity period of the position |
| 5 | `DX.RPH.STRIKE.PRICE` | `DxRepPosHist_StrikePrice` | TField |  | Internal strike price for OPTION type positions. This field is populated from the DX.TRANSACTION record field INT.STRIKE and holds the T24 internal strike price for the option. |
| 6 | `DX.RPH.CALL.PUT` | `DxRepPosHist_CallPut` | TField |  | Type of OPTION trade. CALL or PUT |
| 7 | `DX.RPH.EXT.STRIKE.PRI` | `DxRepPosHist_ExtStrikePri` | TField |  | Strike price for OPTION type position in external format. This field is populated from the DX.TRANSACTION record field STRIKE. |
| 8 | `DX.RPH.BUY.LOTS` | `DxRepPosHist_BuyLots` | TField |  | Total number of lots bought in this contract for this position |
| 9 | `DX.RPH.SELL.LOTS` | `DxRepPosHist_SellLots` | TField |  | Total number of Sold Lots for this position |
| 10 | `DX.RPH.NET.LOTS` | `DxRepPosHist_NetLots` | TField |  | Net lots for this position, long or short. |
| 11 | `DX.RPH.TRANSACTION.IDS` | `DxRepPosHist_TransactionIds` |  |  |  |
| 12 | `DX.RPH.TX.BUY.SELL` | `DxRepPosHist_TxBuySell` |  |  |  |
| 13 | `DX.RPH.TX.OPEN.CLOSE` | `DxRepPosHist_TxOpenClose` |  |  |  |
| 14 | `DX.RPH.TX.PRICE` | `DxRepPosHist_TxPrice` |  |  |  |
| 15 | `DX.RPH.TX.IPRICE` | `DxRepPosHist_TxIprice` |  |  |  |
| 16 | `DX.RPH.TX.LOTS` | `DxRepPosHist_TxLots` |  |  |  |
| 17 | `DX.RPH.TX.ORIG.LOTS` | `DxRepPosHist_TxOrigLots` |  |  |  |
| 18 | `DX.RPH.TX.BASE.LOTS` | `DxRepPosHist_TxBaseLots` |  |  |  |
| 19 | `DX.RPH.TX.BUY.LOTS` | `DxRepPosHist_TxBuyLots` |  |  |  |
| 20 | `DX.RPH.TX.SELL.LOTS` | `DxRepPosHist_TxSellLots` |  |  |  |
| 21 | `DX.RPH.TX.TRADE.DATE` | `DxRepPosHist_TxTradeDate` |  |  |  |
| 22 | `DX.RPH.TX.PREM.OFFSET` | `DxRepPosHist_TxPremOffset` |  |  |  |
| 23 | `DX.RPH.TX.PV.DATE` | `DxRepPosHist_TxPvDate` |  |  |  |
| 24 | `DX.RPH.TX.PVD.LOTS` | `DxRepPosHist_TxPvdLots` |  |  |  |
| 25 | `DX.RPH.TX.PVD.SIGN.LT` | `DxRepPosHist_TxPvdSignLt` |  |  |  |
| 26 | `DX.RPH.TX.PVD.BUY.LT` | `DxRepPosHist_TxPvdBuyLt` |  |  |  |
| 27 | `DX.RPH.TX.PVD.SELL.LT` | `DxRepPosHist_TxPvdSellLt` |  |  |  |
| 28 | `DX.RPH.TX.CO.ID` | `DxRepPosHist_TxCoId` |  |  |  |
| 29 | `DX.RPH.TX.CO.DATE` | `DxRepPosHist_TxCoDate` |  |  |  |
| 30 | `DX.RPH.TX.CO.PV.DT` | `DxRepPosHist_TxCoPvDt` |  |  |  |
| 31 | `DX.RPH.TX.CO.LOTS` | `DxRepPosHist_TxCoLots` |  |  |  |
| 32 | `DX.RPH.TX.CO.PV.LT` | `DxRepPosHist_TxCoPvLt` |  |  |  |
| 33 | `DX.RPH.TX.CO.TYPE` | `DxRepPosHist_TxCoType` |  |  |  |
| 34 | `DX.RPH.TX.CO.OFFSET` | `DxRepPosHist_TxCoOffset` |  |  |  |
| 35 | `DX.RPH.FAR.CO.DATE` | `DxRepPosHist_FarCoDate` |  |  |  |
| 36 | `DX.RPH.FAR.CO.PV.DATE` | `DxRepPosHist_FarCoPvDate` |  |  |  |
| 37 | `DX.RPH.CO.LOTS` | `DxRepPosHist_CoLots` |  |  |  |
| 38 | `DX.RPH.CO.PV.LOTS` | `DxRepPosHist_CoPvLots` |  |  |  |
| 39 | `DX.RPH.ENTITLEMENT` | `DxRepPosHist_Entitlement` |  |  |  |
| 40 | `DX.RPH.VAR.MAR.CCY` | `DxRepPosHist_VarMarCcy` |  |  |  |
| 41 | `DX.RPH.VAR.MARGIN` | `DxRepPosHist_VarMargin` |  |  |  |
| 42 | `DX.RPH.UNR.PL.CCY` | `DxRepPosHist_UnrPlCcy` |  |  |  |
| 43 | `DX.RPH.UNR.PL.AMT` | `DxRepPosHist_UnrPlAmt` |  |  |  |
| 44 | `DX.RPH.TX.NET.COST` | `DxRepPosHist_TxNetCost` |  |  |  |
| 45 | `DX.RPH.OPTION.TYPE` | `DxRepPosHist_OptionType` |  |  |  |
| 46 | `DX.RPH.USR.FLD.NAME` | `DxRepPosHist_UsrFldName` |  |  |  |
| 47 | `DX.RPH.USR.FLD.VAL` | `DxRepPosHist_UsrFldVal` |  |  |  |
| 48 | `DX.RPH.USR.FLD.TEXT` | `DxRepPosHist_UsrFldText` |  |  |  |
| 49 | `DX.RPH.USR.PRICE` | `DxRepPosHist_UsrPrice` |  |  |  |
| 50 | `DX.RPH.PVD.BUY.LOTS` | `DxRepPosHist_PvdBuyLots` | TField |  | The value dated buy positions |
| 51 | `DX.RPH.PVD.SELL.LOTS` | `DxRepPosHist_PvdSellLots` | TField |  | The value dated sell position. |
| 52 | `DX.RPH.PVD.NET.LOTS` | `DxRepPosHist_PvdNetLots` | TField |  | The value dated net position. (Long or Short) |
| 53 | `DX.RPH.AVG.PRICE` | `DxRepPosHist_AvgPrice` | TField |  | The average traded price for this position based on the setup for the contract. This is expressed in external format. |
| 54 | `DX.RPH.AVG.IPRICE` | `DxRepPosHist_AvgIprice` | TField |  | The average traded price for this position based on the setup for the contract. This is expressed in DX internal format. |
| 55 | `DX.RPH.AVG.BUY.PRICE` | `DxRepPosHist_AvgBuyPrice` | TField |  | Weighted average of external price for buy positions |
| 56 | `DX.RPH.AVG.BUY.IPRICE` | `DxRepPosHist_AvgBuyIprice` | TField |  | Weighted average of internal price for buy positions |
| 57 | `DX.RPH.AVG.SELL.PRICE` | `DxRepPosHist_AvgSellPrice` | TField |  | Weighted average of external price for sell positions |
| 58 | `DX.RPH.AVG.SELL.IPRICE` | `DxRepPosHist_AvgSellIprice` | TField |  | Weighted average of internal price for sell positions |
| 59 | `DX.RPH.FAR.PVD.DATE` | `DxRepPosHist_FarPvdDate` | TField |  | This field holds the date of the furthest out of all of the premium currently paid or pending for the position from a value dated perspective. |
| 60 | `DX.RPH.FST.PVD.DATE` | `DxRepPosHist_FstPvdDate` | TField |  | This field holds the date of the first out of all of the premium currently paid or pending for the position from a value dated perspective. |
| 61 | `DX.RPH.NXT.PVD.DATE` | `DxRepPosHist_NxtPvdDate` | TField |  | This field holds the date of the next due date out of all of the premium currently paid or pending for the position from a value dated perspective. |
| 62 | `DX.RPH.GROUP` | `DxRepPosHist_Group` | TField |  | This is the DX customer group to which the customer belongs. This information is taken from the DX.CUSTOMER record for this customer and is a valid entry on the DX.GROUPING file. This field is used as part of the valuation engine. |
| 63 | `DX.RPH.EXCHANGE.CODE` | `DxRepPosHist_ExchangeCode` | TField |  | This is the exchange on which the contract of this position would be traded. |
| 64 | `DX.RPH.CURRENCY` | `DxRepPosHist_Currency` | TField |  | The traded currency of the position. This will be a valid entry on the CURRENCY application. This information is also part of the key. |
| 65 | `DX.RPH.DELIVERY.CURRENCY` | `DxRepPosHist_DeliveryCurrency` | TField |  | For Foreign Exchange positions, this is the currency that this position will deliver at exercise/assignment time. This will be a valid entry on the CURRENCY application. |
| 66 | `DX.RPH.CONTRACT.CLASS` | `DxRepPosHist_ContractClass` | TField |  | The contract class of the position. This will be a valid entry on the DX.CONTRACT.CLASS application. |
| 67 | `DX.RPH.POSITION.TYPE` | `DxRepPosHist_PositionType` | TField |  | The positon type of this position. FUTURE or OPTION |
| 68 | `DX.RPH.OWN.BOOK` | `DxRepPosHist_OwnBook` | TField |  | This field holds the own book portfolio to which this portfolio belongs. It identifies is this position is an own book position. This data is taken from the DX.TRANSACTION OWN.BOOK field, which is taken from the DEALER.DESK field on SEC.ACC.MASTER |
| 69 | `DX.RPH.POS.DATE` | `DxRepPosHist_PosDate` | TField |  | This field represents the value date of this position, it could be in past, today or future. |
| 70 | `DX.RPH.FWD.TXN` | `DxRepPosHist_FwdTxn` |  |  |  |
| 71 | `DX.RPH.FWD.BUY.SELL` | `DxRepPosHist_FwdBuySell` |  |  |  |
| 72 | `DX.RPH.FWD.LOTS` | `DxRepPosHist_FwdLots` |  |  |  |
| 73 | `DX.RPH.FWD.DATE` | `DxRepPosHist_FwdDate` |  |  |  |
| 74 | `DX.RPH.COB.PRICE.ID` | `DxRepPosHist_CobPriceId` | TField |  | Key to the price record used to price this position. This will be a valid DX.MARKET.PRICE id. |
| 75 | `DX.RPH.REGION` | `DxRepPosHist_Region` | TField |  | Region code which applies to this position - this will have been defined in the relevant DX.EXCHANGE.MASTER record in the REGION field. Regions exist to segregate a Region within a Country where the public holidays differ from other parts of the Country. This enables a separate HOLIDAY table to be defined for the Region, to allow delivery to be controlled within the T24 system. |
| 76 | `DX.RPH.LOCAL.REF` | `DxRepPosHist_LocalRef` |  |  |  |
| 77 | `DX.RPH.OPTION.STYLE` | `DxRepPosHist_OptionStyle` | TField |  |  |
| 78 | `DX.RPH.RECORD.STATUS` | `DxRepPosHist_RecordStatus` | String |  |  |
| 79 | `DX.RPH.CURR.NO` | `DxRepPosHist_CurrNo` | String |  |  |
| 80 | `DX.RPH.INPUTTER` | `DxRepPosHist_Inputter` |  |  |  |
| 81 | `DX.RPH.DATE.TIME` | `DxRepPosHist_DateTime` |  |  |  |
| 82 | `DX.RPH.AUTHORISER` | `DxRepPosHist_Authoriser` | String |  |  |
| 83 | `DX.RPH.CO.CODE` | `DxRepPosHist_CoCode` | String |  |  |
| 84 | `DX.RPH.DEPT.CODE` | `DxRepPosHist_DeptCode` | String |  |  |
| 85 | `DX.RPH.AUDITOR.CODE` | `DxRepPosHist_AuditorCode` | String |  |  |
| 86 | `DX.RPH.AUDIT.DATE.TIME` | `DxRepPosHist_AuditDateTime` | String |  |  |
