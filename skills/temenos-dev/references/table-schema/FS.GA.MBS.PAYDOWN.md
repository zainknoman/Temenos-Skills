# FS.GA.MBS.PAYDOWN — Table Schema

> Source: `INSERTS/I_F.FS.GA.MBS.PAYDOWN` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.MBS.PAYDOWN.PARENT.REF.ID` | `FsGaMbsPaydown_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.MBS.PAYDOWN.ORA.ROWID` | `FsGaMbsPaydown_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.MBS.PAYDOWN.PAYDOWN.SEQUENTIAL.NUMBER` | `FsGaMbsPaydown_PaydownSequentialNumber` | TField |  | Paydown Sequential Number Multifonds DB Column is NMBSPAYDOWN. |
| 4 | `FS.GA.MBS.PAYDOWN.FUND.ID` | `FsGaMbsPaydown_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 5 | `FS.GA.MBS.PAYDOWN.SERVICE.CODE` | `FsGaMbsPaydown_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.MBS.PAYDOWN.SETTLE.DATE` | `FsGaMbsPaydown_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 7 | `FS.GA.MBS.PAYDOWN.INTERNAL.SECURITY.ID` | `FsGaMbsPaydown_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 8 | `FS.GA.MBS.PAYDOWN.DEAL.STATUS.CODE` | `FsGaMbsPaydown_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 9 | `FS.GA.MBS.PAYDOWN.TRANSACTION.NUMBER` | `FsGaMbsPaydown_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 10 | `FS.GA.MBS.PAYDOWN.TRADE.DATE` | `FsGaMbsPaydown_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 11 | `FS.GA.MBS.PAYDOWN.ACCOUNTING.DATE` | `FsGaMbsPaydown_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 12 | `FS.GA.MBS.PAYDOWN.DESCRIPTION` | `FsGaMbsPaydown_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 13 | `FS.GA.MBS.PAYDOWN.INVESTMENT.FUND` | `FsGaMbsPaydown_InvestmentFund` | TField |  | Investment fund Multifonds DB Column is FINVEST. |
| 14 | `FS.GA.MBS.PAYDOWN.MANUAL.SETTLEMENT` | `FsGaMbsPaydown_ManualSettlement` | TField |  | Flag at deal level to override the contractual settlement specific to the deal. Multifonds DB Column is CSETTLE_MANU. |
| 15 | `FS.GA.MBS.PAYDOWN.QUOTATION.PLACE` | `FsGaMbsPaydown_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 16 | `FS.GA.MBS.PAYDOWN.OPERATION.CODE` | `FsGaMbsPaydown_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 17 | `FS.GA.MBS.PAYDOWN.LOT.NUMBER` | `FsGaMbsPaydown_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 18 | `FS.GA.MBS.PAYDOWN.CORRESPONDENT` | `FsGaMbsPaydown_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 19 | `FS.GA.MBS.PAYDOWN.CUSTODIAN` | `FsGaMbsPaydown_Custodian` | TField |  | Custodian where the units of the transaction would be lodged Multifonds DB Column is NDEPOSI. |
| 20 | `FS.GA.MBS.PAYDOWN.GL.ACCOUNT` | `FsGaMbsPaydown_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 21 | `FS.GA.MBS.PAYDOWN.GL.ACCOUNT.SUFFIX` | `FsGaMbsPaydown_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 22 | `FS.GA.MBS.PAYDOWN.LOCAL.CURRENCY` | `FsGaMbsPaydown_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 23 | `FS.GA.MBS.PAYDOWN.PREVIOUS.FACTOR.EFFECTIVE.DATE` | `FsGaMbsPaydown_PreviousFactorEffectiveDate` | TField |  | Effective Date of the previous factor. Used for Paydowns Multifonds DB Column is DATE_EFFECTIVE_PREC. |
| 24 | `FS.GA.MBS.PAYDOWN.PREVIOUS.FACTOR` | `FsGaMbsPaydown_PreviousFactor` | TField |  | Previous MBS factor Multifonds DB Column is FACTEUR_PREC. |
| 25 | `FS.GA.MBS.PAYDOWN.CURRENT.FACTOR.EFFECTIVE.DATE` | `FsGaMbsPaydown_CurrentFactorEffectiveDate` | TField |  | Effective date as selected in auto payment or manually input into trade date&quot;&quot; Multifonds DB Column is DATE_EFFECTIVE_ACTUEL. |
| 26 | `FS.GA.MBS.PAYDOWN.CURRENT.FACTOR` | `FsGaMbsPaydown_CurrentFactor` | TField |  | Retrieve from the factored instrument master. The current factor needs to be in definitive status&quot; and should be smaller than the previous factor&quot; Multifonds DB Column is FACTEUR_ACTUEL. |
| 27 | `FS.GA.MBS.PAYDOWN.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaMbsPaydown_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 28 | `FS.GA.MBS.PAYDOWN.RATE.OF.EXCHANGE` | `FsGaMbsPaydown_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 29 | `FS.GA.MBS.PAYDOWN.NET.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaMbsPaydown_NetAmountInLocalCurrency` | TField |  | Net amount of transaction Multifonds DB Column is MONTANT_NET. |
| 30 | `FS.GA.MBS.PAYDOWN.MBS.INTEREST.ADJUSTMENT.AMOUNT` | `FsGaMbsPaydown_MbsInterestAdjustmentAmount` | TField |  | Total difference in the accrued interest due to the application of the pay down (or due to the change in factor) Multifonds DB Column is MINT_AJUSTEMENT. |
| 31 | `FS.GA.MBS.PAYDOWN.FORWARD.AMOUNT` | `FsGaMbsPaydown_ForwardAmount` | TField |  | Forward Amount Multifonds DB Column is MNT_FORWARD. |
| 32 | `FS.GA.MBS.PAYDOWN.DAILY.AMORTISED.AMOUNT` | `FsGaMbsPaydown_DailyAmortisedAmount` | TField |  | Daily Amortised Amount Multifonds DB Column is MNT_DAILY_AMORTISED. |
| 33 | `FS.GA.MBS.PAYDOWN.AMOUNT.TO.AMORTISED` | `FsGaMbsPaydown_AmountToAmortised` | TField |  | Amount To Amortised Multifonds DB Column is MNT_TO_AMORTISE. |
| 34 | `FS.GA.MBS.PAYDOWN.REVISED.DAILY.AMORTISED` | `FsGaMbsPaydown_RevisedDailyAmortised` | TField |  | Revised Daily Amortised Multifonds DB Column is REVISED_DAILY_AMORT. |
| 35 | `FS.GA.MBS.PAYDOWN.AMOUNT.TO.CARRY` | `FsGaMbsPaydown_AmountToCarry` | TField |  | Amount To Carry Multifonds DB Column is MNT_TO_CARRY. |
| 36 | `FS.GA.MBS.PAYDOWN.GAIN.LOSS` | `FsGaMbsPaydown_GainLoss` | TField |  | Gain Loss Multifonds DB Column is GAIN_LOSS. |
| 37 | `FS.GA.MBS.PAYDOWN.ORIGINAL.FACE.VALUE.QUANTITY` | `FsGaMbsPaydown_OriginalFaceValueQuantity` | TField |  | Original face value of the position Multifonds DB Column is QTY_PREC. |
| 38 | `FS.GA.MBS.PAYDOWN.CURRENT.FACE.VALUE.QUANTITY` | `FsGaMbsPaydown_CurrentFaceValueQuantity` | TField |  | Current face value of the position Multifonds DB Column is QTY_ACTUEL. |
| 39 | `FS.GA.MBS.PAYDOWN.QUANTITY` | `FsGaMbsPaydown_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 40 | `FS.GA.MBS.PAYDOWN.MANAGER.CODE` | `FsGaMbsPaydown_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 41 | `FS.GA.MBS.PAYDOWN.ADJUSTED.ENTRY.NUMBER` | `FsGaMbsPaydown_AdjustedEntryNumber` | TField |  | Adjusted Entry Number Multifonds DB Column is NECRITUR_ADJ. |
| 42 | `FS.GA.MBS.PAYDOWN.STATUS.PENDING` | `FsGaMbsPaydown_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 43 | `FS.GA.MBS.PAYDOWN.ARCHIVE` | `FsGaMbsPaydown_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 44 | `FS.GA.MBS.PAYDOWN.INTEREST.AMOUNT.PREV.FACTOR` | `FsGaMbsPaydown_InterestAmountPrevFactor` | TField |  | Amount of accrued interest as stored with the previous NAV Multifonds DB Column is MINT_PREV. |
| 45 | `FS.GA.MBS.PAYDOWN.INTEREST.AMOUNT.NEW.FACTOR` | `FsGaMbsPaydown_InterestAmountNewFactor` | TField |  | Amount of accrued interest as calculated after the pay down processing (i.e. with the new factor) Multifonds DB Column is MINT_NEW. |
| 46 | `FS.GA.MBS.PAYDOWN.DATE.OF.NAV` | `FsGaMbsPaydown_DateOfNav` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 47 | `FS.GA.MBS.PAYDOWN.DATE.OF.PAYDOWN.INTEREST.ADJ` | `FsGaMbsPaydown_DateOfPaydownInterestAdj` | TField |  | Date of Interest adjustment for paydowns Multifonds DB Column is DATE_AS_PER. |
| 48 | `FS.GA.MBS.PAYDOWN.EXTERNAL.REFERENCE` | `FsGaMbsPaydown_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 49 | `FS.GA.MBS.PAYDOWN.COUNTERPARTY` | `FsGaMbsPaydown_Counterparty` | TField |  | Counterparty of the transaction Multifonds DB Column is NCORRESP_EXEC. |
| 50 | `FS.GA.MBS.PAYDOWN.FUND.STRATEGY` | `FsGaMbsPaydown_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 51 | `FS.GA.MBS.PAYDOWN.FUND.LINK.ID` | `FsGaMbsPaydown_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 52 | `FS.GA.MBS.PAYDOWN.AMORTISSMENT.AMOUNT` | `FsGaMbsPaydown_AmortissmentAmount` | TField |  | Amortissment Amount Multifonds DB Column is AMORTISSEMENT. |
| 53 | `FS.GA.MBS.PAYDOWN.FUND.AMORTISSEMENT.AMOUNT` | `FsGaMbsPaydown_FundAmortissementAmount` | TField |  | Fund Amortissement Amount Multifonds DB Column is AMORTISSEMENT_PTF. |
| 54 | `FS.GA.MBS.PAYDOWN.CHECK.DATE` | `FsGaMbsPaydown_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 55 | `FS.GA.MBS.PAYDOWN.CHECKED.BY` | `FsGaMbsPaydown_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 56 | `FS.GA.MBS.PAYDOWN.IFRS.TAG` | `FsGaMbsPaydown_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 57 | `FS.GA.MBS.PAYDOWN.ACCOUNTING.METHOD` | `FsGaMbsPaydown_AccountingMethod` | TField |  | This is the lot relieving methodology. Multifonds DB Column is CPT_METHOD. |
| 58 | `FS.GA.MBS.PAYDOWN.SECURITY.FOREX.VCI.SETTLEMENT` | `FsGaMbsPaydown_SecurityForexVciSettlement` | TField |  | Security Forex VCI Settlement Multifonds DB Column is SEC_SETTL_FX_VCI. |
| 59 | `FS.GA.MBS.PAYDOWN.FUND.FOREX.VCI.SECURITY` | `FsGaMbsPaydown_FundForexVciSecurity` | TField |  | Fund Forex VCI Security Multifonds DB Column is SEC_PTF_FX_VCI. |
| 60 | `FS.GA.MBS.PAYDOWN.FUND.FX.SETTLEMENT.VCI` | `FsGaMbsPaydown_FundFxSettlementVci` | TField |  | Settl Ptf Fx Vci Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 61 | `FS.GA.MBS.PAYDOWN.NON.ACCRUAL.STATUS` | `FsGaMbsPaydown_NonAccrualStatus` | TField |  | Flag to denote whether the security is in a defaulted status Multifonds DB Column is FLG_NON_ACC_STATUS. |
| 62 | `FS.GA.MBS.PAYDOWN.AMORTISATION.AMOUNT.NATIVE.CCY` | `FsGaMbsPaydown_AmortisationAmountNativeCcy` | TField |  | Amortization Amount Native Ccy Multifonds DB Column is AMORTISSEMENT_NCY. |
| 63 | `FS.GA.MBS.PAYDOWN.TRADE.ID` | `FsGaMbsPaydown_TradeId` | TField |  | Trade Id Multifonds DB Column is TRADEID. |
| 64 | `FS.GA.MBS.PAYDOWN.KNOWLEDGE.DATE` | `FsGaMbsPaydown_KnowledgeDate` | TField |  | Knowledge Date Multifonds DB Column is KNOWLEDGEDATE. |
| 65 | `FS.GA.MBS.PAYDOWN.MIGRATION.AMORT.DEAL.AMOUNT` | `FsGaMbsPaydown_MigrationAmortDealAmount` | TField |  | Migration amort deal amount Multifonds DB Column is MIG_MNT_AMORT_DEAL. |
| 66 | `FS.GA.MBS.PAYDOWN.MIGRATION.AMORT.FUND.AMOUNT` | `FsGaMbsPaydown_MigrationAmortFundAmount` | TField |  | Migration amort fund amount Multifonds DB Column is MIG_MNT_AMORT_PTF. |
| 67 | `FS.GA.MBS.PAYDOWN.RESERVED10` | `FsGaMbsPaydown_Reserved10` | TField |  |  |
| 68 | `FS.GA.MBS.PAYDOWN.RESERVED9` | `FsGaMbsPaydown_Reserved9` | TField |  |  |
| 69 | `FS.GA.MBS.PAYDOWN.RESERVED8` | `FsGaMbsPaydown_Reserved8` | TField |  |  |
| 70 | `FS.GA.MBS.PAYDOWN.RESERVED7` | `FsGaMbsPaydown_Reserved7` | TField |  |  |
| 71 | `FS.GA.MBS.PAYDOWN.RESERVED6` | `FsGaMbsPaydown_Reserved6` | TField |  |  |
| 72 | `FS.GA.MBS.PAYDOWN.RESERVED5` | `FsGaMbsPaydown_Reserved5` | TField |  |  |
| 73 | `FS.GA.MBS.PAYDOWN.RESERVED4` | `FsGaMbsPaydown_Reserved4` | TField |  |  |
| 74 | `FS.GA.MBS.PAYDOWN.RESERVED3` | `FsGaMbsPaydown_Reserved3` | TField |  |  |
| 75 | `FS.GA.MBS.PAYDOWN.RESERVED2` | `FsGaMbsPaydown_Reserved2` | TField |  |  |
| 76 | `FS.GA.MBS.PAYDOWN.RESERVED1` | `FsGaMbsPaydown_Reserved1` | TField |  |  |
| 77 | `FS.GA.MBS.PAYDOWN.LOCAL.REF` | `FsGaMbsPaydown_LocalRef` |  |  |  |
| 78 | `FS.GA.MBS.PAYDOWN.OVERRIDE` | `FsGaMbsPaydown_Override` |  |  |  |
| 79 | `FS.GA.MBS.PAYDOWN.RECORD.STATUS` | `FsGaMbsPaydown_RecordStatus` | String |  |  |
| 80 | `FS.GA.MBS.PAYDOWN.CURR.NO` | `FsGaMbsPaydown_CurrNo` | String |  |  |
| 81 | `FS.GA.MBS.PAYDOWN.INPUTTER` | `FsGaMbsPaydown_Inputter` |  |  |  |
| 82 | `FS.GA.MBS.PAYDOWN.DATE.TIME` | `FsGaMbsPaydown_DateTime` |  |  |  |
| 83 | `FS.GA.MBS.PAYDOWN.AUTHORISER` | `FsGaMbsPaydown_Authoriser` | String |  |  |
| 84 | `FS.GA.MBS.PAYDOWN.CO.CODE` | `FsGaMbsPaydown_CoCode` | String |  |  |
| 85 | `FS.GA.MBS.PAYDOWN.DEPT.CODE` | `FsGaMbsPaydown_DeptCode` | String |  |  |
| 86 | `FS.GA.MBS.PAYDOWN.AUDITOR.CODE` | `FsGaMbsPaydown_AuditorCode` | String |  |  |
| 87 | `FS.GA.MBS.PAYDOWN.AUDIT.DATE.TIME` | `FsGaMbsPaydown_AuditDateTime` | String |  |  |
