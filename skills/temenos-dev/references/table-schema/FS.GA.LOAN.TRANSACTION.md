# FS.GA.LOAN.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.LOAN.TRANSACTION` in `FS_Loan.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LOAN.TRANSACTION.PARENT.REF.ID` | `FsGaLoanTransaction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.LOAN.TRANSACTION.ORA.ROWID` | `FsGaLoanTransaction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.LOAN.TRANSACTION.FUND.ID` | `FsGaLoanTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.LOAN.TRANSACTION.TRANSACTION.NUMBER` | `FsGaLoanTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.LOAN.TRANSACTION.LOT.NUMBER` | `FsGaLoanTransaction_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 6 | `FS.GA.LOAN.TRANSACTION.CORRESPONDENT` | `FsGaLoanTransaction_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 7 | `FS.GA.LOAN.TRANSACTION.DESCRIPTION` | `FsGaLoanTransaction_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 8 | `FS.GA.LOAN.TRANSACTION.GL.ACCOUNT` | `FsGaLoanTransaction_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 9 | `FS.GA.LOAN.TRANSACTION.GL.ACCOUNT.SUFFIX` | `FsGaLoanTransaction_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 10 | `FS.GA.LOAN.TRANSACTION.CORRESP.CASH.ACC.NO.DEPOSIT` | `FsGaLoanTransaction_CorrespCashAccNoDeposit` | TField |  | Displays the correspondent cash account no to be used for settlement of deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is NRUBR_CC. |
| 11 | `FS.GA.LOAN.TRANSACTION.CORRESP.CASH.ACC.SUFFIX.DEPO` | `FsGaLoanTransaction_CorrespCashAccSuffixDepo` | TField |  | Displays the correspondent cash account suffix no to be used for settlement of deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is NSUFF_CC. |
| 12 | `FS.GA.LOAN.TRANSACTION.DEAL.CURRENCY` | `FsGaLoanTransaction_DealCurrency` | TField |  | Currency of settlement or currency of deal Multifonds DB Column is CDEV. |
| 13 | `FS.GA.LOAN.TRANSACTION.SETTLE.DATE` | `FsGaLoanTransaction_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 14 | `FS.GA.LOAN.TRANSACTION.MATURITY.DATE.OF.CONTRACT` | `FsGaLoanTransaction_MaturityDateOfContract` | TField |  | Maturity Date of the Contract/Instrument Multifonds DB Column is DECH. |
| 15 | `FS.GA.LOAN.TRANSACTION.NOTICE.DAYS.DEPOSIT` | `FsGaLoanTransaction_NoticeDaysDeposit` | TField |  | Notice days code like 24 hours, 48 hours, for deposits Multifonds DB Column is NOTICE. |
| 16 | `FS.GA.LOAN.TRANSACTION.DAY.COUNT.CONVENTION` | `FsGaLoanTransaction_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 17 | `FS.GA.LOAN.TRANSACTION.LOAN.AMOUNT.IN.LOAN.CCY` | `FsGaLoanTransaction_LoanAmountInLoanCcy` | TField |  | amount of the loan corresponding in loan ccy Multifonds DB Column is MONTANT_EMP. |
| 18 | `FS.GA.LOAN.TRANSACTION.LOAN.INTEREST.RATE` | `FsGaLoanTransaction_LoanInterestRate` | TField |  | Interest rate Multifonds DB Column is TX_EMP. |
| 19 | `FS.GA.LOAN.TRANSACTION.OPERATION.CODE` | `FsGaLoanTransaction_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 20 | `FS.GA.LOAN.TRANSACTION.ENTRY.NUMBER.REPAYMENT` | `FsGaLoanTransaction_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 21 | `FS.GA.LOAN.TRANSACTION.DEAL.STATUS.CODE` | `FsGaLoanTransaction_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 22 | `FS.GA.LOAN.TRANSACTION.FEES.AT.CREATION` | `FsGaLoanTransaction_FeesAtCreation` | TField |  | Enter fees at creation, if required Multifonds DB Column is MFRAIS_CREAT. |
| 23 | `FS.GA.LOAN.TRANSACTION.FEES.AT.MATURITY` | `FsGaLoanTransaction_FeesAtMaturity` | TField |  | Enter any fees to be charged at maturity, if required Multifonds DB Column is MFRAIS_REMB. |
| 24 | `FS.GA.LOAN.TRANSACTION.ACCRUED.INTEREST` | `FsGaLoanTransaction_AccruedInterest` | TField |  | Accrued interest of the security Multifonds DB Column is MINT. |
| 25 | `FS.GA.LOAN.TRANSACTION.SETTLEMENT.CURRENCY` | `FsGaLoanTransaction_SettlementCurrency` | TField |  | Currency in which the settlement would be processed. Multifonds DB Column is CMON_CORR. |
| 26 | `FS.GA.LOAN.TRANSACTION.EXCHANGE.RATE` | `FsGaLoanTransaction_ExchangeRate` | TField |  | Exchange rate between deal currency and settlement currency Multifonds DB Column is TCHG_CORR. |
| 27 | `FS.GA.LOAN.TRANSACTION.LOAN.CHANGED.AMOUNT` | `FsGaLoanTransaction_LoanChangedAmount` | TField |  | Changed amount during increase/decrease Multifonds DB Column is MNT_EMP_CORR. |
| 28 | `FS.GA.LOAN.TRANSACTION.ARCHIVE` | `FsGaLoanTransaction_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 29 | `FS.GA.LOAN.TRANSACTION.TRADE.DATE` | `FsGaLoanTransaction_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 30 | `FS.GA.LOAN.TRANSACTION.INCOME.TYPE` | `FsGaLoanTransaction_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 31 | `FS.GA.LOAN.TRANSACTION.COUNTERPARTY.CORRESPONDENT` | `FsGaLoanTransaction_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 32 | `FS.GA.LOAN.TRANSACTION.COUNTER.PARTY.CODE` | `FsGaLoanTransaction_CounterPartyCode` | TField |  | Guarantor,Issuer Multifonds DB Column is NISSUER_GUARANTEED. |
| 33 | `FS.GA.LOAN.TRANSACTION.MANAGER.ID` | `FsGaLoanTransaction_ManagerId` | TField |  | Manager ID Multifonds DB Column is NACC_MNGR. |
| 34 | `FS.GA.LOAN.TRANSACTION.MANAGER.CODE` | `FsGaLoanTransaction_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 35 | `FS.GA.LOAN.TRANSACTION.STATUS.PENDING` | `FsGaLoanTransaction_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 36 | `FS.GA.LOAN.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaLoanTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 37 | `FS.GA.LOAN.TRANSACTION.SPREAD.IDENTIFIER` | `FsGaLoanTransaction_SpreadIdentifier` | TField |  | Specify the spread percentage to be considered for NAV charges per fund. Multifonds DB Column is SPREAD. |
| 38 | `FS.GA.LOAN.TRANSACTION.FUND.INTEREST.CALCULATION` | `FsGaLoanTransaction_FundInterestCalculation` | TField |  | Fund Interest Calculation Multifonds DB Column is MINT_PTF_CALC. |
| 39 | `FS.GA.LOAN.TRANSACTION.DEAL.INTEREST.CALCULATION` | `FsGaLoanTransaction_DealInterestCalculation` | TField |  | Deal Interest Calcualtion Multifonds DB Column is MINT_DEAL_CALC. |
| 40 | `FS.GA.LOAN.TRANSACTION.EXECUTION.TIMESTAMP` | `FsGaLoanTransaction_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 41 | `FS.GA.LOAN.TRANSACTION.CONFIRMED` | `FsGaLoanTransaction_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 42 | `FS.GA.LOAN.TRANSACTION.CONFIRMATION.DATE` | `FsGaLoanTransaction_ConfirmationDate` | TField |  | Confirmation Date Multifonds DB Column is CONFIRM_DATE. |
| 43 | `FS.GA.LOAN.TRANSACTION.FUND.STRATEGY` | `FsGaLoanTransaction_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 44 | `FS.GA.LOAN.TRANSACTION.FUND.LINK.ID` | `FsGaLoanTransaction_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 45 | `FS.GA.LOAN.TRANSACTION.CHECK.DATE` | `FsGaLoanTransaction_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 46 | `FS.GA.LOAN.TRANSACTION.CHECKED.BY` | `FsGaLoanTransaction_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 47 | `FS.GA.LOAN.TRANSACTION.IFRS.TAG` | `FsGaLoanTransaction_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 48 | `FS.GA.LOAN.TRANSACTION.REPO.TYPE.CODE` | `FsGaLoanTransaction_RepoTypeCode` | TField |  | The field which links to deal screen FDDEP01 and FDEMP02. The list of values is available through F9 in FDCBO01 screen which draws the repo type code from the new repo type definition screen FDRPO01. Multifonds DB Column is REPO_ID. |
| 49 | `FS.GA.LOAN.TRANSACTION.QUOTATION.PLACE` | `FsGaLoanTransaction_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 50 | `FS.GA.LOAN.TRANSACTION.NUMB.OF.DAYS` | `FsGaLoanTransaction_NumbOfDays` | TField |  | Number of day&apos;s between deposit&apos;s value date to maturity date, number of a fixed number of days or number of NAVs as at which fees will be accrued for. Multifonds DB Column is NB_JOURS. |
| 51 | `FS.GA.LOAN.TRANSACTION.REPO.ID` | `FsGaLoanTransaction_RepoId` | TField |  | This field displays Repo Id of the transaction Multifonds DB Column is REPO_SEC_ID. |
| 52 | `FS.GA.LOAN.TRANSACTION.LOCAL.SETTLEMENT.VCI` | `FsGaLoanTransaction_LocalSettlementVci` | TField |  | Local Settlement Vci Multifonds DB Column is LOC_SETT_VCI. |
| 53 | `FS.GA.LOAN.TRANSACTION.FUND.SETTLEMENT.VCI` | `FsGaLoanTransaction_FundSettlementVci` | TField |  | Fund Settlement Vci Multifonds DB Column is SETTL_PTF_VCI. |
| 54 | `FS.GA.LOAN.TRANSACTION.FUND.VCI.LOC` | `FsGaLoanTransaction_FundVciLoc` | TField |  | Fund VCI Loc Multifonds DB Column is LOC_PTF_VCI. |
| 55 | `FS.GA.LOAN.TRANSACTION.EXCH.RATE.SETTLEMENT.TO.DEAL` | `FsGaLoanTransaction_ExchRateSettlementToDeal` | TField |  | The exchange rate between the settlement and deal currency Multifonds DB Column is TCHG_PTF. |
| 56 | `FS.GA.LOAN.TRANSACTION.REPAY.LOCAL.SETTLED.VCI` | `FsGaLoanTransaction_RepayLocalSettledVci` | TField |  | Repay Local Settled VCI Multifonds DB Column is REPAY_LOC_SETT_VCI. |
| 57 | `FS.GA.LOAN.TRANSACTION.REPAY.FUND.SETTLED.VCI` | `FsGaLoanTransaction_RepayFundSettledVci` | TField |  | Repay Fund Settled VCI Multifonds DB Column is REPAY_SETTL_PTF_VCI. |
| 58 | `FS.GA.LOAN.TRANSACTION.REPAY.LOCAL.FUND.VCI` | `FsGaLoanTransaction_RepayLocalFundVci` | TField |  | Repay Local Fund VCI Multifonds DB Column is REPAY_LOC_PTF_VCI. |
| 59 | `FS.GA.LOAN.TRANSACTION.EXCHANGE.RATE.REPAY.FUND` | `FsGaLoanTransaction_ExchangeRateRepayFund` | TField |  | Exchange Rate Repay Fund Multifonds DB Column is REPAY_TCHG_PTF. |
| 60 | `FS.GA.LOAN.TRANSACTION.REPAYMENT.AMOUNT.ACCOUNT.NUM` | `FsGaLoanTransaction_RepaymentAmountAccountNum` | TField |  | Repayment Amount Account Number Multifonds DB Column is REPAY_MINT_NRUBR. |
| 61 | `FS.GA.LOAN.TRANSACTION.REPAY.ACCOUNT.NUMBER` | `FsGaLoanTransaction_RepayAccountNumber` | TField |  | Repay Account Number Multifonds DB Column is REPAY_NRUBR. |
| 62 | `FS.GA.LOAN.TRANSACTION.INTEREST.ACCOUNT.NUMBER` | `FsGaLoanTransaction_InterestAccountNumber` | TField |  | Interest Account Number Multifonds DB Column is MINT_NRUBR. |
| 63 | `FS.GA.LOAN.TRANSACTION.REPAY.OPERATOR.CODE` | `FsGaLoanTransaction_RepayOperatorCode` | TField |  | Repay Operator Code Multifonds DB Column is REPAY_COPER. |
| 64 | `FS.GA.LOAN.TRANSACTION.OPERATION.CODE.MINT` | `FsGaLoanTransaction_OperationCodeMint` | TField |  | Operation Code MINT Multifonds DB Column is MINT_COPER. |
| 65 | `FS.GA.LOAN.TRANSACTION.ACCOUNTING.METHOD` | `FsGaLoanTransaction_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 66 | `FS.GA.LOAN.TRANSACTION.REPAYMENT.DATE` | `FsGaLoanTransaction_RepaymentDate` | TField |  | Repayment Date Multifonds DB Column is REPAYMENT_DATE. |
| 67 | `FS.GA.LOAN.TRANSACTION.PREVIOUS.STATUS.CODE` | `FsGaLoanTransaction_PreviousStatusCode` | TField |  | Previous Status Code Multifonds DB Column is PREV_CSTATUS. |
| 68 | `FS.GA.LOAN.TRANSACTION.COUPON.FREQUENCY.CODE` | `FsGaLoanTransaction_CouponFrequencyCode` | TField |  | Frequency of payment of coupon/ commission Multifonds DB Column is CFREQCOUP. |
| 69 | `FS.GA.LOAN.TRANSACTION.FIRST.COUPON.DATE` | `FsGaLoanTransaction_FirstCouponDate` | TField |  | First Coupon Date Multifonds DB Column is DATCOUPON. |
| 70 | `FS.GA.LOAN.TRANSACTION.EXTERNAL.CONTRACT.NUMBER` | `FsGaLoanTransaction_ExternalContractNumber` | TField |  | External Contract Number Multifonds DB Column is NCONTRAT_EXT. |
| 71 | `FS.GA.LOAN.TRANSACTION.UTI.DESCRIPTION` | `FsGaLoanTransaction_UtiDescription` | TField |  | UTI Description Multifonds DB Column is UTI_DESC. |
| 72 | `FS.GA.LOAN.TRANSACTION.USI.DESCRIPTION` | `FsGaLoanTransaction_UsiDescription` | TField |  | USI Description Multifonds DB Column is USI_DESC. |
| 73 | `FS.GA.LOAN.TRANSACTION.PREVIOUS.REPAYMENT.ENTRY.NUM` | `FsGaLoanTransaction_PreviousRepaymentEntryNum` | TField |  | Previous Repayment Entry Number Multifonds DB Column is PREV_NECRITUR_REMB. |
| 74 | `FS.GA.LOAN.TRANSACTION.OPERATION.TYPE` | `FsGaLoanTransaction_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 75 | `FS.GA.LOAN.TRANSACTION.RESERVED10` | `FsGaLoanTransaction_Reserved10` | TField |  |  |
| 76 | `FS.GA.LOAN.TRANSACTION.RESERVED9` | `FsGaLoanTransaction_Reserved9` | TField |  |  |
| 77 | `FS.GA.LOAN.TRANSACTION.RESERVED8` | `FsGaLoanTransaction_Reserved8` | TField |  |  |
| 78 | `FS.GA.LOAN.TRANSACTION.RESERVED7` | `FsGaLoanTransaction_Reserved7` | TField |  |  |
| 79 | `FS.GA.LOAN.TRANSACTION.RESERVED6` | `FsGaLoanTransaction_Reserved6` | TField |  |  |
| 80 | `FS.GA.LOAN.TRANSACTION.RESERVED5` | `FsGaLoanTransaction_Reserved5` | TField |  |  |
| 81 | `FS.GA.LOAN.TRANSACTION.RESERVED4` | `FsGaLoanTransaction_Reserved4` | TField |  |  |
| 82 | `FS.GA.LOAN.TRANSACTION.RESERVED3` | `FsGaLoanTransaction_Reserved3` | TField |  |  |
| 83 | `FS.GA.LOAN.TRANSACTION.RESERVED2` | `FsGaLoanTransaction_Reserved2` | TField |  |  |
| 84 | `FS.GA.LOAN.TRANSACTION.RESERVED1` | `FsGaLoanTransaction_Reserved1` | TField |  |  |
| 85 | `FS.GA.LOAN.TRANSACTION.LOCAL.REF` | `FsGaLoanTransaction_LocalRef` |  |  |  |
| 86 | `FS.GA.LOAN.TRANSACTION.OVERRIDE` | `FsGaLoanTransaction_Override` |  |  |  |
| 87 | `FS.GA.LOAN.TRANSACTION.RECORD.STATUS` | `FsGaLoanTransaction_RecordStatus` | String |  |  |
| 88 | `FS.GA.LOAN.TRANSACTION.CURR.NO` | `FsGaLoanTransaction_CurrNo` | String |  |  |
| 89 | `FS.GA.LOAN.TRANSACTION.INPUTTER` | `FsGaLoanTransaction_Inputter` |  |  |  |
| 90 | `FS.GA.LOAN.TRANSACTION.DATE.TIME` | `FsGaLoanTransaction_DateTime` |  |  |  |
| 91 | `FS.GA.LOAN.TRANSACTION.AUTHORISER` | `FsGaLoanTransaction_Authoriser` | String |  |  |
| 92 | `FS.GA.LOAN.TRANSACTION.CO.CODE` | `FsGaLoanTransaction_CoCode` | String |  |  |
| 93 | `FS.GA.LOAN.TRANSACTION.DEPT.CODE` | `FsGaLoanTransaction_DeptCode` | String |  |  |
| 94 | `FS.GA.LOAN.TRANSACTION.AUDITOR.CODE` | `FsGaLoanTransaction_AuditorCode` | String |  |  |
| 95 | `FS.GA.LOAN.TRANSACTION.AUDIT.DATE.TIME` | `FsGaLoanTransaction_AuditDateTime` | String |  |  |
