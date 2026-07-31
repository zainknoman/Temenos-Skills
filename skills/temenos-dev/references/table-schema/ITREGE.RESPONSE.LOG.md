# ITREGE.RESPONSE.LOG — Table Schema

> Source: `INSERTS/I_F.ITREGE.RESPONSE.LOG` in `ITREGE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ITREGE.RESPONSE.LOG.RESPONSE.TYPE` | `ItregeResponseLog_ResponseType` | TField |  | The type of the response has been stored in this filed |
| 2 | `ITREGE.RESPONSE.LOG.BANK.CODE` | `ItregeResponseLog_BankCode` | TField |  | The numeric code for the branch will be stored in this field |
| 3 | `ITREGE.RESPONSE.LOG.DATE` | `ItregeResponseLog_Date` | TField |  | Response received date has been stored |
| 4 | `ITREGE.RESPONSE.LOG.OPERATOR` | `ItregeResponseLog_Operator` | TField |  | This field denotes the operator code of initiator |
| 5 | `ITREGE.RESPONSE.LOG.RECORD.NUMBER` | `ItregeResponseLog_RecordNumber` | TField |  | The unique value of the record |
| 6 | `ITREGE.RESPONSE.LOG.ERROR.CODE` | `ItregeResponseLog_ErrorCode` |  |  |  |
| 7 | `ITREGE.RESPONSE.LOG.ERROR.DESCRIPTION` | `ItregeResponseLog_ErrorDescription` |  |  |  |
| 8 | `ITREGE.RESPONSE.LOG.CUSTOMER.ID` | `ItregeResponseLog_CustomerId` | TField |  | The customer who initiate the transaction |
| 9 | `ITREGE.RESPONSE.LOG.PRI.SEC.CUSTOMER` | `ItregeResponseLog_PriSecCustomer` | TField |  | The secondary customer details will be stored in this field |
| 10 | `ITREGE.RESPONSE.LOG.CUST.LINK.TYPE` | `ItregeResponseLog_CustLinkType` | TField |  | The link type of the customers will be stored in this field |
| 11 | `ITREGE.RESPONSE.LOG.ACCOUNT.ID` | `ItregeResponseLog_AccountId` | TField |  | The account number from the response file is stored in this field |
| 12 | `ITREGE.RESPONSE.LOG.ACC.CUST.LINK` | `ItregeResponseLog_AccCustLink` | TField |  | The customer and account link value will be stored in this field |
| 13 | `ITREGE.RESPONSE.LOG.ACC.CUST.LINK.TYPE` | `ItregeResponseLog_AccCustLinkType` | TField |  | The Link type off the customer and account will be stored in this field |
| 14 | `ITREGE.RESPONSE.LOG.REGISTRATION.OPR` | `ItregeResponseLog_RegistrationOpr` | TField |  | This field holds the Registration Type value |
| 15 | `ITREGE.RESPONSE.LOG.TXN.UPLOAD.STATUS` | `ItregeResponseLog_TxnUploadStatus` | TField |  | This field holds the Transaction Upload Status |
| 16 | `ITREGE.RESPONSE.LOG.RECORDING.STATUS` | `ItregeResponseLog_RecordingStatus` | TField |  | Recording status loaded in SIA�s Register: N = Complete registration S = Incomplete registration |
| 17 | `ITREGE.RESPONSE.LOG.ERR.GT.20.INDICATOR` | `ItregeResponseLog_ErrGt20Indicator` | TField |  | Indicator of the number of incompleteness codes greater than 20 for incomplete registrations S = Registration with more than 20 incompleteness codes |
| 18 | `ITREGE.RESPONSE.LOG.REGISTRATION.STATUS` | `ItregeResponseLog_RegistrationStatus` | TField |  | Registration status of transaction. 00 = Complete registration Not equal to 00 = Registration incomplete |
| 19 | `ITREGE.RESPONSE.LOG.TRANSACTION.DATE` | `ItregeResponseLog_TransactionDate` | TField |  | Transaction/relationship event/link event date will be stored in this field |
| 20 | `ITREGE.RESPONSE.LOG.TRANSACTION.ID` | `ItregeResponseLog_TransactionId` | TField |  | Transaction (or relationship or link) ID will be stored in this field |
| 21 | `ITREGE.RESPONSE.LOG.TRANSACTION.AMT` | `ItregeResponseLog_TransactionAmt` | TField |  | Transaction Amount will be stored in this field |
| 22 | `ITREGE.RESPONSE.LOG.REGISTRATION.TYPE` | `ItregeResponseLog_RegistrationType` | TField |  | Registration Type of Transaction will be stored in this field |
| 23 | `ITREGE.RESPONSE.LOG.INTERNAL.KEY` | `ItregeResponseLog_InternalKey` | TField |  | Internal Key of the Record |
| 24 | `ITREGE.RESPONSE.LOG.COMPLETE.RECORD` | `ItregeResponseLog_CompleteRecord` |  |  |  |
| 25 | `ITREGE.RESPONSE.LOG.DELAY.TXN.INDICATOR` | `ItregeResponseLog_DelayTxnIndicator` | TField |  | Delay Transaction Indicator |
