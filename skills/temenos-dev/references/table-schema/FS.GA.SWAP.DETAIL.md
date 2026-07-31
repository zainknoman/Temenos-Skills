# FS.GA.SWAP.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.SWAP.DETAIL` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SWAP.DETAIL.FUND.ID` | `FsGaSwapDetail_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.SWAP.DETAIL.SERVICE.CODE` | `FsGaSwapDetail_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 3 | `FS.GA.SWAP.DETAIL.OPERATION.CODE` | `FsGaSwapDetail_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 4 | `FS.GA.SWAP.DETAIL.LOT.NUMBER` | `FsGaSwapDetail_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 5 | `FS.GA.SWAP.DETAIL.TRANSACTION.NUMBER` | `FsGaSwapDetail_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.SWAP.DETAIL.DEAL.STATUS.CODE` | `FsGaSwapDetail_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 7 | `FS.GA.SWAP.DETAIL.TRADE.DATE` | `FsGaSwapDetail_TradeDate` | TField |  | Trade date of the trnsaction Multifonds DB Column is DOPER. |
| 8 | `FS.GA.SWAP.DETAIL.SETTLE.DATE` | `FsGaSwapDetail_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 9 | `FS.GA.SWAP.DETAIL.MATURITY.DATE.OF.CONTRACT` | `FsGaSwapDetail_MaturityDateOfContract` | TField |  | Maturity Date of the Contract/Instrument Multifonds DB Column is DECH. |
| 10 | `FS.GA.SWAP.DETAIL.CURRENCY.OF.INTEREST` | `FsGaSwapDetail_CurrencyOfInterest` | TField |  | Currency of Interest Multifonds DB Column is CMON_TAUX. |
| 11 | `FS.GA.SWAP.DETAIL.GL.ACCOUNT` | `FsGaSwapDetail_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 12 | `FS.GA.SWAP.DETAIL.GL.ACCOUNT.SUFFIX` | `FsGaSwapDetail_GlAccountSuffix` | TField |  | Suffix number tagged to the account number. In case of cash this identifies the correspondent and for other P and L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 13 | `FS.GA.SWAP.DETAIL.GL.ACCOUNT.OF.CONTRACT` | `FsGaSwapDetail_GlAccountOfContract` | TField |  | Account Number for Contractual Instruments ex. FRAs Multifonds DB Column is NRUBR_INT. |
| 14 | `FS.GA.SWAP.DETAIL.GL.ACCOUNT.SUFFIX.OF.CONTRACT` | `FsGaSwapDetail_GlAccountSuffixOfContract` | TField |  | Account Number Suffix for Contractual Instruments ex. FRAs Multifonds DB Column is NSUFF_INT. |
| 15 | `FS.GA.SWAP.DETAIL.DAY.COUNT.BASIS.FUND.LEG.IRS` | `FsGaSwapDetail_DayCountBasisFundLegIrs` | TField |  | Corresponds to the calculation basis of accrued interest for the Fund leg of IRS (pertains to the lending part of the swap (receivable)). Multifonds DB Column is CUSANCE_INT. |
| 16 | `FS.GA.SWAP.DETAIL.NOMINAL.AMOUNT.FUND.LEG.IRS` | `FsGaSwapDetail_NominalAmountFundLegIrs` | TField |  | Displays the nominal amount of the swap on the fund leg of IRS (pertains to the lending part of the swap (receivable)). Multifonds DB Column is MNT_CAP_INT. |
| 17 | `FS.GA.SWAP.DETAIL.CURRENCY.NOMINAL.FUND` | `FsGaSwapDetail_CurrencyNominalFund` | TField |  | Currency Nominal for Fund leg in Swaps Multifonds DB Column is CMON_INT. |
| 18 | `FS.GA.SWAP.DETAIL.FIXING.DATE.INT` | `FsGaSwapDetail_FixingDateInt` | TField |  | Fixing Date INT Multifonds DB Column is DFIX_INT. |
| 19 | `FS.GA.SWAP.DETAIL.FREQUENCY.CODE.FUND` | `FsGaSwapDetail_FrequencyCodeFund` | TField |  | Frequency code of coupon Fund leg for swaps Multifonds DB Column is CFREQ_INT. |
| 20 | `FS.GA.SWAP.DETAIL.COUPON.PAYMENT.DATE.FUND` | `FsGaSwapDetail_CouponPaymentDateFund` | TField |  | Coupon Payment Date for Fund Leg Multifonds DB Column is DFREQ_INT. |
| 21 | `FS.GA.SWAP.DETAIL.IRREGULAR.PERIOD.START.FUND` | `FsGaSwapDetail_IrregularPeriodStartFund` | TField |  | Irregular period start date for Interest accrual Fund leg Multifonds DB Column is DIRG_DEB_INT. |
| 22 | `FS.GA.SWAP.DETAIL.IRREGULAR.PERIOD.END.FUND` | `FsGaSwapDetail_IrregularPeriodEndFund` | TField |  | Irregular period end date for Interest accrual Fund leg Multifonds DB Column is DIRG_END_INT. |
| 23 | `FS.GA.SWAP.DETAIL.INTEREST.RATE.PCT.FUND.LEG.IRS` | `FsGaSwapDetail_InterestRatePctFundLegIrs` | TField |  | Correspond to fixed int. rate set up manually or floating or variable rate retrieved automatically by the system as per yield curve according to the currency and the delay day,for the fund leg of IRS. Multifonds DB Column is TAUX_INT. |
| 24 | `FS.GA.SWAP.DETAIL.INT.RATE.TYPE.FUND.LEG.IRS` | `FsGaSwapDetail_IntRateTypeFundLegIrs` | TField |  | The int. rate type manages interest calculation on fund leg of swap contract. It is as defined in FDTAU02 Forward interest rate screen and in CMESS table TYP_TAUX (e.g. 'EON' - Eonia, 'LIB' - Libor...) Multifonds DB Column is TYP_TAUX_INT. |
| 25 | `FS.GA.SWAP.DETAIL.INTEREST.RATE.TYPE.TERM.FUND` | `FsGaSwapDetail_InterestRateTypeTermFund` | TField |  | The Term for the interest rate type like OND for overnight etc for Fund leg Multifonds DB Column is TYP_TERM_INT. |
| 26 | `FS.GA.SWAP.DETAIL.SPREAD.FUND` | `FsGaSwapDetail_SpreadFund` | TField |  | Spread for Fund leg in swaps Multifonds DB Column is SPREAD_INT. |
| 27 | `FS.GA.SWAP.DETAIL.CAP.RATE.PERCENT.FUND.LEG.SWAP` | `FsGaSwapDetail_CapRatePercentFundLegSwap` | TField |  | If the swap contract have cap rates on the fund leg of the contract, the entered in this field. This field is usually not used for standard IRS. Multifonds DB Column is CAP_INT. |
| 28 | `FS.GA.SWAP.DETAIL.FLOOR.RATE.PCT.FUND.LEG.SWAP` | `FsGaSwapDetail_FloorRatePctFundLegSwap` | TField |  | If the swap contract have floor rates on the fund leg of the contract, the entered in this field. This field is usually not used for standard IRS. Multifonds DB Column is FLOOR_INT. |
| 29 | `FS.GA.SWAP.DETAIL.CORRESPONDENT` | `FsGaSwapDetail_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 30 | `FS.GA.SWAP.DETAIL.COUNTERPART.ACCOUNT.NUMBER` | `FsGaSwapDetail_CounterpartAccountNumber` | TField |  | Counterpart Account Number Multifonds DB Column is NRUBR_COR. |
| 31 | `FS.GA.SWAP.DETAIL.COUNTERPART.SUFFIX.NUMBER` | `FsGaSwapDetail_CounterpartSuffixNumber` | TField |  | Counterpart Suffix Number Multifonds DB Column is NSUFF_COR. |
| 32 | `FS.GA.SWAP.DETAIL.INTERESTCALCULATIONCODE.CPARTY` | `FsGaSwapDetail_InterestcalculationcodeCparty` | TField |  | Interestcalculationcode for accrued interest calculation for Counterparty in swaps Multifonds DB Column is CUSANCE_COR. |
| 33 | `FS.GA.SWAP.DETAIL.NOMINAL.AMT.COUNTERPARTY.IRS` | `FsGaSwapDetail_NominalAmtCounterpartyIrs` | TField |  | Displays the nominal amount of the swap on the counterparty leg of IRS (pertains to the borrowing part of the swap (payable)). Multifonds DB Column is MNT_CAP_COR. |
| 34 | `FS.GA.SWAP.DETAIL.NOMINAL.CCY.COUNTERPARTY.IRS` | `FsGaSwapDetail_NominalCcyCounterpartyIrs` | TField |  | Currency of the swap contract in which the nominal amount on the counterparty leg (payable) is denominated. Multifonds DB Column is CMON_COR. |
| 35 | `FS.GA.SWAP.DETAIL.FIXING.DATE.COR` | `FsGaSwapDetail_FixingDateCor` | TField |  | Fixing Date COR Multifonds DB Column is DFIX_COR. |
| 36 | `FS.GA.SWAP.DETAIL.FREQUENCY.CODE.CPARTY` | `FsGaSwapDetail_FrequencyCodeCparty` | TField |  | Frequency code of coupon Counterparty leg for swaps Multifonds DB Column is CFREQ_COR. |
| 37 | `FS.GA.SWAP.DETAIL.COUPON.PAYMENT.DATE.CPARTY` | `FsGaSwapDetail_CouponPaymentDateCparty` | TField |  | Coupon Payment Date for Counterparty leg Multifonds DB Column is DFREQ_COR. |
| 38 | `FS.GA.SWAP.DETAIL.IRREGULAR.PERIOD.START.CPARTY` | `FsGaSwapDetail_IrregularPeriodStartCparty` | TField |  | Irregular period start date for Interest accrual counterparty leg Multifonds DB Column is DIRG_DEB_COR. |
| 39 | `FS.GA.SWAP.DETAIL.IRREGULAR.PERIOD.END.CPARTY` | `FsGaSwapDetail_IrregularPeriodEndCparty` | TField |  | Irregular period end date for Interest accrual counterparty leg Multifonds DB Column is DIRG_END_COR. |
| 40 | `FS.GA.SWAP.DETAIL.INT.RATE.PCT.COUNTERPARTY.IRS` | `FsGaSwapDetail_IntRatePctCounterpartyIrs` | TField |  | Correspond to fixed int. rate set up manually or floating or variable rate retrieved automatically by the system as per yield curve according to currency and delay day,for the counterparty leg of IRS. Multifonds DB Column is TAUX_COR. |
| 41 | `FS.GA.SWAP.DETAIL.INTEREST.RATE.TYPE.SWAP.LEG` | `FsGaSwapDetail_InterestRateTypeSwapLeg` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX_COR. |
| 42 | `FS.GA.SWAP.DETAIL.INTEREST.RATE.TYPE.TERM.CPARTY` | `FsGaSwapDetail_InterestRateTypeTermCparty` | TField |  | The Term for the interest rate type like OND for overnight etc for Counterparty leg Multifonds DB Column is TYP_TERM_COR. |
| 43 | `FS.GA.SWAP.DETAIL.SPREAD.CPARTY` | `FsGaSwapDetail_SpreadCparty` | TField |  | Spread for counterparty leg in swaps Multifonds DB Column is SPREAD_COR. |
| 44 | `FS.GA.SWAP.DETAIL.CAP.RATE.PCT.COUNTERPARTY.SWAP` | `FsGaSwapDetail_CapRatePctCounterpartySwap` | TField |  | If the swap contract have cap rates on the counterparty leg of the contract, the entered in this field. This field is usually not used for standard IRS. Multifonds DB Column is CAP_COR. |
| 45 | `FS.GA.SWAP.DETAIL.FLOOR.RATE.COUNTERPARTY.SWAP` | `FsGaSwapDetail_FloorRateCounterpartySwap` | TField |  | If the swap contract have floor rates on the counterparty leg of the contract, the entered in this field. This field is usually not used for standard IRS. Multifonds DB Column is FLOOR_COR. |
| 46 | `FS.GA.SWAP.DETAIL.DESCRIPTION` | `FsGaSwapDetail_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 47 | `FS.GA.SWAP.DETAIL.SWAP.INTEREST.FULLY.PAID` | `FsGaSwapDetail_SwapInterestFullyPaid` | TField |  | The flag located in FDSWI03 screen gets flagged if all the interest payments due (IR6/IR7) till maturity have been paid. Multifonds DB Column is ALL_PAYED. |
| 48 | `FS.GA.SWAP.DETAIL.ENTRY.NUMBER.REPAYMENT` | `FsGaSwapDetail_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 49 | `FS.GA.SWAP.DETAIL.IRS.INTEREST.CALCULATION` | `FsGaSwapDetail_IrsInterestCalculation` | TField |  | If set, for swap transactions, by default field 'Int. calc' is checked in the IRS transaction deal screen to allow the interest calculation. Multifonds DB Column is FCVAL_INT. |
| 50 | `FS.GA.SWAP.DETAIL.MANAGER.CODE` | `FsGaSwapDetail_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 51 | `FS.GA.SWAP.DETAIL.HEDGING.OR.TRADING.CATEGORY` | `FsGaSwapDetail_HedgingOrTradingCategory` | TField |  | Hedging or Trading Category Multifonds DB Column is CD_HEDG. |
| 52 | `FS.GA.SWAP.DETAIL.COUNTERPARTY.CORRESPONDENT` | `FsGaSwapDetail_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 53 | `FS.GA.SWAP.DETAIL.COUNTER.PARTY.CODE` | `FsGaSwapDetail_CounterPartyCode` | TField |  | Guarantor,Issuer Multifonds DB Column is NISSUER_GUARANTEED. |
| 54 | `FS.GA.SWAP.DETAIL.CALCULATION.PAYMENT.DATE` | `FsGaSwapDetail_CalculationPaymentDate` | TField |  | Logic to decide if payment date falls on a non working day should it process paymet on same date or prior/next working day. Multifonds DB Column is CTR_DATE. |
| 55 | `FS.GA.SWAP.DETAIL.EVALUATION.TYPE` | `FsGaSwapDetail_EvaluationType` | TField |  | Valuation method for specific security types such as zero bonds, polish T-bills, Mortgaged Backed Securities. Multifonds DB Column is TEVALUATION. |
| 56 | `FS.GA.SWAP.DETAIL.IRS.DATE` | `FsGaSwapDetail_IrsDate` | TField |  | Always checked by default. The system will populate the IRS date in the interest payment screen FDSWI03 (Deals/IRS/Payment/Create/Periods) Multifonds DB Column is FLG_NEW. |
| 57 | `FS.GA.SWAP.DETAIL.STATUS.PENDING` | `FsGaSwapDetail_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 58 | `FS.GA.SWAP.DETAIL.ARCHIVE` | `FsGaSwapDetail_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 59 | `FS.GA.SWAP.DETAIL.EXTERNAL.REFERENCE` | `FsGaSwapDetail_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 60 | `FS.GA.SWAP.DETAIL.UPFRONT.AMOUNT` | `FsGaSwapDetail_UpfrontAmount` | TField |  | Upfront amount Multifonds DB Column is MNT_UPFRONT. |
| 61 | `FS.GA.SWAP.DETAIL.FLAG.UPFRONT.IRS` | `FsGaSwapDetail_FlagUpfrontIrs` | TField |  | The user can input in this field if upfront amount is receivable "R" or payable "P". Multifonds DB Column is FLG_UPFRONT. |
| 62 | `FS.GA.SWAP.DETAIL.SWAP.CHARGES.OR.FEES.PAYABLE` | `FsGaSwapDetail_SwapChargesOrFeesPayable` | TField |  | The user can input a charge/fee amount payable on the swap contract. This amount is booked with fee code IA if the check box 'New IRS deal' or "CDS index" is ticked. Multifonds DB Column is MNT_MFRAIS. |
| 63 | `FS.GA.SWAP.DETAIL.ACCRUED.INTEREST.CPARTY` | `FsGaSwapDetail_AccruedInterestCparty` | TField |  | Accrued Interest for Swaps counterparty leg Multifonds DB Column is MINT_DEFFERAL. |
| 64 | `FS.GA.SWAP.DETAIL.UPFRONT.AMOUNT.REAL` | `FsGaSwapDetail_UpfrontAmountReal` | TField |  | Upfront amount receivable or payable Multifonds DB Column is MNT_UPFRONT_REAL. |
| 65 | `FS.GA.SWAP.DETAIL.COUPON.DATE.LIST` | `FsGaSwapDetail_CouponDateList` | TField |  | Coupon Date List Multifonds DB Column is DLST_COUPON. |
| 66 | `FS.GA.SWAP.DETAIL.FLAG.FOR.UPFRONT.AMOUNT` | `FsGaSwapDetail_FlagForUpfrontAmount` | TField |  | Flag for upfront amount Multifonds DB Column is FLG_UPFRONT_REAL. |
| 67 | `FS.GA.SWAP.DETAIL.CASH.FLOW.AMOUNT` | `FsGaSwapDetail_CashFlowAmount` | TField |  | Cash Flow Amount Multifonds DB Column is MNT_CASH_FLOW. |
| 68 | `FS.GA.SWAP.DETAIL.CASH.FLOW.FLAG` | `FsGaSwapDetail_CashFlowFlag` | TField |  | Cash Flow Flag Multifonds DB Column is FLG_CASH_FLOW. |
| 69 | `FS.GA.SWAP.DETAIL.RATE.CODE` | `FsGaSwapDetail_RateCode` | TField |  | This field is used for reporting purpose, year end reports. It can be modified after validation Multifonds DB Column is SENSE. |
| 70 | `FS.GA.SWAP.DETAIL.UPFRONT.INTEREST.FUND` | `FsGaSwapDetail_UpfrontInterestFund` | TField |  | Upfront interest amount at fund leg Multifonds DB Column is MNT_UPFRONT_INT. |
| 71 | `FS.GA.SWAP.DETAIL.FLAG.UPFRONT.INTEREST.FUND` | `FsGaSwapDetail_FlagUpfrontInterestFund` | TField |  | Flag for Upfront interest at fund leg Multifonds DB Column is FLG_UPFRONT_INT. |
| 72 | `FS.GA.SWAP.DETAIL.UPFRONT.CURRENCY.FUND.LEG.SWAP` | `FsGaSwapDetail_UpfrontCurrencyFundLegSwap` | TField |  | Represents the currency in which upfront amount is denominated on the fund leg of swap contract. The defining of different upfront amt is specific to op. code IC1. Multifonds DB Column is CDEV_UPFRONT_INT. |
| 73 | `FS.GA.SWAP.DETAIL.UPFRONT.INTEREST.CPARTY` | `FsGaSwapDetail_UpfrontInterestCparty` | TField |  | Upfront interest amount at counteparty leg Multifonds DB Column is MNT_UPFRONT_COR. |
| 74 | `FS.GA.SWAP.DETAIL.FLAG.UPFRONT.INTEREST.CPARTY` | `FsGaSwapDetail_FlagUpfrontInterestCparty` | TField |  | Flag for Upfront interest at counterparty leg Multifonds DB Column is FLG_UPFRONT_COR. |
| 75 | `FS.GA.SWAP.DETAIL.UPFRONT.CCY.COUNTERPARTY.SWAP` | `FsGaSwapDetail_UpfrontCcyCounterpartySwap` | TField |  | Represents the currency in which upfront amount is denominated on the counterparty leg of swap contract. The defining of different upfront amt is specific to op. code IC1. Multifonds DB Column is CDEV_UPFRONT_COR. |
| 76 | `FS.GA.SWAP.DETAIL.INCOME.TYPE` | `FsGaSwapDetail_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 77 | `FS.GA.SWAP.DETAIL.EXCHANGE.OF.NOTIONAL.ICS` | `FsGaSwapDetail_ExchangeOfNotionalIcs` | TField |  | Allows notional (principal) to be exchanged or not. N: Notional of the contract is not exchanged with the counterparty. Y: Notional is exchanged with a cash movement. Used in case of ICS contract. Multifonds DB Column is EXCHANGE_NOTIONAL. |
| 78 | `FS.GA.SWAP.DETAIL.COLLATERAL.VALUATION` | `FsGaSwapDetail_CollateralValuation` | TField |  | Switch to activate the valuation of collateral for Swaps Multifonds DB Column is VALUATION_COLLATERAL. |
| 79 | `FS.GA.SWAP.DETAIL.INT.RATE.DELAY.DAYS.FUND.LEG` | `FsGaSwapDetail_IntRateDelayDaysFundLeg` | TField |  | Only applicable for Revised rate (code = 5). The system auto retrieves int rate date to use minus the no. of days defined on the fund leg of swap. These delay days are used when the rate is revised. Multifonds DB Column is DELAY_DAYS_INT. |
| 80 | `FS.GA.SWAP.DETAIL.INT.RATE.DELAY.DAY.COUNTERPART` | `FsGaSwapDetail_IntRateDelayDayCounterpart` | TField |  | Only applicable for Revised rate (code = 5). System auto retrieves int rate date to use minus the no. of days defined on counterparty leg of swap. These delay days are used when the rate is revised. Multifonds DB Column is DELAY_DAYS_COR. |
| 81 | `FS.GA.SWAP.DETAIL.FLOATING.RATE.METHOD.FUND.LEG` | `FsGaSwapDetail_FloatingRateMethodFundLeg` | TField |  | For floating int rate on swap's fund leg if maturity is defined as daily rate eg. OND,Method is code 3-Avg or 2-Daily avg compound.Method is defined as code 5-Revised rate for periodic rate eg.1MD. Multifonds DB Column is METHOD_INT. |
| 82 | `FS.GA.SWAP.DETAIL.FLOATING.METHOD.COUNTERPARTY` | `FsGaSwapDetail_FloatingMethodCounterparty` | TField |  | For floating int rate on swap counterparty leg if maturity is defined as daily rate eg. OND,Method is 3-Avg or 2-Daily avg compound.Method is defined as code 5-Revised rate for periodic rate eg.1MD. Multifonds DB Column is METHOD_COR. |
| 83 | `FS.GA.SWAP.DETAIL.INTERNAL.SECURITY.ID` | `FsGaSwapDetail_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 84 | `FS.GA.SWAP.DETAIL.GTI.CODE` | `FsGaSwapDetail_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 85 | `FS.GA.SWAP.DETAIL.PROVIDER.ID` | `FsGaSwapDetail_ProviderId` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 86 | `FS.GA.SWAP.DETAIL.PRICE.SOURCE` | `FsGaSwapDetail_PriceSource` | TField |  | Provider code like Telekers, Reuters etc Multifonds DB Column is CORC. |
| 87 | `FS.GA.SWAP.DETAIL.CDS.COLLATERAL` | `FsGaSwapDetail_CdsCollateral` | TField |  | Checked for CDS. Allows attaching underlying asset in "Collateral" button though fund doesn't hold position (for info). If unchecked,only held position is linked in "collateral" tab (for asset swap). Multifonds DB Column is FLG_CDS_SWAP. |
| 88 | `FS.GA.SWAP.DETAIL.EXECUTION.TIMESTAMP` | `FsGaSwapDetail_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 89 | `FS.GA.SWAP.DETAIL.INCOME.TYPE.CPARTY` | `FsGaSwapDetail_IncomeTypeCparty` | TField |  | Denotes when to start interest accrual from first day or from value date for Counterparty leg Multifonds DB Column is TREVENU_COR. |
| 90 | `FS.GA.SWAP.DETAIL.NB.DAYS.TO.ADD.CPARTY` | `FsGaSwapDetail_NbDaysToAddCparty` | TField |  | Nb Days to Add for Value date of coupon for Counterparty leg Multifonds DB Column is ADD_DAYS_COR. |
| 91 | `FS.GA.SWAP.DETAIL.WORKING.DAYS.FLAG.CPARTY` | `FsGaSwapDetail_WorkingDaysFlagCparty` | TField |  | Consider working days for value date of coupon for Counteparty leg Multifonds DB Column is FLG_WORKING_DAYS_COR. |
| 92 | `FS.GA.SWAP.DETAIL.CFS.ID` | `FsGaSwapDetail_CfsId` | TField |  | It is a free text to enter for 20 characters Multifonds DB Column is CFS_ID. |
| 93 | `FS.GA.SWAP.DETAIL.CDS.TYPE` | `FsGaSwapDetail_CdsType` | TField |  | Credit default swap dealing type like Trading or hedging Multifonds DB Column is CDS_TYPE. |
| 94 | `FS.GA.SWAP.DETAIL.INTEREST.TRACKING` | `FsGaSwapDetail_InterestTracking` | TField |  | Interest Tracking Multifonds DB Column is INT_TRACK. |
| 95 | `FS.GA.SWAP.DETAIL.FLAG.CAP` | `FsGaSwapDetail_FlagCap` | TField |  | Flag Cap Multifonds DB Column is FLG_CAP. |
| 96 | `FS.GA.SWAP.DETAIL.FUND.STRATEGY` | `FsGaSwapDetail_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 97 | `FS.GA.SWAP.DETAIL.FUND.LINK.ID` | `FsGaSwapDetail_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 98 | `FS.GA.SWAP.DETAIL.EXTERNAL.CONTRACT.NUMBER` | `FsGaSwapDetail_ExternalContractNumber` | TField |  | External Contract Number Multifonds DB Column is NCONTRAT_EXT. |
| 99 | `FS.GA.SWAP.DETAIL.VALUE.DATE.FOR.UPFRONT` | `FsGaSwapDetail_ValueDateForUpfront` | TField |  | Value Date for upfront Multifonds DB Column is DVALEUR_UPFRONT. |
| 100 | `FS.GA.SWAP.DETAIL.UPFRONT.AMOUNT.CURRENCY` | `FsGaSwapDetail_UpfrontAmountCurrency` | TField |  | Upfront amount Currency Multifonds DB Column is CDEV_UPFRONT. |
| 101 | `FS.GA.SWAP.DETAIL.SHARE.CLASS.CODE` | `FsGaSwapDetail_ShareClassCode` | TField |  | Share class Multifonds DB Column is TPARTS. |
| 102 | `FS.GA.SWAP.DETAIL.CASH.FLOW.AMOUNT.IN.FUND` | `FsGaSwapDetail_CashFlowAmountInFund` | TField |  | Cash Flow Amount In Fund Multifonds DB Column is MNT_CASH_FLOW_PTF. |
| 103 | `FS.GA.SWAP.DETAIL.TOTAL.PROFIT.LOSS.BID.IN.FUND` | `FsGaSwapDetail_TotalProfitLossBidInFund` | TField |  | Total Profit Loss BID In Fund Multifonds DB Column is GAIN_PERTE_BID. |
| 104 | `FS.GA.SWAP.DETAIL.TOTAL.PROFIT.LOSS.OFFER.FUND` | `FsGaSwapDetail_TotalProfitLossOfferFund` | TField |  | Total Profit Loss Offer Fund Multifonds DB Column is GAIN_PERTE_OFFER. |
| 105 | `FS.GA.SWAP.DETAIL.GAIN.LOSS.AT.SECURITY.CURRENCY` | `FsGaSwapDetail_GainLossAtSecurityCurrency` | TField |  | Gain Loss At Security Currency Multifonds DB Column is GAIN_PERTE_BV. |
| 106 | `FS.GA.SWAP.DETAIL.BV.NAV.PRICE.TYPE` | `FsGaSwapDetail_BvNavPriceType` | TField |  | The price to be used in Back value NAV like Mid, Bid of Offer price Multifonds DB Column is BV_PRICE_TYPE. |
| 107 | `FS.GA.SWAP.DETAIL.UNREALIZED` | `FsGaSwapDetail_Unrealized` | TField |  | Unrealized Multifonds DB Column is GAIN_PERTE. |
| 108 | `FS.GA.SWAP.DETAIL.FLAG.CDS` | `FsGaSwapDetail_FlagCds` | TField |  | Flag to activate CDS index Multifonds DB Column is FLG_CDS_INDEX. |
| 109 | `FS.GA.SWAP.DETAIL.ACCRUED.INTEREST.FUND` | `FsGaSwapDetail_AccruedInterestFund` | TField |  | Accrued Interest for Swaps Fund leg Multifonds DB Column is MINT_DEFFERAL_FUND_LEG. |
| 110 | `FS.GA.SWAP.DETAIL.FLAG.FOR.PERFORMANCE.SWAP` | `FsGaSwapDetail_FlagForPerformanceSwap` | TField |  | Flag to activate performance swap features Multifonds DB Column is FLG_PERFORM_SWAP. |
| 111 | `FS.GA.SWAP.DETAIL.CHECK.DATE` | `FsGaSwapDetail_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 112 | `FS.GA.SWAP.DETAIL.CHECKED.BY` | `FsGaSwapDetail_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 113 | `FS.GA.SWAP.DETAIL.IFRS.TAG` | `FsGaSwapDetail_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 114 | `FS.GA.SWAP.DETAIL.OPENING.NOMINAL.AMOUNT.INT` | `FsGaSwapDetail_OpeningNominalAmountInt` | TField |  | Opening Nominal Amount INT Multifonds DB Column is MNT_CAP_INT_DEAL. |
| 115 | `FS.GA.SWAP.DETAIL.OPENING.NOMINAL.AMOUNT.COR` | `FsGaSwapDetail_OpeningNominalAmountCor` | TField |  | Opening Nominal Amount COR Multifonds DB Column is MNT_CAP_COR_DEAL. |
| 116 | `FS.GA.SWAP.DETAIL.UTI.DESCRIPTION` | `FsGaSwapDetail_UtiDescription` | TField |  | UTI Description Multifonds DB Column is UTI_DESC. |
| 117 | `FS.GA.SWAP.DETAIL.USI.DESCRIPTION` | `FsGaSwapDetail_UsiDescription` | TField |  | USI Description Multifonds DB Column is USI_DESC. |
| 118 | `FS.GA.SWAP.DETAIL.CONFIRMATION.DATE` | `FsGaSwapDetail_ConfirmationDate` | TField |  | Confirmation Date Multifonds DB Column is CONFIRM_DATE. |
| 119 | `FS.GA.SWAP.DETAIL.CONFIRMED` | `FsGaSwapDetail_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 120 | `FS.GA.SWAP.DETAIL.FUND.SETTLEMENT.VCI` | `FsGaSwapDetail_FundSettlementVci` | TField |  | Fund Settlement Vci Multifonds DB Column is SETTL_PTF_VCI. |
| 121 | `FS.GA.SWAP.DETAIL.EXCH.RATE.SETTLEMENT.TO.DEAL` | `FsGaSwapDetail_ExchRateSettlementToDeal` | TField |  | The exchange rate between the settlement and deal currency Multifonds DB Column is TCHG_PTF. |
| 122 | `FS.GA.SWAP.DETAIL.REPAY.LOCAL.SETTLED.VCI` | `FsGaSwapDetail_RepayLocalSettledVci` | TField |  | Repay Local Settled VCI Multifonds DB Column is REPAY_LOC_SETT_VCI. |
| 123 | `FS.GA.SWAP.DETAIL.REPAY.FUND.SETTLED.VCI` | `FsGaSwapDetail_RepayFundSettledVci` | TField |  | Repay Fund Settled VCI Multifonds DB Column is REPAY_SETTL_PTF_VCI. |
| 124 | `FS.GA.SWAP.DETAIL.REPAY.LOCAL.FUND.VCI` | `FsGaSwapDetail_RepayLocalFundVci` | TField |  | Repay Local Fund VCI Multifonds DB Column is REPAY_LOC_PTF_VCI. |
| 125 | `FS.GA.SWAP.DETAIL.EXCHANGE.RATE.REPAY.FUND` | `FsGaSwapDetail_ExchangeRateRepayFund` | TField |  | Exchange Rate Repay Fund Multifonds DB Column is REPAY_TCHG_PTF. |
| 126 | `FS.GA.SWAP.DETAIL.REPAY.ACCOUNT.NUMBER` | `FsGaSwapDetail_RepayAccountNumber` | TField |  | Repay Account Number Multifonds DB Column is REPAY_NRUBR. |
| 127 | `FS.GA.SWAP.DETAIL.REPAY.OPERATOR.CODE` | `FsGaSwapDetail_RepayOperatorCode` | TField |  | Repay Operator Code Multifonds DB Column is REPAY_COPER. |
| 128 | `FS.GA.SWAP.DETAIL.ACCOUNTING.METHOD` | `FsGaSwapDetail_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 129 | `FS.GA.SWAP.DETAIL.PREVIOUS.STATUS.CODE` | `FsGaSwapDetail_PreviousStatusCode` | TField |  | Previous Status Code Multifonds DB Column is PREV_CSTATUS. |
| 130 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.SUFFIX.354.DB` | `FsGaSwapDetail_PaymentAmountSuffix354Db` | TField |  | Payment Amount Suffix 354 DB Multifonds DB Column is GLACCSUFF_354_DB. |
| 131 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.SUFFIX.354.CR` | `FsGaSwapDetail_PaymentAmountSuffix354Cr` | TField |  | Payment Amount Suffix 354 CR Multifonds DB Column is GLACCSUFF_354_CR. |
| 132 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.SUFFIX.355.DB` | `FsGaSwapDetail_PaymentAmountSuffix355Db` | TField |  | Payment Amount Suffix 355 DB Multifonds DB Column is GLACCSUFF_355_DB. |
| 133 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.SUFFIX.355.CR` | `FsGaSwapDetail_PaymentAmountSuffix355Cr` | TField |  | Payment Amount Suffix 355 CR Multifonds DB Column is GLACCSUFF_355_CR. |
| 134 | `FS.GA.SWAP.DETAIL.SECURITY.FOREX.VCI.SETTLEMENT` | `FsGaSwapDetail_SecurityForexVciSettlement` | TField |  | Security Forex VCI Settlement Multifonds DB Column is SEC_SETTL_FX_VCI. |
| 135 | `FS.GA.SWAP.DETAIL.FUND.FOREX.VCI.SECURITY` | `FsGaSwapDetail_FundForexVciSecurity` | TField |  | Fund Forex VCI Security Multifonds DB Column is SEC_PTF_FX_VCI. |
| 136 | `FS.GA.SWAP.DETAIL.FUND.FX.SETTLEMENT.VCI` | `FsGaSwapDetail_FundFxSettlementVci` | TField |  | Settl Ptf Fx Vci Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 137 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.354.DB` | `FsGaSwapDetail_PaymentAmount354Db` | TField |  | Payment Amount 354 DB Multifonds DB Column is GLACCOUNT_354_DB. |
| 138 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.354.CR` | `FsGaSwapDetail_PaymentAmount354Cr` | TField |  | Payment Amount 354 CR Multifonds DB Column is GLACCOUNT_354_CR. |
| 139 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.355.DB` | `FsGaSwapDetail_PaymentAmount355Db` | TField |  | Payment Amount 355 DB Multifonds DB Column is GLACCOUNT_355_DB. |
| 140 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.355.CR` | `FsGaSwapDetail_PaymentAmount355Cr` | TField |  | Payment Amount 355 CR Multifonds DB Column is GLACCOUNT_355_CR. |
| 141 | `FS.GA.SWAP.DETAIL.OPERATION.CODE.354` | `FsGaSwapDetail_OperationCode354` | TField |  | Operation Code 354 Multifonds DB Column is OPCODE_354. |
| 142 | `FS.GA.SWAP.DETAIL.OPERATION.CODE.355` | `FsGaSwapDetail_OperationCode355` | TField |  | Operation Code 355 Multifonds DB Column is OPCODE_355. |
| 143 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.IR9.DB` | `FsGaSwapDetail_PaymentAmountIr9Db` | TField |  | Payment Amount IR9 DB Multifonds DB Column is GLACCOUNT_IR9_DB. |
| 144 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.IR9.CR` | `FsGaSwapDetail_PaymentAmountIr9Cr` | TField |  | Payment Amount IR9 CR Multifonds DB Column is GLACCOUNT_IR9_CR. |
| 145 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.SUFFIX.IR9.DB` | `FsGaSwapDetail_PaymentAmountSuffixIr9Db` | TField |  | Payment Amount Suffix IR9 DB Multifonds DB Column is GLACCSUFF_IR9_DB. |
| 146 | `FS.GA.SWAP.DETAIL.PAYMENT.AMOUNT.SUFFIX.IR9.CR` | `FsGaSwapDetail_PaymentAmountSuffixIr9Cr` | TField |  | Payment Amount Suffix IR9 CR Multifonds DB Column is GLACCSUFF_IR9_CR. |
| 147 | `FS.GA.SWAP.DETAIL.FATCA.LIABILITY.FLAG.IRS` | `FsGaSwapDetail_FatcaLiabilityFlagIrs` | TField |  | Defined as 'Y' is FATCA withholding tax occurs and 'N' if FATCA is not applicable. Multifonds DB Column is FLG_FATCA_IRS. |
| 148 | `FS.GA.SWAP.DETAIL.FATCA.LIABILITY.PERCENTAGE.IRS` | `FsGaSwapDetail_FatcaLiabilityPercentageIrs` | TField |  | Required for calculation of FATCA tax and represent the percentage of the US source income of the IRS. If FATCA Liability defined as Y, this field can be 0 to 100% while if N, then defaulted to 0%. Multifonds DB Column is PCT_FATCA_IRS. |
| 149 | `FS.GA.SWAP.DETAIL.CURRENCY.INT.TO.COR.VCI` | `FsGaSwapDetail_CurrencyIntToCorVci` | TField |  | Currency INT To COR VCI Multifonds DB Column is CMON_INT_TO_CMON_COR_VCI. |
| 150 | `FS.GA.SWAP.DETAIL.CURRENCY.INT.TO.UPFRONT.VCI` | `FsGaSwapDetail_CurrencyIntToUpfrontVci` | TField |  | Currency INT To Upfront VCI Multifonds DB Column is CMON_INT_TO_CMON_UPFRONT_VCI. |
| 151 | `FS.GA.SWAP.DETAIL.CURRENCY.INT.TO.FUND.CCY.VCI` | `FsGaSwapDetail_CurrencyIntToFundCcyVci` | TField |  | Currency INT To Fund Ccy VCI Multifonds DB Column is CMON_INT_TO_FUND_CCY_VCI. |
| 152 | `FS.GA.SWAP.DETAIL.CURRENCY.COR.TO.UPFRONT.VCI` | `FsGaSwapDetail_CurrencyCorToUpfrontVci` | TField |  | Currency COR To Upfront VCI Multifonds DB Column is CMON_COR_TO_CMON_UPFRONT_VCI. |
| 153 | `FS.GA.SWAP.DETAIL.CURRENCY.COR.TO.FUND.CCY.VCI` | `FsGaSwapDetail_CurrencyCorToFundCcyVci` | TField |  | Currency COR TO Fund Ccy VCI Multifonds DB Column is CMON_COR_TO_FUND_CCY_VCI. |
| 154 | `FS.GA.SWAP.DETAIL.CCY.UPFRONT.TO.FUND.CCY.VCI` | `FsGaSwapDetail_CcyUpfrontToFundCcyVci` | TField |  | CCy Upfront To Fund Ccy VCI Multifonds DB Column is CMON_UPFRONT_TO_FUND_CCY_VCI. |
| 155 | `FS.GA.SWAP.DETAIL.ACRUED.INTEREST.DEFFERAL.COR` | `FsGaSwapDetail_AcruedInterestDefferalCor` | TField |  | Acrued Interest Defferal COR Multifonds DB Column is MINT_DEFFERAL_COR. |
| 156 | `FS.GA.SWAP.DETAIL.ACRUED.INTEREST.DEFFERAL.FUND` | `FsGaSwapDetail_AcruedInterestDefferalFund` | TField |  | Acrued Interest Defferal Fund Multifonds DB Column is MINT_DEFFERAL_FUND. |
| 157 | `FS.GA.SWAP.DETAIL.IFRS.CATEGORY` | `FsGaSwapDetail_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 158 | `FS.GA.SWAP.DETAIL.CENTRAL.COUNTERPARTY.CLEARING` | `FsGaSwapDetail_CentralCounterpartyClearing` | TField |  | To reduce credit risk that prevailed bet. 2 counterparties in OTC mkt, multilateral relationships are centralized involving CCPs. 'CCP' is to define diff agents at stake (clearing and exec broker, CCP). Multifonds DB Column is CCP. |
| 159 | `FS.GA.SWAP.DETAIL.NEW.VALUATION.OF.SWAP.IN.NAV` | `FsGaSwapDetail_NewValuationOfSwapInNav` | TField |  | New Valuation Of Swap In Nav Multifonds DB Column is FLG_PRICING_LEG_NEW_VAL. |
| 160 | `FS.GA.SWAP.DETAIL.PRICE.INDICATOR` | `FsGaSwapDetail_PriceIndicator` | TField |  | Price indicator to denote if the price of the bond is dirty or clean Multifonds DB Column is TYP_INT_COURS. |
| 161 | `FS.GA.SWAP.DETAIL.COUNTERPARTY.SECURITY` | `FsGaSwapDetail_CounterpartySecurity` | TField |  | Counterparty Security Multifonds DB Column is NOVAL_RECEIVE. |
| 162 | `FS.GA.SWAP.DETAIL.FUND.SECURITY` | `FsGaSwapDetail_FundSecurity` | TField |  | Fund Security Multifonds DB Column is NOVAL_PAY. |
| 163 | `FS.GA.SWAP.DETAIL.ACCRUAL.CONVENTION.RECEIVE` | `FsGaSwapDetail_AccrualConventionReceive` | TField |  | Accrual Convention Receive Multifonds DB Column is ACCRUAL_CONV_RECEIVE. |
| 164 | `FS.GA.SWAP.DETAIL.FUND.ACCRUAL.CONVENTION` | `FsGaSwapDetail_FundAccrualConvention` | TField |  | Fund Accrual Convention Multifonds DB Column is ACCRUAL_CONV_PAY. |
| 165 | `FS.GA.SWAP.DETAIL.SECURITY.COMP.FREQUENCY` | `FsGaSwapDetail_SecurityCompFrequency` | TField |  | Security Comp Frequency Multifonds DB Column is CFREQCOMP_RECEIVE. |
| 166 | `FS.GA.SWAP.DETAIL.FUND.SECURITY.COMP.FREQUENCY` | `FsGaSwapDetail_FundSecurityCompFrequency` | TField |  | Fund Security Comp Frequency Multifonds DB Column is CFREQCOMP_PAY. |
| 167 | `FS.GA.SWAP.DETAIL.FLAG.PERCENTAGE.SPREAD.REC` | `FsGaSwapDetail_FlagPercentageSpreadRec` | TField |  | Flag Percentage Spread Rec Multifonds DB Column is FLG_SPRD_PCT_REC. |
| 168 | `FS.GA.SWAP.DETAIL.FLAG.PERCENTAGE.SPREAD.PAY` | `FsGaSwapDetail_FlagPercentageSpreadPay` | TField |  | Flag Percentage Spread Pay Multifonds DB Column is FLG_SPRD_PCT_PAY. |
| 169 | `FS.GA.SWAP.DETAIL.FACTOR.REC` | `FsGaSwapDetail_FactorRec` | TField |  | Factor Rec Multifonds DB Column is FACTOR_REC. |
| 170 | `FS.GA.SWAP.DETAIL.FACTOR.PAY` | `FsGaSwapDetail_FactorPay` | TField |  | Factor Pay Multifonds DB Column is FACTOR_PAY. |
| 171 | `FS.GA.SWAP.DETAIL.MODIFIED.MAURITY.DATE` | `FsGaSwapDetail_ModifiedMaurityDate` | TField |  | Modified Maurity Date Multifonds DB Column is MFBD_DECH. |
| 172 | `FS.GA.SWAP.DETAIL.RESERVED10` | `FsGaSwapDetail_Reserved10` | TField |  |  |
| 173 | `FS.GA.SWAP.DETAIL.RESERVED9` | `FsGaSwapDetail_Reserved9` | TField |  |  |
| 174 | `FS.GA.SWAP.DETAIL.RESERVED8` | `FsGaSwapDetail_Reserved8` | TField |  |  |
| 175 | `FS.GA.SWAP.DETAIL.RESERVED7` | `FsGaSwapDetail_Reserved7` | TField |  |  |
| 176 | `FS.GA.SWAP.DETAIL.RESERVED6` | `FsGaSwapDetail_Reserved6` | TField |  |  |
| 177 | `FS.GA.SWAP.DETAIL.RESERVED5` | `FsGaSwapDetail_Reserved5` | TField |  |  |
| 178 | `FS.GA.SWAP.DETAIL.RESERVED4` | `FsGaSwapDetail_Reserved4` | TField |  |  |
| 179 | `FS.GA.SWAP.DETAIL.RESERVED3` | `FsGaSwapDetail_Reserved3` | TField |  |  |
| 180 | `FS.GA.SWAP.DETAIL.RESERVED2` | `FsGaSwapDetail_Reserved2` | TField |  |  |
| 181 | `FS.GA.SWAP.DETAIL.RESERVED1` | `FsGaSwapDetail_Reserved1` | TField |  |  |
| 182 | `FS.GA.SWAP.DETAIL.LOCAL.REF` | `FsGaSwapDetail_LocalRef` |  |  |  |
| 183 | `FS.GA.SWAP.DETAIL.OVERRIDE` | `FsGaSwapDetail_Override` |  |  |  |
| 184 | `FS.GA.SWAP.DETAIL.RECORD.STATUS` | `FsGaSwapDetail_RecordStatus` | String |  |  |
| 185 | `FS.GA.SWAP.DETAIL.CURR.NO` | `FsGaSwapDetail_CurrNo` | String |  |  |
| 186 | `FS.GA.SWAP.DETAIL.INPUTTER` | `FsGaSwapDetail_Inputter` |  |  |  |
| 187 | `FS.GA.SWAP.DETAIL.DATE.TIME` | `FsGaSwapDetail_DateTime` |  |  |  |
| 188 | `FS.GA.SWAP.DETAIL.AUTHORISER` | `FsGaSwapDetail_Authoriser` | String |  |  |
| 189 | `FS.GA.SWAP.DETAIL.CO.CODE` | `FsGaSwapDetail_CoCode` | String |  |  |
| 190 | `FS.GA.SWAP.DETAIL.DEPT.CODE` | `FsGaSwapDetail_DeptCode` | String |  |  |
| 191 | `FS.GA.SWAP.DETAIL.AUDITOR.CODE` | `FsGaSwapDetail_AuditorCode` | String |  |  |
| 192 | `FS.GA.SWAP.DETAIL.AUDIT.DATE.TIME` | `FsGaSwapDetail_AuditDateTime` | String |  |  |
