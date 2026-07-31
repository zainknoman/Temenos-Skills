# FS.GA.SWAP.INTEREST.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.SWAP.INTEREST.PAYMENT` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SWAP.INTEREST.PAYMENT.FUND.ID` | `FsGaSwapInterestPayment_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.SWAP.INTEREST.PAYMENT.OPERATION.CODE` | `FsGaSwapInterestPayment_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 3 | `FS.GA.SWAP.INTEREST.PAYMENT.LOT.NUMBER` | `FsGaSwapInterestPayment_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 4 | `FS.GA.SWAP.INTEREST.PAYMENT.TRANSACTION.NUMBER` | `FsGaSwapInterestPayment_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.SWAP.INTEREST.PAYMENT.TRADE.DATE` | `FsGaSwapInterestPayment_TradeDate` | TField |  | Trade date of the trnsaction Multifonds DB Column is DOPER. |
| 6 | `FS.GA.SWAP.INTEREST.PAYMENT.SETTLE.DATE` | `FsGaSwapInterestPayment_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 7 | `FS.GA.SWAP.INTEREST.PAYMENT.DEAL.STATUS.CODE` | `FsGaSwapInterestPayment_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 8 | `FS.GA.SWAP.INTEREST.PAYMENT.INTEREST.PERIOD.BEGIN.DATE` | `FsGaSwapInterestPayment_InterestPeriodBeginDate` | TField |  | Refers to the begin date from which the swap interest has been calculated. Multifonds DB Column is DATE_DEB. |
| 9 | `FS.GA.SWAP.INTEREST.PAYMENT.INTEREST.PERIOD.END.DATE` | `FsGaSwapInterestPayment_InterestPeriodEndDate` | TField |  | Refers to the end date to which the swap interest has been calculated. Multifonds DB Column is DATE_FIN. |
| 10 | `FS.GA.SWAP.INTEREST.PAYMENT.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaSwapInterestPayment_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 11 | `FS.GA.SWAP.INTEREST.PAYMENT.INT.RATE` | `FsGaSwapInterestPayment_IntRate` | TField |  | Interest Rate Multifonds DB Column is TAUX. |
| 12 | `FS.GA.SWAP.INTEREST.PAYMENT.LOCAL.CURRENCY` | `FsGaSwapInterestPayment_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 13 | `FS.GA.SWAP.INTEREST.PAYMENT.STATUS.PENDING` | `FsGaSwapInterestPayment_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 14 | `FS.GA.SWAP.INTEREST.PAYMENT.ARCHIVE` | `FsGaSwapInterestPayment_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 15 | `FS.GA.SWAP.INTEREST.PAYMENT.CAP.AMOUNT.CUR` | `FsGaSwapInterestPayment_CapAmountCur` | TField |  | CAP Amount CUR Multifonds DB Column is MNT_CAP_CUR. |
| 16 | `FS.GA.SWAP.INTEREST.PAYMENT.SUB.FUND.ENTRY.NUMBER` | `FsGaSwapInterestPayment_SubFundEntryNumber` | TField |  | Corresponds to the deal entry number linked to the transaction entered under a fund participating in the Pool or under a Pool or under a segment fund participating in a segment fund structure Multifonds DB Column is NECRITUR_LINK. |
| 17 | `FS.GA.SWAP.INTEREST.PAYMENT.IFRS.TAG` | `FsGaSwapInterestPayment_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 18 | `FS.GA.SWAP.INTEREST.PAYMENT.CHECK.DATE` | `FsGaSwapInterestPayment_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 19 | `FS.GA.SWAP.INTEREST.PAYMENT.CHECKED.BY` | `FsGaSwapInterestPayment_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 20 | `FS.GA.SWAP.INTEREST.PAYMENT.PAYMENT.AMOUNT.DEBIT` | `FsGaSwapInterestPayment_PaymentAmountDebit` | TField |  | Payment Amount Debit Multifonds DB Column is GLACCOUNT_DB. |
| 21 | `FS.GA.SWAP.INTEREST.PAYMENT.PAYMENT.AMOUNT.CREDIT` | `FsGaSwapInterestPayment_PaymentAmountCredit` | TField |  | Payment Amount Credit Multifonds DB Column is GLACCOUNT_CR. |
| 22 | `FS.GA.SWAP.INTEREST.PAYMENT.FUND.PAYMENT.AMOUNT.DEBIT` | `FsGaSwapInterestPayment_FundPaymentAmountDebit` | TField |  | Fund Payment Amount Debit Multifonds DB Column is MNT_PTF_DB. |
| 23 | `FS.GA.SWAP.INTEREST.PAYMENT.FUND.PAYMENT.AMOUNT.CREDIT` | `FsGaSwapInterestPayment_FundPaymentAmountCredit` | TField |  | Fund Payment Amount Credit Multifonds DB Column is MNT_PTF_CR. |
| 24 | `FS.GA.SWAP.INTEREST.PAYMENT.PAYMENT.AMOUNT.SUFFIX.DB` | `FsGaSwapInterestPayment_PaymentAmountSuffixDb` | TField |  | Payment Amount Suffix DB Multifonds DB Column is GLACCSUFF_DB. |
| 25 | `FS.GA.SWAP.INTEREST.PAYMENT.PAYMENT.AMOUNT.SUFFIX.CR` | `FsGaSwapInterestPayment_PaymentAmountSuffixCr` | TField |  | Payment Amount Suffix CR Multifonds DB Column is GLACCSUFF_CR. |
| 26 | `FS.GA.SWAP.INTEREST.PAYMENT.SECURITY.FOREX.VCI.SETTLEMENT` | `FsGaSwapInterestPayment_SecurityForexVciSettlement` | TField |  | Security Forex VCI Settlement Multifonds DB Column is SEC_SETTL_FX_VCI. |
| 27 | `FS.GA.SWAP.INTEREST.PAYMENT.FUND.FOREX.VCI.SECURITY` | `FsGaSwapInterestPayment_FundForexVciSecurity` | TField |  | Fund Forex VCI Security Multifonds DB Column is SEC_PTF_FX_VCI. |
| 28 | `FS.GA.SWAP.INTEREST.PAYMENT.FUND.FX.SETTLEMENT.VCI` | `FsGaSwapInterestPayment_FundFxSettlementVci` | TField |  | Settl Ptf Fx Vci Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 29 | `FS.GA.SWAP.INTEREST.PAYMENT.PAYABLE.FATCA.AMOUNT` | `FsGaSwapInterestPayment_PayableFatcaAmount` | TField |  | Populated when swap deal is eligible for FATCA (Foreign Account Tax Compliance Act) US regulatory reporting with FATCA Liability as 'Y' &amp; FACTA Liability % defined. Payable FATCA=FATCA Rate*Gross Amt Multifonds DB Column is MNT_TAX_FATCA. |
| 30 | `FS.GA.SWAP.INTEREST.PAYMENT.GROSS.AMOUNT.OF.INCOME` | `FsGaSwapInterestPayment_GrossAmountOfIncome` | TField |  | The Gross amount of the income Multifonds DB Column is MNTGLOBAL. |
| 31 | `FS.GA.SWAP.INTEREST.PAYMENT.FACTOR` | `FsGaSwapInterestPayment_Factor` | TField |  | Factor for Mortgage backed instruments, also used in CMV securities and Fair value pricing. This also finds use as a mark up or down value in case of other features Multifonds DB Column is FACTOR. |
| 32 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED10` | `FsGaSwapInterestPayment_Reserved10` | TField |  |  |
| 33 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED9` | `FsGaSwapInterestPayment_Reserved9` | TField |  |  |
| 34 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED8` | `FsGaSwapInterestPayment_Reserved8` | TField |  |  |
| 35 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED7` | `FsGaSwapInterestPayment_Reserved7` | TField |  |  |
| 36 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED6` | `FsGaSwapInterestPayment_Reserved6` | TField |  |  |
| 37 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED5` | `FsGaSwapInterestPayment_Reserved5` | TField |  |  |
| 38 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED4` | `FsGaSwapInterestPayment_Reserved4` | TField |  |  |
| 39 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED3` | `FsGaSwapInterestPayment_Reserved3` | TField |  |  |
| 40 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED2` | `FsGaSwapInterestPayment_Reserved2` | TField |  |  |
| 41 | `FS.GA.SWAP.INTEREST.PAYMENT.RESERVED1` | `FsGaSwapInterestPayment_Reserved1` | TField |  |  |
| 42 | `FS.GA.SWAP.INTEREST.PAYMENT.LOCAL.REF` | `FsGaSwapInterestPayment_LocalRef` |  |  |  |
| 43 | `FS.GA.SWAP.INTEREST.PAYMENT.OVERRIDE` | `FsGaSwapInterestPayment_Override` |  |  |  |
| 44 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.STATUS` | `FsGaSwapInterestPayment_RecordStatus` | String |  |  |
| 45 | `FS.GA.SWAP.INTEREST.PAYMENT.CURR.NO` | `FsGaSwapInterestPayment_CurrNo` | String |  |  |
| 46 | `FS.GA.SWAP.INTEREST.PAYMENT.INPUTTER` | `FsGaSwapInterestPayment_Inputter` |  |  |  |
| 47 | `FS.GA.SWAP.INTEREST.PAYMENT.DATE.TIME` | `FsGaSwapInterestPayment_DateTime` |  |  |  |
| 48 | `FS.GA.SWAP.INTEREST.PAYMENT.AUTHORISER` | `FsGaSwapInterestPayment_Authoriser` | String |  |  |
| 49 | `FS.GA.SWAP.INTEREST.PAYMENT.CO.CODE` | `FsGaSwapInterestPayment_CoCode` | String |  |  |
| 50 | `FS.GA.SWAP.INTEREST.PAYMENT.DEPT.CODE` | `FsGaSwapInterestPayment_DeptCode` | String |  |  |
| 51 | `FS.GA.SWAP.INTEREST.PAYMENT.AUDITOR.CODE` | `FsGaSwapInterestPayment_AuditorCode` | String |  |  |
| 52 | `FS.GA.SWAP.INTEREST.PAYMENT.AUDIT.DATE.TIME` | `FsGaSwapInterestPayment_AuditDateTime` | String |  |  |
