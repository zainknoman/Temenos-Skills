# FS.GA.FORWARD.CONTRACT — Table Schema

> Source: `INSERTS/I_F.FS.GA.FORWARD.CONTRACT` in `FS_Forex.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FORWARD.CONTRACT.PARENT.REF.ID` | `FsGaForwardContract_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FORWARD.CONTRACT.ORA.ROWID` | `FsGaForwardContract_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FORWARD.CONTRACT.FUND.ID` | `FsGaForwardContract_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FORWARD.CONTRACT.SERVICE.CODE` | `FsGaForwardContract_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.FORWARD.CONTRACT.LOT.NUMBER` | `FsGaForwardContract_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 6 | `FS.GA.FORWARD.CONTRACT.GL.ACCOUNT` | `FsGaForwardContract_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 7 | `FS.GA.FORWARD.CONTRACT.GL.ACCOUNT.SUFFIX` | `FsGaForwardContract_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 8 | `FS.GA.FORWARD.CONTRACT.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaForwardContract_TradeOrValueOrAccDate` | TField |  | Input Trade date or Value date or accounting date. Depends on the feature that is used Multifonds DB Column is DCTA. |
| 9 | `FS.GA.FORWARD.CONTRACT.SETTLE.DATE` | `FsGaForwardContract_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 10 | `FS.GA.FORWARD.CONTRACT.PAY.DATE` | `FsGaForwardContract_PayDate` | TField |  | Pay Date Multifonds DB Column is DVAL. |
| 11 | `FS.GA.FORWARD.CONTRACT.RATE.OF.EXCHANGE` | `FsGaForwardContract_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 12 | `FS.GA.FORWARD.CONTRACT.CURRENCY.BOUGHT` | `FsGaForwardContract_CurrencyBought` | TField |  | Purchased Currency Multifonds DB Column is CDEV_ACHAT. |
| 13 | `FS.GA.FORWARD.CONTRACT.SOLD.CURRENCY` | `FsGaForwardContract_SoldCurrency` | TField |  | Sold Currency Multifonds DB Column is CDEV_VENTE. |
| 14 | `FS.GA.FORWARD.CONTRACT.AMOUNT.BOUGHT` | `FsGaForwardContract_AmountBought` | TField |  | The amount of currency purchased Multifonds DB Column is MONTANT_ACHAT. |
| 15 | `FS.GA.FORWARD.CONTRACT.AMOUNT.SOLD` | `FsGaForwardContract_AmountSold` | TField |  | The amount of currency Sold Multifonds DB Column is MONTANT_VENTE. |
| 16 | `FS.GA.FORWARD.CONTRACT.OPERATION.CODE` | `FsGaForwardContract_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 17 | `FS.GA.FORWARD.CONTRACT.TRANSACTION.NUMBER` | `FsGaForwardContract_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 18 | `FS.GA.FORWARD.CONTRACT.ENTRY.NUMBER.REPAYMENT` | `FsGaForwardContract_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 19 | `FS.GA.FORWARD.CONTRACT.DEAL.STATUS.CODE` | `FsGaForwardContract_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 20 | `FS.GA.FORWARD.CONTRACT.FOREX.PURCHASE.ACCOUNT.NUMBER` | `FsGaForwardContract_ForexPurchaseAccountNumber` | TField |  | By default MultiFonds selects the cash account number that has been attached to the correspondentA a a s record in the central register file. Multifonds DB Column is NRUBR_ACHAT. |
| 21 | `FS.GA.FORWARD.CONTRACT.PURCHASE.SUFFIX.NUMBER` | `FsGaForwardContract_PurchaseSuffixNumber` | TField |  | MultiFonds selects the suffix number that has been defined with the cash account attached to the correspondentA a a s record in the central register file. The use may change the suffix, if required. Multifonds DB Column is NSUFF_ACHAT. |
| 22 | `FS.GA.FORWARD.CONTRACT.FOREX.SALE.ACCOUNT.NUMBER` | `FsGaForwardContract_ForexSaleAccountNumber` | TField |  | By default MultiFonds selects the cash account number that has been attached to the correspondentA a a s record in the central register file. Multifonds DB Column is NRUBR_VENTE. |
| 23 | `FS.GA.FORWARD.CONTRACT.SALE.SUFFIX.NUMBER` | `FsGaForwardContract_SaleSuffixNumber` | TField |  | MultiFonds selects the suffix number that has been defined with the cash account attached to the correspondentA a a s record in the central register file. The use may change the suffix, if required. Multifonds DB Column is NSUFF_VENTE. |
| 24 | `FS.GA.FORWARD.CONTRACT.CORRESPONDENT` | `FsGaForwardContract_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 25 | `FS.GA.FORWARD.CONTRACT.FEES.AT.CREATION` | `FsGaForwardContract_FeesAtCreation` | TField |  | Enter fees at creation, if required Multifonds DB Column is MFRAIS_CREAT. |
| 26 | `FS.GA.FORWARD.CONTRACT.FEES.AT.MATURITY` | `FsGaForwardContract_FeesAtMaturity` | TField |  | Enter any fees to be charged at maturity, if required Multifonds DB Column is MFRAIS_REMB. |
| 27 | `FS.GA.FORWARD.CONTRACT.LONG.DESC` | `FsGaForwardContract_LongDesc` | TField |  | This represents description of a report, export type, language name etc Multifonds DB Column is LIBELLE. |
| 28 | `FS.GA.FORWARD.CONTRACT.SWITCH.EXCHANGE.RATE` | `FsGaForwardContract_SwitchExchangeRate` | TField |  | Pertains to the spot part exchange rate in a exchange swap Multifonds DB Column is TCHG_SWITCH. |
| 29 | `FS.GA.FORWARD.CONTRACT.PURCHASE.AMOUNT.SWITCH` | `FsGaForwardContract_PurchaseAmountSwitch` | TField |  | Purchase Amount Switch Multifonds DB Column is MONTANT_ACHAT_SWITCH. |
| 30 | `FS.GA.FORWARD.CONTRACT.AMORTISE.AMOUNT` | `FsGaForwardContract_AmortiseAmount` | TField |  | Amortization. amount of the corresponding deal Multifonds DB Column is MONTANT_VENTE_SWITCH. |
| 31 | `FS.GA.FORWARD.CONTRACT.PURCHASE.ACCOUNT.NUMBER.SWITCH` | `FsGaForwardContract_PurchaseAccountNumberSwitch` | TField |  | Purchase Account Number Switch Multifonds DB Column is NRUBR_ACHAT_SWITCH. |
| 32 | `FS.GA.FORWARD.CONTRACT.PURCHASE.SUFFIX.NUMBER.SWITCH` | `FsGaForwardContract_PurchaseSuffixNumberSwitch` | TField |  | Purchase Suffix Number Switch Multifonds DB Column is NSUFF_ACHAT_SWITCH. |
| 33 | `FS.GA.FORWARD.CONTRACT.SALE.ACCOUNT.NUMBER.SWITCH` | `FsGaForwardContract_SaleAccountNumberSwitch` | TField |  | Sale Account Number Switch Multifonds DB Column is NRUBR_VENTE_SWITCH. |
| 34 | `FS.GA.FORWARD.CONTRACT.SALE.SUFFIX.NUMBER.SWITCH` | `FsGaForwardContract_SaleSuffixNumberSwitch` | TField |  | Sale Suffix Number Switch Multifonds DB Column is NSUFF_VENTE_SWITCH. |
| 35 | `FS.GA.FORWARD.CONTRACT.ARCHIVE` | `FsGaForwardContract_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 36 | `FS.GA.FORWARD.CONTRACT.COUNTERPARTY.CORRESPONDENT` | `FsGaForwardContract_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 37 | `FS.GA.FORWARD.CONTRACT.HEDGING.OR.TRADING.CATEGORY` | `FsGaForwardContract_HedgingOrTradingCategory` | TField |  | Hedging or Trading Category Multifonds DB Column is CD_HEDG. |
| 38 | `FS.GA.FORWARD.CONTRACT.MANAGER.ID` | `FsGaForwardContract_ManagerId` | TField |  | Manager ID Multifonds DB Column is NACC_MNGR. |
| 39 | `FS.GA.FORWARD.CONTRACT.SHARE.CLASS.CODE` | `FsGaForwardContract_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 40 | `FS.GA.FORWARD.CONTRACT.MANAGER.CODE` | `FsGaForwardContract_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 41 | `FS.GA.FORWARD.CONTRACT.SALE.CORRESPONDENT` | `FsGaForwardContract_SaleCorrespondent` | TField |  | Enter a correspondent number. The amount of currency sold will be cleared over the bank account held with the correspondent bank. Multifonds DB Column is NCORRESP_2. |
| 42 | `FS.GA.FORWARD.CONTRACT.ACCOUNT.2` | `FsGaForwardContract_Account2` | TField |  | Account 2 Multifonds DB Column is NRUBR_2. |
| 43 | `FS.GA.FORWARD.CONTRACT.SUFFIX.2` | `FsGaForwardContract_Suffix2` | TField |  | Correspondent Sale Suffix number Multifonds DB Column is NSUFF_2. |
| 44 | `FS.GA.FORWARD.CONTRACT.MATURITY.EXCHANGE.RATE` | `FsGaForwardContract_MaturityExchangeRate` | TField |  | Maturity Exchange Rate Multifonds DB Column is TCHG_CLOSING. |
| 45 | `FS.GA.FORWARD.CONTRACT.PROFIT.OR.LOSS.AMT.IN.FUND.CCY` | `FsGaForwardContract_ProfitOrLossAmtInFundCcy` | TField |  | Will be filled by the system (e.g. in case of corporate actions) Multifonds DB Column is MNT_GP_PTF. |
| 46 | `FS.GA.FORWARD.CONTRACT.VALUATION.METHOD` | `FsGaForwardContract_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 47 | `FS.GA.FORWARD.CONTRACT.STATUS.PENDING` | `FsGaForwardContract_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 48 | `FS.GA.FORWARD.CONTRACT.SWITCH.DATE` | `FsGaForwardContract_SwitchDate` | TField |  | The switch date will be automatically calculated by the system (maturity date of the FET deal A a a switch days) Multifonds DB Column is DVAL_SWITCH. |
| 49 | `FS.GA.FORWARD.CONTRACT.QUOTATION.TYPE` | `FsGaForwardContract_QuotationType` | TField |  | Quatation Type Multifonds DB Column is CTYPE. |
| 50 | `FS.GA.FORWARD.CONTRACT.CONTRACT.LINK` | `FsGaForwardContract_ContractLink` | TField |  | Contract Link Multifonds DB Column is NCONTRAT_LINK. |
| 51 | `FS.GA.FORWARD.CONTRACT.FORWARD.VALUATION.METHOD` | `FsGaForwardContract_ForwardValuationMethod` | TField |  | This field allows user to define the default Valuation Method for Forwards Multifonds DB Column is CEVAL_FX. |
| 52 | `FS.GA.FORWARD.CONTRACT.FUND.GAIN.LOSS.AMOUNT.CLOSED` | `FsGaForwardContract_FundGainLossAmountClosed` | TField |  | Fund Gain Loss Amount Closed Multifonds DB Column is MNT_GP_PTF_CLOSED. |
| 53 | `FS.GA.FORWARD.CONTRACT.EXTERNAL.REFERENCE` | `FsGaForwardContract_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 54 | `FS.GA.FORWARD.CONTRACT.CLOSED` | `FsGaForwardContract_Closed` | TField |  | Closed Multifonds DB Column is FLG_CLOSED. |
| 55 | `FS.GA.FORWARD.CONTRACT.REPORT.DEPORT.CURRENCY` | `FsGaForwardContract_ReportDeportCurrency` | TField |  | Report/Deport Currency Multifonds DB Column is RD_CMON. |
| 56 | `FS.GA.FORWARD.CONTRACT.REPORT.DEPORT.EXCHANGE.RATE` | `FsGaForwardContract_ReportDeportExchangeRate` | TField |  | Exchange rate corresponds to report or deport Multifonds DB Column is RD_TCHG. |
| 57 | `FS.GA.FORWARD.CONTRACT.REPORT.OR.DEPORT.AMOUNT` | `FsGaForwardContract_ReportOrDeportAmount` | TField |  | Report or Deport Amount Multifonds DB Column is RD_AMOUNT. |
| 58 | `FS.GA.FORWARD.CONTRACT.AMORTISEMENT.AMOUNT` | `FsGaForwardContract_AmortisementAmount` | TField |  | Amortisement Amount Multifonds DB Column is RD_RESULT. |
| 59 | `FS.GA.FORWARD.CONTRACT.REPORT.OR.DEPORT.ACCOUNT.DB` | `FsGaForwardContract_ReportOrDeportAccountDb` | TField |  | Report Or Deport Account DB Multifonds DB Column is RD_NRUBR_DB. |
| 60 | `FS.GA.FORWARD.CONTRACT.REPORT.OR.DEPORT.SUFFIX.DB` | `FsGaForwardContract_ReportOrDeportSuffixDb` | TField |  | Report Or Deport Suffix DB Multifonds DB Column is RD_NSUFF_DB. |
| 61 | `FS.GA.FORWARD.CONTRACT.REPORT.OR.DEPORT.ACCOUNT.CR` | `FsGaForwardContract_ReportOrDeportAccountCr` | TField |  | Report Or Deport Account CR Multifonds DB Column is RD_NRUBR_CR. |
| 62 | `FS.GA.FORWARD.CONTRACT.REPORT.OR.DEPORT.SUFFIX.CR` | `FsGaForwardContract_ReportOrDeportSuffixCr` | TField |  | Report Or Deport Suffix CR Multifonds DB Column is RD_NSUFF_CR. |
| 63 | `FS.GA.FORWARD.CONTRACT.REBALANCE` | `FsGaForwardContract_Rebalance` | TField |  | Rebalance Flag Multifonds DB Column is FLG_REBALANCE. |
| 64 | `FS.GA.FORWARD.CONTRACT.EXECUTION.TIMESTAMP` | `FsGaForwardContract_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 65 | `FS.GA.FORWARD.CONTRACT.CONFIRMED` | `FsGaForwardContract_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 66 | `FS.GA.FORWARD.CONTRACT.CONFIRMATION.DATE` | `FsGaForwardContract_ConfirmationDate` | TField |  | Confirmation Date Multifonds DB Column is CONFIRM_DATE. |
| 67 | `FS.GA.FORWARD.CONTRACT.FUND.STRATEGY` | `FsGaForwardContract_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 68 | `FS.GA.FORWARD.CONTRACT.FUND.LINK.ID` | `FsGaForwardContract_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 69 | `FS.GA.FORWARD.CONTRACT.NDF` | `FsGaForwardContract_Ndf` | TField |  | NDF Flag Multifonds DB Column is FLG_NDF. |
| 70 | `FS.GA.FORWARD.CONTRACT.PURCHASE.AMOUNT.CLOSED` | `FsGaForwardContract_PurchaseAmountClosed` | TField |  | Purchase Amount Closed Multifonds DB Column is MNT_ACHAT_CLOSED. |
| 71 | `FS.GA.FORWARD.CONTRACT.CHECK.DATE` | `FsGaForwardContract_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 72 | `FS.GA.FORWARD.CONTRACT.CHECKED.BY` | `FsGaForwardContract_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 73 | `FS.GA.FORWARD.CONTRACT.IFRS.TAG` | `FsGaForwardContract_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 74 | `FS.GA.FORWARD.CONTRACT.IFRS.CATEGORY` | `FsGaForwardContract_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 75 | `FS.GA.FORWARD.CONTRACT.PURCHASE.CURRENCY.AMOUNT` | `FsGaForwardContract_PurchaseCurrencyAmount` | TField |  | Purchase Currency Amount Multifonds DB Column is MONTANT_ACHAT_3DEC. |
| 76 | `FS.GA.FORWARD.CONTRACT.SALE.CURRENCY.AMOUNT` | `FsGaForwardContract_SaleCurrencyAmount` | TField |  | Sale Currency Amount Multifonds DB Column is MONTANT_VENTE_3DEC. |
| 77 | `FS.GA.FORWARD.CONTRACT.PURCHASE.CCY.AMOUNT.SWITCH` | `FsGaForwardContract_PurchaseCcyAmountSwitch` | TField |  | Purchase Ccy Amount Switch Multifonds DB Column is MONTANT_ACHAT_SWITCH_3DEC. |
| 78 | `FS.GA.FORWARD.CONTRACT.SALE.CURRENCY.AMOUNT.SWITCH` | `FsGaForwardContract_SaleCurrencyAmountSwitch` | TField |  | Sale Currency Amount Switch Multifonds DB Column is MONTANT_VENTE_SWITCH_3DEC. |
| 79 | `FS.GA.FORWARD.CONTRACT.RECEIVABLE.ACCOUNT.ON.MATURITY` | `FsGaForwardContract_ReceivableAccountOnMaturity` | TField |  | The account to be used for receivable amount at the time of repayment of forward fx contracts Multifonds DB Column is NRUBR_DB_MAT. |
| 80 | `FS.GA.FORWARD.CONTRACT.PAYABLE.ACCOUNT.ON.MATURITY` | `FsGaForwardContract_PayableAccountOnMaturity` | TField |  | The account to be used for payable amount at the time of repayment of forward fx contracts Multifonds DB Column is NRUBR_CR_MAT. |
| 81 | `FS.GA.FORWARD.CONTRACT.BUY.SELL.EXCHANGE.RATE.VCI` | `FsGaForwardContract_BuySellExchangeRateVci` | TField |  | Buy Sell Exchange Rate VCI Multifonds DB Column is BUY_SELL_TCHG_VCI. |
| 82 | `FS.GA.FORWARD.CONTRACT.BUY.FUND.EXCHANGE.RATE.VCI` | `FsGaForwardContract_BuyFundExchangeRateVci` | TField |  | Buy Fund Exchange Rate VCI Multifonds DB Column is BUY_PTF_TCHG_VCI. |
| 83 | `FS.GA.FORWARD.CONTRACT.SELL.FUND.EXCHANGE.RATE.VCI` | `FsGaForwardContract_SellFundExchangeRateVci` | TField |  | Sell Fund Exchange Rate VCI Multifonds DB Column is SELL_PTF_TCHG_VCI. |
| 84 | `FS.GA.FORWARD.CONTRACT.REPAY.BUY.SELL.EXCHANGE.RATE` | `FsGaForwardContract_RepayBuySellExchangeRate` | TField |  | Repay Buy Sell Exchange Rate Multifonds DB Column is REPAY_BUY_SELL_TCHG_VCI. |
| 85 | `FS.GA.FORWARD.CONTRACT.REPAY.BUY.FUND.EXCHANGE.RATE` | `FsGaForwardContract_RepayBuyFundExchangeRate` | TField |  | Repay Buy Fund Exchange Rate Multifonds DB Column is REPAY_BUY_PTF_TCHG_VCI. |
| 86 | `FS.GA.FORWARD.CONTRACT.REPAY.SELL.FUND.EXCHANGE.RATE` | `FsGaForwardContract_RepaySellFundExchangeRate` | TField |  | Repay Sell Fund Exchange Rate Multifonds DB Column is REPAY_SELL_PTF_TCHG_VCI. |
| 87 | `FS.GA.FORWARD.CONTRACT.PREVIOUS.STATUS.CODE` | `FsGaForwardContract_PreviousStatusCode` | TField |  | Previous Status Code Multifonds DB Column is PREV_CSTATUS. |
| 88 | `FS.GA.FORWARD.CONTRACT.AMORTISATION` | `FsGaForwardContract_Amortisation` | TField |  | Flag Amortization Multifonds DB Column is FLG_AMORT. |
| 89 | `FS.GA.FORWARD.CONTRACT.PROFIT.AND.LOSS.AMOUNT` | `FsGaForwardContract_ProfitAndLossAmount` | TField |  | P&amp;L amount can be initialized for securities/futures/options Multifonds DB Column is MNT_GP. |
| 90 | `FS.GA.FORWARD.CONTRACT.FUND.GAIN.LOSS.AMOUNT.REL` | `FsGaForwardContract_FundGainLossAmountRel` | TField |  | Fund Gain Loss Amount REL Multifonds DB Column is MNT_GP_PTF_REL. |
| 91 | `FS.GA.FORWARD.CONTRACT.EXTERNAL.CONTRACT.NUMBER` | `FsGaForwardContract_ExternalContractNumber` | TField |  | External Contract Number Multifonds DB Column is NCONTRAT_EXT. |
| 92 | `FS.GA.FORWARD.CONTRACT.UTI.DESCRIPTION` | `FsGaForwardContract_UtiDescription` | TField |  | UTI Description Multifonds DB Column is UTI_DESC. |
| 93 | `FS.GA.FORWARD.CONTRACT.USI.DESCRIPTION` | `FsGaForwardContract_UsiDescription` | TField |  | USI Description Multifonds DB Column is USI_DESC. |
| 94 | `FS.GA.FORWARD.CONTRACT.OPERATION.TYPE` | `FsGaForwardContract_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 95 | `FS.GA.FORWARD.CONTRACT.RESERVED10` | `FsGaForwardContract_Reserved10` | TField |  |  |
| 96 | `FS.GA.FORWARD.CONTRACT.RESERVED9` | `FsGaForwardContract_Reserved9` | TField |  |  |
| 97 | `FS.GA.FORWARD.CONTRACT.RESERVED8` | `FsGaForwardContract_Reserved8` | TField |  |  |
| 98 | `FS.GA.FORWARD.CONTRACT.RESERVED7` | `FsGaForwardContract_Reserved7` | TField |  |  |
| 99 | `FS.GA.FORWARD.CONTRACT.RESERVED6` | `FsGaForwardContract_Reserved6` | TField |  |  |
| 100 | `FS.GA.FORWARD.CONTRACT.RESERVED5` | `FsGaForwardContract_Reserved5` | TField |  |  |
| 101 | `FS.GA.FORWARD.CONTRACT.RESERVED4` | `FsGaForwardContract_Reserved4` | TField |  |  |
| 102 | `FS.GA.FORWARD.CONTRACT.RESERVED3` | `FsGaForwardContract_Reserved3` | TField |  |  |
| 103 | `FS.GA.FORWARD.CONTRACT.RESERVED2` | `FsGaForwardContract_Reserved2` | TField |  |  |
| 104 | `FS.GA.FORWARD.CONTRACT.RESERVED1` | `FsGaForwardContract_Reserved1` | TField |  |  |
| 105 | `FS.GA.FORWARD.CONTRACT.LOCAL.REF` | `FsGaForwardContract_LocalRef` |  |  |  |
| 106 | `FS.GA.FORWARD.CONTRACT.OVERRIDE` | `FsGaForwardContract_Override` |  |  |  |
| 107 | `FS.GA.FORWARD.CONTRACT.RECORD.STATUS` | `FsGaForwardContract_RecordStatus` | String |  |  |
| 108 | `FS.GA.FORWARD.CONTRACT.CURR.NO` | `FsGaForwardContract_CurrNo` | String |  |  |
| 109 | `FS.GA.FORWARD.CONTRACT.INPUTTER` | `FsGaForwardContract_Inputter` |  |  |  |
| 110 | `FS.GA.FORWARD.CONTRACT.DATE.TIME` | `FsGaForwardContract_DateTime` |  |  |  |
| 111 | `FS.GA.FORWARD.CONTRACT.AUTHORISER` | `FsGaForwardContract_Authoriser` | String |  |  |
| 112 | `FS.GA.FORWARD.CONTRACT.CO.CODE` | `FsGaForwardContract_CoCode` | String |  |  |
| 113 | `FS.GA.FORWARD.CONTRACT.DEPT.CODE` | `FsGaForwardContract_DeptCode` | String |  |  |
| 114 | `FS.GA.FORWARD.CONTRACT.AUDITOR.CODE` | `FsGaForwardContract_AuditorCode` | String |  |  |
| 115 | `FS.GA.FORWARD.CONTRACT.AUDIT.DATE.TIME` | `FsGaForwardContract_AuditDateTime` | String |  |  |
