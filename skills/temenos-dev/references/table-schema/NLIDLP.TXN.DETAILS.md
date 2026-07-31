# NLIDLP.TXN.DETAILS — Table Schema

> Source: `INSERTS/I_F.NLIDLP.TXN.DETAILS` in `NLIDLP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDEAL.TXN.CREATE.DATETIME.STAMP` | `NlidlpTxnDetails_CreateDatetimeStamp` | TField |  | Contains DateTime at which this Transaction Request message was created. |
| 2 | `IDEAL.TXN.ACQUIRER.ID` | `NlidlpTxnDetails_AcquirerId` | TField |  | Unique four-digit identifier of the Acquirer within an iDx based product, assigned by the product owner when registering the Acquirer. |
| 3 | `IDEAL.TXN.ISSUER.ID` | `NlidlpTxnDetails_IssuerId` | TField |  | Unique identifier of the Issuer that consists of the international Bank Identifier Code (BIC). |
| 4 | `IDEAL.TXN.MERCHANT.ID` | `NlidlpTxnDetails_MerchantId` | TField |  | This is the contract number and merchant obtains this ID after registration for iDIN from the Acquirer. |
| 5 | `IDEAL.TXN.SUB.ID` | `NlidlpTxnDetails_SubId` | TField |  | Unique identifier which defines the name and address of the Merchant to be used for the iDIN. A Merchant can request permission from the Acquirer to use one or more subIDs. Unless agreed otherwise with the Acquirer, the Merchant has to use 0 (zero) as subID by default (if no subIDs are used). |
| 6 | `IDEAL.TXN.LEGAL.NAME` | `NlidlpTxnDetails_LegalName` | TField |  | The legal name of the Merchant as registered with the Acquirer. Used together with Merchant.tradeName to represent the Merchant (e.g. 'Merchant.legalName collecting for Merchant.tradeName'). Also used as a name for the Merchant.merchantIBAN for the transfer by the Issuer. It should be the same as the name of the bank account of the Merchant, as registered with the Acquirer. |
| 7 | `IDEAL.TXN.TRADE.NAME` | `NlidlpTxnDetails_TradeName` | TField |  | The trade name of the Merchant, as registered with the Acquirer in case it differs from the legalName. |
| 8 | `IDEAL.TXN.MERCHANT.IBAN` | `NlidlpTxnDetails_MerchantIban` | TField |  | The IBAN of the Merchant, as registered with the Acquirer. (This is linked to Merchant.merchantID.) |
| 9 | `IDEAL.TXN.MERCHANT.BIC` | `NlidlpTxnDetails_MerchantBic` | TField |  | The BIC of the bank where the Merchant's account is held |
| 10 | `IDEAL.TXN.MERCHANT.RETURN.URL` | `NlidlpTxnDetails_MerchantReturnUrl` | TField |  | URL to which the Consumer must be redirected after authentication and/or authorization of the transaction at the Issuer. The resource indicated by the URL must be the website or mobile app of the Merchant or a part thereof. |
| 11 | `IDEAL.TXN.TRANSACTION.ID` | `NlidlpTxnDetails_TransactionId` | TField |  | Unique 16-digit number within an iDx based product, assigned by an Acquirer. Validation Rules: The first four digits of the TransactionID are made up of the AcquirerID |
| 12 | `IDEAL.TXN.TXN.CREATE.DATETIME.STAMP` | `NlidlpTxnDetails_TxnCreateDatetimeStamp` | TField |  | Contains DateTime at which this Transaction was initiated. |
| 13 | `IDEAL.TXN.PURCHASE.ID` | `NlidlpTxnDetails_PurchaseId` | TField |  | Unique identification of the order within the Merchant's system. This ID ultimately appears on the payment confirmation (Bank statement / account overview of the Consumer and Merchant). |
| 14 | `IDEAL.TXN.AMOUNT` | `NlidlpTxnDetails_Amount` | TField |  | The amount payable in euro (with a period (.) used as decimal separator). |
| 15 | `IDEAL.TXN.CURRENCY` | `NlidlpTxnDetails_Currency` | TField |  | Currency in which payment should be effected, expressed using the three-letter international currency code as per ISO 4217 Since iDEAL currently only supports Euro payments, value should always be 'EUR'. |
| 16 | `IDEAL.TXN.EXPIRATION.PERIOD` | `NlidlpTxnDetails_ExpirationPeriod` | TField |  | The time in which the consumer has to approve the transaction. Otherwise the status will be set to �Expired�. |
| 17 | `IDEAL.TXN.LANGUAGE` | `NlidlpTxnDetails_Language` | TField |  | This field enables the Issuer's site to select the Consumer's preferred language (e.g. the language selected on the Merchant's site) |
| 18 | `IDEAL.TXN.DESCRIPTION` | `NlidlpTxnDetails_Description` | TField |  | Description of the product(s) or services being paid for. This field must not contain characters that can lead to problems To prevent any possible errors most iDEAL systems will reject any description that contains HTML-tags and such other code. |
| 19 | `IDEAL.TXN.ENTRANCE.CODE` | `NlidlpTxnDetails_EntranceCode` | TField |  | An aunthentication identifier created by merchant to faciliate the session continuation between Merchant and Customer. |
| 20 | `IDEAL.TXN.STATUS` | `NlidlpTxnDetails_Status` | TField |  | Specifies the status of the iDIN transaction. Allowed Values: OPEN,SUCCESS,EXPIRED,FAILURE,CANCELLED Validation Rules: This is a no input field. |
| 21 | `IDEAL.TXN.CUSTOMER.ACTION` | `NlidlpTxnDetails_CustomerAction` | TField |  | Specifies the Customer action taken as part of the iDIN transaction authentication. Allowed Values: SUCCESS,FAILURE,CANCELLED |
| 22 | `IDEAL.TXN.DEBIT.ACCOUNT.NUMBER` | `NlidlpTxnDetails_DebitAccountNumber` | TField |  | Specified the account number for Debit |
| 23 | `IDEAL.TXN.CUSTOMER.ID` | `NlidlpTxnDetails_CustomerId` | TField |  | Identifies the Customer to whom IDEAL transaction is initiated. This field is linked with the CUSTOMER table. |
| 24 | `IDEAL.TXN.REMITTANCE.INFO` | `NlidlpTxnDetails_RemittanceInfo` | TField |  | Holds the IDEAL related remittance information |
| 25 | `IDEAL.TXN.PAYMENT.ORDER.ID` | `NlidlpTxnDetails_PaymentOrderId` | TField |  | Holds the ID of Payment order. |
| 26 | `IDEAL.TXN.INPUT.LEVEL` | `NlidlpTxnDetails_InputLevel` | TField |  | Specifies the channel of iDIN transaction initiation based on which reporting is done Allowed Values: INTERNET,MOBILE |
| 27 | `IDEAL.TXN.EXPIRATION.DATETIME` | `NlidlpTxnDetails_ExpirationDatetime` | TField |  | To hold the expiration date and time by which transaction will get expired |
| 28 | `IDEAL.TXN.RESERVED.4` | `NlidlpTxnDetails_Reserved4` | TField |  | Reserved field for future use. |
| 29 | `IDEAL.TXN.RESERVED.3` | `NlidlpTxnDetails_Reserved3` | TField |  | Reserved field for future use. |
| 30 | `IDEAL.TXN.RESERVED.2` | `NlidlpTxnDetails_Reserved2` | TField |  | Reserved field for future use. |
| 31 | `IDEAL.TXN.RESERVED.1` | `NlidlpTxnDetails_Reserved1` | TField |  | Reserved field for future use. |
| 32 | `IDEAL.TXN.OVERRIDE` | `NlidlpTxnDetails_Override` |  |  |  |
| 33 | `IDEAL.TXN.LOCAL.REF` | `NlidlpTxnDetails_LocalRef` |  |  |  |
| 34 | `IDEAL.TXN.RECORD.STATUS` | `NlidlpTxnDetails_RecordStatus` | String |  |  |
| 35 | `IDEAL.TXN.CURR.NO` | `NlidlpTxnDetails_CurrNo` | String |  |  |
| 36 | `IDEAL.TXN.INPUTTER` | `NlidlpTxnDetails_Inputter` |  |  |  |
| 37 | `IDEAL.TXN.DATE.TIME` | `NlidlpTxnDetails_DateTime` |  |  |  |
| 38 | `IDEAL.TXN.AUTHORISER` | `NlidlpTxnDetails_Authoriser` | String |  |  |
| 39 | `IDEAL.TXN.CO.CODE` | `NlidlpTxnDetails_CoCode` | String |  |  |
| 40 | `IDEAL.TXN.DEPT.CODE` | `NlidlpTxnDetails_DeptCode` | String |  |  |
| 41 | `IDEAL.TXN.AUDITOR.CODE` | `NlidlpTxnDetails_AuditorCode` | String |  |  |
| 42 | `IDEAL.TXN.AUDIT.DATE.TIME` | `NlidlpTxnDetails_AuditDateTime` | String |  |  |
