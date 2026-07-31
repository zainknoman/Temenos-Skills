# DX.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.DX.TRANSACTION` in `DX_Trade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.TX.PORT.CUST.ID` | `DxTransaction_PortCustId` | TField |  | Portfolio or customer id for this transaction. Validation Rules: Must be a valid record on DX.CUSTOMER or SEC.ACC.MASTER |
| 2 | `DX.TX.TRANS.DATE` | `DxTransaction_TransDate` | TField |  | Actual date of transaction update. Validation Rules: Up to 11 characters in DATE format |
| 3 | `DX.TX.REVERSAL.DATE` | `DxTransaction_ReversalDate` | TField |  | Date of reversal of source application record, or replacement with newer version. Validation Rules: Up to 11 characters in DATE format Null unless parent transaction is reversed or adjusted |
| 4 | `DX.TX.REVERSAL.TIME` | `DxTransaction_ReversalTime` | TField |  | System time stamp on reversal or amendment of parent transaction. Validation Rules: Up to 5 character in TIME format Null unless parent transaction is reversed or adjusted |
| 5 | `DX.TX.SOURCE.REF` | `DxTransaction_SourceRef` | TField |  | ID of Source transaction. Validation Rules: 35 Alpha |
| 6 | `DX.TX.CONTRACT.CODE` | `DxTransaction_ContractCode` | TField |  | Contract code associated with this transaction. Validation Rules: Up to 12 characters, input must be a valid record on the DX.CONTRACT.MASTER Application |
| 7 | `DX.TX.EXCHANGE.CODE` | `DxTransaction_ExchangeCode` | TField |  | The name of the Exchange where the applicable contract is traded. Up 10 characters, input must be a valid record on the DX.EXCHANGE.MASTER Application |
| 8 | `DX.TX.TRADE.DATE` | `DxTransaction_TradeDate` | TField |  | The date in which the transaction is performed. Validation Rules: Up to 11 characters in DATE format |
| 9 | `DX.TX.MATURITY.DATE` | `DxTransaction_MaturityDate` | TField |  | The delivery period or prompt date of the contract transacted. Validation Rules: Up to 11 characters, input must be a valid Maturity Date |
| 10 | `DX.TX.ACCOUNT` | `DxTransaction_Account` | TField |  | Identifies the account, over which financial entries relating to the transaction are to be passed. Validation Rules: Up to 16 characters, input must be a valid record on the ACCOUNT Application |
| 11 | `DX.TX.EVENT.TYPE` | `DxTransaction_EventType` |  |  |  |
| 12 | `DX.TX.LAST.REP.POS` | `DxTransaction_LastRepPos` | TField |  | Holds the id of DX.REP.POS.LAST. This links to the last time that position was updated. |
| 13 | `DX.TX.TRANS.NAME` | `DxTransaction_TransName` | TField |  | The TRANS.NAME is different depending on the application e.g. DX.TRADE-FUTURE_OPTION Validation Rules: Up to 10 characters |
| 14 | `DX.TX.BUY.SELL` | `DxTransaction_BuySell` | TField |  | Contract buy or sell flag BUY_SELL updated by DX.TRADE. Validation Rules: Up to 4 characters, input must be either BUY/SELL |
| 15 | `DX.TX.CALL.PUT` | `DxTransaction_CallPut` | TField |  | Option contract call or put flag. CALL_PUT. Updated by DX.TRADE. Validation Rules: Up to 4 characters, input must be either CALL/PUT |
| 16 | `DX.TX.LOTS` | `DxTransaction_Lots` | TField |  | Number of active lots remaining on transaction. Validation Rules: Up to 19 characters |
| 17 | `DX.TX.ORIGINAL.LOTS` | `DxTransaction_OriginalLots` | TField |  | Original number of lots for this transaction. Validation Rules: Up to 19 characters |
| 18 | `DX.TX.PRICE` | `DxTransaction_Price` | TField |  | Price/Premium as input, with number of decimal places standardised to price d.p.'s Validation Rules: Up to 19 characters |
| 19 | `DX.TX.INT.PRICE` | `DxTransaction_IntPrice` | TField |  | Internal format trade price/premium for this transaction. Trade ccy. Premium for trades. Quoted as standard T24internal price. Validation Rules: Up to 19 characters |
| 20 | `DX.TX.PRICE.OUTPUT` | `DxTransaction_PriceOutput` | TField |  | Not in use |
| 21 | `DX.TX.STRIKE` | `DxTransaction_Strike` | TField |  | Strike price as input, with number of decimal places standardised to price d.p's. Only for OPTIONs. Required incase input strike needs to be sent to third party application. Validation Rules: Up to 19 characters |
| 22 | `DX.TX.INT.STRIKE` | `DxTransaction_IntStrike` | TField |  | Internal format strike price for option transaction. Only updated by DX.TRADE when trade type is OPTIONs. Held inthe standard internal T24 Format. Validation Rules: Up to 19 characters |
| 23 | `DX.TX.STRIKE.OUTPUT` | `DxTransaction_StrikeOutput` | TField |  | Not in use. |
| 24 | `DX.TX.TRANS.TIME` | `DxTransaction_TransTime` | TField |  | Time of transaction update. Validation Rules: Up to 5 characters in TIME format |
| 25 | `DX.TX.SUB.ASSET.TYPE` | `DxTransaction_SubAssetType` | TField |  | Sub asset type of contract traded. Updated by DX.TRADE Validation Rules: Linked to SUB.ASSET.TYPE 5 Alpha |
| 26 | `DX.TX.DEC.DATE` | `DxTransaction_DecDate` | TField | Yes | The Last Date by which a customer may exercise an option. The exercise date (European Options) or last exercisedate (American Options) for this contract. This field will default to date calculated from Date formula for Dec.Date on DX.CONTRACT.MASTER, but this can beoverriden as required. Validation Rules: Up to 9 type D date format characters. Mandatory Input if CONTRACT.TYPE is "OPTION |
| 27 | `DX.TX.PENDING.DIARY` | `DxTransaction_PendingDiary` | TField |  | Should be a valid record in DX.DIARY. |
| 28 | `DX.TX.ENTITLEMENT` | `DxTransaction_Entitlement` |  |  |  |
| 29 | `DX.TX.PREM.OFFSET` | `DxTransaction_PremOffset` | TField |  | Represents the premium payment offset for this transaction. No of days offset from charging to account posting for premiums for the customer. |
| 30 | `DX.TX.LAST.REVAL.LOTS` | `DxTransaction_LastRevalLots` | TField |  | Number of lots active on this transaction at last reval time. Validation Rules: 19 Numeric |
| 31 | `DX.TX.LOTS.SETTLED` | `DxTransaction_LotsSettled` | TField |  | Number of lots settled in this transaction. Only updated by DX.CO.PROCESS. Validation Rules: Up to 19 characters |
| 32 | `DX.TX.SETT.VAL.ACC.CCY` | `DxTransaction_SettValAccCcy` | TField |  | Settlement value (P&amp;L) generated in account currency. Only updated by DX.CO.PROCESS Validation Rules: 19 Numeric |
| 33 | `DX.TX.SETT.VAL.REF.CCY` | `DxTransaction_SettValRefCcy` | TField |  | Settlement value (P&amp;L) generated in reference currency. Only updated by DX.CO.PROCESS Validation Rules: Up to 19 characters |
| 34 | `DX.TX.LOTS.ACTIONED` | `DxTransaction_LotsActioned` | TField |  | The total number of lots being closed out by this closeout. Updated by DX.CO.PROCESS. Validation Rules: Up to 19 characters |
| 35 | `DX.TX.RESULTING.TRADE` | `DxTransaction_ResultingTrade` | TField |  | Not in use. |
| 36 | `DX.TX.INIT.MAR.CCY` | `DxTransaction_InitMarCcy` |  |  |  |
| 37 | `DX.TX.INIT.ACCOUNT` | `DxTransaction_InitAccount` |  |  |  |
| 38 | `DX.TX.INITIAL.MARGIN` | `DxTransaction_InitialMargin` |  |  |  |
| 39 | `DX.TX.IM.EXC.RATE` | `DxTransaction_ImExcRate` |  |  |  |
| 40 | `DX.TX.INIT.MAR.REF.CCY` | `DxTransaction_InitMarRefCcy` | TField |  | Description Specifies the total of initial margin figures converted into reference currency. |
| 41 | `DX.TX.VAR.MAR.CCY` | `DxTransaction_VarMarCcy` |  |  |  |
| 42 | `DX.TX.VAR.ACCOUNT` | `DxTransaction_VarAccount` |  |  |  |
| 43 | `DX.TX.VAR.MARGIN` | `DxTransaction_VarMargin` |  |  |  |
| 44 | `DX.TX.VM.EXC.RATE` | `DxTransaction_VmExcRate` |  |  |  |
| 45 | `DX.TX.VAR.MAR.REF.CCY` | `DxTransaction_VarMarRefCcy` | TField |  | Total of variation margin figures consolidated back to customer reference currency. Only updated byDX.RUN.REVALUE. Validation Rules: Up to 19 characters |
| 46 | `DX.TX.APP.STATUS` | `DxTransaction_AppStatus` | TField |  | Is this transaction authorised Validation Rules: Up to 4 characters |
| 47 | `DX.TX.STRATEGY` | `DxTransaction_Strategy` | TField |  | Its value is populated from DX.STRATEGY. A different strategy can be used for each side of the trade in the PRI.STRATEGY and SEC.STRATEGY fields. Whentransactions with a strategy are found as part of the revaluation process, the corresponding trades are valuedtogether using the margin routine, if specified, in the DX.STRATEGY record. It is used for reporting purposes. Validation Rules: Up to 20 characters, input must be a valid record on the DX.STRATEGY Application |
| 48 | `DX.TX.CUST.TYPE` | `DxTransaction_CustType` | TField |  | Customer type. Initally updated by DX.TRADE Validation Rules: Up to 15 characters |
| 49 | `DX.TX.CUST.STATUS` | `DxTransaction_CustStatus` | TField |  | Status of customer in terms of segregated/non-segregated business. Validation Rules: Up to 15 characters |
| 50 | `DX.TX.TRASETTNOS` | `DxTransaction_Trasettnos` |  |  |  |
| 51 | `DX.TX.TRASETTLOTS` | `DxTransaction_Trasettlots` |  |  |  |
| 52 | `DX.TX.CO.DATE` | `DxTransaction_CoDate` |  |  |  |
| 53 | `DX.TX.CO.PV.DATE` | `DxTransaction_CoPvDate` |  |  |  |
| 54 | `DX.TX.CO.TYPE` | `DxTransaction_CoType` |  |  |  |
| 55 | `DX.TX.CO.STMT.NOS` | `DxTransaction_CoStmtNos` |  |  |  |
| 56 | `DX.TX.OPEN.CLOSE` | `DxTransaction_OpenClose` | TField |  | Valid values are OPEN and CLOSE. This specifies the open or close status of the transaction. This is used in the new average price method OPENING. Validation Rules: Up to 5 characters, input must be either: OPEN/CLOSE |
| 57 | `DX.TX.HEDGE.TRADE` | `DxTransaction_HedgeTrade` | TField |  | Is this a hedge or speculative trade transaction. Validation Rules: Up to 15 characters, input must be HEDGE/TRADE |
| 58 | `DX.TX.LINK` | `DxTransaction_Link` |  |  |  |
| 59 | `DX.TX.ALLOW.SETT` | `DxTransaction_AllowSett` | TField |  | Are close-outs allowed for the leg of the trrade represented by the transaction record. Validation Rules: Up to 3 characters, input must be either: YES/NO |
| 60 | `DX.TX.COMM.TYP` | `DxTransaction_CommTyp` |  |  |  |
| 61 | `DX.TX.COMM.CDE` | `DxTransaction_CommCde` |  |  |  |
| 62 | `DX.TX.COMM.CCY` | `DxTransaction_CommCcy` |  |  |  |
| 63 | `DX.TX.COMM.AMT` | `DxTransaction_CommAmt` |  |  |  |
| 64 | `DX.TX.COMM.ACC` | `DxTransaction_CommAcc` |  |  |  |
| 65 | `DX.TX.CACC.CCY` | `DxTransaction_CaccCcy` |  |  |  |
| 66 | `DX.TX.COMM.EXC` | `DxTransaction_CommExc` |  |  |  |
| 67 | `DX.TX.CACC.AMT` | `DxTransaction_CaccAmt` |  |  |  |
| 68 | `DX.TX.COMM.TAX` | `DxTransaction_CommTax` |  |  |  |
| 69 | `DX.TX.CHARGE.DATE` | `DxTransaction_ChargeDate` | TField |  | Date of application of commission/charges/premium. Updated by DX.TRADE. Validation Rules: Up to 10 characters, input must be either: TRADE/SETTLEMENT |
| 70 | `DX.TX.REF.CCY` | `DxTransaction_RefCcy` | TField |  | For revaluation this field represents the reference/reporting currency of the client. Validation Rules: Up to 3 characters in CCY format |
| 71 | `DX.TX.ACC.CCY` | `DxTransaction_AccCcy` | TField |  | Customer account currency Updated by DX.TRADE. Validation Rules: Up to 3 characters in CCY format |
| 72 | `DX.TX.EX.RATE.REF` | `DxTransaction_ExRateRef` | TField |  | Exchange rate between customer reference and trade currency. Updated by DX.TRADE Validation Rules: Up to 19 characters in AMT format |
| 73 | `DX.TX.EX.RATE.ACC` | `DxTransaction_ExRateAcc` | TField |  | Exchange rate between trade currency and customer accountcurrency. Updated by DX.TRADE. Validation Rules: Up to 19 characters in AMT format |
| 74 | `DX.TX.OVE.ADDR` | `DxTransaction_OveAddr` |  |  |  |
| 75 | `DX.TX.MESS.CTL` | `DxTransaction_MessCtl` |  |  |  |
| 76 | `DX.TX.DLV.KEY` | `DxTransaction_DlvKey` |  |  |  |
| 77 | `DX.TX.ORDER.NO` | `DxTransaction_OrderNo` |  |  |  |
| 78 | `DX.TX.CUST.NARR` | `DxTransaction_CustNarr` |  |  |  |
| 79 | `DX.TX.CONSTRAINT` | `DxTransaction_Constraint` | TField |  | Trading constraint ID. Updated by DX.TRADE. Validation Rules: Up to 17 characters, input must be a valid record on the DX.TRADING.CONSTRAINT |
| 80 | `DX.TX.COUNTERPARTY` | `DxTransaction_Counterparty` |  |  |  |
| 81 | `DX.TX.CUSTOMER` | `DxTransaction_Customer` | TField |  | Identifies the Customer with whom the trade is made. Its value should be a valid record in CUSTOMER application. |
| 82 | `DX.TX.DEALER.DESK` | `DxTransaction_DealerDesk` | TField |  | The DEALER id for this transaction. Validation Rules: Up to 2 characters, input must exist on the DEALER.DESK Application |
| 83 | `DX.TX.DEPT.ACCT.OFFICER` | `DxTransaction_DeptAcctOfficer` | TField |  | Holds the department or account officer ID. Validation Rules: Up to 4 characters, input must be a valid record on the DEPT.ACCT.OFFICER Application |
| 84 | `DX.TX.OWN.BOOK` | `DxTransaction_OwnBook` | TField |  | This field holds the own book portfolio to which this portfolio belongs. Identifies whether the transaction is a own book transaction or not. Validation Rules: Up to 35 characters |
| 85 | `DX.TX.PRODUCT.CAT` | `DxTransaction_ProductCat` | TField |  | The product category. Validation Rules: Up to 6 characters, input must be a valid record on the CATEGORY Application |
| 86 | `DX.TX.RV.UPDATE.ID` | `DxTransaction_RvUpdateId` | TField |  | Holds the DX Revalue id. Validation Rules: Up to 35 characters |
| 87 | `DX.TX.STATEMENT.NOS` | `DxTransaction_StatementNos` |  |  |  |
| 88 | `DX.TX.CHG.OFFSET` | `DxTransaction_ChgOffset` | TField |  | Number of days charge off-set between earning and posting. Validation Rules: Up to 3 characters |
| 89 | `DX.TX.CUST.REF` | `DxTransaction_CustRef` | TField |  | Free text reference/narrative field mapped from either the PRI.CUS.REF or SEC.CUST.REF on the correspondingDX.TRADE. Up to 16 characters |
| 90 | `DX.TX.UOPT.PANDL.CCY` | `DxTransaction_UoptPandlCcy` |  |  |  |
| 91 | `DX.TX.UOPT.ACCOUNT` | `DxTransaction_UoptAccount` |  |  |  |
| 92 | `DX.TX.UOPT.PANDL` | `DxTransaction_UoptPandl` |  |  |  |
| 93 | `DX.TX.UOPT.PANDL.REF.CCY` | `DxTransaction_UoptPandlRefCcy` | TField |  | Total of variation margin figures consolidated back to customer reference currency. Only updated byDX.RUN.REVALUE. Validation Rules: Up to 19 characters |
| 94 | `DX.TX.TRA.PND.SETT` | `DxTransaction_TraPndSett` |  |  |  |
| 95 | `DX.TX.TRA.PND.LOTS` | `DxTransaction_TraPndLots` |  |  |  |
| 96 | `DX.TX.TRA.PND.STMT` | `DxTransaction_TraPndStmt` |  |  |  |
| 97 | `DX.TX.ACTIVITY.CODE` | `DxTransaction_ActivityCode` |  |  |  |
| 98 | `DX.TX.ACTIVITY.DATE` | `DxTransaction_ActivityDate` |  |  |  |
| 99 | `DX.TX.ACT.EVENT.TYPE` | `DxTransaction_ActEventType` |  |  |  |
| 100 | `DX.TX.MESSAGE` | `DxTransaction_Message` |  |  |  |
| 101 | `DX.TX.MESSAGE.MAP` | `DxTransaction_MessageMap` |  |  |  |
| 102 | `DX.TX.MESSAGE.DATE` | `DxTransaction_MessageDate` |  |  |  |
| 103 | `DX.TX.MESSAGE.REF` | `DxTransaction_MessageRef` |  |  |  |
| 104 | `DX.TX.REVAL.KEY` | `DxTransaction_RevalKey` | TField |  | Holds the DX Revalue key. Validation Rules: Up to 35 characters |
| 105 | `DX.TX.PREV.REVAL.KEY` | `DxTransaction_PrevRevalKey` | TField |  | Holds the DX Revalue key. |
| 106 | `DX.TX.PREV.VM.CCY` | `DxTransaction_PrevVmCcy` |  |  |  |
| 107 | `DX.TX.PREV.VM.ACC` | `DxTransaction_PrevVmAcc` |  |  |  |
| 108 | `DX.TX.PREV.VM` | `DxTransaction_PrevVm` |  |  |  |
| 109 | `DX.TX.PREV.VM.EXC` | `DxTransaction_PrevVmExc` |  |  |  |
| 110 | `DX.TX.PREV.VM.REF.CCY` | `DxTransaction_PrevVmRefCcy` | TField |  | Total of variation margin figures consolidated back to customer reference currency. Only updated byDX.RUN.REVALUE. Validation Rules: 19, Amt |
| 111 | `DX.TX.PREV.UNPL.CCY` | `DxTransaction_PrevUnplCcy` |  |  |  |
| 112 | `DX.TX.PREV.UNPL.ACC` | `DxTransaction_PrevUnplAcc` |  |  |  |
| 113 | `DX.TX.PREV.UNPL` | `DxTransaction_PrevUnpl` |  |  |  |
| 114 | `DX.TX.PREV.UNPL.REF.CCY` | `DxTransaction_PrevUnplRefCcy` | TField |  | Currency for unrealised option value. Multivalue set with PREV.UNPL. Only updated by DX.RUN.REVALUE. Validation Rules: 3, CCY Linked to CURRENCY |
| 115 | `DX.TX.PREV.IM.CCY` | `DxTransaction_PrevImCcy` |  |  |  |
| 116 | `DX.TX.PREV.IM.ACC` | `DxTransaction_PrevImAcc` |  |  |  |
| 117 | `DX.TX.PREV.IM` | `DxTransaction_PrevIm` |  |  |  |
| 118 | `DX.TX.PREV.IM.EXC` | `DxTransaction_PrevImExc` |  |  |  |
| 119 | `DX.TX.PREV.IM.REF.CCY` | `DxTransaction_PrevImRefCcy` | TField |  | Total of initial margin figures consilidated back to customer referency currency. Only updated by DX.RUN.REVALUE Validation Rules: 19, Amt |
| 120 | `DX.TX.LIMIT.REFERENCE` | `DxTransaction_LimitReference` | TField |  | This is the identification code, known as the Limit Reference used in the LIMIT key and in LIMIT.PARAMETER todefine how a LIMIT is defaulted. |
| 121 | `DX.TX.ORIG.LIMIT.AMOUNT` | `DxTransaction_OrigLimitAmount` | TField |  | Limit amount originally available against this limit, see LIMIT.REFERENCE No Input Field - defaulted from LIMIT |
| 122 | `DX.TX.TRADE.CCY` | `DxTransaction_TradeCcy` | TField |  | The trade currency updated by DX.TRADE Validation Rules: 3 Alpha |
| 123 | `DX.TX.CONTRACT.SIZE` | `DxTransaction_ContractSize` | TField |  | Number of units of measure per trading lot. Updated by DX.TRADE Validation Rules: 17, Alpha |
| 124 | `DX.TX.PREM.POST.TXN` | `DxTransaction_PremPostTxn` |  |  |  |
| 125 | `DX.TX.PREM.POST.AMT` | `DxTransaction_PremPostAmt` |  |  |  |
| 126 | `DX.TX.CURRENCY.MARKET` | `DxTransaction_CurrencyMarket` | TField |  | Currency market. Updated by DX.TRADE Validation Rules: 1 Numeric Linked to CURRENCY |
| 127 | `DX.TX.POSITION.TYPE` | `DxTransaction_PositionType` | TField |  | Position type. Updated by DX.TRADE Validation Rules: 2, Alpha |
| 128 | `DX.TX.PRIMARY.TXN` | `DxTransaction_PrimaryTxn` | TField |  | Was this transaction created from the primary side of the trade. Validation Rules: 3, Alpha YES_NO |
| 129 | `DX.TX.SOURCE.ID` | `DxTransaction_SourceId` | TField |  | ID of source transaction. Define concat field based on this field Validation Rules: 35,A |
| 130 | `DX.TX.ONL.TXN.LINK` | `DxTransaction_OnlTxnLink` | TField |  | Links revaluation DX.TRANSACTION records to the original 'online' DX.TRANSACTION record No Input Field - system generated |
| 131 | `DX.TX.EST.IM.CCY` | `DxTransaction_EstImCcy` |  |  |  |
| 132 | `DX.TX.EST.IM` | `DxTransaction_EstIm` |  |  |  |
| 133 | `DX.TX.EST.IM.ACCT` | `DxTransaction_EstImAcct` |  |  |  |
| 134 | `DX.TX.SC.BLOCK.INFO` | `DxTransaction_ScBlockInfo` |  |  |  |
| 135 | `DX.TX.SC.BLOCKAMT` | `DxTransaction_ScBlockamt` |  |  |  |
| 136 | `DX.TX.PRI.PREM.EXC` | `DxTransaction_PriPremExc` |  |  |  |
| 137 | `DX.TX.BASE.LOTS` | `DxTransaction_BaseLots` | TField |  | The number of lots traded prior to any closeout or corporate action taking place. |
| 138 | `DX.TX.ORIGINAL.PRICE` | `DxTransaction_OriginalPrice` | TField |  | This field holds the Price of DX. TRADE prevailing before Corporate action happens for the first time Validation Rules: No input field |
| 139 | `DX.TX.CPARTY.PRICE` | `DxTransaction_CpartyPrice` | TField |  | Represents the price for the number of lots traded. |
| 140 | `DX.TX.CPARTY.IPRICE` | `DxTransaction_CpartyIprice` | TField |  | Represents the price in T24 internal format. |
| 141 | `DX.TX.FAR.CO.PV.DATE` | `DxTransaction_FarCoPvDate` | TField |  | Not in use. |
| 142 | `DX.TX.PREM.VAL.DATE` | `DxTransaction_PremValDate` | TField |  | It represents the trade date. In case of closeout it holds the transaction date. |
| 143 | `DX.TX.LOCAL.REF` | `DxTransaction_LocalRef` |  |  |  |
| 144 | `DX.TX.NET.COST` | `DxTransaction_NetCost` | TField |  | This is the total cost of the DX .TRADE expressed in trade currency equivalent. The total cost is ideally equal to (Lots * Int. Price) +/- (Commissions and Charges) Validation Rules: No input field |
| 145 | `DX.TX.OPTION.TYPE` | `DxTransaction_OptionType` |  |  |  |
| 146 | `DX.TX.USR.FLD.NAME` | `DxTransaction_UsrFldName` |  |  |  |
| 147 | `DX.TX.USR.FLD.VAL` | `DxTransaction_UsrFldVal` |  |  |  |
| 148 | `DX.TX.USR.FLD.TEXT` | `DxTransaction_UsrFldText` |  |  |  |
| 149 | `DX.TX.USR.FLD.PRICE` | `DxTransaction_UsrFldPrice` |  |  |  |
| 150 | `DX.TX.DAYS.PER.YEAR` | `DxTransaction_DaysPerYear` | TField |  | Holds a valid record id of INTEREST.DAY.BASIS. |
| 151 | `DX.TX.SPREAD.RATE` | `DxTransaction_SpreadRate` | TField |  | This is the rate to be added to or subtracted from the reference rate. |
| 152 | `DX.TX.SWAP.REFERENCE` | `DxTransaction_SwapReference` | TField |  | Holds a valid Reference ID. |
| 153 | `DX.TX.CAP.FLOOR` | `DxTransaction_CapFloor` | TField |  | Denotes whether the underlying is a CAP or FLOOR. |
| 154 | `DX.TX.HEDGE.PL.CATEG` | `DxTransaction_HedgePlCateg` | TField |  | It is a valid category code. |
| 155 | `DX.TX.BUY.FLOATING.RATE` | `DxTransaction_BuyFloatingRate` | TField |  | This is the sequence number of the Periodic Interest Table for Buy floating rate. The format is XXYYY where XX is the sequence no and YYY is the currency. |
| 156 | `DX.TX.SELL.FLOATING.RATE` | `DxTransaction_SellFloatingRate` | TField |  | This is the sequence number of the Periodic Interest Table for a Sell floating rate. The format is XXYYY where XX is the sequence no and YYY is the currency. |
| 157 | `DX.TX.MASTER.AGREEMENT` | `DxTransaction_MasterAgreement` | TField |  | Not in use. |
| 158 | `DX.TX.PERIOD.FREQUENCY` | `DxTransaction_PeriodFrequency` | TField |  | Not in use. |
| 159 | `DX.TX.PERIOD.START` | `DxTransaction_PeriodStart` |  |  |  |
| 160 | `DX.TX.PERIOD.END.DATE` | `DxTransaction_PeriodEndDate` |  |  |  |
| 161 | `DX.TX.PERIOD.FIX.DATE` | `DxTransaction_PeriodFixDate` |  |  |  |
| 162 | `DX.TX.PERIOD.PAY.DATE` | `DxTransaction_PeriodPayDate` |  |  |  |
| 163 | `DX.TX.PREM.PYMT.FREQ` | `DxTransaction_PremPymtFreq` | TField |  | Represents the frequency in which the premium payment is to be made. |
| 164 | `DX.TX.PREM.PYMT.DATE` | `DxTransaction_PremPymtDate` |  |  |  |
| 165 | `DX.TX.PREM.PYMT.AMT` | `DxTransaction_PremPymtAmt` |  |  |  |
| 166 | `DX.TX.LOTS.TRANSFER` | `DxTransaction_LotsTransfer` | TField |  | Specifies the number of lots to be transferred. |
| 167 | `DX.TX.DEST.CUST` | `DxTransaction_DestCust` | TField |  | Specifies the external recipient customer reference number Validation Rules: No input field Upto 10 numeric values Must be a valid record in CUSTOMER application |
| 168 | `DX.TX.DEST.PORTFOLIO` | `DxTransaction_DestPortfolio` | TField |  | Specifies the external recipient customer portfolio reference if any Validation Rules: No input field Upto 18 alphanumeric values |
| 169 | `DX.TX.DEST.CUST.PORT` | `DxTransaction_DestCustPort` | TField |  | Specifies the recipient customer or portfolio. Should be valid record in CUSTOMER. |
| 170 | `DX.TX.CUST.CPARTY` | `DxTransaction_CustCparty` | TField |  | Specifies the receiver counterparty. Should be valid record in CUSTOMER. |
| 171 | `DX.TX.CUST.BNK.NME` | `DxTransaction_CustBnkNme` | TField |  | Specifies the receiver bank name. |
| 172 | `DX.TX.CUST.BNK.ADD` | `DxTransaction_CustBnkAdd` | TField |  | Specifies the receiver bank address. |
| 173 | `DX.TX.CUST.BNK.SORT.CDE` | `DxTransaction_CustBnkSortCde` | TField |  | Specifies the receiver bank sort code. |
| 174 | `DX.TX.PRICE.TRADED` | `DxTransaction_PriceTraded` | TField |  | Specifies the price at which the trade is being done Validation Rules: No input field Upto 19 numeric values |
| 175 | `DX.TX.FEE` | `DxTransaction_Fee` | TField |  | Set to YES if fee is required else set to NO Validation Rules: No input field Upto 3 alphanumeric values Valid inputs are either YES or NO |
| 176 | `DX.TX.ADVICE` | `DxTransaction_Advice` | TField |  | Set to YES if a transfer advice is to be produced else set to NO Validation Rules: No input field Upto 3 alphanumeric values Valid inputs are either YES or NO |
| 177 | `DX.TX.EXOTIC.EVENT` | `DxTransaction_ExoticEvent` |  |  |  |
| 178 | `DX.TX.CREATE.TRADES` | `DxTransaction_CreateTrades` | TField |  | Not in use. |
| 179 | `DX.TX.FILLED.LOTS` | `DxTransaction_FilledLots` |  |  |  |
| 180 | `DX.TX.FILLED.PRICE` | `DxTransaction_FilledPrice` |  |  |  |
| 181 | `DX.TX.FILLED.IPRICE` | `DxTransaction_FilledIprice` |  |  |  |
| 182 | `DX.TX.RESERVED.X1` | `DxTransaction_ReservedX1` |  |  |  |
| 183 | `DX.TX.NS.FWD.TXN` | `DxTransaction_NsFwdTxn` |  |  |  |
| 184 | `DX.TX.XO.AMT` | `DxTransaction_XoAmt` |  |  |  |
| 185 | `DX.TX.XO.CCY` | `DxTransaction_XoCcy` |  |  |  |
| 186 | `DX.TX.XO.ACCOUNT` | `DxTransaction_XoAccount` |  |  |  |
| 187 | `DX.TX.XO.ACC.CCY` | `DxTransaction_XoAccCcy` |  |  |  |
| 188 | `DX.TX.XO.ACC.AMT` | `DxTransaction_XoAccAmt` |  |  |  |
| 189 | `DX.TX.XO.EX.RATE` | `DxTransaction_XoExRate` |  |  |  |
| 190 | `DX.TX.XO.ACC.V.DATE` | `DxTransaction_XoAccVDate` |  |  |  |
| 191 | `DX.TX.XO.DATE` | `DxTransaction_XoDate` |  |  |  |
| 192 | `DX.TX.XO.POSTED` | `DxTransaction_XoPosted` |  |  |  |
| 193 | `DX.TX.RV.LINK` | `DxTransaction_RvLink` | TField |  | Should be a valid record in DX.REVALUE.SUMMARY. |
| 194 | `DX.TX.REGION` | `DxTransaction_Region` | TField |  | Regions are used to represent exchanges for the purpose of defining trading calendars in the HOLIDAY application. |
| 195 | `DX.TX.TAX.CODE` | `DxTransaction_TaxCode` |  |  |  |
| 196 | `DX.TX.TAX.TYPE` | `DxTransaction_TaxType` |  |  |  |
| 197 | `DX.TX.TAX.AMT.ACY` | `DxTransaction_TaxAmtAcy` |  |  |  |
| 198 | `DX.TX.TAX.AMT.TCY` | `DxTransaction_TaxAmtTcy` |  |  |  |
| 199 | `DX.TX.RESERVED.X2` | `DxTransaction_ReservedX2` |  |  |  |
| 200 | `DX.TX.EXOTIC.DATE` | `DxTransaction_ExoticDate` |  |  |  |
| 201 | `DX.TX.EXOTIC.TIME` | `DxTransaction_ExoticTime` |  |  |  |
| 202 | `DX.TX.VM.LCY.AMOUNT` | `DxTransaction_VmLcyAmount` | TField |  | Holds Current Variation Margin Amount in Local Currency |
| 203 | `DX.TX.DELIVERY.CCY` | `DxTransaction_DeliveryCcy` | TField |  | Specifies the delivery currency updated by DX.TRADE. Validation Rule: 3 Alpha |
| 204 | `DX.TX.OPTION.STYLE` | `DxTransaction_OptionStyle` | TField |  | Specifies the option style updated from DX.TRADE Validation Rules: Permitted options are AMERICAN,EUROPEAN and CARRIBEAN up to 10 characters. |
| 205 | `DX.TX.AS.CURRENCY` | `DxTransaction_AsCurrency` | TField |  |  |
| 206 | `DX.TX.AS.PRINCIPAL` | `DxTransaction_AsPrincipal` | TField |  |  |
| 207 | `DX.TX.LB.CURRENCY` | `DxTransaction_LbCurrency` | TField |  |  |
| 208 | `DX.TX.LB.PRINCIPAL` | `DxTransaction_LbPrincipal` | TField |  |  |
| 209 | `DX.TX.XO.EXOTIC.TYPE` | `DxTransaction_XoExoticType` |  |  |  |
| 210 | `DX.TX.NOTIONAL.TRADE.CCY` | `DxTransaction_NotionalTradeCcy` | TField |  |  |
| 211 | `DX.TX.NOTIONAL.DLV.CCY` | `DxTransaction_NotionalDlvCcy` | TField |  |  |
| 212 | `DX.TX.SY.TRANS.ID` | `DxTransaction_SyTransId` | TField |  |  |
| 213 | `DX.TX.CASH.PAYOUT.ACC` | `DxTransaction_CashPayoutAcc` | TField |  | Holds the settlement account provided at trade level. |
| 214 | `DX.TX.CASH.PAYOUT.CCY` | `DxTransaction_CashPayoutCcy` | TField |  | Holds the currency of the settlement account updated to CASH.PAYOUT.ACC. |
| 215 | `DX.TX.CASH.PAYOUT.AMT` | `DxTransaction_CashPayoutAmt` | TField |  | The payout amount to be paid / received from customer in the CASH.PAYOUT.CCY. |
| 216 | `DX.TX.FX.PAYOUT.CCY` | `DxTransaction_FxPayoutCcy` | TField |  | The FX.PAYOUT.CCY in trade is mapped. |
| 217 | `DX.TX.STRIKE.QUOTE.CCY` | `DxTransaction_StrikeQuoteCcy` | TField |  | Holds the STRIKE.QUOTE.CCY given at trade level. |
| 218 | `DX.TX.STRIKE.QUOTE` | `DxTransaction_StrikeQuote` | TField |  | Holds the STRIKE.QUOTE given at trad level. |
| 219 | `DX.TX.SY.DX.REFERENCE` | `DxTransaction_SyDxReference` | TField |  |  |
| 220 | `DX.TX.MTM.DATE` | `DxTransaction_MtmDate` | TField |  | Date on which the Mark-to-Market (MTM) is posted. |
| 221 | `DX.TX.MTM.CCY` | `DxTransaction_MtmCcy` | TField |  | Currency in which the MTM is posted. |
| 222 | `DX.TX.MTM.AMT` | `DxTransaction_MtmAmt` | TField |  | Mark-to-Market (MTM) amount posted in MTM.CCY on MTM.DATE. |
| 223 | `DX.TX.MTM.ACCOUNT` | `DxTransaction_MtmAccount` | TField |  | Account in which the Mark-to-Market (MTM) is posted. |
| 224 | `DX.TX.MTM.LCCY` | `DxTransaction_MtmLccy` | TField |  | MTM amount in local currency equivalent. |
| 225 | `DX.TX.MTM.LCCY.RATE` | `DxTransaction_MtmLccyRate` | TField |  | Exchange rate between account currency and local currency. |
| 226 | `DX.TX.PREV.MTM.DATE` | `DxTransaction_PrevMtmDate` | TField |  | The previously posted Mark-to-Market (MTM) date |
| 227 | `DX.TX.PREV.MTM.CCY` | `DxTransaction_PrevMtmCcy` | TField |  | The previously posted Mark-to-Market (MTM) account currency. |
| 228 | `DX.TX.PREV.MTM.AMT` | `DxTransaction_PrevMtmAmt` | TField |  | The previously posted Mark-to-Market (MTM) amount. |
| 229 | `DX.TX.PREV.MTM.ACCOUNT` | `DxTransaction_PrevMtmAccount` | TField |  | The previously posted Mark-to-Market (MTM) account. |
| 230 | `DX.TX.PREV.MTM.LCCY` | `DxTransaction_PrevMtmLccy` | TField |  | The previously posted Mark-to-Market (MTM) amount in local currency. |
| 231 | `DX.TX.PREV.MTM.LCCY.RATE` | `DxTransaction_PrevMtmLccyRate` | TField |  | Exchange rate between account currency and local currency for the previously posted MTM. |
| 232 | `DX.TX.MTM.TERMINATED` | `DxTransaction_MtmTerminated` | TField |  | Flag indicator to reverse the MTM amount on reversal or closeout of the contract. |
| 233 | `DX.TX.FTT.TYPE` | `DxTransaction_FttType` | TField |  | Tax type considered for tax posting. |
| 234 | `DX.TX.FTT.TAX.CODE` | `DxTransaction_FttTaxCode` | TField |  | Tax code defined at TAX.TYPE.CONDITION for the tax calculation. |
| 235 | `DX.TX.FTT.PERC` | `DxTransaction_FttPerc` | TField |  | Percentage of tax that is applied on tax base amount. |
| 236 | `DX.TX.FTT.BSE.AMT` | `DxTransaction_FttBseAmt` | TField |  | Tax base amount in terms of EUR currrency on which the tax percentage is applied. |
| 237 | `DX.TX.FTT.BSE.CCY` | `DxTransaction_FttBseCcy` | TField |  |  |
| 238 | `DX.TX.FTT.AMT.BCY` | `DxTransaction_FttAmtBcy` | TField |  |  |
| 239 | `DX.TX.FTT.CCY.TCY.RATE` | `DxTransaction_FttCcyTcyRate` | TField |  |  |
| 240 | `DX.TX.FTT.AMT.TCY` | `DxTransaction_FttAmtTcy` | TField |  | Tax amount in account currency of the transaction. |
| 241 | `DX.TX.FTT.AMT.LCY` | `DxTransaction_FttAmtLcy` | TField |  | Tax amount in local currency. |
| 242 | `DX.TX.FTT.AMT.CCY` | `DxTransaction_FttAmtCcy` | TField |  | Tax currency which is EUR. |
| 243 | `DX.TX.FTT.AMT` | `DxTransaction_FttAmt` | TField |  | Tax amount in EUR. |
| 244 | `DX.TX.FTT.EX.RATE` | `DxTransaction_FttExRate` | TField |  | Exchange rate between trade currency and local currency. |
| 245 | `DX.TX.LOTS.IN.TRADE.CCY` | `DxTransaction_LotsInTradeCcy` | TField |  | Lots in terms of trade currency of the transaction. |
| 246 | `DX.TX.CONTRACT.TERMS` | `DxTransaction_ContractTerms` | TField |  |  |
| 247 | `DX.TX.SETTLEMENT.METHOD` | `DxTransaction_SettlementMethod` | TField |  | The settlement mode of the option contract is specified in this field. The option can be physically settled (Delivery/Receipt of the underlying takes place )or Cash settled (The cash difference is settled). Possible values are PHYSICAL or CASH. NULL value would by default use physical settlement. |
| 248 | `DX.TX.BASKET.TYPE` | `DxTransaction_BasketType` | TField |  | Indicates the type of basket. EQUITY OR CURRENCY |
| 249 | `DX.TX.ULYING.ASSET.CLASS` | `DxTransaction_UlyingAssetClass` | TField |  | Indicates whether the underlying is security or currency basket. |
| 250 | `DX.TX.STATIC.LEG` | `DxTransaction_StaticLeg` | TField |  | Choose the type of option from the drop down menu 'CALL' or 'PUT'. CALL: Call currency should be same in all multi-value pairs. PUT: Put currency should be same in all multi-value pairs. |
| 251 | `DX.TX.ULYING.SECURITY` | `DxTransaction_UlyingSecurity` |  |  |  |
| 252 | `DX.TX.CALL.CCY` | `DxTransaction_CallCcy` |  |  |  |
| 253 | `DX.TX.PUT.CCY` | `DxTransaction_PutCcy` |  |  |  |
| 254 | `DX.TX.WEIGHT` | `DxTransaction_Weight` |  |  |  |
| 255 | `DX.TX.SPOT.PRICE` | `DxTransaction_SpotPrice` |  |  |  |
| 256 | `DX.TX.STRIKE.PERCENTAGE` | `DxTransaction_StrikePercentage` |  |  |  |
| 257 | `DX.TX.ULYING.STRIKE.CCY` | `DxTransaction_UlyingStrikeCcy` |  |  |  |
| 258 | `DX.TX.ULYING.STRIKE.PRICE` | `DxTransaction_UlyingStrikePrice` |  |  |  |
| 259 | `DX.TX.EXERCISE` | `DxTransaction_Exercise` |  |  |  |
| 260 | `DX.TX.QUANTITY` | `DxTransaction_Quantity` |  |  |  |
| 261 | `DX.TX.CALL.AMOUNT` | `DxTransaction_CallAmount` |  |  |  |
| 262 | `DX.TX.PUT.AMOUNT` | `DxTransaction_PutAmount` |  |  |  |
| 263 | `DX.TX.CASH.EXERCISE` | `DxTransaction_CashExercise` | TField |  | Used for generating cash payouts. |
| 264 | `DX.TX.CASH.AMOUNT` | `DxTransaction_CashAmount` | TField |  | Holds the cash amount that needs to be paid out for a cash settled option. |
| 265 | `DX.TX.CASH.CCY` | `DxTransaction_CashCcy` | TField |  | Holds the currency corresponding to the CASH.AMOUNT field. |
| 266 | `DX.TX.SETTLEMENT.AMT` | `DxTransaction_SettlementAmt` | TField |  | Holds the cash payout amount calculated in settlement account currency. i.e in the SETTLEMENT.CCY field. |
| 267 | `DX.TX.CLOSEOUT.TXN.AMT` | `DxTransaction_CloseoutTxnAmt` | TField |  | Holds the settlement amount for physically settled contracts |
| 268 | `DX.TX.SYS.FEE.TAX.AMT` | `DxTransaction_SysFeeTaxAmt` |  |  |  |
| 269 | `DX.TX.OBSERVATION.DATE` | `DxTransaction_ObservationDate` |  |  |  |
| 270 | `DX.TX.OBSERVED.SPOT.RATE` | `DxTransaction_ObservedSpotRate` |  |  |  |
| 271 | `DX.TX.PARTICIPATION.RATE` | `DxTransaction_ParticipationRate` | TField |  | This fields hold the rate which is used to calculate the final pay out of the option. |
| 272 | `DX.TX.TRD.DELTA` | `DxTransaction_TrdDelta` | TField |  | This field is used to store the trade date delta. |
| 273 | `DX.TX.UNDLYING.MAT.DATE` | `DxTransaction_UndlyingMatDate` | TField |  |  |
| 274 | `DX.TX.AUTO.EXPIRY.DATE` | `DxTransaction_AutoExpiryDate` | TField |  |  |
| 275 | `DX.TX.PARENT.CHILD.REF` | `DxTransaction_ParentChildRef` | TField |  |  |
