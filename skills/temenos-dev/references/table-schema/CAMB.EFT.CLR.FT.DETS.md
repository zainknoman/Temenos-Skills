# CAMB.EFT.CLR.FT.DETS — Table Schema

> Source: `INSERTS/I_F.CAMB.EFT.CLR.FT.DETS` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.EFT.DETS.FT.REF` | `CambEftClrFtDets_FtRef` | TField |  | this Field will hold the FT ID once the transaction is successful.Valid records of FUNDS.TRANSFER |
| 2 | `CAMB.EFT.DETS.DEBIT.ACCOUNT` | `CambEftClrFtDets_DebitAccount` | TField |  | Field will hold debit account number. For a DR record type this field will be customer's account and for CR record type , this field will a GL account number defined in CAMB.EFT.CLR.MAPmapped from the FT record. |
| 3 | `CAMB.EFT.DETS.CREDIT.ACCOUNT` | `CambEftClrFtDets_CreditAccount` | TField |  | This Field will hold Credit account number. For a CR record type this field will be customer's account and for DR record type , this field will a GL account number defined in CAMB.EFT.CLR.MAPmapped from the FT record. |
| 4 | `CAMB.EFT.DETS.TRANSIT` | `CambEftClrFtDets_Transit` | TField |  | Field will hold the last five digits of the transit ID associated with account being debited / credited.Mapped from the incoming file. |
| 5 | `CAMB.EFT.DETS.INSTITUTION` | `CambEftClrFtDets_Institution` | TField |  | This field will hold the institution identification.Mapped from the incoming file.(Position 44-52) |
| 6 | `CAMB.EFT.DETS.CURRENCY` | `CambEftClrFtDets_Currency` | TField |  | This Field will hold the account currency.Mapped from the incoming file. |
| 7 | `CAMB.EFT.DETS.TXN.AMOUNT` | `CambEftClrFtDets_TxnAmount` | TField |  | Field will hold the amount value (taken from incoming file)mapped from the incoming file. |
| 8 | `CAMB.EFT.DETS.CLEAR.FILE.AMT` | `CambEftClrFtDets_ClearFileAmt` | TField |  | Holds the amount value (taken from incoming file)mapped from the incoming file. |
| 9 | `CAMB.EFT.DETS.PROCESSING.DATE` | `CambEftClrFtDets_ProcessingDate` | TField |  | Holds the processing date of transaction.Date on which the file is proessed . (T24 date) |
| 10 | `CAMB.EFT.DETS.VALUE.DATE` | `CambEftClrFtDets_ValueDate` | TField |  | Field which Holds the value date of transaction.Mapped from the incoming file.In case of back value dated, system post the transactions with value date = current date -(minus) 1egToday's date - 15 dec 2018Value date - 10 dec 2018system will post the transaction with value dat as 14 dec 2018 |
| 11 | `CAMB.EFT.DETS.FT.TXN.TYPE` | `CambEftClrFtDets_FtTxnType` | TField |  | Field will contain FT.TXN.TYPE.CONDITION of the underlying posted FT transaction.Mapped from FUNDS.TRANSFER |
| 12 | `CAMB.EFT.DETS.CR.DR.FLAG` | `CambEftClrFtDets_CrDrFlag` | TField |  | Field which holds the debit credit indicator of the transaction.Mapped from CAMB.EFT.CLR.MAP |
| 13 | `CAMB.EFT.DETS.TXN.STATUS` | `CambEftClrFtDets_TxnStatus` | TField |  | Field which holds the transaction status of the transactions processed during clearing.Possible fields values are CLEARED_NOT POSTED_REDIRECTED_REJECTEDCLEARED: transaction successfully posted.NOT POSTED: transaction not posted due to error.REDIRECTED: transction posted to a redirected account if the incoming file acount has a record in CAPL.H.CLR.REDIRECT.ACCTREJECTED: transaction not posted due to validation failuer. |
| 14 | `CAMB.EFT.DETS.TXN.COMMENT` | `CambEftClrFtDets_TxnComment` | TField |  | field which holds transaction comment updated from FT.eg. If account is successfully processed - ''Posted to account 6000017955''If account is successfully processed to a redirect account - ''''Posted to account 6000017992'' |
| 15 | `CAMB.EFT.DETS.ORIGINATOR.NUMBER` | `CambEftClrFtDets_OriginatorNumber` | TField |  |  |
| 16 | `CAMB.EFT.DETS.ORIGINATOR.NAME` | `CambEftClrFtDets_OriginatorName` | TField |  | Field which holds Originator short name.Mapped from the incoming file. |
| 17 | `CAMB.EFT.DETS.SEQUENCE.NUMBER` | `CambEftClrFtDets_SequenceNumber` | TField |  | field which hold the sequence number of the file.Mapped from the incoming file |
| 18 | `CAMB.EFT.DETS.RECORD.TYPE` | `CambEftClrFtDets_RecordType` | TField |  | Field which store the Record type used for processing the transaction.Mapped from the incoming file.Values shall be 'c', 'd', 'I', 'j' |
| 19 | `CAMB.EFT.DETS.REV.STATUS` | `CambEftClrFtDets_RevStatus` | TField |  | Field which holds the reversal status of transaction. Applciable only when the underlying FT is reversed.Value will be ''REVERSE'' |
| 20 | `CAMB.EFT.DETS.REVERSED.DATE` | `CambEftClrFtDets_ReversedDate` | TField |  | Field which holds the reversal date of transaction. Applciable only when the underlying FT is reversed.Valid date. |
| 21 | `CAMB.EFT.DETS.INCOMING.ACCT` | `CambEftClrFtDets_IncomingAcct` | TField |  | Incoming account to be used for Selection.Account mapped from the incoming file.Even when the account is processed to a redirect account, this field will be mapped to the incoming account reference from the incoming file. |
| 22 | `CAMB.EFT.DETS.IN.FILE.DATE` | `CambEftClrFtDets_InFileDate` | TField |  | Incoming value date to be captured and this will be used as a selection criteria for the Enquiry.Used for reporting purpose.This date is the T24 date on which the file is processed. |
| 23 | `CAMB.EFT.DETS.IN.FIELD.NO` | `CambEftClrFtDets_InFieldNo` |  |  |  |
| 24 | `CAMB.EFT.DETS.IN.FIELD.VALUE` | `CambEftClrFtDets_InFieldValue` |  |  |  |
| 25 | `CAMB.EFT.DETS.RESERVED.10` | `CambEftClrFtDets_Reserved10` |  |  |  |
| 26 | `CAMB.EFT.DETS.RESERVED.9` | `CambEftClrFtDets_Reserved9` |  |  |  |
| 27 | `CAMB.EFT.DETS.IN.RAW.VALUE` | `CambEftClrFtDets_InRawValue` |  |  |  |
| 28 | `CAMB.EFT.DETS.RET.FT.REF` | `CambEftClrFtDets_RetFtRef` | TField |  | Field will hold the FT reference when a retun file is processed .Return FT id to be used for Processing. |
| 29 | `CAMB.EFT.DETS.RET.TXN.TYPE` | `CambEftClrFtDets_RetTxnType` | TField |  | Field will store the transaction type used for Processing the Return Item Transaction |
| 30 | `CAMB.EFT.DETS.RET.DEBIT.ACC` | `CambEftClrFtDets_RetDebitAcc` | TField |  |  |
| 31 | `CAMB.EFT.DETS.RET.CREDIT.ACC` | `CambEftClrFtDets_RetCreditAcc` | TField |  |  |
| 32 | `CAMB.EFT.DETS.RESERVED.8` | `CambEftClrFtDets_Reserved8` | TField |  |  |
| 33 | `CAMB.EFT.DETS.RESERVED.7` | `CambEftClrFtDets_Reserved7` | TField |  |  |
| 34 | `CAMB.EFT.DETS.RESERVED.6` | `CambEftClrFtDets_Reserved6` | TField |  |  |
| 35 | `CAMB.EFT.DETS.RET.CURRENCY` | `CambEftClrFtDets_RetCurrency` | TField |  | field stores the Return Currency Used for posting the transaction.Mapped from the incoming file. |
| 36 | `CAMB.EFT.DETS.RET.VALUE.DATE` | `CambEftClrFtDets_RetValueDate` | TField |  | Field which stores the return Value Date used for processing the transaction.Mapped from the incoming file. |
| 37 | `CAMB.EFT.DETS.RET.PROCESS.DATE` | `CambEftClrFtDets_RetProcessDate` | TField |  | Return Processing date used for Posting the Transaction.T24 date on which the return file is processed. |
| 38 | `CAMB.EFT.DETS.RET.REASON.CODE` | `CambEftClrFtDets_RetReasonCode` | TField |  | Return reason code to be used for posting a return Item. |
| 39 | `CAMB.EFT.DETS.FT.COMM.TYPE` | `CambEftClrFtDets_FtCommType` | TField |  | FT.COMMISSION.TYPE to be used for posting the Charges. This field gets defaulted based on the ret reason code selected using the above field (CAPL.RI.REJ.REASON&gt;FT.COMM.TYPE). |
| 40 | `CAMB.EFT.DETS.RET.STATUS` | `CambEftClrFtDets_RetStatus` | TField |  | Return status. (AUTH, UNAUTH, RETURNED). When system process the incoming clearing file this field will be blank.Once the process is completed, this field holds the status of the reversed funds transfer. |
| 41 | `CAMB.EFT.DETS.TXN.CODE` | `CambEftClrFtDets_TxnCode` | TField |  | Field is used to store the valid transaction code for the underling transaction. |
| 42 | `CAMB.EFT.DETS.FT.VERSION` | `CambEftClrFtDets_FtVersion` | TField |  |  |
| 43 | `CAMB.EFT.DETS.FT.SETTLEMENT` | `CambEftClrFtDets_FtSettlement` | TField |  |  |
| 44 | `CAMB.EFT.DETS.RESERVED.5` | `CambEftClrFtDets_Reserved5` |  |  |  |
| 45 | `CAMB.EFT.DETS.RESERVED.4` | `CambEftClrFtDets_Reserved4` | TField |  |  |
| 46 | `CAMB.EFT.DETS.RESERVED.3` | `CambEftClrFtDets_Reserved3` | TField |  |  |
| 47 | `CAMB.EFT.DETS.RESERVED.2` | `CambEftClrFtDets_Reserved2` | TField |  |  |
| 48 | `CAMB.EFT.DETS.RESERVED.1` | `CambEftClrFtDets_Reserved1` | TField |  |  |
| 49 | `CAMB.EFT.DETS.LOCAL.REF` | `CambEftClrFtDets_LocalRef` |  |  |  |
| 50 | `CAMB.EFT.DETS.OVERRIDE` | `CambEftClrFtDets_Override` |  |  |  |
