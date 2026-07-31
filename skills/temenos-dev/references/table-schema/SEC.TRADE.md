# SEC.TRADE — Table Schema

> Source: `INSERTS/I_F.SEC.TRADE` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SBS.SECURITY.CODE` | `SecTrade_SecurityCode` | TField | Yes | Identifies the Security. Validation Rules: 1-6 numeric character Security number separated from a 3 numeric character suffix by "-". or 3-10 type MNE(uppercase alpha or numeric or ".") character Mnemonic Security id. (Mandatory input.) Must be the ID of a valid SECURITY.MASTER file record. Cannot be changed when SERVICE.REF is populated. |
| 2 | `SC.SBS.SECURITY.CURRENCY` | `SecTrade_SecurityCurrency` | TField |  | Specifies the currency of the Security (Field 1). Validation Rules: NO INPUT. Automatic default is to the Ccy of the Security as per the Security. Master record (Field 7 - SECURITYCURRENCY). |
| 3 | `SC.SBS.PRICE.TYPE` | `SecTrade_PriceType` | TField |  | Specifies the type of price calculation relevant to the Security (Field 1). The price type identifies to the system the type of calculation it is to make in terms of the transaction beingprocessed. Within the PRICE.TYPE table there isss information which enables the User to set up the different pricetypes necessary for processing equities bonds and option trades where 1 option may well repressent 100o shares andthe price quoted is per share and NOT by option. Validation Rules: NO INPUT. Automatic default is to the SECURITY.MASTER file record (Field 11 - PRICE TYPE). Must exist on the PRICE.TYPE table. |
| 4 | `SC.SBS.DEPOSITORY` | `SecTrade_Depository` | TField | Yes | Indicates which Depository the Security traded is to be delivered from/to. Whereas the default will work for a majority of transactions T24 do not advise that the default value be kept atSecurity Master level to avoid errors with the automatic SWIFT CEDEL interface contained within the SecuritiesModule for example. For the comprehensive description of the rules and validation concerning the usage of this and further fieldswithin the Securities Delivery messages see the seperate Securities manual concerning Delivery. Validation Rules: 1-10 numeric character Customer ID number. or 3-10 type MNE (uppercase alpha or numeric or ".") characterMnemonic Customer id. (Mandatory input) Default value = the Depository specified on the SECURITY.MASTER file record(Field 35 - Default.Depository). Must be a valid Customer for whom the Customer.Security file record (Field 1 - CUSTOMER TYPE) equals D(Depository). Cannot be changed when SERVICE.REF is populated. |
| 5 | `SC.SBS.TRADE.DATE` | `SecTrade_TradeDate` | TField | Yes | Records the date that the trade is made on. The Trade date of any transaction cannot be greater than today; however the System will allow back dated trades. Note: The trade date of any transaction is important for more than just one reason. The contract is a legallybinding document between the Client and Bank (Broker) and should be retained for legal and tax reasons. The date ofthe transaction is the date at which ownership of shares is transferred along with any rights or dividends due orpayable to that client. Validation Rules: Up to 9 type D date characters, (Standard Date Format in range 1950-2049). (Mandatory input) Default value = RunDate. Can not be greater than Run Date. Cannot be changed when SERVICE.REF is populated. |
| 6 | `SC.SBS.VALUE.DATE` | `SecTrade_ValueDate` | TField | Yes | Records the date on which the trade is to be effected. The value date for any transaction can vary from 1 day to 1 month depending on the security being traded and thestock exchange at which it is being traded. A default value date can be defaulted by using the facility within the STOCK.EXCHANGE table.Here the user candefine the number of Business or Calendar days between the trade and value date of any particular Stock Exchange. In STOCK.EXCHANGE table, user can also specify the settlement basis as 'FIXED'. In this case, a calendar(STK.EXCH.CALENDAR) is maintained for the Stock Exchange and for a Year. A settlement day can be defined for aperiod for a particular Stock Exchange and Year. N.B Care should be taken when and if using this facility. Validation Rules: Up to 9 type D date characters (Standard Date Format in range 1950-2049). (Mandatory input) Default value =Trade Date (Field 5). Can not be less than Trade Date (Field 5). Cannot be changed when SERVICE.REF is populated. |
| 7 | `SC.SBS.TRADE.CCY` | `SecTrade_TradeCcy` | TField | Yes | Specifies the currency in which the trade will be settled. The Trade currency is the currency in which the transaction has been dealt with the Broker or Counterpartyconcerned. The trade currency cannot be changed and the Broker Counterparty account must always be in this currency. The client on the other hand can be debited or credited in whatever currency he or she wishes. As mentioned the default value within the Sec.Trade will be the Security currency although this can be changed. The ONLY time this is not true is when dealing for the Banks Portfolio and in this instance the Trade currencymust equal the security currency. The reasons being the complicated Realised and unrealised P L calculations involved at the End of Dayprocessing. Note: Any change to either the security number, value date or trade currency within the Sec.Trade will promptthe system to recalculate all charges commissions and interest calculations within that particular Sec.Trade. Validation Rules: 3 type CCY (alpha) character currency code. or 1-3 numeric character currency number. (Mandatory input) Defaultvalue = Security Currency (Field 5) on SEC.MASTER. Must exist on Currency file. |
| 8 | `SC.SBS.STOCK.EXCHANGE` | `SecTrade_StockExchange` | TField | Conditional | Identifies the Stock Exchange that the security is traded on. The stock exchange determines several events within the Sec.Trade application. 1. Automatic calculation of the Value date depending on the information opened within that Stock.Exchange record 2. Automatic link to the standard stock Exchange commissions and charges as stored within the variousStock.Exchange tables and again determined by the information within that particular Stock.Exchange record. Each Stock Exchange is linked to a seperate Stock.Exchange Calculation table which contains all the localcharges, stamps and taxes. Plus it allows the user to store the commission rates that YOU the Bank would normallycharge to the client yourselves. Normally when entering a Sec.Trade the User is obliged to enter the Stock Exchange at which the transaction waseffected. The system will then go via the Stock Exchange to the Calculation table and default all the brokerage,stamps taxes etc. accirding to the rates stored within those tables. However there are 3 seperate options availableto the User when entering a Sec.Trade which directly affects the commissions etc being calculated. 1. In Sec.Trade Field 9 there is a GROSS/NET indicator which defaults at the moment to NO i.e NOT NET. Thismeans that the trade is Not Net of commission and the default commissions should take affect. If the flag is set toYES however that tells the system that it is a Net trade and that No commissions whatsoever are to be charged. Thisthen overrides all other default commission rates. 2. Within the Stock.Exchaneg table there is a link to the Calculation Table at Field 3 which is called "CALCCOUNTRY". If input here the country code specifies which if any Calculation table is to be used.It is an optionalfield and if there is no link to the Calculation Tables then the system will default 0.00s. 3. Stored within the Customer.Security record are Customer and Broker rates which if input will obviouslyoverride any general rates as stored within the Stock.Exchange Tables. The Flow within Sec.Trade is therefore:- 1. Check Net/Groos flag. If "YES" No Automatic calculation. If "NO" System carries on. 2. For Customer and Broker it then checks the Customer.Security record for individual commission tarriffs. Ifthe "Calc.Country" indicator within the Stock.Exchange record is links to the Stock.Exchange calculation tablesthen the syetm will use these rates to default all the other fees payable under that Stock Exchange. If it finds noindividual tarriffs within Customer.Security for either the Client or Broker then it will use the default rateswithin the Stock Exchange calculation tables. If there is NO link between the Stock Exchange Table and the Stock.Exchange Calculation tables and there are Noindividual tarriffs for the Client or Broker then the system will default 0.00s. Note: ALL CALCULATED COMMISSIONS AND FEES CAN BE OVERRIDDEN AT SEC.TRADE LEVEL AND THERE ARE ADDITIONAL FIELDSAVAILABLE FOR SUNDRY/MISCELLANEOUS FEES. Validation Rules: 1-5 type S (uppercase alpha or numeric) character Stock Exchange id code. (Mandatory input) Default value =Stock Exchange specified on the SECURITY.MASTER (Field 16 - Stock.Exchange). Must be a valid Stock.Exchange record id. Cannot be changed when SERVICE.REF is populated. |
| 9 | `SC.SBS.NET.TRADE` | `SecTrade_NetTrade` | TField | Yes | The NET.TRADE field enables you to specify whether or not the underlying SEC.TRADE is being entered NET ofcommissions or with commissions. The current default is "NO" which will cause the System to locate the various commissions, charges, stamps, dutyand taxes relative to your customer, the broker, the security and the stock exchange (should these have beenset-up). If set to "YES" then no commissions will be defaulted at all, although stamp tax and duty, if applicable, willcontinue to form part of the transaction consideration. You may also enter "PRORATA" (T24 will recognise "P" on its own), in which case, any broker commission containedon the SEC.TRADE will be pro-rated over the various customers contained in a bulk trade. The allocations are basedon simple nominals or numbers of bonds and shares. NOTE : There is a version, SEC.TRADE,PRORATA which will assist you in completing a trade in which the brokercommission is to be be pro-rated across all customers contained in that trade. Validation Rules: Y = Yes N/NO = No P/PRORATA = Pro-rating required (Mandatory input) Default value = NO. |
| 10 | `SC.SBS.LAST.PAYMNT.DATE` | `SecTrade_LastPaymntDate` | TField |  | Used for information purposes only to highlight to the user the accrual date or coupon last payment date of anyparticular bond being traded. Can be used in conjunction with Field 12 Interest Days to provide the user with information regarding theaccrual date and hence the actual number of days accrued interest payable at Sec.Trade level. For Information purposes only. Note: Whilst the number of days can be altered this should only be done by firstly changing the staticinformation within the particular Security Master record. The user must understand that the System uses the accrualdate within the Security.Master when it processes its daily accruals for the Banks own portfolio and the systemwill merely make an adjustment to the amount posted within Sec.Trade to keep the Integrity in accordance with thedates within Security.Master. Validation Rules: No Input field internally generated by the system and copies over from the Security.Master record. |
| 11 | `SC.SBS.INTEREST.RATE` | `SecTrade_InterestRate` | TField |  | Indicates the Coupon Rate of the Security, ie. the rate at which interest is to be accrued from Last Payment Date(Field 11) to Value Date (Field 6). The system uses the accrual date as displayed within Field 10 along with the interest rate and the Interest dayBasis as per the Security.Master record to calculate both the number of days accrued and the amount of accruedinterest payable on any individual bond transaction. Whilst the number of days and the actual accrued interest amount can be overridden at transaction level theinterest rate has to be changed at Security.Master level. IMPORTANT. The User must understand any change to the number of days accrued or the calculated amount will merely berecovered by the system at the End of Day processing when dealing with the Banks Own Portfolio Transactions. Validation Rules: No input required. Internally generated field. For RFR Instruments, the interest rate will be calculated based on the PERIODIC.INTEREST table and RFR parameters in SECURITY.MASTER record. |
| 12 | `SC.SBS.INTEREST.DAYS` | `SecTrade_InterestDays` | TField |  | Specifies the number of days interest to be accrued from Last Payment Date (Field 10) to Value Date (Field 6). The system uses the accrual date as displayed within Field 10 along with the interest rate and the Interest dayBasis as per the Security.Master record to calculate both the number of days accrued and the amount of accruedinterest payable on any individual bond transaction. Whilst the number of days and the actual accrued interest amount can be overridden at transaction level theinterest rate has to be changed at Security.Master level. IMPORTANT. The User must understand any change to the number of days accrued or the calculated amount will merely berecovered by the system at the End of Day processing when dealing with the Banks Own Portfolio Transactions. For more information about how interest calculations are performed refer to help-text labelled 'INTEREST.BASIS' Validation Rules: 1-3 numeric characters. Internally generated field that may be over ridden to allow for securities withnon-standard interest calculation methods. |
| 13 | `SC.SBS.EXCH.RATE.SEC` | `SecTrade_ExchRateSec` | TField |  | Specifies the exchange rate applicable between the Security currency (Field 2) and the Local Currency. For information purposes only Validation Rules: 1-10 numeric characters "." (1-6 integers and 1-9 decimal places). Default value = relevant rate as per theCURRENCY file. Where input manually the rate must fall between the parameters set on the CURRENCY file. |
| 14 | `SC.SBS.EXCH.RATE.TRD` | `SecTrade_ExchRateTrd` | TField |  | Specifies the exchange rate applicable between the Trade currency (Field 7) and the Local Currency. Validation Rules: 1-10 numeric characters "." (1-6 integers and 1-9 decimal places). Default value = relevant rate as per theCURRENCY file. Where input manually the rate must fall between the parameters set on the CURRENCY file. |
| 15 | `SC.SBS.ISSUE.DATE` | `SecTrade_IssueDate` | TField | No | Specifies the Issue Date of the Security (Field 1). Currently there is no processing involved with this field it defaults from the Security.Master record and caanotbe changed. Validation Rules: Up to 9 type D date characters, (Standard Date format in range 1950-2049). (Optional input) |
| 16 | `SC.SBS.MATURITY.DATE` | `SecTrade_MaturityDate` | TField |  | Specifies the Maturity Date of the Security (Field 1). Date is defaulted from the Security.Master record and cannot be changed.At the moment it is used purely forinformation purpose. Validation Rules: Up to 9 type D date characters, (Standard Date format in range 1950-2049). Internally generated Field. |
| 17 | `SC.SBS.MARKET.TYPE` | `SecTrade_MarketType` | TField |  | Indicates in which market the Trade has been dealt. Validation Rules: Input may be only, S = spot, or F = forward, or N = normal. Default value = N. |
| 18 | `SC.SBS.CUSTOMER.NO` | `SecTrade_CustomerNo` |  |  |  |
| 19 | `SC.SBS.CUST.TRANS.CODE` | `SecTrade_CustTransCode` |  |  |  |
| 20 | `SC.SBS.CUST.SEC.ACC` | `SecTrade_CustSecAcc` |  |  |  |
| 21 | `SC.SBS.CUST.ACC.NO` | `SecTrade_CustAccNo` |  |  |  |
| 22 | `SC.SBS.CUST.NOMINEE` | `SecTrade_CustNominee` |  |  |  |
| 23 | `SC.SBS.SUB.ACCOUNT` | `SecTrade_SubAccount` |  |  |  |
| 24 | `SC.SBS.CUST.NO.NOM` | `SecTrade_CustNoNom` |  |  |  |
| 25 | `SC.SBS.CUST.PRICE` | `SecTrade_CustPrice` |  |  |  |
| 26 | `SC.SBS.CUST.TOT.NOM` | `SecTrade_CustTotNom` |  |  |  |
| 27 | `SC.SBS.CU.GROSS.AM.SEC` | `SecTrade_CuGrossAmSec` |  |  |  |
| 28 | `SC.SBS.CU.GROSS.AM.TRD` | `SecTrade_CuGrossAmTrd` |  |  |  |
| 29 | `SC.SBS.CU.REALLOWANCE` | `SecTrade_CuReallowance` |  |  |  |
| 30 | `SC.SBS.CU.REALLOW.AMT` | `SecTrade_CuReallowAmt` |  |  |  |
| 31 | `SC.SBS.CUST.INTR.AMT` | `SecTrade_CustIntrAmt` |  |  |  |
| 32 | `SC.SBS.CU.GROSS.ACCR` | `SecTrade_CuGrossAccr` |  |  |  |
| 33 | `SC.SBS.CU.BRKR.COMM` | `SecTrade_CuBrkrComm` |  |  |  |
| 34 | `SC.SBS.CU.FOREIGN.FEE` | `SecTrade_CuForeignFee` |  |  |  |
| 35 | `SC.SBS.CU.COMMISSION` | `SecTrade_CuCommission` |  |  |  |
| 36 | `SC.SBS.CU.COMM.TAX` | `SecTrade_CuCommTax` |  |  |  |
| 37 | `SC.SBS.CU.STAMP.TAX` | `SecTrade_CuStampTax` |  |  |  |
| 38 | `SC.SBS.CU.EBV.FEES` | `SecTrade_CuEbvFees` |  |  |  |
| 39 | `SC.SBS.CU.FEES.MISC` | `SecTrade_CuFeesMisc` |  |  |  |
| 40 | `SC.SBS.CU.DISC.PCENT` | `SecTrade_CuDiscPcent` |  |  |  |
| 41 | `SC.SBS.CU.DISC.AMT` | `SecTrade_CuDiscAmt` |  |  |  |
| 42 | `SC.SBS.CU.WHT.PERC` | `SecTrade_CuWhtPerc` |  |  |  |
| 43 | `SC.SBS.CU.WHT.TAX` | `SecTrade_CuWhtTax` |  |  |  |
| 44 | `SC.SBS.CU.TAX.CODE` | `SecTrade_CuTaxCode` |  |  |  |
| 45 | `SC.SBS.CU.TAX.TYPE` | `SecTrade_CuTaxType` |  |  |  |
| 46 | `SC.SBS.CU.TAX.TCY` | `SecTrade_CuTaxTcy` |  |  |  |
| 47 | `SC.SBS.CU.TAX.LCY` | `SecTrade_CuTaxLcy` |  |  |  |
| 48 | `SC.SBS.CU.MANTAXTCY` | `SecTrade_CuMantaxtcy` |  |  |  |
| 49 | `SC.SBS.CU.MANTAXLCY` | `SecTrade_CuMantaxlcy` |  |  |  |
| 50 | `SC.SBS.CU.INT.CTR` | `SecTrade_CuIntCtr` |  |  |  |
| 51 | `SC.SBS.CU.ADVICE.REQD` | `SecTrade_CuAdviceReqd` |  |  |  |
| 52 | `SC.SBS.CU.NET.AM.TRD` | `SecTrade_CuNetAmTrd` |  |  |  |
| 53 | `SC.SBS.CU.EX.RATE.REF` | `SecTrade_CuExRateRef` |  |  |  |
| 54 | `SC.SBS.CU.EX.RATE.ACC` | `SecTrade_CuExRateAcc` |  |  |  |
| 55 | `SC.SBS.CU.ACCOUNT.CCY` | `SecTrade_CuAccountCcy` |  |  |  |
| 56 | `SC.SBS.CU.AMOUNT.DUE` | `SecTrade_CuAmountDue` |  |  |  |
| 57 | `SC.SBS.CU.REF.CCY` | `SecTrade_CuRefCcy` |  |  |  |
| 58 | `SC.SBS.CU.DELIV.INSTR` | `SecTrade_CuDelivInstr` |  |  |  |
| 59 | `SC.SBS.CU.BEN.BANK.1` | `SecTrade_CuBenBank1` |  |  |  |
| 60 | `SC.SBS.CU.BEN.BANK.2` | `SecTrade_CuBenBank2` |  |  |  |
| 61 | `SC.SBS.CU.BEN.ADDR` | `SecTrade_CuBenAddr` |  |  |  |
| 62 | `SC.SBS.CU.BEN.ACCT` | `SecTrade_CuBenAcct` |  |  |  |
| 63 | `SC.SBS.CU.OVE.ADDR` | `SecTrade_CuOveAddr` |  |  |  |
| 64 | `SC.SBS.CU.MESS.CONTROL` | `SecTrade_CuMessControl` |  |  |  |
| 65 | `SC.SBS.CU.DELIV.KEY` | `SecTrade_CuDelivKey` |  |  |  |
| 66 | `SC.SBS.CU.ORDER.NOS` | `SecTrade_CuOrderNos` |  |  |  |
| 67 | `SC.SBS.CU.ENTITL.ID` | `SecTrade_CuEntitlId` |  |  |  |
| 68 | `SC.SBS.CU.NARRATIVE` | `SecTrade_CuNarrative` |  |  |  |
| 69 | `SC.SBS.CU.NOTES` | `SecTrade_CuNotes` |  |  |  |
| 70 | `SC.SBS.COMM.CODE` | `SecTrade_CommCode` |  |  |  |
| 71 | `SC.SBS.COMM.PERCENT` | `SecTrade_CommPercent` |  |  |  |
| 72 | `SC.SBS.COM.TAX.CODE` | `SecTrade_ComTaxCode` |  |  |  |
| 73 | `SC.SBS.COM.TAX.BCUR` | `SecTrade_ComTaxBcur` |  |  |  |
| 74 | `SC.SBS.COM.TAX.XRTE` | `SecTrade_ComTaxXrte` |  |  |  |
| 75 | `SC.SBS.CU.CAP.INT.AMT` | `SecTrade_CuCapIntAmt` |  |  |  |
| 76 | `SC.SBS.CU.UNF.GROSS` | `SecTrade_CuUnfGross` |  |  |  |
| 77 | `SC.SBS.CU.UNF.SEC.GROS` | `SecTrade_CuUnfSecGros` |  |  |  |
| 78 | `SC.SBS.CU.COUP.TAX.AMT` | `SecTrade_CuCoupTaxAmt` |  |  |  |
| 79 | `SC.SBS.CGT.BAMT.CCY` | `SecTrade_CgtBamtCcy` |  |  |  |
| 80 | `SC.SBS.CGT.BASE.AMT` | `SecTrade_CgtBaseAmt` |  |  |  |
| 81 | `SC.SBS.CGT.CODE` | `SecTrade_CgtCode` |  |  |  |
| 82 | `SC.SBS.CGT.TAX.RATE` | `SecTrade_CgtTaxRate` |  |  |  |
| 83 | `SC.SBS.CGT.TAX.LCL` | `SecTrade_CgtTaxLcl` |  |  |  |
| 84 | `SC.SBS.CGT.TAX.AMT` | `SecTrade_CgtTaxAmt` |  |  |  |
| 85 | `SC.SBS.CGT.PARAM.COND` | `SecTrade_CgtParamCond` |  |  |  |
| 86 | `SC.SBS.CGT.SRC.LCL.TAX` | `SecTrade_CgtSrcLclTax` |  |  |  |
| 87 | `SC.SBS.ODD.RTS.CGT` | `SecTrade_OddRtsCgt` |  |  |  |
| 88 | `SC.SBS.DISCOUNT.AMOUNT` | `SecTrade_DiscountAmount` |  |  |  |
| 89 | `SC.SBS.EXT.CUSTODIAN` | `SecTrade_ExtCustodian` |  |  |  |
| 90 | `SC.SBS.RP.REFERENCE` | `SecTrade_RpReference` |  |  |  |
| 91 | `SC.SBS.MV.RESERVED01` | `SecTrade_MvReserved01` |  |  |  |
| 92 | `SC.SBS.AUTO.CUST.SETT` | `SecTrade_AutoCustSett` |  |  |  |
| 93 | `SC.SBS.PORT.CONST.NO` | `SecTrade_PortConstNo` |  |  |  |
| 94 | `SC.SBS.CU.INCOME.ACC` | `SecTrade_CuIncomeAcc` |  |  |  |
| 95 | `SC.SBS.CU.INCOME.CCY` | `SecTrade_CuIncomeCcy` |  |  |  |
| 96 | `SC.SBS.CU.INCOME.AMT` | `SecTrade_CuIncomeAmt` |  |  |  |
| 97 | `SC.SBS.ACT.COMMISSION` | `SecTrade_ActCommission` |  |  |  |
| 98 | `SC.SBS.ALL.IN.COST` | `SecTrade_AllInCost` |  |  |  |
| 99 | `SC.SBS.CU.FTT.TYPE` | `SecTrade_CuFttType` |  |  |  |
| 100 | `SC.SBS.CU.FTT.PERC` | `SecTrade_CuFttPerc` |  |  |  |
| 101 | `SC.SBS.CU.FTT.BSE.AMT` | `SecTrade_CuFttBseAmt` |  |  |  |
| 102 | `SC.SBS.CU.FTT.AMT.TCY` | `SecTrade_CuFttAmtTcy` |  |  |  |
| 103 | `SC.SBS.CU.FTT.AMT.LCY` | `SecTrade_CuFttAmtLcy` |  |  |  |
| 104 | `SC.SBS.CU.FTT.AMT.CCY` | `SecTrade_CuFttAmtCcy` |  |  |  |
| 105 | `SC.SBS.CU.FTT.AMT` | `SecTrade_CuFttAmt` |  |  |  |
| 106 | `SC.SBS.CU.FTT.EX.RATE` | `SecTrade_CuFttExRate` |  |  |  |
| 107 | `SC.SBS.CU.CHARGE.TAX.TYPE` | `SecTrade_CuChargeTaxType` |  |  |  |
| 108 | `SC.SBS.CU.CHARGE.TAX.AMT` | `SecTrade_CuChargeTaxAmt` |  |  |  |
| 109 | `SC.SBS.CU.CHARGE.TAX.CODE` | `SecTrade_CuChargeTaxCode` |  |  |  |
| 110 | `SC.SBS.CU.SYS.CHARGE.TAX.AMT` | `SecTrade_CuSysChargeTaxAmt` |  |  |  |
| 111 | `SC.SBS.CU.CHARGE.TAX.QUAL` | `SecTrade_CuChargeTaxQual` |  |  |  |
| 112 | `SC.SBS.CU.RESERVED.4` | `SecTrade_CuReserved4` |  |  |  |
| 113 | `SC.SBS.CU.SUBS.ACCOUNT` | `SecTrade_CuSubsAccount` |  |  |  |
| 114 | `SC.SBS.TAXLOT.ALLOCATE` | `SecTrade_TaxlotAllocate` |  |  |  |
| 115 | `SC.SBS.QTY.ALLOTED` | `SecTrade_QtyAlloted` |  |  |  |
| 116 | `SC.SBS.CUSTOMER.LEI.NCI` | `SecTrade_CustomerLeiNci` |  |  |  |
| 117 | `SC.SBS.BROKER.NO` | `SecTrade_BrokerNo` |  |  |  |
| 118 | `SC.SBS.BROKER.TYPE` | `SecTrade_BrokerType` |  |  |  |
| 119 | `SC.SBS.BR.TRANS.CODE` | `SecTrade_BrTransCode` |  |  |  |
| 120 | `SC.SBS.BR.ACC.NO` | `SecTrade_BrAccNo` |  |  |  |
| 121 | `SC.SBS.BROKER.DEPO` | `SecTrade_BrokerDepo` |  |  |  |
| 122 | `SC.SBS.BR.SEC.DEPOT.AC` | `SecTrade_BrSecDepotAc` |  |  |  |
| 123 | `SC.SBS.BR.AGENT` | `SecTrade_BrAgent` |  |  |  |
| 124 | `SC.SBS.BR.AGENT.AC` | `SecTrade_BrAgentAc` |  |  |  |
| 125 | `SC.SBS.BR.NO.NOM` | `SecTrade_BrNoNom` |  |  |  |
| 126 | `SC.SBS.BR.PRICE` | `SecTrade_BrPrice` |  |  |  |
| 127 | `SC.SBS.BR.TRD.TIME` | `SecTrade_BrTrdTime` |  |  |  |
| 128 | `SC.SBS.BR.TOT.NOM` | `SecTrade_BrTotNom` |  |  |  |
| 129 | `SC.SBS.BR.GROSS.AM.SEC` | `SecTrade_BrGrossAmSec` |  |  |  |
| 130 | `SC.SBS.BR.GROSS.AM.TRD` | `SecTrade_BrGrossAmTrd` |  |  |  |
| 131 | `SC.SBS.BR.REALLOWANCE` | `SecTrade_BrReallowance` |  |  |  |
| 132 | `SC.SBS.BR.REALLOW.AMT` | `SecTrade_BrReallowAmt` |  |  |  |
| 133 | `SC.SBS.BR.INTR.AM.TRD` | `SecTrade_BrIntrAmTrd` |  |  |  |
| 134 | `SC.SBS.BR.GROSS.ACCR` | `SecTrade_BrGrossAccr` |  |  |  |
| 135 | `SC.SBS.BR.BROKER.COMM` | `SecTrade_BrBrokerComm` |  |  |  |
| 136 | `SC.SBS.BR.FOREIGN.FEE` | `SecTrade_BrForeignFee` |  |  |  |
| 137 | `SC.SBS.CL.COMMISSION` | `SecTrade_ClCommission` |  |  |  |
| 138 | `SC.SBS.BR.STAMP.TAX` | `SecTrade_BrStampTax` |  |  |  |
| 139 | `SC.SBS.BR.EBV.FEES` | `SecTrade_BrEbvFees` |  |  |  |
| 140 | `SC.SBS.BR.FEES.MISC` | `SecTrade_BrFeesMisc` |  |  |  |
| 141 | `SC.SBS.BR.NET.AM.TRD` | `SecTrade_BrNetAmTrd` |  |  |  |
| 142 | `SC.SBS.BR.EX.RATE.ACC` | `SecTrade_BrExRateAcc` |  |  |  |
| 143 | `SC.SBS.BR.ACCOUNT.CCY` | `SecTrade_BrAccountCcy` |  |  |  |
| 144 | `SC.SBS.BR.AMOUNT.DUE` | `SecTrade_BrAmountDue` |  |  |  |
| 145 | `SC.SBS.BR.DELIV.INSTR` | `SecTrade_BrDelivInstr` |  |  |  |
| 146 | `SC.SBS.BR.BEN.BANK.1` | `SecTrade_BrBenBank1` |  |  |  |
| 147 | `SC.SBS.BR.BEN.BANK.2` | `SecTrade_BrBenBank2` |  |  |  |
| 148 | `SC.SBS.BR.BEN.ADDR` | `SecTrade_BrBenAddr` |  |  |  |
| 149 | `SC.SBS.BR.BEN.ACCT` | `SecTrade_BrBenAcct` |  |  |  |
| 150 | `SC.SBS.CUST.REMARKS` | `SecTrade_CustRemarks` |  |  |  |
| 151 | `SC.SBS.BR.OVE.ADDR` | `SecTrade_BrOveAddr` |  |  |  |
| 152 | `SC.SBS.BR.MESS.CONTROL` | `SecTrade_BrMessControl` |  |  |  |
| 153 | `SC.SBS.CONF.BY.BROKER` | `SecTrade_ConfByBroker` |  |  |  |
| 154 | `SC.SBS.BR.DELIV.KEY` | `SecTrade_BrDelivKey` |  |  |  |
| 155 | `SC.SBS.BR.ORDER.NOS` | `SecTrade_BrOrderNos` |  |  |  |
| 156 | `SC.SBS.BR.NARRATIVE` | `SecTrade_BrNarrative` |  |  |  |
| 157 | `SC.SBS.BR.CAP.INT.AMT` | `SecTrade_BrCapIntAmt` |  |  |  |
| 158 | `SC.SBS.BR.UNF.GROSS` | `SecTrade_BrUnfGross` |  |  |  |
| 159 | `SC.SBS.BR.UNF.SEC.GROS` | `SecTrade_BrUnfSecGros` |  |  |  |
| 160 | `SC.SBS.BR.COUP.TAX.AMT` | `SecTrade_BrCoupTaxAmt` |  |  |  |
| 161 | `SC.SBS.STAMP.INDICATOR` | `SecTrade_StampIndicator` |  |  |  |
| 162 | `SC.SBS.BR.CONF.REF` | `SecTrade_BrConfRef` |  |  |  |
| 163 | `SC.SBS.AUTO.BROK.SETT` | `SecTrade_AutoBrokSett` |  |  |  |
| 164 | `SC.SBS.BUYR.SELLER` | `SecTrade_BuyrSeller` |  |  |  |
| 165 | `SC.SBS.BUYR.SELLER.AC` | `SecTrade_BuyrSellerAc` |  |  |  |
| 166 | `SC.SBS.PL.CODE` | `SecTrade_PlCode` |  |  |  |
| 167 | `SC.SBS.PL.SAFEKEEP` | `SecTrade_PlSafekeep` |  |  |  |
| 168 | `SC.SBS.BR.FTT.TYPE` | `SecTrade_BrFttType` |  |  |  |
| 169 | `SC.SBS.BR.FTT.PERC` | `SecTrade_BrFttPerc` |  |  |  |
| 170 | `SC.SBS.BR.FTT.BSE.AMT` | `SecTrade_BrFttBseAmt` |  |  |  |
| 171 | `SC.SBS.BR.FTT.AMT.TCY` | `SecTrade_BrFttAmtTcy` |  |  |  |
| 172 | `SC.SBS.BR.FTT.AMT.LCY` | `SecTrade_BrFttAmtLcy` |  |  |  |
| 173 | `SC.SBS.BR.FTT.AMT.CCY` | `SecTrade_BrFttAmtCcy` |  |  |  |
| 174 | `SC.SBS.BR.FTT.AMT` | `SecTrade_BrFttAmt` |  |  |  |
| 175 | `SC.SBS.BR.FTT.EX.RATE` | `SecTrade_BrFttExRate` |  |  |  |
| 176 | `SC.SBS.BR.CHARGE.TAX.TYPE` | `SecTrade_BrChargeTaxType` |  |  |  |
| 177 | `SC.SBS.BR.CHARGE.TAX.AMT` | `SecTrade_BrChargeTaxAmt` |  |  |  |
| 178 | `SC.SBS.BR.CHARGE.TAX.CODE` | `SecTrade_BrChargeTaxCode` |  |  |  |
| 179 | `SC.SBS.BR.SYS.CHARGE.TAX.AMT` | `SecTrade_BrSysChargeTaxAmt` |  |  |  |
| 180 | `SC.SBS.BR.CHARGE.TAX.QUAL` | `SecTrade_BrChargeTaxQual` |  |  |  |
| 181 | `SC.SBS.BR.RESERVED.5` | `SecTrade_BrReserved5` |  |  |  |
| 182 | `SC.SBS.BR.CHG.AMT.ACCOUNT` | `SecTrade_BrChgAmtAccount` |  |  |  |
| 183 | `SC.SBS.BR.CHG.AMT.TRD.CCY` | `SecTrade_BrChgAmtTrdCcy` |  |  |  |
| 184 | `SC.SBS.BR.CHG.AMT.ACC.CCY` | `SecTrade_BrChgAmtAccCcy` |  |  |  |
| 185 | `SC.SBS.BR.CHG.AMT.EX.RATE` | `SecTrade_BrChgAmtExRate` |  |  |  |
| 186 | `SC.SBS.STAMP.PRICE` | `SecTrade_StampPrice` |  |  |  |
| 187 | `SC.SBS.DEP.DELIV.KEY` | `SecTrade_DepDelivKey` |  |  |  |
| 188 | `SC.SBS.DEP.DELIV.REF` | `SecTrade_DepDelivRef` |  |  |  |
| 189 | `SC.SBS.SETT.NARRATIVE` | `SecTrade_SettNarrative` |  |  |  |
| 190 | `SC.SBS.TRADE.TIME` | `SecTrade_TradeTime` | TField | No | This field will be defaulted from the most recent input to the BR.TRADE.TIME field (if any). If the SEC.TRADE hasbeen generated by a SC.EXE.SEC.ORDERS record, then the first multi-value of BR.TRADE.TIME(if any)will be defaultedinto TRADE.TIME. The value of TRADE.TIME can be overtyped by the user. If this field was previously blank and the TRADE.TIME.FLAG in SC.STD.SEC.TRADE is set to 'YES', then the currentsystem time will be defaulted into this field. If the TRADE.TIME.FLAG is set to 'YES' then a value of "NONE" may be typed if no time of execution is available. Validation Rules: Up to 9 T24 Time characters. Recorded in HH:MM:SS:DDDDD format. The ":" may be omitted Input of three validcharacterswill attract a leading "0". Optional field if TRADE.TIME not set to "Y" on the SC.STD.SEC.TRADE file. |
| 191 | `SC.SBS.TRADE.CURR` | `SecTrade_TradeCurr` |  |  |  |
| 192 | `SC.SBS.CONSOL.AMT` | `SecTrade_ConsolAmt` |  |  |  |
| 193 | `SC.SBS.SETTLE.CURR` | `SecTrade_SettleCurr` |  |  |  |
| 194 | `SC.SBS.CONSOL.RATE` | `SecTrade_ConsolRate` |  |  |  |
| 195 | `SC.SBS.SETTLE.AMT` | `SecTrade_SettleAmt` |  |  |  |
| 196 | `SC.SBS.CON.VAL.DATE` | `SecTrade_ConValDate` |  |  |  |
| 197 | `SC.SBS.LINK.REFERENCE` | `SecTrade_LinkReference` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 12 characters may be entered. |
| 198 | `SC.SBS.CUM.EX.IND` | `SecTrade_CumExInd` |  |  |  |
| 199 | `SC.SBS.BND.RND.METH` | `SecTrade_BndRndMeth` | TField |  | When calculating the accrued interest on a bond, certain rounding parameters can be taken into account in thecalculation. If a bond rounding method has been used then the method used will be stored in this field. Validation Rules: NOINPUT field |
| 200 | `SC.SBS.CPTY.LIMIT.REF` | `SecTrade_CptyLimitRef` | TField | No | The limit reference related to the Counterparty (broker). Input is only allowed if the following conditions apply:- - at least one customer number relates to a banks owntrading book - only one broker is input - the delivery instructions record for the broker indicates thatcounterparty limit processing applies If the above conditions apply then on validation a limit reference will be obtained for the broker. If no limitreference can be obtained then an overrride will be generated. If a limit reference has been obtained then limit checking will take place with overrides generated whenrelevant. The amount used to update limits will be the BR.NET.AM.TRD value. The limits are defined on LIMIT.PARAMETER for the SEC.TRADE application. It is envisaged that the limit product will be dependant on the delivery instructions and whether the trade isfor bonds or shares. Validation Rules: Optional Input. 3 to 7 numeric characters limit reference code. Input in this field must be a valid limitreference number. If no limit exists then an override will be generated. |
| 201 | `SC.SBS.FACTOR` | `SecTrade_Factor` | TField |  | This field will contain the factor that used by the system in the calculation of the consideration for bonds thatuse factors. Validation Rules: No Input allowed Automatically updated |
| 202 | `SC.SBS.CG.TRADE.TIME` | `SecTrade_CgTradeTime` | TField |  | This field enables you to specify an alternative time for any SEC.TRADE undergoing Capital Gains tax processingshould this particular process have been requested within the SC.PARAMETER file field, CG.BASE.UPDATE. If left empty and the TRADE.TIME field is populated then that time(the HH:MM portion) will be defaulted into theCG.TRADE.TIME field. If TRADE.TIME is empty, then CG.TRADE.TIME will also be empty and will require manual input should you wish tospecify a particular time. Input without a time specified is acceptable to the System but you should be aware thatthis will cause the time of actual input to determine the location of the transaction in the Captal Gains taxtransaction file, CG.TXN.BASE Validation Rules: Numeric values from 0 through 9 Formatted so as to give HH:MM although the ":" may be omitted Input of 3 numeric characters will attract a leading "0" so that 745 or 7:45 becomes "07:45" Input of 2 numeric characters separated by a ":" will cause BOTH characters to attract a leading "0" so that aninput of, say, "6:5" becomes "06:05". |
| 203 | `SC.SBS.PAYMENT.REQD` | `SecTrade_PaymentReqd` | TField |  | This field specifies whether a customer payment is to be made. The default is set in the ADVICE.DEFAULT field inthe SC.PARAMETER file. Validation Rules: YES/NO |
| 204 | `SC.SBS.BROKER.ADVICE.REQD` | `SecTrade_BrokerAdviceReqd` | TField |  | This field specifies whether a broker advice is to be sent. The default is set in the ADVICE.DEFAULT field in theSC.PARAMETER file. Validation Rules: YES/NO |
| 205 | `SC.SBS.DEPOT.ADVICE.REQD` | `SecTrade_DepotAdviceReqd` | TField |  | This field specifies whether a depository advice is to be produced. The default is set in the ADVICE.DEFAULTfield in the SC.PARAMETER file. Validation Rules: Allowed Values : YES, NO, CLIENT, BOTH CLIENT / BOTH option is allowed only for brokerage only portfolio |
| 206 | `SC.SBS.CASH.HOLD.SETTLE` | `SecTrade_CashHoldSettle` | TField |  | CASH.HOLD.SETTLE will be used to control whether cash will update the SC.SETTLEMENT application. Validation Rules: CASH.HOLD.SETTLE will allow input of YES or NO only. If the ACTUAL.SETTLEMENT field on the SC.PARAMETER record is NO then CASH.HOLD.SETTLE will be no-input fieldthat will default to NO. If the CASH.HOLD.SETTLE field is YES then the cash accounting will use actual settlement . If SEC.TRADE transaction is authorised with CASH.HOLD.SETTLE field set to YES then the system will create aSC.SETTLEMENT record from the transaction.SC.SETTLEMENT records will be created with an unauthorised status.Thecash settlement can be recorded using the AMT.RECD.PAID field in SC.SETTLEMENT. |
| 207 | `SC.SBS.SEC.HOLD.SETTLE` | `SecTrade_SecHoldSettle` | TField |  | SEC.HOLD.SETTLE will be used to control whether stock will update the SC.SETTLEMENT application. Validation Rules: SEC.HOLD.SETTLE will allow input of YES or NO only. If the ACTUAL.SETTLEMENT field on the SC.PARAMETER record is NO then SEC.HOLD.SETTLE will be no-input field thatwill default to NO. If SEC.TRADE transaction is authorised with SEC.HOLD.SETTLE field set to YES then the system will create aSC.SETTLEMENT record from the transaction.SC.SETTLEMENT records will be created with an unauthorised status.Thestock settlement can be recorded using the NOM.RECD.DEL field in SC.SETTLEMENT. If the user has input YES in the SEC.HOLD.SETTLE field of a transaction and consequently is processing the stocknominal through actual settlement then the system will update UNSETTLE.NOMINAL field on the SECURITY.POSITION filewith the nominal of the transaction when the SC.SETTLEMENT record is created. Where the security position is beingadded to (a purchase for example) this field will be credited with the stock. Where the security position is beingdebited (a sell for example) this field will be debited with the nominal. |
| 208 | `SC.SBS.CUST.ACT.SUSP.CAT` | `SecTrade_CustActSuspCat` | TField |  | This field is used as a category reference for the customer.The suspense amount of the customer is posted to it. The value is picked up from the SC.PARAMETER which holds a similar field in it. The value is defaulted from theSC.PARAMETER fields. Validation Rules: The value in this field should be a valid entry in CATEGORY file. |
| 209 | `SC.SBS.BROK.ACT.SUSP.CAT` | `SecTrade_BrokActSuspCat` | TField |  | This field is used as a category reference for the broker. The suspense amount of the broker is posted to it. The value is picked up from the SC.PARAMETER which holds a similar field in it. The value is defaulted from theSC.PARAMETER fields. Validation Rules: The value in this field should be a valid entry in CATEGORY file. |
| 210 | `SC.SBS.MISC.ACT.SUSP.CAT` | `SecTrade_MiscActSuspCat` | TField |  | This field is used as a category reference for miscellaneous. The suspense amount of miscellaneous is posted toit. The value is picked up from the SC.PARAMETER which holds a similar field in it. The value is defaulted from theSC.PARAMETER fields. Validation Rules: The value in this field should be a valid entry in CATEGORY file. |
| 211 | `SC.SBS.ODD.LOT.TRADE` | `SecTrade_OddLotTrade` | TField |  | This field indicates if the order is an order of odd lot or not. The values allowed are : - YES : Odd lot order. No check is done for trading unit. But the order is validated against the 3 SECURITYMASTER fields added for odd lot process : ODD.LOT.TRADE, ODD.LOT.BROKER, ODD.LOT.EXCHANGE - NO : 'Normal' order. The trading unit will be checked. If the number of shares is not divisible by the tradingunit of the security, then the order is rejected. - BLANK : Default equivalent to NO. when the trade is generated from an order, this field will be automatically updated with field ODD.LOT.ORDER,field from SEC.OPEN.ORDER Validation Rules: |
| 212 | `SC.SBS.FUND.ID` | `SecTrade_FundId` | TField |  | Mutual fund id. |
| 213 | `SC.SBS.PSET` | `SecTrade_Pset` | TField |  | New field added for depository messages This field is used to determine the place of settlement in MT540-MT543 messages. Validation Rules: Text of up to 15 characters can be entered. |
| 214 | `SC.SBS.CONTRA.BY.REF` | `SecTrade_ContraByRef` |  |  |  |
| 215 | `SC.SBS.TO.CONTRA.REF` | `SecTrade_ToContraRef` | TField |  | Field specifying whether the transaction being entered is a contra for an existing sec trade which requirescertain modifications/amendments. Validation Rules: Must exist as a valid sec trade transaction on the sec trade file |
| 216 | `SC.SBS.BULK.PROCESSING` | `SecTrade_BulkProcessing` | TField |  | If set to YES then the accounting relating to this transaction will be authorised by the service SC.BULK.PROCESS. |
| 217 | `SC.SBS.WHT.TAX.CODE` | `SecTrade_WhtTaxCode` | TField |  | Indicates the Tax code from the TAX.TYPE.CONDITION / TAX file. Defaults from the field SHARE.TAX / BOND.TAX fromthe file TXN.TAX.CODE. Validation Rules: No input field |
| 218 | `SC.SBS.SEGMENT` | `SecTrade_Segment` | TField |  | Segment, associated with dealer desk. |
| 219 | `SC.SBS.DEF.DEAL.DESK` | `SecTrade_DefDealDesk` | TField |  | Defaulted dealer desk for this trade. |
| 220 | `SC.SBS.ACT.DEAL.DESK` | `SecTrade_ActDealDesk` | TField |  | Actual dealer desk that actioned the trade. |
| 221 | `SC.SBS.INT.CTR` | `SecTrade_IntCtr` | TField |  | Interest counter from security details. |
| 222 | `SC.SBS.CU.NAV.TYPE` | `SecTrade_CuNavType` | TField |  | Net asset value type for associated customer. |
| 223 | `SC.SBS.TREASURY.PRICE` | `SecTrade_TreasuryPrice` | TField |  | Treasury price, used to calculate treasury and market P&amp;L. |
| 224 | `SC.SBS.SERVICE.REF` | `SecTrade_ServiceRef` | TField |  | The reference number if the SEC.TRADE has been created by a service. |
| 225 | `SC.SBS.THREAD.KEY` | `SecTrade_ThreadKey` | TField |  | The thread key if the SEC.TRADE has been created by a service. |
| 226 | `SC.SBS.MARGIN.FACTOR` | `SecTrade_MarginFactor` | TField |  | This field used in the calculation of consideration using the Columbian Yield Method. |
| 227 | `SC.SBS.PARENT` | `SecTrade_Parent` | TField |  | Allowed value is YES. This Field is to determine whether the order is a parent order. |
| 228 | `SC.SBS.PARENT.REFERENCE` | `SecTrade_ParentReference` | TField |  | This fields contains alphanumeric Value Unique parent reference that is common for both parent and child orders and will serve as a link. |
| 229 | `SC.SBS.REVERSE.CHILD` | `SecTrade_ReverseChild` | TField |  | Allowed value is YES This Field is used to reverse the child transaction |
| 230 | `SC.SBS.SUP.MIS.SUSP` | `SecTrade_SupMisSusp` | TField |  | If this field is set, then miscellaneous entries like TAX, Commission or Charges etc will be raised to therespective PL categories instead of MISC.ACT.SUSP.CAT defined in SEC.TRADE for actual settlement This field will be defaulted from SC.PARAMETER Validation Rules Allowed value is Y or Null Input allowed only if CASH.HOLD.SETTLE is set to YES |
| 231 | `SC.SBS.SPRTY.NARR.QUAL` | `SecTrade_SprtyNarrQual` | TField |  | Qualifier pertaining to Setprty narrative in tag 70C,70D or 70E of SETPRTY block in MT540 to MT543. No validationwill be done against swift qualifier. |
| 232 | `SC.SBS.SPRTY.NARR` | `SecTrade_SprtyNarr` |  |  |  |
| 233 | `SC.SBS.BENE.OWNER` | `SecTrade_BeneOwner` | TField |  | Field to hold benefical ownership and will be mapped to tag 22F qualifier BENE in SETDET block. Value should be entered as per swift guidelines and core validation will not be performed. |
| 234 | `SC.SBS.BUYR.NATION` | `SecTrade_BuyrNation` | TField |  | Field to hold country of buyer and will be mapped to tag 95C in the qualifier INVE of OTHRPRTY block..The valueentered here will be validated against the country table |
| 235 | `SC.SBS.AUTHORISE.CHILD` | `SecTrade_AuthoriseChild` | TField |  | This field is used to specify whether child transactions can be authorised.If this field is YES, Parent ordershould be kept in INAU so that T24 service will authorise both child and parent.This field cannot be set as YES ifthere are no child transactions in exceptionZero authoriser version cannot be used in this caseThis field will alsobe used in conjunction with BULK.UPDATE field in order to perform bulk update and then authorizeparent and child Validation Rules Allowed values are YES |
| 236 | `SC.SBS.DELETE.CHILD` | `SecTrade_DeleteChild` | TField |  | This field is used to specify whether parent and child transactions are to be deleted. After inputting thisfield, order should be left in INAU so that service will delete the child and parent. Zero authoriser version cannot be usedin this case. This field cannot be set as YES if there are no child records in exception Validation Rules Allowed value is only YES |
| 237 | `SC.SBS.BULK.UPDATE` | `SecTrade_BulkUpdate` | TField |  | This field is used to specify whether bulk update is to be performed from parent to child. This field cannot beinput if SC.BULK.UPDATE.PARAMETER is not set for SEC.OPEN.ORDER This field can also be used in conjunction with AUTHORISE.CHILD to determine whether transactions are to beauthorised after performing bulk update. Zero authoriser version cannot be used and transaction should be left in INAU. In orderto perform bulk update, all transaction should be in unauthorised status Validation Rules Allowed value is only YES |
| 238 | `SC.SBS.UPFRONT.SEC` | `SecTrade_UpfrontSec` | TField |  | The field is set to Y when trade is created from SC.EXE.SEC.ORDERS for orders that have the field UPFRONT.SECset in SEC.OPEN.ORDER. This will be used to identify the trades for which a dummy security position has beenupdated pending NAV. The field will be made null once the processing is done using SC.BUILD.UPFRONT.POSITION (i.e. post the NAVupdate). Validation Rules: This field accepts Y or Null values. |
| 239 | `SC.SBS.SY.DX.REFERENCE` | `SecTrade_SyDxReference` | TField |  | A unique reference maintained for trade which will be common for the parent trade and its underlying such asSEC.TRADE/ FOREX/ DX.TRADE. Input to this field will update file SY.DX.LINK.FILE Validation Rules: |
| 240 | `SC.SBS.SY.TRANS.ID` | `SecTrade_SyTransId` | TField |  | Updated with SY.TRANSACTION reference through which the trade is created. Validation Rules: |
| 241 | `SC.SBS.SY.UNIT.ID` | `SecTrade_SyUnitId` | TField |  | Holds the SY.UNIT reference through which unit the trade is created Validation Rules: |
| 242 | `SC.SBS.PRINCIPAL.AGENT` | `SecTrade_PrincipalAgent` | TField |  | This field accepts the following values : PRINCIPAL - Indicates that the bank is acting as a principal in this transaction. AGENT - Indicates that the bank is acting as an agent in this transaction. If the customer is a dealerbook and if the field holds the value 'AGENT' then stamp tax will not be calculatedfor the customer. |
| 243 | `SC.SBS.INTEG.DATA.ITEM` | `SecTrade_IntegDataItem` |  |  |  |
| 244 | `SC.SBS.INTEG.DATA.VALUE` | `SecTrade_IntegDataValue` |  |  |  |
| 245 | `SC.SBS.DEPO.DELIV.INSTR` | `SecTrade_DepoDelivInstr` | TField |  | This field is used to hold delivery instruction such as against payment or free and is specifically used in caseof customer Vs customer trade and child trade where delivery messages are to be generated for depository |
| 246 | `SC.SBS.SSI.ID` | `SecTrade_SsiId` | TField |  | This field will have a valid SC.SETT.INSTRUCT ID and all the broker side details will be defaulted basedSC.SETT.INSTRUCT record of SSI.CODE. when ALLOW.DUPLICATE is set in SC.SSI.PARAM, this field accpets SSI.ID#Duplicate Combination Id |
| 247 | `SC.SBS.TXN.CHANNEL` | `SecTrade_TxnChannel` | TField |  | Holds the information on mode of channel used to enter into the order.Mapped from SC.EXE.SEC.ORDERS.List ofchannels can be configured through EB.LOOKUP with VIRTUAL.TABLE as SC.CHANNEL. Validation Rules: This is a NOINPUT field |
| 248 | `SC.SBS.COM.ORDER.REF` | `SecTrade_ComOrderRef` | TField |  | The field will hold a common reference to link a set of switch orders.Mapped from SEC.OPEN.ORDER Validation Rules: NOINPUT field |
| 249 | `SC.SBS.ORIGINAL.SEC` | `SecTrade_OriginalSec` | TField |  | This field holds Original Security used while placing order, when trade is created from SC.EXE.SEC.ORDERS thatinvolves upfront security. Validation Rules: NOINPUT field |
| 250 | `SC.SBS.AGGREGATION.REF` | `SecTrade_AggregationRef` | TField |  | When aggregation is set in the individual trades, this field will hold the ID of the main aggregated trade. In the main aggregated trade, this will hold the ID of the SP.RECONCILIATION record. When Aggregation Ref is created via DX Transactions, this field will be mapped to SP.AGGREGATION and DepoAdviceReqd will be updated to "No" since Depo message will be generated through SP.AGGR.LAUNCH. When Aggregation Ref is inputted manually without Parent Reference: This field will be mapped to SP.AGGREGATION and DepoAdviceReqd will be updated to "No" since Depo message will be generated through SP.AGGR.LAUNCH '*',' ', '.' are not allowed. |
| 251 | `SC.SBS.NEW.VALUE.DATE` | `SecTrade_NewValueDate` | TField |  | This field will hold the next working day whenever settlement is suspended during COB. System updated field which will be cycled further on each settlement suspension and this will continue till thetransaction is settled. This field will be used for reports and advices. No Input field |
| 252 | `SC.SBS.INVEST.OPTION.TYPE` | `SecTrade_InvestOptionType` | TField |  | The field is used to define the Invest option type derived from EB.LOOKUP table - SC.INV.OPT.TYPE. Option Depository defined for the respective invest option type will be defaulted in the Depository from Securitymaster table |
| 253 | `SC.SBS.CANCEL.BY.DATE` | `SecTrade_CancelByDate` | TField |  | Trade is allowed for cancellation until the date defined in this field. Field will be calculated based on cooling off period defined at SECURITY.MASTER for 1.Initial purchase for the portfolio in the instrument 2.Subsequent purchase for the same instrument by that portfolio and is within the Cancel by date of the initialpurchase. Validation Rules: NOINPUT field |
| 254 | `SC.SBS.CANCEL.TRADE.REF` | `SecTrade_CancelTradeRef` | TField |  | Trade reference that is to be cancelled.Will be mapped from SEC.OPEN.ORDER Validation Rules: NOINPUT field |
| 255 | `SC.SBS.IN.DELIVERY.REF` | `SecTrade_InDeliveryRef` | TField |  | This field will store the internal incoming MT541/543 delivery reference. |
| 256 | `SC.SBS.STP.FAIL.REASON` | `SecTrade_StpFailReason` |  |  |  |
| 257 | `SC.SBS.EAM.ID` | `SecTrade_EamId` | TField |  | External Asset Manager reference through which the transaction is input. Validation Rules: Valid CUSTOMER.SECURITY record with CUSTOMER.TYPE as EAM |
| 258 | `SC.SBS.DECISION.MKR.ID` | `SecTrade_DecisionMkrId` | TField |  |  |
| 259 | `SC.SBS.WAIVER.INDI` | `SecTrade_WaiverIndi` | TField |  |  |
| 260 | `SC.SBS.CG.TAX.EFF.DATE` | `SecTrade_CgTaxEffDate` | TField |  | Field to store Effective Date of transactions updated in CG.TXN.BASE |
| 261 | `SC.SBS.SUPP.EXCH.PL` | `SecTrade_SuppExchPl` | TField |  | If this field value is set to YES, the settlement exchange entries and suspense entries will be suppressed. This is applicable for cross currency trade where trade currency is different from settlement currency andsettlement currencies, exchange rates are same between customer and broker. For all other cases, if the field value is setto YES, then it will raise override |
| 262 | `SC.SBS.CG.EX.RATE.SETT` | `SecTrade_CgExRateSett` | TField |  |  |
| 263 | `SC.SBS.CU.AGENT` | `SecTrade_CuAgent` |  |  |  |
| 264 | `SC.SBS.CU.AGENT.AC` | `SecTrade_CuAgentAc` |  |  |  |
| 265 | `SC.SBS.CU.DEPO` | `SecTrade_CuDepo` | TField |  | This field will hold customer's delivering/receiving custodian.Defaulted from SC.SETT.INSTRUCT for the customer. Validation Rules: Input to this field is allowed only for brokerage only portfolio |
| 266 | `SC.SBS.CU.SEC.DEPOT.AC` | `SecTrade_CuSecDepotAc` | TField |  | This field will hold the customer's delivering/receiving custodian account number. Defaulted fromSC.SETT.INSTRUCT for the customer. Validation Rules: Input to this field is allowed only for brokerage only portfolio |
| 267 | `SC.SBS.CU.BUYR.SELLER` | `SecTrade_CuBuyrSeller` | TField |  | This field will hold the customer's Buyer/seller. Defaulted from SC.SETT.INSTRUCT for the customer. Validation Rules: Input to this field is allowed only for brokerage only portfolio |
| 268 | `SC.SBS.CU.BUYR.SELLER.AC` | `SecTrade_CuBuyrSellerAc` | TField |  | This field will hold the customer's Buyer/seller account number. Defaulted from SC.SETT.INSTRUCT for thecustomer. Validation Rules: Input to this field is allowed only for brokerage only portfolio |
| 269 | `SC.SBS.CU.PSET` | `SecTrade_CuPset` | TField |  | This field will hold the place of settlement of the customer. Defaulted from SC.SETT.INSTRUCT for the customer. Validation Rules: Input to this field is allowed only for brokerage only portfolio |
| 270 | `SC.SBS.EXT.BROKER` | `SecTrade_ExtBroker` | TField |  | This field will capture the external broker for brokerage only transactions. Validation Rules: Must exist as a valid record within the Customer Security File |
| 271 | `SC.SBS.SEC.SSI.ID` | `SecTrade_SecSsiId` | TField |  | This field holds the Combination selected from SC.SETT.INSTRUCT table |
| 272 | `SC.SBS.LOCAL.REF` | `SecTrade_LocalRef` |  |  |  |
| 273 | `SC.SBS.STATEMENT.NOS` | `SecTrade_StatementNos` |  |  |  |
| 274 | `SC.SBS.OVERRIDE` | `SecTrade_Override` |  |  |  |
| 275 | `SC.SBS.RECORD.STATUS` | `SecTrade_RecordStatus` | String |  |  |
| 276 | `SC.SBS.CURR.NO` | `SecTrade_CurrNo` | String |  |  |
| 277 | `SC.SBS.INPUTTER` | `SecTrade_Inputter` |  |  |  |
| 278 | `SC.SBS.DATE.TIME` | `SecTrade_DateTime` |  |  |  |
| 279 | `SC.SBS.AUTHORISER` | `SecTrade_Authoriser` | String |  |  |
| 280 | `SC.SBS.CO.CODE` | `SecTrade_CoCode` | String |  |  |
| 281 | `SC.SBS.DEPT.CODE` | `SecTrade_DeptCode` | String |  |  |
| 282 | `SC.SBS.AUDITOR.CODE` | `SecTrade_AuditorCode` | String |  |  |
| 283 | `SC.SBS.AUDIT.DATE.TIME` | `SecTrade_AuditDateTime` | String |  |  |
| 284 | `SC.SBS.PSET.CLRN.CODE` | `SecTrade_PsetClrnCode` | TField |  | This field holds Clearing Code from SC.CLEARING.CODE and gets defaulted at transaction based on the PSET rule setup on Depository It is allowed to amend by user |
| 285 | `SC.SBS.PSET.COUNTRY` | `SecTrade_PsetCountry` | TField |  | This field holds Country code and gets defaulted at transaction based on the PSET rule setup on Depository It is allowed to amend by user |
| 286 | `SC.SBS.MKT.IND.QUALIFIER` | `SecTrade_MktIndQualifier` |  |  |  |
| 287 | `SC.SBS.MKT.IND.DSN` | `SecTrade_MktIndDsn` |  |  |  |
| 288 | `SC.SBS.MKT.INDICATOR` | `SecTrade_MktIndicator` |  |  |  |
| 289 | `SC.SBS.PO.BR.REFERENCE` | `SecTrade_PoBrReference` |  |  |  |
| 290 | `SC.SBS.END.BEN.NAME` | `SecTrade_EndBenName` |  |  |  |
| 291 | `SC.SBS.END.BEN.ACC` | `SecTrade_EndBenAcc` |  |  |  |
| 292 | `SC.SBS.END.BEN.BIC` | `SecTrade_EndBenBic` |  |  |  |
| 293 | `SC.SBS.SENDER.RECEIVER.INFO` | `SecTrade_SenderReceiverInfo` |  |  |  |
| 294 | `SC.SBS.CASH.SSI.ID` | `SecTrade_CashSsiId` | TField |  | This field holds the valid SC.CASH.SSI.INSTRUCT ID and all the Beneficiary details will be defaulted basedvalid SSI ID combination. when ALLOW.DUPLICATE is set in SC.SSI.PARAM, this field accpets CASH.SSI.ID#Duplicate Combination Id |
| 295 | `SC.SBS.SYS.CASH.SSI.ID` | `SecTrade_SysCashSsiId` | TField |  | This field holds the Combination selected by the system from SC.CASH.SSI.INSTRUCT table for the transaction NoInput field |
| 296 | `SC.SBS.CHARGE.GROUP` | `SecTrade_ChargeGroup` | TField |  | This field holds the generic charge group id of SCTR.GROUP.CONDITION record When the field is manually inputted with generic id that starts with G-Upto 6 Numeric values, SCTR.GROUP.CONDITION will be directly referred using this field value when the field is blank, CUSTOMER.CHARGE is read for the customer to get the SCTR.GROUP.CONDITION id from SC.ACT.GROUP field Validations User has to manually input this field to accept Generic group id of SCTR.GROUP.CONDITION table Value should be a valid record id from SCTR.GROUP.CONDITION record |
| 297 | `SC.SBS.TRADING.VENUE` | `SecTrade_TradingVenue` |  |  |  |
| 298 | `SC.SBS.RESERVED.3` | `SecTrade_Reserved3` |  |  |  |
| 299 | `SC.SBS.SAFEKEEP.ACCT.NO` | `SecTrade_SafekeepAcctNo` |  |  |  |
| 300 | `SC.SBS.SAFEKEEP.FEE.LCY` | `SecTrade_SafekeepFeeLcy` |  |  |  |
| 301 | `SC.SBS.SK.ACY.LCY.RATE` | `SecTrade_SkAcyLcyRate` |  |  |  |
| 302 | `SC.SBS.SAFEKEEP.FEE.ACY` | `SecTrade_SafekeepFeeAcy` |  |  |  |
| 303 | `SC.SBS.LEI.NCI.CHK.REQ` | `SecTrade_LeiNciChkReq` | TField |  |  |
| 304 | `SC.SBS.SUB.ACC.EXT.ID` | `SecTrade_SubAccExtId` |  |  |  |
