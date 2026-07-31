# DX.ORDER — Table Schema

> Source: `INSERTS/I_F.DX.ORDER` in `DX_Order.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.ORD.CONTRACT.CODE` | `DxOrder_ContractCode` | TField | Yes | The Contract CODE for this trade, as per the information in DX.CONTRACT.MASTER. Choose from the drop down menu list, the Contract applicable to the trade dealt. Validation Rules: Up to 12 alphanumeric characters, input must exist on DX.CONTRACT.MASTER Mandatory input field |
| 2 | `DX.ORD.EXCHANGE.CODE` | `DxOrder_ExchangeCode` | TField |  | The name of the Exchange where the applicable contract is traded. Validation Rules: Up to 10 alpha characters available Auto populated field by information stored in DX.EXCHANGE.MASTER under the CONTRACT.ID. No Change Field |
| 3 | `DX.ORD.SUB.ASSET.TYPE` | `DxOrder_SubAssetType` | TField |  | Identifies the group of like Securities, which are reported together. Validation Rules: Up to 5 numeric characters, input must exist on SUB.ASSET.TYPE No Change Field |
| 4 | `DX.ORD.TRADE.STATUS` | `DxOrder_TradeStatus` | TField |  | The status of the trade in the system, 'NO INPUT' field updated by other applications. Validation Rules: No Input Field. Will default to either ACTIVE/INACTIVE |
| 5 | `DX.ORD.TRADE.DATE` | `DxOrder_TradeDate` | TField |  | The date on which the actual trade takes place, 'Contractual Execution Date'. Validation Rules: Up to 11 characters in DATE format If field is left Null the default is Today's Date The date cannot exceed the trade date. |
| 6 | `DX.ORD.MATURITY.DATE` | `DxOrder_MaturityDate` | TField | Yes | The delivery period or prompt date of the contract transacted. Validation Rules: Up to 11 characters in DATE format The field CONTRACT.ID and TRADE.DATE must be populated with a valid maturity date and prior to this field Must be in the format: MONTHLY TRADES = Month/Year e.g. SEP00 DAILY TRADES = Day/Month/Year e.g. 15SEP00 The date must be greater than the Trade Date Mandatory Field |
| 7 | `DX.ORD.INP.MAT.DATE` | `DxOrder_InpMatDate` | TField |  | Holds the T24 internal maturity date returned from DX.VAL.PERIOD. Validation Rules: Up to 11 characters in DATE format No Input Field |
| 8 | `DX.ORD.TRADE.TYPE` | `DxOrder_TradeType` | TField | Yes | The type of contract that has been traded on an exchange, FUTURE, OPTION or STOCK. Validation Rules: Up to 6 alpha characters Auto populated field by information stored in DX.CONTRACT.MASTER under the CONTRACT.ID. Will default to FUTURE/OPTION/STOCK No Change Field Mandatory Input |
| 9 | `DX.ORD.DEC.DATE` | `DxOrder_DecDate` | TField |  | The Last Date by which a customer may exercise an option. The exercise date (European Options) or last exercise date (American Options) for this contract. Validation Rules: Up to 11 date format characters available. Input should default if CONTRACT.TYPE is "OPTION" Date Formula "+3WE,-1BD" = 3 |
| 10 | `DX.ORD.CONTRACT.CCY` | `DxOrder_ContractCcy` | TField |  | The currency of the contract traded. Validation Rules: No Input Field Default from DX.CONTRACT.MASTER CURRENCY |
| 11 | `DX.ORD.TRADE.CCY` | `DxOrder_TradeCcy` | TField | Yes | - the user-defined alpha currency code - the user-defined numeric currency code Validation Rules: Alpha format - This code will then comprise three alpha characters as defined in the currency table. It is recommended to use the standard SWIFT currency code. The following are examples of ISO/SWIFT codes: - USD = US Dollars - GBP = Pounds Sterling - DEM = Deutsche Marks - FRF = French Francs Numeric format - In most Treasury operations, certain currencies are traded more often that others. To continually enter a three alpha character code would be unnecessarily time consuming. Currencies may therefore be given a numeric ranking between 1 and 999 on the Currency table. If USD is the most frequently traded currency it should have a numeric code of 1. Entering 1 will then access the details of US dollars from the Currency table. 3 characters (uppercase alpha) - type SSS or 1-3 numeric characters Currency Code (Mandatory input) The currency code entered must appear on the Currency table. Dealing between LU'X' and BE'X' currency codes is prohibited. |
| 12 | `DX.ORD.TRANSFER.TYPE` | `DxOrder_TransferType` | TField |  | The type of trade executed via a broker and the process route it takes to be cleared for the bank's account. Choose from drop down menu 'GIVEUP', 'GIVEIN', 'TRANSFERS' and 'SWITCH'. GIVEUP; Term used in a transaction involving 3 brokers, Broker A, a floor broker, executes a buy order for broker B, another member firm broker who has too much business at the time to execute the order. The broker whom Broker A completes the transaction(the sell side broker) is Broker C. Broker A "Gives Up" the name of Broker B, so that the record shows a transaction between Broker B and Broker C even though the trade was actually executed between Broker A and Broker C. GIVEIN: Term used for the execution of a transaction by a broker to the floor member firm. TRANSFER: Term used to movement of transactions from one account to another. SWITCH: Selling Stock and Bonds to replace them with other Stocks and Bonds with better prospects for gain or higher yields. Validation Rules: Input must be one of the following :EXECUTION/CLEARING/BOTH./TRANSFER/SWITCH |
| 13 | `DX.ORD.EXECUTING.BROKER` | `DxOrder_ExecutingBroker` | TField |  | The Broker Whom Executed the trade on the Bank's behalf. Validation Rules: Up to 10 alpha characters, input must exist on DX.CUSTOMER with a CUSTOMER.TYPE = &amp;#145;BROKER&amp;#146; |
| 14 | `DX.ORD.OPTION.TYPE` | `DxOrder_OptionType` | TField |  | Choose the type of option from the drop down menu 'CALL' or 'PUT' CALL: Confers upon the holder the right, but not obligation, to BUY stock at a fixed price at a future date PUT: Confers upon the holder the right, but not obligation, to SELL stock at a fixed price at a future date Validation Rules: Up to 4 alpha characters No Input unless TRADE.TYPE = "OPTION" Input must be either CALL/PUT |
| 15 | `DX.ORD.OPTION.STYLE` | `DxOrder_OptionStyle` | TField | No | Defines the rule of settlement of an option according to the type populated in this field. The type is chosen from the drop down menu: AMERICAN: An option that may be exercised at any time prior to its expiry date EUROPEAN: An option that may only be exercised on its expiry date. Validation Rules: An input field for FX-OTC options. Will default to either : AMERICAN/EUROPEAN/CARRIBEAN Field Defaults from DX.CONTRACT.MASTER field OPTION.STYLE For FX-OTC Options alone, user input is allowed. A NOCHANGE field with additional optional definition of CARRIBEAN |
| 16 | `DX.ORD.STRIKE.QUOTE.CCY` | `DxOrder_StrikeQuoteCcy` | TField |  |  |
| 17 | `DX.ORD.STRIKE.QUOTE` | `DxOrder_StrikeQuote` | TField |  |  |
| 18 | `DX.ORD.STRIKE.PRICE` | `DxOrder_StrikePrice` | TField |  | The price at which an option holder has the right to buy (Call Options) or sell (Put Options) the underlying instrument, or to cash-settle the option if appropriate, to exercise the option. Validation Rules: Up to 19 numeric characters available No input unless Trade Type is 'OPTION'. |
| 19 | `DX.ORD.INT.STRIKE.PRICE` | `DxOrder_IntStrikePrice` | TField |  | Price format for T24 calculation. No Input required. Validation Rules: Up to 19 numeric characters No Input Field &amp;#150; calculations will default into the field |
| 20 | `DX.ORD.PREMIUM.DUE` | `DxOrder_PremiumDue` | TField |  | Premium, The amount by which a futures or option contract is priced above either: The theoretical or 'fair' value of the contract or the 'futures equivalent' or 'cash' price of the underlying instrument. Validation Rules: Up to 10 alpha characters Defaulted by information stored in DX.EXCHANGE.MASTER under the PREM.POST.TIME No Input unless TRADE.TYPE = "OPTION" |
| 21 | `DX.ORD.CURRENCY.MARKET` | `DxOrder_CurrencyMarket` | TField | Yes | The system recognizes the need for a number of different markets within one currency. For this reason this field identifies which Exchange Rate Currency Market is accessed for this transaction. The system caters for the need to have more than one market within a given currency. The use of this field will only be applicable for those countries where the exchange market defines different rates for the same foreign Currency according to rules determined by the local authorities or local central bank. A typical example would be Belgium where foreign currencies are quoted on the Regular Market and also on the Free Market. Different sets of exchange rates will exist for these two markets. If default movement is not specified as 'DX', then if DEAL movement type has been specified on MU.TXN.GRP.CCY.MKT the market specified will be defaulted ito this field and the field will be made no input. If neither 'DX' is set or DEAL movement is specified, then input is mandatory in this field and may not be changed after authorisation. It is possible to specify separate markets to be used for COMM.CHRG and BROKERAGE. Any commission or change entries generated will use the specified market for COMM.CHRG if set up and similary BROKERAGE entries will use the BROKERAGE market if set up. If not set up the DEFAULT MOVEMENT currency market will be taken. The system allows the user to view the Foreign Exchange position by currency market when more than one market is applicable. Validation Rules: 1 numeric The market entered must appear on the Currency Market table. This field cannot be changed after authorisation. The market must exist on the local CURRENCY record. The market must exist on the CURRENCY record for both BUY and SELLCCY. |
| 22 | `DX.ORD.POSITION.TYPE` | `DxOrder_PositionType` | TField |  | POSITION.TYPE NO input Default to &amp;#145;TR&amp;#146;. Validation Rules: Rule 1 Default to TR Rule 2 No Input |
| 23 | `DX.ORD.CONTRACT.TIME` | `DxOrder_ContractTime` | TField |  | The time this trade was executed. Validation Rules: Up to 9 time characters in TIME format Default to current time if permitted by DX.PARAMETER under DEFAULT.TIME. |
| 24 | `DX.ORD.DEALER.DESK` | `DxOrder_DealerDesk` | TField |  | The Dealer ID for this executed trade. Validation Rules: Up to 2 alpha characters Input must exist on DEALER.DESK |
| 25 | `DX.ORD.DEPT.ACCT.OFFICER` | `DxOrder_DeptAcctOfficer` | TField |  | Department or Account officer ID. If 'DEALER.DESK' is populated the default will apply. Validation Rules: Up to 4 numeric characters Input must exist in DEP.ACCT.OFFICER |
| 26 | `DX.ORD.NARRATIVE` | `DxOrder_Narrative` |  |  |  |
| 27 | `DX.ORD.EXTERNAL.REF` | `DxOrder_ExternalRef` |  |  |  |
| 28 | `DX.ORD.DLV.CCY` | `DxOrder_DlvCcy` | TField |  | Contract currency. No input, default from DX.CONTRACT.MASTER 'Delivery currency' Validation Rules: No Input field |
| 29 | `DX.ORD.REGION` | `DxOrder_Region` | TField |  | Each exchange is uniquely associated with a REGION. Regions are associated with exchanges to identify record in holiday application for trading calendars. Defaulted from DX.EXCHANGE.MASTER. |
| 30 | `DX.ORD.VALUATION.PRICE` | `DxOrder_ValuationPrice` | TField |  | The last price used to calculate the variation margin for the trade Validation Rules: Input is defaulted from DX.RUN.REVALUE Up to 19 numeric characters No Input |
| 31 | `DX.ORD.ORDER.AMEND` | `DxOrder_OrderAmend` | TField |  | Once this field is set to 'YES' the order behaves as amendment order and not as a fill order and on authorisation doesn't create trade. The fields LIMIT.TYPE, LIMIT.PRICE, LIMIT.DATE, ORDER.TYPE and ORDER.LOTS becomes inputtable when this field is set to YES and fill in secondary side are not allowed. Validation Rules: Allowed value is YES or null |
| 32 | `DX.ORD.PRI.PRICE` | `DxOrder_PriPrice` | TField |  | Price per unit of lot/lots traded. For 'OPTION' trades, this denotes the 'PREMIUM' price in TRADE currency. Default from Secondary side price. Validation Rules: 1-19 numeric characters (0-6 integers and 0-9 decimals) No input field. |
| 33 | `DX.ORD.PRI.INT.PRICE` | `DxOrder_PriIntPrice` | TField |  | Standard T24 price format. Validation Rules: Up to 19 numerical characters available NOINPUT |
| 34 | `DX.ORD.PRI.TRADE.COST` | `DxOrder_PriTradeCost` | TField |  | The cost of this trade by calculating the price or premium multiplied by the total number of lots. Validation Rules: Calculation is based on (Price/premium * total number of Lots) No Input Field Up to 19 numeric characters |
| 35 | `DX.ORD.PRI.BUY.SELL` | `DxOrder_PriBuySell` | TField |  | Indicates if the primary counterparty is Buying or Selling a trade. Validation Rules: Multi-value field. Uo to 4 alphanumeric characters. No Input Field &amp;#150; set automatically |
| 36 | `DX.ORD.PRI.CUST.NO` | `DxOrder_PriCustNo` |  |  |  |
| 37 | `DX.ORD.PRI.SEC.ACC` | `DxOrder_PriSecAcc` |  |  |  |
| 38 | `DX.ORD.PRI.CUST.TYPE` | `DxOrder_PriCustType` |  |  |  |
| 39 | `DX.ORD.PRI.CUST.STATUS` | `DxOrder_PriCustStatus` |  |  |  |
| 40 | `DX.ORD.PRI.ACCOUNT` | `DxOrder_PriAccount` |  |  |  |
| 41 | `DX.ORD.PRI.LOTS` | `DxOrder_PriLots` |  |  |  |
| 42 | `DX.ORD.PRI.ORIG.LOTS` | `DxOrder_PriOrigLots` |  |  |  |
| 43 | `DX.ORD.PRI.SETTNOS` | `DxOrder_PriSettnos` |  |  |  |
| 44 | `DX.ORD.PRI.SETTLOTS` | `DxOrder_PriSettlots` |  |  |  |
| 45 | `DX.ORD.PRI.OPEN.CLOSE` | `DxOrder_PriOpenClose` |  |  |  |
| 46 | `DX.ORD.PRI.HEDGE.TRADE` | `DxOrder_PriHedgeTrade` |  |  |  |
| 47 | `DX.ORD.PRI.LINK` | `DxOrder_PriLink` |  |  |  |
| 48 | `DX.ORD.PRI.ALLOW.SETT` | `DxOrder_PriAllowSett` |  |  |  |
| 49 | `DX.ORD.PRI.STRATEGY` | `DxOrder_PriStrategy` |  |  |  |
| 50 | `DX.ORD.PRI.EXCHANGE.TYPE` | `DxOrder_PriExchangeType` |  |  |  |
| 51 | `DX.ORD.PRI.CHANNEL` | `DxOrder_PriChannel` |  |  |  |
| 52 | `DX.ORD.PRI.AUTO.MANUAL` | `DxOrder_PriAutoManual` |  |  |  |
| 53 | `DX.ORD.PRI.COMM.TYP` | `DxOrder_PriCommTyp` |  |  |  |
| 54 | `DX.ORD.PRI.COMM.CDE` | `DxOrder_PriCommCde` |  |  |  |
| 55 | `DX.ORD.PRI.COMM.PRC` | `DxOrder_PriCommPrc` |  |  |  |
| 56 | `DX.ORD.PRI.COMM.CCY` | `DxOrder_PriCommCcy` |  |  |  |
| 57 | `DX.ORD.PRI.COMM.AMT` | `DxOrder_PriCommAmt` |  |  |  |
| 58 | `DX.ORD.PRI.COMM.ACC` | `DxOrder_PriCommAcc` |  |  |  |
| 59 | `DX.ORD.PRI.CACC.CCY` | `DxOrder_PriCaccCcy` |  |  |  |
| 60 | `DX.ORD.PRI.COMM.EXC` | `DxOrder_PriCommExc` |  |  |  |
| 61 | `DX.ORD.PRI.CACC.AMT` | `DxOrder_PriCaccAmt` |  |  |  |
| 62 | `DX.ORD.PRI.COMM.TAX` | `DxOrder_PriCommTax` |  |  |  |
| 63 | `DX.ORD.PRI.CHARGE.DATE` | `DxOrder_PriChargeDate` |  |  |  |
| 64 | `DX.ORD.PRI.TAX.CODE` | `DxOrder_PriTaxCode` |  |  |  |
| 65 | `DX.ORD.PRI.TAX.TYPE` | `DxOrder_PriTaxType` |  |  |  |
| 66 | `DX.ORD.TAX.AMT.ACY` | `DxOrder_TaxAmtAcy` |  |  |  |
| 67 | `DX.ORD.TAX.AMT.TCY` | `DxOrder_TaxAmtTcy` |  |  |  |
| 68 | `DX.ORD.PRI.PREMIUM.CCY` | `DxOrder_PriPremiumCcy` |  |  |  |
| 69 | `DX.ORD.PRI.PREM.PRICE` | `DxOrder_PriPremPrice` |  |  |  |
| 70 | `DX.ORD.PRI.PREM.EXCH.RATE` | `DxOrder_PriPremExchRate` |  |  |  |
| 71 | `DX.ORD.PRI.TOTAL.PREM.AMT` | `DxOrder_PriTotalPremAmt` |  |  |  |
| 72 | `DX.ORD.PRI.REF.CCY` | `DxOrder_PriRefCcy` |  |  |  |
| 73 | `DX.ORD.PRI.ACC.CCY` | `DxOrder_PriAccCcy` |  |  |  |
| 74 | `DX.ORD.PRI.EX.RATE.REF` | `DxOrder_PriExRateRef` |  |  |  |
| 75 | `DX.ORD.PRI.EX.RATE.ACC` | `DxOrder_PriExRateAcc` |  |  |  |
| 76 | `DX.ORD.PRI.DLV.AMT` | `DxOrder_PriDlvAmt` |  |  |  |
| 77 | `DX.ORD.PRI.NET.COST` | `DxOrder_PriNetCost` |  |  |  |
| 78 | `DX.ORD.PRI.PREM.EXC` | `DxOrder_PriPremExc` |  |  |  |
| 79 | `DX.ORD.PRI.DLV.KEY` | `DxOrder_PriDlvKey` |  |  |  |
| 80 | `DX.ORD.PRI.TRANS.KEY` | `DxOrder_PriTransKey` |  |  |  |
| 81 | `DX.ORD.PRI.ORDER.NO` | `DxOrder_PriOrderNo` |  |  |  |
| 82 | `DX.ORD.PRI.NARR` | `DxOrder_PriNarr` |  |  |  |
| 83 | `DX.ORD.PRI.CONSTRAINT` | `DxOrder_PriConstraint` |  |  |  |
| 84 | `DX.ORD.PRI.CHG.OFFSET` | `DxOrder_PriChgOffset` |  |  |  |
| 85 | `DX.ORD.PRI.CUST.REF` | `DxOrder_PriCustRef` |  |  |  |
| 86 | `DX.ORD.PRI.PND.SETT` | `DxOrder_PriPndSett` |  |  |  |
| 87 | `DX.ORD.PRI.PND.LOTS` | `DxOrder_PriPndLots` |  |  |  |
| 88 | `DX.ORD.PRI.LIMIT.REF` | `DxOrder_PriLimitRef` |  |  |  |
| 89 | `DX.ORD.PRI.PREM.TXN` | `DxOrder_PriPremTxn` |  |  |  |
| 90 | `DX.ORD.PRI.PREM.PST` | `DxOrder_PriPremPst` |  |  |  |
| 91 | `DX.ORD.PRI.IM.AMT` | `DxOrder_PriImAmt` |  |  |  |
| 92 | `DX.ORD.PRI.IM.ACC` | `DxOrder_PriImAcc` |  |  |  |
| 93 | `DX.ORD.PRI.RT.COMPANY` | `DxOrder_PriRtCompany` |  |  |  |
| 94 | `DX.ORD.PRI.RT.PORT.ID` | `DxOrder_PriRtPortId` |  |  |  |
| 95 | `DX.ORD.PRI.RT.WHEN` | `DxOrder_PriRtWhen` |  |  |  |
| 96 | `DX.ORD.PRI.RT.LINK` | `DxOrder_PriRtLink` |  |  |  |
| 97 | `DX.ORD.PRI.ENTITLE` | `DxOrder_PriEntitle` |  |  |  |
| 98 | `DX.ORD.PRI.OVE.ADDR` | `DxOrder_PriOveAddr` |  |  |  |
| 99 | `DX.ORD.PRI.MESS.CTL` | `DxOrder_PriMessCtl` |  |  |  |
| 100 | `DX.ORD.PRI.PREM.OFFSET` | `DxOrder_PriPremOffset` |  |  |  |
| 101 | `DX.ORD.PRI.BEN.NO` | `DxOrder_PriBenNo` |  |  |  |
| 102 | `DX.ORD.PRI.BEN.ADD` | `DxOrder_PriBenAdd` |  |  |  |
| 103 | `DX.ORD.PRI.CPY.NO` | `DxOrder_PriCpyNo` |  |  |  |
| 104 | `DX.ORD.PRI.CPY.ADD` | `DxOrder_PriCpyAdd` |  |  |  |
| 105 | `DX.ORD.PRI.CPY.BNK.ACC` | `DxOrder_PriCpyBnkAcc` |  |  |  |
| 106 | `DX.ORD.PRI.INTR.BK.NO` | `DxOrder_PriIntrBkNo` |  |  |  |
| 107 | `DX.ORD.PRI.INTR.ADD` | `DxOrder_PriIntrAdd` |  |  |  |
| 108 | `DX.ORD.PRI.CONF.NAR` | `DxOrder_PriConfNar` |  |  |  |
| 109 | `DX.ORD.PRI.PYMT.NAR` | `DxOrder_PriPymtNar` |  |  |  |
| 110 | `DX.ORD.PRI.RCAD.NAR` | `DxOrder_PriRcadNar` |  |  |  |
| 111 | `DX.ORD.PRI.BK2BK.IN` | `DxOrder_PriBk2bkIn` |  |  |  |
| 112 | `DX.ORD.SEC.CUST.NO` | `DxOrder_SecCustNo` | TField | Yes | Broker number. Must exsist in both CUSTOMER and DX.CUSTOMER. Validation Rules: No-input until the order has been authorised Mandatory input if this order has been authorised at least once. |
| 113 | `DX.ORD.SEC.SEC.ACC` | `DxOrder_SecSecAcc` | TField | Yes | Portfolio ID. must be 'owned' by customer defined in CUST.NUMBER Validation Rules: No-input until the order has been authorised Mandatory input if this record has been authorised at least once. Default value = the NOSTRO.ACCOUNT for the Trade Currency Must be the Id of a valid Account Trading on portfolio allowed only in the company mentioned in PORT.COMP.ID of SEC.ACC.MASTER |
| 114 | `DX.ORD.SEC.CUST.TYPE` | `DxOrder_SecCustType` | TField |  | Default from DX.CUSTOMER field CUSTOMER.TYPE. Validation Rules: No Input Default from DX.CUSTOMER. Up to 15 alphanumeric characters available |
| 115 | `DX.ORD.SEC.CUST.STATUS` | `DxOrder_SecCustStatus` | TField |  | A No Input field default from DX.CUSTOMER field Trading .status Validation Rules: Default from DX.CUSTOMER field Trading .status No Input Field Up to 10 alphanumeric characters available |
| 116 | `DX.ORD.SEC.ACCOUNT` | `DxOrder_SecAccount` | TField | Yes | For OWN BOOK portfolios (SAM.DEALER.BOOK field not null), construct internal accounty code as follows: TRADE.CCY:(SAM.ASSET.CAT):INT.DEPT.CODE Where SAM ASSET.CAT is rhe contents of the ASSET.CAT field from SAM. INT.DEPT.CODE is hard-coded to "0001" ASSR.CAT may be "CRF00" in which case it is an indicator only and not a valid internal account category code. Do not allow manual override of ACCOUNT field for dealer book portfolios. Enrich with the account SHORT.NAME where valid account is used. Validation Rules: Mandatory input if this record has been authorised at least once. No-input until the order has been authorised Up to 16 alphanumeric characters available |
| 117 | `DX.ORD.SEC.BUY.SELL` | `DxOrder_SecBuySell` | TField |  | Indicates whether the Broker is buying or selling the transaction. Opposite of Primary side BUY or SELL flag. Validation Rules: Multi-value field. Opposite of client side BUY or SELL flag No Input Field &amp;#150; set automatically Up to 4 alphanumeric characters available |
| 118 | `DX.ORD.SEC.LOTS` | `DxOrder_SecLots` | TField | Yes | Number of lots on this trade for the Secondary Customer (broker/client). Format to number of Contract.Dps held in DX.CONTRACT.MASTER. No-input until this record has been authorised Validation Rules: Format to the decimals set in CONTRACT.DPS under DX.CONTRACT.MASTER Multi-value set field No Input Field Mandatory if this record has been authorised at least once. |
| 119 | `DX.ORD.SEC.ORIG.LOTS` | `DxOrder_SecOrigLots` | TField |  | Number of lots originally transacted on this trade for the broker/client. Set when the trade lots was initially populated with a figure, decreases with settlements/close outs or option action. Validation Rules: Format to the decimals set in CONTRACT.DPS under DX.CONTRACT.MASTER Multi-value set field No Input Field |
| 120 | `DX.ORD.SEC.SETTNOS` | `DxOrder_SecSettnos` |  |  |  |
| 121 | `DX.ORD.SEC.SETTLOTS` | `DxOrder_SecSettlots` |  |  |  |
| 122 | `DX.ORD.SEC.PRICE` | `DxOrder_SecPrice` | TField |  | Price per unit of lot/lots traded. For 'OPTION' trades, this denotes the 'PREMIUM' price in TRADE currency Validation Rules: 1-19 numeric characters (0-6 integers and 0-9 decimals) |
| 123 | `DX.ORD.SEC.INT.PRICE` | `DxOrder_SecIntPrice` | TField |  | Standard T24 price format including contract size i.e. price per lot, not price per underlying unit Validation Rules: Multi-value set field No Input Field |
| 124 | `DX.ORD.SEC.TRADE.COST` | `DxOrder_SecTradeCost` | TField |  | The cost of this trade by calculating the price or premium multiplied by the total number of lots, i.e SEC.PRICE*SEC.LOTS. Validation Rules: No Input Field Calculated using the following formula: Price/Premium * total number of lots |
| 125 | `DX.ORD.SEC.OPEN.CLOSE` | `DxOrder_SecOpenClose` | TField |  | The Open or Close of a transaction, information to Notify an Exchange of the status of the transaction and calculation of the commission. Choose from the drop down menu 'OPEN' or 'CLOSE'. Validation Rules: No-input until the order has been authorised Up to 5 alpha characters available &amp;#150; input must be either OPEN/CLOSE |
| 126 | `DX.ORD.SEC.HEDGE.TRADE` | `DxOrder_SecHedgeTrade` | TField |  | Defines trade as hedging or speculative transaction. Very important - Is this a Hedge or Trade (Speculative) transaction? Choose from the drop down menu 'HEDGE' or 'TRADE' HEDGE: A transaction tending to the opposite effect of another transaction, engaged in to minimise loss on the latter. TRADE: Dealing in a commodity or financial asset with a view to obtaining a profit on the prospective change in the market value of the item in question. Validation Rules: No-input until the order has been authorised. Up to 5 alpha character available &amp;#150; input must be either HEDGE/TRADE Controls accounting treatment for the Profit and Loss If left Null, the field will default to 'TRADE' Controls accounting treatment of P&amp;L |
| 127 | `DX.ORD.SEC.LINK` | `DxOrder_SecLink` |  |  |  |
| 128 | `DX.ORD.SEC.ALLOW.SETT` | `DxOrder_SecAllowSett` | TField |  | Is this trade authorised for settlement or close out? Choose from the drop down menu 'Y' (YES) or 'N' (NO). Validation Rules: No Input until this order has been authorised. Up to 1 alpha character allowed. If not populated or left blank/null the default is 'Y'. If HEDGE.TRADE is populated with "HEDGE" than no input is necessary as the Default is set to 'N'. |
| 129 | `DX.ORD.SEC.STRATEGY` | `DxOrder_SecStrategy` | TField |  | The Trading Strategy on futures or stock transactions for reporting purposes. e.g. Straddle, Strangle, Butterfly, Spreads, etc&amp;#133;. Validation Rules: Up to 35 alpha characters &amp;#150; input must exist in DX.STRATEGY Multi-value field No-input until the order has been authorised |
| 130 | `DX.ORD.SEC.AUTO.MANUAL` | `DxOrder_SecAutoManual` | TField |  | Automatically generated or Manual commission entry. Validation Rules: AUTOMATIC-MANUAL Default to AUTOMATIC No Input until this order has been authorised. Up to 9 alphanumeric characters available |
| 131 | `DX.ORD.SEC.COMM.TYP` | `DxOrder_SecCommTyp` |  |  |  |
| 132 | `DX.ORD.SEC.COMM.CDE` | `DxOrder_SecCommCde` |  |  |  |
| 133 | `DX.ORD.SEC.COMM.PRC` | `DxOrder_SecCommPrc` |  |  |  |
| 134 | `DX.ORD.SEC.COMM.CCY` | `DxOrder_SecCommCcy` |  |  |  |
| 135 | `DX.ORD.SEC.COMM.AMT` | `DxOrder_SecCommAmt` |  |  |  |
| 136 | `DX.ORD.SEC.COMM.ACC` | `DxOrder_SecCommAcc` |  |  |  |
| 137 | `DX.ORD.SEC.CACC.CCY` | `DxOrder_SecCaccCcy` |  |  |  |
| 138 | `DX.ORD.SEC.COMM.EXC` | `DxOrder_SecCommExc` |  |  |  |
| 139 | `DX.ORD.SEC.CACC.AMT` | `DxOrder_SecCaccAmt` |  |  |  |
| 140 | `DX.ORD.SEC.COMM.TAX` | `DxOrder_SecCommTax` |  |  |  |
| 141 | `DX.ORD.SEC.CHARGE.DATE` | `DxOrder_SecChargeDate` | TField |  | The date on which to charge commissions, fees, and taxes. Choose from the drop down menu of 'TRADE' or 'SETTLEMENT' to populated this field. Default from DX.CONTRACT.MASTER. Validation Rules: Up to 10 alpha characters available No-input until the order has been authorised. |
| 142 | `DX.ORD.SEC.TAX.CODE` | `DxOrder_SecTaxCode` |  |  |  |
| 143 | `DX.ORD.SEC.TAX.TYPE` | `DxOrder_SecTaxType` |  |  |  |
| 144 | `DX.ORD.SEC.TAX.AMT.ACY` | `DxOrder_SecTaxAmtAcy` |  |  |  |
| 145 | `DX.ORD.SEC.TAX.AMT.TCY` | `DxOrder_SecTaxAmtTcy` |  |  |  |
| 146 | `DX.ORD.SEC.PREMIUM.CCY` | `DxOrder_SecPremiumCcy` |  |  |  |
| 147 | `DX.ORD.SEC.PREM.PRICE` | `DxOrder_SecPremPrice` |  |  |  |
| 148 | `DX.ORD.SEC.PREM.EXCH.RATE` | `DxOrder_SecPremExchRate` |  |  |  |
| 149 | `DX.ORD.SEC.TOTAL.PREM.AMT` | `DxOrder_SecTotalPremAmt` |  |  |  |
| 150 | `DX.ORD.SEC.REF.CCY` | `DxOrder_SecRefCcy` | TField |  | SEC.ACC.MASTER level reference currency. Validation Rules: No Input, field defaults from SEC.ACC.MASTER No-input until the order has been authorised. |
| 151 | `DX.ORD.SEC.ACC.CCY` | `DxOrder_SecAccCcy` | TField |  | Currency of specified secondary customer account. Validation Rules: Up to 3 characters CCY. NO INPUT. |
| 152 | `DX.ORD.SEC.EX.RATE.REF` | `DxOrder_SecExRateRef` | TField |  | Exchange rate to customer account currency Validation Rules: 19 figures for AMT No Input, field defaults with the Exchange rate from the trade CCY to the Customer Ref CCY |
| 153 | `DX.ORD.SEC.EX.RATE.ACC` | `DxOrder_SecExRateAcc` | TField |  | Exchange rate from trade ccy to secondary customer account ccy. Validation Rules: 19 figures for AMT No Input, field defaults with the Exchange rate from the trade CCY to the Customer Ref CCY |
| 154 | `DX.ORD.SEC.ORDER.NO` | `DxOrder_SecOrderNo` |  |  |  |
| 155 | `DX.ORD.SEC.NARR` | `DxOrder_SecNarr` |  |  |  |
| 156 | `DX.ORD.SEC.CONSTRAINT` | `DxOrder_SecConstraint` |  |  |  |
| 157 | `DX.ORD.SEC.DLV.AMT` | `DxOrder_SecDlvAmt` | TField |  | Delivery currency amount-'secondary ccy' amount for FOREX options/futures. Validation Rules: Up to 19 numeric characters. |
| 158 | `DX.ORD.SEC.NET.COST` | `DxOrder_SecNetCost` | TField |  | This is the cost to the secondary customer expressed in trade currency equivalent. The net cost is calculated as (Lots * Sec. Int. Price) +/- (Commissions and Charges) Validation Rules: No input field |
| 159 | `DX.ORD.SEC.PREM.EXC` | `DxOrder_SecPremExc` | TField |  | Specifies the treasury rate or the exchange rate of the two currencies involved in the trade. For FX OTC trade is the rate between the Premium currency and Account currency whereas for other type of trades it is rate between the Trade currency and Account currency. If customer type of DX.TRADE matches the customer type specified in SPECIAL.RATE field of DX.PARAMETER then this field holds the treasury rate of the two currencies. If customer type of DX.TRADE doesn�t matches the customer type specified in SPECIAL.RATE field) of DX.PARAMETER then this field holds the exchange rate of the two currencies. Validation rules: Up to 11 numeric values. |
| 160 | `DX.ORD.SEC.DLV.KEY` | `DxOrder_SecDlvKey` |  |  |  |
| 161 | `DX.ORD.SEC.TRANS.KEY` | `DxOrder_SecTransKey` | TField |  | Transaction generated by this leg of the trade Validation Rules: No Input Field &amp;#150; input will default from DX.TRANSACTION Up to 35 alphanumeric characters. |
| 162 | `DX.ORD.SEC.CHG.OFFSET` | `DxOrder_SecChgOffset` | TField |  | Days offset to apply to CHG.POST. This defaults from the value in DX.CONTRACT.MASTER. Validation Rules: NO INPUT until this order has been authorised. Up to 3 characters This field defaults from the value in DX.CONTRACT.MASTER |
| 163 | `DX.ORD.SEC.CUST.REF` | `DxOrder_SecCustRef` | TField |  | Secondary Customer reference field. Validation Rules: Up to 16 characters NO INPUT until this order has been authorised |
| 164 | `DX.ORD.SEC.PND.SETT` | `DxOrder_SecPndSett` |  |  |  |
| 165 | `DX.ORD.SEC.PND.LOTS` | `DxOrder_SecPndLots` |  |  |  |
| 166 | `DX.ORD.SEC.LIMIT.REF` | `DxOrder_SecLimitRef` | TField |  | The limit reference identifying which Customer credit line to update. If no input is made in this field the Limits system will provide a default according to the LIMIT.REFERENCE record which has its field Application identifier set to DX.TRADE-SEC. The suffix -SEC is used by DX.TRADE to distinguish when a customer exists on the secondary side of the trade. If no match is found in the selective reference(s) the default will be the reference which is set to blank. The amount used to update limits is controlled by the selection field ,LIM.AMT.VAL.CONT, on DX.PARAMETER. No input field |
| 167 | `DX.ORD.SEC.PREM.TXN` | `DxOrder_SecPremTxn` |  |  |  |
| 168 | `DX.ORD.SEC.PREM.PST` | `DxOrder_SecPremPst` |  |  |  |
| 169 | `DX.ORD.SEC.IM.AMT` | `DxOrder_SecImAmt` | TField |  | Amount of Inital Margin charged for this leg of the order/trade. Calculated by the reval suite. Only used on order entry and only as an estimation of the full IM for this trade. Validation Rules: No Input. Up to 19 figures for the AMT. |
| 170 | `DX.ORD.SEC.IM.ACC` | `DxOrder_SecImAcc` | TField |  | Used to default the inital margin account, or override it for this trade. Validation Rules: Up to 16 for ACC NO INPUT. |
| 171 | `DX.ORD.SEC.RT.COMPANY` | `DxOrder_SecRtCompany` | TField |  | The following field allows the user to automatically route Order's/Trades and the resultant fills from the system to another. The system will automatically assign the couterparty to any trade depending on product and location that was traded. Routing of the input of trades and orders can only take place if the secondary customer on the trade has a routing customer set-up on DX.ACC.MASTER. Once a trade/order has been authorised the system can replicate the necessary trade/order data into the company specified in the DX.ACC.MASTER. the Secondary customer will be set as the RT.CUST.ID in the DX.ACC.MASTER. The T24 company in which the SEC.RT.CUST.ID (Secondary Routing Customer Id) is held, this will allow trades/orders to be mirrored into the T24 company Validation Rules: NO INPUT this data will be defaulted from the appropriate DX.ACC.MASTER record. |
| 172 | `DX.ORD.SEC.RT.PORT.ID` | `DxOrder_SecRtPortId` | TField |  | The following field allows the user to automatically route Order's/Trades and the resultant fills from the system to another. The system will automatically assign the couterparty to any trade depending on product and location that was traded. Routing of the input of trades and orders can only take place if the secondary customer on the trade has a routing customer set-up on DX.ACC.MASTER SEC.RT.CUST.ID is the customer Id held in the SEC.RT.COMPANY company. If this field is blank no routing will take place. This customer will be the Secondary customer in the mirrored trade/order in the SEC.RT.COMPANY company. Validation Rules: NOINPUT this data will be defaulted from the appropriate DX.ACC.MASTER record. |
| 173 | `DX.ORD.SEC.RT.WHEN` | `DxOrder_SecRtWhen` | TField |  | The following field allows the user to automatically route Order's/Trades and the resultant fills from the system to another. The system will automatically assign the couterparty to any trade depending on product and location that was traded. Routing of the input of trades and orders can only take place if the secondary customer on the trade has a routing customer set-up on DX.CUSTOMER. SEC.RT.WHEN defaults the date and time as soon as the order/trade has been replicated Validation Rules: No input this field will be defaulted as soon as the order/trade has been replicated |
| 174 | `DX.ORD.SEC.RT.LINK` | `DxOrder_SecRtLink` | TField |  | The following field allows the user to automatically route Order's/Trades and the resultant fills from the system to another. The system will automatically assign the couterparty to any trade depending on product and location that was traded. Routing of the input of trades and orders can only take place if the secondary customer on the trade has a routing customer set-up on DX.CUSTOMER. SEC.RT.LINK (Primary routing link) The Trade ID which this transaction is hedged against. Validation Rules: No input |
| 175 | `DX.ORD.SEC.ENTITLE` | `DxOrder_SecEntitle` | TField |  | When entitlements are pending the PENDING.DIARY field on DX.TRADE is marked with the Diary event. The trade cannot be amended whilst this is set. It is recommended that all trades therefore be authorised before entitlements are created. When entitlements are authorised, the PENDING.DIARY field is cleared and the trades become free to be amended again. The DX.ENTITLEMENT Id. is stamped on the PRI.ENTITLE and SEC.ENTITLE for the relevant customers. Validation Rules: No input |
| 176 | `DX.ORD.SEC.OVE.ADDR` | `DxOrder_SecOveAddr` |  |  |  |
| 177 | `DX.ORD.SEC.MESS.CTL` | `DxOrder_SecMessCtl` |  |  |  |
| 178 | `DX.ORD.SEC.PREM.OFFSET` | `DxOrder_SecPremOffset` | TField |  | No of days offset from charging to account posting for premiums for this SEC.CUSTOMER. Validation Rules: No Input Field Input defaults from values in DX.CONTRACT.MASTER |
| 179 | `DX.ORD.SEC.BEN.NO` | `DxOrder_SecBenNo` | TField |  | This field is used when the secondary counterparty (This is normally the broker.)of the deal instructs us to pay funds to another party who does not have an account with us. Validation Rules: No-Input until the order has been authorised |
| 180 | `DX.ORD.SEC.BEN.ADD` | `DxOrder_SecBenAdd` |  |  |  |
| 181 | `DX.ORD.SEC.CPY.NO` | `DxOrder_SecCpyNo` | TField |  | Identifies the bank to which the secondary counterparty (This is normally the broker) wishes the amount sold to be paid. This will either be the bank of the counterparty or the bank of their nominated beneficiary. When a contract matures, funds must be moved to actually settle the contract. This involves paying the counterparty or his nominated beneficiary for the currency sold and receiving funds for the currency purchased. The counterparty will advise us of where the money which we have sold is to be paid and we will advise them where we require the currency purchased to be remitted. The delivery of funds will normally be as one payment but may be in several instalments. If the bank is known to us (i.e. a customer record exists), the customer number of the bank will be entered in this field. If not, the details should be entered in the CPY.CORR.ADD field. Validation Rules: No-Input until this order is authorised. |
| 182 | `DX.ORD.SEC.CPY.ADD` | `DxOrder_SecCpyAdd` |  |  |  |
| 183 | `DX.ORD.SEC.CPY.BNK.ACC` | `DxOrder_SecCpyBnkAcc` | TField |  | S Contains the account number of the secondary counterparty or nominated beneficiary (This is normally the broker) at their correspondent bank. The field will be used to provide the correspondent with the necessary details to credit the counterparty's or beneficiary's account. When a contract matures, funds must be moved to actually settle the contract. This involves paying the counterparty or his nominated beneficiary for the currency sold and receiving funds for the currency purchased. The counterparty will advise us of where the money which we have sold is to be paid and we will advise them where we require the currency purchased to be remitted. The delivery of funds will normally be as one payment but may be in several installments. Validation Rules: No-input until this order is authorised. |
| 184 | `DX.ORD.SEC.INTR.BK.NO` | `DxOrder_SecIntrBkNo` | TField |  | Identifies any intermediary bank involved in the transaction and will be specified by the counterparty. If the intermediary is known to us (i.e. their is an associated customer record), the customer number of the intermediary bank will be entered in this field. If not, details should be entered in the INTERMED.ADD field. Validation Rules: No-Input until this order is authorised. |
| 185 | `DX.ORD.SEC.INTR.ADD` | `DxOrder_SecIntrAdd` |  |  |  |
| 186 | `DX.ORD.SEC.CONF.NAR` | `DxOrder_SecConfNar` |  |  |  |
| 187 | `DX.ORD.SEC.PYMT.NAR` | `DxOrder_SecPymtNar` |  |  |  |
| 188 | `DX.ORD.SEC.RCAD.NAR` | `DxOrder_SecRcadNar` |  |  |  |
| 189 | `DX.ORD.SEC.BK2BK.IN` | `DxOrder_SecBk2bkIn` |  |  |  |
| 190 | `DX.ORD.TICK.SIZE` | `DxOrder_TickSize` | TField |  | Tick size defaulted from DX.CONTRACT.MASTER No Input Field |
| 191 | `DX.ORD.TICK.VALUE` | `DxOrder_TickValue` | TField |  | Tick Value defaulted from DX.CONTRACT.MASTER Validation Rules: No input field |
| 192 | `DX.ORD.CONTRACT.SIZE` | `DxOrder_ContractSize` | TField |  | Contract data - no of trading units per standard lot orderd. Validation Rules: No input field - defaulted from DX.CONTRACT.MASTER Numeric, up to 16 characters |
| 193 | `DX.ORD.ALT.IND.NAME` | `DxOrder_AltIndName` |  |  |  |
| 194 | `DX.ORD.ALT.IND.ID` | `DxOrder_AltIndId` |  |  |  |
| 195 | `DX.ORD.AI.RESERVED2` | `DxOrder_AiReserved2` |  |  |  |
| 196 | `DX.ORD.AI.RESERVED1` | `DxOrder_AiReserved1` |  |  |  |
| 197 | `DX.ORD.ORDER.DATE` | `DxOrder_OrderDate` | TField | Yes | The date on which the order was recieved. Validation Rules: Default to TODAY Mandatory input Up to 11 DATE format |
| 198 | `DX.ORD.ORDER.TIME` | `DxOrder_OrderTime` | TField | Yes | The time at which the order was recieved. Validation Rules: Default to current time according to the atomic clock Mandatory input Up to 11 TIME format. |
| 199 | `DX.ORD.BROKER.DATE` | `DxOrder_BrokerDate` | TField |  | A Broker Date cannot be entered until a ORDER.DATE and ORDER.TIME have been entered. This is the date at which the order was passed to the broker. Validation Rules: Default to TODAY. All secondary fields cannot be populated until BROKER.DATE and BROKER.TIME field's have been populated. Up to 11 DATE format. |
| 200 | `DX.ORD.BROKER.TIME` | `DxOrder_BrokerTime` | TField |  | A Broker Time cannot be entered until a ORDER.DATE and ORDER.TIME have been entered. This is the time at which the order was passed to the broker. Validation Rules: Default to current time according to atomic clock. All secondary fields cannot be populated until BROKER.DATE and BROKER.TIME field's have been populated. Up to 11 TIME format. |
| 201 | `DX.ORD.ORDER.STATUS` | `DxOrder_OrderStatus` | TField |  | Order status can be OPEN, TRANSMITTED, REJECTED, CANCELLATION REQUEST, CANCELLATION REJECTED, CANCELLED, MODIFICATION REQUEST, PARTIAL and FILLED. Validation Rules: Becomes inputtable when ORDER.AMEND field is set to YES. Up to 21 alphanumeric characters. |
| 202 | `DX.ORD.ORDER.LOTS` | `DxOrder_OrderLots` | TField |  | The total number of lots for which this order has been placed. Validation Rules: No Input |
| 203 | `DX.ORD.LOTS.FILLED` | `DxOrder_LotsFilled` | TField |  | The total number of lots that have been filled so far for this order. Validation Rules: No Input |
| 204 | `DX.ORD.LOTS.OPEN` | `DxOrder_LotsOpen` | TField |  | The total number of lots left open to be filled on this order. Validation Rules: No Input |
| 205 | `DX.ORD.UNDERLYING` | `DxOrder_Underlying` | TField | Yes | Mandatory if the trade is set as covered. Validation Rules: Defaulted from DX.CONTRACT.MASTER No Input. |
| 206 | `DX.ORD.EXOTIC.TYPE` | `DxOrder_ExoticType` |  |  |  |
| 207 | `DX.ORD.RESERVED.X2` | `DxOrder_ReservedX2` |  |  |  |
| 208 | `DX.ORD.EXOTIC.DATE` | `DxOrder_ExoticDate` |  |  |  |
| 209 | `DX.ORD.EXOTIC.TIME` | `DxOrder_ExoticTime` |  |  |  |
| 210 | `DX.ORD.EXOTIC.EVENT` | `DxOrder_ExoticEvent` |  |  |  |
| 211 | `DX.ORD.AUTO.AUTHORISE` | `DxOrder_AutoAuthorise` | TField |  | When set as YES the trade gets automatically authorised. Validation Rules: Once the value YES is provided in AUTO.AUTHORISE it cannot be changed. |
| 212 | `DX.ORD.RESERVED.X3` | `DxOrder_ReservedX3` |  |  |  |
| 213 | `DX.ORD.RESERVED.X4` | `DxOrder_ReservedX4` |  |  |  |
| 214 | `DX.ORD.RESERVED.X5` | `DxOrder_ReservedX5` |  |  |  |
| 215 | `DX.ORD.USR.FLD.NAME` | `DxOrder_UsrFldName` |  |  |  |
| 216 | `DX.ORD.USR.FLD.VAL` | `DxOrder_UsrFldVal` |  |  |  |
| 217 | `DX.ORD.USR.FLD.TEXT` | `DxOrder_UsrFldText` |  |  |  |
| 218 | `DX.ORD.USR.FLD.PRICE` | `DxOrder_UsrFldPrice` |  |  |  |
| 219 | `DX.ORD.USR.RSVD.X3` | `DxOrder_UsrRsvdX3` |  |  |  |
| 220 | `DX.ORD.USR.RSVD.X4` | `DxOrder_UsrRsvdX4` |  |  |  |
| 221 | `DX.ORD.USR.RSVD.X5` | `DxOrder_UsrRsvdX5` |  |  |  |
| 222 | `DX.ORD.LIMIT.TYPE` | `DxOrder_LimitType` | TField | Yes | Defines LIMIT or MARKET orders. Validation Rules: Defaults to Market Mandatory. |
| 223 | `DX.ORD.LIMIT.PRICE` | `DxOrder_LimitPrice` | TField | Yes | The price of the Limit order. Mandatory for 'LIMIT' orders LIMIT.TYPE. Validation Rules: Mandatory for 'LIMIT' orders |
| 224 | `DX.ORD.LIMIT.DATE` | `DxOrder_LimitDate` | TField | Yes | The date the Limit order is valid until . Mandatory for 'LIMIT' orders LIMIT.TYPE. Validation Rules: Mandatory for 'LIMIT' orders Default to TODAY This order is valid from TODAY until, EOE/D of the LIMIT.DATE. |
| 225 | `DX.ORD.ORDER.TYPE` | `DxOrder_OrderType` | TField |  | Defines what kind of order this is, Good till cancel etc. Validation Rules: DX.ORDER.TYPE to define. |
| 226 | `DX.ORD.FX.PIP.TYPE` | `DxOrder_FxPipType` | TField | Yes | Type of FX pips RATE PER LOT, PERCENTAGE or FIXED. Validation Rules: Mandatory for FX options No Input unless this is a foreign ccy contract Up to 11 alphanumeric characters. |
| 227 | `DX.ORD.FX.PIPS` | `DxOrder_FxPips` | TField |  | The pipage on the trade. Calculated depending on FX.PIP.TYPE Validation Rules: The contents of the field will override the premium calculated for this trade, and this calculated value will be used instead. No Input unless this is a foreign ccy contract. Up to 19 alphanumeric characters. |
| 228 | `DX.ORD.FX.PREM.AMT` | `DxOrder_FxPremAmt` | TField |  | The total premium calculated for an FX contract, where the figure overrides the premium calculated. Validation Rules: No Input Up to 19 alphanumeric characters. |
| 229 | `DX.ORD.ORDER.ADVICE` | `DxOrder_OrderAdvice` | TField |  | Order advice may be SOLICTED, UNSOLICTED or DICRETIONARY Validation Rules: Up to 13 alphanumeric characters. |
| 230 | `DX.ORD.PARENT.REF` | `DxOrder_ParentRef` | TField |  | Reference of Parent Order/Expiry etc. that created this trade. Validation Rules: Up to 35 alphanumeric characters. |
| 231 | `DX.ORD.CHILD.REF` | `DxOrder_ChildRef` |  |  |  |
| 232 | `DX.ORD.PENDING.DIARY` | `DxOrder_PendingDiary` | TField |  | When entitlements are pending the PENDING.DIARY field on DX.TRADE is marked with the Diary event. The trade cannot be amended whilst this is set. It is recommended that all trades therefore be authorised before entitlements are created. When entitlements are authorised, the PENDING.DIARY field is cleared and the trades become free to be amended again. The DX.ENTITLEMENT Id. is stamped on the PRI.ENTITLE and SEC.ENTITLE for the relevant customers. Validation Rules: No input |
| 233 | `DX.ORD.SUPPRESS.ALL.MSG` | `DxOrder_SuppressAllMsg` | TField | No | This field is not inputtable within DX.ORDER, but can be set within the resulting DX.TRADE record. If selected, this field suppresses all delivery message generation related to this trade (does not include closeout messages). Optional field - Yes or blank. |
| 234 | `DX.ORD.IND.PRICE` | `DxOrder_IndPrice` | TField |  | This field captures the value entered in the field Sec. Price of DX. ORDER at order stage 0 Validation Rules: No input field |
| 235 | `DX.ORD.ORIG.PRICE` | `DxOrder_OrigPrice` | TField |  | It is a NOINPUT field. |
| 236 | `DX.ORD.STATUS.NARRATIVE` | `DxOrder_StatusNarrative` |  |  |  |
| 237 | `DX.ORD.ORDER.INITIATOR` | `DxOrder_OrderInitiator` | TField |  | This field holds the Order Initiator. This might be the bank or the client (account holder). It can either hold values bank or Client�s customer ID. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 238 | `DX.ORD.TRADER` | `DxOrder_Trader` | TField |  | This field holds the trader third party. It can either hold the LEI or National ID or any other identifier. It can also be mapped to a T24 customer ID, from where the LEI or name of the customer can be got. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 239 | `DX.ORD.MANAGER` | `DxOrder_Manager` | TField |  | This field holds the manager third party. It can either hold the LEI or National ID or any other identifier. It can also be mapped to a T24 customer ID, from where the LEI or name of the customer can be got. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 240 | `DX.ORD.DECISION.MKR.ID` | `DxOrder_DecisionMkrId` | TField |  | This field will provide user with the ability to identify the decision maker on the trade. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 241 | `DX.ORD.INSTRUCTION.MKR` | `DxOrder_InstructionMkr` | TField |  | This field holds the ID of Instruction maker third party who is entitled to place orders on behalf of the main account holder. It can either hold the LEI or National ID or any other identifier. It can also be mapped to a T24 customer ID, from where the LEI or name of the customer can be got. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 242 | `DX.ORD.PREM.PERC` | `DxOrder_PremPerc` | TField |  | This field holds the premium expressed as a percentage of the notional amount. Validation Rules: Value can be between 0 to 100 Premium amount is computed as Notional amount * Premium Percentage in Primary side and Secondary side |
| 243 | `DX.ORD.PARTICIPATION.RATE` | `DxOrder_ParticipationRate` | TField | Yes | This fields hold the rate which is used to calculate the final pay out of the option. Validation Rules: Input is mandatory if PERFORMANCE is set as 'YES' in DX.CONTRACT.MASTER When PERFORMANCE is set to "YES", then Strike price will be defaulted to 1 and Option type to "CALL" |
| 244 | `DX.ORD.OBSERVATION.DATE` | `DxOrder_ObservationDate` |  |  |  |
| 245 | `DX.ORD.OBSERVED.SPOT.RATE` | `DxOrder_ObservedSpotRate` |  |  |  |
| 246 | `DX.ORD.SPOT.PRICE.INITIAL` | `DxOrder_SpotPriceInitial` | TField | Yes | This field holds the spot price of the underlying on commencement of the contract.This price would be used to calculate the performance of contracts with "PERFORMANCE" feature set to "YES" Validation Rules: Input is mandatory if PERFORMANCE is set to 'YES' in DX.CONTRACT.MASTER |
| 247 | `DX.ORD.PRI.CUST.LEI.NCI` | `DxOrder_PriCustLeiNci` |  |  |  |
| 248 | `DX.ORD.SEC.CUST.LEI.NCI` | `DxOrder_SecCustLeiNci` | TField |  | This field holds the LEI/NCI code of the secondary side customer. Validation If blank, system defaults the LEI/NCI of the customer based on priority defined in SC.NCI.PRIORITY and rules defined in SC.NCI.PARAMETER System raises error if it is not in the below format L/N-CustomerNo-LEI/NCI code |
| 249 | `DX.ORD.CHARGE.GROUP` | `DxOrder_ChargeGroup` | TField |  | This field holds the generic charge group id of SCTR.GROUP.CONDITION record When the field is manually inputted with generic id that starts with G-Upto 6 Numeric values, SCTR.GROUP.CONDITION will be directly referred using this field value when the field is blank, CUSTOMER.CHARGE is read for the customer to get the SCTR.GROUP.CONDITION id from SC.ACT.GROUP field Validations User has to manually input this field to accept Generic group id of SCTR.GROUP.CONDITION table Value should be a valid record id from SCTR.GROUP.CONDITION record |
| 250 | `DX.ORD.UNDLYING.MAT.DATE` | `DxOrder_UndlyingMatDate` | TField |  |  |
| 251 | `DX.ORD.LEI.NCI.CHK.REQ` | `DxOrder_LeiNciChkReq` | TField |  |  |
| 252 | `DX.ORD.PARENT` | `DxOrder_Parent` | TField |  |  |
| 253 | `DX.ORD.PARENT.CHILD.REF` | `DxOrder_ParentChildRef` | TField |  |  |
| 254 | `DX.ORD.AUTHORISE.CHILD` | `DxOrder_AuthoriseChild` | TField |  |  |
| 255 | `DX.ORD.RESERVED.X29` | `DxOrder_ReservedX29` | TField |  |  |
| 256 | `DX.ORD.DAYS.PER.YEAR` | `DxOrder_DaysPerYear` | TField |  | Its value is populated from INTEREST.DAY.BASIS of the CURRENCY table. |
| 257 | `DX.ORD.SPREAD.RATE` | `DxOrder_SpreadRate` | TField |  | This is the rate (signed) to be added to or subtracted from the reference rate. |
| 258 | `DX.ORD.SWAP.REFERENCE` | `DxOrder_SwapReference` | TField |  | It is a NOINPUT field. |
| 259 | `DX.ORD.CAP.FLOOR` | `DxOrder_CapFloor` | TField | Yes | Valid inputs are: CAP, FLOOR and SWAPTION. Input for this field is mandatory if underlying is OTHER in DX.CONTRACT.MASTER. |
| 260 | `DX.ORD.HEDGE.PL.CATEG` | `DxOrder_HedgePlCateg` | TField |  | It is a NOINPUT field. |
| 261 | `DX.ORD.BUY.FLOATING.RATE` | `DxOrder_BuyFloatingRate` | TField |  | This is the sequence number of the Periodic Interest Table for Buy floating rate. The format is XXYYY where XX is the sequence no and YYY is the currency. Input not allowed if UNDERLYING is not a Cap, Floor or Swaption. |
| 262 | `DX.ORD.SELL.FLOATING.RATE` | `DxOrder_SellFloatingRate` | TField |  | This is the sequence number of the Periodic Interest Table for a Sell floating rate. The format is XXYYY where XX is the sequence no and YYY is the currency. Input not allowed if UNDERLYING is not a Cap, Floor or Swaption. |
| 263 | `DX.ORD.MASTER.AGREEMENT` | `DxOrder_MasterAgreement` | TField | Yes | Input is mandatory if CAP.FLOOR holds the value swaption. Input should be a valid record in SWAP.AGREEMENT.TYPE. |
| 264 | `DX.ORD.INTEG.DATA.ITEM` | `DxOrder_IntegDataItem` |  |  |  |
| 265 | `DX.ORD.INTEG.DATA.VALUE` | `DxOrder_IntegDataValue` |  |  |  |
| 266 | `DX.ORD.CUT.OFF.TIME` | `DxOrder_CutOffTime` | TField |  | When DAY.TRADE is YES then on reaching the cut off time aggregated trade gets created by broker. Validation Rules: NOINPUT field defaulted from DX.EXCHANGE.MASTER |
| 267 | `DX.ORD.DAY.TRADE` | `DxOrder_DayTrade` | TField |  | When set to YES instead of creating trade for each fills an aggregated trade gets created by broker. Validation Rules: Allowed values are YES and NO. Defaulted from DX.EXCHANGE.MASTER and be overwritten at initial order level. Changes not allowed at fill order. |
| 268 | `DX.ORD.TRADE.TIME` | `DxOrder_TradeTime` | TField |  | Time at which the order is filled or executed in the exchange. When DAY.TRADE is YES then orders that all gets executed before theCUT.OFF.TIME are aggregated together and trade created by broker. Validation Rules: Default to Cut off time when not inputted. Input not allowed when DAY.TRADE is not set. |
| 269 | `DX.ORD.PERIOD.FREQUENCY` | `DxOrder_PeriodFrequency` | TField |  | Input should be of type FQU which is a standard T24 Frequency code. Input not allowed if UNDERLYING is not OTHER in DX.CONTRACT.MASTER. Input not allowed if CAP.FLOOR holds the value SWAPTION. |
| 270 | `DX.ORD.PERIOD.START` | `DxOrder_PeriodStart` |  |  |  |
| 271 | `DX.ORD.PERIOD.END.DATE` | `DxOrder_PeriodEndDate` |  |  |  |
| 272 | `DX.ORD.PERIOD.FIX.DATE` | `DxOrder_PeriodFixDate` |  |  |  |
| 273 | `DX.ORD.PERIOD.PAY.DATE` | `DxOrder_PeriodPayDate` |  |  |  |
| 274 | `DX.ORD.PREM.PYMT.FREQ` | `DxOrder_PremPymtFreq` | TField |  | Input should be of type FQU which is a standard T24 Frequency code. Represents the frequency in which the premium payment is to be made. |
| 275 | `DX.ORD.PREM.PYMT.DATE` | `DxOrder_PremPymtDate` |  |  |  |
| 276 | `DX.ORD.PREM.PYMT.AMT` | `DxOrder_PremPymtAmt` |  |  |  |
| 277 | `DX.ORD.LOTS.TRANSFER` | `DxOrder_LotsTransfer` | TField | Yes | Specifies the number of lots to be transferred. It is a NOINPUT field. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. |
| 278 | `DX.ORD.DEST.CUST` | `DxOrder_DestCust` | TField | Yes | Specifies the external recipient customer reference number. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. Should be a valid record in DX.CUSTOMER. |
| 279 | `DX.ORD.DEST.PORTFOLIO` | `DxOrder_DestPortfolio` | TField | Yes | Specifies the external recipient customer portfolio reference. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. Should be valid record in SEC.ACC.MASTER. |
| 280 | `DX.ORD.DEST.CUST.PORT` | `DxOrder_DestCustPort` | TField | Yes | Specifies the recipient customer or portfolio. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. Should be valid record in CUSTOMER. |
| 281 | `DX.ORD.CUST.CPARTY` | `DxOrder_CustCparty` | TField | Yes | Specifies the receiver counterparty. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. Should be valid record in CUSTOMER. |
| 282 | `DX.ORD.CUST.BNK.NME` | `DxOrder_CustBnkNme` | TField | Yes | Specifies the receiver bank name. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. |
| 283 | `DX.ORD.CUST.BNK.ADD` | `DxOrder_CustBnkAdd` | TField | Yes | Specifies the receiver bank address. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. |
| 284 | `DX.ORD.CUST.BNK.SORT.CDE` | `DxOrder_CustBnkSortCde` | TField | Yes | Specifies the receiver bank sort code. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. |
| 285 | `DX.ORD.PRICE.TRADED` | `DxOrder_PriceTraded` | TField | Yes | Specifies the price at which the trade is being done. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. |
| 286 | `DX.ORD.FEE` | `DxOrder_Fee` | TField | Yes | Specifies whether fee is required or not. It accepts two values either YES or NO. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. |
| 287 | `DX.ORD.ADVICE` | `DxOrder_Advice` | TField | Yes | Specifies whether transfer advice is required or not. It accepts two values either YES or NO. Input mandatory if TRANSFER.TYPE holds the value TRANSFER.INC or TRANSFER.INC.PAY. |
| 288 | `DX.ORD.CREATE.TRADES` | `DxOrder_CreateTrades` | TField |  | This field should be set to YES to authorise a filled DX order, which in turn creates DX trades at average price Validation Rules: Defaults from DX.PARAMETER, but can be amended manually |
| 289 | `DX.ORD.FILLED.LOTS` | `DxOrder_FilledLots` |  |  |  |
| 290 | `DX.ORD.FILLED.PRICE` | `DxOrder_FilledPrice` |  |  |  |
| 291 | `DX.ORD.FILLED.IPRICE` | `DxOrder_FilledIprice` |  |  |  |
| 292 | `DX.ORD.RESERVED.10` | `DxOrder_Reserved10` |  |  |  |
| 293 | `DX.ORD.RESERVED.11` | `DxOrder_Reserved11` |  |  |  |
| 294 | `DX.ORD.TREASURY.CUSTOMER` | `DxOrder_TreasuryCustomer` | TField |  | It is a NOINPUT field. Identifies if the counter party is a treasury customer or not. It is updated at trade level. |
| 295 | `DX.ORD.LINK.REFERENCE` | `DxOrder_LinkReference` | TField |  | Linked to TRANS.LINK.REFERENCE application. It is updated at trade level. |
| 296 | `DX.ORD.CANCEL.PEND.ORDERS` | `DxOrder_CancelPendOrders` | TField |  | When set to yes, remaining order details will be updated |
| 297 | `DX.ORD.CCY.BOUGHT` | `DxOrder_CcyBought` | TField |  |  |
| 298 | `DX.ORD.AMT.BOUGHT` | `DxOrder_AmtBought` | TField |  |  |
| 299 | `DX.ORD.CCY.SOLD` | `DxOrder_CcySold` | TField |  |  |
| 300 | `DX.ORD.AMT.SOLD` | `DxOrder_AmtSold` | TField |  |  |
| 301 | `DX.ORD.ORDER.CLOSEOUT` | `DxOrder_OrderCloseout` | TField |  | Allows null or CLOSE. When set to CLOSE the order is considered as a square-off order to be closed against trades provided in CLOSEOUT.TRADE field. The version to be used for closeout is defined in CLOSEOUT.VERSION field of DX.PARAMETER. For example when set to AUTO.CLOSE, the closeout process uses DX.CO.MANUAL.INPUT,AUTO.CLOSE Also the contract used in order should have B2B set to YES else the user has to manually do the closeout process for the other side. Validation Rules: No partial fill is allowed when this field is set to CLOSE. |
| 302 | `DX.ORD.CLOSEOUT.TRADE` | `DxOrder_CloseoutTrade` |  |  |  |
| 303 | `DX.ORD.CLOSEOUT.LOTS` | `DxOrder_CloseoutLots` |  |  |  |
| 304 | `DX.ORD.KICKIN.EXPIRE` | `DxOrder_KickinExpire` | TField |  | Value to this field gets defaulted from DX.CONTRACT.MASTER field KICKIN.EXPIRE. Validation Rules: Upto 3 alphanumeric values Valid inputs are either YES or NO |
| 305 | `DX.ORD.LOCAL.REF` | `DxOrder_LocalRef` |  |  |  |
| 306 | `DX.ORD.OVERRIDE` | `DxOrder_Override` |  |  |  |
| 307 | `DX.ORD.RECORD.STATUS` | `DxOrder_RecordStatus` | String |  |  |
| 308 | `DX.ORD.CURR.NO` | `DxOrder_CurrNo` | String |  |  |
| 309 | `DX.ORD.INPUTTER` | `DxOrder_Inputter` |  |  |  |
| 310 | `DX.ORD.DATE.TIME` | `DxOrder_DateTime` |  |  |  |
| 311 | `DX.ORD.AUTHORISER` | `DxOrder_Authoriser` | String |  |  |
| 312 | `DX.ORD.CO.CODE` | `DxOrder_CoCode` | String |  |  |
| 313 | `DX.ORD.DEPT.CODE` | `DxOrder_DeptCode` | String |  |  |
| 314 | `DX.ORD.AUDITOR.CODE` | `DxOrder_AuditorCode` | String |  |  |
| 315 | `DX.ORD.AUDIT.DATE.TIME` | `DxOrder_AuditDateTime` | String |  |  |
