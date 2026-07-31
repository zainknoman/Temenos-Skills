# FIIPMT.INCOMING.PAYMENT.FILE — Table Schema

> Source: `INSERTS/I_F.FIIPMT.INCOMING.PAYMENT.FILE` in `FIIPMT_IncomingPayments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INCOMING.PAYMENT.SENDING.BANK.BIC` | `FiipmtIncomingPaymentFile_SendingBankBic` | TField |  | The BIC details of the bank from which the Camt 53/Camt 54 is received. |
| 2 | `INCOMING.PAYMENT.CREDIT.ACC.NO` | `FiipmtIncomingPaymentFile_CreditAccNo` | TField |  | The IBAN Account number for which the camt message is send |
| 3 | `INCOMING.PAYMENT.PROCESSING.DATE` | `FiipmtIncomingPaymentFile_ProcessingDate` | TField |  | The Processing date of the transaction in the respective bank account |
| 4 | `INCOMING.PAYMENT.VALUE.DATE` | `FiipmtIncomingPaymentFile_ValueDate` | TField |  | The Value date of the transaction in the respective bank account |
| 5 | `INCOMING.PAYMENT.CURRENCY` | `FiipmtIncomingPaymentFile_Currency` | TField |  | The currency in which the payment is made |
| 6 | `INCOMING.PAYMENT.TXN.AMOUNT` | `FiipmtIncomingPaymentFile_TxnAmount` | TField |  | The transaction amount |
| 7 | `INCOMING.PAYMENT.CREDIT.REFERENCE.NO` | `FiipmtIncomingPaymentFile_CreditReferenceNo` |  |  |  |
| 8 | `INCOMING.PAYMENT.ARCHIVING.CODE` | `FiipmtIncomingPaymentFile_ArchivingCode` | TField |  | The Archiving code(In finish bank unquie refernce for payment) |
| 9 | `INCOMING.PAYMENT.END.TO.END.ID` | `FiipmtIncomingPaymentFile_EndToEndId` | TField |  | The transactions unique end to end processing chain reference |
| 10 | `INCOMING.PAYMENT.PAYER.NAME` | `FiipmtIncomingPaymentFile_PayerName` | TField |  | The payer name who has made payment |
| 11 | `INCOMING.PAYMENT.PAYER.ID` | `FiipmtIncomingPaymentFile_PayerId` | TField |  | The payers business ID |
| 12 | `INCOMING.PAYMENT.PURPOSE.CODE` | `FiipmtIncomingPaymentFile_PurposeCode` | TField |  | The purpose code of transaction |
| 13 | `INCOMING.PAYMENT.UNSTRUCTURED.REF` | `FiipmtIncomingPaymentFile_UnstructuredRef` | TField |  | The unstructured information |
| 14 | `INCOMING.PAYMENT.STATEMENT.ID` | `FiipmtIncomingPaymentFile_StatementId` | TField |  | The electronic statement sequence number |
| 15 | `INCOMING.PAYMENT.CAMT.TYPE` | `FiipmtIncomingPaymentFile_CamtType` | TField |  | Type of camt message(camt 53 or camt 54) |
| 16 | `INCOMING.PAYMENT.STMT.CREATION.DATE` | `FiipmtIncomingPaymentFile_StmtCreationDate` | TField |  | The statement creation date |
| 17 | `INCOMING.PAYMENT.STATUS` | `FiipmtIncomingPaymentFile_Status` | TField |  | This will denote the Status of the Transaction. This will be an Eb Lookup.1-ADVANCED.SUBSIDY.ERROR - Error for the payments that are received before due date, where the bank will have to manually take the necessary actions.2-CREDIT.REFERENCE.ERROR - Error for the payments that are received with improper or null Credit Reference Number.3-NO.ERROR - The record with validation is successful and no errors4-SUBSIDY.AMOUNT.ERROR - Error for the payments that are received prior to the due amount, where the bank will have to manually take the necessary actions. |
| 18 | `INCOMING.PAYMENT.REMARKS` | `FiipmtIncomingPaymentFile_Remarks` | TField |  | The bank user can provide the remarks in this field. |
| 19 | `INCOMING.PAYMENT.LOAN.REPAYMENT.TYPE` | `FiipmtIncomingPaymentFile_LoanRepaymentType` | TField |  | This field indicates whether the repayment is of customer or subsidy type |
| 20 | `INCOMING.PAYMENT.RESERVED.4` | `FiipmtIncomingPaymentFile_Reserved4` | TField |  |  |
| 21 | `INCOMING.PAYMENT.RESERVED.3` | `FiipmtIncomingPaymentFile_Reserved3` | TField |  |  |
| 22 | `INCOMING.PAYMENT.RESERVED.2` | `FiipmtIncomingPaymentFile_Reserved2` | TField |  |  |
| 23 | `INCOMING.PAYMENT.RESERVED.1` | `FiipmtIncomingPaymentFile_Reserved1` | TField |  |  |
| 24 | `INCOMING.PAYMENT.LOCAL.REF` | `FiipmtIncomingPaymentFile_LocalRef` |  |  |  |
| 25 | `INCOMING.PAYMENT.OVERRIDE` | `FiipmtIncomingPaymentFile_Override` |  |  |  |
| 26 | `INCOMING.PAYMENT.RECORD.STATUS` | `FiipmtIncomingPaymentFile_RecordStatus` | String |  |  |
| 27 | `INCOMING.PAYMENT.CURR.NO` | `FiipmtIncomingPaymentFile_CurrNo` | String |  |  |
| 28 | `INCOMING.PAYMENT.INPUTTER` | `FiipmtIncomingPaymentFile_Inputter` |  |  |  |
| 29 | `INCOMING.PAYMENT.DATE.TIME` | `FiipmtIncomingPaymentFile_DateTime` |  |  |  |
| 30 | `INCOMING.PAYMENT.AUTHORISER` | `FiipmtIncomingPaymentFile_Authoriser` | String |  |  |
| 31 | `INCOMING.PAYMENT.CO.CODE` | `FiipmtIncomingPaymentFile_CoCode` | String |  |  |
| 32 | `INCOMING.PAYMENT.DEPT.CODE` | `FiipmtIncomingPaymentFile_DeptCode` | String |  |  |
| 33 | `INCOMING.PAYMENT.AUDITOR.CODE` | `FiipmtIncomingPaymentFile_AuditorCode` | String |  |  |
| 34 | `INCOMING.PAYMENT.AUDIT.DATE.TIME` | `FiipmtIncomingPaymentFile_AuditDateTime` | String |  |  |
