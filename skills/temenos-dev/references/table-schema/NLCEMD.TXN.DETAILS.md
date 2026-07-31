# NLCEMD.TXN.DETAILS — Table Schema

> Source: `INSERTS/I_F.NLCEMD.TXN.DETAILS` in `NLCEMD_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EMD.TXN.CREATE.DATETIME.STAMP` | `NlcemdTxnDetails_CreateDatetimeStamp` | TField |  | Contains DateTime at which this Transaction Request message was created. |
| 2 | `EMD.TXN.ACQUIRER.ID` | `NlcemdTxnDetails_AcquirerId` | TField |  | Unique four-digit identifier of the Acquirer within an iDx based product, assigned by the product owner when registering the Acquirer. |
| 3 | `EMD.TXN.ISSUER.ID` | `NlcemdTxnDetails_IssuerId` | TField |  | Unique identifier of the Issuer that consists of the international Bank Identifier Code (BIC). |
| 4 | `EMD.TXN.MERCHANT.ID` | `NlcemdTxnDetails_MerchantId` | TField |  | This is the contract number and merchant obtains this ID after registration for eMandate from the Acquirer. |
| 5 | `EMD.TXN.SUB.ID` | `NlcemdTxnDetails_SubId` | TField |  | Unique identifier which defines the name and address of the Merchant to be used for the eMandate. A Merchant can request permission from the Acquirer to use one or more subIDs. Unless agreed otherwise with the Acquirer, the Merchant has to use 0 (zero) as subID by default (if no subIDs are used). |
| 6 | `EMD.TXN.MERCHANT.RETURN.URL` | `NlcemdTxnDetails_MerchantReturnUrl` | TField |  | URL to which the Consumer must be redirected after authentication and/or authorization of the transaction at the Issuer. The resource indicated by the URL must be the website or mobile app of the Merchant or a part thereof. |
| 7 | `EMD.TXN.TRANSACTION.ID` | `NlcemdTxnDetails_TransactionId` | TField |  | Unique 16-digit number within an iDx based product, assigned by an Acquirer. Validation Rules: The first four digits of the TransactionID are made up of the AcquirerID |
| 8 | `EMD.TXN.TXN.CREATE.DATETIME.STAMP` | `NlcemdTxnDetails_TxnCreateDatetimeStamp` | TField |  | Contains DateTime at which this Transaction was initiated. |
| 9 | `EMD.TXN.EXPIRATION.PERIOD` | `NlcemdTxnDetails_ExpirationPeriod` | TField |  | The time in which the consumer has to approve the transaction. Otherwise the status will be set to �Expired�. |
| 10 | `EMD.TXN.LANGUAGE` | `NlcemdTxnDetails_Language` | TField |  | This field enables the Issuer's site to select the Consumer's preferred language (e.g. the language selected on the Merchant's site) |
| 11 | `EMD.TXN.ENTRANCE.CODE` | `NlcemdTxnDetails_EntranceCode` | TField |  | An aunthentication identifier created by merchant to faciliate the session continuation between Merchant and Customer. |
| 12 | `EMD.TXN.MANDATE.MSG.ID` | `NlcemdTxnDetails_MandateMsgId` | TField |  | Identifies the eMandate message from the Creditor. |
| 13 | `EMD.TXN.MANDATE.CREATION.DATE.TIME` | `NlcemdTxnDetails_MandateCreationDateTime` |  |  |  |
| 14 | `EMD.TXN.MANDATE.ID` | `NlcemdTxnDetails_MandateId` | TField |  | Identifies the eMandate that was created. |
| 15 | `EMD.TXN.MANDATE.REQUEST.ID` | `NlcemdTxnDetails_MandateRequestId` | TField |  | Will be filled by the Routing Service later with NOTPROVIDED. |
| 16 | `EMD.TXN.MANDATE.SERVICE.CODE` | `NlcemdTxnDetails_MandateServiceCode` | TField |  | The identification code of the Scheme. Must be: SEPA. |
| 17 | `EMD.TXN.MANDATE.LOCAL.INSTRUMENT.CODE` | `NlcemdTxnDetails_MandateLocalInstrumentCode` | TField |  | The identification code of the Instrument(Core/B2B). Must be:CORE to indicate a Core direct debit and B2B to indicate a B2B direct debit. The mixing of different Local Instrument values is not allowed in the same message. |
| 18 | `EMD.TXN.MANDATE.SEQUENCE.TYPE` | `NlcemdTxnDetails_MandateSequenceType` | TField |  | Indicates type of eMandate: one-off Direct Debit or recurring. Format: 'OOFF' or 'RCUR'. |
| 19 | `EMD.TXN.CREDITOR.REFERENCE` | `NlcemdTxnDetails_CreditorReference` | TField |  | Reference ID that identifies the Debtor to the Creditor. Issued by the Creditor. |
| 20 | `EMD.TXN.CREDITOR.SCHEME.CODE` | `NlcemdTxnDetails_CreditorSchemeCode` | TField |  | The identification code of the Scheme. Must be: SEPA. |
| 21 | `EMD.TXN.CREDITOR.NAME` | `NlcemdTxnDetails_CreditorName` | TField |  | Name of the creditor. Limited to 70 chars in length |
| 22 | `EMD.TXN.CREDITOR.COUNTRY` | `NlcemdTxnDetails_CreditorCountry` | TField |  | Country of the postal address of the Creditor. |
| 23 | `EMD.TXN.CREDITOR.POSTAL.ADRLINE` | `NlcemdTxnDetails_CreditorPostalAdrline` | TField |  | Creditor's P.O. Box or street name + building + add-on (if any). |
| 24 | `EMD.TXN.CREDITOR.POSTAL.ADRLINE1` | `NlcemdTxnDetails_CreditorPostalAdrline1` | TField |  | Creditor's Postcode and City. |
| 25 | `EMD.TXN.DEBTOR.REFERENCE` | `NlcemdTxnDetails_DebtorReference` | TField |  | Reference ID that identifies the Creditor to the Debtor. Issued by the Debtor. |
| 26 | `EMD.TXN.DEBTOR.INSTITUTION.BIC` | `NlcemdTxnDetails_DebtorInstitutionBic` | TField |  | BIC of the Debtor Bank. |
| 27 | `EMD.TXN.MANDATE.AMENDMENT.REASON` | `NlcemdTxnDetails_MandateAmendmentReason` | TField |  | The reason code for amending the eMandate. Must be 'MD16'.Means that amendment was requested by Debtor. |
| 28 | `EMD.TXN.ORIGINAL.MANDATE.ID` | `NlcemdTxnDetails_OriginalMandateId` | TField |  | The emandate ID of the eMandate to be amended. |
| 29 | `EMD.TXN.ORIGINAL.DEBTOR.ACCOUNT.IBAN` | `NlcemdTxnDetails_OriginalDebtorAccountIban` | TField |  | Original debtor account IBAN provided for the eMandate to be amended. |
| 30 | `EMD.TXN.ORIGINAL.DEBTOR.INSTITUTIONBIC` | `NlcemdTxnDetails_OriginalDebtorInstitutionbic` | TField |  | Original debtor institution BIC provided for the eMandate to be amended. |
| 31 | `EMD.TXN.STATUS` | `NlcemdTxnDetails_Status` | TField |  | Status of the eMandate transaction creation. |
| 32 | `EMD.TXN.MANDATE.TYPE` | `NlcemdTxnDetails_MandateType` | TField |  | This identifies the type of the eMandate whether it is issuing or Amendment. |
| 33 | `EMD.TXN.DEBTOR.ACCOUNT.IBAN` | `NlcemdTxnDetails_DebtorAccountIban` | TField |  | IBAN of the Debtor Account. |
| 34 | `EMD.TXN.DEBTOR.NAME` | `NlcemdTxnDetails_DebtorName` | TField |  | Name of the debtor. |
| 35 | `EMD.TXN.CUSTOMER.ACTION` | `NlcemdTxnDetails_CustomerAction` | TField |  | This identifies the customer's acceptance to create the transaction after authentication. |
| 36 | `EMD.TXN.DD.ID` | `NlcemdTxnDetails_DdId` | TField |  | Direct debit reference of the created eMandate transaction. |
| 37 | `EMD.TXN.REJECT.REASON.CODE` | `NlcemdTxnDetails_RejectReasonCode` | TField |  | Identifies the reson for the rejection of the eMandate transaction. |
| 38 | `EMD.TXN.ADDITIONAL.REJECT.REASON.INFO` | `NlcemdTxnDetails_AdditionalRejectReasonInfo` | TField |  | Additional info can be provided for the reason why the request was rejected. Must be present if Reject Reason code is MD02. |
| 39 | `EMD.TXN.MANDATE.MAX.AMOUNT` | `NlcemdTxnDetails_MandateMaxAmount` | TField |  | Contains the maximum amount that can be debited from the account. |
| 40 | `EMD.TXN.MANDATE.REASON` | `NlcemdTxnDetails_MandateReason` | TField |  | Contains the reason for the creation of the Mandate. |
| 41 | `EMD.TXN.ULTIMATE.CREDITOR.NAME` | `NlcemdTxnDetails_UltimateCreditorName` | TField |  | Contains the name of the ultimate creditor. |
| 42 | `EMD.TXN.MANDATE.PURCHASE.ID` | `NlcemdTxnDetails_MandatePurchaseId` | TField |  | Contains the purchase id of the creditor for the mandate. |
| 43 | `EMD.TXN.RESERVED.1` | `NlcemdTxnDetails_Reserved1` | TField |  | Reserved field for future use. |
| 44 | `EMD.TXN.RESERVED.2` | `NlcemdTxnDetails_Reserved2` | TField |  | Reserved field for future use. |
| 45 | `EMD.TXN.RESERVED.3` | `NlcemdTxnDetails_Reserved3` | TField |  | Reserved field for future use. |
| 46 | `EMD.TXN.RESERVED.4` | `NlcemdTxnDetails_Reserved4` | TField |  | Reserved field for future use. |
| 47 | `EMD.TXN.RESERVED.5` | `NlcemdTxnDetails_Reserved5` | TField |  | Reserved field for future use. |
| 48 | `EMD.TXN.OVERRIDE` | `NlcemdTxnDetails_Override` |  |  |  |
| 49 | `EMD.TXN.LOCAL.REF` | `NlcemdTxnDetails_LocalRef` |  |  |  |
| 50 | `EMD.TXN.RECORD.STATUS` | `NlcemdTxnDetails_RecordStatus` | String |  |  |
| 51 | `EMD.TXN.CURR.NO` | `NlcemdTxnDetails_CurrNo` | String |  |  |
| 52 | `EMD.TXN.INPUTTER` | `NlcemdTxnDetails_Inputter` |  |  |  |
| 53 | `EMD.TXN.DATE.TIME` | `NlcemdTxnDetails_DateTime` |  |  |  |
| 54 | `EMD.TXN.AUTHORISER` | `NlcemdTxnDetails_Authoriser` | String |  |  |
| 55 | `EMD.TXN.CO.CODE` | `NlcemdTxnDetails_CoCode` | String |  |  |
| 56 | `EMD.TXN.DEPT.CODE` | `NlcemdTxnDetails_DeptCode` | String |  |  |
| 57 | `EMD.TXN.AUDITOR.CODE` | `NlcemdTxnDetails_AuditorCode` | String |  |  |
| 58 | `EMD.TXN.AUDIT.DATE.TIME` | `NlcemdTxnDetails_AuditDateTime` | String |  |  |
