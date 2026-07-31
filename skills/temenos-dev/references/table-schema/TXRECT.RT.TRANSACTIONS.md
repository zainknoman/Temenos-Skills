# TXRECT.RT.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.TXRECT.RT.TRANSACTIONS` in `TXRECT_TaxRectificationTool.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TXRECT.RT.TXN.RO.TRANSACTION.ID` | `TxrectRtTransactions_RoTransactionId` | TField |  | RO transaction ID-Updated from RO.TRANSACTION |
| 2 | `TXRECT.RT.TXN.RO.TAX.TYPE` | `TxrectRtTransactions_RoTaxType` | TField |  | Tax type on which above Rectification operation type is performed; TAX.TYPE @ID of respective tax - Updated from RO.TRANSACTION |
| 3 | `TXRECT.RT.TXN.RO.DATE` | `TxrectRtTransactions_RoDate` | TField |  | Date of Rectification operation transaction - Updated from RO.TRANSACTION |
| 4 | `TXRECT.RT.TXN.RO.VALUE.DATE` | `TxrectRtTransactions_RoValueDate` | TField |  | Value Date to be used for Accounting entries |
| 5 | `TXRECT.RT.TXN.INITIAL.EXCH.RATE.IND` | `TxrectRtTransactions_InitialExchRateInd` | TField |  | Whether exchange rate from original transaction will be used for conversion if account currency is different from tax account ccy - Updated from RO.TRANSACTION |
| 6 | `TXRECT.RT.TXN.CUST.EXCH.RATE` | `TxrectRtTransactions_CustExchRate` | TField |  | Customer Exchange rate will be applicable if currency of customer account is different from internal tax account ccy. If INITIAL.EXCH.RATE.IND is N, then default todays exchange rate. If INITIAL.EXCH.RATE.IND is Y, then default exchange rate from original transaction. |
| 7 | `TXRECT.RT.TXN.ORIGINAL.TRANSACTION.ID` | `TxrectRtTransactions_OriginalTransactionId` | TField |  | @ID of original transaction on which rectification operation is done |
| 8 | `TXRECT.RT.TXN.TAX.CURRENCY` | `TxrectRtTransactions_TaxCurrency` | TField |  | Currency of Tax Account |
| 9 | `TXRECT.RT.TXN.ORIGINAL.TAX.AMOUNT` | `TxrectRtTransactions_OriginalTaxAmount` | TField |  | Tax Amount from Original Transaction or TAX.AMOUNT from most recent rectification corresponding to original transaction |
| 10 | `TXRECT.RT.TXN.CUSTOMER.ID` | `TxrectRtTransactions_CustomerId` | TField |  | Customer Number from Original Transaction |
| 11 | `TXRECT.RT.TXN.CUST.ACCT.NO` | `TxrectRtTransactions_CustAcctNo` | TField |  | Customer Account Number from Original Transaction |
| 12 | `TXRECT.RT.TXN.CUST.ACCT.CURRENCY` | `TxrectRtTransactions_CustAcctCurrency` | TField |  | Customer Account Currency |
| 13 | `TXRECT.RT.TXN.TAXABLE.BASIS.AMOUNT` | `TxrectRtTransactions_TaxableBasisAmount` | TField |  | Taxable basis amount |
| 14 | `TXRECT.RT.TXN.TAX.AMOUNT` | `TxrectRtTransactions_TaxAmount` | TField |  | Displays new tax amount in Tax Currency which will be calculated by the System or Inputted by the User |
| 15 | `TXRECT.RT.TXN.ADJUSTED.TAX.AMOUNT` | `TxrectRtTransactions_AdjustedTaxAmount` | TField |  | Original Tax Amount minus Tax Amount, i.e. difference between the original posted tax amount and new tax amount. This will be the Tax Amount to be posted to the Tax Account |
| 16 | `TXRECT.RT.TXN.TAX.RATE` | `TxrectRtTransactions_TaxRate` | TField |  | Tax Rate |
| 17 | `TXRECT.RT.TXN.CUSTOMER.TAX.AMOUNT` | `TxrectRtTransactions_CustomerTaxAmount` | TField |  | Customer Tax Amount in customer account ccy.This is the Adjusted Tax Amount converted to Customer Account Currency |
| 18 | `TXRECT.RT.TXN.COMMISSION.AMOUNT` | `TxrectRtTransactions_CommissionAmount` | TField |  | Commission amount for tax reclaim |
| 19 | `TXRECT.RT.TXN.COMMISSION.TAX.AMOUNT.LCY` | `TxrectRtTransactions_CommissionTaxAmountLcy` | TField |  | Commission (VAT) on tax amount in EUR |
| 20 | `TXRECT.RT.TXN.CUSTOMER.NET.TAX.AMOUNT` | `TxrectRtTransactions_CustomerNetTaxAmount` | TField |  | This will be same as Customer Tax Amount in customer account ccy |
| 21 | `TXRECT.RT.TXN.INTERNAL.TAX.ACCT.NO` | `TxrectRtTransactions_InternalTaxAcctNo` | TField |  | Updated from RO transaction |
| 22 | `TXRECT.RT.TXN.HISTORICAL.TRACK.IND` | `TxrectRtTransactions_HistoricalTrackInd` | TField |  | Updated from RO transaction |
| 23 | `TXRECT.RT.TXN.INTERNAL.COMMENT` | `TxrectRtTransactions_InternalComment` | TField |  | Updated from RO transaction |
| 24 | `TXRECT.RT.TXN.FT.TRANSACTION.ID` | `TxrectRtTransactions_FtTransactionId` | TField |  | This field stores Funds transfer ID which is created when rectification transaction is authorised |
| 25 | `TXRECT.RT.TXN.FT.TRANSACTION.REV.ID` | `TxrectRtTransactions_FtTransactionRevId` | TField |  | This field stores funds transfer ID (contra transaction) which is created when rectification transaction is reversed |
| 26 | `TXRECT.RT.TXN.REVERSAL.MARKER` | `TxrectRtTransactions_ReversalMarker` | TField |  | Updated as Y when Rectification transaction is reversed |
| 27 | `TXRECT.RT.TXN.CLIENT.ADVICE.REQUIRED` | `TxrectRtTransactions_ClientAdviceRequired` | TField |  | Updated from RO.TRANSACTION |
| 28 | `TXRECT.RT.TXN.RESERVED.5` | `TxrectRtTransactions_Reserved5` | TField |  | Reserved field for future use |
| 29 | `TXRECT.RT.TXN.RESERVED.4` | `TxrectRtTransactions_Reserved4` | TField |  | Reserved field for future use |
| 30 | `TXRECT.RT.TXN.RESERVED.3` | `TxrectRtTransactions_Reserved3` | TField |  | Reserved field for future use |
| 31 | `TXRECT.RT.TXN.RESERVED.2` | `TxrectRtTransactions_Reserved2` | TField |  | Reserved field for future use |
| 32 | `TXRECT.RT.TXN.RESERVED.1` | `TxrectRtTransactions_Reserved1` | TField |  | Reserved field for future use |
| 33 | `TXRECT.RT.TXN.LOCAL.REF` | `TxrectRtTransactions_LocalRef` |  |  |  |
| 34 | `TXRECT.RT.TXN.OVERRIDE` | `TxrectRtTransactions_Override` |  |  |  |
| 35 | `TXRECT.RT.TXN.RECORD.STATUS` | `TxrectRtTransactions_RecordStatus` | String |  |  |
| 36 | `TXRECT.RT.TXN.CURR.NO` | `TxrectRtTransactions_CurrNo` | String |  |  |
| 37 | `TXRECT.RT.TXN.INPUTTER` | `TxrectRtTransactions_Inputter` |  |  |  |
| 38 | `TXRECT.RT.TXN.DATE.TIME` | `TxrectRtTransactions_DateTime` |  |  |  |
| 39 | `TXRECT.RT.TXN.AUTHORISER` | `TxrectRtTransactions_Authoriser` | String |  |  |
| 40 | `TXRECT.RT.TXN.CO.CODE` | `TxrectRtTransactions_CoCode` | String |  |  |
| 41 | `TXRECT.RT.TXN.DEPT.CODE` | `TxrectRtTransactions_DeptCode` | String |  |  |
| 42 | `TXRECT.RT.TXN.AUDITOR.CODE` | `TxrectRtTransactions_AuditorCode` | String |  |  |
| 43 | `TXRECT.RT.TXN.AUDIT.DATE.TIME` | `TxrectRtTransactions_AuditDateTime` | String |  |  |
| 44 | `TXRECT.RT.TXN.RO.TYPE` | `TxrectRtTransactions_RoType` | TField |  | Rectification Operation type (Reimbursement, recalculation, Amount forcing, Tax reclaim) |
| 45 | `TXRECT.RT.TXN.BOOKING.DATE` | `TxrectRtTransactions_BookingDate` | TField |  | booking date of transaction; same as in CORE enquiry STMT.ENT.BOOK; no input field, Start of multi value set |
| 46 | `TXRECT.RT.TXN.DESCRIPTION` | `TxrectRtTransactions_Description` | TField |  | Description; same as in CORE enquiry STMT.ENT.BOOK; no input field. |
| 47 | `TXRECT.RT.TXN.VALUE.DATE` | `TxrectRtTransactions_ValueDate` | TField |  | Value Date of transaction; same as in CORE enquiry STMT.ENT.BOOK; no input field. |
| 48 | `TXRECT.RT.TXN.DEBIT.AMOUNT` | `TxrectRtTransactions_DebitAmount` | TField |  | amount debited for given account number; same as in CORE enquiry STMT.ENT.BOOK; no input field. |
| 49 | `TXRECT.RT.TXN.CREDIT.AMOUNT` | `TxrectRtTransactions_CreditAmount` | TField |  | amount credited for given account number; same as in CORE enquiry STMT.ENT.BOOK; no input field. |
| 50 | `TXRECT.RT.TXN.PORTFOLIO.ID` | `TxrectRtTransactions_PortfolioId` | TField |  | Portfolio ID given in transaction. |
| 51 | `TXRECT.RT.TXN.SECURITY.ID` | `TxrectRtTransactions_SecurityId` | TField |  | Security number in transaction. |
| 52 | `TXRECT.RT.TXN.AUTO.TAX.RECLAIM` | `TxrectRtTransactions_AutoTaxReclaim` | TField |  | Indicate if a transaction if automatic tax reclaim. it is defaulted as 'NO' |
| 53 | `TXRECT.RT.TXN.MARKET` | `TxrectRtTransactions_Market` | TField |  | Domicile of issuer of security |
| 54 | `TXRECT.RT.TXN.ORIGINAL.TAX.RATE` | `TxrectRtTransactions_OriginalTaxRate` | TField |  | Original tax rate field mapped from STMT.ENTRY narrative field |
| 55 | `TXRECT.RT.TXN.ORIGINAL.TAXABLE.BASIS.AMOUNT` | `TxrectRtTransactions_OriginalTaxableBasisAmount` | TField |  | Deal Amt field mapped from STMT.ENTRY narrative field |
