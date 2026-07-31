# TXRECT.RO.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.TXRECT.RO.TRANSACTIONS` in `TXRECT_TaxRectificationTool.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TXRECT.RO.ALL.ENTRIES.PROCESSED` | `TxrectRoTransactions_AllEntriesProcessed` | TField |  |  |
| 2 | `TXRECT.RO.RO.SELECTION.ID` | `TxrectRoTransactions_RoSelectionId` | TField |  |  |
| 3 | `TXRECT.RO.RO.TYPE` | `TxrectRoTransactions_RoType` | TField |  | Rectification Operation type (Reimbursement, recalculation, Amount forcing, Tax reclaim) |
| 4 | `TXRECT.RO.RECTIFICATION.TRANSACTION` | `TxrectRoTransactions_RectificationTransaction` | TField |  |  |
| 5 | `TXRECT.RO.INITIAL.EXCH.RATE.IND` | `TxrectRoTransactions_InitialExchRateInd` | TField |  | Whether to use exchange rate from initial transaction or current exchange rate - Y or N. Initially this field will be defaulted as N by system. |
| 6 | `TXRECT.RO.HISTORICAL.TRACK.IND` | `TxrectRoTransactions_HistoricalTrackInd` | TField |  | Historical track indicator - Y or N. Initially this field will be defaulted as Y by system. |
| 7 | `TXRECT.RO.CLIENT.ADVICE.REQUIRED` | `TxrectRoTransactions_ClientAdviceRequired` | TField |  | Client advice indicator whether client advice to be sent - Y or N Initially this field will be defaulted as Y by system. |
| 8 | `TXRECT.RO.INTERNAL.TAX.ACCT.NO` | `TxrectRoTransactions_InternalTaxAcctNo` | TField |  |  |
| 9 | `TXRECT.RO.INTERNAL.COMMENT` | `TxrectRoTransactions_InternalComment` | TField |  | User input field to update internal comment to justify the reason for RO. |
| 10 | `TXRECT.RO.RO.DATE` | `TxrectRoTransactions_RoDate` | TField |  | Date of Rectification operation transaction |
| 11 | `TXRECT.RO.RO.VALUE.DATE` | `TxrectRoTransactions_RoValueDate` | TField |  |  |
| 12 | `TXRECT.RO.BOOKING.DATE` | `TxrectRoTransactions_BookingDate` | TField |  |  |
| 13 | `TXRECT.RO.TRANSACTION.REF` | `TxrectRoTransactions_TransactionRef` | TField |  |  |
| 14 | `TXRECT.RO.DESCRIPTION` | `TxrectRoTransactions_Description` | TField |  |  |
| 15 | `TXRECT.RO.VALUE.DATE` | `TxrectRoTransactions_ValueDate` | TField |  | Value date of transaction; same as in CORE enquiry STMT.ENT.BOOK. Inputted by user |
| 16 | `TXRECT.RO.DEBIT.AMOUNT` | `TxrectRoTransactions_DebitAmount` | TField |  |  |
| 17 | `TXRECT.RO.CREDIT.AMOUNT` | `TxrectRoTransactions_CreditAmount` | TField |  |  |
| 18 | `TXRECT.RO.CUSTOMER.ID` | `TxrectRoTransactions_CustomerId` | TField |  |  |
| 19 | `TXRECT.RO.PORTFOLIO.ID` | `TxrectRoTransactions_PortfolioId` | TField |  | Portfolio ID given in transaction.Inputted by user |
| 20 | `TXRECT.RO.SECURITY.ID` | `TxrectRoTransactions_SecurityId` | TField |  | Security number in transaction-Inputted by user |
| 21 | `TXRECT.RO.SECURITY.CODE` | `TxrectRoTransactions_SecurityCode` | TField |  | Valid SECURITY.MASTER @ID |
| 22 | `TXRECT.RO.EVENT.TYPE` | `TxrectRoTransactions_EventType` | TField |  | Valid DIARY.TYPE @ID |
| 23 | `TXRECT.RO.DATE.TYPE` | `TxrectRoTransactions_DateType` | TField |  | Allowed Values are . � Ex-Date � Pay Date � Value Date If set to EX DATE, then all DIARYs with EX.DATE greater than the START.DATE and less than the END.DATE would be fetched. |
| 24 | `TXRECT.RO.START.DATE` | `TxrectRoTransactions_StartDate` | TField |  | Start date of RO. |
| 25 | `TXRECT.RO.END.DATE` | `TxrectRoTransactions_EndDate` | TField |  | Start date of RO |
| 26 | `TXRECT.RO.DIARY.ID` | `TxrectRoTransactions_DiaryId` | TField |  | This field stores Diary ID on which rectification is done |
| 27 | `TXRECT.RO.INCOME.CODE` | `TxrectRoTransactions_IncomeCode` |  |  |  |
| 28 | `TXRECT.RO.INCOME.RATE` | `TxrectRoTransactions_IncomeRate` |  |  |  |
| 29 | `TXRECT.RO.INCOME.PERC` | `TxrectRoTransactions_IncomePerc` |  |  |  |
| 30 | `TXRECT.RO.TAXABLE` | `TxrectRoTransactions_Taxable` |  |  |  |
| 31 | `TXRECT.RO.REPORTABLE` | `TxrectRoTransactions_Reportable` |  |  |  |
| 32 | `TXRECT.RO.CONSOLIDATE.ENTRY` | `TxrectRoTransactions_ConsolidateEntry` | TField |  | Consolidate entry - Yes or No. |
| 33 | `TXRECT.RO.RESERVED.5` | `TxrectRoTransactions_Reserved5` | TField |  | Reserved field for future use |
| 34 | `TXRECT.RO.RESERVED.4` | `TxrectRoTransactions_Reserved4` | TField |  | Reserved field for future use |
| 35 | `TXRECT.RO.RESERVED.3` | `TxrectRoTransactions_Reserved3` | TField |  | Reserved field for future use |
| 36 | `TXRECT.RO.RESERVED.2` | `TxrectRoTransactions_Reserved2` | TField |  | Reserved field for future use |
| 37 | `TXRECT.RO.RESERVED.1` | `TxrectRoTransactions_Reserved1` | TField |  | Reserved field for future use |
| 38 | `TXRECT.RO.LOCAL.REF` | `TxrectRoTransactions_LocalRef` |  |  |  |
| 39 | `TXRECT.RO.OVERRIDE` | `TxrectRoTransactions_Override` |  |  |  |
| 40 | `TXRECT.RO.RECORD.STATUS` | `TxrectRoTransactions_RecordStatus` | String |  |  |
| 41 | `TXRECT.RO.CURR.NO` | `TxrectRoTransactions_CurrNo` | String |  |  |
| 42 | `TXRECT.RO.INPUTTER` | `TxrectRoTransactions_Inputter` |  |  |  |
| 43 | `TXRECT.RO.DATE.TIME` | `TxrectRoTransactions_DateTime` |  |  |  |
| 44 | `TXRECT.RO.AUTHORISER` | `TxrectRoTransactions_Authoriser` | String |  |  |
| 45 | `TXRECT.RO.CO.CODE` | `TxrectRoTransactions_CoCode` | String |  |  |
| 46 | `TXRECT.RO.DEPT.CODE` | `TxrectRoTransactions_DeptCode` | String |  |  |
| 47 | `TXRECT.RO.AUDITOR.CODE` | `TxrectRoTransactions_AuditorCode` | String |  |  |
| 48 | `TXRECT.RO.AUDIT.DATE.TIME` | `TxrectRoTransactions_AuditDateTime` | String |  |  |
| 49 | `TXRECT.RO.ACCOUNT` | `TxrectRoTransactions_Account` | TField |  | Internal tax account for each tax type; same as in CORE enquiry STMT.ENT.BOOK.Inputted by user |
| 50 | `TXRECT.RO.TRANSACTION.BOOKING.DATE` | `TxrectRoTransactions_TransactionBookingDate` | TField |  | Booking date of transaction; same as in CORE enquiry STMT.ENT.BOOK. Inputted by user |
| 51 | `TXRECT.RO.PROCESSING.DATE` | `TxrectRoTransactions_ProcessingDate` | TField |  | Processing date of transaction; same as in CORE enquiry STMT.ENT.BOOK. Inputted by user |
| 52 | `TXRECT.RO.OPERATION.ID` | `TxrectRoTransactions_OperationId` | TField |  | Transaction ID-Inputted by user |
| 53 | `TXRECT.RO.USER.ID` | `TxrectRoTransactions_UserId` | TField |  | Inputter/Authoriser ID from original transaction |
| 54 | `TXRECT.RO.BOOKED.TAX.AMOUNT` | `TxrectRoTransactions_BookedTaxAmount` | TField |  | Booked tax amount from STMT.ENTRY |
| 55 | `TXRECT.RO.CURRENCY` | `TxrectRoTransactions_Currency` | TField |  | transaction trade ccy |
| 56 | `TXRECT.RO.MARKET` | `TxrectRoTransactions_Market` | TField |  | Domicile of issuer of security |
| 57 | `TXRECT.RO.ENTRIES.PROCESSED` | `TxrectRoTransactions_EntriesProcessed` | TField |  | Indicates whether the record is picked up by the serivce or not. |
| 58 | `TXRECT.RO.TXN.COUNT` | `TxrectRoTransactions_TxnCount` | TField |  | Updated with rectification operation ID (Sc Income Reclassification ID) |
