# FS.GA.SHAREHOLDER.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.SHAREHOLDER.TRANSACTION` in `FS_Capstock.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SHAREHOLDER.TRANSACTION.PARENT.REF.ID` | `FsGaShareholderTransaction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SHAREHOLDER.TRANSACTION.ORA.ROWID` | `FsGaShareholderTransaction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SHAREHOLDER.TRANSACTION.SHAREHOLDER` | `FsGaShareholderTransaction_Shareholder` | TField |  | Share holder against whom the share class units are lodged. Multifonds DB Column is NACTIONNAIRE. |
| 4 | `FS.GA.SHAREHOLDER.TRANSACTION.FUND.ID` | `FsGaShareholderTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 5 | `FS.GA.SHAREHOLDER.TRANSACTION.STATUS.PENDING` | `FsGaShareholderTransaction_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 6 | `FS.GA.SHAREHOLDER.TRANSACTION.DEAL.STATUS.CODE` | `FsGaShareholderTransaction_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 7 | `FS.GA.SHAREHOLDER.TRANSACTION.OPERATION.CODE` | `FsGaShareholderTransaction_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 8 | `FS.GA.SHAREHOLDER.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaShareholderTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 9 | `FS.GA.SHAREHOLDER.TRANSACTION.GROSS.AMOUNT` | `FsGaShareholderTransaction_GrossAmount` | TField |  | Gross amount of the transaction which is quantity multiplied by price Multifonds DB Column is MONTANT_BRUT. |
| 10 | `FS.GA.SHAREHOLDER.TRANSACTION.GROSS.AMOUNT.PER.SHARE` | `FsGaShareholderTransaction_GrossAmountPerShare` | TField |  | Gross Amount Per Share Multifonds DB Column is MNT_BRUT_SHARE. |
| 11 | `FS.GA.SHAREHOLDER.TRANSACTION.CAPITAL.GAIN.PER.SHARE` | `FsGaShareholderTransaction_CapitalGainPerShare` | TField |  | Capital Gain Per Share Multifonds DB Column is GAIN_CAP_PART. |
| 12 | `FS.GA.SHAREHOLDER.TRANSACTION.GL.CAPITAL.GAIN.PER.SHARE` | `FsGaShareholderTransaction_GlCapitalGainPerShare` | TField |  | GL Capital Gain Per Share Multifonds DB Column is GAIN_CAP_GL_PART. |
| 13 | `FS.GA.SHAREHOLDER.TRANSACTION.MM.FUND` | `FsGaShareholderTransaction_MmFund` | TField |  | MM Fund Multifonds DB Column is NPTF_MM. |
| 14 | `FS.GA.SHAREHOLDER.TRANSACTION.SHARE.CLASS.CODE` | `FsGaShareholderTransaction_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 15 | `FS.GA.SHAREHOLDER.TRANSACTION.INTERNAL.TRANSACTION.ENTRY.NUM` | `FsGaShareholderTransaction_InternalTransactionEntryNum` | TField |  | This is the internal entry number for a transaction. Multifonds DB Column is NECRITURE. |
| 16 | `FS.GA.SHAREHOLDER.TRANSACTION.CORRESPONDENT` | `FsGaShareholderTransaction_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 17 | `FS.GA.SHAREHOLDER.TRANSACTION.GL.ACCOUNT` | `FsGaShareholderTransaction_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 18 | `FS.GA.SHAREHOLDER.TRANSACTION.GL.ACCOUNT.SUFFIX` | `FsGaShareholderTransaction_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 19 | `FS.GA.SHAREHOLDER.TRANSACTION.SETTLE.DATE` | `FsGaShareholderTransaction_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 20 | `FS.GA.SHAREHOLDER.TRANSACTION.AMOUNT.UNIT` | `FsGaShareholderTransaction_AmountUnit` | TField |  | This is the unit amount for distribution of dividend or tax figures. Multifonds DB Column is MNT_UNIT. |
| 21 | `FS.GA.SHAREHOLDER.TRANSACTION.QUANTITY` | `FsGaShareholderTransaction_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 22 | `FS.GA.SHAREHOLDER.TRANSACTION.NET.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaShareholderTransaction_NetAmountInLocalCurrency` | TField |  | Net amount of transaction Multifonds DB Column is MONTANT_NET. |
| 23 | `FS.GA.SHAREHOLDER.TRANSACTION.DEAL.FEES.AMOUNT` | `FsGaShareholderTransaction_DealFeesAmount` | TField |  | Deal Fees Amount Multifonds DB Column is MFRAIS. |
| 24 | `FS.GA.SHAREHOLDER.TRANSACTION.TRIGGER.ACCOUNTING` | `FsGaShareholderTransaction_TriggerAccounting` | TField |  | This is to trigger the accounting of the capital transaction. If unchecked only the units are considered but there is no impact on capital and cash ( in case of migration) Multifonds DB Column is COMPT. |
| 25 | `FS.GA.SHAREHOLDER.TRANSACTION.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaShareholderTransaction_TradeOrValueOrAccDate` | TField |  | Input Trade date or Value date or accounting date. Depends on the feature that is used Multifonds DB Column is DCTA. |
| 26 | `FS.GA.SHAREHOLDER.TRANSACTION.OFFICER` | `FsGaShareholderTransaction_Officer` | TField |  | Person who made the transaction. Multifonds DB Column is AC_OFFICER. |
| 27 | `FS.GA.SHAREHOLDER.TRANSACTION.INTRODUCER` | `FsGaShareholderTransaction_Introducer` | TField |  | Person who introduced the holder for the transaction. Multifonds DB Column is INTRODUCER. |
| 28 | `FS.GA.SHAREHOLDER.TRANSACTION.IMPRIMER` | `FsGaShareholderTransaction_Imprimer` | TField |  | Imprimer Multifonds DB Column is IMPRIMER. |
| 29 | `FS.GA.SHAREHOLDER.TRANSACTION.NET.AMOUNT.IN.SETTLEMENT.CCY` | `FsGaShareholderTransaction_NetAmountInSettlementCcy` | TField |  | Net amount of settlement as part of the transaction Multifonds DB Column is MNT_NET_CORR. |
| 30 | `FS.GA.SHAREHOLDER.TRANSACTION.RATE.OF.EXCHANGE` | `FsGaShareholderTransaction_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 31 | `FS.GA.SHAREHOLDER.TRANSACTION.SETTLEMENT.CURRENCY` | `FsGaShareholderTransaction_SettlementCurrency` | TField |  | Currency in which the settlement would be processed. Multifonds DB Column is CMON_CORR. |
| 32 | `FS.GA.SHAREHOLDER.TRANSACTION.FORCE.AMOUNT` | `FsGaShareholderTransaction_ForceAmount` | TField |  | This is to fore the subscription amount to be different to the calculated amount. Multifonds DB Column is MNT_IMPOSE. |
| 33 | `FS.GA.SHAREHOLDER.TRANSACTION.IMP.REVERSE` | `FsGaShareholderTransaction_ImpReverse` | TField |  | Imp Reverse Multifonds DB Column is IMP_REVERSE. |
| 34 | `FS.GA.SHAREHOLDER.TRANSACTION.REVERSAL.DATE` | `FsGaShareholderTransaction_ReversalDate` | TField |  | Reversal Date Multifonds DB Column is DEXT. |
| 35 | `FS.GA.SHAREHOLDER.TRANSACTION.FUND.SWITCH` | `FsGaShareholderTransaction_FundSwitch` | TField |  | Nptf Switch Multifonds DB Column is NPTF_SWITCH. |
| 36 | `FS.GA.SHAREHOLDER.TRANSACTION.TPARTS.SWITCH` | `FsGaShareholderTransaction_TpartsSwitch` | TField |  | Tparts Switch Multifonds DB Column is TPARTS_SWITCH. |
| 37 | `FS.GA.SHAREHOLDER.TRANSACTION.NACT.SWITCH` | `FsGaShareholderTransaction_NactSwitch` | TField |  | Nact Switch Multifonds DB Column is NACT_SWITCH. |
| 38 | `FS.GA.SHAREHOLDER.TRANSACTION.ENTRY.NUMBER.SWITCH` | `FsGaShareholderTransaction_EntryNumberSwitch` | TField |  | Necriture Switch Multifonds DB Column is NECRITURE_SWITCH. |
| 39 | `FS.GA.SHAREHOLDER.TRANSACTION.TRADE.DATE` | `FsGaShareholderTransaction_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 40 | `FS.GA.SHAREHOLDER.TRANSACTION.ARCHIVE` | `FsGaShareholderTransaction_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 41 | `FS.GA.SHAREHOLDER.TRANSACTION.DESCRIPTION` | `FsGaShareholderTransaction_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 42 | `FS.GA.SHAREHOLDER.TRANSACTION.NET.INCOME.AMOUNT` | `FsGaShareholderTransaction_NetIncomeAmount` | TField |  | Net Income Amount Multifonds DB Column is RNI. |
| 43 | `FS.GA.SHAREHOLDER.TRANSACTION.INTERIM.PROFIT` | `FsGaShareholderTransaction_InterimProfit` | TField |  | Interim profit amount while transacting on a target fund. Multifonds DB Column is ZWIST. |
| 44 | `FS.GA.SHAREHOLDER.TRANSACTION.CAPITAL.GAIN.AMOUNT` | `FsGaShareholderTransaction_CapitalGainAmount` | TField |  | Capital Gain Amount Multifonds DB Column is GAIN_CAP. |
| 45 | `FS.GA.SHAREHOLDER.TRANSACTION.SUBSCRIPTION.COMMISSION` | `FsGaShareholderTransaction_SubscriptionCommission` | TField |  | Comm Sub Multifonds DB Column is COMM_SUB. |
| 46 | `FS.GA.SHAREHOLDER.TRANSACTION.REDEMPTION.COMMISSION` | `FsGaShareholderTransaction_RedemptionCommission` | TField |  | Comm Red Multifonds DB Column is COMM_RED. |
| 47 | `FS.GA.SHAREHOLDER.TRANSACTION.ROUNDING.DIFFERENCE` | `FsGaShareholderTransaction_RoundingDifference` | TField |  | Rounding Diff Multifonds DB Column is ROUNDING_DIFF. |
| 48 | `FS.GA.SHAREHOLDER.TRANSACTION.QUANTITY.RECALCULATE` | `FsGaShareholderTransaction_QuantityRecalculate` | TField |  | This is to enable/disable quantity recalculation in case of change in amount Multifonds DB Column is FLG_QUANTITE. |
| 49 | `FS.GA.SHAREHOLDER.TRANSACTION.EXCLUDE.EQUALISATION` | `FsGaShareholderTransaction_ExcludeEqualisation` | TField |  | This flag if enabled would exclude the the transaction from equalisation computation. Multifonds DB Column is CREPRISE. |
| 50 | `FS.GA.SHAREHOLDER.TRANSACTION.CAPSTOCK.PRICE.DATE` | `FsGaShareholderTransaction_CapstockPriceDate` | TField |  | This is the price date as of which the subscription/redemption price needs to be applied for the capstock. Multifonds DB Column is PRICE_DATE. |
| 51 | `FS.GA.SHAREHOLDER.TRANSACTION.SETTLEMENT.FRONT.END.LOAD` | `FsGaShareholderTransaction_SettlementFrontEndLoad` | TField |  | If flag is set on settl date the FEL (front-end load charge) comsn is automatically settled. If flag is not set only the shareholder amount is settled, the FEL comsn is stored in a transitory account. Multifonds DB Column is FLG_NET_SETTLE. |
| 52 | `FS.GA.SHAREHOLDER.TRANSACTION.NET.SETTLEMENT` | `FsGaShareholderTransaction_NetSettlement` | TField |  | This is a flag to trigger the net /gross settlement. Multifonds DB Column is MNT_NET_SETTLE. |
| 53 | `FS.GA.SHAREHOLDER.TRANSACTION.DISCOUNT.AMOUNT` | `FsGaShareholderTransaction_DiscountAmount` | TField |  | This is the discount amount offered to a unit holder Multifonds DB Column is MNT_DISCOUNT. |
| 54 | `FS.GA.SHAREHOLDER.TRANSACTION.AMOUNT.AFTER.DISCOUNT` | `FsGaShareholderTransaction_AmountAfterDiscount` | TField |  | This is the subscription amount after netting out the discount. Multifonds DB Column is MNT_AF_DISCOUNT. |
| 55 | `FS.GA.SHAREHOLDER.TRANSACTION.ACCUMULATED.INCOME` | `FsGaShareholderTransaction_AccumulatedIncome` | TField |  | Accumulated Income Multifonds DB Column is MSOLDE_ACC_INC. |
| 56 | `FS.GA.SHAREHOLDER.TRANSACTION.ACC.BONUS.SHARE` | `FsGaShareholderTransaction_AccBonusShare` | TField |  | Acc Bonus Share Multifonds DB Column is MSOLDE_BONUS. |
| 57 | `FS.GA.SHAREHOLDER.TRANSACTION.ACC.CAPITAL.GAIN.LOSS` | `FsGaShareholderTransaction_AccCapitalGainLoss` | TField |  | Acc Capital Gain Loss Multifonds DB Column is GAIN_CAP_GL. |
| 58 | `FS.GA.SHAREHOLDER.TRANSACTION.INCOME.EQUALISATION.PER.UNIT` | `FsGaShareholderTransaction_IncomeEqualisationPerUnit` | TField |  | Income Equalisation Per Unit Multifonds DB Column is RNI_PART. |
| 59 | `FS.GA.SHAREHOLDER.TRANSACTION.ACCUMULATED.INCOME.PER.UNIT` | `FsGaShareholderTransaction_AccumulatedIncomePerUnit` | TField |  | Accumulated Income Per Unit Multifonds DB Column is MSOLDE_ACC_INC_PART. |
| 60 | `FS.GA.SHAREHOLDER.TRANSACTION.ACCUMULATED.BONUS.SHARE` | `FsGaShareholderTransaction_AccumulatedBonusShare` | TField |  | Accumulated Bonus Share Multifonds DB Column is MSOLDE_BONUS_PART. |
| 61 | `FS.GA.SHAREHOLDER.TRANSACTION.INTERIM.PROFIT.PER.UNIT` | `FsGaShareholderTransaction_InterimProfitPerUnit` | TField |  | Interim Profit Per Unit Multifonds DB Column is ZWIST_PART. |
| 62 | `FS.GA.SHAREHOLDER.TRANSACTION.RETRO.COMMISSION.AMOUNT` | `FsGaShareholderTransaction_RetroCommissionAmount` | TField |  | Retro Commission Amount Multifonds DB Column is RETRO_MNT. |
| 63 | `FS.GA.SHAREHOLDER.TRANSACTION.PENDING.SHARES` | `FsGaShareholderTransaction_PendingShares` | TField |  | This is to enable processing of pending capstock ransactions Multifonds DB Column is FLG_PENDING_SHARES. |
| 64 | `FS.GA.SHAREHOLDER.TRANSACTION.FX.TRANSAC.REFERENCE.NO` | `FsGaShareholderTransaction_FxTransacReferenceNo` | TField |  | Linking the spot FX transaction to the subscription when the pool and sub fund currency are different in advanced pooling. Multifonds DB Column is NUM_REP_LINK. |
| 65 | `FS.GA.SHAREHOLDER.TRANSACTION.MANAGER.CODE` | `FsGaShareholderTransaction_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 66 | `FS.GA.SHAREHOLDER.TRANSACTION.SHARE.CURRENCY.CODE` | `FsGaShareholderTransaction_ShareCurrencyCode` | TField |  | Share Currency Code Multifonds DB Column is SHARE_CCY. |
| 67 | `FS.GA.SHAREHOLDER.TRANSACTION.SHARE.PRICE` | `FsGaShareholderTransaction_SharePrice` | TField |  | Share Price Multifonds DB Column is SHARE_PRICE. |
| 68 | `FS.GA.SHAREHOLDER.TRANSACTION.PRICE.BEFORE.SWING` | `FsGaShareholderTransaction_PriceBeforeSwing` | TField |  | Indicates the capstock price before the swing is applied Multifonds DB Column is MNT_UNIT_BF_SWING. |
| 69 | `FS.GA.SHAREHOLDER.TRANSACTION.CHECK.DATE` | `FsGaShareholderTransaction_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 70 | `FS.GA.SHAREHOLDER.TRANSACTION.CHECKED.BY` | `FsGaShareholderTransaction_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 71 | `FS.GA.SHAREHOLDER.TRANSACTION.RETRO.COMMISSION.CURRENCY` | `FsGaShareholderTransaction_RetroCommissionCurrency` | TField |  | Retro Commission Currency Multifonds DB Column is RETRO_CCY. |
| 72 | `FS.GA.SHAREHOLDER.TRANSACTION.KOREAN.TAXABLE.NAV.PER.SHARE` | `FsGaShareholderTransaction_KoreanTaxableNavPerShare` | TField |  | Korean Taxable NAV Per Share Multifonds DB Column is KR_TAX_PER_SHARE. |
| 73 | `FS.GA.SHAREHOLDER.TRANSACTION.KOREA.NONTAXABLE.NAV.PER.SHARE` | `FsGaShareholderTransaction_KoreaNontaxableNavPerShare` | TField |  | Korean Non-Taxable NAV Per Share Multifonds DB Column is KR_NTAX_PER_SHARE. |
| 74 | `FS.GA.SHAREHOLDER.TRANSACTION.REAL.EQUALISATION.AMOUNT` | `FsGaShareholderTransaction_RealEqualisationAmount` | TField |  | Mnt Real Eq Multifonds DB Column is MNT_REAL_EQ. |
| 75 | `FS.GA.SHAREHOLDER.TRANSACTION.PERFORMANCE.FEES` | `FsGaShareholderTransaction_PerformanceFees` | TField |  | Performance fees paid out on redemptions. Multifonds DB Column is PERF_FEES. |
| 76 | `FS.GA.SHAREHOLDER.TRANSACTION.EQUALISATION.CREDITS` | `FsGaShareholderTransaction_EqualisationCredits` | TField |  | Equalisation credits on account of performance fees due to incremental capstock transactions. Multifonds DB Column is EQUAL_CR. |
| 77 | `FS.GA.SHAREHOLDER.TRANSACTION.EXECUTION.TIMESTAMP` | `FsGaShareholderTransaction_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 78 | `FS.GA.SHAREHOLDER.TRANSACTION.TR.ACCOUNT.NUMBER` | `FsGaShareholderTransaction_TrAccountNumber` | TField |  | Nrubr Tr Multifonds DB Column is NRUBR_TR. |
| 79 | `FS.GA.SHAREHOLDER.TRANSACTION.FUND.FX.SETTLEMENT.VCI` | `FsGaShareholderTransaction_FundFxSettlementVci` | TField |  | Settl Ptf Fx Vci Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 80 | `FS.GA.SHAREHOLDER.TRANSACTION.MONTANT.BRUT.3DEC` | `FsGaShareholderTransaction_MontantBrut3dec` | TField |  | Montant Brut 3Dec Multifonds DB Column is MONTANT_BRUT_3DEC. |
| 81 | `FS.GA.SHAREHOLDER.TRANSACTION.MNT.DISCOUNT.3DEC` | `FsGaShareholderTransaction_MntDiscount3dec` | TField |  | Mnt Discount 3Dec Multifonds DB Column is MNT_DISCOUNT_3DEC. |
| 82 | `FS.GA.SHAREHOLDER.TRANSACTION.MNT.AF.DISCOUNT.3DEC` | `FsGaShareholderTransaction_MntAfDiscount3dec` | TField |  | Mnt Af Discount 3Dec Multifonds DB Column is MNT_AF_DISCOUNT_3DEC. |
| 83 | `FS.GA.SHAREHOLDER.TRANSACTION.MONTANT.NET.3DEC` | `FsGaShareholderTransaction_MontantNet3dec` | TField |  | Montant Net 3Dec Multifonds DB Column is MONTANT_NET_3DEC. |
| 84 | `FS.GA.SHAREHOLDER.TRANSACTION.MNT.NET.CORR.3DEC` | `FsGaShareholderTransaction_MntNetCorr3dec` | TField |  | Mnt Net Corr 3Dec Multifonds DB Column is MNT_NET_CORR_3DEC. |
| 85 | `FS.GA.SHAREHOLDER.TRANSACTION.NET.SETTLE` | `FsGaShareholderTransaction_NetSettle` | TField |  | If flag is set: on settlement date the FEL commission is automatically settled. If flag is not set: only the shareholder amount is settled, the FEL commission is stored in a transitory account. Multifonds DB Column is MNT_NET_SETTLE_3DEC. |
| 86 | `FS.GA.SHAREHOLDER.TRANSACTION.REPRISE.CURRENCY` | `FsGaShareholderTransaction_RepriseCurrency` | TField |  | Currency Multifonds DB Column is CMON_REPRISE. |
| 87 | `FS.GA.SHAREHOLDER.TRANSACTION.PRICE.IN.SHARE.CCY` | `FsGaShareholderTransaction_PriceInShareCcy` | TField |  | Price In Share Ccy Multifonds DB Column is SHARE_PRICE_CCY. |
| 88 | `FS.GA.SHAREHOLDER.TRANSACTION.CURRENCY.SHARE.PRICE` | `FsGaShareholderTransaction_CurrencySharePrice` | TField |  | Currency Share Price Multifonds DB Column is CMON_SHARE_PRICE. |
| 89 | `FS.GA.SHAREHOLDER.TRANSACTION.TOTAL.IN.SUB.RED.CCY2` | `FsGaShareholderTransaction_TotalInSubRedCcy2` | TField |  | Total In Sub Red Ccy2 Multifonds DB Column is MONTANT_NET_S. |
| 90 | `FS.GA.SHAREHOLDER.TRANSACTION.MULTILAYER.POOLING.DRILL` | `FsGaShareholderTransaction_MultilayerPoolingDrill` | TField |  | The flag to denote if an increase/decrease on pool units need to be impact other funds or only stanalone. Multifonds DB Column is FLG_AUTOUP_STANDALONE. |
| 91 | `FS.GA.SHAREHOLDER.TRANSACTION.UNSETTLED.N1` | `FsGaShareholderTransaction_UnsettledN1` | TField |  | Flg Unsettled N1 Multifonds DB Column is FLG_UNSETTLED_N1. |
| 92 | `FS.GA.SHAREHOLDER.TRANSACTION.TRADE.ID` | `FsGaShareholderTransaction_TradeId` | TField |  | Trade Id Multifonds DB Column is TRADEID. |
| 93 | `FS.GA.SHAREHOLDER.TRANSACTION.KNOWLEDGE.DATE` | `FsGaShareholderTransaction_KnowledgeDate` | TField |  | Knowledge Date Multifonds DB Column is KNOWLEDGEDATE. |
| 94 | `FS.GA.SHAREHOLDER.TRANSACTION.OPERATION.TYPE` | `FsGaShareholderTransaction_OperationType` | TField |  | Identifier for transaction operation type like reversal, rebooking, etc Multifonds DB Column is TYPE_OPERATION. |
| 95 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED10` | `FsGaShareholderTransaction_Reserved10` | TField |  |  |
| 96 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED9` | `FsGaShareholderTransaction_Reserved9` | TField |  |  |
| 97 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED8` | `FsGaShareholderTransaction_Reserved8` | TField |  |  |
| 98 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED7` | `FsGaShareholderTransaction_Reserved7` | TField |  |  |
| 99 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED6` | `FsGaShareholderTransaction_Reserved6` | TField |  |  |
| 100 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED5` | `FsGaShareholderTransaction_Reserved5` | TField |  |  |
| 101 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED4` | `FsGaShareholderTransaction_Reserved4` | TField |  |  |
| 102 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED3` | `FsGaShareholderTransaction_Reserved3` | TField |  |  |
| 103 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED2` | `FsGaShareholderTransaction_Reserved2` | TField |  |  |
| 104 | `FS.GA.SHAREHOLDER.TRANSACTION.RESERVED1` | `FsGaShareholderTransaction_Reserved1` | TField |  |  |
| 105 | `FS.GA.SHAREHOLDER.TRANSACTION.LOCAL.REF` | `FsGaShareholderTransaction_LocalRef` |  |  |  |
| 106 | `FS.GA.SHAREHOLDER.TRANSACTION.OVERRIDE` | `FsGaShareholderTransaction_Override` |  |  |  |
| 107 | `FS.GA.SHAREHOLDER.TRANSACTION.RECORD.STATUS` | `FsGaShareholderTransaction_RecordStatus` | String |  |  |
| 108 | `FS.GA.SHAREHOLDER.TRANSACTION.CURR.NO` | `FsGaShareholderTransaction_CurrNo` | String |  |  |
| 109 | `FS.GA.SHAREHOLDER.TRANSACTION.INPUTTER` | `FsGaShareholderTransaction_Inputter` |  |  |  |
| 110 | `FS.GA.SHAREHOLDER.TRANSACTION.DATE.TIME` | `FsGaShareholderTransaction_DateTime` |  |  |  |
| 111 | `FS.GA.SHAREHOLDER.TRANSACTION.AUTHORISER` | `FsGaShareholderTransaction_Authoriser` | String |  |  |
| 112 | `FS.GA.SHAREHOLDER.TRANSACTION.CO.CODE` | `FsGaShareholderTransaction_CoCode` | String |  |  |
| 113 | `FS.GA.SHAREHOLDER.TRANSACTION.DEPT.CODE` | `FsGaShareholderTransaction_DeptCode` | String |  |  |
| 114 | `FS.GA.SHAREHOLDER.TRANSACTION.AUDITOR.CODE` | `FsGaShareholderTransaction_AuditorCode` | String |  |  |
| 115 | `FS.GA.SHAREHOLDER.TRANSACTION.AUDIT.DATE.TIME` | `FsGaShareholderTransaction_AuditDateTime` | String |  |  |
