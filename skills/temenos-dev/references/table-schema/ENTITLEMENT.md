# ENTITLEMENT — Table Schema

> Source: `INSERTS/I_F.ENTITLEMENT` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ENT.PORTFOLIO.NO` | `Entitlement_PortfolioNo` | TField |  | Portfolio Number to which the ENTITLEMENT record is for. Enriched by the Account Name field from the SEC.ACC.MASTER file. Validation Rules: This is a NOINPUT, system generated field. |
| 2 | `SC.ENT.SECURITY.NO` | `Entitlement_SecurityNo` | TField |  | SEDOL number of the original security. Updated from the originating DIARY record. Enriched by the Short description of the Security from Security Master file. Validation Rules: This is a NOINPUT field. |
| 3 | `SC.ENT.DEPOSITORY` | `Entitlement_Depository` | TField |  | The Depository number the ENTITLEMENT record related to. Enriched by short description from CUSTOMER.SECURITY file. Validation Rules: Updated by the system and is a NOINPUT field. |
| 4 | `SC.ENT.NOMINEE` | `Entitlement_Nominee` | TField |  | Unique reference which identifies the Nominee Company record. Validation Rules: This is a NOINPUT field updated by the system. |
| 5 | `SC.ENT.SUB.ACCOUNT` | `Entitlement_SubAccount` | TField |  | Specifies the sub account of the depository. It is defaulted from the entitlement key. No input field |
| 6 | `SC.ENT.QUALIFY.HOLDING` | `Entitlement_QualifyHolding` | TField |  | Portfolio's holding in the original security as at EX.DATE. Should the underlying DIARY.TYPE be an equalisation type dividend as may be paid in respect of a UK unit trusttype security, then this holding will comprise the total held prior to the equalisation date (so called "G1"amount), and is therefore ineligible for equalisation processing. Should this field be zero, then you should refer to the EQUALISE.HLDING field as it is likely that thesecurities were purchased during the current equalisation period and, as a consequence, undergo a differentdividend payment process. If you change the qualifying holding then the ENTITLEMENT.AMT will be recalculated, using the newly enteredQUALIFY.HOLDING to ascertain the dividend amount due. Any amendments made to the automatically generated amount will be lost should the parent DIARY be re-run. Validation Rules: Field updated by the System but may be amended |
| 7 | `SC.ENT.EVENT.NOMINAL` | `Entitlement_EventNominal` | TField |  | This is the total nominal involved in the event. If the event is a RIGHTS issue then this is the total number ofrights otherwise this will be equal to the QUALIFY.HOLDING. Validation Rules: This is a NOINPUT field, updated by the system. |
| 8 | `SC.ENT.CURRENCY` | `Entitlement_Currency` | TField |  | Currency in which ENTITLEMENT.AMT is calculated.If CURRENCY in Diary is a non-restricted Currency, then Defaultedfrom the CURRENCY field on the original DIARY record.Else, from SETT.CURRENCY field in the original DIARY record. Enriched by the short description from the CURRENCY file. Validation Rules: This is a NOINPUT field, updated by the system. |
| 9 | `SC.ENT.VALUE.DATE` | `Entitlement_ValueDate` | TField | Yes | Value date of the event, updated by the system. Fed from original DIARY record. Validation Rules: Mandatory Field. User can change the Value of this field. |
| 10 | `SC.ENT.OPTION.DESC` | `Entitlement_OptionDesc` |  |  |  |
| 11 | `SC.ENT.GROSS.RATE` | `Entitlement_GrossRate` |  |  |  |
| 12 | `SC.ENT.NET.RATE` | `Entitlement_NetRate` |  |  |  |
| 13 | `SC.ENT.GROSS.OR.NET` | `Entitlement_GrossOrNet` |  |  |  |
| 14 | `SC.ENT.ENTITLEMENT.AMT` | `Entitlement_EntitlementAmt` |  |  |  |
| 15 | `SC.ENT.MBS.PAID.AMT` | `Entitlement_MbsPaidAmt` |  |  |  |
| 16 | `SC.ENT.EQUALISE.HLDING` | `Entitlement_EqualiseHlding` |  |  |  |
| 17 | `SC.ENT.GROUP2.AMT` | `Entitlement_Group2Amt` |  |  |  |
| 18 | `SC.ENT.EQUALISE.AMT` | `Entitlement_EqualiseAmt` |  |  |  |
| 19 | `SC.ENT.NEW.SECURITY` | `Entitlement_NewSecurity` |  |  |  |
| 20 | `SC.ENT.NOMINAL` | `Entitlement_Nominal` |  |  |  |
| 21 | `SC.ENT.RATIO` | `Entitlement_Ratio` |  |  |  |
| 22 | `SC.ENT.PRICE` | `Entitlement_Price` |  |  |  |
| 23 | `SC.ENT.BOOK.COST` | `Entitlement_BookCost` |  |  |  |
| 24 | `SC.ENT.TAX.PRICE` | `Entitlement_TaxPrice` |  |  |  |
| 25 | `SC.ENT.TAX.VALUE` | `Entitlement_TaxValue` |  |  |  |
| 26 | `SC.ENT.ODD.LOT.NUM` | `Entitlement_OddLotNum` |  |  |  |
| 27 | `SC.ENT.ODD.LOT.NOM` | `Entitlement_OddLotNom` |  |  |  |
| 28 | `SC.ENT.ODD.LOT.REF` | `Entitlement_OddLotRef` |  |  |  |
| 29 | `SC.ENT.FRACTION.DISP` | `Entitlement_FractionDisp` |  |  |  |
| 30 | `SC.ENT.CASH.IN.LIEU.PRICE` | `Entitlement_CashInLieuPrice` |  |  |  |
| 31 | `SC.ENT.FRACTION.NOMINAL` | `Entitlement_FractionNominal` |  |  |  |
| 32 | `SC.ENT.CASH.FRACTION` | `Entitlement_CashFraction` |  |  |  |
| 33 | `SC.ENT.FRACTION.BUY.NOMINAL` | `Entitlement_FractionBuyNominal` |  |  |  |
| 34 | `SC.ENT.ROUND.NOMINAL` | `Entitlement_RoundNominal` |  |  |  |
| 35 | `SC.ENT.AVAILABLE.DATE` | `Entitlement_AvailableDate` |  |  |  |
| 36 | `SC.ENT.ADD.ON.SEC` | `Entitlement_AddOnSec` |  |  |  |
| 37 | `SC.ENT.OPT.SOURCE.TAX` | `Entitlement_OptSourceTax` |  |  |  |
| 38 | `SC.ENT.OPT.LOCAL.TAX` | `Entitlement_OptLocalTax` |  |  |  |
| 39 | `SC.ENT.OPT.TAX.CREDIT` | `Entitlement_OptTaxCredit` |  |  |  |
| 40 | `SC.ENT.OPTION.NOM` | `Entitlement_OptionNom` |  |  |  |
| 41 | `SC.ENT.ORIG.ENT.AMOUNT` | `Entitlement_OrigEntAmount` |  |  |  |
| 42 | `SC.ENT.ENT.AMT.EVENT.CCY` | `Entitlement_EntAmtEventCcy` |  |  |  |
| 43 | `SC.ENT.ENT.AMT.DIV.CCY` | `Entitlement_EntAmtDivCcy` |  |  |  |
| 44 | `SC.ENT.NET.AMT.DIV.CCY` | `Entitlement_NetAmtDivCcy` |  |  |  |
| 45 | `SC.ENT.OPT.CCY.EXCH.RATE` | `Entitlement_OptCcyExchRate` |  |  |  |
| 46 | `SC.ENT.OPT.CCY.DIV.RATE` | `Entitlement_OptCcyDivRate` |  |  |  |
| 47 | `SC.ENT.OPT.CURRENCY` | `Entitlement_OptCurrency` |  |  |  |
| 48 | `SC.ENT.OPTION.IND` | `Entitlement_OptionInd` |  |  |  |
| 49 | `SC.ENT.OPTION.NUM` | `Entitlement_OptionNum` |  |  |  |
| 50 | `SC.ENT.DEFAULT.OPTION` | `Entitlement_DefaultOption` |  |  |  |
| 51 | `SC.ENT.DIV.CCY.ACCOUNT` | `Entitlement_DivCcyAccount` |  |  |  |
| 52 | `SC.ENT.SOURCE.TAX.DIV.CCY` | `Entitlement_SourceTaxDivCcy` |  |  |  |
| 53 | `SC.ENT.LOCAL.TAX.DIV.CCY` | `Entitlement_LocalTaxDivCcy` |  |  |  |
| 54 | `SC.ENT.COMM.DIV.CCY` | `Entitlement_CommDivCcy` |  |  |  |
| 55 | `SC.ENT.COMM.TAX.AMT.DIV.CCY` | `Entitlement_CommTaxAmtDivCcy` |  |  |  |
| 56 | `SC.ENT.OTH.CHG.TAX.DIV.CCY` | `Entitlement_OthChgTaxDivCcy` |  |  |  |
| 57 | `SC.ENT.DIV.CCY.LCL.EXCH.RATE` | `Entitlement_DivCcyLclExchRate` |  |  |  |
| 58 | `SC.ENT.NET.AMT.CU.DIV.CCY` | `Entitlement_NetAmtCuDivCcy` |  |  |  |
| 59 | `SC.ENT.OPT.REPLY.BY.DATE` | `Entitlement_OptReplyByDate` |  |  |  |
| 60 | `SC.ENT.OPT.REPLY.BY.TIME` | `Entitlement_OptReplyByTime` |  |  |  |
| 61 | `SC.ENT.OPT.PAY.DATE` | `Entitlement_OptPayDate` |  |  |  |
| 62 | `SC.ENT.EXPIRY.DATE` | `Entitlement_ExpiryDate` |  |  |  |
| 63 | `SC.ENT.PERIOD.FROM` | `Entitlement_PeriodFrom` |  |  |  |
| 64 | `SC.ENT.PERIOD.TO` | `Entitlement_PeriodTo` |  |  |  |
| 65 | `SC.ENT.MIN.EXC.QTY` | `Entitlement_MinExcQty` |  |  |  |
| 66 | `SC.ENT.MAX.EXC.QTY` | `Entitlement_MaxExcQty` |  |  |  |
| 67 | `SC.ENT.OPT.TRAD.PRD.FROM` | `Entitlement_OptTradPrdFrom` |  |  |  |
| 68 | `SC.ENT.OPT.TRAD.PRD.TO` | `Entitlement_OptTradPrdTo` |  |  |  |
| 69 | `SC.ENT.OPT.ACT.PRD.FROM` | `Entitlement_OptActPrdFrom` |  |  |  |
| 70 | `SC.ENT.OPT.ACT.PRD.TO` | `Entitlement_OptActPrdTo` |  |  |  |
| 71 | `SC.ENT.OPT.REVOC.PRD.FROM` | `Entitlement_OptRevocPrdFrom` |  |  |  |
| 72 | `SC.ENT.OPT.REVOC.PRD.TO` | `Entitlement_OptRevocPrdTo` |  |  |  |
| 73 | `SC.ENT.TAP.REF.ID` | `Entitlement_TapRefId` |  |  |  |
| 74 | `SC.ENT.TAX.CREDIT.DIV.CCY` | `Entitlement_TaxCreditDivCcy` |  |  |  |
| 75 | `SC.ENT.ELECT.NOMINAL` | `Entitlement_ElectNominal` |  |  |  |
| 76 | `SC.ENT.ELECTED.DATE` | `Entitlement_ElectedDate` |  |  |  |
| 77 | `SC.ENT.INT.ELECTED.DATE` | `Entitlement_IntElectedDate` |  |  |  |
| 78 | `SC.ENT.INT.ELECTED.NOM` | `Entitlement_IntElectedNom` |  |  |  |
| 79 | `SC.ENT.INT.ENTITLEMENT.AMT` | `Entitlement_IntEntitlementAmt` |  |  |  |
| 80 | `SC.ENT.MIN.SUBSCR` | `Entitlement_MinSubscr` |  |  |  |
| 81 | `SC.ENT.INCR.SUBSCR` | `Entitlement_IncrSubscr` |  |  |  |
| 82 | `SC.ENT.MAX.SUBSCR` | `Entitlement_MaxSubscr` |  |  |  |
| 83 | `SC.ENT.OPT.ELECT.AMT` | `Entitlement_OptElectAmt` |  |  |  |
| 84 | `SC.ENT.OVER.OPTION.DESC` | `Entitlement_OverOptionDesc` | TField |  | Option desc or indicator for oversubscription. Mapped from DIARY. Validation Rules: No input field |
| 85 | `SC.ENT.OVER.OPTION.NUM` | `Entitlement_OverOptionNum` | TField |  | Option number pertaining to Oversubscription. Mapped from DIARY. Validation Rules: No input field |
| 86 | `SC.ENT.OVER.SUBS.PRICE` | `Entitlement_OverSubsPrice` | TField |  | This holds the price at which Over subscribed quantity is to be sold. Mapped from DIARY. This is for informationpurpose. Validation Rules: No input field |
| 87 | `SC.ENT.OVER.SUBSCRIBED.NOM` | `Entitlement_OverSubscribedNom` | TField |  | This will hold Amount of additional shares that the user want to subscribe. |
| 88 | `SC.ENT.OVER.ALLOTED.NOM` | `Entitlement_OverAllotedNom` | TField |  | Alloted quantity will be calculated by considering by the subscribed nominal,Total subscribed nominal and nominalallocated by depository. This field value will be added to the nominal arrived as a result of exercise option. |
| 89 | `SC.ENT.OVER.SUB.AMOUNT` | `Entitlement_OverSubAmount` | TField |  | Field to store the oversubscription amount : Quantity * Price . Allowed for manual amendment |
| 90 | `SC.ENT.OVER.PAID.AMOUNT` | `Entitlement_OverPaidAmount` | TField |  | Field to store amount paid for the allotted quantity |
| 91 | `SC.ENT.OVER.REFUND.AMOUNT` | `Entitlement_OverRefundAmount` | TField |  |  |
| 92 | `SC.ENT.OVER.SUB.AMT.ACY` | `Entitlement_OverSubAmtAcy` | TField |  | Field to store equivalent value of OVER.SUB.AMT in Account Currency of the Entitlement |
| 93 | `SC.ENT.OVER.REFUND.AMT.ACY` | `Entitlement_OverRefundAmtAcy` | TField |  | Field to store equivalent value of OVER.REFUND.AMT in Account Currency of the Entitlement |
| 94 | `SC.ENT.EXERCISE.NOM` | `Entitlement_ExerciseNom` | TField |  | Field to hold the total of exercised nominal and the alloted nominal. Validation Rules NOINPUT Field |
| 95 | `SC.ENT.SELL.BUY.OPT.DESC` | `Entitlement_SellBuyOptDesc` |  |  |  |
| 96 | `SC.ENT.SELL.BUY.OPT.NO` | `Entitlement_SellBuyOptNo` |  |  |  |
| 97 | `SC.ENT.SELL.BUY.SEC` | `Entitlement_SellBuySec` |  |  |  |
| 98 | `SC.ENT.SELL.BUY.REPLY.DATE` | `Entitlement_SellBuyReplyDate` |  |  |  |
| 99 | `SC.ENT.SELL.BUY.TRAD.FROM.DATE` | `Entitlement_SellBuyTradFromDate` |  |  |  |
| 100 | `SC.ENT.SELL.BUY.TRAD.TO.DATE` | `Entitlement_SellBuyTradToDate` |  |  |  |
| 101 | `SC.ENT.PENDING.NOM` | `Entitlement_PendingNom` | TField |  | This field is used to store nominal available for election. Validation Rules NOINPUT Field. |
| 102 | `SC.ENT.ENTITLEMENT.AMT.RESID` | `Entitlement_EntitlementAmtResid` | TField |  | Entitlement Amount remained from earlier events like Reinvest and is not paid out for entitled portfolio can begiven here. |
| 103 | `SC.ENT.SUBSCRIPTION.CAP` | `Entitlement_SubscriptionCap` | TField |  | Amount defined here is used to limit elected amount during subscription offer based on holding or portfolio valueof holdings in eligible security |
| 104 | `SC.ENT.DECISION.MKR.ID` | `Entitlement_DecisionMkrId` | TField |  |  |
| 105 | `SC.ENT.FINAL.DEBIT.QTY` | `Entitlement_FinalDebitQty` | TField |  | This field will hold the final quantity that will be tendered (removed from security position). Validation Rules: 1. Input to this field is allowed only when BUYBCK.PRICE has value in Diary record. 2. This cannot be greater than the qualify holding excluding the NOAC option and the retain nominal 3. Authorisation of Entitlement record is not possible when this field value is blank and DISC.TENDER field isset in DIARY.TYPE record and CALLED.OFF.EVENT not set |
| 106 | `SC.ENT.FINAL.SUBSCR.AMT` | `Entitlement_FinalSubscrAmt` | TField |  | This field will hold the final subscription amount when the confirmation is received. Validation Rules: This field will be allowed only if SUBSCR.EVENT is set to YES in DIARY.TYPE record. This field cannot be greater than the amount entered in the OPT.ELECT.AMT field. |
| 107 | `SC.ENT.FINAL.SUBSCR.QTY` | `Entitlement_FinalSubscrQty` | TField |  | This field will hold the expected nominal when confirmation is received. Validation Rules: This field will be allowed only if SUBSCR.EVENT is set to YES in DIARY.TYPE record. This amount will be defaulted based on the quantity entered in FINAL.SUBSCR.AMT using the price in NEW.PRICE. |
| 108 | `SC.ENT.REFUND.AMT` | `Entitlement_RefundAmt` | TField |  | This field will hold the amount of cash to be refunded to the client's account. Validation Rules: This field will be allowed only if SUBSCR.EVENT is set to YES in DIARY.TYPE record. This field cannot be greater than the amount in OPT.ELECT.AMT. |
| 109 | `SC.ENT.SEC.TRADE.ID` | `Entitlement_SecTradeId` |  |  |  |
| 110 | `SC.ENT.BUY.NUMBER` | `Entitlement_BuyNumber` |  |  |  |
| 111 | `SC.ENT.SELL.NUMBER` | `Entitlement_SellNumber` |  |  |  |
| 112 | `SC.ENT.RETAIN.NOMINAL` | `Entitlement_RetainNominal` | TField | No | This field allows the user to select some or all of the EVENT.NOMINAL and opt to have this portion of the holdingdo nothing. For example in a Bond Redemption corporate action when the user only wants to redeem 50% of theholding. Any amount input in this field will cause the system to have no effect on this portion of the holding. Validation Rules: Optional input. If anything is entered into this field the total of this field together with the elected option nominals must beequal to the figure input in the EVENT.NOMINAL field. Input must be numeric. |
| 113 | `SC.ENT.OPTION` | `Entitlement_Option` | TField | No | This field allows the user to use all the holding on a single option. Validation Rules: Optional input of numeric characters. Input must be a numeric and cannot be less than one or greater than the total number of options available. |
| 114 | `SC.ENT.ACCOUNT.NO` | `Entitlement_AccountNo` | TField | Yes | The portfolio Account involved in the event. This Account will be used for all commissions, charges, taxes andcash entitlements. This field is updated by the system when creating ENTITLEMENT records taking the default value from settlementdefaults but user has an option to change this. If the portfolio has a suffix defined in REPO.PARAMETER as aRESO.MARGIN.SUF and ENT.CPN.SUSP is also defined then the account will be the internal account for the entitlementcurrency and the suspense category. Validation Rules: Mandatory input. 1-16 character Account number or 3-10 character Mnemonic Account id (uppercase alpha or numeric or "."). Must be a valid Account on the ACCOUNT file. |
| 115 | `SC.ENT.ACCOUNT.CURR` | `Entitlement_AccountCurr` | TField |  | Currency of the account number mentioned in the previous field. Enriched by the Short description from CURRENCY file. Validation Rules: This is a NOINPUT field and updated by the system. |
| 116 | `SC.ENT.REFERENCE.CCY` | `Entitlement_ReferenceCcy` | TField |  | Reference Currency of the portfolio. Updated by the system taking the default value from SEC.ACC.MASTER file. Enriched by the Short description from CURRENCY file. Validation Rules: This is a NOINPUT field. |
| 117 | `SC.ENT.SOURCE.TAX.AMT` | `Entitlement_SourceTaxAmt` | TField |  | Amount of Source Tax charged in Currency of the Event. This field will be updated by the system only if RATE.TYPE field in DIARY record is set to 'G'ROSS. OtherwiseTAX.CREDIT field will be updated. Validation Rules: |
| 118 | `SC.ENT.LOCAL.TAX.AMT` | `Entitlement_LocalTaxAmt` |  |  |  |
| 119 | `SC.ENT.TAX.CREDIT` | `Entitlement_TaxCredit` | TField |  | Amount of Source Tax that has been previously been debited by initiator of Corporate Action and so not charged touser through T24. Amount updated by the system and is for display only. This field will be updated by the systemonly if RATE.TYPE in the original DIARY record is set to 'N'ET. Validation Rules: This is a NOINPUT field. |
| 120 | `SC.ENT.FGN.CHARGES.AMT` | `Entitlement_FgnChargesAmt` | TField |  | Foreign Charges amount charged in the Currency of the event. Validation Rules: This is a NOINPUT field and is updated by the system. |
| 121 | `SC.ENT.COMMISSION.AMT` | `Entitlement_CommissionAmt` | TField |  | Amount of commission charged in the Currency of the event. Validation Rules: This field is updated by the system and is a NOINPUT field. |
| 122 | `SC.ENT.COMM.TAX.AMT` | `Entitlement_CommTaxAmt` | TField |  | Amount of Tax charged on the Commission in the Currency of the event. Validation Rules: This is a NOINPUT field for display only and updated by the system. |
| 123 | `SC.ENT.STAMP.TAX.CODE` | `Entitlement_StampTaxCode` | TField |  | Tax code used to calculate the stamp tax. This field is automatically populated by the system. Validation Rules: Must be a valid entry of TAX file |
| 124 | `SC.ENT.STAMP.BASE.AMT` | `Entitlement_StampBaseAmt` | TField |  | Amount in local currency on which the stamp tax has been calculated. This field is populated by the routine entered in the STAMP.CALC.RTN field of the related DIARY.TYPE record. |
| 125 | `SC.ENT.STAMP.BK.LCY` | `Entitlement_StampBkLcy` | TField |  | Amount of stamp tax in charge of the bank. This field will be populated by the system if the field STAMP.MIN.AMT field of the related DIARY.TYPE record contains an amount which is lower or equal to the stamp tax amount. This amount is expressed in local currency. |
| 126 | `SC.ENT.STAMP.SEC.CCY` | `Entitlement_StampSecCcy` | TField |  | Stamp tax amount in security currency. |
| 127 | `SC.ENT.STAMP.ACC.CCY` | `Entitlement_StampAccCcy` | TField |  | Stamp tax amount in account currency. |
| 128 | `SC.ENT.STAMP.LOC.CCY` | `Entitlement_StampLocCcy` | TField |  | Stamp tax amount in local currency. |
| 129 | `SC.ENT.NET.AMT.ACC.CUR` | `Entitlement_NetAmtAccCur` | TField |  | Net amount to be credited or debited in the Currency of the Account. Validation Rules: This is a NOINPUT field and is updated by the system. |
| 130 | `SC.ENT.NET.AMOUNT` | `Entitlement_NetAmount` | TField |  | Net Amount to be credited or debited in the Currency of the event. Validation Rules: This is a NOINPUT field and is updated by the system. |
| 131 | `SC.ENT.LCCY.EXCH.RATE` | `Entitlement_LccyExchRate` | TField | Yes | Exchange Rate between the Event Currency and the Account Currency. Updated by the system while generatingENTITLEMENT records, but user has an option of changing this field. In the event of any change to this field, thiswill be validated. Validation Rules: Mandatory input. |
| 132 | `SC.ENT.ACC.EXCH.RATE` | `Entitlement_AccExchRate` | TField | Yes | Exchange rate between the Event currency and the Account currency. Updated by the system while generatingENTITLEMENT records but user has an option of changing the value of this field. In the event any change to thisfield proper validations are done. Validation Rules: Mandatory input. |
| 133 | `SC.ENT.REF.LCCY.RATE` | `Entitlement_RefLccyRate` | TField | Yes | Exchange rate between the Portfolio Reference Currency and the Local Currency. Updated by the system while generating ENTITLEMENT records but user has an option of changing the value in thisfield. In the event of changes, proper validations are done. Validation Rules: Mandatory input. |
| 134 | `SC.ENT.FGN.CHGES.LCCY` | `Entitlement_FgnChgesLccy` | TField |  | Foreign Charges amount in the Local Currency. Validation Rules: This is a NOINPUT field and is updated by the system. |
| 135 | `SC.ENT.COMMISSION.LCCY` | `Entitlement_CommissionLccy` | TField |  | Amount of commission charged in Local Currency. Validation Rules: This is a NOINPUT field and is updated by the system. |
| 136 | `SC.ENT.NET.AMT.LCCY` | `Entitlement_NetAmtLccy` | TField |  | Net Amount credited or debited to the account in the Local currency. Validation Rules: This is a NOINPUT field and is updated by the system. |
| 137 | `SC.ENT.REFERENCE.NO` | `Entitlement_ReferenceNo` | TField |  | Internally generated reference number. Display only. Validation Rules: This is a NOINPUT field. |
| 138 | `SC.ENT.COMMISSION.CODE` | `Entitlement_CommissionCode` | TField |  | Commission Code used to calculate the Commission charged on the account. Updated by the system from theoriginating DIARY record. Validation Rules: This is a NOINPUT field. |
| 139 | `SC.ENT.COMM.TAX.CODE` | `Entitlement_CommTaxCode` | TField |  | Tax Code used to calculate the Tax amount charged on the Commission Amount. Validation Rules: This is a NOINPUT field updated by the system and is for display purpose only. |
| 140 | `SC.ENT.COMM.TAX.LCCY` | `Entitlement_CommTaxLccy` | TField |  | Amount of Tax on the Commission amount in the Local currency. Validation Rules: This is a NOINPUT field and is updated by the system. |
| 141 | `SC.ENT.COMM.TAX.XRATE` | `Entitlement_CommTaxXrate` | TField |  | Exchange rate used to calculate Commission Tax Amount. Validation Rules: This is a NOINPUT field and is updated by the system. |
| 142 | `SC.ENT.SEC.NO` | `Entitlement_SecNo` |  |  |  |
| 143 | `SC.ENT.SEC.NOMINAL` | `Entitlement_SecNominal` |  |  |  |
| 144 | `SC.ENT.ACTIVITY.CODE` | `Entitlement_ActivityCode` |  |  |  |
| 145 | `SC.ENT.MESSAGE.TYPE` | `Entitlement_MessageType` |  |  |  |
| 146 | `SC.ENT.DELIVERY.KEY` | `Entitlement_DeliveryKey` |  |  |  |
| 147 | `SC.ENT.OVE.ADDR` | `Entitlement_OveAddr` |  |  |  |
| 148 | `SC.ENT.MESS.CONTROL` | `Entitlement_MessControl` | TField | No | MESSAGE.CONTROL ID used to check the format of the override delivery address entered in the address (previousfield). If entered must exist in MESSAGE.CONTROL file. After validation enriched by the short description of themessage. Validation Rules: Optional input of 1-3 numeric characters. If entered must exist in MESSAGE.CONTROL file. |
| 149 | `SC.ENT.TAX.CHANGED` | `Entitlement_TaxChanged` | TField |  | Displaying either YES or NO depending on whether the default tax has been changed or not. If the default tax hasbeen changed then this field will equal YES otherwise it will be NO. This field is used by the system to prevent the source and local tax fields from being overwritten with defaultvalues if they have already been changed by a user. Validation Rules: This is a NOINPUT field. Internal system use only. |
| 150 | `SC.ENT.COMM.CHANGED` | `Entitlement_CommChanged` | TField |  | Field indicating whether or not the COMMISSION.AMOUNT has been manually changed by an inputter or not. If this field is YES then the COMMISSION.AMT has been manually changed. If this field is NO then the COMMISSION.AMT has been defaulted by the system. Validation Rules: This is a NOINPUT field. |
| 151 | `SC.ENT.FOREIGN.CHGES.TAX` | `Entitlement_ForeignChgesTax` | TField |  | Validation Rules: This is a NOINPUT field. |
| 152 | `SC.ENT.FGN.TAX.CODE` | `Entitlement_FgnTaxCode` | TField |  | Validation Rules: A maximum of 15 characters may be entered. This is a NOINPUT field. |
| 153 | `SC.ENT.FGN.TAX.BCUR` | `Entitlement_FgnTaxBcur` | TField |  | Validation Rules: A maximum of 18 characters may be entered. This is a NOINPUT field. |
| 154 | `SC.ENT.FGN.TAX.XRATE` | `Entitlement_FgnTaxXrate` | TField |  | Standard T24 rate field. Validation Rules: A maximum of 15 characters may be entered. This is a NOINPUT field. |
| 155 | `SC.ENT.MBS.RED.DIV.AMT` | `Entitlement_MbsRedDivAmt` | TField |  | Validation Rules: A maximum of 19 characters may be entered. This is a NOINPUT field. |
| 156 | `SC.ENT.MBS.RED.ACC.AMT` | `Entitlement_MbsRedAccAmt` | TField |  | Validation Rules: A maximum of 19 characters may be entered. This is a NOINPUT field. |
| 157 | `SC.ENT.MBS.RED.LCY.AMT` | `Entitlement_MbsRedLcyAmt` | TField |  | Validation Rules: A maximum of 19 characters may be entered. This is a NOINPUT field. |
| 158 | `SC.ENT.LOCAL.REF` | `Entitlement_LocalRef` |  |  |  |
| 159 | `SC.ENT.PRE.ADVICE.REQ` | `Entitlement_PreAdviceReq` | TField | No | Determines whether pre confirmation advices are generated when entitlements are created via this Entitlementrecord. The value will be defaulted from the relevant DIARY record. The actual message types are determined via the relevant EB.ADVICES records, which will be eitherSC-0100-EVENT.TYPE, for entitlement creation or SC-0101-EVENT.TYPE, for entitlement amendment or deletion. Validation Rules: Optional Input can be set to YES or NO |
| 160 | `SC.ENT.CONFIRM.REQ` | `Entitlement_ConfirmReq` | TField | No | Determines whether confirmation advices are generated when entitlements are created via this Entitlement record. The value will be defaulted from the relevant DIARY.TYPE record. The actual message types are determined via the relevant EB.ADVICES records, which will be eitherSC-0102-EVENT.TYPE, for entitlement creation or SC-0103-EVENT.TYPE, for entitlement reversal. Validation Rules: Optional Input can be set to YES or NO |
| 161 | `SC.ENT.CGT.BAMT.CCY` | `Entitlement_CgtBamtCcy` | TField |  | This field will signify the currency code in which the CGT base amount is denominated. Validation Rules: NOINPUT field |
| 162 | `SC.ENT.CGT.BASE.AMT` | `Entitlement_CgtBaseAmt` | TField |  | This field will hold the amount on which the capital gains tax calculation is to be performed. This field is obtained from the WHT.PL field on the CG.TXN.BASE file. The amount is maintained in the currency of the account being debited. If the field is changed a recalculation of the tax amount is triggered off. Validation Rules: Populated automatically Can be changed |
| 163 | `SC.ENT.CGT.CODE` | `Entitlement_CgtCode` |  |  |  |
| 164 | `SC.ENT.CGT.TAX.RATE` | `Entitlement_CgtTaxRate` |  |  |  |
| 165 | `SC.ENT.CGT.TAX.LCL` | `Entitlement_CgtTaxLcl` |  |  |  |
| 166 | `SC.ENT.CGT.TAX.AMT` | `Entitlement_CgtTaxAmt` |  |  |  |
| 167 | `SC.ENT.CGT.PARAM.COND` | `Entitlement_CgtParamCond` | TField |  | This field will default with the key of the CG.PARAM.CONDITION record which has conditions set that apply to thistransaction (if any). Validation Rules: A NOINPUT field. Alpha or Numeric characters allowed Maximum of 5 characters |
| 168 | `SC.ENT.CGT.SRC.LCL.TAX` | `Entitlement_CgtSrcLclTax` | TField |  | This field indicates whether the Capital Gains Tax for this transaction is to be deducted by the bank (LOCAL) orthe depository (SOURCE). Validation Rules: A NOINPUT field. Field can either be 'SOURCE' or 'LOCAL'. |
| 169 | `SC.ENT.BLOCK.TYPE` | `Entitlement_BlockType` | TField |  | Specifies whether the Security Position updated by the execution of the Corporate Action will be blocked. If the position is to be blocked it can take place at the authorisation of the DIARY record (value DIARY ENTITLEMENT The blocked amount is always the QUALIFY.HOLDING Blocks are created in the SC.BLOCK.SEC.POS application automatically when a block is required, similarly theyare unblocked using the same application automatically. A block / unblock is created under the followingcircumstances: OPTION Block holding will be updated in SECURITY.POSITION only during election of option in ENTITLEMENT record. Amount will be released from position during delete of ENTITLEMENT/ authorisation of ENTITLEMENT record. Validation Rules: System field No input Values DIARY or ENTITLEMENT or OPTION allowed |
| 170 | `SC.ENT.LOCAL.TAX.CODE` | `Entitlement_LocalTaxCode` |  |  |  |
| 171 | `SC.ENT.LOCAL.TAX.PERC` | `Entitlement_LocalTaxPerc` |  |  |  |
| 172 | `SC.ENT.EQUALISATION.ACC` | `Entitlement_EqualisationAcc` | TField |  | Account used to post the capital equalisation amount. This field is updated by the system when creating ENTITLEMENT records taking the default value from customers'SEC.ACC.MASTER portfolio accounts but you have the option to be able to enter any valid account whether belongingto the Customer or not, subject to override conditions being satisfied. Validation Rules: Input only allowed if field EQUALISATION in the underlying DIARY.TYPE is "YES" |
| 173 | `SC.ENT.EQUALISATION.CCY` | `Entitlement_EqualisationCcy` | TField |  | The currency of the account in the EQUALISATION.ACC field. Validation Rules: This is a NOINPUT field and updated by the system. |
| 174 | `SC.ENT.EQUALIS.EX.RATE` | `Entitlement_EqualisExRate` | TField |  | The exchange rate between the security currency and the currency of the EQUALISATION.ACC if they are different. This field is updated by the system when creating ENTITLEMENT records but user has an option to change this rateif necessary. If the EQUALISATION.ACC is changed to an account having a different currency than that originally entered, thenthis field will be updated to the exchange rate applicable between the account and security currencies. Validation Rules: Input only allowed if field EQUALISATION in DIARY.TYPE is YES by this Event Type. |
| 175 | `SC.ENT.EQUALIS.AMT.ACY` | `Entitlement_EqualisAmtAcy` | TField |  | This field shows the equalisation amount having been converted to the customer's account currency and will beposted to his/her account as defined in the EQUALISATION.ACC field. Validation Rules: This is a no-input field |
| 176 | `SC.ENT.SOURCE.TAX.CODE` | `Entitlement_SourceTaxCode` | TField |  | Automatically updated by the system from SOURCE.TAX.CODE field in DIARY record. The field contains the key of the TAX record used to determine the source tax percentage. If APPL.GEN.CONDITION application has a record with id 'DIARY' or 'ENTITLEMENT', then CONTRACT.GRP is identifiedbased on the conditions defined in the fields from DECIS.FIELD to DECISION.TO in APPL.GEN.CONDITION. InTAX.TYPE.CONDITION, the tax codes that are assigned to particular groups of contract (CONTRACT.GRP) are populatedin this field. Validation Rules: |
| 177 | `SC.ENT.SOURCE.TAX.PERC` | `Entitlement_SourceTaxPerc` | TField |  | Automatically updated by the system from the rate of the TAX record keyed on the SOURCE.TAX.CODE field. The field contains the percentage used to calculate the source tax amount. If APPL.GEN.CONDITION application has a record with id 'DIARY' or 'ENTITLEMENT', then CONTRACT.GRP is identifiedbased on the conditions defined in the fields from DECIS.FIELD to DECISION.TO in APPL.GEN.CONDITION. InTAX.TYPE.CONDITION, the tax codes that are assigned to particular groups of contract (CONTRACT.GRP) are populatedin SOURCE.TAX.CODE and the corresponding percentage is displayed in this field. Validation Rules: |
| 178 | `SC.ENT.CUST.ACT.SUSP.CAT` | `Entitlement_CustActSuspCat` | TField |  | This field is used as a category reference for the customer. The suspense amount of the customer is posted to it. The value is picked up from the SC.PARAMETER, which holds a similar field in it. The value is defaulted from theSC.PARAMETER fields. Validation Rules: The value in this field should be a valid entry in CATEGORY file. |
| 179 | `SC.ENT.BROK.ACT.SUSP.CAT` | `Entitlement_BrokActSuspCat` | TField |  | This field is used as a category reference for the broker. The suspense amount of the broker is posted to it. The value is picked up from the SC.PARAMETER which holds a similar field in it. The value is defaulted from theSC.PARAMETER fields. Validation Rules: The value in this field should be a valid entry in CATEGORY file. |
| 180 | `SC.ENT.MISC.ACT.SUSP.CAT` | `Entitlement_MiscActSuspCat` | TField |  | This field is used as a category reference for miscellaneous. The suspense amount of miscellaneous is posted toit. The value is picked up from the SC.PARAMETER which holds a similar field in it. The value is defaulted from theSC.PARAMETER fields. Validation Rules: The value in this field should be a valid entry in CATEGORY file. |
| 181 | `SC.ENT.AUTO.CUST.SETT` | `Entitlement_AutoCustSett` | TField |  | Enables the automatic settlement of the nominal and cash for the Customers. This facility is available for theCustomer side only. The value is defaulted as 'YES', if it has been set to YES in the CUSTOMER.SECURITY file. The automaticsettlement can be turned OFF at transaction level, though it has been turned ON in the CUSTOMER.SECURITY. Though ithas been turned ON in the CUSTOMER.SECURITY, the same could be turned OFF at the transaction namely SEC.TRADE,SECURITY.TRANSFER Validation Rules: Yes, No or Null. Null is equivalent to NO |
| 182 | `SC.ENT.ADJUST.SEC` | `Entitlement_AdjustSec` |  |  |  |
| 183 | `SC.ENT.ADJUST.NOM` | `Entitlement_AdjustNom` |  |  |  |
| 184 | `SC.ENT.AUT.AUTH.DATE` | `Entitlement_AutAuthDate` | TField |  | Noinput field that will contain the date on which the ENTITLEMENT record will be automatically authorised duringthe START.OF.DAY process. This field is populated from the ENT.AUTO.AUTH.DATE field of the related DIARY record. Validation Rules: Noinput field automatically populated by the system |
| 185 | `SC.ENT.DEF.INSTR.DATE` | `Entitlement_DefInstrDate` | TField |  | Noinput field that will contains the date on which the system will apply default instructions to the ENTITLEMENTrecord. This field is populated from the DEF.INSTR.DATE field of the related DIARY record. Validation Rules: Noinput field automatically populated by the system |
| 186 | `SC.ENT.REINVEST.ORDER` | `Entitlement_ReinvestOrder` |  |  |  |
| 187 | `SC.ENT.STAND.INST` | `Entitlement_StandInst` | TField |  | No input field that will record the standing instructions used to default option to be taken on this ENTITLEMENTrecord. Validation Rules: |
| 188 | `SC.ENT.AUTO.BROK.SETT` | `Entitlement_AutoBrokSett` | TField |  | Enables the automatic settlement of the nominal and cash for Brokers who have contractual agreements with the Bank.This value will be defaulted to YES, if there is an "YES" in AUTO.BROK.SETT field in CUSTOMER.SECURITY file. Theautomatic settlement can be turned OFF at transaction level, though it has been turned ON in the CUSTOMER.SECURITY.Though it has been turned ON in the CUSTOMER.SECURITY,the same could be turned OFF at the transaction namelySEC.TRADE, SECURITY.TRANSFER, etc.Validation Rules: Yes, No or Null. Null is equivalent to NO |
| 189 | `SC.ENT.RCVBL.TAX.PERC` | `Entitlement_RcvblTaxPerc` | TField | No | This field shows the rate applicable for the Recoverable Tax code which is taken from the DIARY record. This is an input field and can be modified at the ENTITLEMENT level if needed. Validation Rules: It is an optional field. |
| 190 | `SC.ENT.RCVBL.TAX.REF.AMT` | `Entitlement_RcvblTaxRefAmt` | TField |  | This field shows the Recoverable Tax in the Customer Portfolio Reference Currency. This is defaulted by thesystem when the Corporate Action event is subject to Recoverable Tax. Validation Rules: It is a no input field. |
| 191 | `SC.ENT.RCVBL.TAX.LCY.AMT` | `Entitlement_RcvblTaxLcyAmt` | TField |  | This field shows the Recoverable Tax in the Local Currency. This is defaulted by the system when the CorporateAction event is subject to Recoverable Tax. Validation Rules: It is a no input field. |
| 192 | `SC.ENT.RCVBL.TAX.SEC.AMT` | `Entitlement_RcvblTaxSecAmt` | TField |  | This field shows the Recoverable Tax in the Security Currency. This is defaulted by the system when the CorporateAction event is subject to Recoverable Tax. |
| 193 | `SC.ENT.BND.RND.METH` | `Entitlement_BndRndMeth` | TField |  | When calculating the accrued interest on a bond, certain rounding parameters can be taken into account in thecalculation. If a bond rounding method has been used then the method used will be stored in this field. Validation Rules: NOINPUT field |
| 194 | `SC.ENT.BROKER.TXN.ID` | `Entitlement_BrokerTxnId` |  |  |  |
| 195 | `SC.ENT.TRANS.TYPE` | `Entitlement_TransType` |  |  |  |
| 196 | `SC.ENT.BR.OUTS.NOM` | `Entitlement_BrOutsNom` |  |  |  |
| 197 | `SC.ENT.BR.RIGHTS.NOM` | `Entitlement_BrRightsNom` |  |  |  |
| 198 | `SC.ENT.OPT.DESC` | `Entitlement_OptDesc` |  |  |  |
| 199 | `SC.ENT.OPT.NOM` | `Entitlement_OptNom` |  |  |  |
| 200 | `SC.ENT.TAX.NARR` | `Entitlement_TaxNarr` |  |  |  |
| 201 | `SC.ENT.DEPOT.HOLDING` | `Entitlement_DepotHolding` | TField |  | System generated field which will reflect the effect that the position has on the Depot (Agent), a negativefigure will be produced when the Portfolio has caused a shortage at the Depot and a positive figure will beproduced when the Portfolio holds stock in the Depot.The field will be calculated as the QUALIFY.HOLDING -outstanding credit transactions + outstanding debit transactions + non-returned settled stock borrows -non-returned settled stock lent. |
| 202 | `SC.ENT.DEPO.RIGHTS.NOM` | `Entitlement_DepoRightsNom` | TField |  | Single value field which is the equivalent to DEPOT.HOLDING field and will have the Rights security nominal heldwith the Depository. This field will be updated only if field SETTLE.METHOD in SC.PARAMETER is set to "US". |
| 203 | `SC.ENT.OPT.DESC.DEP` | `Entitlement_OptDescDep` |  |  |  |
| 204 | `SC.ENT.OPT.NOM.DEP` | `Entitlement_OptNomDep` |  |  |  |
| 205 | `SC.ENT.BROKER.NO` | `Entitlement_BrokerNo` |  |  |  |
| 206 | `SC.ENT.OUTSTAND.NOM` | `Entitlement_OutstandNom` |  |  |  |
| 207 | `SC.ENT.RIGHTS.NOM` | `Entitlement_RightsNom` |  |  |  |
| 208 | `SC.ENT.TOT.OUT.NOM` | `Entitlement_TotOutNom` | TField |  | This field will specify the total outstanding nominal entitled from all the brokers for the portfolio. No inputsystem updated field Validation Rules: This is a NOINPUT field. |
| 209 | `SC.ENT.TOT.RIGHTS.NOM` | `Entitlement_TotRightsNom` | TField |  | This field is equivalent to TOT.OUT.NOM field and will hold the total outstanding nominal from theBroker/Counterparty with respect to Rights Security. This field will be updated only if field SETTLE.METHOD in SC.PARAMETER is set to "US". |
| 210 | `SC.ENT.BR.ENT.KEY` | `Entitlement_BrEntKey` |  |  |  |
| 211 | `SC.ENT.ODD.RTS.BAM` | `Entitlement_OddRtsBam` | TField |  | This field is used to signify the number of rights securities that need to be purchased to use all the rightsthat are allocated from the existing holding that would remain unused rights when the rights are converted to thenew security. Validation Rules: NOINPUT |
| 212 | `SC.ENT.ODD.RTS.SAM` | `Entitlement_OddRtsSam` | TField |  | This field is used to signify the number of rights securities that can be sold without affecting then number ofnew securities that would be allocated when the rights securities are converted to the new securities. Validation Rules: NOINPUT |
| 213 | `SC.ENT.OPT.STATUS` | `Entitlement_OptStatus` | TField | No | For optional events, such as rights, this indicates the current status of the ENTITLEMENT. Once the client exercises, the entitlement will be authorized (interim authorization) and the OPT.STATUS will beupdated as "PAID" for the Upfront payment setup.DIARY cannot be rerun when the Opt Status is set to PaidThesecurity position will be updated to reflect the paid up amount (including the oversubscribed portion). For Multiple Settlement, when ELECT.NOMINAL is inputted, OPT.STATUS will be updated as 'INTERIM.ELECTED'.OPTION.NOM will be NOINPUT in this case. |
| 214 | `SC.ENT.BORROW.NOMINAL` | `Entitlement_BorrowNominal` | TField |  | This field holds the net settled Borrow positions as on Record Date |
| 215 | `SC.ENT.BORROW.AMT` | `Entitlement_BorrowAmt` | TField |  | This field stores the Borrow amount.It is calculated as BORROW.NOMINAL * Dividend rate * SBL.DIV.RATE |
| 216 | `SC.ENT.LENT.NOMINAL` | `Entitlement_LentNominal` | TField |  | This field holds the net settled Lent positions as on Record Date |
| 217 | `SC.ENT.LENT.AMT` | `Entitlement_LentAmt` | TField |  | This field stores the Lent amount.It is calculated as LENT.NOMINAL * Dividend rate * SBL.DIV.RATE |
| 218 | `SC.ENT.SBL.QUALIFY.HOLD` | `Entitlement_SblQualifyHold` | TField |  | This field will include the net Qualify holdings for the particular Security, Customer and the Depository.It iscalculated as follows:SBL.QUAL.HOLD = QUALIFY.HOLDING + Settled Borrowed positions as on Record Date - Settled Lentpositions as on Record date. |
| 219 | `SC.ENT.SC.TAX.CODE` | `Entitlement_ScTaxCode` |  |  |  |
| 220 | `SC.ENT.SC.TAX.TYPE` | `Entitlement_ScTaxType` |  |  |  |
| 221 | `SC.ENT.SOURCE.OR.LOCAL` | `Entitlement_SourceOrLocal` |  |  |  |
| 222 | `SC.ENT.SRC.TAX.ADJ.AMT` | `Entitlement_SrcTaxAdjAmt` |  |  |  |
| 223 | `SC.ENT.SC.AMT.ACY` | `Entitlement_ScAmtAcy` |  |  |  |
| 224 | `SC.ENT.SC.AMT.LCY` | `Entitlement_ScAmtLcy` |  |  |  |
| 225 | `SC.ENT.MAN.TAX.ACY` | `Entitlement_ManTaxAcy` |  |  |  |
| 226 | `SC.ENT.MAN.TAX.LCY` | `Entitlement_ManTaxLcy` |  |  |  |
| 227 | `SC.ENT.INT.DIST.FACTOR` | `Entitlement_IntDistFactor` | TField |  | Interest distribution factor for this event. Applicable to shares only. |
| 228 | `SC.ENT.INT.CTR` | `Entitlement_IntCtr` | TField |  | Interest counter for this event. Applicable to shares only. |
| 229 | `SC.ENT.MANUAL.CREATION` | `Entitlement_ManualCreation` | TField |  | This field indicates whether the Entitlement is generated manually or through service. This field gets updated to'YES' when the Entitlement is inputted manually. Validation Rules: No input field. |
| 230 | `SC.ENT.EXT.CUSTODIAN` | `Entitlement_ExtCustodian` | TField |  | To identify the external custodian where position is held. |
| 231 | `SC.ENT.MARGIN.FACTOR` | `Entitlement_MarginFactor` | TField |  | This field used in the calculation of consideration using the Columbian Yield Method. |
| 232 | `SC.ENT.FTT.TYPE` | `Entitlement_FttType` | TField |  | Defines the valid TAX.TYPE Record related to FTT(Finanicial Transactional Tax).Field will get defaulted from thefield FTT.TYPE of DIARY |
| 233 | `SC.ENT.FTT.PERC` | `Entitlement_FttPerc` | TField |  | Defines the valid tax rate of the FTT(Financial Transactional Tax).Field will get defaulted from the fieldTAX.RATE of TAX related to FTT |
| 234 | `SC.ENT.FTT.BSE.AMT` | `Entitlement_FttBseAmt` | TField |  | Tax base amount in terms of EUR currrency on which the tax percentage is applied. |
| 235 | `SC.ENT.FTT.AMT.TCY` | `Entitlement_FttAmtTcy` | TField |  | FTT Tax amount in account currency of the transaction. |
| 236 | `SC.ENT.FTT.AMT.LCY` | `Entitlement_FttAmtLcy` | TField |  | FTT Tax amount in local currency. |
| 237 | `SC.ENT.FTT.AMT.CCY` | `Entitlement_FttAmtCcy` | TField |  | FTT Tax amount currency which is EUR. |
| 238 | `SC.ENT.FTT.AMT` | `Entitlement_FttAmt` | TField |  | Tax amount in EUR. |
| 239 | `SC.ENT.FTT.EX.RATE` | `Entitlement_FttExRate` | TField |  | Exchange rate between account currency and EUR. |
| 240 | `SC.ENT.EVENT.CCY` | `Entitlement_EventCcy` | TField |  |  |
| 241 | `SC.ENT.EXCH.RATE` | `Entitlement_ExchRate` | TField |  | If EVENT.CURRENCY is a restricted currency,then this field contains the Exchange Rate between CURRENCY andEVENT.CURRENCY.This will be defaulted from from EXCH.RATE field in DIARY. Validation Rules: No input field |
| 242 | `SC.ENT.MAND.VOLU.FLAG` | `Entitlement_MandVoluFlag` | TField | Yes | Mandatory or voluntary indicator for the Event. Mapped from DIARY. Validation Rules: No input field |
| 243 | `SC.ENT.MEETING.DATE` | `Entitlement_MeetingDate` | TField |  | This field specifies the date of meeting and so updated from 98A tag of CA option details of MT564 with qualifierMEET. Value to this field is passed from corresponding SC.PRE.DIARY, then to DIARY, and then to ENTITLEMENT record whenit is automatically created by Corporate Action Service Validation Rules Standard T24 Date field |
| 244 | `SC.ENT.MEETING.TIME` | `Entitlement_MeetingTime` | TField |  | This field specifies the time of meeting and so updated from 98C tag of CA option details of MT564 with qualifierMEET. Value to this field is passed from corresponding SC.PRE.DIARY, then to DIARY, and then to ENTITLEMENT record whenit is automatically created by Corporate Action Service Validation Rules Standard T24 time field |
| 245 | `SC.ENT.MEET.VENUE` | `Entitlement_MeetVenue` |  |  |  |
| 246 | `SC.ENT.NEW.INCORP.PLACE` | `Entitlement_NewIncorpPlace` | TField |  | This field specifies the New Company's place of Incorporation. System will update this field from 94E tag of MT564 when the qualifier is NPLI For e.g. if 94E tag contains the value, :94E::NPLI//11 Eunos Rd 8,Lvl 1 Event Hall, system updates this field as"11 Eunos Rd 8,Lvl 1 Event Hall" Value to this field is passed from corresponding SC.PRE.DIARY, then to DIARY, and then to ENTITLEMENT record whenit is automatically created by Corporate Action Service Validation Rules Standard T24 Time field |
| 247 | `SC.ENT.OTH.DATE.TYPE` | `Entitlement_OthDateType` |  |  |  |
| 248 | `SC.ENT.OTH.DATE` | `Entitlement_OthDate` |  |  |  |
| 249 | `SC.ENT.OTH.DATE.TIME` | `Entitlement_OthDateTime` |  |  |  |
| 250 | `SC.ENT.CERTIFICATION.TYPE` | `Entitlement_CertificationType` |  |  |  |
| 251 | `SC.ENT.CERT.PLACE` | `Entitlement_CertPlace` |  |  |  |
| 252 | `SC.ENT.CAEV.TYPE` | `Entitlement_CaevType` | TField |  | Denotes the Corporate action Event Indicator in SWIFT terms. Validation Rules Valid Swift indicator NoInput Field |
| 253 | `SC.ENT.INT.DIST.TYPE` | `Entitlement_IntDistType` | TField |  | This field denotes whether the rights distribution event is for reinvestment, exchange or subscription of rights. This will be mapped from DIARY |
| 254 | `SC.ENT.PERCENT.SOUGHT` | `Entitlement_PercentSought` | TField |  | This field is an information field to denote the percentage of shares sought. This will be mapped from DIARY |
| 255 | `SC.ENT.ADJUST.AMT` | `Entitlement_AdjustAmt` |  |  |  |
| 256 | `SC.ENT.RIGHTS.CREDIT.DATE` | `Entitlement_RightsCreditDate` | TField |  | This field will specify the date on which rights will be credited to the account.Mapped from DIARY Validation Rules NOINPUT field. |
| 257 | `SC.ENT.RIGHTS.EXP.DATE` | `Entitlement_RightsExpDate` | TField |  | Denotes the expiry date of the rights.Mapped from DIARY Validation Rules NOINPUT field. |
| 258 | `SC.ENT.BLOCK.NOMINAL` | `Entitlement_BlockNominal` | TField |  | This field holds the nominal that is blocked during election of option and will be updated when BLOCK.TYPE is setas OPTION |
| 259 | `SC.ENT.TAX.ENT.AMT.EVT.CCY` | `Entitlement_TaxEntAmtEvtCcy` | TField |  | Field to denote the taxable amount of income in event currency The source and local tax will be calculated based on this field value |
| 260 | `SC.ENT.TAXLOT.ALLOCATE` | `Entitlement_TaxlotAllocate` |  |  |  |
| 261 | `SC.ENT.QTY.ALLOTED` | `Entitlement_QtyAlloted` |  |  |  |
| 262 | `SC.ENT.USUFRUCT.CUST` | `Entitlement_UsufructCust` |  |  |  |
| 263 | `SC.ENT.USUFRUCT.ACCT` | `Entitlement_UsufructAcct` |  |  |  |
| 264 | `SC.ENT.USUFRUCT.ACCT.CCY` | `Entitlement_UsufructAcctCcy` |  |  |  |
| 265 | `SC.ENT.USUFRUCT.AMT.EVT.CCY` | `Entitlement_UsufructAmtEvtCcy` |  |  |  |
| 266 | `SC.ENT.USUFRUCT.SOURCE.TAX` | `Entitlement_UsufructSourceTax` |  |  |  |
| 267 | `SC.ENT.USUFRUCT.LOCAL.TAX` | `Entitlement_UsufructLocalTax` |  |  |  |
| 268 | `SC.ENT.USUFRUCT.ACC.EXCH.RATE` | `Entitlement_UsufructAccExchRate` |  |  |  |
| 269 | `SC.ENT.USUFRUCT.AMT.ACCT.CCY` | `Entitlement_UsufructAmtAcctCcy` |  |  |  |
| 270 | `SC.ENT.CUST.EVENT.ID` | `Entitlement_CustEventId` | TField |  | This field maintains the cross reference to the id of the corresponding record in SC.CUST.EVENT.CREATE that wasused to create the DIARY record. Validation Rules: An EXTERNAL field. |
| 271 | `SC.ENT.REFUND.AMT.ACC.CCY` | `Entitlement_RefundAmtAccCcy` | TField |  | This field will hold the amount of cash to be refunded to the client's account in Account Currency. Validation Rules: Noinput Field, Updated by the system |
| 272 | `SC.ENT.SMALL.HOLDINGS.SELL` | `Entitlement_SmallHoldingsSell` | TField |  |  |
| 273 | `SC.ENT.STMT.NOS` | `Entitlement_StmtNos` |  |  |  |
| 274 | `SC.ENT.OVERRIDE` | `Entitlement_Override` |  |  |  |
| 275 | `SC.ENT.RECORD.STATUS` | `Entitlement_RecordStatus` | String |  |  |
| 276 | `SC.ENT.CURR.NO` | `Entitlement_CurrNo` | String |  |  |
| 277 | `SC.ENT.INPUTTER` | `Entitlement_Inputter` |  |  |  |
| 278 | `SC.ENT.DATE.TIME` | `Entitlement_DateTime` |  |  |  |
| 279 | `SC.ENT.AUTHORISER` | `Entitlement_Authoriser` | String |  |  |
| 280 | `SC.ENT.CO.CODE` | `Entitlement_CoCode` | String |  |  |
| 281 | `SC.ENT.DEPT.CODE` | `Entitlement_DeptCode` | String |  |  |
| 282 | `SC.ENT.AUDITOR.CODE` | `Entitlement_AuditorCode` | String |  |  |
| 283 | `SC.ENT.AUDIT.DATE.TIME` | `Entitlement_AuditDateTime` | String |  |  |
| 284 | `SC.ENT.BLOCKED` | `Entitlement_Blocked` | TField |  | Field to denote that the Entitlement is blocked or not.When set, then accounting entries and security positionupdation is skipped. Validation Rules: Allowed Values : YES or Blank |
| 285 | `SC.ENT.BLOCKED.REASON` | `Entitlement_BlockedReason` |  |  |  |
| 286 | `SC.ENT.ELECT.TIME` | `Entitlement_ElectTime` |  |  |  |
| 287 | `SC.ENT.ELECT.USER` | `Entitlement_ElectUser` |  |  |  |
| 288 | `SC.ENT.BENE.OWN.NARR` | `Entitlement_BeneOwnNarr` |  |  |  |
| 289 | `SC.ENT.ADDL.NARR` | `Entitlement_AddlNarr` |  |  |  |
| 290 | `SC.ENT.OPT.AUTH` | `Entitlement_OptAuth` |  |  |  |
| 291 | `SC.ENT.INSTRUCTION.MKR` | `Entitlement_InstructionMkr` | TField |  | This field holds T24 customer ID, from where the LEI or name of the customer can be got. Validation Rules: This will be a free format field |
| 292 | `SC.ENT.ORDER.INITIATOR` | `Entitlement_OrderInitiator` | TField |  | This field holds the Order Initiator. This might be the bank or the client (account holder). It can either hold values bank or Client�s customer ID. This field is for information purpose only. Has to be manually input or interfaced. Validation Rules: Alphanumeric upto 35 characters Free Text field. |
| 293 | `SC.ENT.INCOME.CODE` | `Entitlement_IncomeCode` |  |  |  |
| 294 | `SC.ENT.INCOME.RATE` | `Entitlement_IncomeRate` |  |  |  |
| 295 | `SC.ENT.INCOME.PERCENTAGE` | `Entitlement_IncomePercentage` |  |  |  |
| 296 | `SC.ENT.INCOME.AMOUNT` | `Entitlement_IncomeAmount` |  |  |  |
| 297 | `SC.ENT.INCOME.TAX.RATE` | `Entitlement_IncomeTaxRate` |  |  |  |
| 298 | `SC.ENT.INCOME.TAX.AMOUNT` | `Entitlement_IncomeTaxAmount` |  |  |  |
| 299 | `SC.ENT.INCOME.MAN.TAX.AMT` | `Entitlement_IncomeManTaxAmt` |  |  |  |
| 300 | `SC.ENT.CUSTOMER.LEI.NCI` | `Entitlement_CustomerLeiNci` | TField |  | This field holds the LEI/NCI code of the customer. Validation If blank, system defaults the LEI/NCI of the customer based on priority defined in SC.NCI.PRIORITY and rulesdefined in SC.NCI.PARAMETER System raises error if it is not in the below format L/N-CustomerNo-LEI/NCI code |
| 301 | `SC.ENT.CONTRACT.NO` | `Entitlement_ContractNo` | TField |  | This field holds the DX.CONTRACT.MASTER id which is defaulted from the Diary record. Validation Rules: No Input field. |
| 302 | `SC.ENT.MIFID.REPORT.STATUS` | `Entitlement_MifidReportStatus` | TField |  |  |
| 303 | `SC.ENT.SFTR.INDI` | `Entitlement_SftrIndi` | TField |  |  |
| 304 | `SC.ENT.SC.TAX.EFF.DATE` | `Entitlement_ScTaxEffDate` |  |  |  |
| 305 | `SC.ENT.SAFEKEEP.ACCT.NO` | `Entitlement_SafekeepAcctNo` | TField |  | This field will hold the customer account which will be used to post the Safekeeping Charges. The account will bepopulated based on the field SAFEKEEP.CHRG.ACCOUNT in SEC.ACC.MASTER. If no account is given, then the system will default an internal account based on the Securities Suspense DebitAccount. Validation Rules: If system defaults an internal account based on the Securities Suspense Debit Account override will be raised |
| 306 | `SC.ENT.SAFEKEEP.FEE.LCY` | `Entitlement_SafekeepFeeLcy` | TField |  | This field will hold the respective safekeep fees charged for the event in local currency. Validation Rules: No Input field. |
| 307 | `SC.ENT.SK.ACY.LCY.RATE` | `Entitlement_SkAcyLcyRate` | TField |  | This field holds the exchange rate between the account currency (SAFEKEEP.ACT.NO) and local currency. Validation Rules: This will be a no input field and system will default the MID.REVAL.RATE from CURRENCY table. |
| 308 | `SC.ENT.SAFEKEEP.FEE.ACY` | `Entitlement_SafekeepFeeAcy` | TField |  | This field will hold the respective safekeep fees charged for the event in SAFEKEEP.ACT.NO currency. Validation Rules: No Input field. |
| 309 | `SC.ENT.ELECT.REF` | `Entitlement_ElectRef` |  |  |  |
| 310 | `SC.ENT.ELECT.STATUS` | `Entitlement_ElectStatus` |  |  |  |
| 311 | `SC.ENT.LEI.NCI.CHK.REQ` | `Entitlement_LeiNciChkReq` | TField |  |  |
| 312 | `SC.ENT.DEPO.ADV.REQ` | `Entitlement_DepoAdvReq` | TField |  |  |
| 313 | `SC.ENT.MT566.RECON` | `Entitlement_Mt566Recon` |  |  |  |
