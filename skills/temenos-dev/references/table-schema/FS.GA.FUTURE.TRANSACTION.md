# FS.GA.FUTURE.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUTURE.TRANSACTION` in `FS_FutureTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUTURE.TRANSACTION.PARENT.REF.ID` | `FsGaFutureTransaction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUTURE.TRANSACTION.ORA.ROWID` | `FsGaFutureTransaction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUTURE.TRANSACTION.FUND.ID` | `FsGaFutureTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FUTURE.TRANSACTION.TRANSACTION.NUMBER` | `FsGaFutureTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.FUTURE.TRANSACTION.FUTURE.ID.CODE` | `FsGaFutureTransaction_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 6 | `FS.GA.FUTURE.TRANSACTION.LOT.NUMBER` | `FsGaFutureTransaction_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 7 | `FS.GA.FUTURE.TRANSACTION.FUTURE.OPTION.TRANSACTION.TYPE` | `FsGaFutureTransaction_FutureOptionTransactionType` | TField |  | Represents Opening/Continuing/Closing transaction types for Futures &amp; Options Multifonds DB Column is TYP_TRAIT. |
| 8 | `FS.GA.FUTURE.TRANSACTION.OPERATION.CODE` | `FsGaFutureTransaction_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 9 | `FS.GA.FUTURE.TRANSACTION.DEAL.STATUS.CODE` | `FsGaFutureTransaction_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 10 | `FS.GA.FUTURE.TRANSACTION.QUANTITY` | `FsGaFutureTransaction_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 11 | `FS.GA.FUTURE.TRANSACTION.INITIAL.MARGIN` | `FsGaFutureTransaction_InitialMargin` | TField |  | MultiFonds is able to compute the initial margin to be deposited with each opening or closing transaction. Enter the initial margin to be deposited per contract. Multifonds DB Column is MARG_INIT. |
| 12 | `FS.GA.FUTURE.TRANSACTION.TRANSAC.PRICE` | `FsGaFutureTransaction_TransacPrice` | TField |  | This field corresponds to the price of the transaction. Enter the price in quotation currency of the New CFN contract (unless the future is quoted in percent). Multifonds DB Column is PRICE. |
| 13 | `FS.GA.FUTURE.TRANSACTION.ENGAGEMENT.AMOUNT` | `FsGaFutureTransaction_EngagementAmount` | TField |  | This field displays calculated amount as being the quantity * the contract size * the price. Multifonds DB Column is MNT_ENGAG. |
| 14 | `FS.GA.FUTURE.TRANSACTION.FEES.AMOUNT` | `FsGaFutureTransaction_FeesAmount` | TField |  | Transaction Fees Amount Multifonds DB Column is MNT_FEES. |
| 15 | `FS.GA.FUTURE.TRANSACTION.NET.MNT` | `FsGaFutureTransaction_NetMnt` | TField |  | Net Mnt Multifonds DB Column is MNT_NET. |
| 16 | `FS.GA.FUTURE.TRANSACTION.CORRESPONDENT` | `FsGaFutureTransaction_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 17 | `FS.GA.FUTURE.TRANSACTION.GL.SETTLEMENT.ACCOUNT` | `FsGaFutureTransaction_GlSettlementAccount` | TField |  | GL Settlement Account Number Multifonds DB Column is NRUBR_CORR. |
| 18 | `FS.GA.FUTURE.TRANSACTION.CORRESPONDENT.CASH.SUFFIX.NUM` | `FsGaFutureTransaction_CorrespondentCashSuffixNum` | TField |  | Correspondent Cash Suffix Number Multifonds DB Column is NSUFF_CORR. |
| 19 | `FS.GA.FUTURE.TRANSACTION.SETTLEMENT.CURRENCY` | `FsGaFutureTransaction_SettlementCurrency` | TField |  | Currency in which the settlement would be processed. Multifonds DB Column is CMON_CORR. |
| 20 | `FS.GA.FUTURE.TRANSACTION.EXCHANGE.RATE` | `FsGaFutureTransaction_ExchangeRate` | TField |  | Exchange rate between deal currency and settlement currency Multifonds DB Column is TCHG_CORR. |
| 21 | `FS.GA.FUTURE.TRANSACTION.FEES.AMOUNT.IN.SETTLEMENT.CCY` | `FsGaFutureTransaction_FeesAmountInSettlementCcy` | TField |  | Fees Amount In Settlement Ccy Multifonds DB Column is MNT_FEES_CORR. |
| 22 | `FS.GA.FUTURE.TRANSACTION.SETTLE.DATE` | `FsGaFutureTransaction_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 23 | `FS.GA.FUTURE.TRANSACTION.TRADE.DATE.OF.CONTRACT` | `FsGaFutureTransaction_TradeDateOfContract` | TField |  | Trade Date or Accounting Date for Contractual Instrument Multifonds DB Column is DATACC. |
| 24 | `FS.GA.FUTURE.TRANSACTION.TRADE.DATE` | `FsGaFutureTransaction_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 25 | `FS.GA.FUTURE.TRANSACTION.DESCRIPTION` | `FsGaFutureTransaction_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 26 | `FS.GA.FUTURE.TRANSACTION.ENTRY.NUMBER.REPAYMENT` | `FsGaFutureTransaction_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 27 | `FS.GA.FUTURE.TRANSACTION.ARCHIVE` | `FsGaFutureTransaction_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 28 | `FS.GA.FUTURE.TRANSACTION.HEDGING.OR.TRADING.CATEGORY` | `FsGaFutureTransaction_HedgingOrTradingCategory` | TField |  | Hedging or Trading Category Multifonds DB Column is CD_HEDG. |
| 29 | `FS.GA.FUTURE.TRANSACTION.MANAGER.CODE` | `FsGaFutureTransaction_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 30 | `FS.GA.FUTURE.TRANSACTION.AUTOMATIC.HIFO` | `FsGaFutureTransaction_AutomaticHifo` | TField |  | Automatic HIFO Multifonds DB Column is AUTO_HIFO. |
| 31 | `FS.GA.FUTURE.TRANSACTION.BROKER.ID` | `FsGaFutureTransaction_BrokerId` | TField |  | Enter the broker number Multifonds DB Column is NCORR_VAR_MARG. |
| 32 | `FS.GA.FUTURE.TRANSACTION.VM.ACCOUNT` | `FsGaFutureTransaction_VmAccount` | TField |  | This is the default account used to book the variation margin on Futures Multifonds DB Column is NRUBR_VAR_MARG. |
| 33 | `FS.GA.FUTURE.TRANSACTION.VARIATION.MARGIN.SUFFIX.NUMBER` | `FsGaFutureTransaction_VariationMarginSuffixNumber` | TField |  | To enter variation margin suffix number. Multifonds DB Column is NSUFF_VAR_MARG. |
| 34 | `FS.GA.FUTURE.TRANSACTION.CASH.ACCOUNT.NUMBER` | `FsGaFutureTransaction_CashAccountNumber` | TField |  | This field displays the cash account that has been attached to the counterparty in the central register file. The user may change the account. Do not use transitory accounts. Only use bank accounts Multifonds DB Column is NRUBR_BROKER. |
| 35 | `FS.GA.FUTURE.TRANSACTION.CASH.ACCOUNT.SUFFIX` | `FsGaFutureTransaction_CashAccountSuffix` | TField |  | Cash Account Suffix. Multifonds DB Column is NSUFF_BROKER. |
| 36 | `FS.GA.FUTURE.TRANSACTION.STATUS.PENDING` | `FsGaFutureTransaction_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 37 | `FS.GA.FUTURE.TRANSACTION.COUNTERPARTY.CORRESPONDENT` | `FsGaFutureTransaction_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 38 | `FS.GA.FUTURE.TRANSACTION.MARGIN.ACCOUNT.NUMBER` | `FsGaFutureTransaction_MarginAccountNumber` | TField |  | Future margin account number Multifonds DB Column is NRUBR_MARG. |
| 39 | `FS.GA.FUTURE.TRANSACTION.MARGIN.SUFFIX.NUMBER` | `FsGaFutureTransaction_MarginSuffixNumber` | TField |  | Future margin account suffix number Multifonds DB Column is NSUFF_MARG. |
| 40 | `FS.GA.FUTURE.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaFutureTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 41 | `FS.GA.FUTURE.TRANSACTION.INTEREST.RATE.TYPE` | `FsGaFutureTransaction_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 42 | `FS.GA.FUTURE.TRANSACTION.SPREAD.PERCENT` | `FsGaFutureTransaction_SpreadPercent` | TField |  | Spread rate to be applied on commission rate for commission calculation Multifonds DB Column is PCT_SPREAD. |
| 43 | `FS.GA.FUTURE.TRANSACTION.INCOME.TYPE` | `FsGaFutureTransaction_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 44 | `FS.GA.FUTURE.TRANSACTION.INITIAL.MARGIN.AMOUNT` | `FsGaFutureTransaction_InitialMarginAmount` | TField |  | Initial margin amount of future Multifonds DB Column is MNT_MARG. |
| 45 | `FS.GA.FUTURE.TRANSACTION.ACCOUNTING.DATE` | `FsGaFutureTransaction_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 46 | `FS.GA.FUTURE.TRANSACTION.BASKET.REFERENCE` | `FsGaFutureTransaction_BasketReference` | TField |  | The basket reference is a control of uniqueness done on the fund ID, the currency, the counterpart and the maturity date Multifonds DB Column is BASKET_REF. |
| 47 | `FS.GA.FUTURE.TRANSACTION.ACCRUED.INTEREST` | `FsGaFutureTransaction_AccruedInterest` | TField |  | Accrued interest of the security Multifonds DB Column is MINT. |
| 48 | `FS.GA.FUTURE.TRANSACTION.MATURITY.CODE` | `FsGaFutureTransaction_MaturityCode` | TField |  | Maturity code of the floating interest rate that needs to be applied for commission accrual on a lending/borrowing transaction Multifonds DB Column is CODE_MOIS. |
| 49 | `FS.GA.FUTURE.TRANSACTION.INT.RATE` | `FsGaFutureTransaction_IntRate` | TField |  | Interest Rate Multifonds DB Column is TAUX. |
| 50 | `FS.GA.FUTURE.TRANSACTION.DAY.COUNT.CONVENTION` | `FsGaFutureTransaction_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 51 | `FS.GA.FUTURE.TRANSACTION.REVISION.CODE` | `FsGaFutureTransaction_RevisionCode` | TField |  | Defined the calculation method for the rate defined in Int rate type&quot; and &quot;maturity&quot;&quot; Multifonds DB Column is REVISION_CODE. |
| 52 | `FS.GA.FUTURE.TRANSACTION.FREQUENCY` | `FsGaFutureTransaction_Frequency` | TField |  | Frequency code for processing Multifonds DB Column is CFREQ. |
| 53 | `FS.GA.FUTURE.TRANSACTION.PAYMENT.DAY` | `FsGaFutureTransaction_PaymentDay` | TField |  | Payment Day Multifonds DB Column is DFREQ. |
| 54 | `FS.GA.FUTURE.TRANSACTION.DELAY.DAYS` | `FsGaFutureTransaction_DelayDays` | TField |  | Delay days to be applied on coupon/ paydown transactions to trigger payment Multifonds DB Column is DELAY_DAYS. |
| 55 | `FS.GA.FUTURE.TRANSACTION.CALCULATION.PAYMENT.DATE` | `FsGaFutureTransaction_CalculationPaymentDate` | TField |  | Logic to decide if payment date falls on a non working day should it process paymet on same date or prior/next working day. Multifonds DB Column is CTR_DATE. |
| 56 | `FS.GA.FUTURE.TRANSACTION.COEFFICIENT.CORPORATE.ACTION` | `FsGaFutureTransaction_CoefficientCorporateAction` | TField |  | Enter a CA coefficient which is taken into account to calc the dividend, coupon, split, reverse split, spin off, exchange of security into one new security ID or several security ID on the sec lent. Multifonds DB Column is COEF_CORP. |
| 57 | `FS.GA.FUTURE.TRANSACTION.CURRENCY.OF.INTEREST` | `FsGaFutureTransaction_CurrencyOfInterest` | TField |  | Currency of Interest Multifonds DB Column is CMON_TAUX. |
| 58 | `FS.GA.FUTURE.TRANSACTION.REVISED.INTEREST.RATE` | `FsGaFutureTransaction_RevisedInterestRate` | TField |  | Revised Interest Rate Multifonds DB Column is TAUX_RATE. |
| 59 | `FS.GA.FUTURE.TRANSACTION.MATURITY.DATE.OF.CONTRACT` | `FsGaFutureTransaction_MaturityDateOfContract` | TField |  | Maturity Date of the Contract/Instrument Multifonds DB Column is DECH. |
| 60 | `FS.GA.FUTURE.TRANSACTION.ENGAG.AMOUNT.CLOSE` | `FsGaFutureTransaction_EngagAmountClose` | TField |  | ENGAG Amount Close Multifonds DB Column is MNT_ENGAG_CLOSE. |
| 61 | `FS.GA.FUTURE.TRANSACTION.GL.ACCOUNT.OF.CONTRACT` | `FsGaFutureTransaction_GlAccountOfContract` | TField |  | Account Number for Contractual Instruments ex. FRAs Multifonds DB Column is NRUBR_INT. |
| 62 | `FS.GA.FUTURE.TRANSACTION.GL.ACCOUNT.SUFFIX.OF.CONTRACT` | `FsGaFutureTransaction_GlAccountSuffixOfContract` | TField |  | Account Number Suffix for Contractual Instruments ex. FRAs Multifonds DB Column is NSUFF_INT. |
| 63 | `FS.GA.FUTURE.TRANSACTION.MANUAL.LOT.SELECTION` | `FsGaFutureTransaction_ManualLotSelection` | TField |  | Flag to denote that the lots relieved have been manually selected Multifonds DB Column is FLG_MANUAL_LOT. |
| 64 | `FS.GA.FUTURE.TRANSACTION.MODULE.IDENTIFIER` | `FsGaFutureTransaction_ModuleIdentifier` | TField |  | Module Multifonds DB Column is FLG_MODULE. |
| 65 | `FS.GA.FUTURE.TRANSACTION.EXECUTION.TIMESTAMP` | `FsGaFutureTransaction_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 66 | `FS.GA.FUTURE.TRANSACTION.FUND.STRATEGY` | `FsGaFutureTransaction_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 67 | `FS.GA.FUTURE.TRANSACTION.FUND.LINK.ID` | `FsGaFutureTransaction_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 68 | `FS.GA.FUTURE.TRANSACTION.NET.SETTLEMENT.AMOUNT` | `FsGaFutureTransaction_NetSettlementAmount` | TField |  | Net settlement amount on a transaction Multifonds DB Column is MONTNET_CPT. |
| 69 | `FS.GA.FUTURE.TRANSACTION.RATE.OF.EXCHANGE` | `FsGaFutureTransaction_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 70 | `FS.GA.FUTURE.TRANSACTION.NET.AMOUNT.OPER` | `FsGaFutureTransaction_NetAmountOper` | TField |  | Net Amount. Multifonds DB Column is MNT_NET_OPER. |
| 71 | `FS.GA.FUTURE.TRANSACTION.FUND.MARGIN.AMOUNT` | `FsGaFutureTransaction_FundMarginAmount` | TField |  | Fund Margin Amount Multifonds DB Column is MNT_MARG_PTF. |
| 72 | `FS.GA.FUTURE.TRANSACTION.REBALANCE.ADJUSTED` | `FsGaFutureTransaction_RebalanceAdjusted` | TField |  | Rebalance Adjusted Multifonds DB Column is REBAL_ADJ. |
| 73 | `FS.GA.FUTURE.TRANSACTION.INTEREST.RATE.OLD` | `FsGaFutureTransaction_InterestRateOld` | TField |  | TAUX Rate Old Multifonds DB Column is TAUX_RATE_OLD. |
| 74 | `FS.GA.FUTURE.TRANSACTION.SHARE.CLASS.CODE` | `FsGaFutureTransaction_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 75 | `FS.GA.FUTURE.TRANSACTION.INTEREST.BEGIN.DATE` | `FsGaFutureTransaction_InterestBeginDate` | TField |  | Start date to calculate interest for CFD Multifonds DB Column is DINT_START. |
| 76 | `FS.GA.FUTURE.TRANSACTION.LENDING.FEE` | `FsGaFutureTransaction_LendingFee` | TField |  | Lending fees for CFD instruments Multifonds DB Column is PCT_LEND_FEE. |
| 77 | `FS.GA.FUTURE.TRANSACTION.CHECK.DATE` | `FsGaFutureTransaction_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 78 | `FS.GA.FUTURE.TRANSACTION.CHECKED.BY` | `FsGaFutureTransaction_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 79 | `FS.GA.FUTURE.TRANSACTION.IFRS.TAG` | `FsGaFutureTransaction_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 80 | `FS.GA.FUTURE.TRANSACTION.RESET.PERFORMANCE` | `FsGaFutureTransaction_ResetPerformance` | TField |  | reset performance in FDCFD03 Multifonds DB Column is RESET_PERFORMANCE. |
| 81 | `FS.GA.FUTURE.TRANSACTION.RESET.FREQUENCY` | `FsGaFutureTransaction_ResetFrequency` | TField |  | This field corresponds to the frequency of the reset like monthly, weekly, at maturity etc., Multifonds DB Column is RESET_CFREQ. |
| 82 | `FS.GA.FUTURE.TRANSACTION.RESET.PAYMENT.DAY` | `FsGaFutureTransaction_ResetPaymentDay` | TField |  | This field correspond to the date for reset frequency Multifonds DB Column is RESET_DFREQ. |
| 83 | `FS.GA.FUTURE.TRANSACTION.CALC.PAYMENT.DATE.RESET` | `FsGaFutureTransaction_CalcPaymentDateReset` | TField |  | Reset calc. payment date Multifonds DB Column is RESET_CTR_DATE. |
| 84 | `FS.GA.FUTURE.TRANSACTION.PRICE.DELAY.DAYS` | `FsGaFutureTransaction_PriceDelayDays` | TField |  | Field to enter price delay days Multifonds DB Column is RESET_DELAY_DAYS. |
| 85 | `FS.GA.FUTURE.TRANSACTION.SUB.TYPE.CFD` | `FsGaFutureTransaction_SubTypeCfd` | TField |  | Define to Supports more than to 99 contracts per CFD without changing the maturity date of the contract Multifonds DB Column is SUB_TYPE_CFD. |
| 86 | `FS.GA.FUTURE.TRANSACTION.DATE.RESET` | `FsGaFutureTransaction_DateReset` | TField |  | Date Reset Multifonds DB Column is DRESET. |
| 87 | `FS.GA.FUTURE.TRANSACTION.CONFIRMATION.DATE` | `FsGaFutureTransaction_ConfirmationDate` | TField |  | Confirmation Date Multifonds DB Column is CONFIRM_DATE. |
| 88 | `FS.GA.FUTURE.TRANSACTION.EXTERNAL.CONTRACT.NUMBER` | `FsGaFutureTransaction_ExternalContractNumber` | TField |  | External Contract Number Multifonds DB Column is NCONTRAT_EXT. |
| 89 | `FS.GA.FUTURE.TRANSACTION.INTERNAL.SECURITY.ID` | `FsGaFutureTransaction_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 90 | `FS.GA.FUTURE.TRANSACTION.UNDERLYING.SECURITY.QUANTITY` | `FsGaFutureTransaction_UnderlyingSecurityQuantity` | TField |  | Underlying Security&apos;s Quantity for Security Forward Transaction Multifonds DB Column is QTY_UNDER. |
| 91 | `FS.GA.FUTURE.TRANSACTION.UNDERLYING.SECURITY.PRICE` | `FsGaFutureTransaction_UnderlyingSecurityPrice` | TField |  | Underlying Security&apos;s Price for Security Forward Transaction Multifonds DB Column is COURS_UNDER. |
| 92 | `FS.GA.FUTURE.TRANSACTION.UNDERLYING.AMOUNT` | `FsGaFutureTransaction_UnderlyingAmount` | TField |  | Underlying Amount. Multifonds DB Column is MONTANT_UNDER. |
| 93 | `FS.GA.FUTURE.TRANSACTION.UNDERLYING.VALUATION.METHOD` | `FsGaFutureTransaction_UnderlyingValuationMethod` | TField |  | Underlying Valuation Method. Multifonds DB Column is VAL_METHOD. |
| 94 | `FS.GA.FUTURE.TRANSACTION.AUTO.MATURITY` | `FsGaFutureTransaction_AutoMaturity` | TField |  | Flag Auto Maturity. Multifonds DB Column is FLG_AUTO_MATURITY. |
| 95 | `FS.GA.FUTURE.TRANSACTION.FUTURE.VALUE` | `FsGaFutureTransaction_FutureValue` | TField |  | Future Value. Multifonds DB Column is FUT_VAL. |
| 96 | `FS.GA.FUTURE.TRANSACTION.CONFIRMED` | `FsGaFutureTransaction_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 97 | `FS.GA.FUTURE.TRANSACTION.FUTURE.CURRENCY` | `FsGaFutureTransaction_FutureCurrency` | TField |  | Future Currency Multifonds DB Column is CMON_FUT. |
| 98 | `FS.GA.FUTURE.TRANSACTION.LOCAL.SETTLEMENT.VCI` | `FsGaFutureTransaction_LocalSettlementVci` | TField |  | Local Settlement Vci Multifonds DB Column is LOC_SETT_VCI. |
| 99 | `FS.GA.FUTURE.TRANSACTION.FUND.SETTLEMENT.VCI` | `FsGaFutureTransaction_FundSettlementVci` | TField |  | Fund Settlement Vci Multifonds DB Column is SETTL_PTF_VCI. |
| 100 | `FS.GA.FUTURE.TRANSACTION.FUND.VCI.LOC` | `FsGaFutureTransaction_FundVciLoc` | TField |  | Fund VCI Loc Multifonds DB Column is LOC_PTF_VCI. |
| 101 | `FS.GA.FUTURE.TRANSACTION.ACCOUNTING.METHOD` | `FsGaFutureTransaction_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 102 | `FS.GA.FUTURE.TRANSACTION.FEES.ACCOUNT.NUMBER.SETTLED` | `FsGaFutureTransaction_FeesAccountNumberSettled` | TField |  | Fees Account Number Settled Multifonds DB Column is NRUBR_FEE_SETTL. |
| 103 | `FS.GA.FUTURE.TRANSACTION.FEES.SUFFIX.NUMBER.SETTLED` | `FsGaFutureTransaction_FeesSuffixNumberSettled` | TField |  | Fees Suffix Number Settled Multifonds DB Column is NSUFF_FEE_SETTL. |
| 104 | `FS.GA.FUTURE.TRANSACTION.GAIN.ACCOUNT.NUMBER.SETTLED` | `FsGaFutureTransaction_GainAccountNumberSettled` | TField |  | Gain Account Number Settled Multifonds DB Column is NRUBR_GP_SETTL. |
| 105 | `FS.GA.FUTURE.TRANSACTION.GAIN.SUFFIX.NUMBER.SETTLED` | `FsGaFutureTransaction_GainSuffixNumberSettled` | TField |  | Gain Suffix Number Settled Multifonds DB Column is NSUFF_GP_SETTL. |
| 106 | `FS.GA.FUTURE.TRANSACTION.VM.ACCOUNT.NUMBER.SETTLED` | `FsGaFutureTransaction_VmAccountNumberSettled` | TField |  | VM Account Number Settled Multifonds DB Column is NRUBR_VM_SETTL. |
| 107 | `FS.GA.FUTURE.TRANSACTION.VM.SUFFIX.NUMBER.SETTLED` | `FsGaFutureTransaction_VmSuffixNumberSettled` | TField |  | VM Suffix Number Settled Multifonds DB Column is NSUFF_VM_SETTL. |
| 108 | `FS.GA.FUTURE.TRANSACTION.EXISTING.DEBIT.ACC.NUMBER` | `FsGaFutureTransaction_ExistingDebitAccNumber` | TField |  | accounting number on the DB side Multifonds DB Column is NRUBR_INT_DB. |
| 109 | `FS.GA.FUTURE.TRANSACTION.DEBIT.SUFFIX.NUMBER` | `FsGaFutureTransaction_DebitSuffixNumber` | TField |  | suffix number of the interface of the exisitng system Multifonds DB Column is NSUFF_INT_DB. |
| 110 | `FS.GA.FUTURE.TRANSACTION.ACCOUNT.NUMBER.INTR` | `FsGaFutureTransaction_AccountNumberIntr` | TField |  | Account Number INTR Multifonds DB Column is NRUBR_INTR. |
| 111 | `FS.GA.FUTURE.TRANSACTION.SUFFIX.NUMBER.INTR` | `FsGaFutureTransaction_SuffixNumberIntr` | TField |  | Suffix Number INTR Multifonds DB Column is NSUFF_INTR. |
| 112 | `FS.GA.FUTURE.TRANSACTION.GL.ACCOUNT.NUMBER.INTR` | `FsGaFutureTransaction_GlAccountNumberIntr` | TField |  | GL Account Number INTR Multifonds DB Column is NRUBR_INTR_GL. |
| 113 | `FS.GA.FUTURE.TRANSACTION.GL.SUFFIX.NUMBER.INTR` | `FsGaFutureTransaction_GlSuffixNumberIntr` | TField |  | GL Suffix Number INTR Multifonds DB Column is NSUFF_INTR_GL. |
| 114 | `FS.GA.FUTURE.TRANSACTION.GL.ACCOUNT.NUMBER.INT` | `FsGaFutureTransaction_GlAccountNumberInt` | TField |  | GL Account Number INT Multifonds DB Column is NRUBR_INT_GL. |
| 115 | `FS.GA.FUTURE.TRANSACTION.GL.SUFFIX.NUMBER.INT` | `FsGaFutureTransaction_GlSuffixNumberInt` | TField |  | GL Suffix Number INT Multifonds DB Column is NSUFF_INT_GL. |
| 116 | `FS.GA.FUTURE.TRANSACTION.UTI.DESCRIPTION` | `FsGaFutureTransaction_UtiDescription` | TField |  | UTI Description Multifonds DB Column is UTI_DESC. |
| 117 | `FS.GA.FUTURE.TRANSACTION.USI.DESCRIPTION` | `FsGaFutureTransaction_UsiDescription` | TField |  | USI Description Multifonds DB Column is USI_DESC. |
| 118 | `FS.GA.FUTURE.TRANSACTION.TOTAL.RITC.VALUE` | `FsGaFutureTransaction_TotalRitcValue` | TField |  | Total RITC Value Multifonds DB Column is MFRAIS_RITC. |
| 119 | `FS.GA.FUTURE.TRANSACTION.GST.CLAIM.ID` | `FsGaFutureTransaction_GstClaimId` | TField |  | GST Claim ID Multifonds DB Column is GST_CLAIM_ID. |
| 120 | `FS.GA.FUTURE.TRANSACTION.GST.UPDATED.DATE` | `FsGaFutureTransaction_GstUpdatedDate` | TField |  | GST Updated date Multifonds DB Column is GST_DUPDATED. |
| 121 | `FS.GA.FUTURE.TRANSACTION.GST.UPDATED.BY` | `FsGaFutureTransaction_GstUpdatedBy` | TField |  | GST Updated By Multifonds DB Column is GST_UPDATED_BY. |
| 122 | `FS.GA.FUTURE.TRANSACTION.GST.CONFIRMATION` | `FsGaFutureTransaction_GstConfirmation` | TField |  | GST Confirmation Multifonds DB Column is GST_CONFIRM. |
| 123 | `FS.GA.FUTURE.TRANSACTION.GST.REVISED.CLAIM.ID` | `FsGaFutureTransaction_GstRevisedClaimId` | TField |  | GST Revised Claim ID Multifonds DB Column is GST_CLAIM_ID_REV. |
| 124 | `FS.GA.FUTURE.TRANSACTION.GST.REVISED.UPDATED.BY` | `FsGaFutureTransaction_GstRevisedUpdatedBy` | TField |  | GST Revised Updated By Multifonds DB Column is GST_UPDATED_BY_REV. |
| 125 | `FS.GA.FUTURE.TRANSACTION.GST.REVISED.UPDATED.DATE` | `FsGaFutureTransaction_GstRevisedUpdatedDate` | TField |  | GST Revised Updated Date Multifonds DB Column is GST_DUPDATED_REV. |
| 126 | `FS.GA.FUTURE.TRANSACTION.IM.CONTINUING` | `FsGaFutureTransaction_ImContinuing` | TField |  | This field display whether a particular transaction is continuing transaction or not Multifonds DB Column is FLG_IM_CONTINUING. |
| 127 | `FS.GA.FUTURE.TRANSACTION.ADJUSTMENT.FUND` | `FsGaFutureTransaction_AdjustmentFund` | TField |  | Adjustment Fund Multifonds DB Column is NPTF_ORIGIN. |
| 128 | `FS.GA.FUTURE.TRANSACTION.CORRESPONDENT.ADJ.NUMBER` | `FsGaFutureTransaction_CorrespondentAdjNumber` | TField |  | Correspondent adj number Multifonds DB Column is NCORRESP_ADJ. |
| 129 | `FS.GA.FUTURE.TRANSACTION.INTERPORT.TRADES` | `FsGaFutureTransaction_InterportTrades` | TField |  | Interport trades Multifonds DB Column is FLG_INTERPORT_TRADES. |
| 130 | `FS.GA.FUTURE.TRANSACTION.OPERATION.TYPE` | `FsGaFutureTransaction_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 131 | `FS.GA.FUTURE.TRANSACTION.RESERVED10` | `FsGaFutureTransaction_Reserved10` | TField |  |  |
| 132 | `FS.GA.FUTURE.TRANSACTION.RESERVED9` | `FsGaFutureTransaction_Reserved9` | TField |  |  |
| 133 | `FS.GA.FUTURE.TRANSACTION.RESERVED8` | `FsGaFutureTransaction_Reserved8` | TField |  |  |
| 134 | `FS.GA.FUTURE.TRANSACTION.RESERVED7` | `FsGaFutureTransaction_Reserved7` | TField |  |  |
| 135 | `FS.GA.FUTURE.TRANSACTION.RESERVED6` | `FsGaFutureTransaction_Reserved6` | TField |  |  |
| 136 | `FS.GA.FUTURE.TRANSACTION.RESERVED5` | `FsGaFutureTransaction_Reserved5` | TField |  |  |
| 137 | `FS.GA.FUTURE.TRANSACTION.RESERVED4` | `FsGaFutureTransaction_Reserved4` | TField |  |  |
| 138 | `FS.GA.FUTURE.TRANSACTION.RESERVED3` | `FsGaFutureTransaction_Reserved3` | TField |  |  |
| 139 | `FS.GA.FUTURE.TRANSACTION.RESERVED2` | `FsGaFutureTransaction_Reserved2` | TField |  |  |
| 140 | `FS.GA.FUTURE.TRANSACTION.RESERVED1` | `FsGaFutureTransaction_Reserved1` | TField |  |  |
| 141 | `FS.GA.FUTURE.TRANSACTION.LOCAL.REF` | `FsGaFutureTransaction_LocalRef` |  |  |  |
| 142 | `FS.GA.FUTURE.TRANSACTION.OVERRIDE` | `FsGaFutureTransaction_Override` |  |  |  |
| 143 | `FS.GA.FUTURE.TRANSACTION.RECORD.STATUS` | `FsGaFutureTransaction_RecordStatus` | String |  |  |
| 144 | `FS.GA.FUTURE.TRANSACTION.CURR.NO` | `FsGaFutureTransaction_CurrNo` | String |  |  |
| 145 | `FS.GA.FUTURE.TRANSACTION.INPUTTER` | `FsGaFutureTransaction_Inputter` |  |  |  |
| 146 | `FS.GA.FUTURE.TRANSACTION.DATE.TIME` | `FsGaFutureTransaction_DateTime` |  |  |  |
| 147 | `FS.GA.FUTURE.TRANSACTION.AUTHORISER` | `FsGaFutureTransaction_Authoriser` | String |  |  |
| 148 | `FS.GA.FUTURE.TRANSACTION.CO.CODE` | `FsGaFutureTransaction_CoCode` | String |  |  |
| 149 | `FS.GA.FUTURE.TRANSACTION.DEPT.CODE` | `FsGaFutureTransaction_DeptCode` | String |  |  |
| 150 | `FS.GA.FUTURE.TRANSACTION.AUDITOR.CODE` | `FsGaFutureTransaction_AuditorCode` | String |  |  |
| 151 | `FS.GA.FUTURE.TRANSACTION.AUDIT.DATE.TIME` | `FsGaFutureTransaction_AuditDateTime` | String |  |  |
