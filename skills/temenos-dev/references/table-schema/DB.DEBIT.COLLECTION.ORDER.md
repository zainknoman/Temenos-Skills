# DB.DEBIT.COLLECTION.ORDER — Table Schema

> Source: `INSERTS/I_F.DB.DEBIT.COLLECTION.ORDER` in `DB_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DB.DCO.COLLECTION.PRODUCT.GROUP` | `DbDebitCollectionOrder_CollectionProductGroup` | TField | Yes | Mandatory field Validation Rules: Must be a valid product from DEBIT.COLLECTION.PRODUCT application |
| 2 | `DB.DCO.ORDERING.COMPANY` | `DbDebitCollectionOrder_OrderingCompany` | TField |  | Company from which the transaction is done or debit account's customer's company No Input field |
| 3 | `DB.DCO.CREDIT.ACCOUNT` | `DbDebitCollectionOrder_CreditAccount` | TField | Yes | Account Number of the Creditor Validation Rules: 1. Mandatory Field 2. Valid T24 Account |
| 4 | `DB.DCO.CREDIT.CCY` | `DbDebitCollectionOrder_CreditCcy` | TField |  | Account Number of the Creditor Validation Rules: Can be manually input or it will be defaulted from the credit account in case of T24 accounts |
| 5 | `DB.DCO.CREDITOR.NAME` | `DbDebitCollectionOrder_CreditorName` | TField |  |  |
| 6 | `DB.DCO.COLLECTION.CURRENCY` | `DbDebitCollectionOrder_CollectionCurrency` | TField | Yes | Currency of the Collection Amount Validation Rules: 1. Mandatory Field 2. Must be a valid Currency in the field ALLOWED.PAYMENT.CCY in DEBIT.COLLECTION.PRODUCT |
| 7 | `DB.DCO.COLLECTION.AMOUNT` | `DbDebitCollectionOrder_CollectionAmount` | TField | Yes | Amount to be collected i.e transaction amount. Validation Rules: 1. Mandatory Field 2. Must be a valid Amount 3. Must be greater than 0. |
| 8 | `DB.DCO.REQUESTED.COLLECTION.DATE` | `DbDebitCollectionOrder_RequestedCollectionDate` | TField | Yes | Date at which the creditor requests that the amount of money is to be collected from the debtor. Validation Rules: 1. Mandatory Field 2. Can be manually input or defaulted 3.If not manually input, defaulted to TODAY's date 4.If past dated value is entered, system will auto-update it to Current business date after the collection request is approved. 5.Error must be thrown in following cases:i. If Date is greater than today and ALLOW.FUTURE.DATE is set to NO in DEBIT.COLLECTION.PRODUCT |
| 9 | `DB.DCO.LOCAL.INSTR.PROP` | `DbDebitCollectionOrder_LocalInstrProp` | TField |  | This field is used to specify a local instrument, local clearing option and/or further qualify the service or service level, in a proprietary format. |
| 10 | `DB.DCO.PURPOSE.PROPRIETARY` | `DbDebitCollectionOrder_PurposeProprietary` | TField |  | Purpose code of the payment in a proprietary format |
| 11 | `DB.DCO.CATEGORYPURP.PRTY` | `DbDebitCollectionOrder_CategorypurpPrty` | TField |  | Specifies the high level purpose of the instruction based on a set of pre-defined categories in a proprietary format |
| 12 | `DB.DCO.MANDATE.IDENTIFICATION` | `DbDebitCollectionOrder_MandateIdentification` | TField |  | Indicates the unique mandate identification. Validation Rules: 35 alphabetic characters. |
| 13 | `DB.DCO.DEBTOR.NAME` | `DbDebitCollectionOrder_DebtorName` | TField |  | Debtor Name |
| 14 | `DB.DCO.DEBTOR.ACCOUNT` | `DbDebitCollectionOrder_DebtorAccount` | TField |  | Debtor Account Number |
| 15 | `DB.DCO.DEBTOR.BANK.CLEARING.CODE` | `DbDebitCollectionOrder_DebtorBankClearingCode` | TField |  | Clearing Code of the Debtor Agent |
| 16 | `DB.DCO.PRIORITY` | `DbDebitCollectionOrder_Priority` | TField |  | Identifies the Payment Message Priority and based on this value priority code is set in the payment engine. IF MessagePriority is empty or between 1 and 5, then PriorityCode is 'N' IF MessagePriority is between 6 and 9, then PriorityCode is 'U' Possible values:1 to 9 |
| 17 | `DB.DCO.ORIGINAL.REQ.COLLECTION.DATE` | `DbDebitCollectionOrder_OriginalReqCollectionDate` | TField |  | Stores Requested Collection Date as received in collection initiation request. No Change field. |
| 18 | `DB.DCO.COLLECTION.EXECUTION.TIME` | `DbDebitCollectionOrder_CollectionExecutionTime` | TField |  | The time at which collection is executed Validation Rules: NOINPUT field |
| 19 | `DB.DCO.COLLECTION.EXECUTION.DATE.TIME` | `DbDebitCollectionOrder_CollectionExecutionDateTime` |  |  |  |
| 20 | `DB.DCO.PAYMENT.SYSTEM` | `DbDebitCollectionOrder_PaymentSystem` | TField |  | Indicates the payment system through which the requests/transactions initiated by the payment order is processed. Valid Values: 1. TPH - Requests are processed by TPS Validation Rules: - No input field, updated while authorising the payment order record. |
| 21 | `DB.DCO.PAYMENT.SYSTEM.ID` | `DbDebitCollectionOrder_PaymentSystemId` | TField | No | Reference sent from payment system Validation Rules:Free Text of 35 characters. Optional. No validation |
| 22 | `DB.DCO.PAYMENT.SYSTEM.STATUS` | `DbDebitCollectionOrder_PaymentSystemStatus` | TField |  | Current status of the order in payment system. Values to the field are defined in the EB.LOOKUP table with prefix "PAYMENT.STATUS". Validation Rules: 1. Standard T24 free text field. 2. Field no-input and cleared by copy function. 3. Can be updated only through other applications. |
| 23 | `DB.DCO.PAYMENT.STATUS.ADD.INFO` | `DbDebitCollectionOrder_PaymentStatusAddInfo` | TField |  | Field to record additional status information or narratives which describes the current status of the payment order in the payment system. This value will be updated by the payment system which has processed the contract. Validation Rules: 1. Standard T24 free text field. 2. Field no-input and cleared by copy function. 3. Can be updated only through other applications. |
| 24 | `DB.DCO.PAYMENT.STATUS.UPDATE.DATE` | `DbDebitCollectionOrder_PaymentStatusUpdateDate` | TField |  | Date and time when the payment system status as last updated Validation Rules:NOINPUT field. Updated by system when PAYMENT.SYSTEM.STATUS field is updated |
| 25 | `DB.DCO.CURRENT.STATE` | `DbDebitCollectionOrder_CurrentState` | TField |  | Current state of the payment order Validation Rules:NOINPUT field. Will be updated by StateMachine |
| 26 | `DB.DCO.STATE.HIST` | `DbDebitCollectionOrder_StateHist` |  |  |  |
| 27 | `DB.DCO.ORDER.INITIATION.TYPE` | `DbDebitCollectionOrder_OrderInitiationType` | TField |  |  |
| 28 | `DB.DCO.STATUS.REASON.CODE` | `DbDebitCollectionOrder_StatusReasonCode` | TField |  |  |
| 29 | `DB.DCO.INTERNAL.STATUS` | `DbDebitCollectionOrder_InternalStatus` | TField |  | Status of the order Validation Rules:RETURN_REJECT_CANCEL_ERROR |
| 30 | `DB.DCO.SUBMIT.ORDER` | `DbDebitCollectionOrder_SubmitOrder` | TField |  | Field to trigger Awaiting Ext Submit state Pssible Values: YES NO |
| 31 | `DB.DCO.CONTEXT.NAME` | `DbDebitCollectionOrder_ContextName` |  |  |  |
| 32 | `DB.DCO.CONTEXT.VALUE` | `DbDebitCollectionOrder_ContextValue` |  |  |  |
| 33 | `DB.DCO.PAYMENT.COMPLETE` | `DbDebitCollectionOrder_PaymentComplete` | TField |  | Filed to indicate if the collection order processing is complete. This is updated by the payment system through which the collection order is processed. Once this flag is set, the current state of the complete order is moved to Complete. Validation Rules: 1. Standard T24 flag field. 2. Field no-input and cleared by copy function. 3. Can be updated only through other applications. |
| 34 | `DB.DCO.ADDITIONAL.INFO` | `DbDebitCollectionOrder_AdditionalInfo` |  |  |  |
| 35 | `DB.DCO.DEBTOR.MOBILE.NUMBER` | `DbDebitCollectionOrder_DebtorMobileNumber` | TField |  | Collection of information that identifies a mobile number, as defined by telecom services. |
| 36 | `DB.DCO.DEBTOR.POSTAL.ADDR.LINE` | `DbDebitCollectionOrder_DebtorPostalAddrLine` |  |  |  |
| 37 | `DB.DCO.DEBTOR.POSTAL.ADDR.TYPE` | `DbDebitCollectionOrder_DebtorPostalAddrType` | TField |  | Debtor's address type Validation Rules: Possible values: Postal, PO Box, Residential, Business, Mail To, Delivery To |
| 38 | `DB.DCO.DEBTOR.ISSUR` | `DbDebitCollectionOrder_DebtorIssur` | TField |  | Holds the Id of the Issuer of Debtor Other ID |
| 39 | `DB.DCO.DEBTOR.SCH.NM.PRTY` | `DbDebitCollectionOrder_DebtorSchNmPrty` | TField |  | The proprietary code of the scheme/account type which issued the identifier for the Debtor |
| 40 | `DB.DCO.DEBTOR.SCH.NM.CDE` | `DbDebitCollectionOrder_DebtorSchNmCde` | TField |  | The code of the scheme which issued the identifier for the Debtor It will indicate what is captured in the Debtor Other Identifier - Social Security Number, Tax Identification Number, Passport Number, Clearing Id |
| 41 | `DB.DCO.DEBTOR.OT.ID` | `DbDebitCollectionOrder_DebtorOtId` | TField |  | Holds other identifications such as Social Security Number, a Tax Identification Number, Passport Number, a Clearing Id ,etc., of the Debtor |
| 42 | `DB.DCO.DEBTOR.OT.ID.TYPE` | `DbDebitCollectionOrder_DebtorOtIdType` | TField | No | Debtor Other Id Type identifies if the Debtor is an Organisation or an Individual Validation Rules: Optional Possible values: None, Organisation, Private |
| 43 | `DB.DCO.DEBTOR.LEI` | `DbDebitCollectionOrder_DebtorLei` | TField |  | Field to capture debtor's legal entity identifier |
| 44 | `DB.DCO.DEBTOR.BIC` | `DbDebitCollectionOrder_DebtorBic` | TField |  | BIC code of Debtor of the payment |
| 45 | `DB.DCO.CREDITOR.ACCT.SCH.PRTY` | `DbDebitCollectionOrder_CreditorAcctSchPrty` | TField |  | The proprietary code of the scheme which issued the identifier for the Creditor. |
| 46 | `DB.DCO.CREDITOR.BANK.CLEARING.CODE` | `DbDebitCollectionOrder_CreditorBankClearingCode` | TField |  | Clearing Code of the Creditor Agent. |
| 47 | `DB.DCO.CREDITOR.AGENT.BIC` | `DbDebitCollectionOrder_CreditorAgentBic` | TField |  | BIC code of creditor agent of the payment. |
| 48 | `DB.DCO.CREDITOR.AGENT.NAME` | `DbDebitCollectionOrder_CreditorAgentName` | TField |  | Name of the creditor agent of payment. |
| 49 | `DB.DCO.CREDITOR.EMAIL.ADR` | `DbDebitCollectionOrder_CreditorEmailAdr` | TField |  | Address for electronic mail of the Creditor. |
| 50 | `DB.DCO.CREDITOR.MOBILE.NUMBER` | `DbDebitCollectionOrder_CreditorMobileNumber` | TField |  | Collection of information that identifies a mobile number, as defined by telecom services. |
| 51 | `DB.DCO.CREDITOR.POSTAL.ADDR.LINE` | `DbDebitCollectionOrder_CreditorPostalAddrLine` |  |  |  |
| 52 | `DB.DCO.CREDITOR.POSTAL.ADDR.TYPE` | `DbDebitCollectionOrder_CreditorPostalAddrType` | TField |  | Creditor's address type Validation Rules: Possible values: Postal, PO Box, Residential, Business, Mail To, Delivery To |
| 53 | `DB.DCO.CREDITOR.ISSUR` | `DbDebitCollectionOrder_CreditorIssur` | TField |  | Holds the Id of the Issuer of Creditor Other ID |
| 54 | `DB.DCO.CREDITOR.SCH.NM.PRTY` | `DbDebitCollectionOrder_CreditorSchNmPrty` | TField |  | The proprietary code of the scheme which issued the identifier for the Creditor |
| 55 | `DB.DCO.CREDITOR.SCH.NM.CDE` | `DbDebitCollectionOrder_CreditorSchNmCde` | TField |  | The code of the scheme which issued the identifier for the Creditor It will indicate what is captured in the Creditor Other Identifier - Social Security Number, Tax Identification Number, Passport Number, Clearing Id |
| 56 | `DB.DCO.CREDITOR.OT.ID` | `DbDebitCollectionOrder_CreditorOtId` | TField |  | Holds other identifications such as could be a Social Security Number, a Tax Identification Number, Passport Number, a Clearing Id ,etc., of the Creditor |
| 57 | `DB.DCO.CREDITOR.OT.ID.TYPE` | `DbDebitCollectionOrder_CreditorOtIdType` | TField | No | Creditor Other Id Type identifies if the Creditor is an Organisation or an Individual Validation Rules: Optional Possible values: None, Organisation, Private |
| 58 | `DB.DCO.CREDITOR.LEI` | `DbDebitCollectionOrder_CreditorLei` | TField |  | Field to capture creditor's legal entity identifier |
| 59 | `DB.DCO.CREDITOR.BIC` | `DbDebitCollectionOrder_CreditorBic` | TField |  | BIC code of Creditor of the payment |
| 60 | `DB.DCO.LOCAL.INSTRUMENT.CD` | `DbDebitCollectionOrder_LocalInstrumentCd` | TField |  | Local Instrument code of the payment. Validation Rules: Valid codes from DB.ISO.EXTERNAL.CODE >> LclInstrmCd record. |
| 61 | `DB.DCO.PAYMENT.CATEGORY` | `DbDebitCollectionOrder_PaymentCategory` | TField |  | Category purpose code of the payment. Validation Rules: Valid codes from DB.ISO.EXTERNAL.CODE >> CtgyPurpCd record. |
| 62 | `DB.DCO.PAYMENT.PURPOSE` | `DbDebitCollectionOrder_PaymentPurpose` | TField |  | Purpose code of the payment.Specifies underlying reason for the payment transaction. Validation Rules: Valid codes from DB.ISO.EXTERNAL.CODE >> PurpCd record. |
| 63 | `DB.DCO.LOCAL.REF` | `DbDebitCollectionOrder_LocalRef` |  |  |  |
| 64 | `DB.DCO.OVERRIDE` | `DbDebitCollectionOrder_Override` |  |  |  |
| 65 | `DB.DCO.RECORD.STATUS` | `DbDebitCollectionOrder_RecordStatus` | String |  |  |
| 66 | `DB.DCO.CURR.NO` | `DbDebitCollectionOrder_CurrNo` | String |  |  |
| 67 | `DB.DCO.INPUTTER` | `DbDebitCollectionOrder_Inputter` |  |  |  |
| 68 | `DB.DCO.DATE.TIME` | `DbDebitCollectionOrder_DateTime` |  |  |  |
| 69 | `DB.DCO.AUTHORISER` | `DbDebitCollectionOrder_Authoriser` | String |  |  |
| 70 | `DB.DCO.CO.CODE` | `DbDebitCollectionOrder_CoCode` | String |  |  |
| 71 | `DB.DCO.DEPT.CODE` | `DbDebitCollectionOrder_DeptCode` | String |  |  |
| 72 | `DB.DCO.AUDITOR.CODE` | `DbDebitCollectionOrder_AuditorCode` | String |  |  |
| 73 | `DB.DCO.AUDIT.DATE.TIME` | `DbDebitCollectionOrder_AuditDateTime` | String |  |  |
| 74 | `DB.DCO.DEBTOR.EMAIL.ADR` | `DbDebitCollectionOrder_DebtorEmailAdr` | TField |  | Address for electronic mail of the Debtor. |
| 75 | `DB.DCO.DEBTOR.AGENT.BIC` | `DbDebitCollectionOrder_DebtorAgentBic` | TField |  | BIC code of debtor agent of the payment. |
| 76 | `DB.DCO.DEBTOR.ACCT.SCH.PRTY` | `DbDebitCollectionOrder_DebtorAcctSchPrty` | TField |  | The proprietary code of the scheme which issued the identifier for the Debtor. |
| 77 | `DB.DCO.CHARGE.BEARER` | `DbDebitCollectionOrder_ChargeBearer` | TField |  | Bearer of the charges of the order Validation Rules: 1. Value can be manually selected or defaulted 2. If not manually input, the value is defaulted from the DEFAULT.CHARGE.OPTION field of DB.DEBIT.COLLECTION.PRODUCT 3. The field is validated as follows: i. For the DB.DEBIT.COLLECTION.PRODUCT, the ALLOWED.CHARGE.OPTIONS are obtained ii. The value defined in this field, is checked with the allowed charges iii. If it is not present, then an override is raised |
| 78 | `DB.DCO.INSTRUCTION.ID.REF` | `DbDebitCollectionOrder_InstructionIdRef` | TField | No | Optional No validation |
| 79 | `DB.DCO.END.TO.END.REFERENCE` | `DbDebitCollectionOrder_EndToEndReference` | TField | No | Optional No validation |
| 80 | `DB.DCO.REMITTANCE.INF.USTRD` | `DbDebitCollectionOrder_RemittanceInfUstrd` |  |  |  |
| 81 | `DB.DCO.CLEARING.CHANNEL` | `DbDebitCollectionOrder_ClearingChannel` | TField |  | Clearing channel through which the db.debit.colllection.order is routed. Validation Rules: Only allow values defined in Clearing channel multivalue field in DB.DEBIT.COLLECTION.PRODUCT.Else,override is raised. |
| 82 | `DB.DCO.REJECT.REASON.CODE` | `DbDebitCollectionOrder_RejectReasonCode` | TField |  |  |
| 83 | `DB.DCO.REJECT.ADDL.INFO` | `DbDebitCollectionOrder_RejectAddlInfo` | TField |  |  |
