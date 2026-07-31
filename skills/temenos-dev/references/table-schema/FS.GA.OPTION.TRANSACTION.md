# FS.GA.OPTION.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPTION.TRANSACTION` in `FS_OptionTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPTION.TRANSACTION.PARENT.REF.ID` | `FsGaOptionTransaction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPTION.TRANSACTION.ORA.ROWID` | `FsGaOptionTransaction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPTION.TRANSACTION.FUND.ID` | `FsGaOptionTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.OPTION.TRANSACTION.TRANSACTION.NUMBER` | `FsGaOptionTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.OPTION.TRANSACTION.OPTION.ID` | `FsGaOptionTransaction_OptionId` | TField |  | Option Security ID Multifonds DB Column is NOPT. |
| 6 | `FS.GA.OPTION.TRANSACTION.LOT.NUMBER` | `FsGaOptionTransaction_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 7 | `FS.GA.OPTION.TRANSACTION.FUTURE.OPTION.TRANSACTION.TYPE` | `FsGaOptionTransaction_FutureOptionTransactionType` | TField |  | Represents Opening/Continuing/Closing transaction types for Futures &amp; Options Multifonds DB Column is TYP_TRAIT. |
| 8 | `FS.GA.OPTION.TRANSACTION.OPERATION.CODE` | `FsGaOptionTransaction_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 9 | `FS.GA.OPTION.TRANSACTION.DEAL.STATUS.CODE` | `FsGaOptionTransaction_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 10 | `FS.GA.OPTION.TRANSACTION.QUANTITY` | `FsGaOptionTransaction_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 11 | `FS.GA.OPTION.TRANSACTION.PREMIUM.AMOUNT` | `FsGaOptionTransaction_PremiumAmount` | TField |  | Premium Amount paid/received for Options &amp; Futures transactions Multifonds DB Column is PREMIUM. |
| 12 | `FS.GA.OPTION.TRANSACTION.GROSS.AMOUNT.OF.TRANSACTION` | `FsGaOptionTransaction_GrossAmountOfTransaction` | TField |  | Gross Amount of Transaction Multifonds DB Column is MNT_GROSS. |
| 13 | `FS.GA.OPTION.TRANSACTION.FEES.AMOUNT` | `FsGaOptionTransaction_FeesAmount` | TField |  | Transaction Fees Amount Multifonds DB Column is MNT_FEES. |
| 14 | `FS.GA.OPTION.TRANSACTION.NET.MNT` | `FsGaOptionTransaction_NetMnt` | TField |  | Net Mnt Multifonds DB Column is MNT_NET. |
| 15 | `FS.GA.OPTION.TRANSACTION.CORRESPONDENT` | `FsGaOptionTransaction_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 16 | `FS.GA.OPTION.TRANSACTION.GL.SETTLEMENT.ACCOUNT` | `FsGaOptionTransaction_GlSettlementAccount` | TField |  | GL Settlement Account Number Multifonds DB Column is NRUBR_CORR. |
| 17 | `FS.GA.OPTION.TRANSACTION.CORRESPONDENT.CASH.SUFFIX.NUM` | `FsGaOptionTransaction_CorrespondentCashSuffixNum` | TField |  | Correspondent Cash Suffix Number Multifonds DB Column is NSUFF_CORR. |
| 18 | `FS.GA.OPTION.TRANSACTION.SETTLEMENT.CURRENCY` | `FsGaOptionTransaction_SettlementCurrency` | TField |  | Currency in which the settlement would be processed. Multifonds DB Column is CMON_CORR. |
| 19 | `FS.GA.OPTION.TRANSACTION.EXCHANGE.RATE` | `FsGaOptionTransaction_ExchangeRate` | TField |  | Exchange rate between deal currency and settlement currency Multifonds DB Column is TCHG_CORR. |
| 20 | `FS.GA.OPTION.TRANSACTION.GROSS.AMOUNT.IN.SETTLEMENT.CCY` | `FsGaOptionTransaction_GrossAmountInSettlementCcy` | TField |  | Gross Amount In Settlement Ccy Multifonds DB Column is MNT_GROSS_CORR. |
| 21 | `FS.GA.OPTION.TRANSACTION.FEES.AMOUNT.IN.SETTLEMENT.CCY` | `FsGaOptionTransaction_FeesAmountInSettlementCcy` | TField |  | Fees Amount In Settlement Ccy Multifonds DB Column is MNT_FEES_CORR. |
| 22 | `FS.GA.OPTION.TRANSACTION.NET.AMOUNT.IN.SETTLEMENT.CCY` | `FsGaOptionTransaction_NetAmountInSettlementCcy` | TField |  | Net amount of settlement as part of the transaction Multifonds DB Column is MNT_NET_CORR. |
| 23 | `FS.GA.OPTION.TRANSACTION.SETTLE.DATE` | `FsGaOptionTransaction_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 24 | `FS.GA.OPTION.TRANSACTION.TRADE.DATE.OF.CONTRACT` | `FsGaOptionTransaction_TradeDateOfContract` | TField |  | Trade Date or Accounting Date for Contractual Instrument Multifonds DB Column is DATACC. |
| 25 | `FS.GA.OPTION.TRANSACTION.TRADE.DATE` | `FsGaOptionTransaction_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 26 | `FS.GA.OPTION.TRANSACTION.DESCRIPTION` | `FsGaOptionTransaction_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 27 | `FS.GA.OPTION.TRANSACTION.ENTRY.NUMBER.REPAYMENT` | `FsGaOptionTransaction_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 28 | `FS.GA.OPTION.TRANSACTION.ARCHIVE` | `FsGaOptionTransaction_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 29 | `FS.GA.OPTION.TRANSACTION.EXERCISED.QUANTITY` | `FsGaOptionTransaction_ExercisedQuantity` | TField |  | Exercised Quantity for Options Transactions Multifonds DB Column is QUANTITE_EXEC. |
| 30 | `FS.GA.OPTION.TRANSACTION.ENTRY.NUMBER.FOR.EXERCISE` | `FsGaOptionTransaction_EntryNumberForExercise` | TField |  | Entry Number For Exercise Multifonds DB Column is NECRITUR_EXEC. |
| 31 | `FS.GA.OPTION.TRANSACTION.MANAGER.CODE` | `FsGaOptionTransaction_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 32 | `FS.GA.OPTION.TRANSACTION.HEDGING.OR.TRADING.CATEGORY` | `FsGaOptionTransaction_HedgingOrTradingCategory` | TField |  | Hedging or Trading Category Multifonds DB Column is CD_HEDG. |
| 33 | `FS.GA.OPTION.TRANSACTION.AUTOMATIC.HIFO` | `FsGaOptionTransaction_AutomaticHifo` | TField |  | Automatic HIFO Multifonds DB Column is AUTO_HIFO. |
| 34 | `FS.GA.OPTION.TRANSACTION.STATUS.PENDING` | `FsGaOptionTransaction_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 35 | `FS.GA.OPTION.TRANSACTION.COUNTERPARTY.CORRESPONDENT` | `FsGaOptionTransaction_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 36 | `FS.GA.OPTION.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaOptionTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 37 | `FS.GA.OPTION.TRANSACTION.BLK` | `FsGaOptionTransaction_Blk` | TField |  | Flag BLK Multifonds DB Column is FLG_BLK. |
| 38 | `FS.GA.OPTION.TRANSACTION.MANUAL.LOT.SELECTION` | `FsGaOptionTransaction_ManualLotSelection` | TField |  | Flag to denote that the lots relieved have been manually selected Multifonds DB Column is FLG_MANUAL_LOT. |
| 39 | `FS.GA.OPTION.TRANSACTION.EXECUTION.TIMESTAMP` | `FsGaOptionTransaction_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 40 | `FS.GA.OPTION.TRANSACTION.VM.ACCOUNT` | `FsGaOptionTransaction_VmAccount` | TField |  | This is the default account used to book the variation margin on Futures Multifonds DB Column is NRUBR_VAR_MARG. |
| 41 | `FS.GA.OPTION.TRANSACTION.VARIATION.MARGIN.SUFFIX.NUMBER` | `FsGaOptionTransaction_VariationMarginSuffixNumber` | TField |  | To enter variation margin suffix number. Multifonds DB Column is NSUFF_VAR_MARG. |
| 42 | `FS.GA.OPTION.TRANSACTION.FUND.LINK.ID` | `FsGaOptionTransaction_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 43 | `FS.GA.OPTION.TRANSACTION.FUND.STRATEGY` | `FsGaOptionTransaction_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 44 | `FS.GA.OPTION.TRANSACTION.SHARE.CLASS.CODE` | `FsGaOptionTransaction_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 45 | `FS.GA.OPTION.TRANSACTION.COST.EXERCISED.OPT.IN.DEAL.CCY` | `FsGaOptionTransaction_CostExercisedOptInDealCcy` | TField |  | Cost Exercised Opt In Deal Ccy Multifonds DB Column is EXER_OPT_COST. |
| 46 | `FS.GA.OPTION.TRANSACTION.COST.EXERCISED.OPT.IN.FUND.CCY` | `FsGaOptionTransaction_CostExercisedOptInFundCcy` | TField |  | Cost Exercised Opt In Fund Ccy Multifonds DB Column is EXER_OPT_COST_PTF. |
| 47 | `FS.GA.OPTION.TRANSACTION.CHECK.DATE` | `FsGaOptionTransaction_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 48 | `FS.GA.OPTION.TRANSACTION.CHECKED.BY` | `FsGaOptionTransaction_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 49 | `FS.GA.OPTION.TRANSACTION.IFRS.TAG` | `FsGaOptionTransaction_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 50 | `FS.GA.OPTION.TRANSACTION.CONFIRMATION.DATE` | `FsGaOptionTransaction_ConfirmationDate` | TField |  | Confirmation Date Multifonds DB Column is CONFIRM_DATE. |
| 51 | `FS.GA.OPTION.TRANSACTION.EXTERNAL.CONTRACT.NUMBER` | `FsGaOptionTransaction_ExternalContractNumber` | TField |  | External Contract Number Multifonds DB Column is NCONTRAT_EXT. |
| 52 | `FS.GA.OPTION.TRANSACTION.CONFIRMED` | `FsGaOptionTransaction_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 53 | `FS.GA.OPTION.TRANSACTION.ACCOUNTING.METHOD` | `FsGaOptionTransaction_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 54 | `FS.GA.OPTION.TRANSACTION.DEAL.ACCOUNT.NUMBER` | `FsGaOptionTransaction_DealAccountNumber` | TField |  | Deal Account Number Multifonds DB Column is DEAL_NRUBR. |
| 55 | `FS.GA.OPTION.TRANSACTION.DEAL.SUFFIX.NUMBER` | `FsGaOptionTransaction_DealSuffixNumber` | TField |  | Deal Suffix Number Multifonds DB Column is DEAL_NSUFF. |
| 56 | `FS.GA.OPTION.TRANSACTION.TRANSITORY.ACCOUNT.NUMBER` | `FsGaOptionTransaction_TransitoryAccountNumber` | TField |  | Transitory Account Number Multifonds DB Column is TRANSITORY_NRUBR. |
| 57 | `FS.GA.OPTION.TRANSACTION.TRANSITORY.SUFFIX.NUMBER` | `FsGaOptionTransaction_TransitorySuffixNumber` | TField |  | Transitory Suffix Number Multifonds DB Column is TRANSITORY_NSUFF. |
| 58 | `FS.GA.OPTION.TRANSACTION.LOCAL.BOOK.VCI` | `FsGaOptionTransaction_LocalBookVci` | TField |  | Local Book VCI Multifonds DB Column is LOCALBOOK_VCI. |
| 59 | `FS.GA.OPTION.TRANSACTION.TRANSACTION.PAY.VCI` | `FsGaOptionTransaction_TransactionPayVci` | TField |  | Transaction Pay VCI Multifonds DB Column is TRANPAY_VCI. |
| 60 | `FS.GA.OPTION.TRANSACTION.PAY.BOOK.VCI` | `FsGaOptionTransaction_PayBookVci` | TField |  | Pay Book VCI Multifonds DB Column is PAYBOOK_VCI. |
| 61 | `FS.GA.OPTION.TRANSACTION.PROFIT.AND.LOSS.AMOUNT` | `FsGaOptionTransaction_ProfitAndLossAmount` | TField |  | P&amp;L amount can be initialized for securities/futures/options Multifonds DB Column is MNT_GP. |
| 62 | `FS.GA.OPTION.TRANSACTION.PROFIT.OR.LOSS.AMT.IN.FUND.CCY` | `FsGaOptionTransaction_ProfitOrLossAmtInFundCcy` | TField |  | Will be filled by the system (e.g. in case of corporate actions) Multifonds DB Column is MNT_GP_PTF. |
| 63 | `FS.GA.OPTION.TRANSACTION.GAIN.LOSS.AMOUNT.IN.FX` | `FsGaOptionTransaction_GainLossAmountInFx` | TField |  | Gain Loss Amount In FX Multifonds DB Column is MNT_GP_FX. |
| 64 | `FS.GA.OPTION.TRANSACTION.MARKET.PRICE` | `FsGaOptionTransaction_MarketPrice` | TField |  | Market price for NAV Multifonds DB Column is COURSVAL. |
| 65 | `FS.GA.OPTION.TRANSACTION.CASH.SETTLEMENT` | `FsGaOptionTransaction_CashSettlement` | TField |  | Cash Settlement Flag Multifonds DB Column is FLG_CASH_SET. |
| 66 | `FS.GA.OPTION.TRANSACTION.MODULE.IDENTIFIER` | `FsGaOptionTransaction_ModuleIdentifier` | TField |  | Module Multifonds DB Column is FLG_MODULE. |
| 67 | `FS.GA.OPTION.TRANSACTION.UTI.DESCRIPTION` | `FsGaOptionTransaction_UtiDescription` | TField |  | UTI Description Multifonds DB Column is UTI_DESC. |
| 68 | `FS.GA.OPTION.TRANSACTION.USI.DESCRIPTION` | `FsGaOptionTransaction_UsiDescription` | TField |  | USI Description Multifonds DB Column is USI_DESC. |
| 69 | `FS.GA.OPTION.TRANSACTION.GST.CLAIM.ID` | `FsGaOptionTransaction_GstClaimId` | TField |  | GST Claim ID Multifonds DB Column is GST_CLAIM_ID. |
| 70 | `FS.GA.OPTION.TRANSACTION.GST.UPDATED.DATE` | `FsGaOptionTransaction_GstUpdatedDate` | TField |  | GST Updated date Multifonds DB Column is GST_DUPDATED. |
| 71 | `FS.GA.OPTION.TRANSACTION.GST.UPDATED.BY` | `FsGaOptionTransaction_GstUpdatedBy` | TField |  | GST Updated By Multifonds DB Column is GST_UPDATED_BY. |
| 72 | `FS.GA.OPTION.TRANSACTION.GST.CONFIRMATION` | `FsGaOptionTransaction_GstConfirmation` | TField |  | GST Confirmation Multifonds DB Column is GST_CONFIRM. |
| 73 | `FS.GA.OPTION.TRANSACTION.RITC.FEES.AMOUNT` | `FsGaOptionTransaction_RitcFeesAmount` | TField |  | Reduced Input Tax Credit Fees Amount Multifonds DB Column is RITC_FEES. |
| 74 | `FS.GA.OPTION.TRANSACTION.FXOP.BASE.QUANTITY` | `FsGaOptionTransaction_FxopBaseQuantity` | TField |  | FXOP Base Quantity Multifonds DB Column is FXOP_BASE_QTY. |
| 75 | `FS.GA.OPTION.TRANSACTION.FXOP.QUOTE.QUANTITY` | `FsGaOptionTransaction_FxopQuoteQuantity` | TField |  | FXOP Quote Quantity Multifonds DB Column is FXOP_QUOTE_QTY. |
| 76 | `FS.GA.OPTION.TRANSACTION.UNDERLYING.RECEIVABLE` | `FsGaOptionTransaction_UnderlyingReceivable` | TField |  | Underlying Recievable Multifonds DB Column is TUNDER. |
| 77 | `FS.GA.OPTION.TRANSACTION.LOCAL.BOOK.CMON` | `FsGaOptionTransaction_LocalBookCmon` | TField |  | Local Book CMON Multifonds DB Column is LOCALBOOK_CMON. |
| 78 | `FS.GA.OPTION.TRANSACTION.LOCAL.BOOK.CMON.FX` | `FsGaOptionTransaction_LocalBookCmonFx` | TField |  | Local Book CMON FX Multifonds DB Column is LOCALBOOK_CMONFX. |
| 79 | `FS.GA.OPTION.TRANSACTION.FXOP.BASE.QUANTITY.IN.FUND` | `FsGaOptionTransaction_FxopBaseQuantityInFund` | TField |  | FXOP Base Quantity In Fund Multifonds DB Column is FXOP_BASE_QTY_PTF. |
| 80 | `FS.GA.OPTION.TRANSACTION.FXOP.QUOTE.QUANTITY.IN.FUND` | `FsGaOptionTransaction_FxopQuoteQuantityInFund` | TField |  | FXOP Quote Quantity In Fund Multifonds DB Column is FXOP_QUOTE_QTY_PTF. |
| 81 | `FS.GA.OPTION.TRANSACTION.LOCAL.NOTIONAL.COST.BASE` | `FsGaOptionTransaction_LocalNotionalCostBase` | TField |  | Local Notional Cost Base Multifonds DB Column is NA_LOCALNOTIONALCOST_BASE. |
| 82 | `FS.GA.OPTION.TRANSACTION.LOCAL.NOTIONAL.COST.QUOTE` | `FsGaOptionTransaction_LocalNotionalCostQuote` | TField |  | Local Notional Cost Quote Multifonds DB Column is NA_LOCALNOTIONALCOST_QUOTE. |
| 83 | `FS.GA.OPTION.TRANSACTION.BOOK.NOTIONAL.COST.BASE` | `FsGaOptionTransaction_BookNotionalCostBase` | TField |  | Book Notional Cost Base Multifonds DB Column is NA_BOOKNOTIONALCOST_BASE. |
| 84 | `FS.GA.OPTION.TRANSACTION.BOOK.NOTIONAL.COST.QUOTE` | `FsGaOptionTransaction_BookNotionalCostQuote` | TField |  | Book Notional Cost Quote Multifonds DB Column is NA_BOOKNOTIONALCOST_QUOTE. |
| 85 | `FS.GA.OPTION.TRANSACTION.GST.REVISED.CLAIM.ID` | `FsGaOptionTransaction_GstRevisedClaimId` | TField |  | GST Revised Claim ID Multifonds DB Column is GST_CLAIM_ID_REV. |
| 86 | `FS.GA.OPTION.TRANSACTION.GST.REVISED.UPDATED.BY` | `FsGaOptionTransaction_GstRevisedUpdatedBy` | TField |  | GST Revised Updated By Multifonds DB Column is GST_UPDATED_BY_REV. |
| 87 | `FS.GA.OPTION.TRANSACTION.GST.REVISED.UPDATED.DATE` | `FsGaOptionTransaction_GstRevisedUpdatedDate` | TField |  | GST Revised Updated Date Multifonds DB Column is GST_DUPDATED_REV. |
| 88 | `FS.GA.OPTION.TRANSACTION.ADJUSTMENT.FUND` | `FsGaOptionTransaction_AdjustmentFund` | TField |  | Adjustment Fund Multifonds DB Column is NPTF_ORIGIN. |
| 89 | `FS.GA.OPTION.TRANSACTION.CORRESPONDENT.ADJ.NUMBER` | `FsGaOptionTransaction_CorrespondentAdjNumber` | TField |  | Correspondent adj number Multifonds DB Column is NCORRESP_ADJ. |
| 90 | `FS.GA.OPTION.TRANSACTION.INTERPORT.TRADES` | `FsGaOptionTransaction_InterportTrades` | TField |  | Interport trades Multifonds DB Column is FLG_INTERPORT_TRADES. |
| 91 | `FS.GA.OPTION.TRANSACTION.OPERATION.TYPE` | `FsGaOptionTransaction_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 92 | `FS.GA.OPTION.TRANSACTION.RESERVED10` | `FsGaOptionTransaction_Reserved10` | TField |  |  |
| 93 | `FS.GA.OPTION.TRANSACTION.RESERVED9` | `FsGaOptionTransaction_Reserved9` | TField |  |  |
| 94 | `FS.GA.OPTION.TRANSACTION.RESERVED8` | `FsGaOptionTransaction_Reserved8` | TField |  |  |
| 95 | `FS.GA.OPTION.TRANSACTION.RESERVED7` | `FsGaOptionTransaction_Reserved7` | TField |  |  |
| 96 | `FS.GA.OPTION.TRANSACTION.RESERVED6` | `FsGaOptionTransaction_Reserved6` | TField |  |  |
| 97 | `FS.GA.OPTION.TRANSACTION.RESERVED5` | `FsGaOptionTransaction_Reserved5` | TField |  |  |
| 98 | `FS.GA.OPTION.TRANSACTION.RESERVED4` | `FsGaOptionTransaction_Reserved4` | TField |  |  |
| 99 | `FS.GA.OPTION.TRANSACTION.RESERVED3` | `FsGaOptionTransaction_Reserved3` | TField |  |  |
| 100 | `FS.GA.OPTION.TRANSACTION.RESERVED2` | `FsGaOptionTransaction_Reserved2` | TField |  |  |
| 101 | `FS.GA.OPTION.TRANSACTION.RESERVED1` | `FsGaOptionTransaction_Reserved1` | TField |  |  |
| 102 | `FS.GA.OPTION.TRANSACTION.LOCAL.REF` | `FsGaOptionTransaction_LocalRef` |  |  |  |
| 103 | `FS.GA.OPTION.TRANSACTION.OVERRIDE` | `FsGaOptionTransaction_Override` |  |  |  |
| 104 | `FS.GA.OPTION.TRANSACTION.RECORD.STATUS` | `FsGaOptionTransaction_RecordStatus` | String |  |  |
| 105 | `FS.GA.OPTION.TRANSACTION.CURR.NO` | `FsGaOptionTransaction_CurrNo` | String |  |  |
| 106 | `FS.GA.OPTION.TRANSACTION.INPUTTER` | `FsGaOptionTransaction_Inputter` |  |  |  |
| 107 | `FS.GA.OPTION.TRANSACTION.DATE.TIME` | `FsGaOptionTransaction_DateTime` |  |  |  |
| 108 | `FS.GA.OPTION.TRANSACTION.AUTHORISER` | `FsGaOptionTransaction_Authoriser` | String |  |  |
| 109 | `FS.GA.OPTION.TRANSACTION.CO.CODE` | `FsGaOptionTransaction_CoCode` | String |  |  |
| 110 | `FS.GA.OPTION.TRANSACTION.DEPT.CODE` | `FsGaOptionTransaction_DeptCode` | String |  |  |
| 111 | `FS.GA.OPTION.TRANSACTION.AUDITOR.CODE` | `FsGaOptionTransaction_AuditorCode` | String |  |  |
| 112 | `FS.GA.OPTION.TRANSACTION.AUDIT.DATE.TIME` | `FsGaOptionTransaction_AuditDateTime` | String |  |  |
