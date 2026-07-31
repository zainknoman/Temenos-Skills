# FS.GA.COUPON.MANAGEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUPON.MANAGEMENT` in `FS_Income.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.COUPON.MANAGEMENT.PARENT.REF.ID` | `FsGaCouponManagement_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.COUPON.MANAGEMENT.ORA.ROWID` | `FsGaCouponManagement_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.COUPON.MANAGEMENT.SERVICE.CODE` | `FsGaCouponManagement_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 4 | `FS.GA.COUPON.MANAGEMENT.GROSS.AMOUNT.OF.INCOME` | `FsGaCouponManagement_GrossAmountOfIncome` | TField |  | The Gross amount of the income Multifonds DB Column is MNTGLOBAL. |
| 5 | `FS.GA.COUPON.MANAGEMENT.UNREC.TAX.IN.AMOUNT.TYPE.1` | `FsGaCouponManagement_UnrecTaxInAmountType1` | TField |  | Unrecoverable tax amount on Income , type 1 Multifonds DB Column is MNTUNRECTAX. |
| 6 | `FS.GA.COUPON.MANAGEMENT.UNREC.TAX.IN.AMOUNT.TYPE.2` | `FsGaCouponManagement_UnrecTaxInAmountType2` | TField |  | Unrecoverable tax amount on Income , type 2 Multifonds DB Column is MNTUNRECTAX_2. |
| 7 | `FS.GA.COUPON.MANAGEMENT.SERVICE.CODE.POT` | `FsGaCouponManagement_ServiceCodePot` | TField |  | Service Code Pot Multifonds DB Column is CSERV_POT. |
| 8 | `FS.GA.COUPON.MANAGEMENT.GROSS.AMOUNT.1.OF.INCOME` | `FsGaCouponManagement_GrossAmount1OfIncome` | TField |  | The Gross amount 1 of the income Multifonds DB Column is MNTGROSS. |
| 9 | `FS.GA.COUPON.MANAGEMENT.UNFRANKED.NCFI.AMOUNT` | `FsGaCouponManagement_UnfrankedNcfiAmount` | TField |  | Unfranked Ncfi Amount Multifonds DB Column is MNTUNFRANKED_NCFI. |
| 10 | `FS.GA.COUPON.MANAGEMENT.UNFRANKED.NCFI.FUND.AMOUNT` | `FsGaCouponManagement_UnfrankedNcfiFundAmount` | TField |  | Unfranked Ncfi Fund Amount Multifonds DB Column is MNTUNFRANKED_NCFI_PTF. |
| 11 | `FS.GA.COUPON.MANAGEMENT.FATCA.RECOVERABLE.IN.AMOUNT` | `FsGaCouponManagement_FatcaRecoverableInAmount` | TField |  | Amount of FATCA Tax recoverable on the income. FATCA is taxation based on US residence Multifonds DB Column is MNT_FATCA2. |
| 12 | `FS.GA.COUPON.MANAGEMENT.RECOVERABLE.FATCA.TAX2.AMOUNT` | `FsGaCouponManagement_RecoverableFatcaTax2Amount` | TField |  | Recoverable Fatca Tax2 Amount Multifonds DB Column is MNTFATCATAX2_PTF. |
| 13 | `FS.GA.COUPON.MANAGEMENT.UNRECOVERABLE.TAX.AMOUNT.FCY` | `FsGaCouponManagement_UnrecoverableTaxAmountFcy` | TField |  | Unrecoverable Tax Amount Fcy Multifonds DB Column is MNTUNRECTAX_FCY. |
| 14 | `FS.GA.COUPON.MANAGEMENT.UNRECOVERABLE.TAX.2.AMOUNT.FCY` | `FsGaCouponManagement_UnrecoverableTax2AmountFcy` | TField |  | Unrecoverable Tax 2 Amount Fcy Multifonds DB Column is MNTUNRECTAX_2_FCY. |
| 15 | `FS.GA.COUPON.MANAGEMENT.FUND.ID` | `FsGaCouponManagement_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 16 | `FS.GA.COUPON.MANAGEMENT.INTERNAL.SECURITY.ID` | `FsGaCouponManagement_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 17 | `FS.GA.COUPON.MANAGEMENT.CORRESPONDENT` | `FsGaCouponManagement_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 18 | `FS.GA.COUPON.MANAGEMENT.LOT.NUMBER` | `FsGaCouponManagement_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 19 | `FS.GA.COUPON.MANAGEMENT.TRANSACTION.NUMBER` | `FsGaCouponManagement_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 20 | `FS.GA.COUPON.MANAGEMENT.LINE` | `FsGaCouponManagement_Line` | TField |  | Line Multifonds DB Column is NLIGNE. |
| 21 | `FS.GA.COUPON.MANAGEMENT.DEAL.STATUS.CODE` | `FsGaCouponManagement_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 22 | `FS.GA.COUPON.MANAGEMENT.CUSTODIAN` | `FsGaCouponManagement_Custodian` | TField |  | Custodian where the units of the transaction would be lodged Multifonds DB Column is NDEPOSI. |
| 23 | `FS.GA.COUPON.MANAGEMENT.DESCRIPTION` | `FsGaCouponManagement_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 24 | `FS.GA.COUPON.MANAGEMENT.OPERATION.CODE` | `FsGaCouponManagement_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 25 | `FS.GA.COUPON.MANAGEMENT.INCOME.CURRENCY.CODE` | `FsGaCouponManagement_IncomeCurrencyCode` | TField |  | This field defines the income currency of the security . Multifonds DB Column is CDEVTITR. |
| 26 | `FS.GA.COUPON.MANAGEMENT.EX.DATE` | `FsGaCouponManagement_ExDate` | TField |  | Execution date for Dividend announcement and Corporate Action Multifonds DB Column is DPAYMNT. |
| 27 | `FS.GA.COUPON.MANAGEMENT.ACCOUNTING.DATE` | `FsGaCouponManagement_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 28 | `FS.GA.COUPON.MANAGEMENT.SETTLE.DATE` | `FsGaCouponManagement_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 29 | `FS.GA.COUPON.MANAGEMENT.ENTITLEMENT.DATE` | `FsGaCouponManagement_EntitlementDate` | TField |  | The ex-date, or ex-dividend date, is the date on or after which a security is traded without a previously declared dividend or distribution. Multifonds DB Column is DEXEC. |
| 30 | `FS.GA.COUPON.MANAGEMENT.DEBIT.ACCOUNT.NUMBER` | `FsGaCouponManagement_DebitAccountNumber` | TField |  | Debit account number tagged to a fee code Multifonds DB Column is NRUBRDB. |
| 31 | `FS.GA.COUPON.MANAGEMENT.DEBIT.ACCOUNT.SUFFIX.NUMBER` | `FsGaCouponManagement_DebitAccountSuffixNumber` | TField |  | Debit account suffix number tagged to a fee code Multifonds DB Column is NSUFFDB. |
| 32 | `FS.GA.COUPON.MANAGEMENT.CREDIT.ACCOUNT.NUMBER` | `FsGaCouponManagement_CreditAccountNumber` | TField |  | Credit account number tagged to a fee code Multifonds DB Column is NRUBRCR. |
| 33 | `FS.GA.COUPON.MANAGEMENT.CREDIT.ACCOUNT.SUFFIX.NUMBER` | `FsGaCouponManagement_CreditAccountSuffixNumber` | TField |  | Credit account suffix number tagged to a fee code Multifonds DB Column is NSUFFCR. |
| 34 | `FS.GA.COUPON.MANAGEMENT.INCOME.CURRENCY` | `FsGaCouponManagement_IncomeCurrency` | TField |  | The currency of the security in which the income or tax reclaims are booked Multifonds DB Column is CMONDB. |
| 35 | `FS.GA.COUPON.MANAGEMENT.CURRENCY.CREDIT` | `FsGaCouponManagement_CurrencyCredit` | TField |  | Currency Credit Multifonds DB Column is CMONCR. |
| 36 | `FS.GA.COUPON.MANAGEMENT.NOMINAL.VALUE` | `FsGaCouponManagement_NominalValue` | TField |  | Nominal of the Instrument Multifonds DB Column is NOMINAL. |
| 37 | `FS.GA.COUPON.MANAGEMENT.QUANTITY` | `FsGaCouponManagement_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 38 | `FS.GA.COUPON.MANAGEMENT.UNIT.AMOUNT` | `FsGaCouponManagement_UnitAmount` | TField |  | Denotes the per unit amount in the security currency or the quoted currency Multifonds DB Column is MNTUNIT. |
| 39 | `FS.GA.COUPON.MANAGEMENT.UNIT.AMOUNT.IN.CORRESP.CCY` | `FsGaCouponManagement_UnitAmountInCorrespCcy` | TField |  | Denotes the per unit amount in the correspondent currency or the settlement currency Multifonds DB Column is MNTUNIT_CORR. |
| 40 | `FS.GA.COUPON.MANAGEMENT.COMMISSION.PERCENTAGE` | `FsGaCouponManagement_CommissionPercentage` | TField |  | The commission percentage of the income is defined Multifonds DB Column is PCOMCORR. |
| 41 | `FS.GA.COUPON.MANAGEMENT.COMMISSION.AMOUNT` | `FsGaCouponManagement_CommissionAmount` | TField |  | The commission amount of the income Multifonds DB Column is MNTCOMCORR. |
| 42 | `FS.GA.COUPON.MANAGEMENT.UNREC.TAX.IN.PERCENT.TYPE.1` | `FsGaCouponManagement_UnrecTaxInPercentType1` | TField |  | Unrecoverable tax percentage on Income , type 1 Multifonds DB Column is PUNRECTAX. |
| 43 | `FS.GA.COUPON.MANAGEMENT.REC.TAX.IN.PERCENT.TYPE.1` | `FsGaCouponManagement_RecTaxInPercentType1` | TField |  | Recoverable tax percentage on Income , type 1 Multifonds DB Column is PRECTAX. |
| 44 | `FS.GA.COUPON.MANAGEMENT.REC.TAX.IN.AMOUNT.TYPE.1` | `FsGaCouponManagement_RecTaxInAmountType1` | TField |  | Recoverable tax amount on Income , type 1 Multifonds DB Column is MNTRECTAX. |
| 45 | `FS.GA.COUPON.MANAGEMENT.NET.DIVIDEND.AMOUNT` | `FsGaCouponManagement_NetDividendAmount` | TField |  | Net Dividend Amount Multifonds DB Column is MNTNET. |
| 46 | `FS.GA.COUPON.MANAGEMENT.RATE.OF.EXCHANGE` | `FsGaCouponManagement_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 47 | `FS.GA.COUPON.MANAGEMENT.INTEREST.RATE` | `FsGaCouponManagement_InterestRate` | TField |  | Interest rate applicable on the interest bearing instrument in the transaction Multifonds DB Column is TXINT. |
| 48 | `FS.GA.COUPON.MANAGEMENT.ARCHIVE` | `FsGaCouponManagement_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 49 | `FS.GA.COUPON.MANAGEMENT.CASH.RECEIVE.PAY.IN.FUND.CCY` | `FsGaCouponManagement_CashReceivePayInFundCcy` | TField |  | The Cash amount received or paid in fund ccy as a result of the Corporate action Multifonds DB Column is MNTNET_PTF. |
| 50 | `FS.GA.COUPON.MANAGEMENT.EXCH.RATE.SETTLEMENT.TO.DEAL` | `FsGaCouponManagement_ExchRateSettlementToDeal` | TField |  | The exchange rate between the settlement and deal currency Multifonds DB Column is TCHG_PTF. |
| 51 | `FS.GA.COUPON.MANAGEMENT.MANUAL.SETTLEMENT` | `FsGaCouponManagement_ManualSettlement` | TField |  | Flag at deal level to override the contractual settlement specific to the deal. Multifonds DB Column is CSETTLE_MANU. |
| 52 | `FS.GA.COUPON.MANAGEMENT.UNRECOVERABLE.TAX.PERCENT.2` | `FsGaCouponManagement_UnrecoverableTaxPercent2` | TField |  | Unrecoverable tax percentage on Income , type 2 Multifonds DB Column is PUNRECTAX_2. |
| 53 | `FS.GA.COUPON.MANAGEMENT.RECOVERABLE.TAX.PERCENT.2` | `FsGaCouponManagement_RecoverableTaxPercent2` | TField |  | Recoverable tax percentage on Income , type 2 Multifonds DB Column is PRECTAX_2. |
| 54 | `FS.GA.COUPON.MANAGEMENT.RETROCESSION.COMMISSION.AMOUNT` | `FsGaCouponManagement_RetrocessionCommissionAmount` | TField |  | Recoverable tax amount on Income , type 2 Multifonds DB Column is MNTRECTAX_2. |
| 55 | `FS.GA.COUPON.MANAGEMENT.IMPOT.CURRENCY` | `FsGaCouponManagement_ImpotCurrency` | TField |  | Tax currency of the income Multifonds DB Column is CMON_IMPOT. |
| 56 | `FS.GA.COUPON.MANAGEMENT.EXCHANGE.RATE.BETWEEN.CCY` | `FsGaCouponManagement_ExchangeRateBetweenCcy` | TField |  | Exchange rate between settlement currency and tax currency Multifonds DB Column is TCHG_IMPOT. |
| 57 | `FS.GA.COUPON.MANAGEMENT.IMPOT.AMOUNT` | `FsGaCouponManagement_ImpotAmount` | TField |  | Impot Amount Multifonds DB Column is MNT_IMPOT. |
| 58 | `FS.GA.COUPON.MANAGEMENT.IMPOT.2.AMOUNT` | `FsGaCouponManagement_Impot2Amount` | TField |  | Impot 2 Amount Multifonds DB Column is MNT_IMPOT_2. |
| 59 | `FS.GA.COUPON.MANAGEMENT.MANAGER.ID` | `FsGaCouponManagement_ManagerId` | TField |  | Manager ID Multifonds DB Column is NACC_MNGR. |
| 60 | `FS.GA.COUPON.MANAGEMENT.PIK.INTEREST.RATE` | `FsGaCouponManagement_PikInterestRate` | TField |  | PIK Interest Rate Multifonds DB Column is PIK_TXINT. |
| 61 | `FS.GA.COUPON.MANAGEMENT.PIK.FACTOR` | `FsGaCouponManagement_PikFactor` | TField |  | Factor for PIK security Multifonds DB Column is PIK_FACTOR. |
| 62 | `FS.GA.COUPON.MANAGEMENT.MARKET.VALUE` | `FsGaCouponManagement_MarketValue` | TField |  | Market value used for the operations on pik bonds Multifonds DB Column is MARKET_VALUE. |
| 63 | `FS.GA.COUPON.MANAGEMENT.PIK.GLOBAL.AMOUNT` | `FsGaCouponManagement_PikGlobalAmount` | TField |  | PIK Global Amount Multifonds DB Column is MNTGLOBAL_PIK. |
| 64 | `FS.GA.COUPON.MANAGEMENT.PIK.CORRESPONDENT.FEE.AMOUNT` | `FsGaCouponManagement_PikCorrespondentFeeAmount` | TField |  | PIK Correspondent Fee Amount Multifonds DB Column is MNTCOMCORR_PIK. |
| 65 | `FS.GA.COUPON.MANAGEMENT.DAYS.OF.ACCRUED.INTEREST` | `FsGaCouponManagement_DaysOfAccruedInterest` | TField |  | Number of days of purchase/sale interest in a transaction done on an interest bearing instrument Multifonds DB Column is NBJOURS. |
| 66 | `FS.GA.COUPON.MANAGEMENT.NET.UNIT.AMOUNT.IDENTIFIER` | `FsGaCouponManagement_NetUnitAmountIdentifier` | TField |  | Denotes whether the income is Grossed up from the Net amount. Usually arises when Net amount per unit announcement is done in market Multifonds DB Column is FLAG_BRUT. |
| 67 | `FS.GA.COUPON.MANAGEMENT.FACTOR` | `FsGaCouponManagement_Factor` | TField |  | Factor for Mortgage backed instruments, also used in CMV securities and Fair value pricing. This also finds use as a mark up or down value in case of other features Multifonds DB Column is FACTOR. |
| 68 | `FS.GA.COUPON.MANAGEMENT.MANAGER.CODE` | `FsGaCouponManagement_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 69 | `FS.GA.COUPON.MANAGEMENT.UNIT.AMOUNT.IDENTIFIER` | `FsGaCouponManagement_UnitAmountIdentifier` | TField |  | Recalculates the unit amount fields when global amount field is amended. It is necessary to process the information as outstanding and then go back into the screen and tick the Unit Amount box. Multifonds DB Column is FLAG_CALCUL. |
| 70 | `FS.GA.COUPON.MANAGEMENT.ADJUSTED.ENTRY.NUMBER` | `FsGaCouponManagement_AdjustedEntryNumber` | TField |  | Adjusted Entry Number Multifonds DB Column is NECRITUR_ADJ. |
| 71 | `FS.GA.COUPON.MANAGEMENT.STATUS.PENDING` | `FsGaCouponManagement_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 72 | `FS.GA.COUPON.MANAGEMENT.RECOVERABLE.TAX.1` | `FsGaCouponManagement_RecoverableTax1` | TField |  | To enable Recoverable Tax 1 percentage for dividend or coupon Multifonds DB Column is FLG_PCR. |
| 73 | `FS.GA.COUPON.MANAGEMENT.RECOVERABLE.TAX.2` | `FsGaCouponManagement_RecoverableTax2` | TField |  | To enable Recoverable Tax 2 percentage for dividend or coupon Multifonds DB Column is FLG_PCR_2. |
| 74 | `FS.GA.COUPON.MANAGEMENT.NONRECOVERABLE.TAX1` | `FsGaCouponManagement_NonrecoverableTax1` | TField |  | To enable Non Recoverable Tax 1 percentage for dividend or coupon Multifonds DB Column is FLG_PCUR. |
| 75 | `FS.GA.COUPON.MANAGEMENT.NONRECOVERABLE.TAX2` | `FsGaCouponManagement_NonrecoverableTax2` | TField |  | To enable Non Recoverable Tax 2 percentage for dividend or coupon Multifonds DB Column is FLG_PCUR_2. |
| 76 | `FS.GA.COUPON.MANAGEMENT.NET.PIK.AMOUNT` | `FsGaCouponManagement_NetPikAmount` | TField |  | Net PIK Amount Multifonds DB Column is MNT_NET_PIK. |
| 77 | `FS.GA.COUPON.MANAGEMENT.UNIT.AMOUNT.RETAX.1` | `FsGaCouponManagement_UnitAmountRetax1` | TField |  | Unit amount of Tax , Type 1. This is also used for KEST , which is a witholding tax on German income payments to foreign investment funds Multifonds DB Column is MNTUNIT_RETAX_1. |
| 78 | `FS.GA.COUPON.MANAGEMENT.UNIT.AMOUNT.RETAX.2` | `FsGaCouponManagement_UnitAmountRetax2` | TField |  | Unit amount of Tax , Type 2. This is also used for KOST , which is a witholding tax on German income payments to foreign investment funds Multifonds DB Column is MNTUNIT_RETAX_2. |
| 79 | `FS.GA.COUPON.MANAGEMENT.NET.UNIT.AMOUNT` | `FsGaCouponManagement_NetUnitAmount` | TField |  | Please check if unit amount is net amount (net of withholding taxes). System will calculate the net total amount using this figure and will compute the gross amounts and withheld amounts accordingly. Multifonds DB Column is NET_UNIT_AMOUNT. |
| 80 | `FS.GA.COUPON.MANAGEMENT.TAX.FACC` | `FsGaCouponManagement_TaxFacc` | TField |  | Tax Facc Multifonds DB Column is TAX_FACC. |
| 81 | `FS.GA.COUPON.MANAGEMENT.SHORT.DESCRIPTION` | `FsGaCouponManagement_ShortDescription` | TField |  | Input the description of the transaction, else auto generated Multifonds DB Column is TXT_OST. |
| 82 | `FS.GA.COUPON.MANAGEMENT.PAYABLE.TAX.1.PERCENTAGE` | `FsGaCouponManagement_PayableTax1Percentage` | TField |  | Rate of Tax payable on the income , type of tax 1 Multifonds DB Column is PCT_TAX_1. |
| 83 | `FS.GA.COUPON.MANAGEMENT.TAX.PAYABLE.IN.AMOUNT.TYPE.1` | `FsGaCouponManagement_TaxPayableInAmountType1` | TField |  | Amount of Tax payable on the income , type of tax 1 Multifonds DB Column is MNT_TAX_1. |
| 84 | `FS.GA.COUPON.MANAGEMENT.PAYABLE.TAX.1` | `FsGaCouponManagement_PayableTax1` | TField |  | To enable Payable Tax 1 percentage for dividend or coupon Multifonds DB Column is FLG_TAX_1. |
| 85 | `FS.GA.COUPON.MANAGEMENT.AWV.REPORTING.INCLUSION` | `FsGaCouponManagement_AwvReportingInclusion` | TField |  | Flag to denote whether a coupon is to be included in AWV reporting. Multifonds DB Column is FLG_AWV. |
| 86 | `FS.GA.COUPON.MANAGEMENT.PAYABLE.TAX.2.PERCENTAGE` | `FsGaCouponManagement_PayableTax2Percentage` | TField |  | Rate of Tax payable on the income , type of tax 2 Multifonds DB Column is PCT_TAX_2. |
| 87 | `FS.GA.COUPON.MANAGEMENT.TAX.PAYABLE.IN.AMOUNT.TYPE.2` | `FsGaCouponManagement_TaxPayableInAmountType2` | TField |  | Amount of Tax payable on the income , type of tax 2 Multifonds DB Column is MNT_TAX_2. |
| 88 | `FS.GA.COUPON.MANAGEMENT.PAYABLE.TAX.2` | `FsGaCouponManagement_PayableTax2` | TField |  | To enable Payable Tax 2 percentage for dividend or coupon Multifonds DB Column is FLG_TAX_2. |
| 89 | `FS.GA.COUPON.MANAGEMENT.DCOUPON` | `FsGaCouponManagement_Dcoupon` | TField |  | Dcoupon Multifonds DB Column is DCOUP. |
| 90 | `FS.GA.COUPON.MANAGEMENT.AMORTISATION.AMOUNT.DEAL.CCY` | `FsGaCouponManagement_AmortisationAmountDealCcy` | TField |  | Amortization Amount Deal Ccy Multifonds DB Column is MNT_AMORTISSEMENT_DEAL. |
| 91 | `FS.GA.COUPON.MANAGEMENT.AMORTISED.AMOUNT.IN.BOOK.CCY` | `FsGaCouponManagement_AmortisedAmountInBookCcy` | TField |  | Amortized Amount in Book Currency Multifonds DB Column is MNT_AMORTISSEMENT. |
| 92 | `FS.GA.COUPON.MANAGEMENT.COEFFICIENT.CORPORATE.ACTION` | `FsGaCouponManagement_CoefficientCorporateAction` | TField |  | Enter a CA coefficient which is taken into account to calc the dividend, coupon, split, reverse split, spin off, exchange of security into one new security ID or several security ID on the sec lent. Multifonds DB Column is COEF_CORP. |
| 93 | `FS.GA.COUPON.MANAGEMENT.UNDERLYING.FUTURE.TYPE` | `FsGaCouponManagement_UnderlyingFutureType` | TField |  | This field defines securities underlying Future Type Multifonds DB Column is CHOIX. |
| 94 | `FS.GA.COUPON.MANAGEMENT.SEC.LENDING.TAX.PERCENTAGE` | `FsGaCouponManagement_SecLendingTaxPercentage` | TField |  | Security lending tax percentage on the income Multifonds DB Column is PSECLENTAX. |
| 95 | `FS.GA.COUPON.MANAGEMENT.SEC.LENDING.TAX.AMOUNT` | `FsGaCouponManagement_SecLendingTaxAmount` | TField |  | Security lending tax amount on the income Multifonds DB Column is MNTSECLENTAX. |
| 96 | `FS.GA.COUPON.MANAGEMENT.FUTURE.ID.CODE` | `FsGaCouponManagement_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 97 | `FS.GA.COUPON.MANAGEMENT.DIVIDEND.EXECUTION.DATE` | `FsGaCouponManagement_DividendExecutionDate` | TField |  | Dividend Execution Date Multifonds DB Column is DEXEC_DIV. |
| 98 | `FS.GA.COUPON.MANAGEMENT.EXTERNAL.REFERENCE.NUMBER` | `FsGaCouponManagement_ExternalReferenceNumber` | TField |  | External reference corresponds a trade,security or fund Multifonds DB Column is EXT_REF. |
| 99 | `FS.GA.COUPON.MANAGEMENT.FEE.1.PERCENTAGE` | `FsGaCouponManagement_Fee1Percentage` | TField |  | Rate of Fees charged on Income , type of fee 1 Multifonds DB Column is MFRAIS1. |
| 100 | `FS.GA.COUPON.MANAGEMENT.FEE.2.PERCENTAGE` | `FsGaCouponManagement_Fee2Percentage` | TField |  | Percentage of Fees charged on Income , type of fee 2 Multifonds DB Column is MFRAIS2. |
| 101 | `FS.GA.COUPON.MANAGEMENT.FEE.IN.AMOUNT.TYPE.1` | `FsGaCouponManagement_FeeInAmountType1` | TField |  | Amount of Fees charged on Income , type of fee 1 Multifonds DB Column is MNTFRAIS1. |
| 102 | `FS.GA.COUPON.MANAGEMENT.FEE.IN.AMOUNT.TYPE.2` | `FsGaCouponManagement_FeeInAmountType2` | TField |  | Amount of Fees charged on Income , type of fee 2 Multifonds DB Column is MNTFRAIS2. |
| 103 | `FS.GA.COUPON.MANAGEMENT.FEE.APPLICABLE.IN.AMTTYPE.1` | `FsGaCouponManagement_FeeApplicableInAmttype1` | TField |  | Amount of Fees charged on Income applicable , type of fee 1 Multifonds DB Column is FLG_FEE1. |
| 104 | `FS.GA.COUPON.MANAGEMENT.FEE.APPLICABLE.IN.AMTTYPE.2` | `FsGaCouponManagement_FeeApplicableInAmttype2` | TField |  | Amount of Fees charged on Income applicable, type of fee 2 Multifonds DB Column is FLG_FEE2. |
| 105 | `FS.GA.COUPON.MANAGEMENT.STOCK.DIVIDEND.APPLICABLE` | `FsGaCouponManagement_StockDividendApplicable` | TField |  | Stock dividend applicable on the income Multifonds DB Column is STK_DIV. |
| 106 | `FS.GA.COUPON.MANAGEMENT.SETTLED.INC` | `FsGaCouponManagement_SettledInc` | TField |  | Settled Inc Multifonds DB Column is SETTLED_INC. |
| 107 | `FS.GA.COUPON.MANAGEMENT.RECORD.DATE` | `FsGaCouponManagement_RecordDate` | TField |  | The record date, or date of record, is the cut-off date established by a company in order to determine which shareholders are eligible to receive a dividend or distribution Multifonds DB Column is DRECORD. |
| 108 | `FS.GA.COUPON.MANAGEMENT.LAST.COUPON.DATE` | `FsGaCouponManagement_LastCouponDate` | TField |  | Last Coupon Date Multifonds DB Column is DLASTCOUP_ORIG. |
| 109 | `FS.GA.COUPON.MANAGEMENT.CHECK.DATE` | `FsGaCouponManagement_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 110 | `FS.GA.COUPON.MANAGEMENT.CHECKED.BY` | `FsGaCouponManagement_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 111 | `FS.GA.COUPON.MANAGEMENT.AUTO.MANUAL.TAX` | `FsGaCouponManagement_AutoManualTax` | TField |  | Auto Manual Tax Multifonds DB Column is TAX_MANUAL_AUTO. |
| 112 | `FS.GA.COUPON.MANAGEMENT.IFRS.TAG` | `FsGaCouponManagement_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 113 | `FS.GA.COUPON.MANAGEMENT.LONG.DESCRIPTION` | `FsGaCouponManagement_LongDescription` | TField |  | Long description Multifonds DB Column is XLIBELLE_NEW. |
| 114 | `FS.GA.COUPON.MANAGEMENT.CASH.DIVIDEND` | `FsGaCouponManagement_CashDividend` | TField |  | Cash Dividend Flag Multifonds DB Column is FLG_CASH_DIV. |
| 115 | `FS.GA.COUPON.MANAGEMENT.DIVIDEND.TYPE` | `FsGaCouponManagement_DividendType` | TField |  | Dividend Type Multifonds DB Column is DIV_TYPE. |
| 116 | `FS.GA.COUPON.MANAGEMENT.ELECTION.STATUS` | `FsGaCouponManagement_ElectionStatus` | TField |  | Election Status Multifonds DB Column is ELECTION_STATUS. |
| 117 | `FS.GA.COUPON.MANAGEMENT.INSTRUCTION.STATUS` | `FsGaCouponManagement_InstructionStatus` | TField |  | Instruction Status Multifonds DB Column is INSTRUCTION_STATUS. |
| 118 | `FS.GA.COUPON.MANAGEMENT.AUTO.PROCESS` | `FsGaCouponManagement_AutoProcess` | TField |  | Auto Process Flag Multifonds DB Column is FLG_AUTO_PROCESS. |
| 119 | `FS.GA.COUPON.MANAGEMENT.CASH.RATIO` | `FsGaCouponManagement_CashRatio` | TField |  | Cash Ratio Multifonds DB Column is CASH_RATIO. |
| 120 | `FS.GA.COUPON.MANAGEMENT.CA.TRANSACTION.TYPE` | `FsGaCouponManagement_CaTransactionType` | TField |  | Corresponds to the corporate action transaction type Multifonds DB Column is COPER_CA. |
| 121 | `FS.GA.COUPON.MANAGEMENT.NSEQUENCE` | `FsGaCouponManagement_Nsequence` | TField |  | Corresponds to the sequence number Multifonds DB Column is NSEQ. |
| 122 | `FS.GA.COUPON.MANAGEMENT.SUBSEQUENCE.NUMBER` | `FsGaCouponManagement_SubsequenceNumber` | TField |  | Corresponds to the sub sequence number Multifonds DB Column is NSUB_SEQ. |
| 123 | `FS.GA.COUPON.MANAGEMENT.PA.MODULE` | `FsGaCouponManagement_PaModule` | TField |  | PA Module Multifonds DB Column is FLG_PA_MODULE. |
| 124 | `FS.GA.COUPON.MANAGEMENT.PA.STATUS` | `FsGaCouponManagement_PaStatus` | TField |  | PA Status Multifonds DB Column is PA_CDSTATUS. |
| 125 | `FS.GA.COUPON.MANAGEMENT.KR.RECOVERABLE.TAX` | `FsGaCouponManagement_KrRecoverableTax` | TField |  | Kr Recoverable Tax Multifonds DB Column is KRRECTAX. |
| 126 | `FS.GA.COUPON.MANAGEMENT.CREATE.COPY` | `FsGaCouponManagement_CreateCopy` | TField |  | Create Copy Flag Multifonds DB Column is FLG_CREATE_COPY. |
| 127 | `FS.GA.COUPON.MANAGEMENT.HOLDING.PERIOD.TAX.IN.PERCENT` | `FsGaCouponManagement_HoldingPeriodTaxInPercent` | TField |  | Holding period tax percentage on Income Multifonds DB Column is HOLD_TAX. |
| 128 | `FS.GA.COUPON.MANAGEMENT.FEES.HOLD` | `FsGaCouponManagement_FeesHold` | TField |  | Fees Hold Multifonds DB Column is CFRAIS_HOLD. |
| 129 | `FS.GA.COUPON.MANAGEMENT.TRANSACTION.TYPE.HOLD` | `FsGaCouponManagement_TransactionTypeHold` | TField |  | Transaction Type Hold Multifonds DB Column is COPER_HOLD. |
| 130 | `FS.GA.COUPON.MANAGEMENT.HOLDING.PERIOD.TAX.IN.AMOUNT` | `FsGaCouponManagement_HoldingPeriodTaxInAmount` | TField |  | Holding period tax Amount on Income Multifonds DB Column is MNTHOLD_TAX. |
| 131 | `FS.GA.COUPON.MANAGEMENT.FUND.WITHHOLDING.TAX.AMOUNT` | `FsGaCouponManagement_FundWithholdingTaxAmount` | TField |  | Fund Withholding tax amount Multifonds DB Column is MNTHOLD_TAX_PTF. |
| 132 | `FS.GA.COUPON.MANAGEMENT.TR.ACCOUNT.NUMBER` | `FsGaCouponManagement_TrAccountNumber` | TField |  | Nrubr Tr Multifonds DB Column is NRUBR_TR. |
| 133 | `FS.GA.COUPON.MANAGEMENT.UNRECOVERABLE.TAX.IN.FUND.CCY` | `FsGaCouponManagement_UnrecoverableTaxInFundCcy` | TField |  | Unrecoverable Tax In Fund Ccy Multifonds DB Column is MNTUNRECTAX_PTF. |
| 134 | `FS.GA.COUPON.MANAGEMENT.UNREC.TAX.2.IN.FUND.CCY` | `FsGaCouponManagement_UnrecTax2InFundCcy` | TField |  | Unrecoverabl Tax 2 In Fund Ccy Multifonds DB Column is MNTUNRECTAX_2_PTF. |
| 135 | `FS.GA.COUPON.MANAGEMENT.RECOVERABLE.TAX.IN.FUND.CCY` | `FsGaCouponManagement_RecoverableTaxInFundCcy` | TField |  | Recoverable Tax In Fund Ccy Multifonds DB Column is MNTRECTAX_PTF. |
| 136 | `FS.GA.COUPON.MANAGEMENT.RECOVERABLE.TAX.2.IN.FUND.CCY` | `FsGaCouponManagement_RecoverableTax2InFundCcy` | TField |  | Recoverable Tax 2 In Fund Ccy Multifonds DB Column is MNTRECTAX_2_PTF. |
| 137 | `FS.GA.COUPON.MANAGEMENT.GLOBAL.AMOUNT.IN.FUND.CCY` | `FsGaCouponManagement_GlobalAmountInFundCcy` | TField |  | Global Amount In Fund Ccy Multifonds DB Column is MNTGLOBAL_PTF. |
| 138 | `FS.GA.COUPON.MANAGEMENT.PIK.GLOBAL.AMOUNT.IN.FUND.CCY` | `FsGaCouponManagement_PikGlobalAmountInFundCcy` | TField |  | PIK Global Amount In Fund Ccy Multifonds DB Column is MNTGLOBAL_PIK_PTF. |
| 139 | `FS.GA.COUPON.MANAGEMENT.NET.AMOUNT.2` | `FsGaCouponManagement_NetAmount2` | TField |  | Net Amount 2 Multifonds DB Column is MNT_NET_2. |
| 140 | `FS.GA.COUPON.MANAGEMENT.NET.FUND.AMOUNT.2` | `FsGaCouponManagement_NetFundAmount2` | TField |  | Net Fund Amount 2 Multifonds DB Column is MNT_NET_2_PTF. |
| 141 | `FS.GA.COUPON.MANAGEMENT.SECURITY.FOREX.VCI.SETTLEMENT` | `FsGaCouponManagement_SecurityForexVciSettlement` | TField |  | Security Forex VCI Settlement Multifonds DB Column is SEC_SETTL_FX_VCI. |
| 142 | `FS.GA.COUPON.MANAGEMENT.FUND.FOREX.VCI.SECURITY` | `FsGaCouponManagement_FundForexVciSecurity` | TField |  | Fund Forex VCI Security Multifonds DB Column is SEC_PTF_FX_VCI. |
| 143 | `FS.GA.COUPON.MANAGEMENT.FUND.FX.SETTLEMENT.VCI` | `FsGaCouponManagement_FundFxSettlementVci` | TField |  | Settl Ptf Fx Vci Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 144 | `FS.GA.COUPON.MANAGEMENT.FRANKED.DIVIDEND.TAX.PERCENT` | `FsGaCouponManagement_FrankedDividendTaxPercent` | TField |  | Franked tax percentage on the dividend income Multifonds DB Column is PFRANKTAX. |
| 145 | `FS.GA.COUPON.MANAGEMENT.FRANKING.CREDIT.AMOUNT` | `FsGaCouponManagement_FrankingCreditAmount` | TField |  | Franking credit Amount booked on the income Multifonds DB Column is MNTFRANKTAX. |
| 146 | `FS.GA.COUPON.MANAGEMENT.CONDUIT.FOREIGN.INCOME.PERCENT` | `FsGaCouponManagement_ConduitForeignIncomePercent` | TField |  | Conduit Foreign Income percentage. CFI is ultimately received by a foreign resident through one or more interposed Australian corporate tax entities Multifonds DB Column is CFI_RATE. |
| 147 | `FS.GA.COUPON.MANAGEMENT.CFI.AMOUNT` | `FsGaCouponManagement_CfiAmount` | TField |  | Conduit Foreign Income Amount. CFI is ultimately received by a foreign resident through one or more interposed Australian corporate tax entities Multifonds DB Column is MNT_CFI. |
| 148 | `FS.GA.COUPON.MANAGEMENT.FRANKED.INCOME` | `FsGaCouponManagement_FrankedIncome` | TField |  | Franked Income Multifonds DB Column is PFRANK_INC. |
| 149 | `FS.GA.COUPON.MANAGEMENT.TAX.BASIS` | `FsGaCouponManagement_TaxBasis` | TField |  | Tax Basis Multifonds DB Column is TAX_BASIS. |
| 150 | `FS.GA.COUPON.MANAGEMENT.GTI.CODE` | `FsGaCouponManagement_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 151 | `FS.GA.COUPON.MANAGEMENT.FRANKING.CREDITS.IN.FUND.CCY` | `FsGaCouponManagement_FrankingCreditsInFundCcy` | TField |  | Franking Credits In Fund Ccy Multifonds DB Column is MNTFRANKTAX_PTF. |
| 152 | `FS.GA.COUPON.MANAGEMENT.GROSS.AMOUNT.IN.FUND.CCY` | `FsGaCouponManagement_GrossAmountInFundCcy` | TField |  | Gross Amount In Fund Ccy Multifonds DB Column is MNTGROSS_PTF. |
| 153 | `FS.GA.COUPON.MANAGEMENT.GLOBAL.AMOUNT.SPREAD` | `FsGaCouponManagement_GlobalAmountSpread` | TField |  | Global Amount Spread Multifonds DB Column is MNTGLOBAL_SPRD. |
| 154 | `FS.GA.COUPON.MANAGEMENT.CORRESPONDENT.SPREAD.AMOUNT` | `FsGaCouponManagement_CorrespondentSpreadAmount` | TField |  | Correspondant Spread Amount Multifonds DB Column is MNTCOMCORR_SPRD. |
| 155 | `FS.GA.COUPON.MANAGEMENT.UNRECOVERABLE.TAX.SPREAD.AMT` | `FsGaCouponManagement_UnrecoverableTaxSpreadAmt` | TField |  | Unrecoverable Tax Spread Amt Multifonds DB Column is MNTUNRECTAX_SPRD. |
| 156 | `FS.GA.COUPON.MANAGEMENT.NONRECOVERABLE.TAX.AMOUNT.2` | `FsGaCouponManagement_NonrecoverableTaxAmount2` | TField |  | Non recoverable tax amount 2 for coupon or dividend transaction Multifonds DB Column is MNTUNRECTAX_2_SPRD. |
| 157 | `FS.GA.COUPON.MANAGEMENT.SECURITY.LENDING.TAX.AMOUNT` | `FsGaCouponManagement_SecurityLendingTaxAmount` | TField |  | Security lending tax for coupon or dividend transaction Multifonds DB Column is MNTSECLENTAX_SPRD. |
| 158 | `FS.GA.COUPON.MANAGEMENT.RECOVERABLE.TAX.AMOUNT.1` | `FsGaCouponManagement_RecoverableTaxAmount1` | TField |  | Recoverable tax amount 1 for coupon or dividend transaction Multifonds DB Column is MNTRECTAX_SPRD. |
| 159 | `FS.GA.COUPON.MANAGEMENT.RECOVERABLE.TAX.AMOUNT.2` | `FsGaCouponManagement_RecoverableTaxAmount2` | TField |  | Recoverable tax amount 2 for coupon or dividend transaction Multifonds DB Column is MNTRECTAX_2_SPRD. |
| 160 | `FS.GA.COUPON.MANAGEMENT.HOLDING.PERIOD.TAX.AMOUNT` | `FsGaCouponManagement_HoldingPeriodTaxAmount` | TField |  | Holding period tax amount for coupon or dividend transaction Multifonds DB Column is MNTHOLD_TAX_SPRD. |
| 161 | `FS.GA.COUPON.MANAGEMENT.PAYABLE.TAX.AMOUNT.1` | `FsGaCouponManagement_PayableTaxAmount1` | TField |  | Payable tax amount 1 for coupon or dividend transaction Multifonds DB Column is MNT_TAX_1_SPRD. |
| 162 | `FS.GA.COUPON.MANAGEMENT.PAYABLE.TAX.AMOUNT.2` | `FsGaCouponManagement_PayableTaxAmount2` | TField |  | Payable tax amount 2 for coupon or dividend transaction Multifonds DB Column is MNT_TAX_2_SPRD. |
| 163 | `FS.GA.COUPON.MANAGEMENT.FEE.1.FOR.COUPON.OR.DIVIDEND` | `FsGaCouponManagement_Fee1ForCouponOrDividend` | TField |  | Fee amount 1 for coupon or dividend transaction Multifonds DB Column is MNTFRAIS1_SPRD. |
| 164 | `FS.GA.COUPON.MANAGEMENT.FEE.2.FOR.COUPON.OR.DIVIDEND` | `FsGaCouponManagement_Fee2ForCouponOrDividend` | TField |  | Fee amount 2 for coupon or dividend transaction Multifonds DB Column is MNTFRAIS2_SPRD. |
| 165 | `FS.GA.COUPON.MANAGEMENT.NETAMOUNT.OF.DIVIDEND.ORCOUPON` | `FsGaCouponManagement_NetamountOfDividendOrcoupon` | TField |  | Net amount of dividend or coupon after tax on Gross Amount of dividend or coupon Multifonds DB Column is MNTNET_SPRD. |
| 166 | `FS.GA.COUPON.MANAGEMENT.SPREAD.RATE` | `FsGaCouponManagement_SpreadRate` | TField |  | Spread rate which will be added to the &apos;Reference rate&apos; displayed at the bottom of the screen in order to get the applicable &apos;Interest rate&apos;. Multifonds DB Column is SPREAD_RATE. |
| 167 | `FS.GA.COUPON.MANAGEMENT.DIVIDEND.REINVESTMENT.DATE` | `FsGaCouponManagement_DividendReinvestmentDate` | TField |  | Dividend reinvestment date Multifonds DB Column is DREINV. |
| 168 | `FS.GA.COUPON.MANAGEMENT.DIVIDEND.REINVESTMENT.PRICE` | `FsGaCouponManagement_DividendReinvestmentPrice` | TField |  | The price at which dividend is reinvested. Multifonds DB Column is COURS_REINV. |
| 169 | `FS.GA.COUPON.MANAGEMENT.TOFA.TYPE` | `FsGaCouponManagement_TofaType` | TField |  | Indicates the TOFA category, Pre Tofa, Post TOFA etc Multifonds DB Column is TOFA_TYPE. |
| 170 | `FS.GA.COUPON.MANAGEMENT.CONDUIT.FOREIGN.INCOME.AMOUNT` | `FsGaCouponManagement_ConduitForeignIncomeAmount` | TField |  | Conduit Foreign Income Amount Multifonds DB Column is MNT_CFI_PTF. |
| 171 | `FS.GA.COUPON.MANAGEMENT.FATCA.PAYABLE.IN.PERCENT` | `FsGaCouponManagement_FatcaPayableInPercent` | TField |  | Rate of FATCA Tax payable on the income. FATCA is taxation based on US residence Multifonds DB Column is PFATCA_TAX1. |
| 172 | `FS.GA.COUPON.MANAGEMENT.FATCA.PAYABLE.IN.AMOUNT` | `FsGaCouponManagement_FatcaPayableInAmount` | TField |  | Amount of FATCA Tax payable on the income .FATCA is taxation based on US residence Multifonds DB Column is MNT_FATCA1. |
| 173 | `FS.GA.COUPON.MANAGEMENT.FATCA.TAX.AMOUNT.FUND.CCY` | `FsGaCouponManagement_FatcaTaxAmountFundCcy` | TField |  | FATCA Tax Amount Fund Ccy Multifonds DB Column is MNTFATCATAX1_PTF. |
| 174 | `FS.GA.COUPON.MANAGEMENT.FATCA.SPREAD.AMOUNT` | `FsGaCouponManagement_FatcaSpreadAmount` | TField |  | Payable fatca amount spread Multifonds DB Column is MNTFATCATAX1_SPRD. |
| 175 | `FS.GA.COUPON.MANAGEMENT.FATCA.RECOVERABLE.IN.PERCENT` | `FsGaCouponManagement_FatcaRecoverableInPercent` | TField |  | Rate of FATCA Tax recoverable on the income. FATCA is taxation based on US residence Multifonds DB Column is PFATCA_TAX2. |
| 176 | `FS.GA.COUPON.MANAGEMENT.FATCA.REC.SPREAD.AMOUNT` | `FsGaCouponManagement_FatcaRecSpreadAmount` | TField |  | Recoverable fatca amount spread Multifonds DB Column is MNTFATCATAX2_SPRD. |
| 177 | `FS.GA.COUPON.MANAGEMENT.FATCA.PAYABLE.TAX` | `FsGaCouponManagement_FatcaPayableTax` | TField |  | To enable FATCA Payable Tax percentage for dividend or coupon Multifonds DB Column is FLG_FATCATAX1. |
| 178 | `FS.GA.COUPON.MANAGEMENT.FATCA.RECEIVABLE.TAX` | `FsGaCouponManagement_FatcaReceivableTax` | TField |  | To enable FATCA Tax 2 percentage for dividend or coupon Multifonds DB Column is FLG_FATCATAX2. |
| 179 | `FS.GA.COUPON.MANAGEMENT.PERCENTAGE.OF.TAX` | `FsGaCouponManagement_PercentageOfTax` | TField |  | Tax income percentage on income Multifonds DB Column is TAX_INC. |
| 180 | `FS.GA.COUPON.MANAGEMENT.NON.ACCRUAL.STATUS` | `FsGaCouponManagement_NonAccrualStatus` | TField |  | Flag to denote whether the security is in a defaulted status Multifonds DB Column is FLG_NON_ACC_STATUS. |
| 181 | `FS.GA.COUPON.MANAGEMENT.AMOUNT.RECEIVED` | `FsGaCouponManagement_AmountReceived` | TField |  | Amount Received Multifonds DB Column is AMOUNT_RECEIVED. |
| 182 | `FS.GA.COUPON.MANAGEMENT.AMOUNT.RECEIVED.IN.FUND.CCY` | `FsGaCouponManagement_AmountReceivedInFundCcy` | TField |  | Amount Received In Fund Ccy Multifonds DB Column is AMOUNT_RECEIVED_PTF. |
| 183 | `FS.GA.COUPON.MANAGEMENT.NET.AMOUNT.IN.FCY` | `FsGaCouponManagement_NetAmountInFcy` | TField |  | Net Amount In Fcy Multifonds DB Column is MNTNET_FCY. |
| 184 | `FS.GA.COUPON.MANAGEMENT.EXCHANGE.RATE.IN.FCY` | `FsGaCouponManagement_ExchangeRateInFcy` | TField |  | Exchange Rate In Fcy Multifonds DB Column is TCHG_FCY. |
| 185 | `FS.GA.COUPON.MANAGEMENT.45.DAY.INCLUSION` | `FsGaCouponManagement_45DayInclusion` |  |  |  |
| 186 | `FS.GA.COUPON.MANAGEMENT.ID.OF.TRANSACTION` | `FsGaCouponManagement_IdOfTransaction` | TField |  | ID Of Transaction Multifonds DB Column is TRANSACTION_ID. |
| 187 | `FS.GA.COUPON.MANAGEMENT.TRADE.ID` | `FsGaCouponManagement_TradeId` | TField |  | Trade Id Multifonds DB Column is TRADEID. |
| 188 | `FS.GA.COUPON.MANAGEMENT.KNOWLEDGE.DATE` | `FsGaCouponManagement_KnowledgeDate` | TField |  | Knowledge Date Multifonds DB Column is KNOWLEDGEDATE. |
| 189 | `FS.GA.COUPON.MANAGEMENT.LOT.ID` | `FsGaCouponManagement_LotId` | TField |  | Lot ID Multifonds DB Column is LOTID. |
| 190 | `FS.GA.COUPON.MANAGEMENT.INCOME.LAG.PRC` | `FsGaCouponManagement_IncomeLagPrc` | TField |  | Income Lag Prc Flag Multifonds DB Column is FLG_INC_LAG_PRC. |
| 191 | `FS.GA.COUPON.MANAGEMENT.TAXABLE.FACTOR` | `FsGaCouponManagement_TaxableFactor` | TField |  | Taxable Factor Multifonds DB Column is FACTOR_TAX. |
| 192 | `FS.GA.COUPON.MANAGEMENT.TAX.FREE.FACTOR` | `FsGaCouponManagement_TaxFreeFactor` | TField |  | Tax Free Factor Multifonds DB Column is FACTOR_TAX_FREE. |
| 193 | `FS.GA.COUPON.MANAGEMENT.TAXABLE.AMOUNT.CMV` | `FsGaCouponManagement_TaxableAmountCmv` | TField |  | Taxable Amount Cmv Multifonds DB Column is MNT_TAX_CMV. |
| 194 | `FS.GA.COUPON.MANAGEMENT.TAX.FREE.AMOUNT.CMV` | `FsGaCouponManagement_TaxFreeAmountCmv` | TField |  | Tax Free Amount Cmv Multifonds DB Column is MNT_TAX_FREE_CMV. |
| 195 | `FS.GA.COUPON.MANAGEMENT.AGS.QUANTITY` | `FsGaCouponManagement_AgsQuantity` | TField |  | AGS Quantity Multifonds DB Column is AGS_QUANTITE. |
| 196 | `FS.GA.COUPON.MANAGEMENT.NON.AGS.QUANTITY` | `FsGaCouponManagement_NonAgsQuantity` | TField |  | Non AGS Quantity Multifonds DB Column is NON_AGS_QUANTITE. |
| 197 | `FS.GA.COUPON.MANAGEMENT.CORPORATE.ACTION.TYPE` | `FsGaCouponManagement_CorporateActionType` | TField |  | Corporate Action Type Multifonds DB Column is CA_TYPE. |
| 198 | `FS.GA.COUPON.MANAGEMENT.ISSUE.COUNTRY` | `FsGaCouponManagement_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 199 | `FS.GA.COUPON.MANAGEMENT.RESERVED10` | `FsGaCouponManagement_Reserved10` | TField |  |  |
| 200 | `FS.GA.COUPON.MANAGEMENT.RESERVED9` | `FsGaCouponManagement_Reserved9` | TField |  |  |
| 201 | `FS.GA.COUPON.MANAGEMENT.RESERVED8` | `FsGaCouponManagement_Reserved8` | TField |  |  |
| 202 | `FS.GA.COUPON.MANAGEMENT.RESERVED7` | `FsGaCouponManagement_Reserved7` | TField |  |  |
| 203 | `FS.GA.COUPON.MANAGEMENT.RESERVED6` | `FsGaCouponManagement_Reserved6` | TField |  |  |
| 204 | `FS.GA.COUPON.MANAGEMENT.RESERVED5` | `FsGaCouponManagement_Reserved5` | TField |  |  |
| 205 | `FS.GA.COUPON.MANAGEMENT.RESERVED4` | `FsGaCouponManagement_Reserved4` | TField |  |  |
| 206 | `FS.GA.COUPON.MANAGEMENT.RESERVED3` | `FsGaCouponManagement_Reserved3` | TField |  |  |
| 207 | `FS.GA.COUPON.MANAGEMENT.RESERVED2` | `FsGaCouponManagement_Reserved2` | TField |  |  |
| 208 | `FS.GA.COUPON.MANAGEMENT.RESERVED1` | `FsGaCouponManagement_Reserved1` | TField |  |  |
| 209 | `FS.GA.COUPON.MANAGEMENT.LOCAL.REF` | `FsGaCouponManagement_LocalRef` |  |  |  |
| 210 | `FS.GA.COUPON.MANAGEMENT.OVERRIDE` | `FsGaCouponManagement_Override` |  |  |  |
| 211 | `FS.GA.COUPON.MANAGEMENT.RECORD.STATUS` | `FsGaCouponManagement_RecordStatus` | String |  |  |
| 212 | `FS.GA.COUPON.MANAGEMENT.CURR.NO` | `FsGaCouponManagement_CurrNo` | String |  |  |
| 213 | `FS.GA.COUPON.MANAGEMENT.INPUTTER` | `FsGaCouponManagement_Inputter` |  |  |  |
| 214 | `FS.GA.COUPON.MANAGEMENT.DATE.TIME` | `FsGaCouponManagement_DateTime` |  |  |  |
| 215 | `FS.GA.COUPON.MANAGEMENT.AUTHORISER` | `FsGaCouponManagement_Authoriser` | String |  |  |
| 216 | `FS.GA.COUPON.MANAGEMENT.CO.CODE` | `FsGaCouponManagement_CoCode` | String |  |  |
| 217 | `FS.GA.COUPON.MANAGEMENT.DEPT.CODE` | `FsGaCouponManagement_DeptCode` | String |  |  |
| 218 | `FS.GA.COUPON.MANAGEMENT.AUDITOR.CODE` | `FsGaCouponManagement_AuditorCode` | String |  |  |
| 219 | `FS.GA.COUPON.MANAGEMENT.AUDIT.DATE.TIME` | `FsGaCouponManagement_AuditDateTime` | String |  |  |
