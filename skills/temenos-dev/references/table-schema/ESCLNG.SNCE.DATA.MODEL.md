# ESCLNG.SNCE.DATA.MODEL — Table Schema

> Source: `INSERTS/I_F.ESCLNG.SNCE.DATA.MODEL` in `ESCLNG_MiscellaneousPayments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.SNCE.RECORD.CODE` | `EsclngSnceDataModel_RecordCode` | TField |  | This field captures Record Code |
| 2 | `ES.SNCE.TRANSACTION.CODE` | `EsclngSnceDataModel_TransactionCode` | TField |  | This field captures Transaction Code |
| 3 | `ES.SNCE.TRANSACTION.NATURE` | `EsclngSnceDataModel_TransactionNature` | TField |  | This field captures Nature of Transaction 1-collections 2-Payments |
| 4 | `ES.SNCE.TRANSACTION.TYPE` | `EsclngSnceDataModel_TransactionType` | TField |  | This field captures Transaction Type range from 01 to 15 |
| 5 | `ES.SNCE.TRANSACTION.REFERENCE` | `EsclngSnceDataModel_TransactionReference` | TField |  | This field provides the Payment Transaction Reference |
| 6 | `ES.SNCE.SOURCE.ENTITY` | `EsclngSnceDataModel_SourceEntity` | TField |  | This field captures Source Office Entity |
| 7 | `ES.SNCE.IBAN` | `EsclngSnceDataModel_Iban` | TField |  | This field captures IBAN value |
| 8 | `ES.SNCE.MAIN.TRANSACTION.AMOUNT` | `EsclngSnceDataModel_MainTransactionAmount` | TField |  | This field provides the Amount of transaction that has been done |
| 9 | `ES.SNCE.INTERBANK.RATE.NATURE` | `EsclngSnceDataModel_InterbankRateNature` | TField |  | This field captures Nature of the Interbank Rate 1-assigned 2-impacted |
| 10 | `ES.SNCE.INTERBANK.RATE.KEY` | `EsclngSnceDataModel_InterbankRateKey` | TField |  | This field captures Interbank Rate Key |
| 11 | `ES.SNCE.INTERBANK.RATE.AMOUNT` | `EsclngSnceDataModel_InterbankRateAmount` | TField |  | This field captures Interbank Rate Amount |
| 12 | `ES.SNCE.AUTHORIZATION.KEY` | `EsclngSnceDataModel_AuthorizationKey` | TField |  | This field captures Authorization Key value |
| 13 | `ES.SNCE.ORIGINAL.AMOUNT` | `EsclngSnceDataModel_OriginalAmount` | TField |  | This field holds the Original Amount |
| 14 | `ES.SNCE.SUBSYSTEM.INDICATOR` | `EsclngSnceDataModel_SubsystemIndicator` | TField |  | This field provides Subsystem Indicator value |
| 15 | `ES.SNCE.SCHEME.TYPE` | `EsclngSnceDataModel_SchemeType` | TField |  | This field captures Scheme Type |
| 16 | `ES.SNCE.TRANSACTION.TYPE.INDICATOR` | `EsclngSnceDataModel_TransactionTypeIndicator` | TField |  | This field captures Transaction Type Indicator value |
| 17 | `ES.SNCE.REIMBURSEMENT.REQUEST` | `EsclngSnceDataModel_ReimbursementRequest` | TField |  | This field captures Reasons for Reimbursement Request |
| 18 | `ES.SNCE.RESPONSE.REQUEST` | `EsclngSnceDataModel_ResponseRequest` | TField |  | This field captures Reasons for Response to Reimbursement Request |
| 19 | `ES.SNCE.REIMBURSEMENT.AMOUNT` | `EsclngSnceDataModel_ReimbursementAmount` | TField |  | This field captures Unauthorized Reimbursement Amount |
| 20 | `ES.SNCE.DEBIT.REFERENCE` | `EsclngSnceDataModel_DebitReference` | TField |  | This field captures Reference of the debit given by creditor client |
| 21 | `ES.SNCE.UNIQUE.ORDER.REFERENCE` | `EsclngSnceDataModel_UniqueOrderReference` | TField |  | This field captures Unique Order Reference |
| 22 | `ES.SNCE.SETTLEMENT.DATE` | `EsclngSnceDataModel_SettlementDate` | TField |  | This field captures Settlement Date |
| 23 | `ES.SNCE.REIMBURSEMENT.REQUEST.DATE` | `EsclngSnceDataModel_ReimbursementRequestDate` | TField |  | This field captures Reimbursement Request Date |
| 24 | `ES.SNCE.CREDITOR.BIC` | `EsclngSnceDataModel_CreditorBic` | TField |  | This field captures BIC of the creditor's entity |
| 25 | `ES.SNCE.DEBTOR.IBAN` | `EsclngSnceDataModel_DebtorIban` | TField |  | This field captures IBAN of the debtor |
| 26 | `ES.SNCE.PAYEE.IBAN` | `EsclngSnceDataModel_PayeeIban` | TField |  | This field captures IBAN of the Payee |
| 27 | `ES.SNCE.CREDITOR.ID` | `EsclngSnceDataModel_CreditorId` | TField |  | This field captures Creditor ID |
| 28 | `ES.SNCE.DEBTOR.NAME` | `EsclngSnceDataModel_DebtorName` |  |  |  |
| 29 | `ES.SNCE.DEBTOR.BIC` | `EsclngSnceDataModel_DebtorBic` | TField |  | This field captures Debtor Entity's BIC code |
| 30 | `ES.SNCE.CREDITOR.NAME` | `EsclngSnceDataModel_CreditorName` |  |  |  |
| 31 | `ES.SNCE.RECOVERY.DATE` | `EsclngSnceDataModel_RecoveryDate` | TField |  | This field captures Date of Recovery from the Debtor |
| 32 | `ES.SNCE.DIRECT.DEBIT.ORDER.TYPE` | `EsclngSnceDataModel_DirectDebitOrderType` | TField |  | This field captures Direct Debit Oder Type |
| 33 | `ES.SNCE.CREDIT.REFERENCE` | `EsclngSnceDataModel_CreditReference` | TField |  | This field captures Credit Entity Reference |
| 34 | `ES.SNCE.REQUEST.REFERENCE` | `EsclngSnceDataModel_RequestReference` | TField |  | This field captures Request Reference |
| 35 | `ES.SNCE.DEBTOR.ENTITY.NAME` | `EsclngSnceDataModel_DebtorEntityName` |  |  |  |
| 36 | `ES.SNCE.RECEIPT.DATE` | `EsclngSnceDataModel_ReceiptDate` | TField |  | This field captures Date of the Receipt of the debtor's request |
| 37 | `ES.SNCE.DELIVERY.DATE` | `EsclngSnceDataModel_DeliveryDate` | TField |  | This field captures Response Delivery date |
| 38 | `ES.SNCE.RESPONSE.REFERENCE` | `EsclngSnceDataModel_ResponseReference` | TField |  | This field captures Response Reference |
| 39 | `ES.SNCE.COMPLEMENTARY.CONCEPT` | `EsclngSnceDataModel_ComplementaryConcept` |  |  |  |
| 40 | `ES.SNCE.PROCESS.DATE` | `EsclngSnceDataModel_ProcessDate` | TField |  | This field provides the Processed date |
| 41 | `ES.SNCE.STATUS.CODE` | `EsclngSnceDataModel_StatusCode` | TField |  | This field provides the Status of the Payment |
| 42 | `ES.SNCE.LOCAL.REF` | `EsclngSnceDataModel_LocalRef` |  |  |  |
| 43 | `ES.SNCE.DIRECTION` | `EsclngSnceDataModel_Direction` | TField |  | This field provides the Direction of the Payment |
| 44 | `ES.SNCE.STATUS` | `EsclngSnceDataModel_Status` | TField |  | This field provides the Status of Cancellation |
| 45 | `ES.SNCE.CURRENCY` | `EsclngSnceDataModel_Currency` | TField |  | This field holds the currency |
| 46 | `ES.SNCE.CANCEL.REASON.CODE` | `EsclngSnceDataModel_CancelReasonCode` | TField |  | This field holds Cancel Reason Code |
| 47 | `ES.SNCE.CANCEL.REASON` | `EsclngSnceDataModel_CancelReason` | TField |  | This field holds Cancel Reason |
| 48 | `ES.SNCE.COMP.VAL.CONCEPT` | `EsclngSnceDataModel_CompValConcept` | TField |  | This field holds the Computer Validation Concept |
| 49 | `ES.SNCE.REJECT.REASON` | `EsclngSnceDataModel_RejectReason` |  |  |  |
| 50 | `ES.SNCE.ORIGINATOR.ACCOUNT` | `EsclngSnceDataModel_OriginatorAccount` | TField |  | This field holds Originator Account |
| 51 | `ES.SNCE.BENEFICIARY.ACCOUNT` | `EsclngSnceDataModel_BeneficiaryAccount` | TField |  | This field holds Beneficiary Account |
| 52 | `ES.SNCE.MESSAGE.TYPE` | `EsclngSnceDataModel_MessageType` | TField |  | This field holds Message Type |
| 53 | `ES.SNCE.ORIGINAL.MESG.TYPE` | `EsclngSnceDataModel_OriginalMesgType` | TField |  | This field holds Original Message Type |
| 54 | `ES.SNCE.ORIG.TXN.TYPE` | `EsclngSnceDataModel_OrigTxnType` | TField |  | This field Original Transaction type |
| 55 | `ES.SNCE.CUSTOMER.ID` | `EsclngSnceDataModel_CustomerId` | TField |  | This field holds the Customer Id |
| 56 | `ES.SNCE.RESENT.COUNT` | `EsclngSnceDataModel_ResentCount` | TField |  | This field holds the resent count |
| 57 | `ES.SNCE.PAYMENT.REFERENCE` | `EsclngSnceDataModel_PaymentReference` | TField |  | This field holds the Payment Reference |
| 58 | `ES.SNCE.OVERRIDE` | `EsclngSnceDataModel_Override` |  |  |  |
| 59 | `ES.SNCE.RECORD.STATUS` | `EsclngSnceDataModel_RecordStatus` | String |  |  |
| 60 | `ES.SNCE.CURR.NO` | `EsclngSnceDataModel_CurrNo` | String |  |  |
| 61 | `ES.SNCE.INPUTTER` | `EsclngSnceDataModel_Inputter` |  |  |  |
| 62 | `ES.SNCE.DATE.TIME` | `EsclngSnceDataModel_DateTime` |  |  |  |
| 63 | `ES.SNCE.AUTHORISER` | `EsclngSnceDataModel_Authoriser` | String |  |  |
| 64 | `ES.SNCE.CO.CODE` | `EsclngSnceDataModel_CoCode` | String |  |  |
| 65 | `ES.SNCE.DEPT.CODE` | `EsclngSnceDataModel_DeptCode` | String |  |  |
| 66 | `ES.SNCE.AUDITOR.CODE` | `EsclngSnceDataModel_AuditorCode` | String |  |  |
| 67 | `ES.SNCE.AUDIT.DATE.TIME` | `EsclngSnceDataModel_AuditDateTime` | String |  |  |
| 68 | `ES.SNCE.SNCE08.UNIQUE.REF` | `EsclngSnceDataModel_Snce08UniqueRef` | TField |  | This field holds the Unique Reference |
| 69 | `ES.SNCE.PARTIAL.TRANSACTION` | `EsclngSnceDataModel_PartialTransaction` | TField |  | This field holds the Partial Transaction |
