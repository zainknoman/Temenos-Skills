# FS.GA.FEE.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.FEE.PAYMENT` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.FEE.PAYMENT.FUND.ID` | `FsGaFeePayment_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `GA.FEE.PAYMENT.CHARGE.CODE` | `FsGaFeePayment_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 3 | `GA.FEE.PAYMENT.TRANSACTION.NUMBER` | `FsGaFeePayment_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 4 | `GA.FEE.PAYMENT.LINE` | `FsGaFeePayment_Line` | TField |  | Line Multifonds DB Column is NLIGNE. |
| 5 | `GA.FEE.PAYMENT.GL.ACCOUNT` | `FsGaFeePayment_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 6 | `GA.FEE.PAYMENT.GL.ACCOUNT.SUFFIX` | `FsGaFeePayment_GlAccountSuffix` | TField |  | Suffix number tagged to the account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 7 | `GA.FEE.PAYMENT.PAY.DATE` | `FsGaFeePayment_PayDate` | TField |  |  |
| 8 | `GA.FEE.PAYMENT.LOCAL.CURRENCY` | `FsGaFeePayment_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 9 | `GA.FEE.PAYMENT.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaFeePayment_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 10 | `GA.FEE.PAYMENT.REFARENCE.CCY` | `FsGaFeePayment_RefarenceCcy` | TField |  |  |
| 11 | `GA.FEE.PAYMENT.AMOUNT.IN.REFERENCE.CURRENCY` | `FsGaFeePayment_AmountInReferenceCurrency` | TField |  | Amount In Reference Currency Multifonds DB Column is MONT_BASE. |
| 12 | `GA.FEE.PAYMENT.RATE.OF.EXCHANGE` | `FsGaFeePayment_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 13 | `GA.FEE.PAYMENT.DEBIT.CREDIT.INDICATOR` | `FsGaFeePayment_DebitCreditIndicator` | TField |  | Debit credit indicator tagged to an account number Multifonds DB Column is CSENS. |
| 14 | `GA.FEE.PAYMENT.OPERATION.CODE` | `FsGaFeePayment_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 15 | `GA.FEE.PAYMENT.TRADE.DATE` | `FsGaFeePayment_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 16 | `GA.FEE.PAYMENT.SETTLE.DATE` | `FsGaFeePayment_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 17 | `GA.FEE.PAYMENT.ACCOUNTING.DATE` | `FsGaFeePayment_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 18 | `GA.FEE.PAYMENT.DEAL.STATUS.CODE` | `FsGaFeePayment_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 19 | `GA.FEE.PAYMENT.EXECUTION.DATE` | `FsGaFeePayment_ExecutionDate` | TField |  | Execution Date Multifonds DB Column is DAT_TRAITE. |
| 20 | `GA.FEE.PAYMENT.ARCHIVE` | `FsGaFeePayment_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 21 | `GA.FEE.PAYMENT.MANAGER.ID` | `FsGaFeePayment_ManagerId` | TField |  | Manager ID Multifonds DB Column is NACC_MNGR. |
| 22 | `GA.FEE.PAYMENT.MANAGER.CODE` | `FsGaFeePayment_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 23 | `GA.FEE.PAYMENT.STATUS.PENDING` | `FsGaFeePayment_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 24 | `GA.FEE.PAYMENT.EXTERNAL.REFERENCE` | `FsGaFeePayment_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 25 | `GA.FEE.PAYMENT.VAT.CODE` | `FsGaFeePayment_VatCode` | TField |  | The VAT incidence can be taken into consideration independently of the principal of the comm in the respect of the conditions of the agreement among the fund and the 3rd party initiating the fee. Multifonds DB Column is FLAG_TVA. |
| 26 | `GA.FEE.PAYMENT.CHECK.DATE` | `FsGaFeePayment_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 27 | `GA.FEE.PAYMENT.CHECKED.BY` | `FsGaFeePayment_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 28 | `GA.FEE.PAYMENT.EXECUTION.TIMESTAMP` | `FsGaFeePayment_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 29 | `GA.FEE.PAYMENT.FUND.STRATEGY` | `FsGaFeePayment_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 30 | `GA.FEE.PAYMENT.ALLOW.MULTIPLE.REBOOKING` | `FsGaFeePayment_AllowMultipleRebooking` | TField |  | If checked, the system allows multiple rebooking more than once for a fund set with the rebooking function (NAV Type = R or M). Multifonds DB Column is FLG_REBOOK. |
| 31 | `GA.FEE.PAYMENT.CUSTODIAN` | `FsGaFeePayment_Custodian` | TField |  | Custodian where the units of the transaction would be lodged Multifonds DB Column is NDEPOSI. |
| 32 | `GA.FEE.PAYMENT.COMMENTS` | `FsGaFeePayment_Comments` | TField |  | Comments Multifonds DB Column is COMMENTS. |
| 33 | `GA.FEE.PAYMENT.MANUAL.SETTLEMENT.FOR.FEES` | `FsGaFeePayment_ManualSettlementForFees` | TField |  | Flag to enable/disable manual settlements for fees amount Multifonds DB Column is FLG_MANUAL_SETT. |
| 34 | `GA.FEE.PAYMENT.INTERNAL.SECURITY.ID` | `FsGaFeePayment_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 35 | `GA.FEE.PAYMENT.RESERVED10` | `FsGaFeePayment_Reserved10` | TField |  |  |
| 36 | `GA.FEE.PAYMENT.RESERVED9` | `FsGaFeePayment_Reserved9` | TField |  |  |
| 37 | `GA.FEE.PAYMENT.RESERVED8` | `FsGaFeePayment_Reserved8` | TField |  |  |
| 38 | `GA.FEE.PAYMENT.RESERVED7` | `FsGaFeePayment_Reserved7` | TField |  |  |
| 39 | `GA.FEE.PAYMENT.RESERVED6` | `FsGaFeePayment_Reserved6` | TField |  |  |
| 40 | `GA.FEE.PAYMENT.RESERVED5` | `FsGaFeePayment_Reserved5` | TField |  |  |
| 41 | `GA.FEE.PAYMENT.RESERVED4` | `FsGaFeePayment_Reserved4` | TField |  |  |
| 42 | `GA.FEE.PAYMENT.RESERVED3` | `FsGaFeePayment_Reserved3` | TField |  |  |
| 43 | `GA.FEE.PAYMENT.RESERVED2` | `FsGaFeePayment_Reserved2` | TField |  |  |
| 44 | `GA.FEE.PAYMENT.RESERVED1` | `FsGaFeePayment_Reserved1` | TField |  |  |
| 45 | `GA.FEE.PAYMENT.LOCAL.REF` | `FsGaFeePayment_LocalRef` |  |  |  |
| 46 | `GA.FEE.PAYMENT.OVERRIDE` | `FsGaFeePayment_Override` |  |  |  |
| 47 | `GA.FEE.PAYMENT.RECORD.STATUS` | `FsGaFeePayment_RecordStatus` | String |  |  |
| 48 | `GA.FEE.PAYMENT.CURR.NO` | `FsGaFeePayment_CurrNo` | String |  |  |
| 49 | `GA.FEE.PAYMENT.INPUTTER` | `FsGaFeePayment_Inputter` |  |  |  |
| 50 | `GA.FEE.PAYMENT.DATE.TIME` | `FsGaFeePayment_DateTime` |  |  |  |
| 51 | `GA.FEE.PAYMENT.AUTHORISER` | `FsGaFeePayment_Authoriser` | String |  |  |
| 52 | `GA.FEE.PAYMENT.CO.CODE` | `FsGaFeePayment_CoCode` | String |  |  |
| 53 | `GA.FEE.PAYMENT.DEPT.CODE` | `FsGaFeePayment_DeptCode` | String |  |  |
| 54 | `GA.FEE.PAYMENT.AUDITOR.CODE` | `FsGaFeePayment_AuditorCode` | String |  |  |
| 55 | `GA.FEE.PAYMENT.AUDIT.DATE.TIME` | `FsGaFeePayment_AuditDateTime` | String |  |  |
