# FS.GA.CALL.DEPOSIT.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.CALL.DEPOSIT.TRANSACTION` in `FS_CallDeposit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CALL.DEPOSIT.TRANSACTION.PARENT.REF.ID` | `FsGaCallDepositTransaction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CALL.DEPOSIT.TRANSACTION.ORA.ROWID` | `FsGaCallDepositTransaction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FUND.ID` | `FsGaCallDepositTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.CALL.DEPOSIT.TRANSACTION.TRANSACTION.NUMBER` | `FsGaCallDepositTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.CALL.DEPOSIT.TRANSACTION.LOT.NUMBER` | `FsGaCallDepositTransaction_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 6 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CORRESPONDENT` | `FsGaCallDepositTransaction_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 7 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DESCRIPTION` | `FsGaCallDepositTransaction_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 8 | `FS.GA.CALL.DEPOSIT.TRANSACTION.GL.ACCOUNT` | `FsGaCallDepositTransaction_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 9 | `FS.GA.CALL.DEPOSIT.TRANSACTION.GL.ACCOUNT.SUFFIX` | `FsGaCallDepositTransaction_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 10 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CORRESP.CASH.ACC.NO.DEPOSIT` | `FsGaCallDepositTransaction_CorrespCashAccNoDeposit` | TField |  | Displays the correspondent cash account no to be used for settlement of deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is NRUBR_CC. |
| 11 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CORRESP.CASH.ACC.SUFFIX.DEPO` | `FsGaCallDepositTransaction_CorrespCashAccSuffixDepo` | TField |  | Displays the correspondent cash account suffix no to be used for settlement of deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is NSUFF_CC. |
| 12 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DEAL.CURRENCY` | `FsGaCallDepositTransaction_DealCurrency` | TField |  | Currency of settlement or currency of deal Multifonds DB Column is CDEV. |
| 13 | `FS.GA.CALL.DEPOSIT.TRANSACTION.SETTLE.DATE` | `FsGaCallDepositTransaction_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 14 | `FS.GA.CALL.DEPOSIT.TRANSACTION.NOTICE.DAYS.DEPOSIT` | `FsGaCallDepositTransaction_NoticeDaysDeposit` | TField |  | Notice days code like 24 hours, 48 hours, for deposits Multifonds DB Column is NOTICE. |
| 15 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DAY.COUNT.CONVENTION` | `FsGaCallDepositTransaction_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 16 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DEPOSIT.AMOUNT.IN.DEPOSIT.CCY` | `FsGaCallDepositTransaction_DepositAmountInDepositCcy` | TField |  | amount of the DP corresponding in the deposit ccy Multifonds DB Column is MONTANT_DPO. |
| 17 | `FS.GA.CALL.DEPOSIT.TRANSACTION.INTEREST.RATE.PERCENTAGE` | `FsGaCallDepositTransaction_InterestRatePercentage` | TField |  | Refers to interest rate % to be applied to deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is TX_DPO. |
| 18 | `FS.GA.CALL.DEPOSIT.TRANSACTION.OPERATION.CODE` | `FsGaCallDepositTransaction_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 19 | `FS.GA.CALL.DEPOSIT.TRANSACTION.ENTRY.NUMBER.REPAYMENT` | `FsGaCallDepositTransaction_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 20 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DEAL.STATUS.CODE` | `FsGaCallDepositTransaction_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 21 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FEES.AT.CREATION` | `FsGaCallDepositTransaction_FeesAtCreation` | TField |  | Enter fees at creation, if required Multifonds DB Column is MFRAIS_CREAT. |
| 22 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FEES.AT.MATURITY` | `FsGaCallDepositTransaction_FeesAtMaturity` | TField |  | Enter any fees to be charged at maturity, if required Multifonds DB Column is MFRAIS_REMB. |
| 23 | `FS.GA.CALL.DEPOSIT.TRANSACTION.INTEREST.RATE.TYPE` | `FsGaCallDepositTransaction_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 24 | `FS.GA.CALL.DEPOSIT.TRANSACTION.INTEREST.AMOUNT.CR` | `FsGaCallDepositTransaction_InterestAmountCr` | TField |  | Displays the interest amount Multifonds DB Column is MNT_INT_CR. |
| 25 | `FS.GA.CALL.DEPOSIT.TRANSACTION.SETTLEMENT.CURRENCY` | `FsGaCallDepositTransaction_SettlementCurrency` | TField |  | Currency in which the settlement would be processed. Multifonds DB Column is CMON_CORR. |
| 26 | `FS.GA.CALL.DEPOSIT.TRANSACTION.EXCHANGE.RATE` | `FsGaCallDepositTransaction_ExchangeRate` | TField |  | Exchange rate between deal currency and settlement currency Multifonds DB Column is TCHG_CORR. |
| 27 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DEPOSIT.REPAYMENT.AMOUNT` | `FsGaCallDepositTransaction_DepositRepaymentAmount` | TField |  | Deposit Repayment Amount in settlement currency Multifonds DB Column is MNT_DEP_CORR. |
| 28 | `FS.GA.CALL.DEPOSIT.TRANSACTION.ARCHIVE` | `FsGaCallDepositTransaction_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 29 | `FS.GA.CALL.DEPOSIT.TRANSACTION.ACCRUED.INTEREST` | `FsGaCallDepositTransaction_AccruedInterest` | TField |  | Accrued interest of the security Multifonds DB Column is MINT. |
| 30 | `FS.GA.CALL.DEPOSIT.TRANSACTION.TRADE.DATE` | `FsGaCallDepositTransaction_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 31 | `FS.GA.CALL.DEPOSIT.TRANSACTION.COUNTERPARTY.CORRESPONDENT` | `FsGaCallDepositTransaction_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 32 | `FS.GA.CALL.DEPOSIT.TRANSACTION.COUNTER.PARTY.CODE` | `FsGaCallDepositTransaction_CounterPartyCode` | TField |  | Guarantor,Issuer Multifonds DB Column is NISSUER_GUARANTEED. |
| 33 | `FS.GA.CALL.DEPOSIT.TRANSACTION.MANAGER.ID` | `FsGaCallDepositTransaction_ManagerId` | TField |  | Manager ID Multifonds DB Column is NACC_MNGR. |
| 34 | `FS.GA.CALL.DEPOSIT.TRANSACTION.MANAGER.CODE` | `FsGaCallDepositTransaction_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 35 | `FS.GA.CALL.DEPOSIT.TRANSACTION.STATUS.PENDING` | `FsGaCallDepositTransaction_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 36 | `FS.GA.CALL.DEPOSIT.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaCallDepositTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 37 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CODE.OF.FREQUENCY` | `FsGaCallDepositTransaction_CodeOfFrequency` | TField |  | Frequence Code Multifonds DB Column is CODE_FREQUENCE. |
| 38 | `FS.GA.CALL.DEPOSIT.TRANSACTION.MATURITY.DATE.OF.CONTRACT` | `FsGaCallDepositTransaction_MaturityDateOfContract` | TField |  | Maturity Date of the Contract/Instrument Multifonds DB Column is DECH. |
| 39 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CONTRACT.NO.RES.TRANSACTION` | `FsGaCallDepositTransaction_ContractNoResTransaction` | TField |  | contract number for reserve trasnactions Multifonds DB Column is NCONTRAT_RESERVE. |
| 40 | `FS.GA.CALL.DEPOSIT.TRANSACTION.SERVICE.CODE` | `FsGaCallDepositTransaction_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 41 | `FS.GA.CALL.DEPOSIT.TRANSACTION.REDEMPTION.DATE.SECURITY` | `FsGaCallDepositTransaction_RedemptionDateSecurity` | TField |  | Generally the redemption date for bonds and deposits Multifonds DB Column is DATE_REMB. |
| 42 | `FS.GA.CALL.DEPOSIT.TRANSACTION.INTERNAL.REFERENCE.NUMBER` | `FsGaCallDepositTransaction_InternalReferenceNumber` | TField |  | Internal Reference Number for Deposits/Loans Multifonds DB Column is DEAL_ID. |
| 43 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CALCULATION.PAYMENT.DATE` | `FsGaCallDepositTransaction_CalculationPaymentDate` | TField |  | Logic to decide if payment date falls on a non working day should it process paymet on same date or prior/next working day. Multifonds DB Column is CTR_DATE. |
| 44 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DEAL.INTEREST.CALCULATION` | `FsGaCallDepositTransaction_DealInterestCalculation` | TField |  | Deal Interest Calcualtion Multifonds DB Column is MINT_DEAL_CALC. |
| 45 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FUND.INTEREST.CALCULATION` | `FsGaCallDepositTransaction_FundInterestCalculation` | TField |  | Fund Interest Calculation Multifonds DB Column is MINT_PTF_CALC. |
| 46 | `FS.GA.CALL.DEPOSIT.TRANSACTION.WITHOLDING.TAX.PERCENTAGE` | `FsGaCallDepositTransaction_WitholdingTaxPercentage` | TField |  | The &apos;Withholding tax %&apos; field is defined with a default tax rate to be applied to deposit transactions if a tax rate is not setup for deposit transaction operation codes taxes. Multifonds DB Column is PCT_IMPOT. |
| 47 | `FS.GA.CALL.DEPOSIT.TRANSACTION.EXECUTION.TIMESTAMP` | `FsGaCallDepositTransaction_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 48 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CONFIRMED` | `FsGaCallDepositTransaction_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 49 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CONFIRMATION.DATE` | `FsGaCallDepositTransaction_ConfirmationDate` | TField |  | Confirmation Date Multifonds DB Column is CONFIRM_DATE. |
| 50 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FUND.STRATEGY` | `FsGaCallDepositTransaction_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 51 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FUND.LINK.ID` | `FsGaCallDepositTransaction_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 52 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CHECK.DATE` | `FsGaCallDepositTransaction_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 53 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CHECKED.BY` | `FsGaCallDepositTransaction_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 54 | `FS.GA.CALL.DEPOSIT.TRANSACTION.IFRS.TAG` | `FsGaCallDepositTransaction_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 55 | `FS.GA.CALL.DEPOSIT.TRANSACTION.LOCAL.SETTLE.VCI` | `FsGaCallDepositTransaction_LocalSettleVci` | TField |  | Local Settle VCI Multifonds DB Column is LOC_SETTL_VCI. |
| 56 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FUND.SETTLEMENT.VCI` | `FsGaCallDepositTransaction_FundSettlementVci` | TField |  | Fund Settlement Vci Multifonds DB Column is SETTL_PTF_VCI. |
| 57 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FUND.VCI.LOC` | `FsGaCallDepositTransaction_FundVciLoc` | TField |  | Fund VCI Loc Multifonds DB Column is LOC_PTF_VCI. |
| 58 | `FS.GA.CALL.DEPOSIT.TRANSACTION.LOCAL.REPAYMENT.SETTLE.VCI` | `FsGaCallDepositTransaction_LocalRepaymentSettleVci` | TField |  | Local Repayment Settle Vci Multifonds DB Column is REPAY_LOC_SETTL_VCI. |
| 59 | `FS.GA.CALL.DEPOSIT.TRANSACTION.REPAY.FUND.SETTLED.VCI` | `FsGaCallDepositTransaction_RepayFundSettledVci` | TField |  | Repay Fund Settled VCI Multifonds DB Column is REPAY_SETTL_PTF_VCI. |
| 60 | `FS.GA.CALL.DEPOSIT.TRANSACTION.REPAY.LOCAL.FUND.VCI` | `FsGaCallDepositTransaction_RepayLocalFundVci` | TField |  | Repay Local Fund VCI Multifonds DB Column is REPAY_LOC_PTF_VCI. |
| 61 | `FS.GA.CALL.DEPOSIT.TRANSACTION.ANTICIPATED.PAYMENT` | `FsGaCallDepositTransaction_AnticipatedPayment` | TField |  | Anticipated Payment Multifonds DB Column is REPAY_DATE. |
| 62 | `FS.GA.CALL.DEPOSIT.TRANSACTION.REPAYMENT.AMOUNT.ACCOUNT.NUM` | `FsGaCallDepositTransaction_RepaymentAmountAccountNum` | TField |  | Repayment Amount Account Number Multifonds DB Column is REPAY_MINT_NRUBR. |
| 63 | `FS.GA.CALL.DEPOSIT.TRANSACTION.SUFFIX.REPAYMENT.AMOUNT` | `FsGaCallDepositTransaction_SuffixRepaymentAmount` | TField |  | Suffix Repayment Amount Multifonds DB Column is REPAY_MINT_NSUFF. |
| 64 | `FS.GA.CALL.DEPOSIT.TRANSACTION.REPAYMENT.AMOUNT.OP.CODE` | `FsGaCallDepositTransaction_RepaymentAmountOpCode` | TField |  | Repayment Amount COPER Multifonds DB Column is REPAY_MINT_COPER. |
| 65 | `FS.GA.CALL.DEPOSIT.TRANSACTION.REPAY.ACCOUNT.NUMBER` | `FsGaCallDepositTransaction_RepayAccountNumber` | TField |  | Repay Account Number Multifonds DB Column is REPAY_NRUBR. |
| 66 | `FS.GA.CALL.DEPOSIT.TRANSACTION.SUFFIX.NUMBER.REPAY` | `FsGaCallDepositTransaction_SuffixNumberRepay` | TField |  | Suffix Number Repay Multifonds DB Column is REPAY_NSUFF. |
| 67 | `FS.GA.CALL.DEPOSIT.TRANSACTION.REPAY.OPERATOR.CODE` | `FsGaCallDepositTransaction_RepayOperatorCode` | TField |  | Repay Operator Code Multifonds DB Column is REPAY_COPER. |
| 68 | `FS.GA.CALL.DEPOSIT.TRANSACTION.ACCOUNTING.METHOD` | `FsGaCallDepositTransaction_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 69 | `FS.GA.CALL.DEPOSIT.TRANSACTION.PREVIOUS.STATUS.CODE` | `FsGaCallDepositTransaction_PreviousStatusCode` | TField |  | Previous Status Code Multifonds DB Column is PREV_CSTATUS. |
| 70 | `FS.GA.CALL.DEPOSIT.TRANSACTION.FIRST.COUPON.DATE` | `FsGaCallDepositTransaction_FirstCouponDate` | TField |  | First Coupon Date Multifonds DB Column is DATCOUPON. |
| 71 | `FS.GA.CALL.DEPOSIT.TRANSACTION.OPERATION.TYPE` | `FsGaCallDepositTransaction_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 72 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED10` | `FsGaCallDepositTransaction_Reserved10` | TField |  |  |
| 73 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED9` | `FsGaCallDepositTransaction_Reserved9` | TField |  |  |
| 74 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED8` | `FsGaCallDepositTransaction_Reserved8` | TField |  |  |
| 75 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED7` | `FsGaCallDepositTransaction_Reserved7` | TField |  |  |
| 76 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED6` | `FsGaCallDepositTransaction_Reserved6` | TField |  |  |
| 77 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED5` | `FsGaCallDepositTransaction_Reserved5` | TField |  |  |
| 78 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED4` | `FsGaCallDepositTransaction_Reserved4` | TField |  |  |
| 79 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED3` | `FsGaCallDepositTransaction_Reserved3` | TField |  |  |
| 80 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED2` | `FsGaCallDepositTransaction_Reserved2` | TField |  |  |
| 81 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RESERVED1` | `FsGaCallDepositTransaction_Reserved1` | TField |  |  |
| 82 | `FS.GA.CALL.DEPOSIT.TRANSACTION.LOCAL.REF` | `FsGaCallDepositTransaction_LocalRef` |  |  |  |
| 83 | `FS.GA.CALL.DEPOSIT.TRANSACTION.OVERRIDE` | `FsGaCallDepositTransaction_Override` |  |  |  |
| 84 | `FS.GA.CALL.DEPOSIT.TRANSACTION.RECORD.STATUS` | `FsGaCallDepositTransaction_RecordStatus` | String |  |  |
| 85 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CURR.NO` | `FsGaCallDepositTransaction_CurrNo` | String |  |  |
| 86 | `FS.GA.CALL.DEPOSIT.TRANSACTION.INPUTTER` | `FsGaCallDepositTransaction_Inputter` |  |  |  |
| 87 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DATE.TIME` | `FsGaCallDepositTransaction_DateTime` |  |  |  |
| 88 | `FS.GA.CALL.DEPOSIT.TRANSACTION.AUTHORISER` | `FsGaCallDepositTransaction_Authoriser` | String |  |  |
| 89 | `FS.GA.CALL.DEPOSIT.TRANSACTION.CO.CODE` | `FsGaCallDepositTransaction_CoCode` | String |  |  |
| 90 | `FS.GA.CALL.DEPOSIT.TRANSACTION.DEPT.CODE` | `FsGaCallDepositTransaction_DeptCode` | String |  |  |
| 91 | `FS.GA.CALL.DEPOSIT.TRANSACTION.AUDITOR.CODE` | `FsGaCallDepositTransaction_AuditorCode` | String |  |  |
| 92 | `FS.GA.CALL.DEPOSIT.TRANSACTION.AUDIT.DATE.TIME` | `FsGaCallDepositTransaction_AuditDateTime` | String |  |  |
