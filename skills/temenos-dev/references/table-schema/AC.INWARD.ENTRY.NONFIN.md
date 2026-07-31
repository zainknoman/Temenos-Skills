# AC.INWARD.ENTRY.NONFIN — Table Schema

> Source: `INSERTS/I_F.AC.INWARD.ENTRY.NONFIN` in `ACCCSM_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACIE.ACCOUNT.NUMBER` | `AcInwardEntryNonfin_AccountNumber` | TField |  | Validation Rules: A maximum of 16 characters may be entered. |
| 2 | `ACIE.COMPANY.CODE` | `AcInwardEntryNonfin_CompanyCode` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 11 characters may be entered. Must be the key to a valid entry on the COMPANY file. |
| 3 | `ACIE.AMOUNT.LCY` | `AcInwardEntryNonfin_AmountLcy` | TField |  | Validation Rules: A maximum of 19 characters may be entered. |
| 4 | `ACIE.TRANSACTION.CODE` | `AcInwardEntryNonfin_TransactionCode` | TField | Yes | Standard T24 numeric field. Validation Rules: Mandatory input. A maximum of 3 characters may be entered. Must be the key to a valid entry on the TRANSACTION file. |
| 5 | `ACIE.THEIR.REFERENCE` | `AcInwardEntryNonfin_TheirReference` | TField |  | Validation Rules: A maximum of 16 characters may be entered. |
| 6 | `ACIE.NARRATIVE` | `AcInwardEntryNonfin_Narrative` |  |  |  |
| 7 | `ACIE.PL.CATEGORY` | `AcInwardEntryNonfin_PlCategory` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 6 characters may be entered. Must be the key to a valid entry on the CATEGORY file. |
| 8 | `ACIE.CUSTOMER.ID` | `AcInwardEntryNonfin_CustomerId` | TField |  | Standard T24 customer field. Validation Rules: A maximum of 10 characters may be entered. Must be the key to a valid entry on the CUSTOMER file. |
| 9 | `ACIE.ACCOUNT.OFFICER` | `AcInwardEntryNonfin_AccountOfficer` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 4 characters may be entered. Must be the key to a valid entry on the DEPT.ACCT.OFFICER file. |
| 10 | `ACIE.PRODUCT.CATEGORY` | `AcInwardEntryNonfin_ProductCategory` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 6 characters may be entered. Must be the key to a valid entry on the CATEGORY file. |
| 11 | `ACIE.VALUE.DATE` | `AcInwardEntryNonfin_ValueDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters may be entered. |
| 12 | `ACIE.CURRENCY` | `AcInwardEntryNonfin_Currency` | TField |  | Standard T24 currency field. Validation Rules: A maximum of 3 characters may be entered. Must be the key to a valid entry on the CURRENCY file. |
| 13 | `ACIE.AMOUNT.FCY` | `AcInwardEntryNonfin_AmountFcy` | TField |  | Validation Rules: A maximum of 19 characters may be entered. |
| 14 | `ACIE.EXCHANGE.RATE` | `AcInwardEntryNonfin_ExchangeRate` | TField |  | Standard T24 rate field. Validation Rules: A maximum of 11 characters may be entered. |
| 15 | `ACIE.NEGOTIATED.REF.NUM` | `AcInwardEntryNonfin_NegotiatedRefNum` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 5 characters may be entered. |
| 16 | `ACIE.POSITION.TYPE` | `AcInwardEntryNonfin_PositionType` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 2 characters may be entered. Must be the key to a valid entry on the FX.POS.TYPE file. |
| 17 | `ACIE.OUR.REFERENCE` | `AcInwardEntryNonfin_OurReference` | TField |  | Validation Rules: A maximum of 16 characters may be entered. |
| 18 | `ACIE.REVERSAL.MARKER` | `AcInwardEntryNonfin_ReversalMarker` | TField |  | Validation Rules: A maximum of 1 characters may be entered. The following values are permitted: R |
| 19 | `ACIE.EXPOSURE.DATE` | `AcInwardEntryNonfin_ExposureDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters may be entered. |
| 20 | `ACIE.CURRENCY.MARKET` | `AcInwardEntryNonfin_CurrencyMarket` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 1 characters may be entered. Must be the key to a valid entry on the CURRENCY.MARKET file. |
| 21 | `ACIE.LOCAL.REF` | `AcInwardEntryNonfin_LocalRef` |  |  |  |
| 22 | `ACIE.DEPARTMENT.CODE` | `AcInwardEntryNonfin_DepartmentCode` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 4 characters may be entered. This is a NOINPUT field. Must be the key to a valid entry on the DEPT.ACCT.OFFICER file. |
| 23 | `ACIE.TRANS.REFERENCE` | `AcInwardEntryNonfin_TransReference` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 25 characters may be entered. This is a NOINPUT field. |
| 24 | `ACIE.SYSTEM.ID` | `AcInwardEntryNonfin_SystemId` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 4 characters may be entered. This is a NOINPUT field. Must be the key to a valid entry on the EB.SYSTEM.ID file. |
| 25 | `ACIE.BOOKING.DATE` | `AcInwardEntryNonfin_BookingDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters may be entered. This is a NOINPUT field. |
| 26 | `ACIE.STMT.NO` | `AcInwardEntryNonfin_StmtNo` |  |  |  |
| 27 | `ACIE.OVERRIDE` | `AcInwardEntryNonfin_Override` |  |  |  |
| 28 | `ACIE.RECORD.STATUS` | `AcInwardEntryNonfin_RecordStatus` | String |  |  |
| 29 | `ACIE.CURR.NO` | `AcInwardEntryNonfin_CurrNo` | String |  |  |
| 30 | `ACIE.INPUTTER` | `AcInwardEntryNonfin_Inputter` |  |  |  |
| 31 | `ACIE.DATE.TIME` | `AcInwardEntryNonfin_DateTime` |  |  |  |
| 32 | `ACIE.AUTHORISER` | `AcInwardEntryNonfin_Authoriser` | String |  |  |
| 33 | `ACIE.SUSPENSE.CATEGORY` | `AcInwardEntryNonfin_SuspenseCategory` | TField |  | The category of the suspense account which is used when suspense entries are raised when account doesn't exist or other overrides have triggered and are not approved |
| 34 | `ACIE.SUSPNSE.VALUE.DATE` | `AcInwardEntryNonfin_SuspnseValueDate` | TField |  | The value date assigned to the suspense entry |
| 35 | `ACIE.SUPPRESS.POSITION` | `AcInwardEntryNonfin_SuppressPosition` | TField |  | Specifies whether the entry which has been raise will be be considered when calculating the effect on the Position file. |
| 36 | `ACIE.CRF.TYPE` | `AcInwardEntryNonfin_CrfType` | TField |  | Indicates the CRF Asset Type which corresponds to the 'other' side of the accounting entry. |
| 37 | `ACIE.CRF.TXN.CODE` | `AcInwardEntryNonfin_CrfTxnCode` | TField |  | The transaction code to be used for the CRF movement for the CRF.TYPE. |
| 38 | `ACIE.CRF.CURRENCY` | `AcInwardEntryNonfin_CrfCurrency` | TField |  | The currency for which the CRF movement is to be raised, if different to the currency of the entry. |
| 39 | `ACIE.CONSOL.KEY` | `AcInwardEntryNonfin_ConsolKey` | TField |  | This is the consolidation key associated with the entry |
| 40 | `ACIE.CRF.MAT.DATE` | `AcInwardEntryNonfin_CrfMatDate` | TField |  | The maturity date associated with the resultant CRF entry. This date may be present where maturity splitting of CRF date is required. |
| 41 | `ACIE.CRF.PROD.CAT` | `AcInwardEntryNonfin_CrfProdCat` | TField |  | This field is used to store the product category code associated with the contract for which the entry has been raised |
| 42 | `ACIE.PM.TYPE` | `AcInwardEntryNonfin_PmType` | TField |  | The position management type which is updated by the entry |
| 43 | `ACIE.DEALER.DESK` | `AcInwardEntryNonfin_DealerDesk` | TField |  | The dealer desk for the entry when a currency conversion has been involved |
| 44 | `ACIE.COUNTERPARTY` | `AcInwardEntryNonfin_Counterparty` | TField |  | Identifies the counterparty with whom the Bank has arranged a transaction. Must refer a valid customer number |
| 45 | `ACIE.ERROR.MESSAGE` | `AcInwardEntryNonfin_ErrorMessage` |  |  |  |
| 46 | `ACIE.SUSP.REASON` | `AcInwardEntryNonfin_SuspReason` |  |  |  |
| 47 | `ACIE.SUSP.FT.ID` | `AcInwardEntryNonfin_SuspFtId` | TField |  | The id of the FT which has been raised for suspense entries |
| 48 | `ACIE.ENTRY.POSTED` | `AcInwardEntryNonfin_EntryPosted` | TField |  | Identifies if the entry has been posted or not |
| 49 | `ACIE.DRAFT.PAYEE.NAME` | `AcInwardEntryNonfin_DraftPayeeName` | TField |  | The payee name for a draft transaction |
| 50 | `ACIE.SIGN` | `AcInwardEntryNonfin_Sign` | TField |  |  |
| 51 | `ACIE.ADD.DETAIL.REQUEST.SOURCE` | `AcInwardEntryNonfin_AddDetailRequestSource` | TField |  |  |
| 52 | `ACIE.ORIGINAL.ACCOUNT` | `AcInwardEntryNonfin_OriginalAccount` | TField |  | This fied stores Original account when entry is suspended Validation Rules: A maximum of 35 characters will be allowed. |
| 53 | `ACIE.RESERVATION.KEY` | `AcInwardEntryNonfin_ReservationKey` | TField |  | This field is used to store the reservation key passed in clearing message of BOOK requests. Validation Rules: A maximum of 35 characters will be allowed. |
| 54 | `ACIE.REQUEST.TYPE` | `AcInwardEntryNonfin_RequestType` | TField |  | Store request type it can be COVER,RESERVE,BOOK or Null for old clearing formats Validation Rules: A maximum of 35 characters will be allowed. |
| 55 | `ACIE.SESSION.NO` | `AcInwardEntryNonfin_SessionNo` | TField |  | Store OFS Session no. Useful information in case we wanted to pull report based on session Validation Rules: A maximum of 35 characters will be allowed. |
| 56 | `ACIE.CLEARING.RESULT` | `AcInwardEntryNonfin_ClearingResult` | TField |  | Holds values- SUCCESS, FAIL for the entry Validation Rules: A maximum of 35 characters will be allowed. |
| 57 | `ACIE.UNIQUE.BATCH.REF` | `AcInwardEntryNonfin_UniqueBatchRef` | TField |  | Uniqe id formed by system for batch clearing, this will be the ID of the header batch item, to link the child transactions with header. Validation Rules: A maximum of 66 characters will be allowed. Will be populated only for the transactions part of a batch. This will be the link to the record which stores the batch header details. |
| 58 | `ACIE.EXTERNAL.BATCH.REF` | `AcInwardEntryNonfin_ExternalBatchRef` | TField |  | To have uniqe identification of external batch , it can be given in string by user Validation Rules: A maximum of 35 characters will be allowed. The batch reference provided in the batch message, if any Will be populated in the batch entry but also in the individual ones. |
| 59 | `ACIE.NO.TXN.BATCH` | `AcInwardEntryNonfin_NoTxnBatch` | TField |  | Total number of transaction in the batch message Validation Rules: A maximum of 5 characters will be allowed. |
| 60 | `ACIE.STATUS` | `AcInwardEntryNonfin_Status` | TField |  | Will be updated as 'Error' when the batch is rejected because of technical error otherwise ,Ready when it is for processing individual message,Complete once all the messages in that particular batch is processed. Validation Rules: A maximum of 10 characters will be allowed. |
| 61 | `ACIE.NO.SUCCESS.TXN` | `AcInwardEntryNonfin_NoSuccessTxn` | TField |  | Number of successful transaction Validation Rules: A maximum of 5 characters will be allowed. |
| 62 | `ACIE.NO.REJECT.TXN` | `AcInwardEntryNonfin_NoRejectTxn` | TField |  | Number of rejected transaction Validation Rules: A maximum of 5 characters will be allowed. |
| 63 | `ACIE.NO.SUSP.TXN` | `AcInwardEntryNonfin_NoSuspTxn` | TField |  | Number of suspended transaction Validation Rules: A maximum of 5 characters will be allowed. |
| 64 | `ACIE.PARENT.REQUEST.TYPE` | `AcInwardEntryNonfin_ParentRequestType` | TField |  | To identify the request type of the batch. Validation Rules: To denote in child data messages whether the parent is from CSMBATCH. A maximum of 15 characters will be allowed. |
| 65 | `ACIE.SPLIT.EXPOSURE.DATE` | `AcInwardEntryNonfin_AcieSplitExposureDate` |  |  |  |
| 66 | `ACIE.SPLIT.EXPOSURE.AMT` | `AcInwardEntryNonfin_AcieSplitExposureAmt` |  |  |  |
| 67 | `ACIE.AC.FUNDS.AUTH.ID` | `AcInwardEntryNonfin_AcieAcFundsAuthId` |  |  |  |
| 68 | `ACIE.ORIG.RAW.ENTRY` | `AcInwardEntryNonfin_AcieOrigRawEntry` |  |  |  |
| 69 | `ACIE.CLEARING.APP.NAME` | `AcInwardEntryNonfin_AcieClearingAppName` |  |  |  |
| 70 | `ACIE.FA.STATUS` | `AcInwardEntryNonfin_AcieFaStatus` |  |  |  |
| 71 | `ACIE.REQUEST.AMOUNT` | `AcInwardEntryNonfin_AcieRequestAmount` |  |  |  |
| 72 | `ACIE.REQUEST.CURRENCY` | `AcInwardEntryNonfin_AcieRequestCurrency` |  |  |  |
| 73 | `ACIE.EXTERNAL.SEPA.ID` | `AcInwardEntryNonfin_ExternalSepaId` | TField |  |  |
| 74 | `ACIE.JOURNAL.ID` | `AcInwardEntryNonfin_JournalId` | TField |  | The unique identifier of the incremental authorization. |
| 75 | `ACIE.PARTIAL.BOOKING` | `AcInwardEntryNonfin_PartialBooking` | TField |  | Flag to indicate if partial booking is opted or not. Identifies if a reservation is flagged as a partial payment for booking. Can be YES, NO or Null based on the value of PARTIAL.BOOKING data item that is passed in the clearing string. |
| 76 | `ACIE.UPDATE.MODE` | `AcInwardEntryNonfin_UpdateMode` | TField |  | Indicates the type of update to be performed on the locked amount. Can be either ADD, SUBTRACT, SET or Null based on the value of UPDATE.MODE data item that is passed in the clearing string. SET - The Amount in the clearing string replaces the existing reservation amount. ADD - The Amount in the clearing string will be added to existing reservation amount. SUBTRACT - The Amount in the clearing string will be subtracted from existing reservation amount. SET and Null are the same. |
| 77 | `ACIE.SUB.ACCOUNT` | `AcInwardEntryNonfin_SubAccount` | TField |  | The field indicates the sub account used for posting the request for the multi currency parent account received |
| 78 | `ACIE.MATCH.RES.STATUS` | `AcInwardEntryNonfin_MatchResStatus` | TField |  | Identifies if the reservation passed at booking was found or not. Valid Options are FOUND, NOT.FOUND or BEST.MATCH |
| 79 | `ACIE.RELEASED.RESERVES` | `AcInwardEntryNonfin_ReleasedReserves` |  |  |  |
| 80 | `ACIE.ORIG.CCY.MARKET` | `AcInwardEntryNonfin_AcieOrigCcyMarket` |  |  |  |
| 81 | `ACIE.REQUESTOR.SYSTEM.ID` | `AcInwardEntry_AcieRequestorSystemId` |  |  |  |
| 82 | `ACIE.REQUESTOR.COMPANY.ID` | `AcInwardEntry_AcieRequestorCompanyId` |  |  |  |
| 83 | `ACIE.REQUESTOR.ACCOUNT.ID` | `AcInwardEntry_AcieRequestorAccountId` |  |  |  |
| 84 | `ACIE.CALL.BACK.ACTIVITY` | `AcInwardEntry_AcieCallBackActivity` |  |  |  |
