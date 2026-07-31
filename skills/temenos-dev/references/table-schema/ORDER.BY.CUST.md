# ORDER.BY.CUST — Table Schema

> Source: `INSERTS/I_F.ORDER.BY.CUST` in `SC_SctModelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ORD.ORDER.TYPE` | `OrderByCust_OrderType` | TField | Yes | Type of order. Currently four type of order can be specified with ORDER.BY.CUST. PURCHASE create order(s) for the purchase of 1 security SELL create order(s) for the sale of 1 security SWITCH create orders for the sale of one or more securities and the purchase of one or more other securities with the anticipated proceeds of the sale. Note ; Both the buy and sell sides of the order will be specificed on a single ORDER.BY.CUST record. CASH Create an order to specify the sale of all securities to a given percentage to generate cash for the portfolio concerned. TARGET Create orders to ensure that the holding for the specified security is the PERCENTAGE specified of the valuation amount. You will either BUY or SELL to achieve that percentage. PURCHASE.INCR Increase the holdings of the specified security by the PERCENTAGE specified. SELL.PERC Sell the PERCENTAGE of the valuation amount in the specified security. If this value is greater than the holdings in the security, SELL all that is held. Validation Rules: Mandatory input. Input must be one of the above order types |
| 2 | `SC.ORD.DEPT.ACCT.OFF` | `OrderByCust_DeptAcctOff` |  |  |  |
| 3 | `SC.ORD.FIELD.SELECT` | `OrderByCust_FieldSelect` |  |  |  |
| 4 | `SC.ORD.FIELD.OPERATOR` | `OrderByCust_FieldOperator` |  |  |  |
| 5 | `SC.ORD.FIELD.OPERAND` | `OrderByCust_FieldOperand` |  |  |  |
| 6 | `SC.ORD.SOO.ORDER.TYPE` | `OrderByCust_SooOrderType` | TField |  | This input details the type of Order being passed to the dealers. Whether buy or sell at BEST or at MARKET price. A buy or sell instruction to a dealer with the at Market flag signifies that there is no limit or restriction on the price at which he can execute the transaction. The client or investment manager is happy with the market price. Best price indicates that the dealer ought really to shop around for his price as there may be a lot of activity and consequently differing prices to be achieved. Price indicates that the price input within field 9 is a minimum or maximum price to be paid or received for the securities stipulated. Validation Rules: : Should be a valid record in SC.ORDER.TYPE. CASH type order is not allowed. |
| 7 | `SC.ORD.SECURITY.NO.DB` | `OrderByCust_SecurityNoDb` |  |  |  |
| 8 | `SC.ORD.SECURITY.CCY.DB` | `OrderByCust_SecurityCcyDb` |  |  |  |
| 9 | `SC.ORD.MARKET.PRICE` | `OrderByCust_MarketPrice` |  |  |  |
| 10 | `SC.ORD.SETTLE.CCY.DB` | `OrderByCust_SettleCcyDb` |  |  |  |
| 11 | `SC.ORD.EXCH.RATE.DB` | `OrderByCust_ExchRateDb` |  |  |  |
| 12 | `SC.ORD.LIMIT.PRICE.DB` | `OrderByCust_LimitPriceDb` |  |  |  |
| 13 | `SC.ORD.EXPIRY.DATE.DB` | `OrderByCust_ExpiryDateDb` |  |  |  |
| 14 | `SC.ORD.PERCENTAGE.DB` | `OrderByCust_PercentageDb` |  |  |  |
| 15 | `SC.ORD.TRADE.UNITS.DB` | `OrderByCust_TradeUnitsDb` |  |  |  |
| 16 | `SC.ORD.BROKER.NO.DB` | `OrderByCust_BrokerNoDb` |  |  |  |
| 17 | `SC.ORD.STOCK.EXCH.DB` | `OrderByCust_StockExchDb` |  |  |  |
| 18 | `SC.ORD.ROUND.FACTOR.DB` | `OrderByCust_RoundFactorDb` |  |  |  |
| 19 | `SC.ORD.MAXIMUM.LOT.DB` | `OrderByCust_MaximumLotDb` |  |  |  |
| 20 | `SC.ORD.MINIMUM.LOT.DB` | `OrderByCust_MinimumLotDb` |  |  |  |
| 21 | `SC.ORD.RESERVED.1.DB` | `OrderByCust_Reserved1Db` |  |  |  |
| 22 | `SC.ORD.SECURITY.NO.CR` | `OrderByCust_SecurityNoCr` |  |  |  |
| 23 | `SC.ORD.SECURITY.CCY.CR` | `OrderByCust_SecurityCcyCr` |  |  |  |
| 24 | `SC.ORD.MARKET.PRICE.CR` | `OrderByCust_MarketPriceCr` |  |  |  |
| 25 | `SC.ORD.SETTLE.CCY.CR` | `OrderByCust_SettleCcyCr` |  |  |  |
| 26 | `SC.ORD.EXCH.RATE.CR` | `OrderByCust_ExchRateCr` |  |  |  |
| 27 | `SC.ORD.LIMIT.PRICE.CR` | `OrderByCust_LimitPriceCr` |  |  |  |
| 28 | `SC.ORD.EXPIRY.DATE.CR` | `OrderByCust_ExpiryDateCr` |  |  |  |
| 29 | `SC.ORD.PERCENTAGE.CR` | `OrderByCust_PercentageCr` |  |  |  |
| 30 | `SC.ORD.TRADE.UNITS.CR` | `OrderByCust_TradeUnitsCr` |  |  |  |
| 31 | `SC.ORD.BROKER.NO.CR` | `OrderByCust_BrokerNoCr` |  |  |  |
| 32 | `SC.ORD.STOCK.EXCH.CR` | `OrderByCust_StockExchCr` |  |  |  |
| 33 | `SC.ORD.ROUND.FACTOR.CR` | `OrderByCust_RoundFactorCr` |  |  |  |
| 34 | `SC.ORD.MAXIMUM.LOT.CR` | `OrderByCust_MaximumLotCr` |  |  |  |
| 35 | `SC.ORD.MINIMUM.LOT.CR` | `OrderByCust_MinimumLotCr` |  |  |  |
| 36 | `SC.ORD.RESERVED.1.CR` | `OrderByCust_Reserved1Cr` |  |  |  |
| 37 | `SC.ORD.TRADER.CODE` | `OrderByCust_TraderCode` | TField |  | Specifies the dealer of the trading department for the order. This will get defaulted to SEC.OPEN.ORDER created for this order. Validation Rules: Should be a valid DEPT.ACCT.OFFICER |
| 38 | `SC.ORD.TRADER.DESC` | `OrderByCust_TraderDesc` |  |  |  |
| 39 | `SC.ORD.DEAL.STATUS` | `OrderByCust_DealStatus` | TField |  | Current status of the order. Validation Rules: : Values allowed are TRANSMITTED, TRADED, NULL |
| 40 | `SC.ORD.ORDER.NOMINAL` | `OrderByCust_OrderNominal` | TField | No | This is the Total Nominal to be Purchased or Sold . Validation Rules: Optional Input Must be entered if GROSS.AMT, PERCENTAGE or CASH.AMOUNT is not entered. |
| 41 | `SC.ORD.GROSS.AMOUNT` | `OrderByCust_GrossAmount` | TField | No | This is the Total Value of the required order Validation Rules: Optional Input Must be entered, if Order.Nominal or Percentage is not entered. |
| 42 | `SC.ORD.PERCENTAGE` | `OrderByCust_Percentage` | TField | No | This is the Percentage Value to be used in conjunction with the order type. Validation Rules: Percentage input will result in the generation of Nominals to this Percentage depending on the order type, e.g. Total Holding to equal input percentage Optional Input. Must be entered if ORDER.NOMINAL, GROSS.AMOUNT or CASH.AMOUNT is not entered. |
| 43 | `SC.ORD.CASH.AMOUNT` | `OrderByCust_CashAmount` | TField | No | The cash amount entered here will be applied to each portfolio selected will be used to determine the amount of nominal to trade. If field CU.CHRGS.DEF is set to GROSS then the system will take the cash amount, calculate the nominal then add any charges in addition to the CASH.AMOUNT. If field CU.CHRGS.DEF is set to NET then the system will take the cash amount work out the nominal based on all the charges being included in the CASH.AMOUNT. Validation Rules: Optional Input. Must be entered if ORDER.NOMINAL, GROSS.AMOUNT or PERCENTAGE is not entered. |
| 44 | `SC.ORD.CU.CHRGS.DEF` | `OrderByCust_CuChrgsDef` | TField | Yes | Determines how charges are applied to cash transactions only for calculating the Nominal amount. If set to GROSS the nominal is calculated then the charges are added to the CASH.AMOUNT. If set to NET the nominal is calculated so that the CASH.AMOUNT includes all charges. Validation Rules: Mandatory Input if CASH.AMOUNT field is used. NET or GROSS |
| 45 | `SC.ORD.CASH.ROUNDING` | `OrderByCust_CashRounding` | TField |  | Each time the NET option is used the system always tries to match the cash amount exactly, however, sometimes this is not possible this field determines what to do with the transaction. If set to UNDER/OVER the system will calculate to the nearest trading unit under the cash amount for a purchase to the nearest trading unit over the cash amount for a sale. If set to EXACT the system will then allow the user to use the ADJUST.COMMISSION field to determine whether to adjust the commission down to make the total trade equal the cash amount. Validation Rules: |
| 46 | `SC.ORD.ADJUST.COMMISSION` | `OrderByCust_AdjustCommission` | TField | Yes | If the CASH.ROUNDING field is set to EXACT then this field becomes active to determine whether to reduce the commission in order to make the total trade match the cash amount exactly. If set to YES and the value of the total trade does not match the cash amount, the system will check to see if there is enough commission to cover the difference between the two figures. If there is the system will reduce of commission (and tax on commission) to make the values match. If there is not enough commission to achieve this an error message will be displayed the user will have to choose another option if they require the trade to proceed. If set to NO and the value of the total trade does not match the cash amount an error message will be displayed the user will have to choose another option if they require the trade to proceed. Validation Rules: MANDATORY field if the CASH.ROUNDING field is set to EXACT otherwise a NOINPUT field. YES or NO |
| 47 | `SC.ORD.TARGET` | `OrderByCust_Target` | TField |  | Validation Rules: A maximum of 3 characters may be entered. The following values are permitted: YES NO |
| 48 | `SC.ORD.TRANS.TYPE.DB` | `OrderByCust_TransTypeDb` | TField |  | The transaction type of the SALE side of the order Validation Rules: Must exist on the SC.TRANS.NAME file. Must be defined on the SC.TRANS.TYPE field as a debit transaction. |
| 49 | `SC.ORD.TRANS.TYPE.CR` | `OrderByCust_TransTypeCr` | TField |  | The transaction type of the PURCHASE side of the order Validation Rules: Must exist on the SC.TRANS.NAME file. Must be defined on the SC.TRANS.TYPE application as a credit transaction. |
| 50 | `SC.ORD.ROUNDING.FACTOR` | `OrderByCust_RoundingFactor` | TField |  | This is is the Minimum Lot Size of the suggested Nominal for each portfolio. Validation Rules: If not enetered, will default Trading.Units from Security.Master. |
| 51 | `SC.ORD.POLICY.REQD` | `OrderByCust_PolicyReqd` | TField |  | For Purchase Order, the Portfolio Policy Parameter will be taken into account. Validation Rules: Reserved For Future Use |
| 52 | `SC.ORD.CASH.AVAIL.REQD` | `OrderByCust_CashAvailReqd` | TField | No | For Purchase Orders, the Customer Account Balance on any account in this currency will be looked at and used to calculate if the portfolio has enough cash for the order. If YES is input all currencies will be checked. If this field is left blank then no check against available cash will be made. Validation Rules: Optional Input Any input made must be a valid currency of YES. Default is blank, i.e. no cash availability check. |
| 53 | `SC.ORD.CASH.PCENT.LIMIT` | `OrderByCust_CashPcentLimit` | TField | No | For Purchase Orders, the user can specify how much of the portfolio balance is to remain as cash. Validation Rules: Optional Input Input will only be allowed in this field if the CASH.AVAIL.REQD field has had something entered into it. Input must be in the range 0 - 100 |
| 54 | `SC.ORD.MAXIMUM.LOT` | `OrderByCust_MaximumLot` | TField | No | For Purchase Orders, allows the user to specify the Maximum nominal that will be allotted to a single portfolio. This field will be used to amend the calculated theoretical nominal field to ensure that the order nominal is not greater than this figure. Validation Rules: Optional Input. Input should be positive and exactly divisable by the ROUNDING.FACTOR Anything input into this field must be greater than any input in the MINIMUM.LOT field if input has been made into both. |
| 55 | `SC.ORD.MINIMUM.LOT` | `OrderByCust_MinimumLot` | TField | No | For Purchase Orders, allows the user to specify the Minimum nominal that will be allotted to a single portfolio. This field will be used to amend the calculated theoretical nominal field to ensure that the order nominal is not less than this figure. Validation Rules: Does not apply for PURCHASE.INCR order types where the current position is zero. Optional Input. Input should be positive and exactly divisable by the ROUNDING.FACTOR Anything input into this field must be less than any input in the MAXIMUM.LOT field if input has been made into both. |
| 56 | `SC.ORD.ARBITRAGE` | `OrderByCust_Arbitrage` | TField |  | This field is used to generate a Arbitage Order using the customers and order value. of a previous Sell Order.By.Cust |
| 57 | `SC.ORD.ALL.VIEW` | `OrderByCust_AllView` | TField | No | This field is used to show or hide suggested orders with a zero nominal. If YES or not set then zero nominal orders will be shown. Optional Input, Default is YES |
| 58 | `SC.ORD.AUTO.SELECT` | `OrderByCust_AutoSelect` | TField |  | Input of Y, will generate/re-generate portfolios with suggested nominals to complete the Total Order SERVICE option will generate the order via a service. Validation Rules: Option Input If this field is not entered - For New Input - No Portfolios will be generated For Amend Input - previously generated porfolios and nominals will not be altered. |
| 59 | `SC.ORD.ORDER.PRESENT` | `OrderByCust_OrderPresent` | TField |  | This field determines the order of display for the suggested orders. If SECURITY is selected then orders will be shown in SECURITY order, i.e. field SECURITY.NO will contain unique multi-values containing sub-values for each SEC.ACC.NO listing each portfolio. If the value is PORTFOLIO then the orders will be displayed in PORTFOLIO order, i.e. SECURITY.NO will be repeated for each portfolio and each portfolio will be listed as a sub-value within the SECURITY multi-value. Validation Rules: The following values are permitted: SECURITY or PORTFOLIO |
| 60 | `SC.ORD.SECURITY.NO` | `OrderByCust_SecurityNo` |  |  |  |
| 61 | `SC.ORD.SEC.ACC.NO` | `OrderByCust_SecAccNo` |  |  |  |
| 62 | `SC.ORD.INVEST.PROG` | `OrderByCust_InvestProg` |  |  |  |
| 63 | `SC.ORD.VALUE` | `OrderByCust_Value` |  |  |  |
| 64 | `SC.ORD.TRANS.TYPE` | `OrderByCust_TransType` |  |  |  |
| 65 | `SC.ORD.THEOR.NOM` | `OrderByCust_TheorNom` |  |  |  |
| 66 | `SC.ORD.NOMINAL` | `OrderByCust_Nominal` |  |  |  |
| 67 | `SC.ORD.CU.CASH.AMT` | `OrderByCust_CuCashAmt` |  |  |  |
| 68 | `SC.ORD.CALC.CHRGS` | `OrderByCust_CalcChrgs` |  |  |  |
| 69 | `SC.ORD.CASH.CHRGS` | `OrderByCust_CashChrgs` |  |  |  |
| 70 | `SC.ORD.SPLIT.CHRGS` | `OrderByCust_SplitChrgs` |  |  |  |
| 71 | `SC.ORD.CU.BRKR.COMM` | `OrderByCust_CuBrkrComm` |  |  |  |
| 72 | `SC.ORD.CU.FOR.FEE` | `OrderByCust_CuForFee` |  |  |  |
| 73 | `SC.ORD.CU.COMM` | `OrderByCust_CuComm` |  |  |  |
| 74 | `SC.ORD.CU.COMM.TAX` | `OrderByCust_CuCommTax` |  |  |  |
| 75 | `SC.ORD.CU.STAMP.TAX` | `OrderByCust_CuStampTax` |  |  |  |
| 76 | `SC.ORD.CU.EBV.FEES` | `OrderByCust_CuEbvFees` |  |  |  |
| 77 | `SC.ORD.CU.FEES.MISC` | `OrderByCust_CuFeesMisc` |  |  |  |
| 78 | `SC.ORD.CU.DISC.PCNT` | `OrderByCust_CuDiscPcnt` |  |  |  |
| 79 | `SC.ORD.CU.DISC.AMT` | `OrderByCust_CuDiscAmt` |  |  |  |
| 80 | `SC.ORD.COMM.CODE` | `OrderByCust_CommCode` |  |  |  |
| 81 | `SC.ORD.COMM.PERCENT` | `OrderByCust_CommPercent` |  |  |  |
| 82 | `SC.ORD.COM.TAX.CODE` | `OrderByCust_ComTaxCode` |  |  |  |
| 83 | `SC.ORD.COM.TAX.BCUR` | `OrderByCust_ComTaxBcur` |  |  |  |
| 84 | `SC.ORD.COM.TAX.XRTE` | `OrderByCust_ComTaxXrte` |  |  |  |
| 85 | `SC.ORD.MARKET.VALUE` | `OrderByCust_MarketValue` |  |  |  |
| 86 | `SC.ORD.PORT.PERCENT` | `OrderByCust_PortPercent` |  |  |  |
| 87 | `SC.ORD.DEPOSITORY` | `OrderByCust_Depository` |  |  |  |
| 88 | `SC.ORD.POLICY.AMT` | `OrderByCust_PolicyAmt` |  |  |  |
| 89 | `SC.ORD.CASH.BALANCE` | `OrderByCust_CashBalance` |  |  |  |
| 90 | `SC.ORD.EXT.CUSTODIAN` | `OrderByCust_ExtCustodian` |  |  |  |
| 91 | `SC.ORD.WHT.TAX.CODE` | `OrderByCust_WhtTaxCode` |  |  |  |
| 92 | `SC.ORD.SEC.ORDER.KEY` | `OrderByCust_SecOrderKey` |  |  |  |
| 93 | `SC.ORD.ORDER.DATE` | `OrderByCust_OrderDate` | TField |  | This field may be used to enter a date should the date required differ from todays date. If a date is entered, then that date will filter through on verification of the ORDER.BY.CUST transaction and be recorded on the resultant SEC.OPEN.ORDER transaction field of the same name. If not entered, then following successful verification, the resultant SEC.OPEN.ORDER will contain the date on which the verification was performed. Validation Rules: Must be a valid date |
| 94 | `SC.ORD.ORDER.TIME` | `OrderByCust_OrderTime` | TField | No | This is an optional field where you may record the time the order was arranged. If entered, the time will, upon successful verification, filter through to the resultant SEC.OPEN.ORDER transaction. Validation Rules: Time is stored in HH:MM:SS format and may be entered in that format. You may also enter the time in several different formats. |
| 95 | `SC.ORD.STOCK.EXCHANGE` | `OrderByCust_StockExchange` | TField |  | If this transaction is CASH then this field will be populated automatically from the SECURITY.MASTER record. If the transaction is Validation Rules: Must exist on the STOCK.EXCHANGE file. |
| 96 | `SC.ORD.TRADE.CCY` | `OrderByCust_TradeCcy` | TField |  | The trade currency for the ORDER.BY.CUST. Will be defaulted from the ORDER.TYPE and the security field SECURITY.CURRENCY. Validation Rules: If the order type is PURCHASE then this will be set from the SECURITY.NO.CR record If the order type is SELL or SWITCH then this will be set from the SECURITY.NO.DB record Otherwise it will be set from SECURITY.NO |
| 97 | `SC.ORD.TOTAL.NOMINAL` | `OrderByCust_TotalNominal` | TField |  | A system calculated field. Will display the total of all NOMINAL. Validation Rules: A NOINPUT field. |
| 98 | `SC.ORD.CU.WHT.PERC` | `OrderByCust_CuWhtPerc` |  |  |  |
| 99 | `SC.ORD.CU.WHT.TAX` | `OrderByCust_CuWhtTax` |  |  |  |
| 100 | `SC.ORD.ROUNDING.TYPE` | `OrderByCust_RoundingType` | TField |  | For NOMINAL based orders this field will determine how the surplus/deficit is allocated. Proportional will spread the surplus/deficit based on the portfolio valuation as a proportion of the whole, thereby allocating or removing based on the strength of the portfolio. For HIGH.LOW method. If there is a surplus it will remove, one trading unit at a time from the highest initial allocation. If there is a deficit it will add, one trading unit at a time, to the lowest allocation. |
| 101 | `SC.ORD.NOMINAL.ROUNDING` | `OrderByCust_NominalRounding` | TField |  | If this field is left blank or set to NATURAL it will perform the natural rounding method, i.e. greater than or equal 0.5 goes up to 1, less than 0.5 goes down. UNDER will ensure that all nominal allocations are rounded down to the previous trading unit. OVER will ensure that all nominal allocations are rounded up to the next trading unit. If not set NATURAL will be used |
| 102 | `SC.ORD.INC.OPEN.ORDERS` | `OrderByCust_IncOpenOrders` | TField |  | This option, if set to YES, will include the NET.OPEN.ORDER.VAL from SEC.ACC.MASTER in the valuation and include the NET.OPEN.ORDER.POS from SECURITY.POSITION in the calculations for nominal required to be bought or sold. |
| 103 | `SC.ORD.INC.ACCRD.INT` | `OrderByCust_IncAccrdInt` | TField |  | This field, when set to 'ALL', will calculate the proceeds of the sale of a bond instrument to include accrued interest. This requires PRICE.TYPE, PRICE.BASIS to be set to 'EXC.ACCR'. |
| 104 | `SC.ORD.INC.UNSETTLED` | `OrderByCust_IncUnsettled` | TField |  | This option, if set to YES, will not deduct the UNSETTLED.NOM.CR from the nominal figure in CLOSING.BAL.NO.NOM in SECURITY.POSITION when calculating the nominal held by the portfolio. The resulting figure is used when calculating the nominal required to be purchased or sold depending on what is currently held. For TARGET and PURCHASE.INCR this will default to YES. |
| 105 | `SC.ORD.EXTERNAL.TXN` | `OrderByCust_ExternalTxn` | TField |  | Determine whether external transaction is allowed. Allowed value is YES |
| 106 | `SC.ORD.PARENT.REFERENCE` | `OrderByCust_ParentReference` | TField |  | The parent reference provided in this field will form part of the common reference between parent and child. Validation Rules Alphabetical characters A maximum of 21 characters may be entered |
| 107 | `SC.ORD.PARENT.CHILD` | `OrderByCust_ParentChild` | TField |  | This field is used to generate parent child SEC.OPEN.ORDERS and will accept a value YES. Parent order will be generated for each security and all the portfolio under that security will be individual child orders. Validation Rules Alphabetical characters |
| 108 | `SC.ORD.RESERVED5` | `OrderByCust_Reserved5` | TField |  |  |
| 109 | `SC.ORD.RESERVED4` | `OrderByCust_Reserved4` | TField |  |  |
| 110 | `SC.ORD.RESERVED3` | `OrderByCust_Reserved3` | TField |  |  |
| 111 | `SC.ORD.RESERVED2` | `OrderByCust_Reserved2` | TField |  |  |
| 112 | `SC.ORD.RESERVED1` | `OrderByCust_Reserved1` | TField |  |  |
| 113 | `SC.ORD.LOCAL.REF` | `OrderByCust_LocalRef` |  |  |  |
| 114 | `SC.ORD.OVERRIDE` | `OrderByCust_Override` |  |  |  |
| 115 | `SC.ORD.RECORD.STATUS` | `OrderByCust_RecordStatus` | String |  |  |
| 116 | `SC.ORD.CURR.NO` | `OrderByCust_CurrNo` | String |  |  |
| 117 | `SC.ORD.INPUTTER` | `OrderByCust_Inputter` |  |  |  |
| 118 | `SC.ORD.DATE.TIME` | `OrderByCust_DateTime` |  |  |  |
| 119 | `SC.ORD.AUTHORISER` | `OrderByCust_Authoriser` | String |  |  |
| 120 | `SC.ORD.CO.CODE` | `OrderByCust_CoCode` | String |  |  |
| 121 | `SC.ORD.DEPT.CODE` | `OrderByCust_DeptCode` | String |  |  |
| 122 | `SC.ORD.AUDITOR.CODE` | `OrderByCust_AuditorCode` | String |  |  |
| 123 | `SC.ORD.AUDIT.DATE.TIME` | `OrderByCust_AuditDateTime` | String |  |  |
