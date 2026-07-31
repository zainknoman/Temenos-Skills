# NLIDIN.IDIN.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.NLIDIN.IDIN.TRANSACTION` in `NLIDIN_CustomerAuthentication.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDIN.STATUS` | `NlidinIdinTransaction_Status` | TField |  | Specifies the status of the iDIN transaction. Allowed Values: OPEN,SUCCESS,EXPIRED,FAILURE,CANCELLED Validation Rules: This is a no input field. |
| 2 | `IDIN.CREATE.DATETIMESTAMP` | `NlidinIdinTransaction_CreateDatetimestamp` | TField |  | Contains DateTime at which this Transaction Request message was created. |
| 3 | `IDIN.ACQUIRER.ID` | `NlidinIdinTransaction_AcquirerId` | TField |  | Unique four-digit identifier of the Acquirer within an iDx based product, assigned by the product owner when registering the Acquirer. |
| 4 | `IDIN.ISSUER.ID` | `NlidinIdinTransaction_IssuerId` | TField |  | Unique identifier of the Issuer that consists of the international Bank Identifier Code (BIC). |
| 5 | `IDIN.MERCHANT.ID` | `NlidinIdinTransaction_MerchantId` | TField |  | This is the contract number and merchant obtains this ID after registration for iDIN from the Acquirer. |
| 6 | `IDIN.LEGAL.ID` | `NlidinIdinTransaction_LegalId` | TField |  | This is the registered legal id of the merchant. |
| 7 | `IDIN.DEPRECATED.LEGAL.ID` | `NlidinIdinTransaction_DeprecatedLegalId` | TField |  | This is the deprecated legal id of the merchant. |
| 8 | `IDIN.SUB.ID` | `NlidinIdinTransaction_SubId` | TField |  | Unique identifier which defines the name and address of the Merchant to be used for the iDIN. A Merchant can request permission from the Acquirer to use one or more subIDs. Unless agreed otherwise with the Acquirer, the Merchant has to use 0 (zero) as subID by default (if no subIDs are used). |
| 9 | `IDIN.MERCHANT.RETURN.URL` | `NlidinIdinTransaction_MerchantReturnUrl` | TField |  | URL to which the Consumer must be redirected after authentication and/or authorization of the transaction at the Issuer. The resource indicated by the URL must be the website or mobile app of the Merchant or a part thereof. |
| 10 | `IDIN.TRANSACTION.ID` | `NlidinIdinTransaction_TransactionId` | TField |  | Unique 16-digit number within an iDx based product, assigned by an Acquirer. Validation Rules: The first four digits of the TransactionID are made up of the AcquirerID |
| 11 | `IDIN.CUSTOMER.ID` | `NlidinIdinTransaction_CustomerId` | TField |  | Identifies the Customer to whom iDIN transaction is initiated. This field is linked with the CUSTOMER table. |
| 12 | `IDIN.TXN.CREATE.DATETIMESTAMP` | `NlidinIdinTransaction_TxnCreateDatetimestamp` | TField |  | Contains DateTime at which this Transaction was initiated. |
| 13 | `IDIN.EXPIRATION.PERIOD` | `NlidinIdinTransaction_ExpirationPeriod` | TField |  | The time in which the consumer has to approve the transaction. Otherwise the status will be set to �Expired�. |
| 14 | `IDIN.LANGUAGE` | `NlidinIdinTransaction_Language` | TField |  | This field specifies the customer preferred language. |
| 15 | `IDIN.ENTRANCE.CODE` | `NlidinIdinTransaction_EntranceCode` | TField |  | An aunthentication identifier created by merchant to faciliate the session continuation between Merchant and Customer. |
| 16 | `IDIN.SERVICE.CODE` | `NlidinIdinTransaction_ServiceCode` | TField |  | Merchant requested service code based on which customer details are displayed in the enquiry. |
| 17 | `IDIN.USER.ACTION` | `NlidinIdinTransaction_UserAction` | TField |  | Specifies the Customer action taken as part of the iDIN transaction authentication. Allowed Values: SUCCESS,FAILURE,CANCELLED |
| 18 | `IDIN.INPUT.CHANNEL` | `NlidinIdinTransaction_InputChannel` | TField |  | Specifies the channel of iDIN transaction initiation based on which reporting is done Allowed Values: INTERNET,MOBILE |
| 19 | `IDIN.LOCAL.REF` | `NlidinIdinTransaction_LocalRef` |  |  |  |
| 20 | `IDIN.RESERVED.5` | `NlidinIdinTransaction_Reserved5` | TField |  | Reserved field for future use. |
| 21 | `IDIN.RESERVED.4` | `NlidinIdinTransaction_Reserved4` | TField |  | Reserved field for future use. |
| 22 | `IDIN.RESERVED.3` | `NlidinIdinTransaction_Reserved3` | TField |  | Reserved field for future use. |
| 23 | `IDIN.RESERVED.2` | `NlidinIdinTransaction_Reserved2` | TField |  | Reserved field for future use. |
| 24 | `IDIN.RESERVED.1` | `NlidinIdinTransaction_Reserved1` | TField |  | Reserved field for future use. |
| 25 | `IDIN.OVERRIDE` | `NlidinIdinTransaction_Override` |  |  |  |
| 26 | `IDIN.RECORD.STATUS` | `NlidinIdinTransaction_RecordStatus` | String |  |  |
| 27 | `IDIN.CURR.NO` | `NlidinIdinTransaction_CurrNo` | String |  |  |
| 28 | `IDIN.INPUTTER` | `NlidinIdinTransaction_Inputter` |  |  |  |
| 29 | `IDIN.DATE.TIME` | `NlidinIdinTransaction_DateTime` |  |  |  |
| 30 | `IDIN.AUTHORISER` | `NlidinIdinTransaction_Authoriser` | String |  |  |
| 31 | `IDIN.CO.CODE` | `NlidinIdinTransaction_CoCode` | String |  |  |
| 32 | `IDIN.DEPT.CODE` | `NlidinIdinTransaction_DeptCode` | String |  |  |
| 33 | `IDIN.AUDITOR.CODE` | `NlidinIdinTransaction_AuditorCode` | String |  |  |
| 34 | `IDIN.AUDIT.DATE.TIME` | `NlidinIdinTransaction_AuditDateTime` | String |  |  |
