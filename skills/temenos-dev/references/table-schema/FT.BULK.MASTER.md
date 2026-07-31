# FT.BULK.MASTER — Table Schema

> Source: `INSERTS/I_F.FT.BULK.MASTER` in `BU_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FT.BLK.MAS.DESCRIPTION` | `FtBulkMaster_Description` |  |  |  |
| 2 | `FT.BLK.MAS.BULK.TYPE` | `FtBulkMaster_BulkType` | TField | Yes | The ID given here is linked to the FT.BULK.UPDATE.TYPE table. The details from FT.BULK.UPDATE.TYPE table will be used while payments are made. Validation Rules: Not a mandatory field. Will be defaulted with an ID as SYSTEM which is expected to exist in the FT.BULK.UPDATE.TYPE table. |
| 3 | `FT.BLK.MAS.DEBIT.CREDIT` | `FtBulkMaster_DebitCredit` | TField | Yes | Indicates whether the Bulk processing is for Credit or Debit Payments. Validation Rules: Mandatory field. DEBIT or CREDIT are the allowed values. |
| 4 | `FT.BLK.MAS.SINGLE.MULTI` | `FtBulkMaster_SingleMulti` | TField | Yes | Whether the ACTIVE.ACCOUNT account should receive single or multiple payments. Validation Rules: Not a Mandatory field. NOCHANGE field. If inputted SINGLE or MULTI are the allowed values. Will be defaulted from FT.BULK.UPDATE.TYPE. |
| 5 | `FT.BLK.MAS.CUSTOMER` | `FtBulkMaster_Customer` | TField | Yes | Refers the Customer of the ACTIVE.ACCOUNT. It should be same as the customer of ACTIVE.ACCOUNT. Validation Rules: Not a Mandatory field. NOCHANGE field. Should be a valid customer in the CUSTOMER table. |
| 6 | `FT.BLK.MAS.ACTIVE.ACCOUNT` | `FtBulkMaster_ActiveAccount` | TField | Yes | Main Account that will receive Credit / Debit thru Bulk Processing. It should be the Account owned by the Customer specified in the Bulk. Account should be in the Currency specified in the bulk processing. Validation Rules: Mandatory field. Should be a valid T24 ACCOUNT. Field Not Mandatory when DEBIT.ACCOUNT.IBAN/DEBIT.ACCOUNT.PL is entered |
| 7 | `FT.BLK.MAS.CURRENCY` | `FtBulkMaster_Currency` | TField | Yes | Currency on which the BULK payment process will happen. Validation Rules: Not a mandatory field. NOCHANGE field. When DEBIT.CREDIT is set to DEBIT, the currency given should exist in the DD.PARAMETER linked in the FT.BULK.UPDATE.TYPE. |
| 8 | `FT.BLK.MAS.WASH.ACCOUNT` | `FtBulkMaster_WashAccount` | TField | Yes | Intermediate Account which will be used to hold the Funds if the Bulk processing is set to receive only single Debit / Credit. Validation Rules: Should belong to the CUSTOMER defined. Should be a Valid T24 account. Mandatory when SINGLE.MULTI is set to SINGLE. Should be same as ACTIVE.ACCOUNT when MODE.OF.TRANSFER is PAYMENT |
| 9 | `FT.BLK.MAS.ERROR.ACCOUNT` | `FtBulkMaster_ErrorAccount` | TField |  | The account that can be used instead of ACTIVE.ACCOUNT when there is problem during payment process. But it is reserved for future use. Validation Rules: No input field. |
| 10 | `FT.BLK.MAS.MODE.OF.TRANSFER` | `FtBulkMaster_ModeOfTransfer` | TField |  | To indicate the mode of transfer to be used during the payment process. But it is reserved for future use. Validation Rules: No input field. |
| 11 | `FT.BLK.MAS.PROCESSING.DATE` | `FtBulkMaster_ProcessingDate` | TField | Yes | Date on which Bulk upload is taken for Processing. For Debit Bulk Upload it should be Greater than Today. For Credit Bulk Uploads it can be Today or future date. Validation Rules: Standard date format. Not a mandatory field. Will be defaulted as TODAY + PROCESSING.DAYS given in FT.BULK.UPDATE.TYPE. |
| 12 | `FT.BLK.MAS.PAYMENT.VALUE.DATE` | `FtBulkMaster_PaymentValueDate` | TField | Yes | Date on which the payment will be made. Validation Rules: Standard date format. Mandatory field for MODE.OF.TRANSFER other than PAYMENT |
| 13 | `FT.BLK.MAS.CLEARING.DATE` | `FtBulkMaster_ClearingDate` | TField | Yes | Date from which the payment is expected. Used only for Credit payments to specify Payment exposure date. Validation Rules: Standard date format. Not a Mandatory field. If inputted cannot be less than PAYMENT.VALUE.DATE. |
| 14 | `FT.BLK.MAS.UPLOAD.REFERENCE` | `FtBulkMaster_UploadReference` | TField | Yes | Hold the reference details if the Bulk is uploaded thru Generic upload. Validation Rules: Not a Mandatory field. Text upto 90 characters of type A can be given. Will be blank when MASTER is created manually. |
| 15 | `FT.BLK.MAS.DEBIT.REFERENCE` | `FtBulkMaster_DebitReference` | TField | Yes | Reference details for a Debit Entry in the case of debit payments. This can be overridden with bulk item reference. Validation Rules: Not a Mandatory field. Text upto 35 characters of type A can be given. |
| 16 | `FT.BLK.MAS.CREDIT.REFERENCE` | `FtBulkMaster_CreditReference` | TField | Yes | Reference details for a Credit Entry in the case of debit payments. Validation Rules: Not a Mandatory field. Text upto 35 characters of type A can be given. |
| 17 | `FT.BLK.MAS.SIGNATORY` | `FtBulkMaster_Signatory` |  |  |  |
| 18 | `FT.BLK.MAS.STATUS` | `FtBulkMaster_Status` | TField |  | The valid status for the MASTER are CREATED, REJECTED, ERROR, READY, PROCESSING and PROCESSED. Validation Rules: Values allowed for user input: CREATED - When the MASTER is created newly. REJECTED - To reject a payment System updated status: READY - After the Validation of both MASTER and FT.BULK.ITEM or PAYEMENT.ORDER records. PROCESSING - When the MASTER is taken for payments process. PROCESSED - When all the FT.BULK.ITEM payment process is over. ERROR - When validation or payment is unsuccessful. Below STATUS are used only when the MODE.OF.TRANSFER is PAYMENT Values allowed for user input: PENDING - Intermediate state for Payment. Can be moved to PENDING only from CREATED status CANCELLED - Cancellation of Bulk Master. System updated status: WAITFUNDS - Awaiting Funds as reservation does not have sufficient funds to reserve WAITACK - Waiting Acknowledgement. When Master with PO items is taken for Process COMPLETED - When All the PO items are completed DISCARDED - When the Cancellation Process is Approved WAITEXEC - When the READY Status Master is Approved WAREHOUSED - When the Status is Warehoused CANCELWAREHOUSE - When the Status is Cancel Warehoused |
| 19 | `FT.BLK.MAS.REJECTION.REASON` | `FtBulkMaster_RejectionReason` |  |  |  |
| 20 | `FT.BLK.MAS.REJECTED.BY` | `FtBulkMaster_RejectedBy` |  |  |  |
| 21 | `FT.BLK.MAS.SOURCE` | `FtBulkMaster_Source` | TField |  | It will be updated as UPLOAD when the UPLOAD.REFERENCE field is not null otherwise it will be updated as MANUAL. This is to identify whether the MASTER is MANUAL or UPLOAD one. Validation Rules: No input field. UPLOAD or MANUAL or TCIB are the updated values. |
| 22 | `FT.BLK.MAS.RESERVED.11` | `FtBulkMaster_Reserved11` | TField |  |  |
| 23 | `FT.BLK.MAS.TOTAL.AMOUNT` | `FtBulkMaster_TotalAmount` | TField |  | Sum of all AMOUNT of the FT.BULK.ITEM records under this MASTER. Validation Rules: No input field. Numeric character. |
| 24 | `FT.BLK.MAS.AMT.TO.BE.UPLOADED` | `FtBulkMaster_AmtToBeUploaded` | TField | Yes | Applicable only for UPLOAD type of Bulk. Holds the Total amount uploaded which can be verified with Actual upload amount. Validation Rules: Not a mandatory field. Standard amount format. |
| 25 | `FT.BLK.MAS.ITEMS.UPLOADED` | `FtBulkMaster_ItemsUploaded` | TField |  | This is the count of FT.BULK.ITEM records that are uploaded. Validation Rules: No input field. Numeric character. |
| 26 | `FT.BLK.MAS.TOT.VALUE.UPLOADED` | `FtBulkMaster_TotValueUploaded` | TField |  | This is sum of all AMOUNT in FT.BULK.ITEM records that are uploaded. Validation Rules: No input field. Numeric character. |
| 27 | `FT.BLK.MAS.ITEMS.STATUS.ERR` | `FtBulkMaster_ItemsStatusErr` | TField |  | This is the count of FT.BULK.ITEM records updated as ERROR. Validation Rules: No input field. Numeric character. |
| 28 | `FT.BLK.MAS.VALUE.ITEMS.ERR` | `FtBulkMaster_ValueItemsErr` | TField |  | This is sum of all AMOUNT in FT.BULK.ITEM records that are in ERROR status. Validation Rules: No input field. Numeric character. |
| 29 | `FT.BLK.MAS.ITEMS.REJECTED` | `FtBulkMaster_ItemsRejected` | TField |  | This is the count of FT.BULK.ITEM records with STATUS as REJECTED. Validation Rules: No input field. Numeric character. |
| 30 | `FT.BLK.MAS.VAL.ITEMS.REJECTED` | `FtBulkMaster_ValItemsRejected` | TField |  | This is sum of all AMOUNT in FT.BULK.ITEM records that are in REJECTED status. Validation Rules: No input field. Numeric character. |
| 31 | `FT.BLK.MAS.MANUAL.ITEMS` | `FtBulkMaster_ManualItems` | TField |  | This is the count of FT.BULK.ITEM records that are manually inputted. Validation Rules: No input field. Numeric character. |
| 32 | `FT.BLK.MAS.VALUE.MANUAL.ITEMS` | `FtBulkMaster_ValueManualItems` | TField |  | This is sum of all AMOUNT in FT.BULK.ITEM records that are in uploaded manually. Validation Rules: No input field. Numeric character. |
| 33 | `FT.BLK.MAS.PAYMENT.ID` | `FtBulkMaster_PaymentId` | TField |  | This stores the id of the FT when the bulk processing type is Single ( the FT which is raised for the single side, for the total bulk amount ) |
| 34 | `FT.BLK.MAS.TOT.ITEM.TO.BE.UPLOADED` | `FtBulkMaster_TotItemToBeUploaded` | TField |  | User can enter the total number of Items that will be uploaded for the Master Validation Rules: Numeric field. Input allowed only when the SOURCE is UPLOAD/TCIB |
| 35 | `FT.BLK.MAS.ORDERING.CUSTOMER.BIC` | `FtBulkMaster_OrderingCustomerBic` | TField |  | BIC of the Ordering customer |
| 36 | `FT.BLK.MAS.ORDERING.CUSTOMER.NAME` | `FtBulkMaster_OrderingCustomerName` | TField |  | Ordering customer name |
| 37 | `FT.BLK.MAS.ORDERING.POST.ADDRESS.TYPE` | `FtBulkMaster_OrderingPostAddressType` | TField |  | Ordering customer's address type |
| 38 | `FT.BLK.MAS.LOCAL.REF` | `FtBulkMaster_LocalRef` |  |  |  |
| 39 | `FT.BLK.MAS.ORDERING.POST.SWIFT.ADDR` | `FtBulkMaster_OrderingPostSwiftAddr` |  |  |  |
| 40 | `FT.BLK.MAS.ORDERING.POST.ADDR.LINE` | `FtBulkMaster_OrderingPostAddrLine` |  |  |  |
| 41 | `FT.BLK.MAS.ORDERING.PORTFOLIO` | `FtBulkMaster_OrderingPortfolio` | TField |  | Debit portfolio id Validation Rules: Valid SEC.ACC.MASTER record Id |
| 42 | `FT.BLK.MAS.DEBIT.ACCOUNT.IBAN` | `FtBulkMaster_DebitAccountIban` | TField |  | IBAN of the active account Validation Rules: Can be manually input or defaulted If manually input, must be a valid IBAN number for the active account IBAN should be a valid T24 IBAN If not manually defined, then will be populated based on the active account If IBAN is defined, but ACTIVE.ACCOUNT is not defined, then the active account number will be defaulted If IBAN is defined, but ORDERING.CUSTOMER.BIC is not defined, then BIC will be derived from IBAN and populated If ORDERING.CUSTOMER.BIC and IBAN are defined, then check must be done to ensure that the IBAN is valid for the BIC defined |
| 43 | `FT.BLK.MAS.DEBIT.ACCOUNT.PL` | `FtBulkMaster_DebitAccountPl` | TField |  | PL category to be debited Validation Rules: Can be manually input Must be a valid PL category Allowed only when ACTIVE.ACCOUNT and DEBIT.ACCOUNT.IBAN are not defined |
| 44 | `FT.BLK.MAS.DEBTOR.AGENT.NAME` | `FtBulkMaster_DebtorAgentName` | TField |  | Name of the debtor agent of payment. |
| 45 | `FT.BLK.MAS.DEBTOR.AGENT.BIC` | `FtBulkMaster_DebtorAgentBic` | TField |  | BIC code of Debtor Agent of payment. |
| 46 | `FT.BLK.MAS.DEBTOR.AGENT.ADDR.TYPE` | `FtBulkMaster_DebtorAgentAddrType` | TField |  | Address type to be used for the Debtor Agent of payment. |
| 47 | `FT.BLK.MAS.DEBTOR.AGENT.ADDR.LINE` | `FtBulkMaster_DebtorAgentAddrLine` |  |  |  |
| 48 | `FT.BLK.MAS.DEBTOR.AGENT.CLEARING.CODE` | `FtBulkMaster_DebtorAgentClearingCode` | TField | No | Clearing code or sort code of the Debtor Agent. Validation Rules: Optional field. |
| 49 | `FT.BLK.MAS.ERROR.DETAILS` | `FtBulkMaster_ErrorDetails` |  |  |  |
| 50 | `FT.BLK.MAS.OVERRIDE` | `FtBulkMaster_Override` |  |  |  |
| 51 | `FT.BLK.MAS.RECORD.STATUS` | `FtBulkMaster_RecordStatus` | String |  |  |
| 52 | `FT.BLK.MAS.CURR.NO` | `FtBulkMaster_CurrNo` | String |  |  |
| 53 | `FT.BLK.MAS.INPUTTER` | `FtBulkMaster_Inputter` |  |  |  |
| 54 | `FT.BLK.MAS.DATE.TIME` | `FtBulkMaster_DateTime` |  |  |  |
| 55 | `FT.BLK.MAS.AUTHORISER` | `FtBulkMaster_Authoriser` | String |  |  |
| 56 | `FT.BLK.MAS.CO.CODE` | `FtBulkMaster_CoCode` | String |  |  |
| 57 | `FT.BLK.MAS.DEPT.CODE` | `FtBulkMaster_DeptCode` | String |  |  |
| 58 | `FT.BLK.MAS.AUDITOR.CODE` | `FtBulkMaster_AuditorCode` | String |  |  |
| 59 | `FT.BLK.MAS.AUDIT.DATE.TIME` | `FtBulkMaster_AuditDateTime` | String |  |  |
| 60 | `FT.BLK.MAS.REJECT.REMARK` | `FtBulkMaster_RejectRemark` |  |  |  |
| 61 | `FT.BLK.MAS.REJECT.DATE.TIME` | `FtBulkMaster_RejectDateTime` |  |  |  |
| 62 | `FT.BLK.MAS.REJECT.RESPONSE` | `FtBulkMaster_RejectResponse` |  |  |  |
| 63 | `FT.BLK.MAS.DEBTOR.AGENT.IDENTIFIER` | `FtBulkMaster_DebtorAgentIdentifier` | TField | No | Other Identification Code for Debtor Agent. Validation Rules: Optional field. |
| 64 | `FT.BLK.MAS.DEBTOR.AGENT.RESERVED.5` | `FtBulkMaster_DebtorAgentReserved5` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 65 | `FT.BLK.MAS.DEBTOR.AGENT.RESERVED.4` | `FtBulkMaster_DebtorAgentReserved4` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 66 | `FT.BLK.MAS.DEBTOR.AGENT.RESERVED.3` | `FtBulkMaster_DebtorAgentReserved3` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 67 | `FT.BLK.MAS.DEBTOR.AGENT.RESERVED.2` | `FtBulkMaster_DebtorAgentReserved2` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 68 | `FT.BLK.MAS.DEBTOR.AGENT.RESERVED.1` | `FtBulkMaster_DebtorAgentReserved1` | TField | No | Reserved fields of Debtor Agent. Validation Rules: Optional field. |
| 69 | `FT.BLK.MAS.ORDERING.OT.ID.TYPE` | `FtBulkMaster_OrderingOtIdType` | TField | No | Unique identification assigned by the account servicer. Validation Rules: Optional. Free Text |
| 70 | `FT.BLK.MAS.ORDERING.SCHME.CDE` | `FtBulkMaster_OrderingSchmeCde` | TField | No | Name of the identification scheme, in a coded form as published in an external list. Validation Rules: Optional. Free Text |
| 71 | `FT.BLK.MAS.ORDERING.SCH.PRTY` | `FtBulkMaster_OrderingSchPrty` | TField | No | Name of the identification scheme, in a free text form. Validation Rules: Optional. Free Text |
| 72 | `FT.BLK.MAS.ORDERING.SCH.ISSUR` | `FtBulkMaster_OrderingSchIssur` | TField | No | Entity that assigns the identification. Validation Rules: Optional. Free Text |
| 73 | `FT.BLK.MAS.ORDERING.DOB` | `FtBulkMaster_OrderingDob` | TField |  | Date on which a person is born. Validation Rules: T24 DATE |
| 74 | `FT.BLK.MAS.ORDERING.BR.PRVNC` | `FtBulkMaster_OrderingBrPrvnc` | TField | No | Province where a person was born. Validation Rules: Optional. Free Text |
| 75 | `FT.BLK.MAS.ORDERING.BR.CITY` | `FtBulkMaster_OrderingBrCity` | TField | No | City where a person was born. Validation Rules: Optional. Free Text |
| 76 | `FT.BLK.MAS.ORDERING.COUNTRY.RESIDENCE` | `FtBulkMaster_OrderingCountryResidence` | TField | No | Country where a person was born. Validation Rules: Optional. Valid Country |
| 77 | `FT.BLK.MAS.ORDERING.OT.ID` | `FtBulkMaster_OrderingOtId` | TField | No | Unique identification assigned by the account servicer. Validation Rules: Optional. Free Text |
| 78 | `FT.BLK.MAS.ULTIMATE.DEBTOR.NAME` | `FtBulkMaster_UltimateDebtorName` | TField |  | Name of the Ultimate debitor of payment. |
| 79 | `FT.BLK.MAS.ULTIMATE.DEBTOR.ADDR.TYPE` | `FtBulkMaster_UltimateDebtorAddrType` | TField |  | Address type to be used for the Ultimate debtor of payment. |
| 80 | `FT.BLK.MAS.ULTIMATE.DEBTOR.ADDR.LINE` | `FtBulkMaster_UltimateDebtorAddrLine` |  |  |  |
| 81 | `FT.BLK.MAS.ULTIMATE.DEBTOR.BIC` | `FtBulkMaster_UltimateDebtorBic` | TField |  | BIC code of Ultimate debtor of payment. |
| 82 | `FT.BLK.MAS.ULTIMATE.DEBTOR.COUNTRY` | `FtBulkMaster_UltimateDebtorCountry` | TField |  | Country of Ultimate debtor of payment. |
| 83 | `FT.BLK.MAS.ULTIMATE.DEBTOR.RESERVED.5` | `FtBulkMaster_UltimateDebtorReserved5` | TField | No | Reserved fields of Ultimate creditor. Validation Rules: Optional field. |
| 84 | `FT.BLK.MAS.ULTIMATE.DEBTOR.RESERVED.4` | `FtBulkMaster_UltimateDebtorReserved4` | TField | No | Reserved fields of Ultimate creditor. Validation Rules: Optional field. |
| 85 | `FT.BLK.MAS.ULTIMATE.DEBTOR.RESERVED.3` | `FtBulkMaster_UltimateDebtorReserved3` | TField | No | Reserved fields of Ultimate creditor. Validation Rules: Optional field. |
| 86 | `FT.BLK.MAS.ULTIMATE.DEBTOR.RESERVED.2` | `FtBulkMaster_UltimateDebtorReserved2` | TField | No | Reserved fields of Ultimate creditor. Validation Rules: Optional field. |
| 87 | `FT.BLK.MAS.ULTIMATE.DEBTOR.RESERVED.1` | `FtBulkMaster_UltimateDebtorReserved1` | TField | No | Reserved fields of Ultimate creditor. Validation Rules: Optional field. |
| 88 | `FT.BLK.MAS.ULTIMATE.DEBTOR.OT.ID.TYPE` | `FtBulkMaster_UltimateDebtorOtIdType` | TField |  | Ultimate Debtor Id Type identifies if the Ultimate Debtor is an Organisation or an Individual Possible values: None Organisation Private |
| 89 | `FT.BLK.MAS.ULTIMATE.DEBTOR.SCHME.CDE` | `FtBulkMaster_UltimateDebtorSchmeCde` | TField | Yes | The code of the scheme, which issued the identifier for the Ultimate Debtor It will indicate what is captured in the Beneficiary Other Identifier - Social Security Number,Tax Identification Number, Passport Number, Clearing Id Validation Rules: Ultimate Debtor Id Type is mandatory when this field is captured. |
| 90 | `FT.BLK.MAS.ULTIMATE.DEBTOR.SCH.PRTY` | `FtBulkMaster_UltimateDebtorSchPrty` | TField | Yes | The proprietary code of the scheme, which issued the identifier for the Ultimate Debtor Validation Rules: Ultimate Debtor Id Type is mandatory when this field is captured. |
| 91 | `FT.BLK.MAS.ULTIMATE.DEBTOR.SCH.ISSUR` | `FtBulkMaster_UltimateDebtorSchIssur` | TField | Yes | Issuer of the identifier Validation Rules: Ultimate Debtor Id Type is mandatory when this field is captured |
| 92 | `FT.BLK.MAS.ULTIMATE.DEBTOR.DOB` | `FtBulkMaster_UltimateDebtorDob` | TField |  | Holds the birth date of the Ultimate Debtor Validation Rules: It can be used when Ultimate Debtor Identifier Type is set to Private |
| 93 | `FT.BLK.MAS.ULTIMATE.DEBTOR.BR.PRVNC` | `FtBulkMaster_UltimateDebtorBrPrvnc` | TField | Yes | Holds the birth Province of the Ultimate Debtor Validation Rules: It can be used when Ultimate Debtor Identifier Type is set to Private Ultimate Debtor Birth Date is mandatory when this field is captured. |
| 94 | `FT.BLK.MAS.ULTIMATE.DEBTOR.BR.CITY` | `FtBulkMaster_UltimateDebtorBrCity` | TField | Yes | Holds the birth City of the Ultimate Debtor Validation Rules: It can be used when Ultimate Debtor Identifier Type is set to Private Ultimate Debtor Birth Date is mandatory when this field is captured. |
| 95 | `FT.BLK.MAS.ULTIMATE.DEBTOR.OT.ID` | `FtBulkMaster_UltimateDebtorOtId` | TField | Yes | Holds other identifications such as could be a Social Security Number, a Tax Identification Number, Passport Number, a Clearing Id ,etc., of the Ultimate Debtor. Validation Rules: Ultimate Debtor Id Type is mandatory when this field is captured |
| 96 | `FT.BLK.MAS.BULK.REFERENCE` | `FtBulkMaster_BulkReference` | TField | No | This field contains the Bulk Reference generated in ESB for a batch containing more than one transaction and will be used as a unique identifier for each bulk present/part of the Payment Initiation message (pain.001). If the Bulk Reference is associated with a payment then it helps in identifying/tracing the payments that is part of a bulk containing other transactions (more than 1). Validation Rules: Optional. Free Text |
| 97 | `FT.BLK.MAS.CHARGE.BEARER` | `FtBulkMaster_ChargeBearer` | TField |  | Bearer of the charges of the order |
| 98 | `FT.BLK.MAS.DEFAULT.PO.PRODUCT` | `FtBulkMaster_DefaultPoProduct` | TField |  | Payment Order Product Validation Rules: Can be Manually entered or defaulted If entered, Only the ALLOW.PAYMENT.ORDER.PRODUCT from FT.BULK.UPDATE.TYPE parameter is allowed If not entered, the DEFAULT.PAYMENT.ORDER.PRODUCT from FT.BULK.UPDATE.TYPE is populated only when MODE.OF.TRANSFER is PAYMENT |
| 99 | `FT.BLK.MAS.DUPLICATE.CHECK` | `FtBulkMaster_DuplicateCheck` | TField |  | Will define the duplicate criteria which will be used if such a Bulk Master is already defined Validation Rules: Can be Manually entered or defaulted A valid EB.DUPLICATE.TYPE record If not entered, the DUPLICATE.CHECK.CRITERIA from FT.BULK.UPDATE.TYPE is populated |
| 100 | `FT.BLK.MAS.DEFAULT.PAYMENT.SYSTEM` | `FtBulkMaster_DefaultPaymentSystem` | TField |  | Payment Order System Validation Rules: Can be Manually entered or defaulted. If not entered, the DEFAULT.PAYMENT.SYSTEM from FT.BULK.UPDATE.TYPE is populated only when MODE.OF.TRANSFER is PAYMENT |
| 101 | `FT.BLK.MAS.CANCEL.REASON` | `FtBulkMaster_CancelReason` |  |  |  |
| 102 | `FT.BLK.MAS.CANCEL.REMARK` | `FtBulkMaster_CancelRemark` |  |  |  |
| 103 | `FT.BLK.MAS.CANCEL.INITIATED.BY` | `FtBulkMaster_CancelInitiatedBy` |  |  |  |
| 104 | `FT.BLK.MAS.COMPLETION.DATE` | `FtBulkMaster_CompletionDate` | TField |  | Date when the Bulk Master is marked as Completed/Cancelled No Input field |
| 105 | `FT.BLK.MAS.PAYMENT.SYSTEM` | `FtBulkMaster_PaymentSystem` | TField |  | Payment Order System Validation Rules: Allowed values are EXTERNAL or TPS or CONDITIONAL or FT |
| 106 | `FT.BLK.MAS.PAYMENT.SYSTEM.STATUS` | `FtBulkMaster_PaymentSystemStatus` | TField |  | Status of Payment System Validation Rules: No Input Field. System populated |
| 107 | `FT.BLK.MAS.PAYMENT.SYSTEM.UPD.DT` | `FtBulkMaster_PaymentSystemUpdDt` | TField |  | Field to denote when the Status of Payment System is changed Validation Rules: No Input Field. System populated |
| 108 | `FT.BLK.MAS.TOTAL.ITEMS` | `FtBulkMaster_TotalItems` | TField |  | Sum of Uploaded Items and Manual Items Validation Rules: No Input Field. System populated when Mode of Transfer is PAYMENT |
| 109 | `FT.BLK.MAS.ITEMS.CANCELLED` | `FtBulkMaster_ItemsCancelled` | TField |  | Total PO items in CANCELLED Status Validation Rules: No Input Field. System populated when Mode of Transfer is PAYMENT |
| 110 | `FT.BLK.MAS.ITEMS.COMPLETED` | `FtBulkMaster_ItemsCompleted` | TField |  | Total PO items in COMPLETED Status Validation Rules: No Input Field. System populated when Mode of Transfer is PAYMENT |
| 111 | `FT.BLK.MAS.ITEMS.PLACED` | `FtBulkMaster_ItemsPlaced` | TField |  | Total PO items in PLACED Status Validation Rules: No Input Field. System populated when Mode of Transfer is PAYMENT |
| 112 | `FT.BLK.MAS.VALUE.PLACED` | `FtBulkMaster_ValuePlaced` | TField |  | Total Amount of PO items in PLACED Status Validation Rules: No Input Field. System populated when Mode of Transfer is PAYMENT |
| 113 | `FT.BLK.MAS.VALUE.VALID.ITEMS` | `FtBulkMaster_ValueValidItems` | TField |  | This is sum of all AMOUNT in FT.BULK.ITEM/PO records that are in READY status. Validation Rules: No input field. Numeric character. |
| 114 | `FT.BLK.MAS.INITIATOR.NAME` | `FtBulkMaster_InitiatorName` | TField |  | Name of the initiator of payment. |
| 115 | `FT.BLK.MAS.INITIATOR.BIC` | `FtBulkMaster_InitiatorBic` | TField |  | BIC code of initiator of payment. |
| 116 | `FT.BLK.MAS.INITIATOR.OTHER.ID` | `FtBulkMaster_InitiatorOtherId` | TField |  | Other Identification of the initiator of payment |
| 117 | `FT.BLK.MAS.PAYMENT.METHOD` | `FtBulkMaster_PaymentMethod` | TField |  | Field to define method of transfer being initiated, which is required when it is to be processed through payment suites. |
| 118 | `FT.BLK.MAS.MESSAGE.PRIORITY` | `FtBulkMaster_MessagePriority` | TField |  | Priority of the message Validation Rules:Free text of 35 characters. No validations |
| 119 | `FT.BLK.MAS.PYMT.INFO.SER.LEVEL.CODE` | `FtBulkMaster_PymtInfoSerLevelCode` | TField | No | Payment service level code to be sent to account with bank, which describes the priority and execution type of payment. Validation Rules: Valid record from lookup table PAYMENT.SERVICE.LEVEL.CODE. Optional field. |
| 120 | `FT.BLK.MAS.LOCAL.INSTR.CODE` | `FtBulkMaster_LocalInstrCode` | TField |  | Field to define Local Instruction codes |
| 121 | `FT.BLK.MAS.PAYMENT.CATEGORY` | `FtBulkMaster_PaymentCategory` | TField |  | Field to define additional information related to SEPA standing order transactions which can be provided when a payment is initiated within T24 to be processed through payment suites. |
| 122 | `FT.BLK.MAS.FILE.REFERENCE` | `FtBulkMaster_FileReference` | TField |  | Field to denote the File reference of the Uploaded Bulk Master Validation Rules: Input not allowed when SOURCE is MANUAL |
| 123 | `FT.BLK.MAS.AC.FUNDS.AUTH.ID` | `FtBulkMaster_AcFundsAuthId` | TField |  | To capture the record id of AC.FUNDS.AUTHORISATION Validation Rules: User input will not be allowed, only updated by system when creating AC.FUNDS.AUTHORISATION record |
| 124 | `FT.BLK.MAS.LOCKED.EVENT.ID` | `FtBulkMaster_LockedEventId` | TField |  | To capture the AC.LOCKED.EVENTS id if in case the funds is available and reserved Validation Rules: User input will not be allowed, only updated by system when creating AC.LOCKED.EVENTS record |
| 125 | `FT.BLK.MAS.CONTEXT.NAME` | `FtBulkMaster_ContextName` |  |  |  |
| 126 | `FT.BLK.MAS.CONTEXT.VALUE` | `FtBulkMaster_ContextValue` |  |  |  |
| 127 | `FT.BLK.MAS.CREATE.DATE.TIME` | `FtBulkMaster_CreateDateTime` |  |  |  |
| 128 | `FT.BLK.MAS.INITIATOR.OT.ID.TYPE` | `FtBulkMaster_InitiatorOtIdType` | TField |  | Initiator Id Type identifies if the Initiator is an Organisation or an Individual Possible values: None ORGANISATION PRIVATE |
| 129 | `FT.BLK.MAS.ORIGINATING.SOURCE` | `FtBulkMaster_OriginatingSource` | TField |  | Specifies the source from which the payment is originated. Linked to EB.LOOKUP |
| 130 | `FT.BLK.MAS.MESSAGE.CONTENT.NAME` | `FtBulkMaster_MessageContentName` |  |  |  |
| 131 | `FT.BLK.MAS.MESSAGE.CONTENT` | `FtBulkMaster_MessageContent` |  |  |  |
| 132 | `FT.BLK.MAS.TOTAL.TXNS.IN.FILE` | `FtBulkMaster_TotalTxnsInFile` | TField |  | Value updated shows the actual number of transactions in the bulk which is derived by the system during de-bulking |
