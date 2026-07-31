# FT.BULK.ITEM — Table Schema

> Source: `INSERTS/I_F.FT.BULK.ITEM` in `FT_Clearing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FT.BLK.IT.SORT.CODE` | `FtBulkItem_SortCode` | TField |  | This field indicates the bank sort code. If SORT.CODE entered then account number is treated as other bank account. Validation Rules: Valid sort code in BC.SORT.CODE. SORT.CODE when inputted should not be the Bank�s own SORT.CODE. |
| 2 | `FT.BLK.IT.ACCOUNT.NO` | `FtBulkItem_AccountNo` | TField | Yes | Hold the Account details that is going to send / release payments. Should be in the Currency of the Bulk. Validation Rules: Valid T24 account or if other bank account then SORT.CODE field is mandatory. Mandatory Input |
| 3 | `FT.BLK.IT.CUSTOMER` | `FtBulkItem_Customer` | TField | Yes | This field indicates the customer of the account to whom the fund is going to be Credit/Debit. Validation Rules: Value for this field is defaulted for T24 accounts. For other bank account�s, input is mandatory. |
| 4 | `FT.BLK.IT.CURRENCY` | `FtBulkItem_Currency` | TField | Yes | This field indicates the currency in which the fund is going to be Debit/Credit. Currency should be same as currency given in Bulk Master Validation Rules: Valid Currency in Currency table. Mandatory Input |
| 5 | `FT.BLK.IT.AMOUNT` | `FtBulkItem_Amount` | TField | Yes | This filed hold the payment amount, the amount going to be Credit/Debit. Validation Rules: Mandatory Input |
| 6 | `FT.BLK.IT.VALUE.DATE` | `FtBulkItem_ValueDate` | TField |  | This field indicates the value date that is going to be used in the entry raised for Credit/Debit. Defaulted from Bulk Master Payment Value Date field. Validation Rules: SINGLE type Bulk it should be same as PAYMENT.VALUE.DATE in BULK.MASTER. MULTI type bulk it can be greater than or equal to the PAYMENT.VALUE.DATE in the BULK.MASTER |
| 7 | `FT.BLK.IT.UPLOAD.MANUAL` | `FtBulkItem_UploadManual` | TField |  | This field indicates whether the Bulk item record is inputted manually by the user or uploaded from a file. Validation Rules: System Updated field. Default is NULL and will be updated as Manual if manually inputted. |
| 8 | `FT.BLK.IT.REFERENCE` | `FtBulkItem_Reference` | TField | No | This field indicates the reference of payment. This will override any reference from Bulk Update Type file. Validation Rule Upto 35 characters Optional Input |
| 9 | `FT.BLK.IT.TRANSACTION.TYPE` | `FtBulkItem_TransactionType` | TField | No | This field indicates the transaction type applicable to the transaction being processed. This will override the transaction type from Bulk Update Type file. Validation Rules: Valid record in TXN.TYPE.CONDITION Optional Input |
| 10 | `FT.BLK.IT.STATUS` | `FtBulkItem_Status` | TField |  | This field indicates the status of an item. Following are the values updated in this field, Values allowed for user input, CREATED � When an item is first inputted REJECTED � To reject a payment System updated status, ERROR � If there is any error during validation or during FT/DD item creation READY � If there is no error during validation service and ready for payment PROCESSED � If FT or DD item is created for this Bulk Item, then gets updated with this status |
| 11 | `FT.BLK.IT.BENEFICIARY.ID` | `FtBulkItem_BeneficiaryID` |  |  |  |
| 12 | `FT.BLK.IT.REQUEST.TYPE` | `FtBulkItem_RequestType` | TField |  | This field indicates whether the account specified is a T24 account or other Bank account. If T24 account it will be updated as INTERNAL else it will be NULL. Validation Rules: No Input Field Updated by System. |
| 13 | `FT.BLK.IT.PAYMENT.ID` | `FtBulkItem_PaymentId` | TField |  | This field is used to specify the payment Id. Reference for send / release of payment. NoInput Field Updated by System. |
| 14 | `FT.BLK.IT.LOCAL.REF` | `FtBulkItem_LocalRef` |  |  |  |
| 15 | `FT.BLK.IT.ERROR.DETAILS` | `FtBulkItem_ErrorDetails` |  |  |  |
| 16 | `FT.BLK.IT.RESERVED.10` | `FtBulkItem_Reserved10` | TField |  |  |
| 17 | `FT.BLK.IT.RESERVED.9` | `FtBulkItem_Reserved9` | TField |  |  |
| 18 | `FT.BLK.IT.RESERVED.8` | `FtBulkItem_Reserved8` | TField |  |  |
| 19 | `FT.BLK.IT.RESERVED.7` | `FtBulkItem_Reserved7` | TField |  |  |
| 20 | `FT.BLK.IT.RESERVED.6` | `FtBulkItem_Reserved6` | TField |  |  |
| 21 | `FT.BLK.IT.RESERVED.5` | `FtBulkItem_Reserved5` | TField |  |  |
| 22 | `FT.BLK.IT.RESERVED.4` | `FtBulkItem_Reserved4` | TField |  |  |
| 23 | `FT.BLK.IT.RESERVED.3` | `FtBulkItem_Reserved3` | TField |  |  |
| 24 | `FT.BLK.IT.RESERVED.2` | `FtBulkItem_Reserved2` | TField |  |  |
| 25 | `FT.BLK.IT.RESERVED.1` | `FtBulkItem_Reserved1` | TField |  |  |
| 26 | `FT.BLK.IT.OVERRIDE` | `FtBulkItem_Override` |  |  |  |
| 27 | `FT.BLK.IT.RECORD.STATUS` | `FtBulkItem_RecordStatus` | String |  |  |
| 28 | `FT.BLK.IT.CURR.NO` | `FtBulkItem_CurrNo` | String |  |  |
| 29 | `FT.BLK.IT.INPUTTER` | `FtBulkItem_Inputter` |  |  |  |
| 30 | `FT.BLK.IT.DATE.TIME` | `FtBulkItem_DateTime` |  |  |  |
| 31 | `FT.BLK.IT.AUTHORISER` | `FtBulkItem_Authoriser` | String |  |  |
| 32 | `FT.BLK.IT.CO.CODE` | `FtBulkItem_CoCode` | String |  |  |
| 33 | `FT.BLK.IT.DEPT.CODE` | `FtBulkItem_DeptCode` | String |  |  |
| 34 | `FT.BLK.IT.AUDITOR.CODE` | `FtBulkItem_AuditorCode` | String |  |  |
| 35 | `FT.BLK.IT.AUDIT.DATE.TIME` | `FtBulkItem_AuditDateTime` | String |  |  |
