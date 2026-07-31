# FS.GA.DEPOSIT — Table Schema

> Source: `INSERTS/I_F.FS.GA.DEPOSIT` in `FS_Deposit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DEPOSIT.PARENT.REF.ID` | `FsGaDeposit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.DEPOSIT.ORA.ROWID` | `FsGaDeposit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.DEPOSIT.FUND.ID` | `FsGaDeposit_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.DEPOSIT.TRANSACTION.NUMBER` | `FsGaDeposit_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.DEPOSIT.LOT.NUMBER` | `FsGaDeposit_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 6 | `FS.GA.DEPOSIT.CORRESPONDENT` | `FsGaDeposit_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 7 | `FS.GA.DEPOSIT.DESCRIPTION` | `FsGaDeposit_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 8 | `FS.GA.DEPOSIT.GL.ACCOUNT` | `FsGaDeposit_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 9 | `FS.GA.DEPOSIT.GL.ACCOUNT.SUFFIX` | `FsGaDeposit_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 10 | `FS.GA.DEPOSIT.CORRESP.CASH.ACC.NO.DEPOSIT` | `FsGaDeposit_CorrespCashAccNoDeposit` | TField |  | Displays the correspondent cash account no to be used for settlement of deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is NRUBR_CC. |
| 11 | `FS.GA.DEPOSIT.CORRESP.CASH.ACC.SUFFIX.DEPO` | `FsGaDeposit_CorrespCashAccSuffixDepo` | TField |  | Displays the correspondent cash account suffix no to be used for settlement of deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is NSUFF_CC. |
| 12 | `FS.GA.DEPOSIT.DEAL.CURRENCY` | `FsGaDeposit_DealCurrency` | TField |  | Currency of settlement or currency of deal Multifonds DB Column is CDEV. |
| 13 | `FS.GA.DEPOSIT.SETTLE.DATE` | `FsGaDeposit_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 14 | `FS.GA.DEPOSIT.MATURITY.DATE.OF.CONTRACT` | `FsGaDeposit_MaturityDateOfContract` | TField |  | Maturity Date of the Contract/Instrument Multifonds DB Column is DECH. |
| 15 | `FS.GA.DEPOSIT.NOTICE.DAYS.DEPOSIT` | `FsGaDeposit_NoticeDaysDeposit` | TField |  | Notice days code like 24 hours, 48 hours, for deposits Multifonds DB Column is NOTICE. |
| 16 | `FS.GA.DEPOSIT.DAY.COUNT.CONVENTION` | `FsGaDeposit_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 17 | `FS.GA.DEPOSIT.DEPOSIT.AMOUNT.IN.DEPOSIT.CCY` | `FsGaDeposit_DepositAmountInDepositCcy` | TField |  | amount of the DP corresponding in the deposit ccy Multifonds DB Column is MONTANT_DPO. |
| 18 | `FS.GA.DEPOSIT.INTEREST.RATE.PERCENTAGE` | `FsGaDeposit_InterestRatePercentage` | TField |  | Refers to interest rate % to be applied to deposit transactions which includes call deposits, fixed deposits, cash sweep transactions, cash sweep adjustment etc Multifonds DB Column is TX_DPO. |
| 19 | `FS.GA.DEPOSIT.OPERATION.CODE` | `FsGaDeposit_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 20 | `FS.GA.DEPOSIT.ENTRY.NUMBER.REPAYMENT` | `FsGaDeposit_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 21 | `FS.GA.DEPOSIT.DEAL.STATUS.CODE` | `FsGaDeposit_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 22 | `FS.GA.DEPOSIT.FEES.AT.CREATION` | `FsGaDeposit_FeesAtCreation` | TField |  | Enter fees at creation, if required Multifonds DB Column is MFRAIS_CREAT. |
| 23 | `FS.GA.DEPOSIT.FEES.AT.MATURITY` | `FsGaDeposit_FeesAtMaturity` | TField |  | Enter any fees to be charged at maturity, if required Multifonds DB Column is MFRAIS_REMB. |
| 24 | `FS.GA.DEPOSIT.ACCRUED.INTEREST` | `FsGaDeposit_AccruedInterest` | TField |  | Accrued interest of the security Multifonds DB Column is MINT. |
| 25 | `FS.GA.DEPOSIT.SETTLEMENT.CURRENCY` | `FsGaDeposit_SettlementCurrency` | TField |  | Currency in which the settlement would be processed. Multifonds DB Column is CMON_CORR. |
| 26 | `FS.GA.DEPOSIT.EXCHANGE.RATE` | `FsGaDeposit_ExchangeRate` | TField |  | Exchange rate between deal currency and settlement currency Multifonds DB Column is TCHG_CORR. |
| 27 | `FS.GA.DEPOSIT.DEPOSIT.REPAYMENT.AMOUNT` | `FsGaDeposit_DepositRepaymentAmount` | TField |  | Deposit Repayment Amount in settlement currency Multifonds DB Column is MNT_DEP_CORR. |
| 28 | `FS.GA.DEPOSIT.ARCHIVE` | `FsGaDeposit_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 29 | `FS.GA.DEPOSIT.TRADE.DATE` | `FsGaDeposit_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 30 | `FS.GA.DEPOSIT.SERVICE.CODE.REP` | `FsGaDeposit_ServiceCodeRep` | TField |  | Service Code REP Multifonds DB Column is CSERVICE_REP. |
| 31 | `FS.GA.DEPOSIT.ENTRY.NUMBER.REP` | `FsGaDeposit_EntryNumberRep` | TField |  | Entry Number REP Multifonds DB Column is NECRITUR_REP. |
| 32 | `FS.GA.DEPOSIT.COMMISSION.ON.DEPOSIT` | `FsGaDeposit_CommissionOnDeposit` | TField |  | Commission on Deposit Multifonds DB Column is COMM_REP. |
| 33 | `FS.GA.DEPOSIT.SPLIT` | `FsGaDeposit_Split` | TField |  | Only used for repurchase agreements. This field is used for information. Multifonds DB Column is SPLIT_REP. |
| 34 | `FS.GA.DEPOSIT.COUNTERPARTY.CORRESPONDENT` | `FsGaDeposit_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 35 | `FS.GA.DEPOSIT.ROLLOVER` | `FsGaDeposit_Rollover` | TField |  | Rollover Identifier Multifonds DB Column is FLG_ROLLOVER. |
| 36 | `FS.GA.DEPOSIT.COUNTER.PARTY.CODE` | `FsGaDeposit_CounterPartyCode` | TField |  | Guarantor,Issuer Multifonds DB Column is NISSUER_GUARANTEED. |
| 37 | `FS.GA.DEPOSIT.IMPOT.AMOUNT` | `FsGaDeposit_ImpotAmount` | TField |  | Impot Amount Multifonds DB Column is MNT_IMPOT. |
| 38 | `FS.GA.DEPOSIT.IMPOT.CURRENCY` | `FsGaDeposit_ImpotCurrency` | TField |  | Tax currency of the income Multifonds DB Column is CMON_IMPOT. |
| 39 | `FS.GA.DEPOSIT.TAX.AMOUNT` | `FsGaDeposit_TaxAmount` | TField |  | Tax Amount Multifonds DB Column is MNT_IMPOT_DEV. |
| 40 | `FS.GA.DEPOSIT.EXCHANGE.RATE.BETWEEN.CCY` | `FsGaDeposit_ExchangeRateBetweenCcy` | TField |  | Exchange rate between settlement currency and tax currency Multifonds DB Column is TCHG_IMPOT. |
| 41 | `FS.GA.DEPOSIT.MANAGER.ID` | `FsGaDeposit_ManagerId` | TField |  | Manager ID Multifonds DB Column is NACC_MNGR. |
| 42 | `FS.GA.DEPOSIT.MANAGER.CODE` | `FsGaDeposit_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 43 | `FS.GA.DEPOSIT.TRANSACTION.FEES` | `FsGaDeposit_TransactionFees` | TField |  | Transaction fees Multifonds DB Column is FLAG_TR_FEES. |
| 44 | `FS.GA.DEPOSIT.COMMISSION.FEE.AMOUNT` | `FsGaDeposit_CommissionFeeAmount` | TField |  | Commision amount for Pool increase or decrease transaction Multifonds DB Column is MNT_TR_FEES. |
| 45 | `FS.GA.DEPOSIT.CURRENCY.CODE.FOR.COMMISSION` | `FsGaDeposit_CurrencyCodeForCommission` | TField |  | Currency code for commission for Pool increase or decrease transaction Multifonds DB Column is CMON_TR_FEES. |
| 46 | `FS.GA.DEPOSIT.SHARE.CLASS.CODE` | `FsGaDeposit_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 47 | `FS.GA.DEPOSIT.REDEMPTION.DATE.SECURITY` | `FsGaDeposit_RedemptionDateSecurity` | TField |  | Generally the redemption date for bonds and deposits Multifonds DB Column is DATE_REMB. |
| 48 | `FS.GA.DEPOSIT.SPREAD.IDENTIFIER` | `FsGaDeposit_SpreadIdentifier` | TField |  | Specify the spread percentage to be considered for NAV charges per fund. Multifonds DB Column is SPREAD. |
| 49 | `FS.GA.DEPOSIT.INCOME.TYPE` | `FsGaDeposit_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 50 | `FS.GA.DEPOSIT.STATUS.PENDING` | `FsGaDeposit_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 51 | `FS.GA.DEPOSIT.MATURITY.REPAYMENT.PRICE` | `FsGaDeposit_MaturityRepaymentPrice` | TField |  | The price at which an instruments if matured Multifonds DB Column is COURS_REMB. |
| 52 | `FS.GA.DEPOSIT.SWITCH.DATE` | `FsGaDeposit_SwitchDate` | TField |  | The switch date will be automatically calculated by the system (maturity date of the FET deal A a a switch days) Multifonds DB Column is DVAL_SWITCH. |
| 53 | `FS.GA.DEPOSIT.SWITCH.RATE` | `FsGaDeposit_SwitchRate` | TField |  | This field is used for the &apos;MKTM&apos; deposit valuation method Multifonds DB Column is COURS_OLD_NAV. |
| 54 | `FS.GA.DEPOSIT.EXTERNAL.REFERENCE` | `FsGaDeposit_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 55 | `FS.GA.DEPOSIT.MATURITY.CODE.FOR.DEPOSIT` | `FsGaDeposit_MaturityCodeForDeposit` | TField |  | Maturity code for deposit Multifonds DB Column is MATCODE. |
| 56 | `FS.GA.DEPOSIT.FUND.INTEREST.CALCULATION` | `FsGaDeposit_FundInterestCalculation` | TField |  | Fund Interest Calculation Multifonds DB Column is MINT_PTF_CALC. |
| 57 | `FS.GA.DEPOSIT.DEAL.INTEREST.CALCULATION` | `FsGaDeposit_DealInterestCalculation` | TField |  | Deal Interest Calcualtion Multifonds DB Column is MINT_DEAL_CALC. |
| 58 | `FS.GA.DEPOSIT.FEE.SETTLEMENT` | `FsGaDeposit_FeeSettlement` | TField |  | Fee Settlement Multifonds DB Column is MFRAIS_SETTLE. |
| 59 | `FS.GA.DEPOSIT.REPO.CALL.COVERAGE` | `FsGaDeposit_RepoCallCoverage` | TField |  | The minimum percentage rate required for repo collateral should be definable at fund level. A positive percentage rate should be entered. Multifonds DB Column is PCT_REPO_COVERAGE. |
| 60 | `FS.GA.DEPOSIT.INTERNAL.SECURITY.ID` | `FsGaDeposit_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 61 | `FS.GA.DEPOSIT.INVESTMENT.CURRENCY` | `FsGaDeposit_InvestmentCurrency` | TField |  | Local ccy for securities, Transaction ccy for non securitised instruments Multifonds DB Column is NOVAL_CODMON. |
| 62 | `FS.GA.DEPOSIT.MARKET.PRICE` | `FsGaDeposit_MarketPrice` | TField |  | Market price for NAV Multifonds DB Column is COURSVAL. |
| 63 | `FS.GA.DEPOSIT.QUANTITY` | `FsGaDeposit_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 64 | `FS.GA.DEPOSIT.MARKET.VALUE.IN.BOOK.CURRENCY` | `FsGaDeposit_MarketValueInBookCurrency` | TField |  | Market Value in Book Currency Multifonds DB Column is MNT_ACT. |
| 65 | `FS.GA.DEPOSIT.ACCRUED.INTEREST.COLLATERAL` | `FsGaDeposit_AccruedInterestCollateral` | TField |  | Displayed by the system in case of bonds. It is computed from the last coupon date of the collateral security to the accounting date on which the collateral is attached to the counterparty. Multifonds DB Column is MNT_INT_ACR. |
| 66 | `FS.GA.DEPOSIT.TOTAL.VALUE.COLLATERAL` | `FsGaDeposit_TotalValueCollateral` | TField |  | Total value of the collateral attached to security lending or deposit contract,i.e. sm of Market Value and the interest accruals. Multifonds DB Column is MNT_TOTAL. |
| 67 | `FS.GA.DEPOSIT.PERCENT.COVERED` | `FsGaDeposit_PercentCovered` | TField |  | This fields represents market value of the security lent / Market value of the security collateralized Multifonds DB Column is PCT_COVERED. |
| 68 | `FS.GA.DEPOSIT.TOTAL.AMOUNT.OF.DEPOSIT` | `FsGaDeposit_TotalAmountOfDeposit` | TField |  | Total amount of deposit in deposit currency including fees Multifonds DB Column is MONTANT_TOTAL. |
| 69 | `FS.GA.DEPOSIT.WITHOLDING.TAX.PERCENTAGE` | `FsGaDeposit_WitholdingTaxPercentage` | TField |  | The &apos;Withholding tax %&apos; field is defined with a default tax rate to be applied to deposit transactions if a tax rate is not setup for deposit transaction operation codes taxes. Multifonds DB Column is PCT_IMPOT. |
| 70 | `FS.GA.DEPOSIT.EXECUTION.TIMESTAMP` | `FsGaDeposit_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 71 | `FS.GA.DEPOSIT.CONFIRMED` | `FsGaDeposit_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 72 | `FS.GA.DEPOSIT.CONFIRMATION.DATE` | `FsGaDeposit_ConfirmationDate` | TField |  | Confirmation Date Multifonds DB Column is CONFIRM_DATE. |
| 73 | `FS.GA.DEPOSIT.FUND.STRATEGY` | `FsGaDeposit_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 74 | `FS.GA.DEPOSIT.FUND.LINK.ID` | `FsGaDeposit_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 75 | `FS.GA.DEPOSIT.VALUATION.METHOD` | `FsGaDeposit_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 76 | `FS.GA.DEPOSIT.INTEREST.RATE.TYPE` | `FsGaDeposit_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 77 | `FS.GA.DEPOSIT.CHECK.DATE` | `FsGaDeposit_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 78 | `FS.GA.DEPOSIT.CHECKED.BY` | `FsGaDeposit_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 79 | `FS.GA.DEPOSIT.IFRS.TAG` | `FsGaDeposit_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 80 | `FS.GA.DEPOSIT.REPO.TYPE.CODE` | `FsGaDeposit_RepoTypeCode` | TField |  | The field which links to deal screen FDDEP01 and FDEMP02. The list of values is available through F9 in FDCBO01 screen which draws the repo type code from the new repo type definition screen FDRPO01. Multifonds DB Column is REPO_ID. |
| 81 | `FS.GA.DEPOSIT.QUOTATION.PLACE` | `FsGaDeposit_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 82 | `FS.GA.DEPOSIT.NUMB.OF.DAYS` | `FsGaDeposit_NumbOfDays` | TField |  | Number of day&apos;s between deposit&apos;s value date to maturity date, number of a fixed number of days or number of NAVs as at which fees will be accrued for. Multifonds DB Column is NB_JOURS. |
| 83 | `FS.GA.DEPOSIT.REPO.ID` | `FsGaDeposit_RepoId` | TField |  | This field displays Repo Id of the transaction Multifonds DB Column is REPO_SEC_ID. |
| 84 | `FS.GA.DEPOSIT.AMOUNT.IN.DEPOSIT` | `FsGaDeposit_AmountInDeposit` | TField |  | Amount in Deposit. Multifonds DB Column is MONTANT_DPO_3DEC. |
| 85 | `FS.GA.DEPOSIT.AMOUNT.AT.CREATION` | `FsGaDeposit_AmountAtCreation` | TField |  | Amount at Creation. Multifonds DB Column is MONTANT_CREATE_3DEC. |
| 86 | `FS.GA.DEPOSIT.DEPOSIT.AMOUNT.3.DECIMAL` | `FsGaDeposit_DepositAmount3Decimal` | TField |  | Deposit Amount 3 Decimal. Multifonds DB Column is MNT_DEP_CORR_3DEC. |
| 87 | `FS.GA.DEPOSIT.REPRISE.CURRENCY` | `FsGaDeposit_RepriseCurrency` | TField |  | Currency Multifonds DB Column is CMON_REPRISE. |
| 88 | `FS.GA.DEPOSIT.PREVIOUS.CODE.STATUS` | `FsGaDeposit_PreviousCodeStatus` | TField |  | Previous Code Status Multifonds DB Column is PRV_CSTATUS. |
| 89 | `FS.GA.DEPOSIT.ACCOUNTING.METHOD` | `FsGaDeposit_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 90 | `FS.GA.DEPOSIT.DEPOSITORY.AMOUNT.IN.FUND` | `FsGaDeposit_DepositoryAmountInFund` | TField |  | Depository Amount In Fund Multifonds DB Column is MNT_DEP_PTF. |
| 91 | `FS.GA.DEPOSIT.INTEREST.AMOUNT.IN.FUND` | `FsGaDeposit_InterestAmountInFund` | TField |  | Interest Amount In Fund Multifonds DB Column is MINT_PTF. |
| 92 | `FS.GA.DEPOSIT.LOCAL.SETTLED.IN.FX.VCI` | `FsGaDeposit_LocalSettledInFxVci` | TField |  | Local Settled In FX VCI Multifonds DB Column is LOC_SETTL_FX_VCI. |
| 93 | `FS.GA.DEPOSIT.LOCAL.FUND.IN.FX.VCI` | `FsGaDeposit_LocalFundInFxVci` | TField |  | Local Fund In FX VCI Multifonds DB Column is LOC_PTF_FX_VCI. |
| 94 | `FS.GA.DEPOSIT.FUND.FX.SETTLEMENT.VCI` | `FsGaDeposit_FundFxSettlementVci` | TField |  | Settl Ptf Fx Vci Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 95 | `FS.GA.DEPOSIT.REPAY.OPERATOR.CODE` | `FsGaDeposit_RepayOperatorCode` | TField |  | Repay Operator Code Multifonds DB Column is REPAY_COPER. |
| 96 | `FS.GA.DEPOSIT.LOCAL.REPAYMENT.SETTLE.VCI` | `FsGaDeposit_LocalRepaymentSettleVci` | TField |  | Local Repayment Settle Vci Multifonds DB Column is REPAY_LOC_SETTL_VCI. |
| 97 | `FS.GA.DEPOSIT.REPAY.LOCAL.FUND.VCI` | `FsGaDeposit_RepayLocalFundVci` | TField |  | Repay Local Fund VCI Multifonds DB Column is REPAY_LOC_PTF_VCI. |
| 98 | `FS.GA.DEPOSIT.REPAY.FUND.SETTLED.VCI` | `FsGaDeposit_RepayFundSettledVci` | TField |  | Repay Fund Settled VCI Multifonds DB Column is REPAY_SETTL_PTF_VCI. |
| 99 | `FS.GA.DEPOSIT.FATCA.LIABILITY.DP` | `FsGaDeposit_FatcaLiabilityDp` | TField |  | FATCA Liability. Multifonds DB Column is FLG_FATCA_DP. |
| 100 | `FS.GA.DEPOSIT.FATCA.LIABILITY.PERCENTAGE` | `FsGaDeposit_FatcaLiabilityPercentage` | TField |  | FATCA Liability Percentage. Multifonds DB Column is PCT_FATCA_DP. |
| 101 | `FS.GA.DEPOSIT.INTEREST.AMOUNT.TAX.FATCA` | `FsGaDeposit_InterestAmountTaxFatca` | TField |  | Interest Amount Tax FATCA Multifonds DB Column is MINT_TAX_FATCA. |
| 102 | `FS.GA.DEPOSIT.MATURITY.TYPE` | `FsGaDeposit_MaturityType` | TField |  | Maturity Type. Multifonds DB Column is TYP_TERM. |
| 103 | `FS.GA.DEPOSIT.REVISION.CODE` | `FsGaDeposit_RevisionCode` | TField |  | Defined the calculation method for the rate defined in Int rate type&quot; and &quot;maturity&quot;&quot; Multifonds DB Column is REVISION_CODE. |
| 104 | `FS.GA.DEPOSIT.COLLATERAL.REUSE` | `FsGaDeposit_CollateralReuse` | TField |  | Flag to denote if the transaction is made out of a collateral position which was received Multifonds DB Column is FLG_COLL_REUSE. |
| 105 | `FS.GA.DEPOSIT.TAX.AMOUNT.IN.NATIVE.CCY` | `FsGaDeposit_TaxAmountInNativeCcy` | TField |  | Tax Amount In Native Ccy Multifonds DB Column is MNT_IMPOT_FCY. |
| 106 | `FS.GA.DEPOSIT.MANUAL.INTEREST.AMOUNT` | `FsGaDeposit_ManualInterestAmount` | TField |  | Manual Interest Amount Identifier Multifonds DB Column is FLG_MANUAL_MINT. |
| 107 | `FS.GA.DEPOSIT.FLOATING.RATE` | `FsGaDeposit_FloatingRate` | TField |  | Flag Floating Rate. Multifonds DB Column is FLG_FLOATING_RATE. |
| 108 | `FS.GA.DEPOSIT.MONTHLY.INTEREST.PAYMENT.IDENT` | `FsGaDeposit_MonthlyInterestPaymentIdent` | TField |  | Flag Monthly Interest Payment. Multifonds DB Column is FLG_MONTHLY_INT_PAY. |
| 109 | `FS.GA.DEPOSIT.SCALE` | `FsGaDeposit_Scale` | TField |  | Scale Code allows the user to create different types of scale of fee calculations. E.g, Defining the NAV changes, performance fee. Multifonds DB Column is SCALE_CODE. |
| 110 | `FS.GA.DEPOSIT.MONTHLY.INTEREST.PAY.DATE` | `FsGaDeposit_MonthlyInterestPayDate` | TField |  | Monthly Interest Pay Date Multifonds DB Column is DATE_MTH_INT_PAY. |
| 111 | `FS.GA.DEPOSIT.NEXT.COUPON.DATE` | `FsGaDeposit_NextCouponDate` | TField |  | Next Coupon Date Multifonds DB Column is NEXT_COUPON_DATE. |
| 112 | `FS.GA.DEPOSIT.DATE.OF.REPAYMENT` | `FsGaDeposit_DateOfRepayment` | TField |  | Date Of Repayment Multifonds DB Column is DREPAYMENT. |
| 113 | `FS.GA.DEPOSIT.REPAYMENT.INTEREST.AMOUNT` | `FsGaDeposit_RepaymentInterestAmount` | TField |  | Repayment Interest Amount Multifonds DB Column is MINT_REPAYMENT. |
| 114 | `FS.GA.DEPOSIT.REPAY.INTEREST.RATE` | `FsGaDeposit_RepayInterestRate` | TField |  | Repay Interest Rate Multifonds DB Column is REPAY_INT_RATE. |
| 115 | `FS.GA.DEPOSIT.REMAIN.INTEREST.AMOUNT` | `FsGaDeposit_RemainInterestAmount` | TField |  | Remain Interest Amount Multifonds DB Column is MINT_REMAIN. |
| 116 | `FS.GA.DEPOSIT.EXTERNAL.CONTRACT.NUMBER` | `FsGaDeposit_ExternalContractNumber` | TField |  | External Contract Number Multifonds DB Column is NCONTRAT_EXT. |
| 117 | `FS.GA.DEPOSIT.UTI.DESCRIPTION` | `FsGaDeposit_UtiDescription` | TField |  | UTI Description Multifonds DB Column is UTI_DESC. |
| 118 | `FS.GA.DEPOSIT.USI.DESCRIPTION` | `FsGaDeposit_UsiDescription` | TField |  | USI Description Multifonds DB Column is USI_DESC. |
| 119 | `FS.GA.DEPOSIT.MONTHLY.INTEREST.PAYMENT` | `FsGaDeposit_MonthlyInterestPayment` | TField |  | Monthly Interest Payment Multifonds DB Column is MTH_INT_PAY. |
| 120 | `FS.GA.DEPOSIT.PREVIOUS.REPAYMENT.ENTRY.NUM` | `FsGaDeposit_PreviousRepaymentEntryNum` | TField |  | Previous Repayment Entry Number Multifonds DB Column is PREV_NECRITUR_REMB. |
| 121 | `FS.GA.DEPOSIT.TRADE.ID` | `FsGaDeposit_TradeId` | TField |  | Trade Id Multifonds DB Column is TRADEID. |
| 122 | `FS.GA.DEPOSIT.KNOWLEDGE.DATE` | `FsGaDeposit_KnowledgeDate` | TField |  | Knowledge Date Multifonds DB Column is KNOWLEDGEDATE. |
| 123 | `FS.GA.DEPOSIT.INSTRUMENT.ID.CODE` | `FsGaDeposit_InstrumentIdCode` | TField |  | This field displays instrument code Multifonds DB Column is INSTRUMENTCODE. |
| 124 | `FS.GA.DEPOSIT.ACCOUNT.NUMBER.MIGRATION` | `FsGaDeposit_AccountNumberMigration` | TField |  | Account Number Migration Multifonds DB Column is NRUBR_MIG. |
| 125 | `FS.GA.DEPOSIT.SUFFIX.NUMBER.MIGRATION` | `FsGaDeposit_SuffixNumberMigration` | TField |  | Suffix Number Migration Multifonds DB Column is NSUFF_MIG. |
| 126 | `FS.GA.DEPOSIT.MIGRATION` | `FsGaDeposit_Migration` | TField |  | Flag Migration. Multifonds DB Column is FLG_MIG. |
| 127 | `FS.GA.DEPOSIT.OPERATION.TYPE` | `FsGaDeposit_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 128 | `FS.GA.DEPOSIT.RESERVED10` | `FsGaDeposit_Reserved10` | TField |  |  |
| 129 | `FS.GA.DEPOSIT.RESERVED9` | `FsGaDeposit_Reserved9` | TField |  |  |
| 130 | `FS.GA.DEPOSIT.RESERVED8` | `FsGaDeposit_Reserved8` | TField |  |  |
| 131 | `FS.GA.DEPOSIT.RESERVED7` | `FsGaDeposit_Reserved7` | TField |  |  |
| 132 | `FS.GA.DEPOSIT.RESERVED6` | `FsGaDeposit_Reserved6` | TField |  |  |
| 133 | `FS.GA.DEPOSIT.RESERVED5` | `FsGaDeposit_Reserved5` | TField |  |  |
| 134 | `FS.GA.DEPOSIT.RESERVED4` | `FsGaDeposit_Reserved4` | TField |  |  |
| 135 | `FS.GA.DEPOSIT.RESERVED3` | `FsGaDeposit_Reserved3` | TField |  |  |
| 136 | `FS.GA.DEPOSIT.RESERVED2` | `FsGaDeposit_Reserved2` | TField |  |  |
| 137 | `FS.GA.DEPOSIT.RESERVED1` | `FsGaDeposit_Reserved1` | TField |  |  |
| 138 | `FS.GA.DEPOSIT.LOCAL.REF` | `FsGaDeposit_LocalRef` |  |  |  |
| 139 | `FS.GA.DEPOSIT.OVERRIDE` | `FsGaDeposit_Override` |  |  |  |
| 140 | `FS.GA.DEPOSIT.RECORD.STATUS` | `FsGaDeposit_RecordStatus` | String |  |  |
| 141 | `FS.GA.DEPOSIT.CURR.NO` | `FsGaDeposit_CurrNo` | String |  |  |
| 142 | `FS.GA.DEPOSIT.INPUTTER` | `FsGaDeposit_Inputter` |  |  |  |
| 143 | `FS.GA.DEPOSIT.DATE.TIME` | `FsGaDeposit_DateTime` |  |  |  |
| 144 | `FS.GA.DEPOSIT.AUTHORISER` | `FsGaDeposit_Authoriser` | String |  |  |
| 145 | `FS.GA.DEPOSIT.CO.CODE` | `FsGaDeposit_CoCode` | String |  |  |
| 146 | `FS.GA.DEPOSIT.DEPT.CODE` | `FsGaDeposit_DeptCode` | String |  |  |
| 147 | `FS.GA.DEPOSIT.AUDITOR.CODE` | `FsGaDeposit_AuditorCode` | String |  |  |
| 148 | `FS.GA.DEPOSIT.AUDIT.DATE.TIME` | `FsGaDeposit_AuditDateTime` | String |  |  |
