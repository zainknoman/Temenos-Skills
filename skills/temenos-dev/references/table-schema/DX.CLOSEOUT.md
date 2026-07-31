# DX.CLOSEOUT — Table Schema

> Source: `INSERTS/I_F.DX.CLOSEOUT` in `DX_Closeout.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.CO.STATUS` | `DxCloseout_Status` | TField |  | The status of this close out. Maybe one of the following RUNNING. The closeout is currently taking place. ACTIVE. The closeout has occurred. I.e the trades have been matched and the close out is now waiting for authorisation. DELETED. The closeout has been reversed/bust |
| 2 | `DX.CO.TYPE` | `DxCloseout_Type` | TField |  | This field identifies the type of close out. Type Meaning Creation SETTLEMENT A closeout matching lot against lot. MANUAL/AUTOMATIC/SYSTEM MATURITY An Manual settlement maturing individual trades. MANUAL EXERCISE The Exercising of an Option MANUAL/AUTOMATIC/SYSTEM EXPIRY The Expiry of a Option. MANUAL/AUTOMATIC/SYSTEM ASSIGNMENT The Assignment of a Option. MANUAL/AUTOMATIC FIXING The Fixing of a IRS Option MANUAL Validation Rules: Can only be one of the following : SETTLEMENT, MATURITY, EXERCISE, EXPIRY or ASSIGNMENT |
| 3 | `DX.CO.CREATION` | `DxCloseout_Creation` | TField |  | How the close out was created. MANUAL - As part of a manual/maturity closeout from using a series of selection criteria. AUTOMATIC - The automatic closeout of a customer or a customers positions. SYSTEM - A system closeout carried out under instruction of the end of day or end of exchange. BACK2BACK &amp;#8211; Back to back closeout triggered for a secondary customer Validation Rules: Can only be MANUAL, AUTOMATIC, SYSTEM or BACK2BACK |
| 4 | `DX.CO.SETT.TYPE` | `DxCloseout_SettType` | TField |  | The automatic settlement type selected by the system for this closeout. Validation Rules: Must exisit on the DX.CLOSEOUT.METHOD field Must be defined as the closeout method for this customer. |
| 5 | `DX.CO.DELIVERY.CCY` | `DxCloseout_DeliveryCcy` | TField |  | Specifies the delivery currency of the trade involved for the closeout. Validation Rules: Type CCY NOINPUT field Must correspond to the id of record in the CURRENCY table |
| 6 | `DX.CO.CUSTOMER` | `DxCloseout_Customer` | TField |  | The customer for who the close out occurred. May be the Bank's own book or an external customer or broker Validation Rules: A valid T24 customer. Must exist as a valid record within the DX.CUSTOMER and CUSTOMER File. |
| 7 | `DX.CO.PORTFOLIO` | `DxCloseout_Portfolio` | TField |  | The portfolio for which this closeout is taking place. In the case of brokers this will be the same as there customer no. Validation Rules: Must exist as a valid portfolio on SEC.ACC.MASTER |
| 8 | `DX.CO.ACCOUNT` | `DxCloseout_Account` | TField |  | Identifies the Account over which financial entries relating to the customer for the closeout, are to be passed. Validation Rules: None |
| 9 | `DX.CO.CONTRACT.CODE` | `DxCloseout_ContractCode` | TField |  | The Contract code for this closeout. All transactions and trades associated with this Closeout will be of this contract type. Validation Rules: None |
| 10 | `DX.CO.MATURITY.DATE` | `DxCloseout_MaturityDate` | TField |  | The delivery period or prompt date of the contract transacted. All transactions associated with this closeout will have matching maturity dates. Validation Rules: None |
| 11 | `DX.CO.INP.MAT.DATE` | `DxCloseout_InpMatDate` | TField |  | The delivery period or prompt date of the contract transacted, in the format entered by the user. All transactions associated with this closeout will have matching maturity dates. Validation Rules: None |
| 12 | `DX.CO.TRADE.TYPE` | `DxCloseout_TradeType` | TField |  | The type of trades that are being closed out. FUTURE - A futures contract STOCK - A stock contract OPTION - An Options Contract Validation Rules: None |
| 13 | `DX.CO.OPTION.TYPE` | `DxCloseout_OptionType` | TField |  | Only applicable for option close outs. The option type of the trades/transactions which constiute this closout Validation Rules: Only CALL or PUT |
| 14 | `DX.CO.STRIKE.PRICE` | `DxCloseout_StrikePrice` | TField |  | Only applicable for option close outs. The price at which an option holder has the right to buy (Call Options) or sell (Put Options) the underlying instrument, or to cash-settle the option if appropriate, to exercise the option. All trades and transaction associated with this closeout will have the same Strike Price Validation Rules: None |
| 15 | `DX.CO.INT.STRIKE.PRICE` | `DxCloseout_IntStrikePrice` | TField |  | This field represents the strike price in internal format for T24 calculation. Validation Rules: None |
| 16 | `DX.CO.CURRENCY` | `DxCloseout_Currency` | TField |  | The currency of the profit or loss created by this close out. Validation Rules: None |
| 17 | `DX.CO.TOTAL.LOTS` | `DxCloseout_TotalLots` | TField |  | The total number of lots being closed out by this closeout. Validation Rules: None |
| 18 | `DX.CO.TOTAL.PANDL` | `DxCloseout_TotalPandl` | TField |  | The total value of the profit and loss for this closeout. The figure is held in the CURRENCY currecy. Validation Rules: None |
| 19 | `DX.CO.BUY.VALUE` | `DxCloseout_BuyValue` | TField |  | The total value of the lots bought, stored in the closeout currency. Validation Rules: None |
| 20 | `DX.CO.SELL.VALUE` | `DxCloseout_SellValue` | TField |  | The total value of the lots sold, stored in the closeout currency. Validation Rules: None |
| 21 | `DX.CO.CSN.TOTAL` | `DxCloseout_CsnTotal` | TField |  | Total Commission - not currently used Validation Rules: Rule 1 Rule 2 |
| 22 | `DX.CO.CSN.CCY` | `DxCloseout_CsnCcy` | TField |  | Commission Curreny - not currently used Validation Rules: Rule 1 Rule 2 |
| 23 | `DX.CO.MATURITY.PRICE` | `DxCloseout_MaturityPrice` | TField |  | Price at maturity of the contracts traded and associated with this closeout. For 'OPTION' trades, this is the Maturity 'PREMIUM' price. Validation Rules: None |
| 24 | `DX.CO.INT.MATURITY.PRICE` | `DxCloseout_IntMaturityPrice` | TField |  | The maturity price in standard T24 derivatives internal price format. Validation Rules: None |
| 25 | `DX.CO.BLOCK.REV` | `DxCloseout_BlockRev` | TField |  | If set to "YES" then reversals are not allowed for this closeout. |
| 26 | `DX.CO.NO.REV.REASON` | `DxCloseout_NoRevReason` | TField |  | If BLOCK.REV is set to yes then this field explains why |
| 27 | `DX.CO.DIARY.EVENT` | `DxCloseout_DiaryEvent` | TField |  | An valid ID from the DX.DIARY application. |
| 28 | `DX.CO.PRICE.TRADED` | `DxCloseout_PriceTraded` | TField |  | Specifies the price at which the trade is being done Validation Rules: No input field Upto 19 numeric values |
| 29 | `DX.CO.FEE` | `DxCloseout_Fee` | TField |  | Set to YES if fee is required else set to NO Validation Rules: No input field Upto 3 alphanumeric values Valid inputs are either YES or NO |
| 30 | `DX.CO.ADVICE` | `DxCloseout_Advice` | TField |  | Set to YES if a transfer advice is to be produced else set to NO Validation Rules: No input field Upto 3 alphanumeric values Valid inputs are either YES or NO |
| 31 | `DX.CO.B2B.CO.ID` | `DxCloseout_B2bCoId` |  |  |  |
| 32 | `DX.CO.B2B.PAR.ID` | `DxCloseout_B2bParId` |  |  |  |
| 33 | `DX.CO.RESERVED17` | `DxCloseout_Reserved17` | TField |  | Reserved For Future Use Validation Rules: None |
| 34 | `DX.CO.CHILD.TRADE.ID` | `DxCloseout_ChildTradeId` |  |  |  |
| 35 | `DX.CO.TRADE.ID` | `DxCloseout_TradeId` |  |  |  |
| 36 | `DX.CO.TRANS.ID` | `DxCloseout_TransId` |  |  |  |
| 37 | `DX.CO.TRA.BUY.LOTS` | `DxCloseout_TraBuyLots` |  |  |  |
| 38 | `DX.CO.TRA.SELL.LOTS` | `DxCloseout_TraSellLots` |  |  |  |
| 39 | `DX.CO.TRA.BUY.VALUE` | `DxCloseout_TraBuyValue` |  |  |  |
| 40 | `DX.CO.TRA.SELL.VALUE` | `DxCloseout_TraSellValue` |  |  |  |
| 41 | `DX.CO.RESERVED15` | `DxCloseout_Reserved15` |  |  |  |
| 42 | `DX.CO.RESERVED14` | `DxCloseout_Reserved14` |  |  |  |
| 43 | `DX.CO.RESERVED13` | `DxCloseout_Reserved13` |  |  |  |
| 44 | `DX.CO.RESERVED12` | `DxCloseout_Reserved12` |  |  |  |
| 45 | `DX.CO.RESERVED11` | `DxCloseout_Reserved11` |  |  |  |
| 46 | `DX.CO.RESERVED10` | `DxCloseout_Reserved10` |  |  |  |
| 47 | `DX.CO.DET.LOTS` | `DxCloseout_DetLots` |  |  |  |
| 48 | `DX.CO.O.C` | `DxCloseout_OC` |  |  |  |
| 49 | `DX.CO.D.S` | `DxCloseout_DS` |  |  |  |
| 50 | `DX.CO.DET.RES05` | `DxCloseout_DetRes05` |  |  |  |
| 51 | `DX.CO.SAFEKEEP.ACCT.NO` | `DxCloseout_SafekeepAcctNo` | TField |  | This field will hold the customer account which will be used to post the Safekeeping Charges. |
| 52 | `DX.CO.SAFEKEEP.FEE.LCY` | `DxCloseout_SafekeepFeeLcy` | TField |  | This field will be populated with the respective safekeep fees charged during Exercise/Expire/Assign. |
| 53 | `DX.CO.SK.ACY.LCY.RATE` | `DxCloseout_SkAcyLcyRate` | TField |  | This field holds the exchange rate between the account currency (SAFEKEEP.ACT.NO) and local currency |
| 54 | `DX.CO.SAFEKEEP.FEE.ACY` | `DxCloseout_SafekeepFeeAcy` | TField |  | This field will be populated with the respective safekeep fees charged during Exercise/Expire/Assign The amount calculated will be in the SAFEKEEP.ACCT.NO currency. |
| 55 | `DX.CO.DEST.CUST` | `DxCloseout_DestCust` | TField |  | Specifies the internal recipient customer Validation Rules: Upto 10 numeric values Must be a valid record in CUSTOMER application |
| 56 | `DX.CO.DEST.PORTFOLIO` | `DxCloseout_DestPortfolio` | TField |  | Specifies the external recipient customer portfolio reference if any Validation Rules: No input field Upto 18 alphanumeric values |
| 57 | `DX.CO.DEST.CUST.PORT` | `DxCloseout_DestCustPort` | TField |  | A valid id from the CUSTOMER table. |
| 58 | `DX.CO.CUST.CPARTY` | `DxCloseout_CustCparty` | TField |  | A valid id from the CUSTOMER table. |
| 59 | `DX.CO.CUST.BNK.NME` | `DxCloseout_CustBnkNme` | TField |  | The name of the customers bank. |
| 60 | `DX.CO.CUST.BNK.ADD` | `DxCloseout_CustBnkAdd` | TField |  | The address of the customers bank. |
| 61 | `DX.CO.CUST.BNK.SORT.CDE` | `DxCloseout_CustBnkSortCde` | TField |  | The sort code of the customers bank. |
| 62 | `DX.CO.PRI.HEDGE.TRADE` | `DxCloseout_PriHedgeTrade` | TField |  | This will can be set to HEDGE or TRADE. |
| 63 | `DX.CO.TAX.CODE` | `DxCloseout_TaxCode` |  |  |  |
| 64 | `DX.CO.TAX.TYPE` | `DxCloseout_TaxType` |  |  |  |
| 65 | `DX.CO.TAX.AMT.ACY` | `DxCloseout_TaxAmtAcy` |  |  |  |
| 66 | `DX.CO.TAX.AMT.TCY` | `DxCloseout_TaxAmtTcy` |  |  |  |
| 67 | `DX.CO.MARKET.PRICE` | `DxCloseout_MarketPrice` | TField |  | Holds the market price of the security at the time of exercise. |
| 68 | `DX.CO.DLV.CCY.RATE` | `DxCloseout_DlvCcyRate` | TField |  | Holds the excahnge rate between trade currency and settlement currecny. |
| 69 | `DX.CO.SETTLE.INSTRUMENT` | `DxCloseout_SettleInstrument` | TField |  | Holds the settlement instrument for physically settled contracts |
| 70 | `DX.CO.SETT.INSTR.CONT.SIZE` | `DxCloseout_SettInstrContSize` | TField | Yes | The contract size of the alternate settlement instrument which is mandatory when settled using alternate underlying. |
| 71 | `DX.CO.SETT.INSTR.PRICE` | `DxCloseout_SettInstrPrice` | TField | Yes | The price of the alternate settlement instrument which is mandatory when settled using alternate underlying. |
| 72 | `DX.CO.QUOTE.CCY` | `DxCloseout_QuoteCcy` | TField |  | The currency in which the SPOT.EXCHANGE.RATE is quoted. |
| 73 | `DX.CO.SPOT.EXCHANGE.RATE` | `DxCloseout_SpotExchangeRate` | TField |  | Holds the current exchange rate between the currency pairs of an FX option quoted in the QUOTE.CCY i.e base currency being the strike quote currency for generic FX-OTC options and delivery currency for fx options. |
| 74 | `DX.CO.FX.PAYOUT.CCY` | `DxCloseout_FxPayoutCcy` | TField |  | Currency in which the payout is to be made for cash settled FX options. |
| 75 | `DX.CO.SPOT.PAYOUT.RATE` | `DxCloseout_SpotPayoutRate` | TField |  | Holds the exchange rate between QUOTE.CCY and FX.PAYOUT.CCY. |
| 76 | `DX.CO.CLO.APP.ID` | `DxCloseout_CloAppId` | TField |  | Updated with closeout application id i.e the Id of DX.CO.EXERCISE.MANUAL or DX.CO.EXERCISE.AUTO or DX.CO.ASSIGN.MANUAL or DX.CO.ASSIGN.AUTO. |
| 77 | `DX.CO.PAYMENT.ORDER.ID` | `DxCloseout_PaymentOrderId` |  |  |  |
| 78 | `DX.CO.DATE.UPDATED` | `DxCloseout_DateUpdated` | TField |  |  |
| 79 | `DX.CO.RESERVED02` | `DxCloseout_Reserved02` | TField |  | Reserved for future use. Validation Rules: None |
| 80 | `DX.CO.RESERVED01` | `DxCloseout_Reserved01` | TField |  | Reserved for future use. Validation Rules: None |
| 81 | `DX.CO.LOCAL.REF` | `DxCloseout_LocalRef` |  |  |  |
| 82 | `DX.CO.OVERRIDE` | `DxCloseout_Override` |  |  |  |
| 83 | `DX.CO.RECORD.STATUS` | `DxCloseout_RecordStatus` | String |  |  |
| 84 | `DX.CO.CURR.NO` | `DxCloseout_CurrNo` | String |  |  |
| 85 | `DX.CO.INPUTTER` | `DxCloseout_Inputter` |  |  |  |
| 86 | `DX.CO.DATE.TIME` | `DxCloseout_DateTime` |  |  |  |
| 87 | `DX.CO.AUTHORISER` | `DxCloseout_Authoriser` | String |  |  |
| 88 | `DX.CO.CO.CODE` | `DxCloseout_CoCode` | String |  |  |
| 89 | `DX.CO.DEPT.CODE` | `DxCloseout_DeptCode` | String |  |  |
| 90 | `DX.CO.AUDITOR.CODE` | `DxCloseout_AuditorCode` | String |  |  |
| 91 | `DX.CO.AUDIT.DATE.TIME` | `DxCloseout_AuditDateTime` | String |  |  |
