# FS.GA.FORWARD.RATE.AGREEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.FORWARD.RATE.AGREEMENT` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FORWARD.RATE.AGREEMENT.FUND.ID` | `FsGaForwardRateAgreement_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.FORWARD.RATE.AGREEMENT.LOT.NUMBER` | `FsGaForwardRateAgreement_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 3 | `FS.GA.FORWARD.RATE.AGREEMENT.TRANSACTION.NUMBER` | `FsGaForwardRateAgreement_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 4 | `FS.GA.FORWARD.RATE.AGREEMENT.SERVICE.CODE` | `FsGaForwardRateAgreement_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.FORWARD.RATE.AGREEMENT.OPERATION.CODE` | `FsGaForwardRateAgreement_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 6 | `FS.GA.FORWARD.RATE.AGREEMENT.DEAL.STATUS.CODE` | `FsGaForwardRateAgreement_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 7 | `FS.GA.FORWARD.RATE.AGREEMENT.GL.ACCOUNT` | `FsGaForwardRateAgreement_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 8 | `FS.GA.FORWARD.RATE.AGREEMENT.GL.ACCOUNT.SUFFIX` | `FsGaForwardRateAgreement_GlAccountSuffix` | TField |  | Suffix number tagged to the account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 9 | `FS.GA.FORWARD.RATE.AGREEMENT.CORRESPONDENT` | `FsGaForwardRateAgreement_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 10 | `FS.GA.FORWARD.RATE.AGREEMENT.TRADE.DATE` | `FsGaForwardRateAgreement_TradeDate` | TField |  | Trade date of the trnsaction Multifonds DB Column is DOPER. |
| 11 | `FS.GA.FORWARD.RATE.AGREEMENT.SETTLE.DATE` | `FsGaForwardRateAgreement_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 12 | `FS.GA.FORWARD.RATE.AGREEMENT.MATURITY.DATE.OF.CONTRACT` | `FsGaForwardRateAgreement_MaturityDateOfContract` | TField |  | Maturity Date of the Contract/Instrument Multifonds DB Column is DECH. |
| 13 | `FS.GA.FORWARD.RATE.AGREEMENT.ACCOUNTING.DATE` | `FsGaForwardRateAgreement_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 14 | `FS.GA.FORWARD.RATE.AGREEMENT.GL.ACCOUNT.OF.CONTRACT` | `FsGaForwardRateAgreement_GlAccountOfContract` | TField |  | Account Number for Contractual Instruments ex. FRAs Multifonds DB Column is NRUBR_INT. |
| 15 | `FS.GA.FORWARD.RATE.AGREEMENT.GL.ACCOUNT.SUFFIX.OF.CONTRACT` | `FsGaForwardRateAgreement_GlAccountSuffixOfContract` | TField |  | Account Number Suffix for Contractual Instruments ex. FRAs Multifonds DB Column is NSUFF_INT. |
| 16 | `FS.GA.FORWARD.RATE.AGREEMENT.COUNTERPART.ACCOUNT.NUMBER` | `FsGaForwardRateAgreement_CounterpartAccountNumber` | TField |  | Counterpart Account Number Multifonds DB Column is NRUBR_COR. |
| 17 | `FS.GA.FORWARD.RATE.AGREEMENT.COUNTERPART.SUFFIX.NUMBER` | `FsGaForwardRateAgreement_CounterpartSuffixNumber` | TField |  | Counterpart Suffix Number Multifonds DB Column is NSUFF_COR. |
| 18 | `FS.GA.FORWARD.RATE.AGREEMENT.DAY.COUNT.CONVENTION` | `FsGaForwardRateAgreement_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 19 | `FS.GA.FORWARD.RATE.AGREEMENT.LOCAL.CURRENCY` | `FsGaForwardRateAgreement_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 20 | `FS.GA.FORWARD.RATE.AGREEMENT.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaForwardRateAgreement_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 21 | `FS.GA.FORWARD.RATE.AGREEMENT.INTEREST.RATE.CODE` | `FsGaForwardRateAgreement_InterestRateCode` | TField |  | Interest/forward exchange rate maintenance code based on source ( LIBOR/MIBOR) Multifonds DB Column is CTAUX. |
| 22 | `FS.GA.FORWARD.RATE.AGREEMENT.INT.RATE` | `FsGaForwardRateAgreement_IntRate` | TField |  | Interest Rate Multifonds DB Column is TAUX. |
| 23 | `FS.GA.FORWARD.RATE.AGREEMENT.VALUE.DATE` | `FsGaForwardRateAgreement_ValueDate` | TField |  | Value date of the Forward Interest/exchange rate Multifonds DB Column is DFIXING. |
| 24 | `FS.GA.FORWARD.RATE.AGREEMENT.DESCRIPTION` | `FsGaForwardRateAgreement_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 25 | `FS.GA.FORWARD.RATE.AGREEMENT.ARCHIVE` | `FsGaForwardRateAgreement_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 26 | `FS.GA.FORWARD.RATE.AGREEMENT.ENTRY.NUMBER.REPAYMENT` | `FsGaForwardRateAgreement_EntryNumberRepayment` | TField |  | Entry number of original transaction for triggering repayment Multifonds DB Column is NECRITUR_REMB. |
| 27 | `FS.GA.FORWARD.RATE.AGREEMENT.MANAGER.CODE` | `FsGaForwardRateAgreement_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 28 | `FS.GA.FORWARD.RATE.AGREEMENT.COUNTERPARTY.CORRESPONDENT` | `FsGaForwardRateAgreement_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 29 | `FS.GA.FORWARD.RATE.AGREEMENT.COUNTER.PARTY.CODE` | `FsGaForwardRateAgreement_CounterPartyCode` | TField |  | Guarantor,Issuer Multifonds DB Column is NISSUER_GUARANTEED. |
| 30 | `FS.GA.FORWARD.RATE.AGREEMENT.STATUS.PENDING` | `FsGaForwardRateAgreement_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 31 | `FS.GA.FORWARD.RATE.AGREEMENT.EXTERNAL.REFERENCE` | `FsGaForwardRateAgreement_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 32 | `FS.GA.FORWARD.RATE.AGREEMENT.FUND.STRATEGY` | `FsGaForwardRateAgreement_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 33 | `FS.GA.FORWARD.RATE.AGREEMENT.FUND.LINK.ID` | `FsGaForwardRateAgreement_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 34 | `FS.GA.FORWARD.RATE.AGREEMENT.INTERNAL.SECURITY.ID` | `FsGaForwardRateAgreement_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 35 | `FS.GA.FORWARD.RATE.AGREEMENT.POSITION.TYPE.LONG.OR.SHORT` | `FsGaForwardRateAgreement_PositionTypeLongOrShort` | TField |  | Position Type Long/Short Multifonds DB Column is FLG_POS_TYPE. |
| 36 | `FS.GA.FORWARD.RATE.AGREEMENT.CHECK.DATE` | `FsGaForwardRateAgreement_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 37 | `FS.GA.FORWARD.RATE.AGREEMENT.CHECKED.BY` | `FsGaForwardRateAgreement_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 38 | `FS.GA.FORWARD.RATE.AGREEMENT.IFRS.TAG` | `FsGaForwardRateAgreement_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 39 | `FS.GA.FORWARD.RATE.AGREEMENT.UTI.DESCRIPTION` | `FsGaForwardRateAgreement_UtiDescription` | TField |  | UTI Description Multifonds DB Column is UTI_DESC. |
| 40 | `FS.GA.FORWARD.RATE.AGREEMENT.USI.DESCRIPTION` | `FsGaForwardRateAgreement_UsiDescription` | TField |  | USI Description Multifonds DB Column is USI_DESC. |
| 41 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED10` | `FsGaForwardRateAgreement_Reserved10` | TField |  |  |
| 42 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED9` | `FsGaForwardRateAgreement_Reserved9` | TField |  |  |
| 43 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED8` | `FsGaForwardRateAgreement_Reserved8` | TField |  |  |
| 44 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED7` | `FsGaForwardRateAgreement_Reserved7` | TField |  |  |
| 45 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED6` | `FsGaForwardRateAgreement_Reserved6` | TField |  |  |
| 46 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED5` | `FsGaForwardRateAgreement_Reserved5` | TField |  |  |
| 47 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED4` | `FsGaForwardRateAgreement_Reserved4` | TField |  |  |
| 48 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED3` | `FsGaForwardRateAgreement_Reserved3` | TField |  |  |
| 49 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED2` | `FsGaForwardRateAgreement_Reserved2` | TField |  |  |
| 50 | `FS.GA.FORWARD.RATE.AGREEMENT.RESERVED1` | `FsGaForwardRateAgreement_Reserved1` | TField |  |  |
| 51 | `FS.GA.FORWARD.RATE.AGREEMENT.LOCAL.REF` | `FsGaForwardRateAgreement_LocalRef` |  |  |  |
| 52 | `FS.GA.FORWARD.RATE.AGREEMENT.OVERRIDE` | `FsGaForwardRateAgreement_Override` |  |  |  |
| 53 | `FS.GA.FORWARD.RATE.AGREEMENT.RECORD.STATUS` | `FsGaForwardRateAgreement_RecordStatus` | String |  |  |
| 54 | `FS.GA.FORWARD.RATE.AGREEMENT.CURR.NO` | `FsGaForwardRateAgreement_CurrNo` | String |  |  |
| 55 | `FS.GA.FORWARD.RATE.AGREEMENT.INPUTTER` | `FsGaForwardRateAgreement_Inputter` |  |  |  |
| 56 | `FS.GA.FORWARD.RATE.AGREEMENT.DATE.TIME` | `FsGaForwardRateAgreement_DateTime` |  |  |  |
| 57 | `FS.GA.FORWARD.RATE.AGREEMENT.AUTHORISER` | `FsGaForwardRateAgreement_Authoriser` | String |  |  |
| 58 | `FS.GA.FORWARD.RATE.AGREEMENT.CO.CODE` | `FsGaForwardRateAgreement_CoCode` | String |  |  |
| 59 | `FS.GA.FORWARD.RATE.AGREEMENT.DEPT.CODE` | `FsGaForwardRateAgreement_DeptCode` | String |  |  |
| 60 | `FS.GA.FORWARD.RATE.AGREEMENT.AUDITOR.CODE` | `FsGaForwardRateAgreement_AuditorCode` | String |  |  |
| 61 | `FS.GA.FORWARD.RATE.AGREEMENT.AUDIT.DATE.TIME` | `FsGaForwardRateAgreement_AuditDateTime` | String |  |  |
