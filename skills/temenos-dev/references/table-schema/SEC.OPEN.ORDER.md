# SEC.OPEN.ORDER — Table Schema

> Source: `INSERTS/I_F.SEC.OPEN.ORDER` in `SC_SctOrderCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SOO.ORDER.DATE` | `SecOpenOrder_OrderDate` | TField | Yes | Date of the instructions contained within the transaction. The date in this field is important since, if a clients instructions are missed, this effectively is the date towhich any loss will apply. The validation on the ORDER.DATE field in this SEC.OPEN.ORDER application can be controlled to a certain extentby the User. The current versions of this transaction enable this field to contain a date of less than the systemdate. This is to allow the booking of orders that had been previously agreed but not yet been input into thesystem, perhaps resulting from the ORDER.BY.CUST application. If you wish to INHIBIT input of past order dates, a VERSION routine has been written to ensure that ordervalidation will prevent this field from allowing past dates. The name of this VERSION routine is SC.SOO.ORDER.DATE.VAL and to invoke this alternative field validation, youshould enter the following into the fields : Field : VALIDATION.FLD ORDER.DATE VALIDATION.RTN SC.SOO.ORDER.DATE.VAL on all SEC.OPEN.ORDER versions for which you wish to inhibit input of dates in the past and authorise. It is also possible for the date to be fed through from the ORDER.BY.CUST application if the SEC.OPEN.ORDER wasgenerated as a result of a successful verification of the underlying ORDER.BY.CUST transaction. Even so, the datewill still be subject to the checks described above. Validation Rules No matter whether running under the sub-routine or not, the default date is always the System date. Up to 9 type D date characters, (Standard Date Format) Mandatory input. Date cannot be less than today if this field is under the control of the sub-routine described above. An override will be required if the date input is greater than today whether validation is running under thesub-routine or not. |
| 2 | `SC.SOO.ORDER.TIME` | `SecOpenOrder_OrderTime` | TField | No | Time of the instructions contained within the transactions. This field is the time of the order. It is possible that the time may have been supplied from the successful verification of an ORDER.BY.CUSTtransaction, in which case the field will already have been populated. If this was the case, then you may stillchange the time if so required. Validation Rules Up to 14 Type T Time characters. Optional input. (Default is time the order is input) Will default to current time unless a time is input or has been defaulted from an ORDER.BY.CUST transaction The time will be recorded in an HH:MM:SS:DDDDD format |
| 3 | `SC.SOO.SECURITY.NO` | `SecOpenOrder_SecurityNo` | TField |  | Identifies the Security number involved in this particular Open Order Transaction. Validation Rules Security Number, Security Mnemonic or Security alternate index. Cannot be changed once the order has been TRADED or TRANSMITTED if STP processing is used. For Cancel Order , value in this field should match with Security in Trade. |
| 4 | `SC.SOO.VALUE.DATE` | `SecOpenOrder_ValueDate` | TField |  | Records the date on which the trade is to be effected. The value date for any transaction can vary from 1 day to 1 month depending on the security being traded and thestock exchange at which it is being traded. A default value date can be defaulted by using the facility within the STOCK.EXCHANGE table.Here the user candefine the number of Business or Calendar days between the trade and value date of any particular Stock Exchange. In STOCK.EXCHANGE table, user can also specify the settlement basis as FIXED. In this case, a calendar(STK.EXCH.CALENDAR) is maintained for the Stock Exchange and for a Year. A settlement day can be defined for aperiod for a particular Stock Exchange and Year. The value date specified here would be carried forward to the order execution and would be used as the valuedate of the trade N.B Care should be taken when and if using this facility. Validation Rules Up to 9 type D date characters |
| 5 | `SC.SOO.MATURITY.DATE` | `SecOpenOrder_MaturityDate` | TField |  | Specifies the maturity date of the security. The date is defaulted from the SECURITY.MASTER record and can not bechanged. For information purposes only. N.B - This field is only applicable for Bonds. Validation Rules Up to 9 type D date characters (Standard date format) Internally generated field. |
| 6 | `SC.SOO.ORDER.TYPE` | `SecOpenOrder_OrderType` | TField | Yes | This input details the type of Order being passed to the Dealers. Whether buy or sell at BEST or at MARKET. A buy or sell instruction to a dealer with the at Market flag signifies that there is no limit or restriction onthe price at which he can execute the transaction. The client or investment manager is happy with the market price. Best price indicates that the dealer ought really to shop around for his price as there may be a lot of activityand consequently differing prices to be achieved. Price indicates that the price input within field 9 is a minimum or maximum price to be paid or received for thesecurities stipulated. LIMIT.PRICE is mandatory input for both Price and Stop kind of order types. Cash indicates that the customer wants to trade a particular amount of cash in the transaction. The nominal willbe calculated from this cash amount can either be net or gross of charges/commissions. This is controlled by theCASH.CHRGS field. The type of order is determined based on the specifications for various order types in SC.ORDER.TYPE file. Validation Rules MUST BE A VALID SC.ORDER.TYPE record |
| 7 | `SC.SOO.TYPE.OF.TRADE` | `SecOpenOrder_TypeOfTrade` | TField |  | The Open Order can be used by the Portfolio Manager to process Buy or Sell instructions for Bonds or sharestraded on either the Spot market or on the Forward market. It is at this level that the Portfolio Manager instructs the Dealers that the order he is giving relates to aparticular transaction. This then determines the transaction that will be created when the deal has been executed.i.e. S will generate a SEC.TRADE Validation Rules It will accept S and its valid. Where S = SEC.TRADE. |
| 8 | `SC.SOO.TRANSACTION.CODE` | `SecOpenOrder_TransactionCode` | TField | Yes | Indicates whether the Customer is placing an order to buy or sell. The transaction code is user defined for convenience and adaptability to cover all eventualities within theSecuritys Module From Coupon Payments to Redemptions and Capital Increase Type updates. Within the Open Orderapplication it is suggested that the same codes as for the Sec.Trade application i.e. For A purchase of securitiesSPR and for a Sale SSL be used. Validation Rules 1-3 type S (uppercase alpha) character Sc.Trans.Name. (Mandatory Input.) Must be a valid code on the SC.TRANS.NAME file. |
| 9 | `SC.SOO.TRADE.CCY` | `SecOpenOrder_TradeCcy` | TField | Yes | Specifies the currency in which the transaction will be settled. The trade currency is the settlement currency for the Broker involved. As with the SEC.TRADE application itdetermines the currency of the account to which the Broker Net amount is posted. The customer however can bedebited in a different currency. Validation Rules 3 type CCY (alpha) character currency code. or 1-3 numeric character currency number. (Mandatory Input.) Defaultvalue = Price currency as specified within the Security Master record for that particular Security ID. Must exist on the CCY file. For Cancel Order , value in this field should match with Customer in Trade. |
| 10 | `SC.SOO.CUST.NUMBER` | `SecOpenOrder_CustNumber` |  |  |  |
| 11 | `SC.SOO.SECURITY.ACCNT` | `SecOpenOrder_SecurityAccnt` |  |  |  |
| 12 | `SC.SOO.NO.NOMINAL` | `SecOpenOrder_NoNominal` |  |  |  |
| 13 | `SC.SOO.CU.CASH.AMOUNT` | `SecOpenOrder_CuCashAmount` |  |  |  |
| 14 | `SC.SOO.CURR.PRICE` | `SecOpenOrder_CurrPrice` |  |  |  |
| 15 | `SC.SOO.CALC.CHRGS` | `SecOpenOrder_CalcChrgs` |  |  |  |
| 16 | `SC.SOO.CASH.CHRGS` | `SecOpenOrder_CashChrgs` |  |  |  |
| 17 | `SC.SOO.SPLIT.CHRGS` | `SecOpenOrder_SplitChrgs` |  |  |  |
| 18 | `SC.SOO.CASH.ROUNDING` | `SecOpenOrder_CashRounding` |  |  |  |
| 19 | `SC.SOO.ADJUST.COMM` | `SecOpenOrder_AdjustComm` |  |  |  |
| 20 | `SC.SOO.NARRATIVE` | `SecOpenOrder_Narrative` |  |  |  |
| 21 | `SC.SOO.CUST.ACC.NO` | `SecOpenOrder_CustAccNo` |  |  |  |
| 22 | `SC.SOO.CU.EX.RATE.ACC` | `SecOpenOrder_CuExRateAcc` |  |  |  |
| 23 | `SC.SOO.SETTLEMENT.CCY` | `SecOpenOrder_SettlementCcy` |  |  |  |
| 24 | `SC.SOO.CU.BRKR.COMM` | `SecOpenOrder_CuBrkrComm` |  |  |  |
| 25 | `SC.SOO.WAIVE.CU.BR.COM` | `SecOpenOrder_WaiveCuBrCom` |  |  |  |
| 26 | `SC.SOO.INVEST.OPTION.TYPE` | `SecOpenOrder_InvestOptionType` |  |  |  |
| 27 | `SC.SOO.TAXLOT.ALLOCATE` | `SecOpenOrder_TaxlotAllocate` |  |  |  |
| 28 | `SC.SOO.CU.FOREIGN.FEE` | `SecOpenOrder_CuForeignFee` |  |  |  |
| 29 | `SC.SOO.CU.COMMISSION` | `SecOpenOrder_CuCommission` |  |  |  |
| 30 | `SC.SOO.CU.COMM.TAX` | `SecOpenOrder_CuCommTax` |  |  |  |
| 31 | `SC.SOO.CU.STAMP.TAX` | `SecOpenOrder_CuStampTax` |  |  |  |
| 32 | `SC.SOO.CU.EBV.FEES` | `SecOpenOrder_CuEbvFees` |  |  |  |
| 33 | `SC.SOO.CU.FEES.MISC` | `SecOpenOrder_CuFeesMisc` |  |  |  |
| 34 | `SC.SOO.CU.DISC.PCENT` | `SecOpenOrder_CuDiscPcent` |  |  |  |
| 35 | `SC.SOO.CU.DISC.AMT` | `SecOpenOrder_CuDiscAmt` |  |  |  |
| 36 | `SC.SOO.CU.WHT.PERC` | `SecOpenOrder_CuWhtPerc` |  |  |  |
| 37 | `SC.SOO.CU.WHT.TAX` | `SecOpenOrder_CuWhtTax` |  |  |  |
| 38 | `SC.SOO.COMM.CODE` | `SecOpenOrder_CommCode` |  |  |  |
| 39 | `SC.SOO.COMM.PERCENT` | `SecOpenOrder_CommPercent` |  |  |  |
| 40 | `SC.SOO.COM.TAX.CODE` | `SecOpenOrder_ComTaxCode` |  |  |  |
| 41 | `SC.SOO.COM.TAX.BCUR` | `SecOpenOrder_ComTaxBcur` |  |  |  |
| 42 | `SC.SOO.COM.TAX.XRTE` | `SecOpenOrder_ComTaxXrte` |  |  |  |
| 43 | `SC.SOO.CU.DEPOSITORY` | `SecOpenOrder_CuDepository` |  |  |  |
| 44 | `SC.SOO.SUB.ACCOUNT` | `SecOpenOrder_SubAccount` |  |  |  |
| 45 | `SC.SOO.PORT.CONST.NO` | `SecOpenOrder_PortConstNo` |  |  |  |
| 46 | `SC.SOO.CU.BROKER.NO` | `SecOpenOrder_CuBrokerNo` |  |  |  |
| 47 | `SC.SOO.CU.NOTES` | `SecOpenOrder_CuNotes` |  |  |  |
| 48 | `SC.SOO.CU.ENTL.ID` | `SecOpenOrder_CuEntlId` |  |  |  |
| 49 | `SC.SOO.CU.INT.CTR` | `SecOpenOrder_CuIntCtr` |  |  |  |
| 50 | `SC.SOO.BUYING.POWER` | `SecOpenOrder_BuyingPower` |  |  |  |
| 51 | `SC.SOO.EXT.CUSTODIAN` | `SecOpenOrder_ExtCustodian` |  |  |  |
| 52 | `SC.SOO.CU.INCOME.ACC` | `SecOpenOrder_CuIncomeAcc` |  |  |  |
| 53 | `SC.SOO.CU.INCOME.CCY` | `SecOpenOrder_CuIncomeCcy` |  |  |  |
| 54 | `SC.SOO.CU.CHARGE.TAX.TYPE` | `SecOpenOrder_CuChargeTaxType` |  |  |  |
| 55 | `SC.SOO.CU.CHARGE.TAX.AMT` | `SecOpenOrder_CuChargeTaxAmt` |  |  |  |
| 56 | `SC.SOO.CU.CHARGE.TAX.CODE` | `SecOpenOrder_CuChargeTaxCode` |  |  |  |
| 57 | `SC.SOO.PERCENTAGE` | `SecOpenOrder_Percentage` |  |  |  |
| 58 | `SC.SOO.CU.ORDER.AMOUNT` | `SecOpenOrder_CuOrderAmount` |  |  |  |
| 59 | `SC.SOO.CU.BID.TYPE` | `SecOpenOrder_CuBidType` |  |  |  |
| 60 | `SC.SOO.CU.BID.QUANTITY` | `SecOpenOrder_CuBidQuantity` |  |  |  |
| 61 | `SC.SOO.CU.BID.PRICE` | `SecOpenOrder_CuBidPrice` |  |  |  |
| 62 | `SC.SOO.CU.SUBSCRIPTION.AMOUNT` | `SecOpenOrder_CuSubscriptionAmount` |  |  |  |
| 63 | `SC.SOO.QTY.ALLOTED` | `SecOpenOrder_QtyAlloted` |  |  |  |
| 64 | `SC.SOO.LIMIT.PRICE` | `SecOpenOrder_LimitPrice` | TField | Conditional | The Price at which the shares are to be bought or sold. This can be used in conjunction with field ORDER.TYPE to inform the Dealers of a Limit price to be reachedbefore the transaction should be executed. When this value is left blank, with field ORDER.TYPE set to M, it indicates that the securities are to be boughtor sold at Market. If field ORDER.TYPE is set to P, and this field is entered, then the instructions to the Dealer are to trade,but only, at the price stipulated. Validation Rules 1-15 numeric characters (0-6 integers 0-9 decimals) plus a . (Optional Input) If this field is entered the following field LIMIT.EXP.DATE becomes Mandatory. Dealers will rarely accept open ended Limit instructions as it places a heavy burden on them. |
| 65 | `SC.SOO.LIMIT.TYPE` | `SecOpenOrder_LimitType` | TField | No | Field used to default the LIMIT.DATE field. Input of GTC,GTD, GTM, GTY or GTW allowed. GTD - Order valid until theorder date. GTW - Good this week (GTW) orders will be only valid in the week of its placement.(i.e. If Saturday andSunday are weekends, Expiry date will be Friday's date but, If Friday is holiday, Expiry date will be Thursday'sdate.). GTM - Order valid until the end of the month of the order date. GTY - Order valid until the end of the yearof the order date.GTC � Order valid until it is CANCELLED so limit exp date will be null. Validation Rules Valid input GTC,GTD, GTM, GTY, GTW (Optional Input) Will default to GTD. |
| 66 | `SC.SOO.LIMIT.EXP.DATE` | `SecOpenOrder_LimitExpDate` | TField | Conditional | This field specifies the validity of the Limit, i.e. how long is it to remain in force. When field 9 is entered this field becomes Mandatory. The logic being that if a limit price is passed onto theDealers then they require an expiry date for that Order. The validity of that date will depend very much on work and local practices. Validation Rules Up to 9 type D date characters,(Standard Date format in range 1950 - 2049). (Optional Input) |
| 67 | `SC.SOO.LINK.ORDER.NO` | `SecOpenOrder_LinkOrderNo` |  |  |  |
| 68 | `SC.SOO.DEPOSITORY` | `SecOpenOrder_Depository` | TField |  | Stipulates into or out of which Depository Securities should be placed or withdrawn when a Security Transactionis effected. Once this Sec.Open.Order has been validated there is an on-line check to verify that sufficient securities areheld in the case of a Sale. In the case where insufficient securities exist then an override message will informthe inputter of the fact. Validation Rules Customer Number or Customer Mnemonic Must exist as a valid Customer type DEPOSITORY in the CUSTOMER.SECURITY application. Cannot be changed once the order has been TRADED or TRANSMITTED if STP processing is used. |
| 69 | `SC.SOO.NOMINEE.CODE` | `SecOpenOrder_NomineeCode` | TField | No | Identifies the Nominee Company if any with whom or in whose name the securities are registered. The Nominee code when entered throughout the Securities Module forms part of the position key used for storingand accessing Clients positions in a specified position. It is therefore important to note that when and if inputinitially, when creating a security position, it must be entered when carrying out transactions or administrationduties at a later date; failure to do so might cause misleading warning messages such as Insufficient Stock. Validation Rules 1 - 5 type S (uppercase alpha or numeric) character Nominee code. (Optional Input.) |
| 70 | `SC.SOO.ACCOUNT.MANAGER` | `SecOpenOrder_AccountManager` | TField |  | Automatic default to the Account Manager as specified for this client at Customer level. Validation Rules Default is a valid Account Officer ID. (Automatic Default.) Must exist as a valid Account Officer record on the Account Officer File. |
| 71 | `SC.SOO.ACCT.NARRATIVE` | `SecOpenOrder_AcctNarrative` |  |  |  |
| 72 | `SC.SOO.BROKER` | `SecOpenOrder_Broker` |  |  |  |
| 73 | `SC.SOO.DATE.TO.BROKER` | `SecOpenOrder_DateToBroker` |  |  |  |
| 74 | `SC.SOO.TIME.TO.BROKER` | `SecOpenOrder_TimeToBroker` |  |  |  |
| 75 | `SC.SOO.AMT.TO.BROKER` | `SecOpenOrder_AmtToBroker` |  |  |  |
| 76 | `SC.SOO.BR.CASH.AMT` | `SecOpenOrder_BrCashAmt` |  |  |  |
| 77 | `SC.SOO.BR.PRICE` | `SecOpenOrder_BrPrice` |  |  |  |
| 78 | `SC.SOO.BROKER.TYPE` | `SecOpenOrder_BrokerType` |  |  |  |
| 79 | `SC.SOO.BR.SEC.ACCT` | `SecOpenOrder_BrSecAcct` |  |  |  |
| 80 | `SC.SOO.BR.ACC.NO` | `SecOpenOrder_BrAccNo` |  |  |  |
| 81 | `SC.SOO.BR.ACCOUNT.CCY` | `SecOpenOrder_BrAccountCcy` |  |  |  |
| 82 | `SC.SOO.BR.EX.RATE.ACC` | `SecOpenOrder_BrExRateAcc` |  |  |  |
| 83 | `SC.SOO.BR.DELIV.INSTR` | `SecOpenOrder_BrDelivInstr` |  |  |  |
| 84 | `SC.SOO.EXE.BY.BROKER` | `SecOpenOrder_ExeByBroker` |  |  |  |
| 85 | `SC.SOO.BANK.CORRES` | `SecOpenOrder_BankCorres` |  |  |  |
| 86 | `SC.SOO.BROK.CORRES` | `SecOpenOrder_BrokCorres` |  |  |  |
| 87 | `SC.SOO.CONFIRMATION` | `SecOpenOrder_Confirmation` |  |  |  |
| 88 | `SC.SOO.DELIVERY.KEY` | `SecOpenOrder_DeliveryKey` |  |  |  |
| 89 | `SC.SOO.BR.RESERVED.1` | `SecOpenOrder_BrReserved1` |  |  |  |
| 90 | `SC.SOO.ORDER.INITIATOR` | `SecOpenOrder_OrderInitiator` | TField |  | This field holds the Order Initiator. This might be the bank or the client (account holder). It can either hold values bank or Client�s customer ID. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 91 | `SC.SOO.TRADER` | `SecOpenOrder_Trader` | TField |  | This field holds the trader third party. It can either hold the LEI or National ID or any other identifier. It can also be mapped to a T24 customer ID, from where the LEI or name of the customer can be got. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 92 | `SC.SOO.MANAGER` | `SecOpenOrder_Manager` | TField |  | This field holds the manager third party. It can either hold the LEI or National ID or any other identifier. It can also be mapped to a T24 customer ID, from where the LEI or name of the customer can be got. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 93 | `SC.SOO.UTC.DATE.TIME` | `SecOpenOrder_UtcDateTime` |  |  |  |
| 94 | `SC.SOO.SECURITIES.CR.DR` | `SecOpenOrder_SecuritiesCrDr` | TField |  | Indication only of the type of transaction as regards the Broker side of the transaction. When transaction code entered at field 6 for the client the system reads the SC.TRANS.TYPE file in which arestored sets of transaction codes and defaults to the reverse code for the Broker side of a particular transaction. Validation Rules 1 - 3 type S (uppercase alpha) character SC.Trans.Name Code. (Automatic Default) Must exist as a valid transaction code on the SC.TRANS.NAME file. |
| 95 | `SC.SOO.REFERENCE.NO` | `SecOpenOrder_ReferenceNo` |  |  |  |
| 96 | `SC.SOO.CUSTOMER.NO` | `SecOpenOrder_CustomerNo` |  |  |  |
| 97 | `SC.SOO.SEC.ACC.NO` | `SecOpenOrder_SecAccNo` |  |  |  |
| 98 | `SC.SOO.BROKER.NO` | `SecOpenOrder_BrokerNo` |  |  |  |
| 99 | `SC.SOO.EXE.DETAIL` | `SecOpenOrder_ExeDetail` |  |  |  |
| 100 | `SC.SOO.NO.NOM.FILLED` | `SecOpenOrder_NoNomFilled` |  |  |  |
| 101 | `SC.SOO.TRADE.PRICE` | `SecOpenOrder_TradePrice` |  |  |  |
| 102 | `SC.SOO.TRADE.DATE` | `SecOpenOrder_TradeDate` |  |  |  |
| 103 | `SC.SOO.TRADE.TIME` | `SecOpenOrder_TradeTime` |  |  |  |
| 104 | `SC.SOO.ORDER.NOMINAL` | `SecOpenOrder_OrderNominal` | TField |  | System generated. Validation Rules Up to 14 numeric amounts according to currency (No input field) |
| 105 | `SC.SOO.LIQUIDATION.PERIOD` | `SecOpenOrder_LiquidationPeriod` | TField |  | Validation Rules 6 Year and month characters |
| 106 | `SC.SOO.PREMIUM.PRICE` | `SecOpenOrder_PremiumPrice` | TField |  | Amount of premium price Validation Rules 10 Character amount field |
| 107 | `SC.SOO.MARKET.TYPE` | `SecOpenOrder_MarketType` | TField | No | Market type can be Spot (S), Forward (F) or Normal (N) Validation Rules S, N or F (Optional Input) |
| 108 | `SC.SOO.DEAL.STATUS` | `SecOpenOrder_DealStatus` | TField | No | Current status of the order. Validation Rules ACCEPTED, REJECTED, TRANSMITTED, OFFICER.TRANS, TRADED (Optional Input),'CANCELLED' AND 'CANCEL.CHILD'. When DEAL.STATUS is CANCELLED, Pending executions will be executed and remaining orders will be cancelled. Ifthere are no pending executions, whole order will be cancelled. DEAL.STATUS of CANCEL.CHILD can be set only forparent order and similar processing with deal status CANCELLED will happen for child orders |
| 109 | `SC.SOO.DEAL.NARRATIVE` | `SecOpenOrder_DealNarrative` |  |  |  |
| 110 | `SC.SOO.VAL.IN.SETT.CCY` | `SecOpenOrder_ValInSettCcy` |  |  |  |
| 111 | `SC.SOO.VERIFY.BY.DEALER` | `SecOpenOrder_VerifyByDealer` | TField |  | System updated field Validation Rules Up to 40 SWIFT characters (No Input) |
| 112 | `SC.SOO.LOCAL.REF` | `SecOpenOrder_LocalRef` |  |  |  |
| 113 | `SC.SOO.CUST.DEPO` | `SecOpenOrder_CustDepo` |  |  |  |
| 114 | `SC.SOO.CU.DEPO.NOM` | `SecOpenOrder_CuDepoNom` |  |  |  |
| 115 | `SC.SOO.CU.NOM.CODE` | `SecOpenOrder_CuNomCode` |  |  |  |
| 116 | `SC.SOO.MARKET.PRICE` | `SecOpenOrder_MarketPrice` | TField |  | This field holds the market price of the security when the order is placed |
| 117 | `SC.SOO.STOCK.EXCHANGE` | `SecOpenOrder_StockExchange` | TField | No | This optional field is used to record the STOCK.EXCHANGE in which the order is to be processed. It is possible that this field may already be populated from the details recorded in the ORDER.BY.CUSTapplication. If this was the case, then it may still be changed if found to be necessary. Validation Rules Must be a valid stock exchange record existing on the STOCK.EXCHANGE file. |
| 118 | `SC.SOO.GROUP.ORDER` | `SecOpenOrder_GroupOrder` | TField |  | When orders are grouped by SC.GROUP.ORDERS a grouped SEC.OPEN.ORDER is created. This grouped SEC.OPEN.ORDER idis written in this field. Validation Rules No-input system updated field |
| 119 | `SC.SOO.ODD.LOT.ORDER` | `SecOpenOrder_OddLotOrder` | TField |  | This field indicates if the order is an order of odd lot or not. The values allowed are : - YES : Odd lot order. No check is done for trading unit. But the order is validated against the 3 SECURITYMASTER fields added for odd lot process : ODD.LOT.TRADE, ODD.LOT.BROKER, ODD.LOT.EXCHANGE - NO : Normal order. The trading unit will be checked. If the number of shares is not divisible by the tradingunit of the security, then the order is rejected. - BLANK : Default equivalent to NO. Validation Rules |
| 120 | `SC.SOO.ACTIVITY.CODE` | `SecOpenOrder_ActivityCode` |  |  |  |
| 121 | `SC.SOO.MSG.BROKER` | `SecOpenOrder_MsgBroker` |  |  |  |
| 122 | `SC.SOO.MSG.NO` | `SecOpenOrder_MsgNo` |  |  |  |
| 123 | `SC.SOO.MSG.CLASS` | `SecOpenOrder_MsgClass` |  |  |  |
| 124 | `SC.SOO.OVR.CARRIER` | `SecOpenOrder_OvrCarrier` |  |  |  |
| 125 | `SC.SOO.OVR.ADDRESS` | `SecOpenOrder_OvrAddress` |  |  |  |
| 126 | `SC.SOO.SEND.ADVICE` | `SecOpenOrder_SendAdvice` |  |  |  |
| 127 | `SC.SOO.SOFT.DLVRY.KEY` | `SecOpenOrder_SoftDlvryKey` |  |  |  |
| 128 | `SC.SOO.ROUT.COMPANY` | `SecOpenOrder_RoutCompany` | TField |  | The company through which the order needs to be routed. Defaulted based on conditions specified inSC.ORDER.ROUTING. Validation Rules Valid COMPANY to be input. Routing done in cases where portfolios are shared across companies. |
| 129 | `SC.SOO.CUM.EX.IND` | `SecOpenOrder_CumExInd` |  |  |  |
| 130 | `SC.SOO.WHT.TAX.CODE` | `SecOpenOrder_WhtTaxCode` | TField |  | Indicates the Tax code from the TAX.TYPE.CONDITION / TAX file. Defaults from the field SHARE.TAX / BOND.TAX fromthe file TXN.TAX.CODE. Validation Rules No input field |
| 131 | `SC.SOO.SEGMENT` | `SecOpenOrder_Segment` | TField |  | System populated field, identifies the segment allocated to the transaction. |
| 132 | `SC.SOO.DEF.DEAL.DESK` | `SecOpenOrder_DefDealDesk` | TField |  | System populated field, the dealer desk allocated to the order. |
| 133 | `SC.SOO.ACT.DEAL.DESK` | `SecOpenOrder_ActDealDesk` | TField |  | System populated field, the dealer desk that executed the transaction. |
| 134 | `SC.SOO.INT.CTR` | `SecOpenOrder_IntCtr` | TField |  | Interest counter for the associated security, applicable to shares only. |
| 135 | `SC.SOO.SERVICE.REF` | `SecOpenOrder_ServiceRef` | TField |  | The service reference number if the SEC.OPEN.ORDER record was created through the service. |
| 136 | `SC.SOO.THREAD.KEY` | `SecOpenOrder_ThreadKey` | TField |  | The thread key if the SEC.OPEN.ORDER was created by the service. |
| 137 | `SC.SOO.TRADED.NOM` | `SecOpenOrder_TradedNom` |  |  |  |
| 138 | `SC.SOO.OUTSTAND.NOM` | `SecOpenOrder_OutstandNom` |  |  |  |
| 139 | `SC.SOO.TRADER.CODE` | `SecOpenOrder_TraderCode` | TField |  | Specifies the dealer of the trading department for the order. This will get defaulted from the ORDER.BY.CUST. Validation Rules: Should be a valid DEPT.ACCT.OFFICER |
| 140 | `SC.SOO.TRADER.DESC` | `SecOpenOrder_TraderDesc` |  |  |  |
| 141 | `SC.SOO.ROUT.SEC.ACC` | `SecOpenOrder_RoutSecAcc` | TField |  | Portfolio reference under the company to which order will be routed |
| 142 | `SC.SOO.ROUT.BROKER` | `SecOpenOrder_RoutBroker` | TField |  | Broker reference under the company to which order will be routed |
| 143 | `SC.SOO.ROUTED.ORDER.REF` | `SecOpenOrder_RoutedOrderRef` | TField |  | SEC.OPEN.ORDER reference under the routed company |
| 144 | `SC.SOO.IN.HOUSE.SEC.ACC` | `SecOpenOrder_InHouseSecAcc` | TField |  | Portfolio for which in house dealing transaction is done. External positions will be captured for Portfoliodefined in this field. |
| 145 | `SC.SOO.IN.HOUSE.CUSTODIAN` | `SecOpenOrder_InHouseCustodian` | TField |  | External custodian involved in inhouse dealing. If IN.HOUSE.SEC.ACC is defined, Custodian defined in this fieldwill maintain that portfolio. Custodian defined in this field must be a valid record in CUSTOMER.SECURITY with typeas Broker/counterparty. |
| 146 | `SC.SOO.STP.ORDER` | `SecOpenOrder_StpOrder` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 147 | `SC.SOO.AUTHORISE.TRADE` | `SecOpenOrder_AuthoriseTrade` | TField |  | To be set to YES if the corresponding SEC.TRADE needs to be authorised automatically. If this Field is set to YES and DEAL.STATUS is TRANSMITTED this value will be carried over to CorrespondingSC.EXE.SEC.ORDER Record. |
| 148 | `SC.SOO.PARENT` | `SecOpenOrder_Parent` | TField |  | Allowed value is YES This Field is to determine whether the order is a parent order |
| 149 | `SC.SOO.PARENT.REFERENCE` | `SecOpenOrder_ParentReference` | TField |  | This field will accept alphanumeric Value Unique parent reference that is common for both parent and child orders and will serve as a link. |
| 150 | `SC.SOO.REVERSE.CHILD` | `SecOpenOrder_ReverseChild` | TField |  | Allowed value is YES This Field is used to reverse the child transaction |
| 151 | `SC.SOO.EXE.HLT` | `SecOpenOrder_ExeHlt` | TField |  | Allowed options are YES,NO and NULL. YES will indicate whether the execution should be flagged for halt. NO willindicate execution should be processed without halt.On setting NULL then system will populate the value for EXE.HLTeithier from CUSTOMER.SERCURITY or SECURITY.MASTER |
| 152 | `SC.SOO.TRADE.HLT` | `SecOpenOrder_TradeHlt` | TField |  | Allowed options are YES,NO and NULL. YES will indicate whether the execution should be flagged for halt. NO willindicate execution should be processed without halt.On setting NULL then system will populate the value forTRADE.HLT eithier from CUSTOMER.SERCURITY or SECURITY.MASTER |
| 153 | `SC.SOO.AUTHORISE.CHILD` | `SecOpenOrder_AuthoriseChild` | TField |  | This field is used to specify whether child transactions can be authorised and will be defaulted fromAUTH.CHILD.ORDER field of SC.STD.SEC.TRADE only on initial input. In case of subsequent amendments afterauthorisation, this field has to be manually specified Manual amendment is possible. If this field is YES, Parent order should be kept in INAU so that T24 service willauthorise both child and parent. This field cannot be set as YES if there are no child transactions in exception This field will be used in conjunction with ORDER.EXCEP.CHECK field of SC.BULK.TRANS.MATCHING in which caseparent will not be allowed to authorise if child orders are in exception and Zero authoriser version cannot be used in this case This field will also be used in conjunction with BULK.UPDATE field in order to perform bulk update and thenauthorize parent and child Validation Rules Allowed values are YES, NO |
| 154 | `SC.SOO.DELETE.CHILD` | `SecOpenOrder_DeleteChild` | TField |  | This field is used to specify whether parent and child transactions are to be deleted. After inputting thisfield, order should be left in INAU so that service will delete the child and parent. Zero authoriser version cannot be usedin this case. This field cannot be set as YES if there are no child records in exception Validation Rules Allowed value is only YES |
| 155 | `SC.SOO.ROUNDING.FACTOR` | `SecOpenOrder_RoundingFactor` | TField |  | Minimum lot using which nominal will be executed. This will be defaulted from ORDER.BY.CUST. Value should be inmultiple of trading units and nominal in order should be in multiple of this field |
| 156 | `SC.SOO.MKT.IDN.CODE` | `SecOpenOrder_MktIdnCode` | TField |  | The swift market identifier code is defined in this field This field gets defaulted by reading the value in stock exchange in order and default the MIC from StockExchange. Validation Rules 1-4 Alphanumeric input |
| 157 | `SC.SOO.BULK.UPDATE` | `SecOpenOrder_BulkUpdate` | TField |  | This field is used to specify whether bulk update is to be performed from parent to child. This field cannot beinput if SC.BULK.UPDATE.PARAMETER is not set for SEC.OPEN.ORDER This field can also be used in conjunction with AUTHORISE.CHILD to determine whether transactions are to beauthorised after performing bulk update. Zero authoriser version cannot be used and transaction should be left in INAU. In orderto perform bulk update, all transaction should be in unauthorised status Validation Rules Allowed value is only YES |
| 158 | `SC.SOO.UPFRONT.SEC` | `SecOpenOrder_UpfrontSec` | TField |  | The field gets defaulted, from the UPFRONT.SEC field in SECURITY.MASTER, for Credit transactions. If this fieldis set, the position will be created for this security. /Validation Rules: This field is a NOCHANGE field |
| 159 | `SC.SOO.INTEG.DATA.ITEM` | `SecOpenOrder_IntegDataItem` |  |  |  |
| 160 | `SC.SOO.INTEG.DATA.VALUE` | `SecOpenOrder_IntegDataValue` |  |  |  |
| 161 | `SC.SOO.TXN.CHANNEL` | `SecOpenOrder_TxnChannel` | TField |  | Holds the information on mode of channel used to enter into the order.List of channels can be configured throughEB.LOOKUP with VIRTUAL.TABLE as SC.CHANNEL |
| 162 | `SC.SOO.SWITCH.ORDER` | `SecOpenOrder_SwitchOrder` | TField | Yes | This field determines the type of SWITCH order. Validation Rules: Allowed Values: INTRAFUND,INTERFUND Input is allowed for SWITCH orders alone. Mandatory Input for SWITCH order. |
| 163 | `SC.SOO.SWITCH.QTY` | `SecOpenOrder_SwitchQty` | TField | Yes | This field determines the target mode for INTRAFUND SWITCH order. Validation Rules: Allowed Values: UNIT,AMOUNT,PERCENTAGE Input is allowed for SWITCH orders alone. Mandatory Input for INTRAFUND SWITCH order. |
| 164 | `SC.SOO.COM.ORDER.MASTER` | `SecOpenOrder_ComOrderMaster` | TField |  | A value of YES will indicate that this is the Master Order in this switch.This will determine if the switch is Buy driven or Sell Driven. Only one Order in the group can be set as MASTER. Validation Rules: Allowed Values: YES or BLANK Input is allowed for SWITCH orders alone. |
| 165 | `SC.SOO.COM.ORDER.REF` | `SecOpenOrder_ComOrderRef` | TField | Yes | The field will hold a common reference to link a set of switch orders. Validation Rules: Input is allowed for SWITCH orders alone. Mandatory Input for SWITCH order. |
| 166 | `SC.SOO.COM.ORDER.COUNT` | `SecOpenOrder_ComOrderCount` | TField | Yes | This field will hold the total number of orders placed with the same reference. This will be used to handle Transmission checks for Intrafund order. Validation Rules: Input is allowed for SWITCH orders alone. Mandatory Input for Master Order. |
| 167 | `SC.SOO.ORDER.STATUS` | `SecOpenOrder_OrderStatus` | TField |  | This field will hold the status of order.Field will be updated from incoming message:MT509,MX-setr.016. Informatory Field. Validation Rules: Allowed Values:ACKNOWLEDGED,PASSED,FAILED,SUSPENDED |
| 168 | `SC.SOO.MUTUAL.FUND` | `SecOpenOrder_MutualFund` | TField |  | This field is used to identify if the order is for a Mutual Fund.Field will be updated from MUTUAL.FUND field in SECURITY.MASTER.Informatory Field Validation Rules: NOINPUT field |
| 169 | `SC.SOO.IPO.END.DATE` | `SecOpenOrder_IpoEndDate` | TField |  |  |
| 170 | `SC.SOO.TRANSMIT.DATE` | `SecOpenOrder_TransmitDate` | TField |  | Used to provide the possible transmission date of the order such that this order is settled on/after highest Sell Orders Settlement. Auto Populated, to reach highest settlement date of Sell Orders by identifying Settlement Days in the Buy Order. Allowed for manual edit. Validation Rules: Applicable only for InterFund switch orders |
| 171 | `SC.SOO.ORD.INV.OPT.TYPE` | `SecOpenOrder_OrdInvOptType` | TField |  | The field is used to store the Invest option type and will be used for order grouping. Informatory Field Validation Rules: NOINPUT field |
| 172 | `SC.SOO.CANCEL.TRADE.REF` | `SecOpenOrder_CancelTradeRef` | TField | Yes | Trade reference that is to be cancelled can be input in this field. Validation Rules: Mandatory if this is a Cancellation Order is set Parent Trades are not allowed for Cancellation Debit Trades are not allowed for Cancellation Multiple Customer Trades are not allowed for Cancellation |
| 173 | `SC.SOO.DECISION.MKR.ID` | `SecOpenOrder_DecisionMkrId` | TField |  |  |
| 174 | `SC.SOO.SEND.ORD.STATUS.ADV` | `SecOpenOrder_SendOrdStatusAdv` | TField |  |  |
| 175 | `SC.SOO.CUSTOMER.LEI.NCI` | `SecOpenOrder_CustomerLeiNci` |  |  |  |
| 176 | `SC.SOO.STATEMENT.NOS` | `SecOpenOrder_StatementNos` |  |  |  |
| 177 | `SC.SOO.OVERRIDE` | `SecOpenOrder_Override` |  |  |  |
| 178 | `SC.SOO.RECORD.STATUS` | `SecOpenOrder_RecordStatus` | String |  |  |
| 179 | `SC.SOO.CURR.NO` | `SecOpenOrder_CurrNo` | String |  |  |
| 180 | `SC.SOO.INPUTTER` | `SecOpenOrder_Inputter` |  |  |  |
| 181 | `SC.SOO.DATE.TIME` | `SecOpenOrder_DateTime` |  |  |  |
| 182 | `SC.SOO.AUTHORISER` | `SecOpenOrder_Authoriser` | String |  |  |
| 183 | `SC.SOO.CO.CODE` | `SecOpenOrder_CoCode` | String |  |  |
| 184 | `SC.SOO.DEPT.CODE` | `SecOpenOrder_DeptCode` | String |  |  |
| 185 | `SC.SOO.AUDITOR.CODE` | `SecOpenOrder_AuditorCode` | String |  |  |
| 186 | `SC.SOO.AUDIT.DATE.TIME` | `SecOpenOrder_AuditDateTime` | String |  |  |
| 187 | `SC.SOO.CHARGE.GROUP` | `SecOpenOrder_ChargeGroup` | TField |  | This field holds the generic charge group id of SCTR.GROUP.CONDITION record When the field is manually inputted with generic id that starts with G- followed by 6 Numeric values, SCTR.GROUP.CONDITION will be directly referred using this field value when the field is blank, CUSTOMER.CHARGE is read for the customer to get the SCTR.GROUP.CONDITION id from SC.ACT.GROUP field Validations User has to manually input this field to accept Generic group id of SCTR.GROUP.CONDITION table Value should be a valid record id from SCTR.GROUP.CONDITION record |
| 188 | `SC.SOO.FACILITY.FUNDED` | `SecOpenOrder_FacilityFunded` | TField |  |  |
| 189 | `SC.SOO.LEI.NCI.CHK.REQ` | `SecOpenOrder_LeiNciChkReq` | TField |  |  |
