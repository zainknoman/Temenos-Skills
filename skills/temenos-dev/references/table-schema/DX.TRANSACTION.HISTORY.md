# DX.TRANSACTION.HISTORY — Table Schema

> Source: `INSERTS/I_F.DX.TRANSACTION.HISTORY` in `DX_Trade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.TXH.PORT.CUST.ID` | `DxTransactionHistory_PortCustId` | TField |  | Portfolio or customer id for this transaction. Validation Rules: Must be a valid record on DX.CUSTOMER or SEC.ACC.MASTER |
| 2 | `DX.TXH.TRANS.DATE` | `DxTransactionHistory_TransDate` | TField |  | Actual date of transaction update. Validation Rules: Up to 11 characters in DATE format |
| 3 | `DX.TXH.REVERSAL.DATE` | `DxTransactionHistory_ReversalDate` | TField |  | Date of reversal of source application record, or replacement with newer version. Validation Rules: Up to 11 characters in DATE format Null unless parent transaction is reversed or adjusted |
| 4 | `DX.TXH.REVERSAL.TIME` | `DxTransactionHistory_ReversalTime` | TField |  | System time stamp on reversal or amendment of parent transaction. Validation Rules: Up to 5 character in TIME format Null unless parent transaction is reversed or adjusted |
| 5 | `DX.TXH.SOURCE.REF` | `DxTransactionHistory_SourceRef` | TField |  | ID of Source transaction. Validation Rules: 35 Alpha |
| 6 | `DX.TXH.CONTRACT.CODE` | `DxTransactionHistory_ContractCode` | TField |  | Contract code associated with this transaction. Validation Rules: Up to 12 characters, input must be a valid record on the DX.CONTRACT.MASTER Application |
| 7 | `DX.TXH.EXCHANGE.CODE` | `DxTransactionHistory_ExchangeCode` | TField |  | The name of the Exchange where the applicable contract is traded. |
| 8 | `DX.TXH.TRADE.DATE` | `DxTransactionHistory_TradeDate` | TField |  | The date in which the transaction is performed. |
| 9 | `DX.TXH.MATURITY.DATE` | `DxTransactionHistory_MaturityDate` | TField |  | The delivery period or prompt date of the contract transacted. |
| 10 | `DX.TXH.ACCOUNT` | `DxTransactionHistory_Account` | TField |  | Identifies the account, over which financial entries relating to the transaction are to be passed. |
| 11 | `DX.TXH.EVENT.TYPE` | `DxTransactionHistory_EventType` |  |  |  |
| 12 | `DX.TXH.LAST.REP.POS` | `DxTransactionHistory_LastRepPos` | TField |  | Holds the id of DX.REP.POS.LAST. This links to the last time that position was updated. |
| 13 | `DX.TXH.TRANS.NAME` | `DxTransactionHistory_TransName` | TField |  | The TRANS.NAME is different depending on the application e.g. DX.TRADE-FUTURE_OPTION Validation Rules: Up to 10 characters |
| 14 | `DX.TXH.BUY.SELL` | `DxTransactionHistory_BuySell` | TField |  | Contract buy or sell flag BUY_SELL updated by DX.TRADE. Validation Rules: Up to 4 characters, input must be either BUY/SELL |
| 15 | `DX.TXH.CALL.PUT` | `DxTransactionHistory_CallPut` | TField |  | Option contract call or put flag. CALL_PUT. Updated by DX.TRADE. Validation Rules: Up to 4 characters, input must be either CALL/PUT |
| 16 | `DX.TXH.LOTS` | `DxTransactionHistory_Lots` | TField |  | Number of active lots remaining on transaction. Validation Rules: Up to 19 characters |
| 17 | `DX.TXH.ORIGINAL.LOTS` | `DxTransactionHistory_OriginalLots` | TField |  | Original number of lots for this transaction. Validation Rules: Up to 19 characters |
| 18 | `DX.TXH.PRICE` | `DxTransactionHistory_Price` | TField |  | Price/Premium as input, with number of decimal places standardised to price d.p.'s Validation Rules: Up to 19 characters |
| 19 | `DX.TXH.INT.PRICE` | `DxTransactionHistory_IntPrice` | TField |  | Internal format trade price/premium for this transaction. Trade ccy. Premium for trades. Quoted as standard T24internal price. Validation Rules: Up to 19 characters |
| 20 | `DX.TXH.PRICE.OUTPUT` | `DxTransactionHistory_PriceOutput` | TField |  | Not in use. |
| 21 | `DX.TXH.STRIKE` | `DxTransactionHistory_Strike` | TField |  | Strike price as input, with number of decimal places standardised to price d.p's. Only for OPTIONs. Required incase input strike needs to be sent to third party application. Validation Rules: Up to 19 characters |
| 22 | `DX.TXH.INT.STRIKE` | `DxTransactionHistory_IntStrike` | TField |  | Internal format strike price for option transaction. Only updated by DX.TRADE when trade type is OPTIONs. Held inthe standard internal T24 Format. Validation Rules: Up to 19 characters |
| 23 | `DX.TXH.STRIKE.OUTPUT` | `DxTransactionHistory_StrikeOutput` | TField |  | Not in use. |
| 24 | `DX.TXH.TRANS.TIME` | `DxTransactionHistory_TransTime` | TField |  | Time of transaction update. Validation Rules: Up to 5 characters in TIME format |
| 25 | `DX.TXH.SUB.ASSET.TYPE` | `DxTransactionHistory_SubAssetType` | TField |  | Sub asset type of contract traded. Updated by DX.TRADE Validation Rules: Linked to SUB.ASSET.TYPE 5 Alpha |
| 26 | `DX.TXH.DEC.DATE` | `DxTransactionHistory_DecDate` | TField | Yes | The Last Date by which a customer may exercise an option. The exercise date (European Options) or last exercisedate (American Options) for this contract. This field will default to date calculated from Date formula for Dec.Date on DX.CONTRACT.MASTER, but this can beoverriden as required. Validation Rules: Up to 9 type D date format characters. Mandatory Input if CONTRACT.TYPE is OPTION |
| 27 | `DX.TXH.PENDING.DIARY` | `DxTransactionHistory_PendingDiary` | TField |  | Should be a valid record in DX.DIARY. |
| 28 | `DX.TXH.ENTITLEMENT` | `DxTransactionHistory_Entitlement` |  |  |  |
| 29 | `DX.TXH.PREM.OFFSET` | `DxTransactionHistory_PremOffset` | TField |  | Represents the premium payment offset for this transaction. No of days offset from charging to account posting for premiums for the customer. |
| 30 | `DX.TXH.LAST.REVAL.LOTS` | `DxTransactionHistory_LastRevalLots` | TField |  | Number of lots active on this transaction at last reval time. Validation Rules: 19 Numeric |
| 31 | `DX.TXH.LOTS.SETTLED` | `DxTransactionHistory_LotsSettled` | TField |  | Number of lots settled in this transaction. Only updated by DX.CO.PROCESS. Validation Rules: Up to 19 characters |
| 32 | `DX.TXH.SETT.VAL.ACC.CCY` | `DxTransactionHistory_SettValAccCcy` | TField |  | Settlement value (P&amp;L) generated in account currency. Only updated by DX.CO.PROCESS Validation Rules: 19 Numeric |
| 33 | `DX.TXH.SETT.VAL.REF.CCY` | `DxTransactionHistory_SettValRefCcy` | TField |  | Settlement value (P&amp;L) generated in reference currency. Only updated by DX.CO.PROCESS Validation Rules: Up to 19 characters |
| 34 | `DX.TXH.LOTS.ACTIONED` | `DxTransactionHistory_LotsActioned` | TField |  | The total number of lots being closed out by this closeout. Updated by DX.CO.PROCESS. |
| 35 | `DX.TXH.RESULTING.TRADE` | `DxTransactionHistory_ResultingTrade` | TField |  | Not in use. |
| 36 | `DX.TXH.INIT.MAR.CCY` | `DxTransactionHistory_InitMarCcy` |  |  |  |
| 37 | `DX.TXH.INIT.ACCOUNT` | `DxTransactionHistory_InitAccount` |  |  |  |
| 38 | `DX.TXH.INITIAL.MARGIN` | `DxTransactionHistory_InitialMargin` |  |  |  |
| 39 | `DX.TXH.IM.EXC.RATE` | `DxTransactionHistory_ImExcRate` |  |  |  |
| 40 | `DX.TXH.INIT.MAR.REF.CCY` | `DxTransactionHistory_InitMarRefCcy` | TField |  | Total of initial margin figures consolidated back to customer reference currency. Only updated by DX.RUN.REVALUE. Validation Rules: Up to 19 characters |
| 41 | `DX.TXH.VAR.MAR.CCY` | `DxTransactionHistory_VarMarCcy` |  |  |  |
| 42 | `DX.TXH.VAR.ACCOUNT` | `DxTransactionHistory_VarAccount` |  |  |  |
| 43 | `DX.TXH.VAR.MARGIN` | `DxTransactionHistory_VarMargin` |  |  |  |
| 44 | `DX.TXH.VM.EXC.RATE` | `DxTransactionHistory_VmExcRate` |  |  |  |
| 45 | `DX.TXH.VAR.MAR.REF.CCY` | `DxTransactionHistory_VarMarRefCcy` | TField |  | Total of variation margin figures consolidated back to customer reference currency. Only updated byDX.RUN.REVALUE. Validation Rules: Up to 19 characters |
| 46 | `DX.TXH.APP.STATUS` | `DxTransactionHistory_AppStatus` | TField |  | Is this transaction authorised Validation Rules: Up to 4 characters |
| 47 | `DX.TXH.STRATEGY` | `DxTransactionHistory_Strategy` | TField |  | Its value is populated from DX.STRATEGY. A different strategy can be used for each side of the trade in the PRI.STRATEGY and SEC.STRATEGY fields. When transactions with a strategy are found as part of the revaluation process, the corresponding trades arevalued together using the margin routine, if specified, in the DX.STRATEGY record. It is used for reporting purposes. |
| 48 | `DX.TXH.CUST.TYPE` | `DxTransactionHistory_CustType` | TField |  | Customer type. Initally updated by DX.TRADE Validation Rules: Up to 15 characters |
| 49 | `DX.TXH.CUST.STATUS` | `DxTransactionHistory_CustStatus` | TField |  | Status of customer in terms of segregated/non-segregated business. Validation Rules: Up to 15 characters |
| 50 | `DX.TXH.TRASETTNOS` | `DxTransactionHistory_Trasettnos` |  |  |  |
| 51 | `DX.TXH.TRASETTLOTS` | `DxTransactionHistory_Trasettlots` |  |  |  |
| 52 | `DX.TXH.CO.DATE` | `DxTransactionHistory_CoDate` |  |  |  |
| 53 | `DX.TXH.CO.PV.DATE` | `DxTransactionHistory_CoPvDate` |  |  |  |
| 54 | `DX.TXH.CO.TYPE` | `DxTransactionHistory_CoType` |  |  |  |
| 55 | `DX.TXH.CO.STMT.NOS` | `DxTransactionHistory_CoStmtNos` |  |  |  |
| 56 | `DX.TXH.OPEN.CLOSE` | `DxTransactionHistory_OpenClose` | TField |  | Valid values are OPEN and CLOSE. This specifies the open or close status of the transaction. This is used in the new average price method OPENING. |
| 57 | `DX.TXH.HEDGE.TRADE` | `DxTransactionHistory_HedgeTrade` | TField |  | Is this a hedge or speculative trade transaction. Validation Rules: Up to 15 characters, input must be HEDGE/TRADE |
| 58 | `DX.TXH.LINK` | `DxTransactionHistory_Link` |  |  |  |
| 59 | `DX.TXH.ALLOW.SETT` | `DxTransactionHistory_AllowSett` | TField |  | Are close-outs allowed for the leg of the trrade represented by the transaction record. Validation Rules: Up to 3 characters, input must be either: YES/NO |
| 60 | `DX.TXH.COMM.TYP` | `DxTransactionHistory_CommTyp` |  |  |  |
| 61 | `DX.TXH.COMM.CDE` | `DxTransactionHistory_CommCde` |  |  |  |
| 62 | `DX.TXH.COMM.CCY` | `DxTransactionHistory_CommCcy` |  |  |  |
| 63 | `DX.TXH.COMM.AMT` | `DxTransactionHistory_CommAmt` |  |  |  |
| 64 | `DX.TXH.COMM.ACC` | `DxTransactionHistory_CommAcc` |  |  |  |
| 65 | `DX.TXH.CACC.CCY` | `DxTransactionHistory_CaccCcy` |  |  |  |
| 66 | `DX.TXH.COMM.EXC` | `DxTransactionHistory_CommExc` |  |  |  |
| 67 | `DX.TXH.CACC.AMT` | `DxTransactionHistory_CaccAmt` |  |  |  |
| 68 | `DX.TXH.COMM.TAX` | `DxTransactionHistory_CommTax` |  |  |  |
| 69 | `DX.TXH.CHARGE.DATE` | `DxTransactionHistory_ChargeDate` | TField |  | Date of application of commission/charges/premium. Updated by DX.TRADE. Validation Rules: Up to 10 characters, input must be either: TRADE/SETTLEMENT |
| 70 | `DX.TXH.REF.CCY` | `DxTransactionHistory_RefCcy` | TField |  | For revaluation this field represents the reference/reporting currency of the client. Validation Rules: Up to 3 characters in CCY format |
| 71 | `DX.TXH.ACC.CCY` | `DxTransactionHistory_AccCcy` | TField |  | Customer account currency Updated by DX.TRADE. Validation Rules: Up to 3 characters in CCY format |
| 72 | `DX.TXH.EX.RATE.REF` | `DxTransactionHistory_ExRateRef` | TField |  | Exchange rate between customer reference and trade currency. Updated by DX.TRADE Validation Rules: Up to 19 characters in AMT format |
| 73 | `DX.TXH.EX.RATE.ACC` | `DxTransactionHistory_ExRateAcc` | TField |  | Exchange rate between trade currency and customer accountcurrency. Updated by DX.TRADE. Validation Rules: Up to 19 characters in AMT format |
| 74 | `DX.TXH.OVE.ADDR` | `DxTransactionHistory_OveAddr` |  |  |  |
| 75 | `DX.TXH.MESS.CTL` | `DxTransactionHistory_MessCtl` |  |  |  |
| 76 | `DX.TXH.DLV.KEY` | `DxTransactionHistory_DlvKey` |  |  |  |
| 77 | `DX.TXH.ORDER.NO` | `DxTransactionHistory_OrderNo` |  |  |  |
| 78 | `DX.TXH.CUST.NARR` | `DxTransactionHistory_CustNarr` |  |  |  |
| 79 | `DX.TXH.CONSTRAINT` | `DxTransactionHistory_Constraint` | TField |  | Trading constraint ID. Updated by DX.TRADE. Validation Rules: Up to 17 characters, input must be a valid record on the DX.TRADING.CONSTRAINT |
| 80 | `DX.TXH.COUNTERPARTY` | `DxTransactionHistory_Counterparty` |  |  |  |
| 81 | `DX.TXH.CUSTOMER` | `DxTransactionHistory_Customer` | TField |  | Identifies the Customer with whom the trade is made. Its value should be a valid record in CUSTOMER application. |
| 82 | `DX.TXH.DEALER.DESK` | `DxTransactionHistory_DealerDesk` | TField |  | The DEALER id for this transaction. |
| 83 | `DX.TXH.DEPT.ACCT.OFFICER` | `DxTransactionHistory_DeptAcctOfficer` | TField |  | Holds the department or account officer ID. Should be a valid record in DEPT.ACCT.OFFICER. |
| 84 | `DX.TXH.OWN.BOOK` | `DxTransactionHistory_OwnBook` | TField |  | This field holds the own book portfolio to which this portfolio belongs. Identifies whether the transaction is a own book transaction or not. |
| 85 | `DX.TXH.PRODUCT.CAT` | `DxTransactionHistory_ProductCat` | TField |  | The product category. Validation Rules: Up to 6 characters, input must be a valid record on the CATEGORY Application |
| 86 | `DX.TXH.RV.UPDATE.ID` | `DxTransactionHistory_RvUpdateId` | TField |  | Holds the DX Revalue id. Validation Rules: Up to 35 characters |
| 87 | `DX.TXH.STATEMENT.NOS` | `DxTransactionHistory_StatementNos` |  |  |  |
| 88 | `DX.TXH.CHG.OFFSET` | `DxTransactionHistory_ChgOffset` | TField |  | Number of days charge off-set between earning and posting. Validation Rules: Up to 3 characters |
| 89 | `DX.TXH.CUST.REF` | `DxTransactionHistory_CustRef` | TField |  | Free text reference/narrative field mapped from either the PRI.CUS.REF or SEC.CUST.REF on the correspondingDX.TRADE. Up to 16 characters |
| 90 | `DX.TXH.UOPT.PANDL.CCY` | `DxTransactionHistory_UoptPandlCcy` |  |  |  |
| 91 | `DX.TXH.UOPT.ACCOUNT` | `DxTransactionHistory_UoptAccount` |  |  |  |
| 92 | `DX.TXH.UOPT.PANDL` | `DxTransactionHistory_UoptPandl` |  |  |  |
| 93 | `DX.TXH.UOPT.PANDL.REF.CCY` | `DxTransactionHistory_UoptPandlRefCcy` | TField |  | Total of variation margin figures consolidated back to customer reference currency. Only updated byDX.RUN.REVALUE. Validation Rules: Up to 19 characters |
| 94 | `DX.TXH.TRA.PND.SETT` | `DxTransactionHistory_TraPndSett` |  |  |  |
| 95 | `DX.TXH.TRA.PND.LOTS` | `DxTransactionHistory_TraPndLots` |  |  |  |
| 96 | `DX.TXH.TRA.PND.STMT` | `DxTransactionHistory_TraPndStmt` |  |  |  |
| 97 | `DX.TXH.ACTIVITY.CODE` | `DxTransactionHistory_ActivityCode` |  |  |  |
| 98 | `DX.TXH.ACTIVITY.DATE` | `DxTransactionHistory_ActivityDate` |  |  |  |
| 99 | `DX.TXH.ACT.EVENT.TYPE` | `DxTransactionHistory_ActEventType` |  |  |  |
| 100 | `DX.TXH.MESSAGE` | `DxTransactionHistory_Message` |  |  |  |
| 101 | `DX.TXH.MESSAGE.MAP` | `DxTransactionHistory_MessageMap` |  |  |  |
| 102 | `DX.TXH.MESSAGE.DATE` | `DxTransactionHistory_MessageDate` |  |  |  |
| 103 | `DX.TXH.MESSAGE.REF` | `DxTransactionHistory_MessageRef` |  |  |  |
| 104 | `DX.TXH.REVAL.KEY` | `DxTransactionHistory_RevalKey` | TField |  | Holds the DX Revalue key. |
| 105 | `DX.TXH.PREV.REVAL.KEY` | `DxTransactionHistory_PrevRevalKey` | TField |  | Holds the DX Revalue key. |
| 106 | `DX.TXH.PREV.VM.CCY` | `DxTransactionHistory_PrevVmCcy` |  |  |  |
| 107 | `DX.TXH.PREV.VM.ACC` | `DxTransactionHistory_PrevVmAcc` |  |  |  |
| 108 | `DX.TXH.PREV.VM` | `DxTransactionHistory_PrevVm` |  |  |  |
| 109 | `DX.TXH.PREV.VM.EXC` | `DxTransactionHistory_PrevVmExc` |  |  |  |
| 110 | `DX.TXH.PREV.VM.REF.CCY` | `DxTransactionHistory_PrevVmRefCcy` | TField |  | Total of variation margin figures consolidated back to customer reference currency. Only updated byDX.RUN.REVALUE. Validation Rules: 19, Amt |
| 111 | `DX.TXH.PREV.UNPL.CCY` | `DxTransactionHistory_PrevUnplCcy` |  |  |  |
| 112 | `DX.TXH.PREV.UNPL.ACC` | `DxTransactionHistory_PrevUnplAcc` |  |  |  |
| 113 | `DX.TXH.PREV.UNPL` | `DxTransactionHistory_PrevUnpl` |  |  |  |
| 114 | `DX.TXH.PREV.UNPL.REF.CCY` | `DxTransactionHistory_PrevUnplRefCcy` | TField |  | Currency for unrealised option value. Multivalue set with PREV.UNPL. Only updated by DX.RUN.REVALUE. Validation Rules: 3, CCY Linked to CURRENCY |
| 115 | `DX.TXH.PREV.IM.CCY` | `DxTransactionHistory_PrevImCcy` |  |  |  |
| 116 | `DX.TXH.PREV.IM.ACC` | `DxTransactionHistory_PrevImAcc` |  |  |  |
| 117 | `DX.TXH.PREV.IM` | `DxTransactionHistory_PrevIm` |  |  |  |
| 118 | `DX.TXH.PREV.IM.EXC` | `DxTransactionHistory_PrevImExc` |  |  |  |
| 119 | `DX.TXH.PREV.IM.REF.CCY` | `DxTransactionHistory_PrevImRefCcy` | TField |  | Total of initial margin figures consilidated back to customer referency currency. Only updated by DX.RUN.REVALUE Validation Rules: 19, Amt |
| 120 | `DX.TXH.LIMIT.REFERENCE` | `DxTransactionHistory_LimitReference` | TField |  | This is the identification code, known as the Limit Reference used in the LIMIT key and in LIMIT.PARAMETER todefine how a LIMIT is defaulted. |
| 121 | `DX.TXH.ORIG.LIMIT.AMOUNT` | `DxTransactionHistory_OrigLimitAmount` | TField |  | Limit amount originally available against this limit, see LIMIT.REFERENCE No Input Field - defaulted from LIMIT |
| 122 | `DX.TXH.TRADE.CCY` | `DxTransactionHistory_TradeCcy` | TField |  | The trade currency updated by DX.TRADE Validation Rules: 3 Alpha |
| 123 | `DX.TXH.CONTRACT.SIZE` | `DxTransactionHistory_ContractSize` | TField |  | Number of units of measure per trading lot. Updated by DX.TRADE Validation Rules: 17, Alpha |
| 124 | `DX.TXH.PREM.POST.TXN` | `DxTransactionHistory_PremPostTxn` |  |  |  |
| 125 | `DX.TXH.PREM.POST.AMT` | `DxTransactionHistory_PremPostAmt` |  |  |  |
| 126 | `DX.TXH.CURRENCY.MARKET` | `DxTransactionHistory_CurrencyMarket` | TField |  | Currency market. Updated by DX.TRADE Validation Rules: 1 Numeric Linked to CURRENCY |
| 127 | `DX.TXH.POSITION.TYPE` | `DxTransactionHistory_PositionType` | TField |  | Position type. Updated by DX.TRADE Validation Rules: 2, Alpha |
| 128 | `DX.TXH.PRIMARY.TXN` | `DxTransactionHistory_PrimaryTxn` | TField |  | Was this transaction created from the primary side of the trade. Validation Rules: 3, Alpha YES_NO |
| 129 | `DX.TXH.SOURCE.ID` | `DxTransactionHistory_SourceId` | TField |  | ID of source transaction. Define concat field based on this field Validation Rules: 35,A |
| 130 | `DX.TXH.ONL.TXN.LINK` | `DxTransactionHistory_OnlTxnLink` | TField |  | Links revaluation DX.TRANSACTION records to the original online DX.TRANSACTION record No Input Field - system generated |
| 131 | `DX.TXH.EST.IM.CCY` | `DxTransactionHistory_EstImCcy` |  |  |  |
| 132 | `DX.TXH.EST.IM` | `DxTransactionHistory_EstIm` |  |  |  |
| 133 | `DX.TXH.EST.IM.ACCT` | `DxTransactionHistory_EstImAcct` |  |  |  |
| 134 | `DX.TXH.SC.BLOCK.INFO` | `DxTransactionHistory_ScBlockInfo` |  |  |  |
| 135 | `DX.TXH.SC.BLOCKAMT` | `DxTransactionHistory_ScBlockamt` |  |  |  |
| 136 | `DX.TXH.PRI.PREM.EXC` | `DxTransactionHistory_PriPremExc` |  |  |  |
| 137 | `DX.TXH.BASE.LOTS` | `DxTransactionHistory_BaseLots` | TField |  | The number of lots traded prior to any closeout or corporate action taking place. |
| 138 | `DX.TXH.ORIGINAL.PRICE` | `DxTransactionHistory_OriginalPrice` | TField |  | This field holds the Price of DX. TRADE prevailing before Corporate action happens for the first time Validation Rules: No input field |
| 139 | `DX.TXH.CPARTY.PRICE` | `DxTransactionHistory_CpartyPrice` | TField |  | Represents the price for the number of lots traded. |
| 140 | `DX.TXH.CPARTY.IPRICE` | `DxTransactionHistory_CpartyIprice` | TField |  | Represents the price in T24 internal format. |
| 141 | `DX.TXH.FAR.CO.PV.DATE` | `DxTransactionHistory_FarCoPvDate` | TField |  | Not in use. |
| 142 | `DX.TXH.PREM.VAL.DATE` | `DxTransactionHistory_PremValDate` | TField |  | It represents the trade date. In case of closeout it holds the transaction date. |
| 143 | `DX.TXH.LOCAL.REF` | `DxTransactionHistory_LocalRef` |  |  |  |
| 144 | `DX.TXH.NET.COST` | `DxTransactionHistory_NetCost` | TField |  | This is the total cost of the DX .TRADE expressed in trade currency equivalent. The total cost is ideally equal to (Lots * Int. Price) +/- (Commissions and Charges) Validation Rules: No input field |
| 145 | `DX.TXH.OPTION.TYPE` | `DxTransactionHistory_OptionType` |  |  |  |
| 146 | `DX.TXH.USR.FLD.NAME` | `DxTransactionHistory_UsrFldName` |  |  |  |
| 147 | `DX.TXH.USR.FLD.VAL` | `DxTransactionHistory_UsrFldVal` |  |  |  |
| 148 | `DX.TXH.USR.FLD.TEXT` | `DxTransactionHistory_UsrFldText` |  |  |  |
| 149 | `DX.TXH.USR.FLD.PRICE` | `DxTransactionHistory_UsrFldPrice` |  |  |  |
| 150 | `DX.TXH.DAYS.PER.YEAR` | `DxTransactionHistory_DaysPerYear` | TField |  | Holds a valid record id of INTEREST.DAY.BASIS. |
| 151 | `DX.TXH.SPREAD.RATE` | `DxTransactionHistory_SpreadRate` | TField |  | This is the rate to be added to or subtracted from the reference rate. |
| 152 | `DX.TXH.SWAP.REFERENCE` | `DxTransactionHistory_SwapReference` | TField |  | Holds a valid Reference ID. |
| 153 | `DX.TXH.CAP.FLOOR` | `DxTransactionHistory_CapFloor` | TField |  | Denotes whether the underlying is a CAP or FLOOR. |
| 154 | `DX.TXH.HEDGE.PL.CATEG` | `DxTransactionHistory_HedgePlCateg` | TField |  | It is a valid category code. |
| 155 | `DX.TXH.BUY.FLOATING.RATE` | `DxTransactionHistory_BuyFloatingRate` | TField |  | This is the sequence number of the Periodic Interest Table for Buy floating rate. The format is XXYYY where XX isthe sequence no and YYY is the currency. |
| 156 | `DX.TXH.SELL.FLOATING.RATE` | `DxTransactionHistory_SellFloatingRate` | TField |  | This is the sequence number of the Periodic Interest Table for a Sell floating rate. The format is XXYYY where XXis the sequence no and YYY is the currency. |
| 157 | `DX.TXH.MASTER.AGREEMENT` | `DxTransactionHistory_MasterAgreement` | TField |  | Not in use. |
| 158 | `DX.TXH.PERIOD.FREQUENCY` | `DxTransactionHistory_PeriodFrequency` | TField |  | Not in use. |
| 159 | `DX.TXH.PERIOD.START` | `DxTransactionHistory_PeriodStart` |  |  |  |
| 160 | `DX.TXH.PERIOD.END.DATE` | `DxTransactionHistory_PeriodEndDate` |  |  |  |
| 161 | `DX.TXH.PERIOD.FIX.DATE` | `DxTransactionHistory_PeriodFixDate` |  |  |  |
| 162 | `DX.TXH.PERIOD.PAY.DATE` | `DxTransactionHistory_PeriodPayDate` |  |  |  |
| 163 | `DX.TXH.PREM.PYMT.FREQ` | `DxTransactionHistory_PremPymtFreq` | TField |  | Represents the frequency in which the premium payment is to be made. |
| 164 | `DX.TXH.PREM.PYMT.DATE` | `DxTransactionHistory_PremPymtDate` |  |  |  |
| 165 | `DX.TXH.PREM.PYMT.AMT` | `DxTransactionHistory_PremPymtAmt` |  |  |  |
| 166 | `DX.TXH.LOTS.TRANSFER` | `DxTransactionHistory_LotsTransfer` | TField |  | Specifies the number of lots to be transferred. |
| 167 | `DX.TXH.DEST.CUST` | `DxTransactionHistory_DestCust` | TField |  | Specifies the external recipient customer reference number Validation Rules: No input field Upto 10 numeric values Must be a valid record in CUSTOMER application |
| 168 | `DX.TXH.DEST.PORTFOLIO` | `DxTransactionHistory_DestPortfolio` | TField |  | Specifies the external recipient customer portfolio reference if any Validation Rules: No input field Upto 18 alphanumeric values |
| 169 | `DX.TXH.DEST.CUST.PORT` | `DxTransactionHistory_DestCustPort` | TField |  | Specifies the recipient customer or portfolio. Should be valid record in CUSTOMER. |
| 170 | `DX.TXH.CUST.CPARTY` | `DxTransactionHistory_CustCparty` | TField |  | Specifies the receiver counterparty. Should be valid record in CUSTOMER. |
| 171 | `DX.TXH.CUST.BNK.NME` | `DxTransactionHistory_CustBnkNme` | TField |  | Specifies the receiver bank name. |
| 172 | `DX.TXH.CUST.BNK.ADD` | `DxTransactionHistory_CustBnkAdd` | TField |  | Specifies the receiver bank address. |
| 173 | `DX.TXH.CUST.BNK.SORT.CDE` | `DxTransactionHistory_CustBnkSortCde` | TField |  | Specifies the receiver bank sort code. |
| 174 | `DX.TXH.PRICE.TRADED` | `DxTransactionHistory_PriceTraded` | TField |  | Specifies the price at which the trade is being done Validation Rules: No input field Upto 19 numeric values |
| 175 | `DX.TXH.FEE` | `DxTransactionHistory_Fee` | TField |  | Set to YES if fee is required else set to NO Validation Rules: No input field Upto 3 alphanumeric values Valid inputs are either YES or NO |
| 176 | `DX.TXH.ADVICE` | `DxTransactionHistory_Advice` | TField |  | Set to YES if a transfer advice is to be produced else set to NO Validation Rules: No input field Upto 3 alphanumeric values Valid inputs are either YES or NO |
| 177 | `DX.TXH.EXOTIC.EVENT` | `DxTransactionHistory_ExoticEvent` |  |  |  |
| 178 | `DX.TXH.CREATE.TRADES` | `DxTransactionHistory_CreateTrades` | TField |  | Not in use. |
| 179 | `DX.TXH.FILLED.LOTS` | `DxTransactionHistory_FilledLots` |  |  |  |
| 180 | `DX.TXH.FILLED.PRICE` | `DxTransactionHistory_FilledPrice` |  |  |  |
| 181 | `DX.TXH.FILLED.IPRICE` | `DxTransactionHistory_FilledIprice` |  |  |  |
| 182 | `DX.TXH.RESERVED.X1` | `DxTransactionHistory_ReservedX1` |  |  |  |
| 183 | `DX.TXH.NS.FWD.TXN` | `DxTransactionHistory_NsFwdTxn` |  |  |  |
| 184 | `DX.TXH.XO.AMT` | `DxTransactionHistory_XoAmt` |  |  |  |
| 185 | `DX.TXH.XO.CCY` | `DxTransactionHistory_XoCcy` |  |  |  |
| 186 | `DX.TXH.XO.ACCOUNT` | `DxTransactionHistory_XoAccount` |  |  |  |
| 187 | `DX.TXH.XO.ACC.CCY` | `DxTransactionHistory_XoAccCcy` |  |  |  |
| 188 | `DX.TXH.XO.ACC.AMT` | `DxTransactionHistory_XoAccAmt` |  |  |  |
| 189 | `DX.TXH.XO.EX.RATE` | `DxTransactionHistory_XoExRate` |  |  |  |
| 190 | `DX.TXH.XO.ACC.V.DATE` | `DxTransactionHistory_XoAccVDate` |  |  |  |
| 191 | `DX.TXH.XO.DATE` | `DxTransactionHistory_XoDate` |  |  |  |
| 192 | `DX.TXH.XO.POSTED` | `DxTransactionHistory_XoPosted` |  |  |  |
| 193 | `DX.TXH.RV.LINK` | `DxTransactionHistory_RvLink` | TField |  | Should be a valid record in DX.REVALUE.SUMMARY. |
| 194 | `DX.TXH.REGION` | `DxTransactionHistory_Region` | TField |  | Regions are used to represent exchanges for the purpose of defining trading calendars in the HOLIDAY application. |
| 195 | `DX.TXH.TAX.CODE` | `DxTransactionHistory_TaxCode` |  |  |  |
| 196 | `DX.TXH.TAX.TYPE` | `DxTransactionHistory_TaxType` |  |  |  |
| 197 | `DX.TXH.TAX.AMT.ACY` | `DxTransactionHistory_TaxAmtAcy` |  |  |  |
| 198 | `DX.TXH.TAX.AMT.TCY` | `DxTransactionHistory_TaxAmtTcy` |  |  |  |
| 199 | `DX.TXH.RESERVED.X2` | `DxTransactionHistory_ReservedX2` |  |  |  |
| 200 | `DX.TXH.EXOTIC.DATE` | `DxTransactionHistory_ExoticDate` |  |  |  |
| 201 | `DX.TXH.EXOTIC.TIME` | `DxTransactionHistory_ExoticTime` |  |  |  |
| 202 | `DX.TXH.VM.LCY.AMOUNT` | `DxTransactionHistory_VmLcyAmount` | TField |  | Holds Current Variation Margin Amount in Local Currency |
| 203 | `DX.TXH.DELIVERY.CCY` | `DxTransactionHistory_DeliveryCcy` | TField |  |  |
| 204 | `DX.TXH.OPTION.STYLE` | `DxTransactionHistory_OptionStyle` | TField |  |  |
| 205 | `DX.TXH.AS.CURRENCY` | `DxTransactionHistory_AsCurrency` | TField |  |  |
| 206 | `DX.TXH.AS.PRINCIPAL` | `DxTransactionHistory_AsPrincipal` | TField |  |  |
| 207 | `DX.TXH.LB.CURRENCY` | `DxTransactionHistory_LbCurrency` | TField |  |  |
| 208 | `DX.TXH.LB.PRINCIPAL` | `DxTransactionHistory_LbPrincipal` | TField |  |  |
| 209 | `DX.TXH.XO.EXOTIC.TYPE` | `DxTransactionHistory_XoExoticType` |  |  |  |
| 210 | `DX.TXH.NOTIONAL.TRADE.CCY` | `DxTransactionHistory_NotionalTradeCcy` | TField |  |  |
| 211 | `DX.TXH.NOTIONAL.DLV.CCY` | `DxTransactionHistory_NotionalDlvCcy` | TField |  |  |
| 212 | `DX.TXH.SY.TRANS.ID` | `DxTransactionHistory_SyTransId` | TField |  |  |
| 213 | `DX.TXH.CASH.PAYOUT.ACC` | `DxTransactionHistory_CashPayoutAcc` | TField |  | Holds the settlement account provided at trade level. |
| 214 | `DX.TXH.CASH.PAYOUT.CCY` | `DxTransactionHistory_CashPayoutCcy` | TField |  | Holds the currency of the settlement account updated to CASH.PAYOUT.ACC. |
| 215 | `DX.TXH.CASH.PAYOUT.AMT` | `DxTransactionHistory_CashPayoutAmt` | TField |  | The payout amount to be paid / received from customer in the CASH.PAYOUT.CCY. |
| 216 | `DX.TXH.FX.PAYOUT.CCY` | `DxTransactionHistory_FxPayoutCcy` | TField |  | The FX.PAYOUT.CCY in trade is mapped. |
| 217 | `DX.TXH.STRIKE.QUOTE.CCY` | `DxTransactionHistory_StrikeQuoteCcy` | TField |  | Holds the STRIKE.QUOTE.CCY given at trade level. |
| 218 | `DX.TXH.STRIKE.QUOTE` | `DxTransactionHistory_StrikeQuote` | TField |  | Holds the STRIKE.QUOTE given at trad level. |
| 219 | `DX.TXH.SY.DX.REFERENCE` | `DxTransactionHistory_SyDxReference` | TField |  |  |
| 220 | `DX.TXH.MTM.DATE` | `DxTransactionHistory_MtmDate` | TField |  | Date on which the Mark-to-Market (MTM) is posted. |
| 221 | `DX.TXH.MTM.CCY` | `DxTransactionHistory_MtmCcy` | TField |  | Currency in which the MTM is posted. |
| 222 | `DX.TXH.MTM.AMT` | `DxTransactionHistory_MtmAmt` | TField |  | Mark-to-Market (MTM) amount posted in MTM.CCY on MTM.DATE. |
| 223 | `DX.TXH.MTM.ACCOUNT` | `DxTransactionHistory_MtmAccount` | TField |  | Account in which the Mark-to-Market (MTM) is posted. |
| 224 | `DX.TXH.MTM.LCCY` | `DxTransactionHistory_MtmLccy` | TField |  | MTM amount in local currency equivalent. |
| 225 | `DX.TXH.MTM.LCCY.RATE` | `DxTransactionHistory_MtmLccyRate` | TField |  | Exchange rate between account currency and local currency. |
| 226 | `DX.TXH.PREV.MTM.DATE` | `DxTransactionHistory_PrevMtmDate` | TField |  | The previously posted Mark-to-Market (MTM) date |
| 227 | `DX.TXH.PREV.MTM.CCY` | `DxTransactionHistory_PrevMtmCcy` | TField |  | The previously posted Mark-to-Market (MTM) account currency. |
| 228 | `DX.TXH.PREV.MTM.AMT` | `DxTransactionHistory_PrevMtmAmt` | TField |  | The previously posted Mark-to-Market (MTM) amount. |
| 229 | `DX.TXH.PREV.MTM.ACCOUNT` | `DxTransactionHistory_PrevMtmAccount` | TField |  | The previously posted Mark-to-Market (MTM) account. |
| 230 | `DX.TXH.PREV.MTM.LCCY` | `DxTransactionHistory_PrevMtmLccy` | TField |  | The previously posted Mark-to-Market (MTM) amount in local currency. |
| 231 | `DX.TXH.PREV.MTM.LCCY.RATE` | `DxTransactionHistory_PrevMtmLccyRate` | TField |  | Exchange rate between account currency and local currency for the previously posted MTM. |
| 232 | `DX.TXH.MTM.TERMINATED` | `DxTransactionHistory_MtmTerminated` | TField |  | Flag indicator to reverse the MTM amount on reversal or closeout of the contract. |
| 233 | `DX.TXH.FTT.TYPE` | `DxTransactionHistory_FttType` | TField |  | Tax type considered for tax posting. |
| 234 | `DX.TXH.FTT.TAX.CODE` | `DxTransactionHistory_FttTaxCode` | TField |  | Tax code defined at TAX.TYPE.CONDITION for the tax calculation. |
| 235 | `DX.TXH.FTT.PERC` | `DxTransactionHistory_FttPerc` | TField |  | Percentage of tax that is applied on tax base amount. |
| 236 | `DX.TXH.FTT.BSE.AMT` | `DxTransactionHistory_FttBseAmt` | TField |  | Tax base amount in terms of EUR currrency on which the tax percentage is applied. |
| 237 | `DX.TXH.FTT.BSE.CCY` | `DxTransactionHistory_FttBseCcy` | TField |  |  |
| 238 | `DX.TXH.FTT.AMT.BCY` | `DxTransactionHistory_FttAmtBcy` | TField |  |  |
| 239 | `DX.TXH.FTT.CCY.TCY.RATE` | `DxTransactionHistory_FttCcyTcyRate` | TField |  |  |
| 240 | `DX.TXH.FTT.AMT.TCY` | `DxTransactionHistory_FttAmtTcy` | TField |  | Tax amount in account currency of the transaction. |
| 241 | `DX.TXH.FTT.AMT.LCY` | `DxTransactionHistory_FttAmtLcy` | TField |  | Tax amount in local currency. |
| 242 | `DX.TXH.FTT.AMT.CCY` | `DxTransactionHistory_FttAmtCcy` | TField |  | Tax currency which is EUR. |
| 243 | `DX.TXH.FTT.AMT` | `DxTransactionHistory_FttAmt` | TField |  | Tax amount in EUR. |
| 244 | `DX.TXH.FTT.EX.RATE` | `DxTransactionHistory_FttExRate` | TField |  | Exchange rate between trade currency and local currency. |
| 245 | `DX.TXH.LOTS.IN.TRADE.CCY` | `DxTransactionHistory_LotsInTradeCcy` | TField |  | Lots in terms of trade currency of the transaction. |
| 246 | `DX.TXH.CONTRACT.TERMS` | `DxTransactionHistory_ContractTerms` | TField |  |  |
| 247 | `DX.TXH.SETTLEMENT.METHOD` | `DxTransactionHistory_SettlementMethod` | TField |  | The settlement mode of the option contract is specified in this field. The option can be physically settled (Delivery/Receipt of the underlying takes place )or Cash settled (The cash difference is settled). Possible values are PHYSICAL or CASH. NULL value would by default use physical settlement. |
| 248 | `DX.TXH.BASKET.TYPE` | `DxTransactionHistory_BasketType` | TField |  | Indicates the type of basket. EQUITY OR CURRENCY |
| 249 | `DX.TXH.ULYING.ASSET.CLASS` | `DxTransactionHistory_UlyingAssetClass` | TField |  | Indicates whether the underlying is security or currency basket. |
| 250 | `DX.TXH.STATIC.LEG` | `DxTransactionHistory_StaticLeg` | TField |  | Choose the type of option from the drop down menu 'CALL' or 'PUT'. CALL: Call currency should be same in all multi-value pairs. PUT: Put currency should be same in all multi-value pairs. |
| 251 | `DX.TXH.ULYING.SECURITY` | `DxTransactionHistory_UlyingSecurity` |  |  |  |
| 252 | `DX.TXH.CALL.CCY` | `DxTransactionHistory_CallCcy` |  |  |  |
| 253 | `DX.TXH.PUT.CCY` | `DxTransactionHistory_PutCcy` |  |  |  |
| 254 | `DX.TXH.WEIGHT` | `DxTransactionHistory_Weight` |  |  |  |
| 255 | `DX.TXH.SPOT.PRICE` | `DxTransactionHistory_SpotPrice` |  |  |  |
| 256 | `DX.TXH.STRIKE.PERCENTAGE` | `DxTransactionHistory_StrikePercentage` |  |  |  |
| 257 | `DX.TXH.ULYING.STRIKE.CCY` | `DxTransactionHistory_UlyingStrikeCcy` |  |  |  |
| 258 | `DX.TXH.ULYING.STRIKE.PRICE` | `DxTransactionHistory_UlyingStrikePrice` |  |  |  |
| 259 | `DX.TXH.QUANTITY` | `DxTransactionHistory_Quantity` |  |  |  |
| 260 | `DX.TXH.CALL.AMOUNT` | `DxTransactionHistory_CallAmount` |  |  |  |
| 261 | `DX.TXH.PUT.AMOUNT` | `DxTransactionHistory_PutAmount` |  |  |  |
| 262 | `DX.TXH.EXERCISE` | `DxTransactionHistory_Exercise` |  |  |  |
| 263 | `DX.TXH.CASH.EXERCISE` | `DxTransactionHistory_CashExercise` | TField |  | Used for generating cash payouts. |
| 264 | `DX.TXH.CASH.AMOUNT` | `DxTransactionHistory_CashAmount` | TField |  | Holds the cash amount that needs to be paid out for a cash settled option. |
| 265 | `DX.TXH.CASH.CCY` | `DxTransactionHistory_CashCcy` | TField |  | Holds the currency corresponding to the CASH.AMOUNT field. |
| 266 | `DX.TXH.SETTLEMENT.AMT` | `DxTransactionHistory_SettlementAmt` | TField |  | Holds the cash payout amount calculated in settlement account currency. i.e in the SETTLEMENT.CCY field. |
| 267 | `DX.TXH.CLOSEOUT.TXN.AMT` | `DxTransactionHistory_CloseoutTxnAmt` | TField |  | Holds the settlement amount for physically settled contracts |
| 268 | `DX.TXH.SYS.FEE.TAX.AMT` | `DxTransactionHistory_SysFeeTaxAmt` |  |  |  |
| 269 | `DX.TX.OBSERVATION.DATE` | `DxTransaction_ObservationDate` |  |  |  |
| 270 | `DX.TX.OBSERVED.SPOT.RATE` | `DxTransaction_ObservedSpotRate` |  |  |  |
| 271 | `DX.TX.PARTICIPATION.RATE` | `DxTransaction_ParticipationRate` | TField |  | This fields hold the rate which is used to calculate the final pay out of the option. |
