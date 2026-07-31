# SC.EXE.SEC.ORDERS — Table Schema

> Source: `INSERTS/I_F.SC.EXE.SEC.ORDERS` in `SC_SctOrderExecution.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ESO.ORDER.NUMBER` | `ScExeSecOrders_OrderNumber` | TField |  | Validation Rules A maximum of 17 characters may be entered. This is a NOINPUT field. |
| 2 | `SC.ESO.SECURITY.NO` | `ScExeSecOrders_SecurityNo` | TField | Yes | Validation Rules Mandatory input. A maximum of 12 characters may be entered. This is a NOINPUT field. Must be the key to a valid entry on the SECURITY.MASTER file. |
| 3 | `SC.ESO.TRANSACTION.CODE` | `ScExeSecOrders_TransactionCode` | TField | Yes | Validation Rules Mandatory input. A maximum of 3 characters may be entered. This is a NOINPUT field. Must be the key to a valid entry on the SC.TRANS.NAME file. |
| 4 | `SC.ESO.ORDER.TYPE` | `ScExeSecOrders_OrderType` | TField |  | Validation Rules A maximum of 17 characters may be entered. This is a NOINPUT field. |
| 5 | `SC.ESO.TRADE.CCY` | `ScExeSecOrders_TradeCcy` | TField |  | Standard T24 currency field. Validation Rules A maximum of 3 characters may be entered. This is a NOINPUT field. Must be the key to a valid entry on the CURRENCY file. |
| 6 | `SC.ESO.NOMINAL.BALANCE` | `ScExeSecOrders_NominalBalance` | TField | Yes | Standard T24 amount field. Validation Rules Mandatory input. A maximum of 18 characters may be entered. This is a NOINPUT field. |
| 7 | `SC.ESO.CUSTOMER.NO` | `ScExeSecOrders_CustomerNo` |  |  |  |
| 8 | `SC.ESO.SECURITY.ACCT` | `ScExeSecOrders_SecurityAcct` |  |  |  |
| 9 | `SC.ESO.CUST.ACC.NO` | `ScExeSecOrders_CustAccNo` |  |  |  |
| 10 | `SC.ESO.CUST.NOMINAL` | `ScExeSecOrders_CustNominal` |  |  |  |
| 11 | `SC.ESO.CUST.PRICE` | `ScExeSecOrders_CustPrice` |  |  |  |
| 12 | `SC.ESO.CU.CASH.AMOUNT` | `ScExeSecOrders_CuCashAmount` |  |  |  |
| 13 | `SC.ESO.CALC.CHRGS` | `ScExeSecOrders_CalcChrgs` |  |  |  |
| 14 | `SC.ESO.CASH.CHRGS` | `ScExeSecOrders_CashChrgs` |  |  |  |
| 15 | `SC.ESO.SPLIT.CHRGS` | `ScExeSecOrders_SplitChrgs` |  |  |  |
| 16 | `SC.ESO.CASH.ROUNDING` | `ScExeSecOrders_CashRounding` |  |  |  |
| 17 | `SC.ESO.ADJUST.COMM` | `ScExeSecOrders_AdjustComm` |  |  |  |
| 18 | `SC.ESO.CU.BRKR.COMM` | `ScExeSecOrders_CuBrkrComm` |  |  |  |
| 19 | `SC.ESO.CU.FOREIGN.FEE` | `ScExeSecOrders_CuForeignFee` |  |  |  |
| 20 | `SC.ESO.CU.COMMISSION` | `ScExeSecOrders_CuCommission` |  |  |  |
| 21 | `SC.ESO.CU.COMM.TAX` | `ScExeSecOrders_CuCommTax` |  |  |  |
| 22 | `SC.ESO.CU.STAMP.TAX` | `ScExeSecOrders_CuStampTax` |  |  |  |
| 23 | `SC.ESO.CU.EBV.FEES` | `ScExeSecOrders_CuEbvFees` |  |  |  |
| 24 | `SC.ESO.CU.FEES.MISC` | `ScExeSecOrders_CuFeesMisc` |  |  |  |
| 25 | `SC.ESO.CU.DISC.PCENT` | `ScExeSecOrders_CuDiscPcent` |  |  |  |
| 26 | `SC.ESO.CU.DISC.AMT` | `ScExeSecOrders_CuDiscAmt` |  |  |  |
| 27 | `SC.ESO.CU.WHT.PERC` | `ScExeSecOrders_CuWhtPerc` |  |  |  |
| 28 | `SC.ESO.CU.WHT.TAX` | `ScExeSecOrders_CuWhtTax` |  |  |  |
| 29 | `SC.ESO.COMM.CODE` | `ScExeSecOrders_CommCode` |  |  |  |
| 30 | `SC.ESO.COMM.PERCENT` | `ScExeSecOrders_CommPercent` |  |  |  |
| 31 | `SC.ESO.COM.TAX.CODE` | `ScExeSecOrders_ComTaxCode` |  |  |  |
| 32 | `SC.ESO.COM.TAX.BCUR` | `ScExeSecOrders_ComTaxBcur` |  |  |  |
| 33 | `SC.ESO.COM.TAX.XRTE` | `ScExeSecOrders_ComTaxXrte` |  |  |  |
| 34 | `SC.ESO.CU.EX.RATE.ACC` | `ScExeSecOrders_CuExRateAcc` |  |  |  |
| 35 | `SC.ESO.CU.ACCOUNT.CCY` | `ScExeSecOrders_CuAccountCcy` |  |  |  |
| 36 | `SC.ESO.CU.DEPOSITORY` | `ScExeSecOrders_CuDepository` |  |  |  |
| 37 | `SC.ESO.SUB.ACCOUNT` | `ScExeSecOrders_SubAccount` |  |  |  |
| 38 | `SC.ESO.CU.BROKER.NO` | `ScExeSecOrders_CuBrokerNo` |  |  |  |
| 39 | `SC.ESO.CUST.AVG.PRICE` | `ScExeSecOrders_CustAvgPrice` |  |  |  |
| 40 | `SC.ESO.CU.INT.CTR` | `ScExeSecOrders_CuIntCtr` |  |  |  |
| 41 | `SC.ESO.SEC.TRADE.ID` | `ScExeSecOrders_SecTradeId` |  |  |  |
| 42 | `SC.ESO.CU.NOTES` | `ScExeSecOrders_CuNotes` |  |  |  |
| 43 | `SC.ESO.NARRATIVE` | `ScExeSecOrders_Narrative` |  |  |  |
| 44 | `SC.ESO.CU.INCOME.ACC` | `ScExeSecOrders_CuIncomeAcc` |  |  |  |
| 45 | `SC.ESO.CU.INCOME.CCY` | `ScExeSecOrders_CuIncomeCcy` |  |  |  |
| 46 | `SC.ESO.CU.CHARGE.TAX.TYPE` | `ScExeSecOrders_CuChargeTaxType` |  |  |  |
| 47 | `SC.ESO.CU.CHARGE.TAX.AMT` | `ScExeSecOrders_CuChargeTaxAmt` |  |  |  |
| 48 | `SC.ESO.CU.CHARGE.TAX.CODE` | `ScExeSecOrders_CuChargeTaxCode` |  |  |  |
| 49 | `SC.ESO.CU.SUBSCRIPTION.AMOUNT` | `ScExeSecOrders_CuSubscriptionAmount` |  |  |  |
| 50 | `SC.ESO.CU.ALLOTED.AMOUNT` | `ScExeSecOrders_CuAllotedAmount` |  |  |  |
| 51 | `SC.ESO.CU.REFUND.AMOUNT` | `ScExeSecOrders_CuRefundAmount` |  |  |  |
| 52 | `SC.ESO.TAXLOT.ALLOCATE` | `ScExeSecOrders_TaxlotAllocate` |  |  |  |
| 53 | `SC.ESO.QTY.ALLOTED` | `ScExeSecOrders_QtyAlloted` |  |  |  |
| 54 | `SC.ESO.CU.RESERVED.2` | `ScExeSecOrders_CuReserved2` |  |  |  |
| 55 | `SC.ESO.CU.RESERVED.1` | `ScExeSecOrders_CuReserved1` |  |  |  |
| 56 | `SC.ESO.BROKER.NO` | `ScExeSecOrders_BrokerNo` |  |  |  |
| 57 | `SC.ESO.BROKER.TYPE` | `ScExeSecOrders_BrokerType` |  |  |  |
| 58 | `SC.ESO.BR.ACC.NO` | `ScExeSecOrders_BrAccNo` |  |  |  |
| 59 | `SC.ESO.BR.SEC.ACCT` | `ScExeSecOrders_BrSecAcct` |  |  |  |
| 60 | `SC.ESO.NOMINAL.RECD` | `ScExeSecOrders_NominalRecd` |  |  |  |
| 61 | `SC.ESO.PRICE` | `ScExeSecOrders_Price` |  |  |  |
| 62 | `SC.ESO.UTC.DATE.TIME` | `ScExeSecOrders_UtcDateTime` |  |  |  |
| 63 | `SC.ESO.BR.BROKER.COMM` | `ScExeSecOrders_BrBrokerComm` |  |  |  |
| 64 | `SC.ESO.BR.FOREIGN.FEE` | `ScExeSecOrders_BrForeignFee` |  |  |  |
| 65 | `SC.ESO.CL.COMMISSION` | `ScExeSecOrders_ClCommission` |  |  |  |
| 66 | `SC.ESO.BR.STAMP.TAX` | `ScExeSecOrders_BrStampTax` |  |  |  |
| 67 | `SC.ESO.BR.EBV.FEES` | `ScExeSecOrders_BrEbvFees` |  |  |  |
| 68 | `SC.ESO.BR.FEES.MISC` | `ScExeSecOrders_BrFeesMisc` |  |  |  |
| 69 | `SC.ESO.BR.EX.RATE.ACC` | `ScExeSecOrders_BrExRateAcc` |  |  |  |
| 70 | `SC.ESO.BR.ACCOUNT.CCY` | `ScExeSecOrders_BrAccountCcy` |  |  |  |
| 71 | `SC.ESO.DELIVERY.INSTR` | `ScExeSecOrders_DeliveryInstr` |  |  |  |
| 72 | `SC.ESO.TRADE.TIME` | `ScExeSecOrders_TradeTime` |  |  |  |
| 73 | `SC.ESO.BR.EXE.ADV.REF` | `ScExeSecOrders_BrExeAdvRef` |  |  |  |
| 74 | `SC.ESO.BR.TR.AL.REF` | `ScExeSecOrders_BrTrAlRef` |  |  |  |
| 75 | `SC.ESO.BR.CHARGE.TAX.TYPE` | `ScExeSecOrders_BrChargeTaxType` |  |  |  |
| 76 | `SC.ESO.BR.CHARGE.TAX.AMT` | `ScExeSecOrders_BrChargeTaxAmt` |  |  |  |
| 77 | `SC.ESO.BR.CHARGE.TAX.CODE` | `ScExeSecOrders_BrChargeTaxCode` |  |  |  |
| 78 | `SC.ESO.BR.RESERVED.05` | `ScExeSecOrders_BrReserved05` |  |  |  |
| 79 | `SC.ESO.BR.RESERVED.04` | `ScExeSecOrders_BrReserved04` |  |  |  |
| 80 | `SC.ESO.BR.RESERVED.03` | `ScExeSecOrders_BrReserved03` |  |  |  |
| 81 | `SC.ESO.BR.RESERVED.02` | `ScExeSecOrders_BrReserved02` |  |  |  |
| 82 | `SC.ESO.BR.RESERVED.01` | `ScExeSecOrders_BrReserved01` |  |  |  |
| 83 | `SC.ESO.TRADE.DATE` | `ScExeSecOrders_TradeDate` | TField |  | Standard T24 date field. Validation Rules A maximum of 11 characters may be entered. |
| 84 | `SC.ESO.VALUE.DATE` | `ScExeSecOrders_ValueDate` | TField |  | Standard T24 date field. Validation Rules A maximum of 11 characters may be entered. |
| 85 | `SC.ESO.DEPOSITORY` | `ScExeSecOrders_Depository` | TField |  | Standard T24 customer field. Validation Rules A maximum of 10 characters may be entered. Must be the key to a valid entry on the CUSTOMER.SECURITY file. |
| 86 | `SC.ESO.STOCK.EXCHANGE` | `ScExeSecOrders_StockExchange` | TField |  | Validation Rules A maximum of 5 characters may be entered. Must be the key to a valid entry on the STOCK.EXCHANGE file. |
| 87 | `SC.ESO.MARKET.TYPE` | `ScExeSecOrders_MarketType` | TField |  | Validation Rules A maximum of 2 characters may be entered. The following values are permitted: S N F |
| 88 | `SC.ESO.SETT.NARRATIVE` | `ScExeSecOrders_SettNarrative` |  |  |  |
| 89 | `SC.ESO.ACCT.NARRATIVE` | `ScExeSecOrders_AcctNarrative` |  |  |  |
| 90 | `SC.ESO.ORDER.BROKER` | `ScExeSecOrders_OrderBroker` |  |  |  |
| 91 | `SC.ESO.AMT.TO.BROKER` | `ScExeSecOrders_AmtToBroker` |  |  |  |
| 92 | `SC.ESO.EXE.BY.BROKER` | `ScExeSecOrders_ExeByBroker` |  |  |  |
| 93 | `SC.ESO.INT.CTR` | `ScExeSecOrders_IntCtr` | TField |  | Interest counter for this execution, applicable for shares only. |
| 94 | `SC.ESO.ORDER.STATUS` | `ScExeSecOrders_OrderStatus` | TField |  | Validation Rules A maximum of 15 characters may be entered. The following values are permitted: ACCEPTED REJECTED TRANSMITTED |
| 95 | `SC.ESO.ODD.LOT.ORDER` | `ScExeSecOrders_OddLotOrder` | TField |  | Field specifying whether the order being executed is an odd lot order and is allowed to be specified only for ODDLOT SECURITY as defined in SECURITY.MASTER. If the order is an odd lots order then the order will be validatedagainst the odd lots fields on the SECURITY.MASTER record to ensure the order is valid. Validation Rules Valid Input - Yes/No |
| 96 | `SC.ESO.TRADE.DEPT` | `ScExeSecOrders_TradeDept` | TField |  | Currently unused by T24. |
| 97 | `SC.ESO.PRO.BR.CHGS` | `ScExeSecOrders_ProBrChgs` | TField | No | Flag controlling whether Broker Charges and Commission is to be Prorated across customer's or not. Gets defaultedfrom SC.STD.SEC.TRADE. Also the user can override it. Validation Rules Only input of 'YES' or 'NO' is allowed. Input of 'YES' is not allowed when TRADE.CREATION is BY.BROKER' Optional Field. |
| 98 | `SC.ESO.CALC.AVG.PRICE` | `ScExeSecOrders_CalcAvgPrice` | TField | No | Flag controlling whether or not Average Price for customer's is to be calculated or not. Gets defaulted from SC.STD.SEC.TRADE. Also the user can override it. Validation Rules Only input of 'YES' or 'NO' allowed. Optional Input. |
| 99 | `SC.ESO.TRADE.CREATION` | `ScExeSecOrders_TradeCreation` | TField | No | This field controls the SEC.TRADE creation from SC.EXE.SEC.ORDERS. Example: If Trade Creation is 'BY.PORTFOLIO' then SEC.TRADE's will be created for each Portfolio. To accept an option PARENT.CHILD. This will trigger generation of parent and child trades on execution ofindividual order. This field cannot be entered if order is already a parent child order Validation Rules Valid options are 'BY.CUST', 'BY.DEPO', 'BY.BROKER', 'BY.PORTFOLIO','PARENT.CHILD'. Optional Input. |
| 100 | `SC.ESO.PRORATA.NOM` | `ScExeSecOrders_ProrataNom` | TField | No | Yes/No field defaulted from PRORATA.NOM field in SC.STD.SEC.TRADE. If set to "YES" the nominals of each brokerwould be prorated to all the customers based on outstanding order nominals. Rounding differences if any would beadjusted against the first customer to the extent possible and further to the second customer and so on Validation Rules Only input of 'YES' or 'NO' is allowed. Optional Input. |
| 101 | `SC.ESO.CANCEL.REMAIN.ORD` | `ScExeSecOrders_CancelRemainOrd` | TField | No | Flag controlling whether the Text message displayed during partial execution to put the order to history shouldbe displayed or not. Gets defaulted from SC.STD.SEC.TRADE. Also the user can override it. Validation Rules Only input of 'YES' or 'NO' is allowed. Optional Input. |
| 102 | `SC.ESO.ROUT.COMPANY` | `ScExeSecOrders_RoutCompany` | TField |  | Routing company, i.e. the company through which the trade should be executed. |
| 103 | `SC.ESO.ROUT.SEC.ACC` | `ScExeSecOrders_RoutSecAcc` | TField |  | Field identifying the cross trading (internal) portfolio to be used in a multi company order/execution scenariowhen portfolio is shared across companies. If this portfolio is specified, there would be two trades : One betweenthe cross trading portfolio and street side broker and the other between the cross trading portfolio and actualcustomers. Validation Rules Must be a valid dealer book portfolio |
| 104 | `SC.ESO.PRICE.SPREAD` | `ScExeSecOrders_PriceSpread` | TField |  | Percentage of customer spread which would be applied over the broker price. It is the spread between the brokerprice and customer price and would be applied only for internal brokers in a scenario when portfolio is sharedacross companies. Validation Rules |
| 105 | `SC.ESO.DEFAULT.CALC.CHG` | `ScExeSecOrders_DefaultCalcChg` | TField |  | Field controlling the computation of commission/charges in SC.EXE.SEC.ORDERS. Charges are computed if this fieldis set to Yes and if the fields do not already have a value. Validation Rules YES/NO/Blank are the accepted values |
| 106 | `SC.ESO.CUM.EX.IND` | `ScExeSecOrders_CumExInd` |  |  |  |
| 107 | `SC.ESO.WHT.TAX.CODE` | `ScExeSecOrders_WhtTaxCode` | TField |  | Indicates the Tax code from the TAX.TYPE.CONDITION / TAX file. Defaults from the field SHARE.TAX / BOND.TAX fromthe file TXN.TAX.CODE. Validation Rules No input field |
| 108 | `SC.ESO.CHARGE.CALC.METHOD` | `ScExeSecOrders_ChargeCalcMethod` | TField |  | Determines how broker charges will be calculated. Can be BY.TRANCHE (default value if not set) or BY.BROKER. BY.TRANCHE will calculate charges for each execution, BY.BROKER will calculate charges by broker, these chargeswill then be allocated on a pro-rate basis for each execution. |
| 109 | `SC.ESO.SEGMENT` | `ScExeSecOrders_Segment` | TField |  | System populated field, identifies the segment allocated to the transaction. |
| 110 | `SC.ESO.DEF.DEAL.DESK` | `ScExeSecOrders_DefDealDesk` | TField |  | System populated field, the dealer desk allocated to the order. |
| 111 | `SC.ESO.ACT.DEAL.DESK` | `ScExeSecOrders_ActDealDesk` | TField |  | System populated field, the dealer desk that executed the transaction. |
| 112 | `SC.ESO.ADVICE.REQD` | `ScExeSecOrders_AdviceReqd` | TField |  | To be set to YES if MT514 is to be sent. |
| 113 | `SC.ESO.MT502.REJ.REASON` | `ScExeSecOrders_Mt502RejReason` |  |  |  |
| 114 | `SC.ESO.CONSOLIDATE.EXEC` | `ScExeSecOrders_ConsolidateExec` | TField |  | This field is used only for inward message processing. Allowed value YES. Creation of trade will happen only onfull execution of order though multiple MT513 are received. |
| 115 | `SC.ESO.DAY.TRADE` | `ScExeSecOrders_DayTrade` | TField |  | This field is used only for inward message processing. Allowed Value YES. Enable single trade creation for aday.Creation of trade will happen at the end of day before COB after the cut off time specified in EXEC.CUT.OFF. |
| 116 | `SC.ESO.AUTHORISE.TRADE` | `ScExeSecOrders_AuthoriseTrade` | TField |  | To be set to YES if the corresponding SEC.TRADE needs to be authorised automatically. |
| 117 | `SC.ESO.PARENT` | `ScExeSecOrders_Parent` | TField |  | Allowed value is YES This Field is to determine whether the order is a parent order |
| 118 | `SC.ESO.PARENT.REFERENCE` | `ScExeSecOrders_ParentReference` | TField |  |  |
| 119 | `SC.ESO.EXE.HLT` | `ScExeSecOrders_ExeHlt` | TField |  | This field will be populated from SEC.OPEN.ORDER record field EXE.HLT.Allowed options are YES,NO or NULL. Onsetting YES system will throw an override on committing th record. NO or NULL will allow the process of executingorder. |
| 120 | `SC.ESO.TRADE.HLT` | `ScExeSecOrders_TradeHlt` | TField |  | This field will be populated from SEC.OPEN.ORDER record field TRADE.HLT.Allowed options are YES,NO or NULL. Onsetting YES system will be create the SEC.TRADE in IHLD status. |
| 121 | `SC.ESO.PARENT.CHILD.DEPO` | `ScExeSecOrders_ParentChildDepo` | TField |  | This field is used to specify whether parent trades are to be created based on each depository. The value will be defaulted from similar field of SC.STD.SEC.TRADE but can be manually overridden. This field has a significance only if either TRADE.CREATION field is set as PARENT.CHILD or order itself iscreated as a parent child order. Validation Rules Allowed values is YES or No |
| 122 | `SC.ESO.ROUNDING.FACTOR` | `ScExeSecOrders_RoundingFactor` | TField |  | Minimum lot using which nominal will be executed. This will be defaulted from SEC.OPEN.ORDER. Value should be inmultiple of trading units and nominal execution will consider this field instead of trading units fromSECURITY.MASTER |
| 123 | `SC.ESO.UPFRONT.SEC` | `ScExeSecOrders_UpfrontSec` | TField |  | The field gets defaulted from the UPFRONT.SEC in SEC.OPEN.ORDER /Validation Rules: This is a NOINPUT field |
| 124 | `SC.ESO.INTEG.DATA.ITEM` | `ScExeSecOrders_IntegDataItem` |  |  |  |
| 125 | `SC.ESO.INTEG.DATA.VALUE` | `ScExeSecOrders_IntegDataValue` |  |  |  |
| 126 | `SC.ESO.TXN.CHANNEL` | `ScExeSecOrders_TxnChannel` | TField |  | Holds the information on mode of channel used to enter into the order.Mapped from SEC.OPEN.ORDER.List of channelscan be configured through EB.LOOKUP with VIRTUAL.TABLE as SC.CHANNEL. Validation Rules: This is a NOINPUT field |
| 127 | `SC.ESO.COM.ORDER.REF` | `ScExeSecOrders_ComOrderRef` | TField |  | The field will hold a common reference to link a set of switch orders.Mapped from SEC.OPEN.ORDER Validation Rules: NOINPUT field |
| 128 | `SC.ESO.AGGREGATION` | `ScExeSecOrders_Aggregation` | TField |  | Allowed value is NO. This Field is to determine whether the individual execution order needs to be considered for aggregation. |
| 129 | `SC.ESO.MANUAL.ALLOC` | `ScExeSecOrders_ManualAlloc` | TField |  |  |
| 130 | `SC.ESO.CANCEL.TRADE.REF` | `ScExeSecOrders_CancelTradeRef` | TField |  | Trade reference that is to be cancelled.Will be mapped from SEC.OPEN.ORDER Validation Rules: NOINPUT field |
| 131 | `SC.ESO.TRADING.VENUE` | `ScExeSecOrders_TradingVenue` |  |  |  |
| 132 | `SC.ESO.RESERVED.6` | `ScExeSecOrders_Reserved6` | TField |  |  |
| 133 | `SC.ESO.RESERVED.5` | `ScExeSecOrders_Reserved5` | TField |  |  |
| 134 | `SC.ESO.RESERVED.4` | `ScExeSecOrders_Reserved4` | TField |  |  |
| 135 | `SC.ESO.RESERVED.3` | `ScExeSecOrders_Reserved3` | TField |  |  |
| 136 | `SC.ESO.RESERVED.2` | `ScExeSecOrders_Reserved2` | TField |  |  |
| 137 | `SC.ESO.RESERVED.1` | `ScExeSecOrders_Reserved1` | TField |  |  |
| 138 | `SC.ESO.LOCAL.REF` | `ScExeSecOrders_LocalRef` |  |  |  |
| 139 | `SC.ESO.OVERRIDE` | `ScExeSecOrders_Override` |  |  |  |
| 140 | `SC.ESO.RECORD.STATUS` | `ScExeSecOrders_RecordStatus` | String |  |  |
| 141 | `SC.ESO.CURR.NO` | `ScExeSecOrders_CurrNo` | String |  |  |
| 142 | `SC.ESO.INPUTTER` | `ScExeSecOrders_Inputter` |  |  |  |
| 143 | `SC.ESO.DATE.TIME` | `ScExeSecOrders_DateTime` |  |  |  |
| 144 | `SC.ESO.AUTHORISER` | `ScExeSecOrders_Authoriser` | String |  |  |
| 145 | `SC.ESO.CO.CODE` | `ScExeSecOrders_CoCode` | String |  |  |
| 146 | `SC.ESO.DEPT.CODE` | `ScExeSecOrders_DeptCode` | String |  |  |
| 147 | `SC.ESO.AUDITOR.CODE` | `ScExeSecOrders_AuditorCode` | String |  |  |
| 148 | `SC.ESO.AUDIT.DATE.TIME` | `ScExeSecOrders_AuditDateTime` | String |  |  |
