# DX.REP.POSITION — Table Schema

> Source: `INSERTS/I_F.DX.REP.POSITION` in `DX_Position.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.RP.CUSTOMER` | `DxRepPosition_Customer` | TField |  | The customer holding the position |
| 2 | `DX.RP.PORTFOLIO` | `DxRepPosition_Portfolio` | TField |  | The T24 Portfolio holding the position |
| 3 | `DX.RP.CONTRACT` | `DxRepPosition_Contract` | TField |  | The contract that is being traded. This will be a valid DX.CONTRACT.MASTER id. |
| 4 | `DX.RP.MATURITY.DATE` | `DxRepPosition_MaturityDate` | TField |  | Maturity period of the position |
| 5 | `DX.RP.STRIKE.PRICE` | `DxRepPosition_StrikePrice` | TField |  | Internal strike price for OPTION type positions. This field is populated from the DX.TRANSACTION record field INT.STRIKE and holds the T24 internal strike price for the option. |
| 6 | `DX.RP.CALL.PUT` | `DxRepPosition_CallPut` | TField |  | Type of OPTION trade. CALL or PUT |
| 7 | `DX.RP.EXT.STRIKE.PRI` | `DxRepPosition_ExtStrikePri` | TField |  | Strike price for OPTION type position in external format. This field is populated from the DX.TRANSACTION record field STRIKE. |
| 8 | `DX.RP.BUY.LOTS` | `DxRepPosition_BuyLots` | TField |  | Total number of lots bought in this contract for this position |
| 9 | `DX.RP.SELL.LOTS` | `DxRepPosition_SellLots` | TField |  | Total number of Sold Lots for this position |
| 10 | `DX.RP.NET.LOTS` | `DxRepPosition_NetLots` | TField |  | Net lots for this position, long or short. |
| 11 | `DX.RP.TRANSACTION.IDS` | `DxRepPosition_TransactionIds` |  |  |  |
| 12 | `DX.RP.TX.BUY.SELL` | `DxRepPosition_TxBuySell` |  |  |  |
| 13 | `DX.RP.TX.OPEN.CLOSE` | `DxRepPosition_TxOpenClose` |  |  |  |
| 14 | `DX.RP.TX.PRICE` | `DxRepPosition_TxPrice` |  |  |  |
| 15 | `DX.RP.TX.IPRICE` | `DxRepPosition_TxIprice` |  |  |  |
| 16 | `DX.RP.TX.LOTS` | `DxRepPosition_TxLots` |  |  |  |
| 17 | `DX.RP.TX.ORIG.LOTS` | `DxRepPosition_TxOrigLots` |  |  |  |
| 18 | `DX.RP.TX.BASE.LOTS` | `DxRepPosition_TxBaseLots` |  |  |  |
| 19 | `DX.RP.TX.BUY.LOTS` | `DxRepPosition_TxBuyLots` |  |  |  |
| 20 | `DX.RP.TX.SELL.LOTS` | `DxRepPosition_TxSellLots` |  |  |  |
| 21 | `DX.RP.TX.TRADE.DATE` | `DxRepPosition_TxTradeDate` |  |  |  |
| 22 | `DX.RP.TX.PREM.OFFSET` | `DxRepPosition_TxPremOffset` |  |  |  |
| 23 | `DX.RP.TX.PV.DATE` | `DxRepPosition_TxPvDate` |  |  |  |
| 24 | `DX.RP.TX.PVD.LOTS` | `DxRepPosition_TxPvdLots` |  |  |  |
| 25 | `DX.RP.TX.PVD.SIGN.LT` | `DxRepPosition_TxPvdSignLt` |  |  |  |
| 26 | `DX.RP.TX.PVD.BUY.LT` | `DxRepPosition_TxPvdBuyLt` |  |  |  |
| 27 | `DX.RP.TX.PVD.SELL.LT` | `DxRepPosition_TxPvdSellLt` |  |  |  |
| 28 | `DX.RP.TX.CO.ID` | `DxRepPosition_TxCoId` |  |  |  |
| 29 | `DX.RP.TX.CO.DATE` | `DxRepPosition_TxCoDate` |  |  |  |
| 30 | `DX.RP.TX.CO.PV.DT` | `DxRepPosition_TxCoPvDt` |  |  |  |
| 31 | `DX.RP.TX.CO.LOTS` | `DxRepPosition_TxCoLots` |  |  |  |
| 32 | `DX.RP.TX.CO.PV.LT` | `DxRepPosition_TxCoPvLt` |  |  |  |
| 33 | `DX.RP.TX.CO.TYPE` | `DxRepPosition_TxCoType` |  |  |  |
| 34 | `DX.RP.TX.CO.OFFSET` | `DxRepPosition_TxCoOffset` |  |  |  |
| 35 | `DX.RP.FAR.CO.DATE` | `DxRepPosition_FarCoDate` |  |  |  |
| 36 | `DX.RP.FAR.CO.PV.DATE` | `DxRepPosition_FarCoPvDate` |  |  |  |
| 37 | `DX.RP.CO.LOTS` | `DxRepPosition_CoLots` |  |  |  |
| 38 | `DX.RP.CO.PV.LOTS` | `DxRepPosition_CoPvLots` |  |  |  |
| 39 | `DX.RP.ENTITLEMENT` | `DxRepPosition_Entitlement` |  |  |  |
| 40 | `DX.RP.VAR.MAR.CCY` | `DxRepPosition_VarMarCcy` |  |  |  |
| 41 | `DX.RP.VAR.MARGIN` | `DxRepPosition_VarMargin` |  |  |  |
| 42 | `DX.RP.UNR.PL.CCY` | `DxRepPosition_UnrPlCcy` |  |  |  |
| 43 | `DX.RP.UNR.PL.AMT` | `DxRepPosition_UnrPlAmt` |  |  |  |
| 44 | `DX.RP.TX.NET.COST` | `DxRepPosition_TxNetCost` |  |  |  |
| 45 | `DX.RP.OPTION.TYPE` | `DxRepPosition_OptionType` |  |  |  |
| 46 | `DX.RP.USR.FLD.NAME` | `DxRepPosition_UsrFldName` |  |  |  |
| 47 | `DX.RP.USR.FLD.VAL` | `DxRepPosition_UsrFldVal` |  |  |  |
| 48 | `DX.RP.USR.FLD.TEXT` | `DxRepPosition_UsrFldText` |  |  |  |
| 49 | `DX.RP.USR.PRICE` | `DxRepPosition_UsrPrice` |  |  |  |
| 50 | `DX.RP.PVD.BUY.LOTS` | `DxRepPosition_PvdBuyLots` | TField |  | The value dated buy positions |
| 51 | `DX.RP.PVD.SELL.LOTS` | `DxRepPosition_PvdSellLots` | TField |  | The value dated sell position. |
| 52 | `DX.RP.PVD.NET.LOTS` | `DxRepPosition_PvdNetLots` | TField |  | The value dated net position. (Long or Short) |
| 53 | `DX.RP.AVG.PRICE` | `DxRepPosition_AvgPrice` | TField |  | The average traded price for this position based on the setup for the contract. This is expressed in external format. |
| 54 | `DX.RP.AVG.IPRICE` | `DxRepPosition_AvgIprice` | TField |  | The average traded price for this position based on the setup for the contract. This is expressed in DX internal format. |
| 55 | `DX.RP.AVG.BUY.PRICE` | `DxRepPosition_AvgBuyPrice` | TField |  | Weighted average of external price for buy positions |
| 56 | `DX.RP.AVG.BUY.IPRICE` | `DxRepPosition_AvgBuyIprice` | TField |  | Weighted average of internal price for buy positions |
| 57 | `DX.RP.AVG.SELL.PRICE` | `DxRepPosition_AvgSellPrice` | TField |  | Weighted average of external price for sell positions |
| 58 | `DX.RP.AVG.SELL.IPRICE` | `DxRepPosition_AvgSellIprice` | TField |  | Weighted average of internal price for sell positions |
| 59 | `DX.RP.FAR.PVD.DATE` | `DxRepPosition_FarPvdDate` | TField |  | This field holds the date of the furthest out of all of the premium currently paid or pending for the position from a value dated perspective. |
| 60 | `DX.RP.FST.PVD.DATE` | `DxRepPosition_FstPvdDate` | TField |  | This field holds the date of the first out of all of the premium currently paid or pending for the position from a value dated perspective. |
| 61 | `DX.RP.NXT.PVD.DATE` | `DxRepPosition_NxtPvdDate` | TField |  | This field holds the date of the next due date out of all of the premium currently paid or pending for the position from a value dated perspective. |
| 62 | `DX.RP.GROUP` | `DxRepPosition_Group` | TField |  | This is the DX customer group to which the customer belongs. This information is taken from the DX.CUSTOMER record for this customer and is a valid entry on the DX.GROUPING file. This field is used as part of the valuation engine. |
| 63 | `DX.RP.EXCHANGE.CODE` | `DxRepPosition_ExchangeCode` | TField |  | This is the exchange on which the contract of this position would be traded. |
| 64 | `DX.RP.CURRENCY` | `DxRepPosition_Currency` | TField |  | The traded currency of the position. This will be a valid entry on the CURRENCY application. This information is also part of the key. |
| 65 | `DX.RP.DELIVERY.CURRENCY` | `DxRepPosition_DeliveryCurrency` | TField |  | For Foreign Exchange positions, this is the currency that this position will deliver at exercise/assignment time. This will be a valid entry on the CURRENCY application. |
| 66 | `DX.RP.CONTRACT.CLASS` | `DxRepPosition_ContractClass` | TField |  | The contract class of the position. This will be a valid entry on the DX.CONTRACT.CLASS application. |
| 67 | `DX.RP.POSITION.TYPE` | `DxRepPosition_PositionType` | TField |  | The positon type of this position. FUTURE or OPTION |
| 68 | `DX.RP.OWN.BOOK` | `DxRepPosition_OwnBook` | TField |  | This field holds the own book portfolio to which this portfolio belongs. It identifies is this position is an own book position. This data is taken from the DX.TRANSACTION OWN.BOOK field, which is taken from the DEALER.DESK field on SEC.ACC.MASTER |
| 69 | `DX.RP.POS.DATE` | `DxRepPosition_PosDate` | TField |  | This field represents the value date of this position, it could be in past, today or future. |
| 70 | `DX.RP.FWD.TXN` | `DxRepPosition_FwdTxn` |  |  |  |
| 71 | `DX.RP.FWD.BUY.SELL` | `DxRepPosition_FwdBuySell` |  |  |  |
| 72 | `DX.RP.FWD.LOTS` | `DxRepPosition_FwdLots` |  |  |  |
| 73 | `DX.RP.FWD.DATE` | `DxRepPosition_FwdDate` |  |  |  |
| 74 | `DX.RP.COB.PRICE.ID` | `DxRepPosition_CobPriceId` | TField |  | Key to the price record used to price this position. This will be a valid DX.MARKET.PRICE id. |
| 75 | `DX.RP.REGION` | `DxRepPosition_Region` | TField |  | Region code which applies to this position - this will have been defined in the relevant DX.EXCHANGE.MASTER record in the REGION field. Regions exist to segregate a Region within a Country where the public holidays differ from other parts of the Country. This enables a separate HOLIDAY table to be defined for the Region, to allow delivery to be controlled within the T24 system. |
| 76 | `DX.RP.LOCAL.REF` | `DxRepPosition_LocalRef` |  |  |  |
| 77 | `DX.RP.OPTION.STYLE` | `DxRepPosition_OptionStyle` | TField |  | A NOINPUT field which holds the first character of option style value in DX.TRADE. This will hold the value either �A� for American, �E� for European or �C� for Carribean options |
| 78 | `DX.RP.TERMS` | `DxRepPosition_Terms` | TField |  | Holds a valid DX.CONTRACT.TERMS |
