# DD.CREDITOR.REGISTRY — Table Schema

> Source: `INSERTS/I_F.DD.CREDITOR.REGISTRY` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.CR.CREDITOR.ID` | `DdCreditorRegistry_CreditorId` | TField |  | Creditor Id Validation Rules&#58; Alphanumeric field. A maximum of 35 characters can be entered. |
| 2 | `DD.CR.CREDITOR.NAME` | `DdCreditorRegistry_CreditorName` | TField |  | Creditor Name Validation Rules&#58; Alphanumeric field. A maximum of 140 characters can be entered. |
| 3 | `DD.CR.CREDITOR.ADDRESS` | `DdCreditorRegistry_CreditorAddress` | TField |  | Creditor Address Validation Rules&#58; Alphanumeric field. A maximum of 70 characters can be entered. |
| 4 | `DD.CR.CRED.CITY.POST.CODE` | `DdCreditorRegistry_CredCityPostCode` | TField |  | Creditor City Post Code Validation Rules&#58; Alphanumeric field. A maximum of 35 characters can be entered. |
| 5 | `DD.CR.CREDITOR.COUNTRY` | `DdCreditorRegistry_CreditorCountry` | TField |  | Creditor Nationality Validation Rules&#58; Valid country record ID. |
| 6 | `DD.CR.PAYMENT.SERVICE` | `DdCreditorRegistry_PaymentService` | TField |  | Payment Service Validation Rules&#58; Alphanumeric field. A maximum of 35 characters can be entered. |
| 7 | `DD.CR.MANDATE.SERVICE` | `DdCreditorRegistry_MandateService` | TField |  | Mandate Service Validation Rules&#58; Alphanumeric field. A maximum of 4 characters can be entered. |
| 8 | `DD.CR.E.MANDATE.SVC.OPTION` | `DdCreditorRegistry_EMandateSvcOption` | TField |  | Indicates the type of the e-mandates service to which the Creditor has subscribed. Validation Rules&#58; Options field. Valid inputs are Debtor, Creditor, Both or None. |
| 9 | `DD.CR.FEES.SUPPORT` | `DdCreditorRegistry_FeesSupport` | TField |  | Indicates if the type of the Service the Creditor adhered supports fees. For future use Validation Rules&#58; Options field. Valid inputs are Yes or No. |
| 10 | `DD.CR.MAND.SVC.START.DATE` | `DdCreditorRegistry_MandSvcStartDate` | TField |  | The Start Date for the support of the DD Mandate service. Validation Rules&#58; Input must be a valid date. |
| 11 | `DD.CR.MAND.SVC.END.DATE` | `DdCreditorRegistry_MandSvcEndDate` | TField |  | The End Date for the support of the DD Mandate service. Validation Rules&#58; Input must be a valid date. |
| 12 | `DD.CR.CREDITOR.BANK.BIC` | `DdCreditorRegistry_CreditorBankBic` | TField |  | The BIC of the Creditor Bank. Validation Rules&#58; Alphanumeric field. A maximum of 11 characters can be entered. |
| 13 | `DD.CR.CRED.BANK.CLR.CODE` | `DdCreditorRegistry_CredBankClrCode` | TField |  | The Clearing Code of the Creditor Bank. Validation Rules&#58; Alphanumeric field. A maximum of 35 characters can be entered. |
| 14 | `DD.CR.CREDITOR.IBAN` | `DdCreditorRegistry_CreditorIban` | TField |  | The IBAN of the account the Creditor maintains with the bank, which could be used for fee collection. For future use Validation Rules&#58; Alphanumeric field. A maximum of 35 characters can be entered. |
| 15 | `DD.CR.CRED.ACCT.NUMBER` | `DdCreditorRegistry_CredAcctNumber` | TField |  | The account the Creditor maintains with the bank, which could be used for fee collection. For future use. Validation Rules&#58; Alphanumeric field. A maximum of 35 characters can be entered. |
| 16 | `DD.CR.CRED.BANK.START.DATE` | `DdCreditorRegistry_CredBankStartDate` | TField |  | The date when the Creditor starts using this Creditor (Alignment) Bank. Validation Rules&#58; Input must be a valid date. |
| 17 | `DD.CR.CRED.BANK.END.DATE` | `DdCreditorRegistry_CredBankEndDate` | TField |  | The date when the Creditor stops using this Creditor (Alignment) Bank. Validation Rules&#58; Input must be a valid date. |
| 18 | `DD.CR.UPLOAD.DATE` | `DdCreditorRegistry_UploadDate` | TField |  | Upload date. Validation Rules&#58; Input must be a valid date. |
| 19 | `DD.CR.SOURCE.FILE.NAME` | `DdCreditorRegistry_SourceFileName` | TField |  | The name of the file through which the record has been created. Validation Rules&#58; Alphanumeric field. A maximum of 50 characters can be entered. |
| 20 | `DD.CR.STATUS` | `DdCreditorRegistry_Status` | TField |  | Indicates if a record can be used or not. Validation Rules&#58; Options field. Blank&#58; Record can be used. Deleted&#58; Record is deleted and is immediately moved to history |
| 21 | `DD.CR.RESERVED.15` | `DdCreditorRegistry_Reserved15` | TField |  |  |
| 22 | `DD.CR.RESERVED.14` | `DdCreditorRegistry_Reserved14` | TField |  |  |
| 23 | `DD.CR.RESERVED.13` | `DdCreditorRegistry_Reserved13` | TField |  |  |
| 24 | `DD.CR.RESERVED.12` | `DdCreditorRegistry_Reserved12` | TField |  |  |
| 25 | `DD.CR.RESERVED.11` | `DdCreditorRegistry_Reserved11` | TField |  |  |
| 26 | `DD.CR.RESERVED.10` | `DdCreditorRegistry_Reserved10` | TField |  |  |
| 27 | `DD.CR.RESERVED.9` | `DdCreditorRegistry_Reserved9` | TField |  |  |
| 28 | `DD.CR.RESERVED.8` | `DdCreditorRegistry_Reserved8` | TField |  |  |
| 29 | `DD.CR.RESERVED.7` | `DdCreditorRegistry_Reserved7` | TField |  |  |
| 30 | `DD.CR.RESERVED.6` | `DdCreditorRegistry_Reserved6` | TField |  |  |
| 31 | `DD.CR.RESERVED.5` | `DdCreditorRegistry_Reserved5` | TField |  |  |
| 32 | `DD.CR.RESERVED.4` | `DdCreditorRegistry_Reserved4` | TField |  |  |
| 33 | `DD.CR.RESERVED.3` | `DdCreditorRegistry_Reserved3` | TField |  |  |
| 34 | `DD.CR.RESERVED.2` | `DdCreditorRegistry_Reserved2` | TField |  |  |
| 35 | `DD.CR.RESERVED.1` | `DdCreditorRegistry_Reserved1` | TField |  |  |
| 36 | `DD.CR.LOCAL.REF` | `DdCreditorRegistry_LocalRef` |  |  |  |
| 37 | `DD.CR.OVERRIDE` | `DdCreditorRegistry_Override` |  |  |  |
| 38 | `DD.CR.RECORD.STATUS` | `DdCreditorRegistry_RecordStatus` | String |  |  |
| 39 | `DD.CR.CURR.NO` | `DdCreditorRegistry_CurrNo` | String |  |  |
| 40 | `DD.CR.INPUTTER` | `DdCreditorRegistry_Inputter` |  |  |  |
| 41 | `DD.CR.DATE.TIME` | `DdCreditorRegistry_DateTime` |  |  |  |
| 42 | `DD.CR.AUTHORISER` | `DdCreditorRegistry_Authoriser` | String |  |  |
| 43 | `DD.CR.CO.CODE` | `DdCreditorRegistry_CoCode` | String |  |  |
| 44 | `DD.CR.DEPT.CODE` | `DdCreditorRegistry_DeptCode` | String |  |  |
| 45 | `DD.CR.AUDITOR.CODE` | `DdCreditorRegistry_AuditorCode` | String |  |  |
| 46 | `DD.CR.AUDIT.DATE.TIME` | `DdCreditorRegistry_AuditDateTime` | String |  |  |
