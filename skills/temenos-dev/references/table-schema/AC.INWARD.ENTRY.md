# AC.INWARD.ENTRY — Table Schema

> Source: `INSERTS/I_F.AC.INWARD.ENTRY` in `ACCCSM_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACIE.ACCOUNT.NUMBER` | `AcInwardEntry_AccountNumber` | TField |  | Validation Rules: A maximum of 16 characters may be entered. |
| 2 | `ACIE.COMPANY.CODE` | `AcInwardEntry_CompanyCode` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 11 characters may be entered. Must be the key to a valid entry on the COMPANY file. |
| 3 | `ACIE.AMOUNT.LCY` | `AcInwardEntry_AmountLcy` | TField |  | Validation Rules: A maximum of 19 characters may be entered. |
| 4 | `ACIE.TRANSACTION.CODE` | `AcInwardEntry_TransactionCode` | TField | Yes | Standard T24 numeric field. Validation Rules: Mandatory input. A maximum of 3 characters may be entered. Must be the key to a valid entry on the TRANSACTION file. |
| 5 | `ACIE.THEIR.REFERENCE` | `AcInwardEntry_TheirReference` | TField |  | Validation Rules: A maximum of 16 characters may be entered. |
| 6 | `ACIE.NARRATIVE` | `AcInwardEntry_Narrative` |  |  |  |
| 7 | `ACIE.PL.CATEGORY` | `AcInwardEntry_PlCategory` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 6 characters may be entered. Must be the key to a valid entry on the CATEGORY file. |
| 8 | `ACIE.CUSTOMER.ID` | `AcInwardEntry_CustomerId` | TField |  | Standard T24 customer field. Validation Rules: A maximum of 10 characters may be entered. Must be the key to a valid entry on the CUSTOMER file. |
| 9 | `ACIE.ACCOUNT.OFFICER` | `AcInwardEntry_AccountOfficer` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 4 characters may be entered. Must be the key to a valid entry on the DEPT.ACCT.OFFICER file. |
| 10 | `ACIE.PRODUCT.CATEGORY` | `AcInwardEntry_ProductCategory` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 6 characters may be entered. Must be the key to a valid entry on the CATEGORY file. |
| 11 | `ACIE.VALUE.DATE` | `AcInwardEntry_ValueDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters may be entered. |
| 12 | `ACIE.CURRENCY` | `AcInwardEntry_Currency` | TField |  | Standard T24 currency field. Validation Rules: A maximum of 3 characters may be entered. Must be the key to a valid entry on the CURRENCY file. |
| 13 | `ACIE.AMOUNT.FCY` | `AcInwardEntry_AmountFcy` | TField |  | Validation Rules: A maximum of 19 characters may be entered. |
| 14 | `ACIE.EXCHANGE.RATE` | `AcInwardEntry_ExchangeRate` | TField |  | Standard T24 rate field. Validation Rules: A maximum of 11 characters may be entered. |
| 15 | `ACIE.NEGOTIATED.REF.NUM` | `AcInwardEntry_NegotiatedRefNum` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 5 characters may be entered. |
| 16 | `ACIE.POSITION.TYPE` | `AcInwardEntry_PositionType` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 2 characters may be entered. Must be the key to a valid entry on the FX.POS.TYPE file. |
| 17 | `ACIE.OUR.REFERENCE` | `AcInwardEntry_OurReference` | TField |  | Validation Rules: A maximum of 16 characters may be entered. |
| 18 | `ACIE.REVERSAL.MARKER` | `AcInwardEntry_ReversalMarker` | TField |  | Validation Rules: A maximum of 1 characters may be entered. The following values are permitted: R |
| 19 | `ACIE.EXPOSURE.DATE` | `AcInwardEntry_ExposureDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters may be entered. |
| 20 | `ACIE.CURRENCY.MARKET` | `AcInwardEntry_CurrencyMarket` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 1 characters may be entered. Must be the key to a valid entry on the CURRENCY.MARKET file. |
| 21 | `ACIE.LOCAL.REF` | `AcInwardEntry_LocalRef` |  |  |  |
| 22 | `ACIE.DEPARTMENT.CODE` | `AcInwardEntry_DepartmentCode` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 4 characters may be entered. This is a NOINPUT field. Must be the key to a valid entry on the DEPT.ACCT.OFFICER file. |
| 23 | `ACIE.TRANS.REFERENCE` | `AcInwardEntry_TransReference` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 25 characters may be entered. This is a NOINPUT field. |
| 24 | `ACIE.SYSTEM.ID` | `AcInwardEntry_SystemId` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 4 characters may be entered. This is a NOINPUT field. Must be the key to a valid entry on the EB.SYSTEM.ID file. |
| 25 | `ACIE.BOOKING.DATE` | `AcInwardEntry_BookingDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters may be entered. This is a NOINPUT field. |
| 26 | `ACIE.STMT.NO` | `AcInwardEntry_StmtNo` |  |  |  |
| 27 | `ACIE.OVERRIDE` | `AcInwardEntry_Override` |  |  |  |
| 28 | `ACIE.RECORD.STATUS` | `AcInwardEntry_RecordStatus` | String |  |  |
| 29 | `ACIE.CURR.NO` | `AcInwardEntry_CurrNo` | String |  |  |
| 30 | `ACIE.INPUTTER` | `AcInwardEntry_Inputter` |  |  |  |
| 31 | `ACIE.DATE.TIME` | `AcInwardEntry_DateTime` |  |  |  |
| 32 | `ACIE.AUTHORISER` | `AcInwardEntry_Authoriser` | String |  |  |
| 33 | `ACIE.SUSPENSE.CATEGORY` | `AcInwardEntry_SuspenseCategory` | TField |  | The category of the suspense account which is used when suspense entries are raised when account doesn't exist or other overrides have triggered and are not approved |
| 34 | `ACIE.SUSPNSE.VALUE.DATE` | `AcInwardEntry_SuspnseValueDate` | TField |  | The value date assigned to the suspense entry |
| 35 | `ACIE.SUPPRESS.POSITION` | `AcInwardEntry_SuppressPosition` | TField |  | Specifies whether the entry which has been raise will be be considered when calculating the effect on the Position file. |
| 36 | `ACIE.CRF.TYPE` | `AcInwardEntry_CrfType` | TField |  | Indicates the CRF Asset Type which corresponds to the 'other' side of the accounting entry. |
| 37 | `ACIE.CRF.TXN.CODE` | `AcInwardEntry_CrfTxnCode` | TField |  | The transaction code to be used for the CRF movement for the CRF.TYPE. |
| 38 | `ACIE.CRF.CURRENCY` | `AcInwardEntry_CrfCurrency` | TField |  | The currency for which the CRF movement is to be raised, if different to the currency of the entry. |
| 39 | `ACIE.CONSOL.KEY` | `AcInwardEntry_ConsolKey` | TField |  | This is the consolidation key associated with the entry |
| 40 | `ACIE.CRF.MAT.DATE` | `AcInwardEntry_CrfMatDate` | TField |  | The maturity date associated with the resultant CRF entry. This date may be present where maturity splitting of CRF date is required. |
| 41 | `ACIE.CRF.PROD.CAT` | `AcInwardEntry_CrfProdCat` | TField |  | This field is used to store the product category code associated with the contract for which the entry has been raised |
| 42 | `ACIE.PM.TYPE` | `AcInwardEntry_PmType` | TField |  | The position management type which is updated by the entry |
| 43 | `ACIE.DEALER.DESK` | `AcInwardEntry_DealerDesk` | TField |  | The dealer desk for the entry when a currency conversion has been involved |
| 44 | `ACIE.COUNTERPARTY` | `AcInwardEntry_Counterparty` | TField |  | Identifies the counterparty with whom the Bank has arranged a transaction. Must refer a valid customer number |
| 45 | `ACIE.ERROR.MESSAGE` | `AcInwardEntry_ErrorMessage` |  |  |  |
| 46 | `ACIE.SUSP.REASON` | `AcInwardEntry_SuspReason` |  |  |  |
| 47 | `ACIE.SUSP.FT.ID` | `AcInwardEntry_SuspFtId` | TField |  | The id of the FT which has been raised for suspense entries |
| 48 | `ACIE.ENTRY.POSTED` | `AcInwardEntry_EntryPosted` | TField |  | Identifies if the entry has been posted or not |
| 49 | `ACIE.DRAFT.PAYEE.NAME` | `AcInwardEntry_DraftPayeeName` | TField |  | The payee name for a draft transaction |
| 50 | `ACIE.SIGN` | `AcInwardEntry_Sign` | TField |  |  |
| 51 | `ACIE.ADD.DETAIL.REQUEST.SOURCE` | `AcInwardEntry_AddDetailRequestSource` | TField |  |  |
| 52 | `ACIE.ORIGINAL.ACCOUNT` | `AcInwardEntry_OriginalAccount` | TField |  | This fied stores Original account when entry is suspended Validation Rules: A maximum of 35 characters will be allowed. |
| 53 | `ACIE.RESERVATION.KEY` | `AcInwardEntry_ReservationKey` | TField |  | This field is used to store the reservation key passed in clearing message of BOOK requests. Validation Rules: A maximum of 35 characters will be allowed. |
| 54 | `ACIE.REQUEST.TYPE` | `AcInwardEntry_RequestType` | TField |  | Store request type it can be COVER,RESERVE,BOOK or Null for old clearing formats Validation Rules: A maximum of 35 characters will be allowed. |
| 55 | `ACIE.SESSION.NO` | `AcInwardEntry_SessionNo` | TField |  | Store OFS Session no. Useful information in case we wanted to pull report based on session Validation Rules: A maximum of 35 characters will be allowed. |
| 56 | `ACIE.CLEARING.RESULT` | `AcInwardEntry_ClearingResult` | TField |  | Holds values- SUCCESS, FAIL for the entry Validation Rules: A maximum of 35 characters will be allowed. |
| 57 | `ACIE.UNIQUE.BATCH.REF` | `AcInwardEntry_UniqueBatchRef` | TField |  | Uniqe id formed by system for batch clearing, this will be the ID of the header batch item, to link the child transactions with header. Validation Rules: A maximum of 66 characters will be allowed. Will be populated only for the transactions part of a batch. This will be the link to the record which stores the batch header details. |
| 58 | `ACIE.EXTERNAL.BATCH.REF` | `AcInwardEntry_ExternalBatchRef` | TField |  | To have uniqe identification of external batch , it can be given in string by user Validation Rules: A maximum of 35 characters will be allowed. The batch reference provided in the batch message, if any Will be populated in the batch entry but also in the individual ones. |
| 59 | `ACIE.NO.TXN.BATCH` | `AcInwardEntry_NoTxnBatch` | TField |  | Total number of transaction in the batch message Validation Rules: A maximum of 5 characters will be allowed. |
| 60 | `ACIE.STATUS` | `AcInwardEntry_Status` | TField |  | Will be updated as 'Error' when the batch is rejected because of technical error otherwise ,Ready when it is for processing individual message,Complete once all the messages in that particular batch is processed APPROVALRQ - when a reservation request is moved to manual funds authorisation. Validation Rules: A maximum of 10 characters will be allowed. |
| 61 | `ACIE.NO.SUCCESS.TXN` | `AcInwardEntry_NoSuccessTxn` | TField |  | Number of successful transaction Validation Rules: A maximum of 5 characters will be allowed. |
| 62 | `ACIE.NO.REJECT.TXN` | `AcInwardEntry_NoRejectTxn` | TField |  | Number of rejected transaction Validation Rules: A maximum of 5 characters will be allowed. |
| 63 | `ACIE.NO.SUSP.TXN` | `AcInwardEntry_NoSuspTxn` | TField |  | Number of suspended transaction Validation Rules: A maximum of 5 characters will be allowed. |
| 64 | `ACIE.PARENT.REQUEST.TYPE` | `AcInwardEntry_ParentRequestType` | TField |  | To identify the request type of the batch. Validation Rules: To denote in child data messages whether the parent is from CSMBATCH. A maximum of 15 characters will be allowed. |
| 65 | `ACIE.SPLIT.EXPOSURE.DATE` | `AcInwardEntry_AcieSplitExposureDate` |  |  |  |
| 66 | `ACIE.SPLIT.EXPOSURE.AMT` | `AcInwardEntry_AcieSplitExposureAmt` |  |  |  |
| 67 | `ACIE.AC.FUNDS.AUTH.ID` | `AcInwardEntry_AcieAcFundsAuthId` |  |  |  |
| 68 | `ACIE.ORIG.RAW.ENTRY` | `AcInwardEntry_AcieOrigRawEntry` |  |  |  |
| 69 | `ACIE.CLEARING.APP.NAME` | `AcInwardEntry_AcieClearingAppName` |  |  |  |
| 70 | `ACIE.FA.STATUS` | `AcInwardEntry_AcieFaStatus` |  |  |  |
| 71 | `ACIE.REQUEST.AMOUNT` | `AcInwardEntry_AcieRequestAmount` |  |  |  |
| 72 | `ACIE.REQUEST.CURRENCY` | `AcInwardEntry_AcieRequestCurrency` |  |  |  |
| 73 | `ACIE.EXTERNAL.SEPA.ID` | `AcInwardEntry_ExternalSepaId` | TField |  |  |
| 74 | `ACIE.JOURNAL.ID` | `AcInwardEntry_JournalId` | TField |  | The unique identifier of the incremental authorization. |
| 75 | `ACIE.PARTIAL.BOOKING` | `AcInwardEntry_PartialBooking` | TField |  | Flag to indicate if partial booking is opted or not. Identifies if a reservation is flagged as a partial payment for booking. Can be YES, NO or Null based on the value of PARTIAL.BOOKING data item that is passed in the clearing string. |
| 76 | `ACIE.UPDATE.MODE` | `AcInwardEntry_UpdateMode` | TField |  | Indicates the type of update to be performed on the locked amount. Can be either ADD, SUBTRACT, SET or Null based on the value of UPDATE.MODE data item that is passed in the clearing string. SET - The Amount in the clearing string replaces the existing reservation amount. ADD - The Amount in the clearing string will be added to existing reservation amount. SUBTRACT - The Amount in the clearing string will be subtracted from existing reservation amount. SET and Null are the same. |
| 77 | `ACIE.SUB.ACCOUNT` | `AcInwardEntry_SubAccount` | TField |  | The field indicates the sub account used for posting the request for the multi currency parent account received |
| 78 | `ACIE.MATCH.RES.STATUS` | `AcInwardEntry_MatchResStatus` | TField |  | Identifies if the reservation passed at booking was found or not. Valid Options are FOUND, NOT.FOUND or BEST.MATCH |
| 79 | `ACIE.RELEASED.RESERVES` | `AcInwardEntry_ReleasedReserves` |  |  |  |
| 80 | `ACIE.ORIG.CCY.MARKET` | `AcInwardEntry_AcieOrigCcyMarket` |  |  |  |
| 81 | `ACIE.REQUESTOR.SYSTEM.ID` | `AcInwardEntry_AcieRequestorSystemId` |  |  |  |
| 82 | `ACIE.REQUESTOR.COMPANY.ID` | `AcInwardEntry_AcieRequestorCompanyId` |  |  |  |
| 83 | `ACIE.REQUESTOR.ACCOUNT.ID` | `AcInwardEntry_AcieRequestorAccountId` |  |  |  |
| 84 | `ACIE.CALL.BACK.ACTIVITY` | `AcInwardEntry_AcieCallBackActivity` |  |  |  |
| 85 | `ACIE.EXT.EVENT.STATUS` | `AcInwardEntry_AcieExtEventStatus` |  |  |  |
