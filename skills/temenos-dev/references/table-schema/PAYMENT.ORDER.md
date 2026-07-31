# PAYMENT.ORDER — Table Schema

> Source: `INSERTS/I_F.PAYMENT.ORDER` in `PI_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PO.PAYMENT.ORDER.PRODUCT` | `PaymentOrder_PaymentOrderProduct` | TField | Yes | Payment order product Mandatory field.Defaulted in case field left blank and populated from PREF.PYMT.PRODUCT of beneficiary id used in the payment order contract If PREF.PYMT.PRODUCT is blank for beneficiary id defined in the contract then prompted for a valid product from PAYMENT.ORDER.PRODUCT application |
| 2 | `PO.ORDERING.COMPANY` | `PaymentOrder_OrderingCompany` | TField |  | Company from which the transaction is done or debit account's customer's company No Input field |
| 3 | `PO.ORDERING.CUSTOMER` | `PaymentOrder_OrderingCustomer` | TField |  | Debit Account customer |
| 4 | `PO.ORDERING.CUSTOMER.BIC` | `PaymentOrder_OrderingCustomerBic` | TField |  | BIC of the Ordering customer |
| 5 | `PO.ORDERING.CUST.NAME` | `PaymentOrder_OrderingCustName` | TField | Yes | Ordering customer name Validation Rules: 1. Name of Ordering customer 2. Mandatory when the customer is not in T24 and ORDERING.CUSTOMER.BIC is not defined |
| 6 | `PO.ORDERING.POST.ADDRESS.TYPE` | `PaymentOrder_OrderingPostAddressType` | TField |  | Ordering customer's address type Validation Rules: |
| 7 | `PO.ORDERING.POST.SWIFT.ADDR` | `PaymentOrder_OrderingPostSwiftAddr` |  |  |  |
| 8 | `PO.ORDERING.POST.ADDR.LINE` | `PaymentOrder_OrderingPostAddrLine` |  |  |  |
| 9 | `PO.ORDERING.PORTFOLIO` | `PaymentOrder_OrderingPortfolio` | TField |  | Debit portfolio id Validation Rules:1. Inputtable field only if SC is installed 2. If DEBIT.ACCOUNT field has value, then the account will be checked if it is an account in the portfolio else error will be thrown 3. If DEBIT.ACCOUNT field is null, then the account from portfolio will be defaulted based on the setup in ACCOUNT.PARAMETER. |
| 10 | `PO.DEBIT.ACCOUNT` | `PaymentOrder_DebitAccount` | TField | Yes | Debit account id Validation Rules:1. Can be manually input or defaulted from SEC.ACC.MASTER if ORDERING.PORTFOLIO is defined2. Valid T24 account 3. Mandatory whenDEBIT.IBAN and DEBIT.PL are not defined4. If DEBIT.ACCOUNT and DEBIT.IBAN are defined, then check is done to ensure that IBAN is for the debit account else error will be thrown.5. If DEBIT.ACCOUNT is defined and DEBIT.IBAN is not defined, if IN is installed, then DEBIT.IBAN for the account is defaulted |
| 11 | `PO.DEBIT.CCY` | `PaymentOrder_DebitCcy` | TField |  | Currency of the debit account Validation Rules: 1. Can be manually input or it will be defaulted from the debit account in case of T24 accounts 2. For external accounts, Currency should be keyed in by the user 3. If the currency is not allowed currency in the PAYMENT.ORDER.PRODUCT, then error will be thrown4. If the currency is different from PAYMENT.CURRENCY, then the field ALLOW.FX will be checked in PAYMENT.ORDER.PRODUCT. If it not set to YES, then error will be thrown5. If DEBIT.PL is defined, then DEBIT.CCY should be mandatorily input else error will be thrown 6. If it is bulk PO (BULK.PROCESSING.MODE is present) then debit currency has to be same as payment currency if the field ALLOW.MULTI.CURRENCY = No in FT.BULK.UPDATE.TYPE table |
| 12 | `PO.DEBIT.ACCOUNT.IBAN` | `PaymentOrder_DebitAccountIban` | TField |  | IBAN of the debit account Validation Rules:1. Inputtable field only if IN is installed 2. Can be manually input or defaulted3. If manually input, must be a valid IBAN number for the debit account4. IBAN should be a valid T24 IBAN 5. If not manually defined, then will be populated based on the debit account6. If DEBIT.IBAN is defined, but DEBIT.ACCOUNT is not defined, then the debit account number will be defaulted7. If DEBIT.IBAN is not defined, but ORDERING.CUST.BIC is defined, then BIC will be derived from IBAN and populated8. If DEBIT.IBAN and DEBIT.ACCOUNT are not defined, but ORDERING.CUST.BIC is defined, then IBAN will be derived from BIC and populated9. If ORDERING.CUST.BIC and DEBIT.IBAN are defined, then check must be done to ensure that the IBAN is valid for the BIC defined |
| 13 | `PO.DEBIT.PL` | `PaymentOrder_DebitPl` | TField |  | PL category to be debited Validation Rules:1. Can be manually input2. Must be a valid PL category3. If DEBIT.PL is defined, then DEBIT.CCY should be mandatorily input4. Allowed only when DEBIT.ACCOUNT and DEBIT.IBAN are not defined |
| 14 | `PO.DEBIT.VALUE.DATE` | `PaymentOrder_DebitValueDate` | TField | No | Value date for debit Validation Rules:1. Debit Value date passed to Payment system2. Optional field3. Override will be raised if less then TODAY |
| 15 | `PO.ORDERING.REFERENCE` | `PaymentOrder_OrderingReference` | TField | No | Reference related to the ordering details Validation Rules:Free Text of 18 characters. Optional. No validation |
| 16 | `PO.SIGNATORY` | `PaymentOrder_Signatory` |  |  |  |
| 17 | `PO.BENEFICIARY.ID` | `PaymentOrder_BeneficiaryId` | TField | Yes | Valid Beneficiary id Validation Rules:Id of the Beneficiary. Must be a valid record in BENEFICIARY application. Allowed only when Pay Through Beneficiary is set to Yes in PAYMENT.ORDER.PRODUCT. Mandatory if PAY.THROUGH.BENEFICIARY is set to YES and Beneficiary Account number and Beneficiary Account IBAN are not defined. If the beneficairy ID is input and validated, system defaults the related beneficairy details from the BENEFICIARY application into the current PO record. Once system defaults the beneficiary details, all the beneficiary fields in the PO record are disabled for user input If the Beneficairy ID is modified, corresponding details are again defaulted into the PO record. |
| 18 | `PO.CREDIT.ACCOUNT` | `PaymentOrder_CreditAccount` | TField | Yes | Credit Account number. T24 account Validation Rules:Not allowed for External payment. For Internal Payment:1. Can be manually input or defaulted from SEC.ACC.MASTER if CREDIT.PORTFOLIO is defined 2. Valid T24 account 3. Mandatory when CREDIT.IBAN and CREDIT.PL are not defined4. If CREDIT.ACCOUNT and CREDIT.IBAN are defined, then check is done to ensure that IBAN is for the credit account else error will be thrown5. If CREDIT.ACCOUNT is defined and CREDIT.IBAN is not defined, if IN is installed and IBAN is allowed for the product, then CREDIT.IBAN for the account is defaulted |
| 19 | `PO.CREDIT.PORTFOLIO` | `PaymentOrder_CreditPortfolio` | TField |  | Portfolio id to be credit Validation Rules:Not allowed for External Payment. For Internal Payment:1. Inputtable field only if SC is installed 2. Validation will be done as follows: i. Pass the customer id from ORDERING.CUST field and portfolio no. to GET.SETTLEMENT.DEFAULTS routine ii. If no error is returned, the field CREDIT.ACCOUNT will be checked iii. If CREDIT.ACCOUNT field has value, then the account will be checked if it is an account in the portfolio else error will be thrown iv. If CREDIT.ACCOUNT field is null, then the account from portfolio will be defaulted based on the setup in ACCOUNT.PARAMETER. This will also be done in the routine GET.SETTLEMENT.DEFAULTS |
| 20 | `PO.CREDIT.ACCOUNT.IBAN` | `PaymentOrder_CreditAccountIban` | TField |  | IBAN of the credit account Validation Rules:Not allowed for External Payment. For Internal payment:1. Inputtable field only if IN is installed (done in record routine)2. Allowed only if IBAN is allowed for the product3. Can be manually input or defaulted4. If manually input, must be a valid IBAN number for the credit account5. IBAN should be a valid T24 IBAN 6. If not manually defined, then will be populated based on the credit account if IN is installed and IBAN is allowed for the product7. If CREDIT.IBAN is defined, but CREDIT.ACCOUNT is not defined, then the credit account number will be defaulted |
| 21 | `PO.CREDIT.PL` | `PaymentOrder_CreditPl` | TField |  | PL category to be credited Validation Rules:1. Can be manually input2. Must be a valid PL category3. If CREDIT.PL is defined, then PAYMENT.CCY should be mandatorily input |
| 22 | `PO.BENEFICIARY.ACCOUNT.NO` | `PaymentOrder_BeneficiaryAccountNo` | TField |  | Beneficiary Account number Validation Rules:Not allowed for Internal payment. For external payment:1. Defaulted from Beneficiary record-BEN.ACCT.NO field. Cannot be overwritten2. Not allowed if Beneficiary id is defined |
| 23 | `PO.BENEFICIARY.IBAN` | `PaymentOrder_BeneficiaryIban` | TField | Yes | IBAN of the beneficiary account Validation Rules:Not allowed for Internal payment or if Beneficiary id is defined. Defaulted from Beneficiary record-IBAN.BEN field. Should be in Valid IBAN structure. Mandatory/Not allowed based on the PAYMENT.ORDER.COUNTRY.RULES/PAYMENT.ORDER.PRODUCT |
| 24 | `PO.BENEFICIARY.BIC` | `PaymentOrder_BeneficiaryBic` | TField |  | BIC of the beneficiary customer Validation Rules:Not allowed for Internal payment or if Beneficiary id is defined. Defaulted from Beneficiary record-BEN.CUSTOMER field when the value has SW- prefix |
| 25 | `PO.BENEFICIARY.CUSTOMER` | `PaymentOrder_BeneficiaryCustomer` | TField |  | Customer number of the beneficiary Validation Rules:Not allowed for Internal payment or if Beneficiary id is defined. Defaulted from Beneficiary record-BEN.CUSTOMER field it the customer is a T24 customer |
| 26 | `PO.BENEFICIARY.NAME` | `PaymentOrder_BeneficiaryName` | TField |  | Name of the beneficiary, can contain upto 70 chars Validation Rules:Not allowed for Internal payment or if Beneficiary id is defined. It is defaulted with the values in BenNameOne or BenNameTwo is mentioned in the Benficiary Record. If both the names are present, they are concatenated with a space and then defaulted here If Beneficiary doesnot contain the names, but the Customer is a valid T24customer, then the names are obtained from the Customer record and are defaulted in the same manner Defaulted from Beneficiary record-BEN.CUSTOMER field if the value does not have SW- prefix and not a valid T24 customer |
| 27 | `PO.BEN.POST.ADDRESS.TYPE` | `PaymentOrder_BenPostAddressType` | TField |  | Beneficiary customer's address type Validation Rules: |
| 28 | `PO.BEN.POST.SWIFT.ADDR` | `PaymentOrder_BenPostSwiftAddr` |  |  |  |
| 29 | `PO.BEN.POST.ADDR.LINE` | `PaymentOrder_BenPostAddrLine` |  |  |  |
| 30 | `PO.BEN.BANK.CLEARING.CODE` | `PaymentOrder_BenBankClearingCode` | TField |  | Clearing code or sort code of the beneficiary bank Validation Rules:Not allowed for Internal payment or if Beneficiary id is defined. Defaulted from Beneficiary record-BANK.SORT.CODE field |
| 31 | `PO.BENEFICIARY.COUNTRY.CODE` | `PaymentOrder_BeneficiaryCountryCode` | TField |  | Beneficiary country Validation Rules:Not allowed for Internal payment or if beneficiar id is defined. Defaulted from Beneficiary record-BEN.PYMT.COUNTRY. Override raised when the Country code is not ALLOWED.COUNTRY.CODE as per PAYMENT.ORDER.PRODUCT |
| 32 | `PO.BEN.IDENTIFIER` | `PaymentOrder_BenIdentifier` | TField |  | This field will hold the 5 letter ISO identifier Example : GBDSC. When payment is sent to TPH, this will be stored in field CLEARING.SYSTEM.ID.CODE in table POR.SUPPLIMENTARY.INFO. Sytsem uses this code, looks up the table ISO.CLEARING.SYSTEM.ID and fetches the 2 letter SWIFT prefix from field SWIFT.PREFIX. Sytem concatenates '//' followed by the extracted swift prefix followed by the value in BEN.BANK.CLEARING.CODE. This concatenated value is also sent to TPH and stored in field PARTY.ACCOUNT.LINE in POR.SUPPLIMENTARY.INFO (For role BENFCY). Example : If Swift Prefix for GBDSC is SC and BEN.BANK.CLEARING.CODE contains 4352, value formed would be //SC4352 |
| 33 | `PO.BENEFICIARY.DOB` | `PaymentOrder_BeneficiaryDob` | TField |  | Holds the birth date of the beneficiary Validation Rules: If populated then Beneficiary Identifier Type must be set to Private |
| 34 | `PO.BENEFICIARY.BR.PRVNC` | `PaymentOrder_BeneficiaryBrPrvnc` | TField | Yes | Holds the birth province of the beneficiary Validation Rules: If populated then Beneficiary Identifier Type must be set to Private Beneficiary Birth Date is mandatory when this field is captured |
| 35 | `PO.BENEFICIARY.BR.CITY` | `PaymentOrder_BeneficiaryBrCity` | TField | Yes | Holds the birth city of the beneficiary Validation Rules: If populated then Beneficiary Identifier Type must be set to Private Beneficiary Birth Date is mandatory when this field is captured |
| 36 | `PO.BENEFICIARY.BR.COUNTRY` | `PaymentOrder_BeneficiaryBrCountry` | TField | Yes | Holds the birth country of the beneficiary Validation Rules: It must be a valid code on the COUNTRY table It will be used when Beneficiary is a person (private) Beneficiary Birth Date is mandatory when this field is captured |
| 37 | `PO.BENEFICIARY.OT.ID.TYPE` | `PaymentOrder_BeneficiaryOtIdType` | TField | Conditional | Holds other identifications such as could be a Social Security Number, a Tax Identification Number, PassportNumber, a Clearing Id ,etc., of the beneficiary. Validation Rules: Optional Beneficiary Id Type is mandatory when this field is captured If populated then either Beneficiary Scheme Code or Beneficiary Scheme Proprietary must be populated |
| 38 | `PO.ACCT.WITH.BANK.IBAN` | `PaymentOrder_AcctWithBankIban` | TField |  | IBAN of Account with Bank Validation Rules:Not allowed for Internal payment or if Beneficiary id is defined. Defaulted from Beneficiary record-ACCT.WITH.BANK.IBAN field. Should be in Valid IBAN structure |
| 39 | `PO.ACCT.WITH.BANK.BIC` | `PaymentOrder_AcctWithBankBic` | TField | Yes | BIC of Account with Bank Validation Rules:1.Not allowed for Internal payment or if Beneficiary id is defined. Defaulted from Beneficiary record-ACCT.WITH.BANK field when the value has SW- prefix. If ACCT.WITH.BANK is null, then the value is fetched from the field BIC.IBAN.BEN. If Derive BIC functionality is not enabled, it is defaulted from the ISO.CLEARING.SYSTEM.ID record, corresponding to the ACCT.WITH.BANK.IDENTIFIER given 2.Mandatory/Not allowed based on the PAYMENT.ORDER.COUNTRY.RULES/PAYMENT.ORDER.PRODUCT |
| 40 | `PO.ACCT.WITH.BANK.CUSTOMER` | `PaymentOrder_AcctWithBankCustomer` | TField |  | Account with Bank's customer id Validation Rules:Not allowed for Internal payment or if Beneficiary id is defined. Defaulted from Beneficiary record-ACCT.WITH.BANK field if the customer is a T24 customer |
| 41 | `PO.ACCT.WITH.BANK.POST.ADDR.TYPE` | `PaymentOrder_AcctWithBankPostAddrType` | TField |  | Account with bank's address type Validation Rules: |
| 42 | `PO.ACCT.WITH.BANK.SWIFT.ADDR` | `PaymentOrder_AcctWithBankSwiftAddr` |  |  |  |
| 43 | `PO.ACCT.WITH.BANK.POST.ADDR.LN` | `PaymentOrder_AcctWithBankPostAddrLn` |  |  |  |
| 44 | `PO.ACCT.WITH.BANK.CLEARING.CODE` | `PaymentOrder_AcctWithBankClearingCode` | TField | Yes | Clearing code or sort code of the account with bank Validation Rules:Not allowed for Internal payment or if Beneficiary id is defined. Defaulted from Beneficiary record-ACCT.WITH.BANK.BK.SORT.CODE field. Mandatory/Not allowed based on the PAYMENT.ORDER.COUNTRY.RULES/PAYMENT.ORDER.PRODUCT |
| 45 | `PO.ACCT.WITH.BANK.IDENTIFIER` | `PaymentOrder_AcctWithBankIdentifier` | TField |  | This field will hold the 5 letter ISO identifier Example : GBDSC. When payment is sent to TPH, this will be stored in field CLEARING.SYSTEM.ID.CODE in table POR.SUPPLIMENTARY.INFO System uses this code, looks up the table ISO.CLEARING.SYSTEM.ID and fetches the 2 letter SWIFT prefix from field SWIFT.PREFIX. System concatenates '//' followed by the extracted swift prefix followed by the value in ACCT.BANK.CLEARING.CODE. This concatenated value is also sent to TPH and stored in field PARTY.ACCOUNT.LINE in POR.SUPPLIMENTARY.INFO (For role ACWINS). Example : If Swift Prefix for GBDSC is SC and ACCOUNT.WITH.BANK.CLEARING.CODE contains 4352, value formed would be //SC4352 |
| 46 | `PO.ACCT.WITH.BANK.COUNTRY` | `PaymentOrder_AcctWithBankCountry` | TField |  | Country for account with bank Validation Rules:OtherIdentification code for Beneficiary. Valid record from Country application |
| 47 | `PO.ACCT.WITH.BANK.ACC` | `PaymentOrder_AcctWithBankAcc` | TField | No | Optional The Account Number inputted here along with the Account with Bank details as given in ACCT.WITH.BANK will be used in tag 57 of Swift message. |
| 48 | `PO.ACCT.WITH.BANK.RESERVED.3` | `PaymentOrder_AcctWithBankReserved3` | TField |  | Validation Rules:Reserved fields for Account with bank |
| 49 | `PO.ACCT.WITH.BANK.RESERVED.2` | `PaymentOrder_AcctWithBankReserved2` | TField |  | Validation Rules:Reserved fields for Account with bank |
| 50 | `PO.ACCT.WITH.BANK.RESERVED.1` | `PaymentOrder_AcctWithBankReserved1` | TField |  | Validation Rules:Reserved fields for Account with bank |
| 51 | `PO.INTERMED.BANK.IBAN` | `PaymentOrder_IntermedBankIban` | TField |  | IBAN of Intermediary bank Validation Rules:Will be NOINPUT when transfer is not done through beneficairy. |
| 52 | `PO.INTERMED.BIC` | `PaymentOrder_IntermedBic` | TField |  | BIC of Intermediary bank. Validation Rules:Valid BIC record from DE.BIC. Will be NOINPUT when transfer is not done through beneficairy. |
| 53 | `PO.INTERMED.BANK.CUSTOMER` | `PaymentOrder_IntermedBankCustomer` | TField |  | Customer name of Intermediary bank. Validation Rules:Will be NOINPUT when transfer is not done through beneficairy. |
| 54 | `PO.INTERMED.BANK.POSTAL.ADDR.TYPE` | `PaymentOrder_IntermedBankPostalAddrType` | TField |  | Address type of Intermediary bank. Validation Rules:Will be NOINPUT when transfer is not done through beneficairy. |
| 55 | `PO.INTERMED.SWIFT.ADDR` | `PaymentOrder_IntermedSwiftAddr` |  |  |  |
| 56 | `PO.INTERMED.POSTAL.ADDR.LINE` | `PaymentOrder_IntermedPostalAddrLine` |  |  |  |
| 57 | `PO.INTERMED.BANK.CLEARING.CODE` | `PaymentOrder_IntermedBankClearingCode` | TField |  | Clearing code of Intermediary bank. Validation Rules:Will be NOINPUT when transfer is not done through beneficairy. |
| 58 | `PO.INTERMED.BANK.IDENTIFIER` | `PaymentOrder_IntermedBankIdentifier` | TField |  | Other Identifier of Intermediary bank. Validation Rules:Will be NOINPUT when transfer is not done through beneficairy. |
| 59 | `PO.INTERMED.BANK.COUNTRY` | `PaymentOrder_IntermedBankCountry` | TField |  | Country of Intermediary bank. Validation Rules:Will be NOINPUT when transfer is not done through beneficairy. |
| 60 | `PO.INTERMED.BANK.ACC` | `PaymentOrder_IntermedBankAcc` | TField | No | Optional The Account Number inputted here along with the Intermediary Bank details as given in INTERMED.BANK will be used in tag 56 of Swift message. |
| 61 | `PO.INTERMED.BANK.RESERVED.3` | `PaymentOrder_IntermedBankReserved3` | TField |  | Reserved fields for Intermed Bank. Validation Rules:NOINPUT field. |
| 62 | `PO.INTERMED.BANK.RESERVED.2` | `PaymentOrder_IntermedBankReserved2` | TField |  | Reserved fields for Intermed Bank. Validation Rules:NOINPUT field. |
| 63 | `PO.INTERMED.BANK.RESERVED.1` | `PaymentOrder_IntermedBankReserved1` | TField |  | Reserved fields for Intermed Bank. Validation Rules:NOINPUT field. |
| 64 | `PO.REMITTANCE.INFORMATION` | `PaymentOrder_RemittanceInformation` |  |  |  |
| 65 | `PO.PAYMENT.CURRENCY` | `PaymentOrder_PaymentCurrency` | TField |  | Credit account currency or Payment currency for the beneficiary Validation Rules:1. Must be present in the ALLOWED.PAYMENT.CCY in PAYMENT.ORDER.PRODUCT else error should be thrown3. Defaulted from PAYMENT.CCY field (36th field) of Beneficiary application for external payments |
| 66 | `PO.PAYMENT.AMOUNT` | `PaymentOrder_PaymentAmount` | TField | Yes | Amount to be paid i.e transaction amount Validation Rules:1. Defaulted from Beneficiary record - Preferred Payment amount field (37th field) for external payment2. Mandatory field |
| 67 | `PO.REQUESTED.CURRENCY` | `PaymentOrder_RequestedCurrency` | TField | No | Validation Rules:Optional currency used to specify the request amount to pay prior to conversion to payment currency. Allowed only when ALLOW.REQUESTED.CURRENCY is set to YES in PAYMENT.ORDER.PRODUCT. No Input for Phase I |
| 68 | `PO.REQUESTED.AMOUNT` | `PaymentOrder_RequestedAmount` | TField | No | Validation Rules:Optional amount in the request currency. Either requested amount or payment amount must be present. Allowed only when ALLOW.REQUESTED.CURRENCY is set to YES in PAYMENT.ORDER.PRODUCT. No Input for Phase I |
| 69 | `PO.PAYMENT.EXECUTION.DATE` | `PaymentOrder_PaymentExecutionDate` | TField |  | Processing date of the transaction Validation Rules:1. Can be manually input or defaulted2. If not manually input or if backdated, defaulted to TODAY's date3. Error must be thrown in following case: i. If Execution date is greater than today and ALLOW.FUTURE.DATE is set to NO in PAYMENT.ORDER.PRODUCT |
| 70 | `PO.REQUIRED.CREDIT.VALUE.DATE` | `PaymentOrder_RequiredCreditValueDate` | TField |  | Credit value date i.e. tentative date on which the payment system will process the payment Validation Rules:Override to be raised in the following scenarios:1. If ALLOW.REQUIRED.CREDIT.VALUE.DATE field is set to NO in PAYMENT.ORDER.PRODUCT2. If the date is less than today3. If the date is less the calculated float date |
| 71 | `PO.PAYMENT.PURPOSE` | `PaymentOrder_PaymentPurpose` | TField |  | Purpose code of the payment Validation Rules:Valid record in the table PAYMENT.PURPOSE.CODE |
| 72 | `PO.INVOICE.REFERENCE` | `PaymentOrder_InvoiceReference` |  |  |  |
| 73 | `PO.STRUCTURED.COMMUNICATION.CODE` | `PaymentOrder_StructuredCommunicationCode` | TField |  | Used for SEPA Validation Rules: |
| 74 | `PO.STRUCTURED.ISSUER` | `PaymentOrder_StructuredIssuer` | TField | No | Used for SEPA Validation Rules:Free Text of 65 characters. Optional. No validation |
| 75 | `PO.STRUCTURED.CREDITOR.REFERENCE` | `PaymentOrder_StructuredCreditorReference` | TField | No | Used for SEPA Validation Rules:Free Text of 25 characters. Optional. No validation |
| 76 | `PO.END.TO.END.REFERENCE` | `PaymentOrder_EndToEndReference` | TField | No | Used for SEPA Validation Rules:Free Text of 35 characters. Optional. No validation |
| 77 | `PO.INSTRUCTION.ID.REF` | `PaymentOrder_InstructionIdRef` | TField | No | Used for SEPA Validation Rules:Free Text of 35 characters. Optional. No validation |
| 78 | `PO.CHARGE.BEARER` | `PaymentOrder_ChargeBearer` | TField |  | Bearer of the charges of the order Validation Rules:1. Value can be manually selected or defaulted2. If not manually input, the value is defaulted as follows: i. From the Beneficiary record (BEN.OUR.CHARGES field) ii. If not present in Beneficiary, then from the DEFAULT.CHARGE.OPTION field of PAYMENT.ORDER.PRODUCT3. The field is validated as follows: i. For the PAYMENT.ORDER.PRODUCT, the ALLOWED.CHARGE.OPTIONS are obtained ii. The value defined in this field, is checked with the allowed charges iii. If it is not present, then an override is raised |
| 79 | `PO.WAIVE.ALL.CHARGES` | `PaymentOrder_WaiveAllCharges` | TField | No | Whether charges to be waived or not Validation Rules:Optional field. Value allowed is YES or Null. No validation |
| 80 | `PO.PAY.REQ.FX.CUST.RATE` | `PaymentOrder_PayReqFxCustRate` | TField |  | Validation Rules:Not allowed if PAY.REQ.FX.SPREAD and PAY.REQ.TREASURY.RATE fields have value |
| 81 | `PO.PAY.REQ.FX.SPREAD` | `PaymentOrder_PayReqFxSpread` | TField |  | Validation Rules:Not allowed if PAY.REQ.FX.CUST.RATE is defined |
| 82 | `PO.PAY.REQ.TREASURY.RATE` | `PaymentOrder_PayReqTreasuryRate` | TField |  | Validation Rules:Not allowed if PAY.REQ.FX.CUST.RATE is defined |
| 83 | `PO.ORDERING.PAYMENT.FX.CUST.RATE` | `PaymentOrder_OrderingPaymentFxCustRate` | TField |  | Customer rate for the conversion between payment currency and ordering currency Validation Rules: Allowed only when ALLOW.FX.RATE is set to YES in PAYMENT.ORDER.PRODUCT Customer rate needs to be equal to the sum of FX spread and Treasury rate When all the 3 fields -Cust rate, Spread and Treasury are- are input, get the default treasury rate for the currency pair from Currency application. If the user input treasury rate is equal to the default treasury rate, calculate the spread, and repopulate,if required When only Customer rate is input, treasury rate and spread are calculated and populated into the application. Override is raised if the spread is negative Override is raised if the rate tolerance percentage exceeds that of the value maintained in the PO Product Not all the 3 fields can be changed during amendment |
| 84 | `PO.ORDERING.PAYMENT.FX.SPREAD` | `PaymentOrder_OrderingPaymentFxSpread` | TField |  | Customer spread for the conversion between payment currency and ordering currency Validation Rules: Allowed only when ALLOW.FX.RATE is set to YES in PAYMENT.ORDER.PRODUCT Positive FX spread is added to the treasury rate to calculate the Cust rate and negative FX spread is deducted from the treasury rate to calculate the Cust rate. When FX spread and treasury rates are input, Cust rate is calculated and populated back to the PO record. When only FX spread is input, both Cust rate and treasury rate are arrived at and populated back to the PO record. User cannot input both When Cust rate and FX spread. Override is raised if the rate tolerance percentage exceeds that of the value maintained in the PO Product Not all the 3 fields can be changed during amendment |
| 85 | `PO.ORDERING.PAYMENT.TREASURY.RATE` | `PaymentOrder_OrderingPaymentTreasuryRate` | TField |  | Treasury rate for the conversion between payment currency and ordering currency Validation Rules: Allowed only when ALLOW.FX.RATE is set to YES in PAYMENT.ORDER.PRODUCT When only treasury rate is input, both Cust rate and FX spread are calculated and defaulted into the PO application. When Cust rate and treasury rates are input, both spread and treasury rates are calculated. Override is raised if the spread is negative Override is raised if the rate tolerance percentage exceeds that of the value maintained in the PO Product |
| 86 | `PO.INDICATIVE.RATE` | `PaymentOrder_IndicativeRate` | TField |  | Indicative rate for debit and payment ccy at time of booking the payment order Validation Rules:Indicative rate for debit and payment ccy at time of booking the payment order. Default Rate. NOINPUT field. Populated by system The value will be the sell rate of the curreny in the Currency application. |
| 87 | `PO.CURRENCY.MARKET` | `PaymentOrder_CurrencyMarket` | TField |  | The currency market to apply the corresponding exchange rates for conversion. This is applicable where more than one market exists for the currency. Validation Rules: If the user has not input the value or inputs the value where the exchange rates are not available, then default value of 1 will be considered. If the user inputs a valid currency market (other than value 1) where the exchange rates are available, then the currency market value is considered as imposed on to the payment system. |
| 88 | `PO.CLEARING.CHANNEL` | `PaymentOrder_ClearingChannel` | TField |  | Clearing channel for the order Validation Rules:1. Can be manually defined or defaulted2. For external payment, if beneficiary id is defined, defaulted from beneficiary record-CLEARING.TYPE field - 38th field3. It is validated as follows: i. Check PAYMENT.ORDER.PRODUCT record ii. If CLEARING.CHANNEL is defined, then locate the clearing channel defined in payment order with the clearing channels defined in payment order product iii. If it is not located, then raise override that Clearing channel not allowed for the product |
| 89 | `PO.REGULATORY.REPORT` | `PaymentOrder_RegulatoryReport` |  |  |  |
| 90 | `PO.MESSAGE.PRIORITY` | `PaymentOrder_MessagePriority` | TField |  | Priority of the message Validation Rules:Free text of 35 characters. No validations |
| 91 | `PO.BANK.TO.BANK.INFO` | `PaymentOrder_BankToBankInfo` |  |  |  |
| 92 | `PO.NARRATIVE` | `PaymentOrder_Narrative` |  |  |  |
| 93 | `PO.ADDITIONAL.INFO` | `PaymentOrder_AdditionalInfo` |  |  |  |
| 94 | `PO.INTERNAL.ORDER.DETAILS` | `PaymentOrder_InternalOrderDetails` |  |  |  |
| 95 | `PO.INTERNAL.STATUS` | `PaymentOrder_InternalStatus` | TField |  | Status of the order Validation Rules:RETURN_REJECT_CANCEL_ERROR |
| 96 | `PO.ORDER.EXECUTION.DATE.TIME` | `PaymentOrder_OrderExecutionDateTime` |  |  |  |
| 97 | `PO.PAYMENT.SYSTEM.ID` | `PaymentOrder_PaymentSystemId` | TField | No | Reference sent from payment system Validation Rules:Free Text of 35 characters. Optional. No validation |
| 98 | `PO.PAYMENT.SYSTEM.STATUS` | `PaymentOrder_PaymentSystemStatus` | TField |  | Current status of the order in payment system. Values to the field are defined in the EB.LOOKUP table with prefix "PAYMENT.STATUS". Validation Rules: 1. Standard T24 free text field. 2. Field no-input and cleared by copy function. 3. Can be updated only through other applications. |
| 99 | `PO.PAYMENT.STATUS.UPDATE.DATE` | `PaymentOrder_PaymentStatusUpdateDate` | TField |  | Date and time when the payment system status as last updated Validation Rules:NOINPUT field. Updated by system when PAYMENT.SYSTEM.STATUS field is updated |
| 100 | `PO.TERMS.AND.CONDITIONS` | `PaymentOrder_TermsAndConditions` | TField |  | Address fields of Ultimate creditor of payment. |
| 101 | `PO.CURRENT.STATE` | `PaymentOrder_CurrentState` | TField |  | Current state of the payment order Validation Rules:NOINPUT field. Will be updated by StateMachine |
| 102 | `PO.STATE.HIST` | `PaymentOrder_StateHist` |  |  |  |
| 103 | `PO.ORDER.INITIATION.TYPE` | `PaymentOrder_OrderInitiationType` | TField |  | An indicator to show whether the payment was initiated by bank user, corporate or private client Validation Rules:An indicator to show whether the payment was initiated by bank user, corporate or private client. EB.LOOKUP to be used |
| 104 | `PO.PAYMENT.CATEGORY` | `PaymentOrder_PaymentCategory` | TField |  | Field to define additional information related to SEPA standing order transactions which can be provided when a payment is initiated within T24 to be processed through payment suites. |
| 105 | `PO.PAYMENT.METHOD` | `PaymentOrder_PaymentMethod` | TField |  | Field to define method of transfer being initiated, which is required when it is to be processed through payment suites. |
| 106 | `PO.ORDER.TYPE` | `PaymentOrder_OrderType` | TField |  | Options field indicating whether Order is for Customer or Bank transfer, which is required when it is to be processed through payment suites. |
| 107 | `PO.INITIATOR.NAME` | `PaymentOrder_InitiatorName` | TField |  | Name of the initiator of payment. |
| 108 | `PO.INITIATOR.BIC` | `PaymentOrder_InitiatorBic` | TField |  | BIC code of initiator of payment. |
| 109 | `PO.INITIATOR.POST.ADDR.TYPE` | `PaymentOrder_InitiatorPostAddrType` | TField |  | Address type of the initiator of payment. |
| 110 | `PO.INITIATOR.SWIFT.ADDRESS` | `PaymentOrder_InitiatorSwiftAddress` |  |  |  |
| 111 | `PO.INITIATOR.POST.ADDR.LINE` | `PaymentOrder_InitiatorPostAddrLine` |  |  |  |
| 112 | `PO.DEBTOR.AGENT.NAME` | `PaymentOrder_DebtorAgentName` | TField |  | Name of the debtor agent of payment. |
| 113 | `PO.DEBTOR.AGENT.BIC` | `PaymentOrder_DebtorAgentBic` | TField |  | BIC code of Debtor Agent of payment. |
| 114 | `PO.DEBTOR.AGENT.ADDR.TYPE` | `PaymentOrder_DebtorAgentAddrType` | TField |  | Address type to be used for the Debtor Agent of payment. |
| 115 | `PO.DEBTOR.AGENT.ADDR.LINE` | `PaymentOrder_DebtorAgentAddrLine` |  |  |  |
| 116 | `PO.DEBTOR.AGENT.CLEARING.CODE` | `PaymentOrder_DebtorAgentClearingCode` | TField | No | Clearing code or sort code of the Debtor Agent. Validation Rules: Optional field. |
| 117 | `PO.DEBTOR.AGENT.IDENTIFIER` | `PaymentOrder_DebtorAgentIdentifier` | TField | No | Other Identification Code for Debtor Agent. Validation Rules: Optional field. |
| 118 | `PO.DEBTOR.AGENT.RESERVED.5` | `PaymentOrder_DebtorAgentReserved5` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 119 | `PO.DEBTOR.AGENT.RESERVED.4` | `PaymentOrder_DebtorAgentReserved4` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 120 | `PO.DEBTOR.AGENT.RESERVED.3` | `PaymentOrder_DebtorAgentReserved3` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 121 | `PO.DEBTOR.AGENT.RESERVED.2` | `PaymentOrder_DebtorAgentReserved2` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 122 | `PO.DEBTOR.AGENT.RESERVED.1` | `PaymentOrder_DebtorAgentReserved1` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 123 | `PO.ULTIMATE.DEBTOR.NAME` | `PaymentOrder_UltimateDebtorName` | TField |  | Name of the Ultimate debitor of payment. |
| 124 | `PO.ULTIMATE.DEBTOR.ADDR.TYPE` | `PaymentOrder_UltimateDebtorAddrType` | TField |  | Address type to be used for the Ultimate debtor of payment. |
| 125 | `PO.ULTIMATE.DEBTOR.ADDR.LINE` | `PaymentOrder_UltimateDebtorAddrLine` |  |  |  |
| 126 | `PO.ULTIMATE.DEBTOR.BIC` | `PaymentOrder_UltimateDebtorBic` | TField |  | BIC code of Ultimate debtor of payment. |
| 127 | `PO.ULTIMATE.DEBTOR.COUNTRY` | `PaymentOrder_UltimateDebtorCountry` | TField |  | Country of Ultimate debtor of payment. |
| 128 | `PO.INT.OVERRIDE.ID` | `PaymentOrder_IntOverrideId` |  |  |  |
| 129 | `PO.INT.OVERRIDE.VAL` | `PaymentOrder_IntOverrideVal` |  |  |  |
| 130 | `PO.ACTIVITY.CODE` | `PaymentOrder_ActivityCode` |  |  |  |
| 131 | `PO.MESSAGE.TYPE` | `PaymentOrder_MessageType` |  |  |  |
| 132 | `PO.DELIVERY.REF` | `PaymentOrder_DeliveryRef` |  |  |  |
| 133 | `PO.ULTIMATE.CREDITOR.NAME` | `PaymentOrder_UltimateCreditorName` | TField |  | Name of the Ultimate creditor of payment. |
| 134 | `PO.ULTIMATE.CREDITOR.ADDR.TYPE` | `PaymentOrder_UltimateCreditorAddrType` | TField |  | Address type to be used for the Ultimate creditor of payment. |
| 135 | `PO.ULTIMATE.CRED.ADDR.LN` | `PaymentOrder_UltimateCredAddrLn` |  |  |  |
| 136 | `PO.ULTIMATE.CREDITOR.BIC` | `PaymentOrder_UltimateCreditorBic` | TField |  | BIC code of Ultimate creditor of payment. |
| 137 | `PO.ULTIMATE.CREDITOR.COUNTRY` | `PaymentOrder_UltimateCreditorCountry` | TField |  | Country of Ultimate creditor of payment. |
| 138 | `PO.ULTIMATE.CREDITOR.DOB` | `PaymentOrder_UltimateCreditorDob` | TField |  | Holds the birth date of the Ultimate Creditor Validation Rules: It can be used when Ultimate Creditor Identifier Type is set to Private |
| 139 | `PO.ULTIMATE.CREDITOR.BR.PRVNC` | `PaymentOrder_UltimateCreditorBrPrvnc` | TField | Yes | Holds the birth province of the Ultimate Creditor Validation Rules: It can be used when Ultimate Creditor Identifier Type is set to Private Ultimate Creditor Birth Date is mandatory when this field is captured |
| 140 | `PO.ULTIMATE.CREDITOR.BR.CITY` | `PaymentOrder_UltimateCreditorBrCity` | TField | Yes | Holds the birth city of the Ultimate Creditor Validation Rules: It can be used when Ultimate Creditor Identifier Type is set to Private Ultimate Creditor Birth Date is mandatory when this field is captured |
| 141 | `PO.ULTIMATE.CREDITOR.BR.COUNTRY` | `PaymentOrder_UltimateCreditorBrCountry` | TField | Yes | Holds the birth country of the Ultimate Creditor Validation Rules: It must be a valid code on the COUNTRY table It can be used when Ultimate Creditor Identifier Type is set to Private Ultimate Creditor Birth Date is mandatory when this field is captured |
| 142 | `PO.ULTIMATE.CREDITOR.OT.ID.TYPE` | `PaymentOrder_UltimateCreditorOtIdType` | TField | No | Optional Ultimate Creditor Id Type identifies if the Ultimate Creditor is an Organisation or an Individual Possible values: None Organisation Private |
| 143 | `PO.INSTRUCTION.CODE` | `PaymentOrder_InstructionCode` |  |  |  |
| 144 | `PO.INSTRUCTION.CODE.TEXT` | `PaymentOrder_InstructionCodeText` |  |  |  |
| 145 | `PO.PYMT.INFO.SER.LEVEL.CODE` | `PaymentOrder_PymtInfoSerLevelCode` |  |  |  |
| 146 | `PO.ORDERING.CUSTOMER.SSI` | `PaymentOrder_OrderingCustomerSsi` | TField |  | Indicates the record which stores the Ordering Customer SSI details. If defined, system defaults the related values from the corresponding beneficiary record to the debit information in the payment order record. Debit Account details that are manually provided by user would take priority and default will not be done even is Ordering CUstomer SSI is provided Validation Rules: - Valid Id in the BENEFICIARY table |
| 147 | `PO.PAYMENT.SYSTEM` | `PaymentOrder_PaymentSystem` | TField |  | Indicates the payment system through which the requests/transactions initiated by the payment order is processed. Valid Values: 1. External - Requests are processed by external system 2. TPS - Requests are processed by TPS 3. FT - Requests are processed by FT Validation Rules: - No input field, updated while authorising the payment order record. |
| 148 | `PO.PAYMENT.STATUS.ADD.INFO` | `PaymentOrder_PaymentStatusAddInfo` | TField |  | Field to record additional status information or narratives which describes the current status of the payment order in the payment system. This value will be updated by the payment system which has processed the contract. Validation Rules: 1. Standard T24 free text field. 2. Field no-input and cleared by copy function. 3. Can be updated only through other applications. |
| 149 | `PO.PAYMENT.COMPLETE` | `PaymentOrder_PaymentComplete` | TField |  | Filed to indicate if the payment order processing is complete. This is updated by the payment system through which the payment order is processed. Once this flag is set, the current state of the payment order is moved to Complete. Validation Rules: 1. Standard T24 flag field. 2. Field no-input and cleared by copy function. 3. Can be updated only through other applications. |
| 150 | `PO.MANUAL.PAYMENT.STATUS` | `PaymentOrder_ManualPaymentStatus` | TField |  | Field to indicate the current status of the order in payment system and is manually updated by the user in exceptional scenarios. Values to the field are defined in the EB.LOOKUP table with prefix "PAYMENT.STATUS". Validation Rules: 1. Standard T24 Alphanumeric field. 2. Field no-input and cleared by copy function. 3. Available for input by the user only through browser when the order state is "AwaitingAck" or "Placed" or "Complete". |
| 151 | `PO.MANUAL.PAY.STATUS.ADD.INFO` | `PaymentOrder_ManualPayStatusAddInfo` | TField |  | Field to record additional status information or narratives which describes the current status of the payment order in the payment system.This is updated by the user while updating the manual payment status. Validation Rules: 1. Standard T24 free text field. 2. Field No-input and cleared by copy function. 3. Available for input by the user only through browser when the order state is "AwaitingAck" or "Placed" or "Complete". |
| 152 | `PO.MANUAL.COMPLETE` | `PaymentOrder_ManualComplete` | TField |  | Field to indicate if the payment order has been manually marked for completion and is updated by the user for exceptional cases where payment system could not update the status of payment order. Once this flag is set, the current state of the payment order is moved to Complete. Validation Rules: 1. Standard T24 flag field. 2. Field no-input and cleared by copy function. 3. Available for input by the user only through browser when the order state is "AwaitingAck" or "Placed" or "Complete". |
| 153 | `PO.MANUAL.STATUS.UPDATE.DATE` | `PaymentOrder_ManualStatusUpdateDate` | TField |  | Date and time when the manual payment status is last updated. Validation Rules: 1. Standard T24 Alphanumeric field. 2. Field no-input and cleared by copy function. 3. Updated by system when MANUAL.PAYMENT.STATUS or MANUAL.PAY.STATUS.ADD.INFO or MANUAL.COMPLETE fields are updated. |
| 154 | `PO.CHARGE.ACCOUNT` | `PaymentOrder_ChargeAccount` | TField |  | Indicates the account to which the charges has to be levied. Validation Rules: User Inputtable. |
| 155 | `PO.CHARGE.ACCOUNT.CCY` | `PaymentOrder_ChargeAccountCcy` | TField |  | Represent the currency of the CHARGE.ACCOUNT. Validation Rules: When CHARGE.ACCOUNT has value then the currency will be validated against the CHARGE.ACCOUNT field. When the field is blank and the Account being T24.ACCOUNT system will auto populate the currency of the account defined in CHARGE.ACCOUNT. else if the Account is external, then system will insist user to input the currency. So that charges can be calculated in that currency also. |
| 156 | `PO.CHARGE.TYPE` | `PaymentOrder_ChargeType` |  |  |  |
| 157 | `PO.CHARGE.DESCRIPTION` | `PaymentOrder_ChargeDescription` |  |  |  |
| 158 | `PO.CHARGE.CURRENCY` | `PaymentOrder_ChargeCurrency` |  |  |  |
| 159 | `PO.CHARGE.AMOUNT` | `PaymentOrder_ChargeAmount` |  |  |  |
| 160 | `PO.CHARGE.AC.CCY.AMOUNT` | `PaymentOrder_ChargeAcCcyAmount` |  |  |  |
| 161 | `PO.CREDIT.VALUE.DATE` | `PaymentOrder_CreditValueDate` | TField | No | Value date for credit Validation Rules: User will be allowed to input based on configuration in the Payment Order Product. Credit value date passed to payment system, only when user inputs. When both Required Credit Value Date and Credit Value Date are input, only Credit Value Date is considered. Optional field. Date less than TODAY can be inputted if Check Transparency and Calc Value Date is not set in PAYMENT.ORDER.PRODUCT. Validation error will be thrown if the Credit Value Date is less than Debit Value Date. Override will be raised if it is less than TODAY or if it is a non-working day. When user inputs Credit Value Date, it will be imposed in the payment system |
| 162 | `PO.CUT.OFF.TIME` | `PaymentOrder_CutOffTime` | TField |  | Time until which transaction can be submitted to payment system Validation Rules: NOINPUT field. Mapped during simulation |
| 163 | `PO.PSD.COMPLIANT` | `PaymentOrder_PsdCompliant` | TField |  | Field to indicate if transaction is PSD compliant or Not Validation Rules: NOINPUT field. |
| 164 | `PO.LAST.TC.SIM.TIME` | `PaymentOrder_LastTcSimTime` | TField |  | Field to indicate time when payment order was last simulated Validation Rules: NOINPUT field. |
| 165 | `PO.TC.SIM.CHECKED` | `PaymentOrder_TcSimChecked` | TField |  | Field to indicate if simulation verified or not Validation Rules: NOINPUT field. Yes - Simulation verified No - Simulation not verified |
| 166 | `PO.CONTEXT.NAME` | `PaymentOrder_ContextName` |  |  |  |
| 167 | `PO.CONTEXT.VALUE` | `PaymentOrder_ContextValue` |  |  |  |
| 168 | `PO.SUBMIT.ORDER` | `PaymentOrder_SubmitOrder` | TField |  | Field to trigger Awaiting Ext Submit state Validation Rules: YES - Order submitted to first state NO - Order placed in AwaitingExtSubmit |
| 169 | `PO.TOTAL.DEBIT.AMOUNT` | `PaymentOrder_TotalDebitAmount` | TField |  | Field holding total debit amount including charge and transaction debit amount Validation Rules: NOINPUT field. Populated from TPS during simulation |
| 170 | `PO.STATUS.REASON.CODE` | `PaymentOrder_StatusReasonCode` | TField | No | Optional If the order was previously rejected by the supervisor, user will be able to view the reject reason code and remark. User can add a reject response |
| 171 | `PO.LOCAL.INSTR.CODE` | `PaymentOrder_LocalInstrCode` | TField |  |  |
| 172 | `PO.INIT.OTHER.ID.TYPE` | `PaymentOrder_InitOtherIdType` | TField |  |  |
| 173 | `PO.INIT.OTHER.ID` | `PaymentOrder_InitOtherId` | TField |  |  |
| 174 | `PO.FRAUD.CHECK.INDICATOR` | `PaymentOrder_FraudCheckIndicator` | TField |  | Indicates whether the fraud check has been successfully completed or not Possible values are SUCCESS, FAILED, PENDING or TIMEOUT or HOLD. Based on this field, further processing of Payment order will take place Validation Rules: - This is a NOINPUT field generally but when the status of the Payment order is FraudCheck input is allowed. |
| 175 | `PO.LOCAL.INSTR.PROP` | `PaymentOrder_LocalInstrProp` | TField |  |  |
| 176 | `PO.AC.FUNDS.AUTH.ID` | `PaymentOrder_AcFundsAuthId` | TField |  | This field either automatically captures the record id of AC.FUNDS.AUTHORISATION when AUTO.RETY is set to YES in PAYMENT.ORDER.PRODUCT or it should be manually keyed in when PRE.APPROVED.PAYMENT is set as YES in PAYMENT.ORDER.PARAMETER. Validation Rules: User input will be allowed only when the PRE.APPROVED.PAYMENT is set to YES else user input is not allowed (Only updated by system when creating the AC.FUNDS.AUTHORISATION record). |
| 177 | `PO.LOCKED.EVENT.ID` | `PaymentOrder_LockedEventId` | TField |  | To capture the AC.LOCKED.EVENTS id if in case the funds is available and reserved. Validation Rules: It is made user inputtable only when "AC" module is installed. User needs to specify a valid AC.LOCKED.EVENTS id. In such a case, the user should ensure that Reserve Funds and Check Funds options are not enabled at the payment order product level. If AC module is not installed user input will not be allowed, only updated by system when creating AC.LOCKED.EVENTS record. |
| 178 | `PO.INITIAL.PRODUCT` | `PaymentOrder_InitialProduct` | TField |  | This field is used to store the product that was initially given when the Payment Order is initiated Validation Rules: This field contains value only when the Product is changed to Cut off product or product determined from Rule or API No inputtable field |
| 179 | `PO.ONUS.INDICATOR` | `PaymentOrder_OnusIndicator` | TField |  | Indicates if the transaction is a ONUS payment Allowed options are either "YES" or "NO". Validation Rules: No input field |
| 180 | `PO.ORD.ACCOUNT.LOCATION` | `PaymentOrder_OrdAccountLocation` | TField |  | Location of the ordering account returned from the locator service - it is either "Own" meaning it belongs to T24. External it is not in the bank, or a location code returned by the account locator service. Its a NOINPUT field. |
| 181 | `PO.ORD.ACCOUNT.VALIDATED` | `PaymentOrder_OrdAccountValidated` | TField |  | Indicator to note that validation has been done for the ordering account. Its a NOINPUT field. |
| 182 | `PO.BEN.ACCOUNT.LOCATION` | `PaymentOrder_BenAccountLocation` | TField |  | Location of the beneficiary account returned from the locator service - it is either "Own" meaning it belongs to T24. External it is not in the bank, or a location code returned by the account locator service. Its a NOINPUT field. |
| 183 | `PO.BEN.ACCOUNT.VALIDATED` | `PaymentOrder_BenAccountValidated` | TField |  | Indicator to note that validation has been done for the beneficiary account. Its a NOINPUT field. |
| 184 | `PO.CHEQUE.NUMBER` | `PaymentOrder_ChequeNumber` | TField | No | Optional field which indicates the Cheque/Draft number in case of Draft Payments via TPH payment system Validation Rules: Cannot be blank in case of Draft Payments. If the Stock Register Id and Stock Series Id are mentioned, then the cheque/Draft number must be available in the Stock Register |
| 185 | `PO.ISSUE.CHEQUE.TYPE` | `PaymentOrder_IssueChequeType` | TField | No | Optional field which contains the type of Cheque issued such as Current, Savings or Drafts Validation Rules: Must be a valid record from CHEQUE.TYPE |
| 186 | `PO.STOCK.REGISTER.ID` | `PaymentOrder_StockRegisterId` | TField | No | Optional field to indicate the Stock Register Id which must be checked to confirm if the given Cheque number is available or not When the Contract is committed, the given Cheque number is made unavailable from the respective register, and it is restored when the payment is reversed or cancelled or rejected Validation Rules: Must be a valid record from STOCK.REGISTER |
| 187 | `PO.STOCK.SERIES.ID` | `PaymentOrder_StockSeriesId` | TField | No | Optional field to indicate the Stock Series Id against which the Cheque number must be checked in the Stock Register for availability Validation Rules: Though no error is raised, both Stock Register and Stock Series Id is required to check if the given Cheque number is available in the Register |
| 188 | `PO.BENEFICIARY.OT.ID` | `PaymentOrder_BeneficiaryOtId` | TField | Conditional | Holds other identifications such as could be a Social Security Number, a Tax Identification Number, Passport Number, a Clearing Id ,etc., of the beneficiary Optional Validation Rules: Beneficiary Id Type is mandatory when this field is captured If populated then either Beneficiary Scheme Code or Beneficiary Scheme Proprietary must be populated |
| 189 | `PO.BENEFICIARY.SCHME.CDE` | `PaymentOrder_BeneficiarySchmeCde` | TField | Yes | The code of the scheme which issued the identifier for the Beneficiary It will indicate what is captured in the Beneficiary Other Identifier - Social Security Number, Tax Identification Number, Passport Number, Clearing Id Validation Rules: Beneficiary Id Type is mandatory when this field is captured |
| 190 | `PO.BENEFICIARY.SCH.PRTY` | `PaymentOrder_BeneficiarySchPrty` | TField | Yes | The proprietary code of the scheme which issued the identifier for the Beneficiary Validation Rules: Beneficiary Id Type is mandatory when this field is captured |
| 191 | `PO.BENEFICIARY.SCH.ISSUR` | `PaymentOrder_BeneficiarySchIssur` | TField | Yes | Holds the Id of the Issuer of Ben Other ID Validation Rules: Beneficiary Id Type is mandatory when this field is captured |
| 192 | `PO.ULTIMATE.CREDITOR.OT.ID` | `PaymentOrder_UltimateCreditorOtId` | TField | Yes | Holds other identifications such as could be a Social Security Number, a Tax Identification Number, Passport Number, a Clearing Id ,etc., of the Ultimate Creditor Validation Rules: Ultimate Creditor Id Type is mandatory when this field is captured |
| 193 | `PO.ULTIMATE.CREDITOR.SCHME.CDE` | `PaymentOrder_UltimateCreditorSchmeCde` | TField | Yes | The code of the scheme, which issued the identifier for the Ultimate Creditor It will indicate what is captured in the Beneficiary Other Identifier - Social Security Number, Tax Identification Number, Passport Number, Clearing Id Validation Rules: Ultimate Creditor Id Type is mandatory when this field is captured |
| 194 | `PO.ULTIMATE.CREDITOR.SCH.PRTY` | `PaymentOrder_UltimateCreditorSchPrty` | TField | Yes | The proprietary code of the scheme which issued the identifier for the Ultimate Creditor. Validation Rules: Ultimate Creditor Id Type is mandatory when this field is captured |
| 195 | `PO.ULTIMATE.CREDITOR.SCH.ISSUR` | `PaymentOrder_UltimateCreditorSchIssur` | TField | Yes | Issuer of the identifier Validation Rules: Ultimate Creditor Id Type is mandatory when this field is captured |
| 196 | `PO.ORDERING.COUNTRY.RESIDENCE` | `PaymentOrder_OrderingCountryResidence` | TField |  | Holds the Country of residence for Debtor Validation Rules: Default CUSTOMER>RESIDENCE It must be a valid code on the COUNTRY table. |
| 197 | `PO.ULTIMATE.DEBTOR.DOB` | `PaymentOrder_UltimateDebtorDob` | TField |  | Holds the birth date of the Ultimate Debtor Validation Rules: It can be used when Ultimate Debtor Identifier Type is set to Private |
| 198 | `PO.ULTIMATE.DEBTOR.BR.PRVNC` | `PaymentOrder_UltimateDebtorBrPrvnc` | TField | Yes | Holds the birth Province of the Ultimate Debtor Validation Rules: It can be used when Ultimate Debtor Identifier Type is set to Private Ultimate Debtor Birth Date is mandatory when this field is captured. |
| 199 | `PO.LOCAL.REF` | `PaymentOrder_LocalRef` |  |  |  |
| 200 | `PO.OVERRIDE` | `PaymentOrder_Override` |  |  |  |
| 201 | `PO.RECORD.STATUS` | `PaymentOrder_RecordStatus` | String |  |  |
| 202 | `PO.CURR.NO` | `PaymentOrder_CurrNo` | String |  |  |
| 203 | `PO.INPUTTER` | `PaymentOrder_Inputter` |  |  |  |
| 204 | `PO.DATE.TIME` | `PaymentOrder_DateTime` |  |  |  |
| 205 | `PO.AUTHORISER` | `PaymentOrder_Authoriser` | String |  |  |
| 206 | `PO.CO.CODE` | `PaymentOrder_CoCode` | String |  |  |
| 207 | `PO.DEPT.CODE` | `PaymentOrder_DeptCode` | String |  |  |
| 208 | `PO.AUDITOR.CODE` | `PaymentOrder_AuditorCode` | String |  |  |
| 209 | `PO.AUDIT.DATE.TIME` | `PaymentOrder_AuditDateTime` | String |  |  |
| 210 | `PO.ULTIMATE.DEBTOR.BR.CITY` | `PaymentOrder_UltimateDebtorBrCity` | TField | Yes | Holds the birth City of the Ultimate Debtor Validation Rules: It can be used when Ultimate Debtor Identifier Type is set to Private Ultimate Debtor Birth Date is mandatory when this field is captured. |
| 211 | `PO.ULTIMATE.DEBTOR.BR.COUNTRY` | `PaymentOrder_UltimateDebtorBrCountry` | TField | Yes | Holds the birth Country of the Ultimate Debtor Validation Rules: It must be a valid code on the COUNTRY table. It can be used when Ultimate Debtor Identifier Type is set to Private Ultimate Debtor Birth Date is mandatory when this field is captured. |
| 212 | `PO.ULTIMATE.DEBTOR.OT.ID.TYPE` | `PaymentOrder_UltimateDebtorOtIdType` | TField | No | Optional Ultimate Debtor Id Type identifies if the Ultimate Debtor is an Organisation or an Individual Possible values: None Organisation Private |
| 213 | `PO.ULTIMATE.DEBTOR.OT.ID` | `PaymentOrder_UltimateDebtorOtId` | TField | Yes | Holds other identifications such as could be a Social Security Number, a Tax Identification Number, Passport Number, a Clearing Id ,etc., of the Ultimate Debtor. Validation Rules: Ultimate Debtor Id Type is mandatory when this field is captured |
| 214 | `PO.ULTIMATE.DEBTOR.SCHME.CDE` | `PaymentOrder_UltimateDebtorSchmeCde` | TField | Yes | The code of the scheme, which issued the identifier for the Ultimate Debtor It will indicate what is captured in the Beneficiary Other Identifier - Social Security Number,Tax Identification Number, Passport Number, Clearing Id Validation Rules: Ultimate Debtor Id Type is mandatory when this field is captured. |
| 215 | `PO.ULTIMATE.DEBTOR.SCH.PRTY` | `PaymentOrder_UltimateDebtorSchPrty` | TField | Yes | The proprietary code of the scheme, which issued the identifier for the Ultimate Debtor Validation Rules: Ultimate Debtor Id Type is mandatory when this field is captured. |
| 216 | `PO.ULTIMATE.DEBTOR.SCH.ISSUR` | `PaymentOrder_UltimateDebtorSchIssur` | TField | Yes | Issuer of the identifier Validation Rules: Ultimate Debtor Id Type is mandatory when this field is captured |
| 217 | `PO.BULK.REFERENCE` | `PaymentOrder_BulkReference` | TField | No | Optional This field contains the Bulk Reference generated in ESB for a batch containing more than one transaction and will be used as a unique identifier for each bulk present/part of the Payment Initiation message (pain.001). If the Bulk Reference is associated with a payment then it helps in identifying/tracing the payments that is part of a bulk containing other transactions (more than 1). |
| 218 | `PO.ACCEPTANCE.DATE.TIME` | `PaymentOrder_AcceptanceDateTime` |  |  |  |
| 219 | `PO.BULK.SENDER.REFERENCE` | `PaymentOrder_BulkSenderReference` | TField | No | Optional Payment Information Identification ID (Bulk level) in a pain.001 received from the sender. |
| 220 | `PO.ORIGINAL.MSG.CONTENT` | `PaymentOrder_OriginalMsgContent` | TField | No | Optional This field will store the transaction content from the xml file .Each transaction will also include group header and bulk level details from the XML. |
| 221 | `PO.BENEFICIARY.CONT.MOB` | `PaymentOrder_BeneficiaryContMob` | TField | No | Optional Mobile phone number on which the beneficiary can be contacted. |
| 222 | `PO.BENEFICIARY.CONT.FAX` | `PaymentOrder_BeneficiaryContFax` | TField | No | Optional Fax number on which the beneficiary can be contacted. |
| 223 | `PO.BENEFICIARY.CONT.EML` | `PaymentOrder_BeneficiaryContEml` | TField | No | Optional Email on which the beneficiary can be contacted. |
| 224 | `PO.BENEFICIARY.CONT.OTH` | `PaymentOrder_BeneficiaryContOth` | TField | No | Optional Contact details in another form on which the beneficiary can be contacted. |
| 225 | `PO.ORDERING.OT.ID.TYPE` | `PaymentOrder_OrderingOtIdType` | TField | No | Optional Unique identification assigned by the account servicer. |
| 226 | `PO.ORDERING.OT.ID` | `PaymentOrder_OrderingOtId` | TField | No | Optional Unique identification as assigned by an institution, using an identification scheme. |
| 227 | `PO.ORDERING.SCHME.CDE` | `PaymentOrder_OrderingSchmeCde` | TField | No | Optional Name of the identification scheme, in a coded form as published in an external list. |
| 228 | `PO.ORDERING.SCH.PRTY` | `PaymentOrder_OrderingSchPrty` | TField | No | Optional Name of the identification scheme, in a free text form. |
| 229 | `PO.ORDERING.SCH.ISSUR` | `PaymentOrder_OrderingSchIssur` | TField | No | Optional Entity that assigns the identification. |
| 230 | `PO.ORDERING.DOB` | `PaymentOrder_OrderingDob` | TField | No | Optional Date on which a person is born. |
| 231 | `PO.ORDERING.BR.PRVNC` | `PaymentOrder_OrderingBrPrvnc` | TField | No | Optional Province where a person was born. |
| 232 | `PO.ORDERING.BR.CITY` | `PaymentOrder_OrderingBrCity` | TField | No | Optional City where a person was born. |
| 233 | `PO.ORDERING.BR.COUNTRY` | `PaymentOrder_OrderingBrCountry` | TField | No | Optional Country where a person was born. |
| 234 | `PO.REJECTED.BY` | `PaymentOrder_RejectedBy` | TField | No | Optional User who Rejected the order in the approval chain |
| 235 | `PO.REJECT.DATE.TIME` | `PaymentOrder_RejectDateTime` |  |  |  |
| 236 | `PO.STATUS.REASON.REMARK` | `PaymentOrder_StatusReasonRemark` |  |  |  |
| 237 | `PO.STATUS.REASON.RESPONSE` | `PaymentOrder_StatusReasonResponse` |  |  |  |
| 238 | `PO.CANCEL.REASON` | `PaymentOrder_CancelReason` | TField | No | Optional If the order is cancelled by the user, User can update reason for cancellation |
| 239 | `PO.CANCEL.REMARK` | `PaymentOrder_CancelRemark` | TField | No | Optional If the order is cancelled by the user, this field will get updated with Cancel Remarks |
| 240 | `PO.CANCEL.INITIATED.BY` | `PaymentOrder_CancelInitiatedBy` | TField | No | Optional User initiated the cancellation |
| 241 | `PO.SOURCE` | `PaymentOrder_Source` | TField | No | Optional Manual or UPLOAD |
| 242 | `PO.BULK.PROCESSING.MODE` | `PaymentOrder_BulkProcessingMode` | TField |  | Process the bulk in batch mode or transaction mode Allowed values 'SINGLE' or 'MULTI' |
| 243 | `PO.USER.ACTION` | `PaymentOrder_UserAction` | TField | No | Optional User can select the action that needs to be performed on the Bulk payment order Authorise, Reject, Cancel, Discard |
| 244 | `PO.PAYMENT.CATEGORYPURP.PRTY` | `PaymentOrder_PaymentCategorypurpPrty` | TField | No | Optional The proprietary code of the scheme which issued the identifier related to SEPA standing order transactions which can be provided when a payment is initiated within T24 to be processed through payment suites |
| 245 | `PO.CUSTOMER.CONSENT` | `PaymentOrder_CustomerConsent` | TField | No | Optional This field indicates if Ordering customer has provided consent for this payment order to be initiated. The field is relevant only in case of Open Banking. Value can be up to three characters. (example - Y, YES, N, NO) |
| 246 | `PO.AUTHORISATION.ID` | `PaymentOrder_AuthorisationId` | TField |  | Free text field to hold the Authoriser Id of the Payment Order. This field is expected be updated by external API. Field is enabled only when PX is installed Input allowed only if the payment has been previously submitted by the external API |
| 247 | `PO.EXEMPT.FROM.SCA` | `PaymentOrder_ExemptFromSca` | TField | No | Optional Field Field is enabled only when PX is installed System should set this flag to YES, if PAYMENT.ORDER initiated from external API are SCA (Strong Customer Authentication) exempted |
| 248 | `PO.REMITTED.CCY` | `PaymentOrder_RemittedCcy` | TField |  | Details on the amounts of the referred document - Currency of the remitted amount. |
| 249 | `PO.REMITTED.AMOUNT` | `PaymentOrder_RemittedAmount` | TField |  | Details on the amounts of the referred document - Amount of money remitted for the referred document. |
| 250 | `PO.REG.DEBTOR.CREDITOR.RPT` | `PaymentOrder_RegDebtorCreditorRpt` |  |  |  |
| 251 | `PO.REG.AUTHORITY.NAME` | `PaymentOrder_RegAuthorityName` |  |  |  |
| 252 | `PO.REG.AUTHORITY.CTRY.CODE` | `PaymentOrder_RegAuthorityCtryCode` |  |  |  |
| 253 | `PO.REG.REP.TYPE` | `PaymentOrder_RegRepType` |  |  |  |
| 254 | `PO.REG.REP.DATE` | `PaymentOrder_RegRepDate` |  |  |  |
| 255 | `PO.REG.REP.COUNTRY.CODE` | `PaymentOrder_RegRepCountryCode` |  |  |  |
| 256 | `PO.REG.REP.CODE` | `PaymentOrder_RegRepCode` |  |  |  |
| 257 | `PO.REG.REP.CCY` | `PaymentOrder_RegRepCcy` |  |  |  |
| 258 | `PO.REG.REP.AMOUNT` | `PaymentOrder_RegRepAmount` |  |  |  |
| 259 | `PO.REG.REP.INFORMATION` | `PaymentOrder_RegRepInformation` |  |  |  |
| 260 | `PO.DEBTOR.NAME.PREFIX` | `PaymentOrder_DebtorNamePrefix` | TField |  | Specifies the terms used to formally address a person. |
| 261 | `PO.DEBTOR.NAME` | `PaymentOrder_DebtorName` | TField |  | Name by which a party is known and which is usually used to identify that party . |
| 262 | `PO.DEBTOR.PHONE.NUMBER` | `PaymentOrder_DebtorPhoneNumber` | TField |  | Collection of information that identifies a phone number, as defined by telecom services. |
| 263 | `PO.DEBTOR.MOBILE.NUMBER` | `PaymentOrder_DebtorMobileNumber` | TField |  | Collection of information that identifies a mobile number, as defined by telecom services. |
| 264 | `PO.DEBTOR.FAX` | `PaymentOrder_DebtorFax` | TField |  | Collection of information that identifies a FAX number, as defined by telecom services. |
| 265 | `PO.DEBTOR.EMAIL.ADR` | `PaymentOrder_DebtorEmailAdr` | TField |  | Address for electronic mail. |
| 266 | `PO.DEBTOR.OTHER` | `PaymentOrder_DebtorOther` | TField |  | Contact Details in other form. |
| 267 | `PO.PURPOSE.PROPRIETARY` | `PaymentOrder_PurposeProprietary` | TField |  | This field to store additional details related to purpose of payment which is specific to Clearing |
| 268 | `PO.ORIGINAL.REQ.EXECUTION.DATE` | `PaymentOrder_OriginalReqExecutionDate` | TField | No | Stores RED as received in payment initiation request.No Change field.Its an Optional Field |
| 269 | `PO.BENEFICIARY.ALIAS.TYPE` | `PaymentOrder_BeneficiaryAliasType` | TField |  | Field to indicate the Type of the Alias |
| 270 | `PO.GPI.STATUS` | `PaymentOrder_GpiStatus` | TField |  | This field to store the GPI status as received in gpi confirmation tracker. |
| 271 | `PO.GPI.REASON` | `PaymentOrder_GpiReason` | TField |  | This field to store the reason code (which is along with GPI status like ACSP, RJCT) as received in gpi confirmation tracker. |
| 272 | `PO.GPI.DATE.TIME` | `PaymentOrder_GpiDateTime` |  |  |  |
| 273 | `PO.UNIQUE.TXN.REFERENCE` | `PaymentOrder_UniqueTxnReference` | TField |  | Field to store the UETR in gpi confirmation. |
| 274 | `PO.PAYMENT.EXECUTION.TIME` | `PaymentOrder_PaymentExecutionTime` | TField |  | This field can be stamped by the system with the next available execution time (System Time) as defined in the Payment Order product. Such payment orders will be parked in 'WarehouseOrder' status and then executed at the defined time. This field can also be input by the user while initiating a payment order with the execution time for the payment, thus replacing the stamped value. Such payment orders will be parked in Payment order warehouse or Payment system warehouse (based on configuration) and released for further processing when corresponding service runs at configured time. Validation Rules: Standard Time Format - HH:MM |
| 275 | `PO.CREDIT.NOSTRO.ACCOUNT` | `PaymentOrder_CreditNostroAccount` | TField | No | This field is to capture the Correspondent Nostro Account to be used to credit the payment. This field is instructed when there are multiple Nostro-Vostro Accounts maintained by a bank with its correspondents. The account number is passed to payment system to be used for Credit Posting. Validation Rules: Optional field Valid T24 NOSTRO account |
| 276 | `PO.ORDERING.CUSTOMER.ACCOUNT` | `PaymentOrder_OrderingCustomerAccount` | TField | No | This field is to capture the ordering customer account Validation Rules: Optional field No validation on this field by POA. |
| 277 | `PO.RECEIVER.BIC` | `PaymentOrder_ReceiverBic` | TField | No | Validation Rules: Optional field POA should validate against the RD module for BIC validation |
| 278 | `PO.CREDIT.AMOUNT` | `PaymentOrder_CreditAmount` | TField |  | Amount to be credited. Defaulted by the system Validation Rules:Not allowed for input |
| 279 | `PO.CREDIT.CURRENCY` | `PaymentOrder_CreditCurrency` | TField |  | Currency of Credit Account Validation Rules:Defaulted from the credit account as the credit account is a t24 account |
| 280 | `PO.DEBIT.AMOUNT` | `PaymentOrder_DebitAmount` | TField |  | Amount to be debited. Defaulted by the system Validation Rules:Not allowed for input |
| 281 | `PO.BENEFICIARY.TOWN.NAME` | `PaymentOrder_BeneficiaryTownName` | TField |  | Field to capture town name of the beneficiary. |
| 282 | `PO.ORDERING.CUSTOMER.TOWN.NAME` | `PaymentOrder_OrderingCustomerTownName` | TField |  | Field to capture town name of the Ordering Customer. |
| 283 | `PO.ULTIMATE.DEBTOR.TOWN.NAME` | `PaymentOrder_UltimateDebtorTownName` | TField |  | Field to capture town name of the Ultimate Debtor. |
| 284 | `PO.ULTIMATE.CREDITOR.TOWN.NAME` | `PaymentOrder_UltimateCreditorTownName` | TField |  | Field to capture town name of the Ultimate Creditor |
| 285 | `PO.ORDERING.LEI` | `PaymentOrder_OrderingLei` | TField |  | Field to capture Ordering customer legal entity identifier |
| 286 | `PO.BENEFICIARY.LEI` | `PaymentOrder_BeneficiaryLei` | TField |  | Field to capture Beneficiary customer legal entity identifier |
| 287 | `PO.ULTIMATE.DEBTOR.LEI` | `PaymentOrder_UltimateDebtorLei` | TField |  | Field to capture Ultimate debtor legal entity identifier |
| 288 | `PO.ULTIMATE.CREDITOR.LEI` | `PaymentOrder_UltimateCreditorLei` | TField |  | Field to capture Ultimate Creditor legal entity identifier |
| 289 | `PO.EXTENDED.FIELDS` | `PaymentOrder_ExtendedFields` | TField |  | Field to denote to TPH which OE repair screen to be used |
| 290 | `PO.DEBIT.CHARGE.IMPOSED` | `PaymentOrder_DebitChargeImposed` | TField |  | Field indicates to impose the debit side charges on to the payment system. This field has 4 options - ChargeWithAccount, OnlyAccount, Yes, Blank Blank - The charge details will not be imposed in payment system. Yes - The charge details alone will imposed in payment system and charge account will not be imposed. ChargeWithAccount - The charge details along with the charge account will be imposed. OnlyAccount - Only the charge account will be imposed, the other charge details will not be imposed. When charg account is imposed, if the charge account is different from debit main account, funds reservation must be performed only for the transaction amount (against the debit account) even if 'Reserve with Charges' is set to 'Yes'. |
| 291 | `PO.STRUCTURED` | `PaymentOrder_Structured` |  |  |  |
| 292 | `PO.REF.DOC.INF.TP.CD.OR.PROPCD` | `PaymentOrder_RefDocInfTpCdOrPropcd` |  |  |  |
| 293 | `PO.REF.DOC.INF.NR` | `PaymentOrder_RefDocInfNr` |  |  |  |
| 294 | `PO.REF.DOC.AM.CRNOTEAM` | `PaymentOrder_RefDocAmCrnoteam` |  |  |  |
| 295 | `PO.REF.DOC.AM.CRNOTEAMCCY` | `PaymentOrder_RefDocAmCrnoteamccy` |  |  |  |
| 296 | `PO.REF.DOC.AM.REMITTEDAM` | `PaymentOrder_RefDocAmRemittedam` |  |  |  |
| 297 | `PO.REF.DOC.AM.REMITTEDAMCCY` | `PaymentOrder_RefDocAmRemittedamccy` |  |  |  |
| 298 | `PO.CRD.REF.INF.TP.CD.OR.PROPCD` | `PaymentOrder_CrdRefInfTpCdOrPropcd` |  |  |  |
| 299 | `PO.CRD.REF.INF.TP.ISSUER` | `PaymentOrder_CrdRefInfTpIssuer` |  |  |  |
| 300 | `PO.CRD.REF.INF.REF` | `PaymentOrder_CrdRefInfRef` |  |  |  |
| 301 | `PO.CRD.REF.INF.TP.CD.OR.PROPPROP` | `PaymentOrder_CrdRefInfTpCdOrPropprop` |  |  |  |
| 302 | `PO.ADREMITTANCEINF1` | `PaymentOrder_Adremittanceinf1` |  |  |  |
| 303 | `PO.CANCELLATION.STATUS` | `PaymentOrder_CancellationStatus` | TField |  | This field represents the current status of the Recall request. The Values to this field are defined in the EB.LOOKUP table with prefix "RECALL.STATUS". NOINPUT field. The default value will be blank. |
| 304 | `PO.REJECT.REASON.CODE` | `PaymentOrder_RejectReasonCode` | TField |  | This field specifies the ISO reason code or the proprietary reason code for the rejection of the cancellation request. It is a NOINPUT field with a default value of blank. |
| 305 | `PO.REJECT.ADDL.INFO` | `PaymentOrder_RejectAddlInfo` | TField |  | This field specifies the additional information for the rejection of the cancellation request. It is a NOINPUT field with a default value of blank. |
| 306 | `PO.TIME.INDICATION.CODE.TYPE` | `PaymentOrder_TimeIndicationCodeType` |  |  |  |
| 307 | `PO.TIME.INDICATION.CODE.VALUE` | `PaymentOrder_TimeIndicationCodeValue` |  |  |  |
| 308 | `PO.ACCOUNT.TYPE` | `PaymentOrder_AccountType` | TField |  | Type of account. It can have values: C - Client V - Vostro / Loro I - Suspense / Internal PL - Profit and Loss Account |
| 309 | `PO.SETTLEMENT.PRIORITY` | `PaymentOrder_SettlementPriority` | TField |  | Field to define the settlement priority of the message |
| 310 | `PO.BENEFICIARY.DEPARTMENT` | `PaymentOrder_BeneficiaryDepartment` | TField |  | Field to define the department of the Beneficiary. |
| 311 | `PO.BENEFICIARY.SUB.DEPARTMENT` | `PaymentOrder_BeneficiarySubDepartment` | TField |  | Field to define the sub department of the Beneficiary. |
| 312 | `PO.BENEFICIARY.STREET.NAME` | `PaymentOrder_BeneficiaryStreetName` | TField |  | Field to define the sub Street Name of the Beneficiary. |
| 313 | `PO.BENEFICIARY.BUILDING.NUMBER` | `PaymentOrder_BeneficiaryBuildingNumber` | TField |  | Field to define the sub Building Number of the Beneficiary. |
| 314 | `PO.BENEFICIARY.BUILDING.NAME` | `PaymentOrder_BeneficiaryBuildingName` | TField |  | Field to define the sub Building Name of the Beneficiary. |
| 315 | `PO.BENEFICIARY.BUILDING.FLOOR` | `PaymentOrder_BeneficiaryBuildingFloor` | TField |  | Field to define the sub Building Floor of the Beneficiary. |
| 316 | `PO.BENEFICIARY.POST.BOX` | `PaymentOrder_BeneficiaryPostBox` | TField |  | Field to define the sub Post Box Number of the Beneficiary. |
| 317 | `PO.BENEFICIARY.BUILDING.ROOMNO` | `PaymentOrder_BeneficiaryBuildingRoomno` | TField |  | Field to define the sub Building Room Number of the Beneficiary. |
| 318 | `PO.BENEFICIARY.POST.CODE` | `PaymentOrder_BeneficiaryPostCode` | TField |  | Field to define the sub Postal Code of the Beneficiary. |
| 319 | `PO.BENEFICIARY.TOWN.LOCATION` | `PaymentOrder_BeneficiaryTownLocation` | TField |  | Field to define the sub Town location of the Beneficiary. |
| 320 | `PO.BENEFICIARY.DISTRICT.NAME` | `PaymentOrder_BeneficiaryDistrictName` | TField |  | Field to define the sub district name of the Beneficiary. |
| 321 | `PO.BENEFICIARY.CTRY.SUBDIVISION` | `PaymentOrder_BeneficiaryCtrySubdivision` | TField |  | Field to define the sub country subdivision of the Beneficiary. |
| 322 | `PO.IMPOSE.DEBTOR.DETAILS` | `PaymentOrder_ImposeDebtorDetails` | TField |  | Field to define if the debtor details need to be imposed on to the payment message generated in TPH |
| 323 | `PO.ORDERING.DEPARTMENT` | `PaymentOrder_OrderingDepartment` | TField |  | Field to define the department of the Ordering Customer. |
| 324 | `PO.ORDERING.SUB.DEPARTMENT` | `PaymentOrder_OrderingSubDepartment` | TField |  | Field to define the sub department of the Ordering Customer. |
| 325 | `PO.ORDERING.STREET.NAME` | `PaymentOrder_OrderingStreetName` | TField |  | Field to define the sub Street Name of the Ordering Customer. |
| 326 | `PO.ORDERING.BUILDING.NUMBER` | `PaymentOrder_OrderingBuildingNumber` | TField |  | Field to define the sub Building Number of the Ordering Customer. |
| 327 | `PO.ORDERING.BUILDING.NAME` | `PaymentOrder_OrderingBuildingName` | TField |  | Field to define the sub Building Name of the Ordering Customer. |
| 328 | `PO.ORDERING.BUILDING.FLOOR` | `PaymentOrder_OrderingBuildingFloor` | TField |  | Field to define the sub Building Floor of the Ordering Customer. |
| 329 | `PO.ORDERING.POST.BOX` | `PaymentOrder_OrderingPostBox` | TField |  | Field to define the sub Post Box Number of the Ordering Customer. |
| 330 | `PO.ORDERING.BUILDING.ROOMNO` | `PaymentOrder_OrderingBuildingRoomno` | TField |  | Field to define the sub Building Room Number of the Ordering Customer. |
| 331 | `PO.ORDERING.POST.CODE` | `PaymentOrder_OrderingPostCode` | TField |  | Field to define the sub Postal Code of the Ordering Customer. |
| 332 | `PO.ORDERING.TOWN.LOCATION` | `PaymentOrder_OrderingTownLocation` | TField |  | Field to define the sub Town location of the Ordering Customer. |
| 333 | `PO.ORDERING.DISTRICT.NAME` | `PaymentOrder_OrderingDistrictName` | TField |  | Field to define the sub district name of the Ordering Customer. |
| 334 | `PO.ORDERING.COUNTRY.SUBDIVISION` | `PaymentOrder_OrderingCountrySubdivision` | TField |  | Field to define the sub country subdivision of the Ordering Customer. |
| 335 | `PO.INTERMED.BANK.LEI` | `PaymentOrder_IntermedBankLei` | TField |  | Field to define the legal entity identifier of the Intermediary bank1. |
| 336 | `PO.INTERMED.BANK.NAME` | `PaymentOrder_IntermedBankName` | TField |  | Field to define the name of the intermediary bank1 |
| 337 | `PO.INTERMED.POST.CODE` | `PaymentOrder_IntermedPostCode` | TField |  | Field to define the postal code of the intermediary bank1 |
| 338 | `PO.INTERMED.TOWN.NAME` | `PaymentOrder_IntermedTownName` | TField |  | Field to define the town name of intermediary bank1 |
| 339 | `PO.INTERMED2.BIC` | `PaymentOrder_Intermed2Bic` | TField |  | Field to define the BIC of the intermediary bank 2 |
| 340 | `PO.INTERMED2.BANK.CLEARING.CODE` | `PaymentOrder_Intermed2BankClearingCode` | TField |  | Field to define the member id of the intermediary bank 2 |
| 341 | `PO.INTERMED2.BANK.IDENTIFIER` | `PaymentOrder_Intermed2BankIdentifier` | TField |  | Field to define the clearing system if code of the intermediary bank 2 |
| 342 | `PO.INTERMED2.BANK.LEI` | `PaymentOrder_Intermed2BankLei` | TField |  | Field to define the legal entity identifier of the Intermediary bank2. |
| 343 | `PO.INTERMED2.BANK.NAME` | `PaymentOrder_Intermed2BankName` | TField |  | Field to define the name of the intermediary bank2 |
| 344 | `PO.INTERMED2.POST.CODE` | `PaymentOrder_Intermed2PostCode` | TField |  | Field to determine the postal code of the intermediary bank2 |
| 345 | `PO.INTERMED2.TOWN.NAME` | `PaymentOrder_Intermed2TownName` | TField |  | Field to determine the Town Name of the intermediary bank2 |
| 346 | `PO.INTERMED2.BANK.COUNTRY` | `PaymentOrder_Intermed2BankCountry` | TField |  | Field to determine the country of the intermediary bank2 |
| 347 | `PO.INTERMED2.SWIFT.ADDR1` | `PaymentOrder_Intermed2SwiftAddr1` |  |  |  |
| 348 | `PO.INTERMED3.BIC` | `PaymentOrder_Intermed3Bic` | TField |  | Field to define the BIC of the intermediary bank 3 |
| 349 | `PO.INTERMED3.BANK.CLEARING.CODE` | `PaymentOrder_Intermed3BankClearingCode` | TField |  | Field to define the member id of the intermediary bank 3 |
| 350 | `PO.INTERMED3.BANK.IDENTIFIER` | `PaymentOrder_Intermed3BankIdentifier` | TField |  | Field to define the clearing system if code of the intermediary bank 3 |
| 351 | `PO.INTERMED3.BANK.LEI` | `PaymentOrder_Intermed3BankLei` | TField |  | Field to define the legal entity identifier of the Intermediary bank3. |
| 352 | `PO.INTERMED3.BANK.NAME` | `PaymentOrder_Intermed3BankName` | TField |  | Field to define the name of the intermediary bank3 |
| 353 | `PO.INTERMED3.POST.CODE` | `PaymentOrder_Intermed3PostCode` | TField |  | Field to determine the postal code of the intermediary bank3 |
| 354 | `PO.INTERMED3.TOWN.NAME` | `PaymentOrder_Intermed3TownName` | TField |  | Field to determine the Town Name of the intermediary bank3 |
| 355 | `PO.INTERMED3.BANK.COUNTRY` | `PaymentOrder_Intermed3BankCountry` | TField |  | Field to determine the country of the intermediary bank3 |
| 356 | `PO.INTERMED3.SWIFT.ADDR1` | `PaymentOrder_Intermed3SwiftAddr1` |  |  |  |
| 357 | `PO.ACCT.WITH.BANK.LEI` | `PaymentOrder_AcctWithBankLei` | TField |  | Field to determine the legal entity identifier of Beneficiary bank |
| 358 | `PO.ACCT.WITH.BANK.NAME` | `PaymentOrder_AcctWithBankName` | TField |  | Field to determine the Bank Name of Beneficiary bank |
| 359 | `PO.ACCT.WITH.POST.CODE` | `PaymentOrder_AcctWithPostCode` | TField |  | Field to determine the postal code of Beneficiary bank |
| 360 | `PO.ACCT.WITH.TOWN.NAME` | `PaymentOrder_AcctWithTownName` | TField |  | Field to determine the Town name of Beneficiary bank |
| 361 | `PO.ULTIMATE.DEBTOR.DEPARTMENT` | `PaymentOrder_UltimateDebtorDepartment` | TField |  | Field to define the department of the Ultimate Debtor. |
| 362 | `PO.ULTIMATE.DEBTOR.SUB.DEPARTMENT` | `PaymentOrder_UltimateDebtorSubDepartment` | TField |  | Field to define the sub department of the Ultimate Debtor. |
| 363 | `PO.ULTIMATE.DEBTOR.STREET.NAME` | `PaymentOrder_UltimateDebtorStreetName` | TField |  | Field to define the sub Street Name of the Ultimate Debtor. |
| 364 | `PO.ULTIMATE.DEBTOR.BUILDING.NUM` | `PaymentOrder_UltimateDebtorBuildingNum` | TField |  | Field to define the sub Building Number of the Ultimate Debtor. |
| 365 | `PO.ULTIMATE.DEBTOR.BUILDING.NAME` | `PaymentOrder_UltimateDebtorBuildingName` | TField |  | Field to define the sub Building Name of the Ultimate Debtor. |
| 366 | `PO.ULTIMATE.DEBTOR.BUILDING.FLOOR` | `PaymentOrder_UltimateDebtorBuildingFloor` | TField |  | Field to define the sub Building Floor of the Ultimate Debtor. |
| 367 | `PO.ULTIMATE.DEBTOR.POST.BOX` | `PaymentOrder_UltimateDebtorPostBox` | TField |  | Field to define the sub Post Box Number of the Ultimate Debtor. |
| 368 | `PO.ULTIMATE.DB.BUILDING.ROOMNO` | `PaymentOrder_UltimateDbBuildingRoomno` | TField |  | Field to define the sub Post Box Number of the Ultimate Debtor. |
| 369 | `PO.ULTIMATE.DEBTOR.POST.CODE` | `PaymentOrder_UltimateDebtorPostCode` | TField |  | Field to define the sub Postal Code of the Ultimate Debtor. |
| 370 | `PO.ULTIMATE.DEBTOR.TOWN.LOCATION` | `PaymentOrder_UltimateDebtorTownLocation` | TField |  | Field to define the sub Postal Code of the Ultimate Debtor. |
| 371 | `PO.ULTIMATE.DEBTOR.DISTRICT.NAME` | `PaymentOrder_UltimateDebtorDistrictName` | TField |  | Field to define the sub district name of the Ultimate Debtor. |
| 372 | `PO.ULTIMATE.DB.CTRY.SUBDIVISION` | `PaymentOrder_UltimateDbCtrySubdivision` | TField |  | Field to define the sub country subdivision of the Ultimate Debtor. |
| 373 | `PO.ULTIMATE.CREDITOR.DEPARTMENT` | `PaymentOrder_UltimateCreditorDepartment` | TField |  | Field to define the department of the Ultimate Creditor. |
| 374 | `PO.ULTIMATE.CR.SUB.DEPARTMENT` | `PaymentOrder_UltimateCrSubDepartment` | TField |  | Field to define the sub department of the Ultimate Creditor. |
| 375 | `PO.ULTIMATE.CREDITOR.STREET.NAME` | `PaymentOrder_UltimateCreditorStreetName` | TField |  | Field to define the sub department of the Ultimate Creditor. |
| 376 | `PO.ULTIMATE.CREDITOR.BUILDING.NUM` | `PaymentOrder_UltimateCreditorBuildingNum` | TField |  | Field to define the sub Building Number of the Ultimate Creditor. |
| 377 | `PO.ULTIMATE.CR.BUILDING.NAME` | `PaymentOrder_UltimateCrBuildingName` | TField |  |  |
| 378 | `PO.ULTIMATE.CR.BUILDING.FLOOR` | `PaymentOrder_UltimateCrBuildingFloor` | TField |  |  |
| 379 | `PO.ULTIMATE.CREDITOR.POST.BOX` | `PaymentOrder_UltimateCreditorPostBox` | TField |  | Field to define the sub Building Floor of the Ultimate Creditor. |
| 380 | `PO.ULTIMATE.CR.BUILDING.ROOMNO` | `PaymentOrder_UltimateCrBuildingRoomno` | TField |  | Field to define the sub Building Room Number of the Ultimate Creditor. |
| 381 | `PO.ULTIMATE.CREDITOR.POST.CODE` | `PaymentOrder_UltimateCreditorPostCode` | TField |  | Field to define the sub Postal Code of the Ultimate Creditor. |
| 382 | `PO.ULTIMATE.CREDITOR.TOWNLOCATION` | `PaymentOrder_UltimateCreditorTownlocation` | TField |  |  |
| 383 | `PO.ULTIMATE.CREDITOR.DISTRICTNAME` | `PaymentOrder_UltimateCreditorDistrictname` | TField |  |  |
| 384 | `PO.ULTIMATE.CR.CTRY.SUBDIVISION` | `PaymentOrder_UltimateCrCtrySubdivision` | TField |  | Field to define the sub country subdivision of the Ultimate Creditor. |
| 385 | `PO.SNDCBK.BIC` | `PaymentOrder_SndcbkBic` | TField |  | Field to define the BIC of the Senders Correspondent |
| 386 | `PO.SNDCBK.BANK.CLEARING.CODE` | `PaymentOrder_SndcbkBankClearingCode` | TField |  | Field to define the member id of the Senders Correspondent |
| 387 | `PO.SNDCBK.BANK.IDENTIFIER` | `PaymentOrder_SndcbkBankIdentifier` | TField |  | Field to define the clearing system if code of the Senders Correspondent |
| 388 | `PO.SNDCBK.BANK.LEI` | `PaymentOrder_SndcbkBankLei` | TField |  | Field to define the legal entity identifier of the Senders Correspondent |
| 389 | `PO.SNDCBK.BANK.NAME` | `PaymentOrder_SndcbkBankName` | TField |  | Field to define the name of the Senders Correspondent |
| 390 | `PO.SNDCBK.POST.CODE` | `PaymentOrder_SndcbkPostCode` | TField |  | Field to determine the postal code of the Senders Correspondent |
| 391 | `PO.SNDCBK.TOWN.NAME` | `PaymentOrder_SndcbkTownName` | TField |  | Field to determine the Town Name of the Senders Correspondent |
| 392 | `PO.SNDCBK.BANK.COUNTRY` | `PaymentOrder_SndcbkBankCountry` | TField |  | Field to determine the country of the Senders Correspondent |
| 393 | `PO.SNDCBK.SWIFT.ADDR1` | `PaymentOrder_SndcbkSwiftAddr1` |  |  |  |
| 394 | `PO.RCVCBK.BIC` | `PaymentOrder_RcvcbkBic` | TField |  | Field to define the BIC of the Receivers Correspondent |
| 395 | `PO.RCVCBK.BANK.CLEARING.CODE` | `PaymentOrder_RcvcbkBankClearingCode` | TField |  | Field to define the member id of the Receivers Correspondent |
| 396 | `PO.RCVCBK.BANK.IDENTIFIER` | `PaymentOrder_RcvcbkBankIdentifier` | TField |  | Field to define the clearing system if code of the Receivers Correspondent |
| 397 | `PO.RCVCBK.BANK.LEI` | `PaymentOrder_RcvcbkBankLei` | TField |  | Field to define the legal entity identifier of the Receivers Correspondent |
| 398 | `PO.RCVCBK.BANK.NAME` | `PaymentOrder_RcvcbkBankName` | TField |  | Field to define the name of the Receivers Correspondent |
| 399 | `PO.RCVCBK.POST.CODE` | `PaymentOrder_RcvcbkPostCode` | TField |  | Field to determine the postal code of the Receivers Correspondent |
| 400 | `PO.RCVCBK.TOWN.NAME` | `PaymentOrder_RcvcbkTownName` | TField |  | Field to determine the Town Name of the Receivers Correspondent |
| 401 | `PO.RCVCBK.BANK.COUNTRY` | `PaymentOrder_RcvcbkBankCountry` | TField |  | Field to determine the country of the Receivers Correspondent |
| 402 | `PO.RCVCBK.SWIFT.ADDR1` | `PaymentOrder_RcvcbkSwiftAddr1` |  |  |  |
| 403 | `PO.TRMINS.BIC` | `PaymentOrder_TrminsBic` | TField |  | Field to define the BIC of the Third party reimbursement Agent |
| 404 | `PO.TRMINS.BANK.CLEARING.CODE` | `PaymentOrder_TrminsBankClearingCode` | TField |  | Field to define the member id of the Third party reimbursement Agent |
| 405 | `PO.TRMINS.BANK.IDENTIFIER` | `PaymentOrder_TrminsBankIdentifier` | TField |  | Field to define the clearing system if code of the Third party reimbursement Agent |
| 406 | `PO.TRMINS.BANK.LEI` | `PaymentOrder_TrminsBankLei` | TField |  | Field to define the legal entity identifier of the Third party reimbursement Agent |
| 407 | `PO.TRMINS.BANK.NAME` | `PaymentOrder_TrminsBankName` | TField |  | Field to define the name of the Third party reimbursement Agent |
| 408 | `PO.TRMINS.POST.CODE` | `PaymentOrder_TrminsPostCode` | TField |  | Field to determine the postal code of the Third party reimbursement Agent |
| 409 | `PO.TRMINS.TOWN.NAME` | `PaymentOrder_TrminsTownName` | TField |  | Field to determine the Town Name of the Third party reimbursement Agent |
| 410 | `PO.TRMINS.BANK.COUNTRY` | `PaymentOrder_TrminsBankCountry` | TField |  | Field to determine the country of the Third party reimbursement Agent |
| 411 | `PO.TRMINS.SWIFT.ADDR1` | `PaymentOrder_TrminsSwiftAddr1` |  |  |  |
| 412 | `PO.MESSAGE.CONTENT.NAME` | `PaymentOrder_MessageContentName` |  |  |  |
| 413 | `PO.MESSAGE.DATA` | `PaymentOrder_MessageData` |  |  |  |
| 414 | `PO.BENEFICIARY.RESIDENCE.CTRY` | `PaymentOrder_BeneficiaryResidenceCtry` | TField |  | Identifies the residence country of the Beneficiary |
| 415 | `PO.ORDERING.RESIDENCE.CTRY` | `PaymentOrder_OrderingResidenceCtry` | TField |  | Identifies the residence country of the debtor |
| 416 | `PO.ULTIMATE.DEBTOR.RESIDENCE.CTRY` | `PaymentOrder_UltimateDebtorResidenceCtry` | TField |  | Identifies the residence country of the ultimate debtor |
| 417 | `PO.ULTIMATE.CR.RESIDENCE.CTRY` | `PaymentOrder_UltimateCrResidenceCtry` | TField |  |  |
| 418 | `PO.REL.REMINF.IDENTIFICATION` | `PaymentOrder_RelReminfIdentification` | TField |  | Identifies the Related remittance information |
| 419 | `PO.REL.REMINF.METHOD` | `PaymentOrder_RelReminfMethod` |  |  |  |
| 420 | `PO.REL.REMINF.ELECTRONIC.ADDRESS` | `PaymentOrder_RelReminfElectronicAddress` |  |  |  |
| 421 | `PO.REL.REMINF.NAME` | `PaymentOrder_RelReminfName` |  |  |  |
| 422 | `PO.REL.REMINF.DEPARTMENT` | `PaymentOrder_RelReminfDepartment` |  |  |  |
| 423 | `PO.REL.REMINF.SUBDEPARTMENT` | `PaymentOrder_RelReminfSubdepartment` |  |  |  |
| 424 | `PO.REL.REMINF.STREETNAME` | `PaymentOrder_RelReminfStreetname` |  |  |  |
| 425 | `PO.REL.REMINF.BUILDING.NUMBER` | `PaymentOrder_RelReminfBuildingNumber` |  |  |  |
| 426 | `PO.REL.REMINF.BUILDING.NAME` | `PaymentOrder_RelReminfBuildingName` |  |  |  |
| 427 | `PO.REL.REMINF.FLOOR` | `PaymentOrder_RelReminfFloor` |  |  |  |
| 428 | `PO.REL.REMINF.POSTBOX` | `PaymentOrder_RelReminfPostbox` |  |  |  |
| 429 | `PO.REL.REMINF.ROOM` | `PaymentOrder_RelReminfRoom` |  |  |  |
| 430 | `PO.REL.REMINF.POST.CODE` | `PaymentOrder_RelReminfPostCode` |  |  |  |
| 431 | `PO.REL.REMINF.TOWN.NAME` | `PaymentOrder_RelReminfTownName` |  |  |  |
| 432 | `PO.REL.REMINF.TOWN.LOCATION.NAME` | `PaymentOrder_RelReminfTownLocationName` |  |  |  |
| 433 | `PO.REL.REMINF.DISTRICT.NAME` | `PaymentOrder_RelReminfDistrictName` |  |  |  |
| 434 | `PO.REL.REMINF.COUNTRY.SUBDIVISION` | `PaymentOrder_RelReminfCountrySubdivision` |  |  |  |
| 435 | `PO.REL.REMINF.COUNTRY` | `PaymentOrder_RelReminfCountry` |  |  |  |
| 436 | `PO.REL.REMINF.ADDRESSLINE` | `PaymentOrder_RelReminfAddressline` |  |  |  |
| 437 | `PO.ADREMITTANCEINF2` | `PaymentOrder_Adremittanceinf2` |  |  |  |
| 438 | `PO.ADREMITTANCEINF3` | `PaymentOrder_Adremittanceinf3` |  |  |  |
| 439 | `PO.PYMT.INFO.SER.LEVEL.PROP` | `PaymentOrder_PymtInfoSerLevelProp` |  |  |  |
| 440 | `PO.REG.REP.RELATION` | `PaymentOrder_RegRepRelation` |  |  |  |
| 441 | `PO.PARTY.TYPE` | `PaymentOrder_PartyType` |  |  |  |
| 442 | `PO.PARTY.OT.ID.TYPE` | `PaymentOrder_PartyOtIdType` |  |  |  |
| 443 | `PO.PARTY.OT.ID` | `PaymentOrder_PartyOtId` |  |  |  |
| 444 | `PO.PARTY.SCH.CDE` | `PaymentOrder_PartySchCde` |  |  |  |
| 445 | `PO.PARTY.SCHME.PRTY` | `PaymentOrder_PartySchmePrty` |  |  |  |
| 446 | `PO.PARTY.SCH.ISSUR` | `PaymentOrder_PartySchIssur` |  |  |  |
| 447 | `PO.AA.CHARGE.ACCOUNT.TYPE` | `PaymentOrder_AaChargeAccountType` |  |  |  |
| 448 | `PO.AA.CHARGE.AMOUNT` | `PaymentOrder_AaChargeAmount` |  |  |  |
| 449 | `PO.SIM.PRODUCT` | `PaymentOrder_SimProduct` | TField |  |  |
| 450 | `PO.REF.DOC.INF.TP.CD.OR.PROP` | `PaymentOrder_RefDocInfTpCdOrProp` |  |  |  |
| 451 | `PO.CREDITOR.NAME` | `PaymentOrder_CreditorName` | TField |  | Name of the creditor of the payment |
| 452 | `PO.REF.DOC.INF.RELATED.DATE` | `PaymentOrder_RefDocInfRelatedDate` |  |  |  |
| 453 | `PO.FX.CONTRACT.ID` | `PaymentOrder_FxContractId` | TField |  | Contains the reference to the foreign exchange contract utilized for the payment. Must allow input only for cross currency payments If valid FX contract ID is input, API calls will be made to Treasury module to validate/update FX utilisation and to default the customer rate Currently supported only when TPH is embedded with TRANSACT |
| 454 | `PO.EXTERNAL.DEBIT.ACCOUNT` | `PaymentOrder_ExternalDebitAccount` | TField |  | This field is to capture the corresponding account number of the Debit Account as maintained in an external entity's system. Examples of external entity: A bank that holds a Vostro of a TPH bank, a Clearing System that holds an account of a participant bank. |
| 455 | `PO.EXTERNAL.CREDIT.ACCOUNT` | `PaymentOrder_ExternalCreditAccount` | TField |  | This field is to capture the corresponding account number of the Credit Account as maintained in an external entity's system. Examples of external entity: A bank that holds a Vostro of a TPH bank, a Clearing System that holds an account of a participant bank. |
| 456 | `PO.BASE.CURRENCY` | `PaymentOrder_BaseCurrency` | TField |  | Indicates the base currency code. |
| 457 | `PO.BENEFICIARY.PARTY.TAG.OPTION` | `PaymentOrder_BeneficiaryPartyTagOption` | TField |  | If the operator wants to impose the tag option 59F or 59 he can do so by setting this field. The data inputted by the operator will be present in the respective tags of the outgoing message. |
