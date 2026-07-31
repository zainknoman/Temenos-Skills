# FS.GA.SWAP.INTEREST.PAYMENT.RECORD — Table Schema

> Source: `INSERTS/I_F.FS.GA.SWAP.INTEREST.PAYMENT.RECORD` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.FUND.ID` | `FsGaSwapInterestPaymentRecord_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.OPERATION.CODE` | `FsGaSwapInterestPaymentRecord_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 3 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.LOT.NUMBER` | `FsGaSwapInterestPaymentRecord_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 4 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.INTEREST.PERIOD.BEGIN.DATE` | `FsGaSwapInterestPaymentRecord_InterestPeriodBeginDate` | TField |  | Refers to the begin date from which the swap interest has been calculated. Multifonds DB Column is DATE_DEB. |
| 5 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.INTEREST.PERIOD.END.DATE` | `FsGaSwapInterestPaymentRecord_InterestPeriodEndDate` | TField |  | Refers to the end date to which the swap interest has been calculated. Multifonds DB Column is DATE_FIN. |
| 6 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaSwapInterestPaymentRecord_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 7 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.INT.RATE` | `FsGaSwapInterestPaymentRecord_IntRate` | TField |  | Interest Rate Multifonds DB Column is TAUX. |
| 8 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.LOCAL.CURRENCY` | `FsGaSwapInterestPaymentRecord_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 9 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.PAID.FEE.FLAG` | `FsGaSwapInterestPaymentRecord_PaidFeeFlag` | TField |  | Y if fees already paid. N for periods not yet paid. The flag applies to swap interest period payment and expense accrual payment. Multifonds DB Column is CD_PAY. |
| 10 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.ARCHIVE` | `FsGaSwapInterestPaymentRecord_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 11 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.GL.ACCOUNT` | `FsGaSwapInterestPaymentRecord_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 12 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.GL.ACCOUNT.SUFFIX` | `FsGaSwapInterestPaymentRecord_GlAccountSuffix` | TField |  | Suffix number tagged to the account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 13 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.MODIFIED.MAURITY.DATE` | `FsGaSwapInterestPaymentRecord_ModifiedMaurityDate` | TField |  | Modified Maurity Date Multifonds DB Column is MFBD_DECH. |
| 14 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED10` | `FsGaSwapInterestPaymentRecord_Reserved10` | TField |  |  |
| 15 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED9` | `FsGaSwapInterestPaymentRecord_Reserved9` | TField |  |  |
| 16 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED8` | `FsGaSwapInterestPaymentRecord_Reserved8` | TField |  |  |
| 17 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED7` | `FsGaSwapInterestPaymentRecord_Reserved7` | TField |  |  |
| 18 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED6` | `FsGaSwapInterestPaymentRecord_Reserved6` | TField |  |  |
| 19 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED5` | `FsGaSwapInterestPaymentRecord_Reserved5` | TField |  |  |
| 20 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED4` | `FsGaSwapInterestPaymentRecord_Reserved4` | TField |  |  |
| 21 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED3` | `FsGaSwapInterestPaymentRecord_Reserved3` | TField |  |  |
| 22 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED2` | `FsGaSwapInterestPaymentRecord_Reserved2` | TField |  |  |
| 23 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RESERVED1` | `FsGaSwapInterestPaymentRecord_Reserved1` | TField |  |  |
| 24 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.LOCAL.REF` | `FsGaSwapInterestPaymentRecord_LocalRef` |  |  |  |
| 25 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.OVERRIDE` | `FsGaSwapInterestPaymentRecord_Override` |  |  |  |
| 26 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.RECORD.STATUS` | `FsGaSwapInterestPaymentRecord_RecordStatus` | String |  |  |
| 27 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.CURR.NO` | `FsGaSwapInterestPaymentRecord_CurrNo` | String |  |  |
| 28 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.INPUTTER` | `FsGaSwapInterestPaymentRecord_Inputter` |  |  |  |
| 29 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.DATE.TIME` | `FsGaSwapInterestPaymentRecord_DateTime` |  |  |  |
| 30 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.AUTHORISER` | `FsGaSwapInterestPaymentRecord_Authoriser` | String |  |  |
| 31 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.CO.CODE` | `FsGaSwapInterestPaymentRecord_CoCode` | String |  |  |
| 32 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.DEPT.CODE` | `FsGaSwapInterestPaymentRecord_DeptCode` | String |  |  |
| 33 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.AUDITOR.CODE` | `FsGaSwapInterestPaymentRecord_AuditorCode` | String |  |  |
| 34 | `FS.GA.SWAP.INTEREST.PAYMENT.RECORD.AUDIT.DATE.TIME` | `FsGaSwapInterestPaymentRecord_AuditDateTime` | String |  |  |
