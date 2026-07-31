# FIIPMT.PAYMENT.INFO — Table Schema

> Source: `INSERTS/I_F.FIIPMT.PAYMENT.INFO` in `FIIPMT_IncomingPayments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PAYMENT.INFO.CREDIT.ACC.NO` | `FiipmtPaymentInfo_CreditAccNo` | TField |  | The IBAN Account number for which the camt message is send. |
| 2 | `PAYMENT.INFO.AMOUNT` | `FiipmtPaymentInfo_Amount` | TField |  | The transaction amount |
| 3 | `PAYMENT.INFO.STATUS` | `FiipmtPaymentInfo_Status` | TField |  | This will denote the Status of the Transaction. This will be an Eb Lookup.1-READY.FOR.PAYMENT - Indicates that a Payment has been received and the Loan Settlement is yet to be raised2-PAYMENT.POSTED - Payment is created by TPH via Payment Order but yet to be processed with Heavy Weight Product Condition Service.3-POSTING.FAILED - Error while creating the payment in TPH via PO. No TPH entry created for this record.4-PAYMENT.FAILED - Payment is in error queue in TPH.5-PAYMENT.PROCESSED - Payment is processed successfully by TPH with Status Code as 999.6-PAYMENT.REVERSED - Payment is processed successfully and reversal posting is raised in TPH. |
| 4 | `PAYMENT.INFO.PAYMENT.ORDER.REF` | `FiipmtPaymentInfo_PaymentOrderRef` | TField |  | Payment Order Reference number which is @ID of PAYMENT.ORDER application for the transaction. |
| 5 | `PAYMENT.INFO.CREDIT.REFERENCE.NO` | `FiipmtPaymentInfo_CreditReferenceNo` | TField |  | The Structured creditor reference number for which the payment has been made by the customer |
| 6 | `PAYMENT.INFO.VALUE.DATE` | `FiipmtPaymentInfo_ValueDate` | TField |  | The Value date of the transaction in the respective bank account |
| 7 | `PAYMENT.INFO.RESERVED.5` | `FiipmtPaymentInfo_Reserved5` | TField |  |  |
| 8 | `PAYMENT.INFO.RESERVED.4` | `FiipmtPaymentInfo_Reserved4` | TField |  |  |
| 9 | `PAYMENT.INFO.RESERVED.3` | `FiipmtPaymentInfo_Reserved3` | TField |  |  |
| 10 | `PAYMENT.INFO.RESERVED.2` | `FiipmtPaymentInfo_Reserved2` | TField |  |  |
| 11 | `PAYMENT.INFO.RESERVED.1` | `FiipmtPaymentInfo_Reserved1` | TField |  |  |
| 12 | `PAYMENT.INFO.LOCAL.REF` | `FiipmtPaymentInfo_LocalRef` |  |  |  |
| 13 | `PAYMENT.INFO.OVERRIDE` | `FiipmtPaymentInfo_Override` |  |  |  |
| 14 | `PAYMENT.INFO.RECORD.STATUS` | `FiipmtPaymentInfo_RecordStatus` | String |  |  |
| 15 | `PAYMENT.INFO.CURR.NO` | `FiipmtPaymentInfo_CurrNo` | String |  |  |
| 16 | `PAYMENT.INFO.INPUTTER` | `FiipmtPaymentInfo_Inputter` |  |  |  |
| 17 | `PAYMENT.INFO.DATE.TIME` | `FiipmtPaymentInfo_DateTime` |  |  |  |
| 18 | `PAYMENT.INFO.AUTHORISER` | `FiipmtPaymentInfo_Authoriser` | String |  |  |
| 19 | `PAYMENT.INFO.CO.CODE` | `FiipmtPaymentInfo_CoCode` | String |  |  |
| 20 | `PAYMENT.INFO.DEPT.CODE` | `FiipmtPaymentInfo_DeptCode` | String |  |  |
| 21 | `PAYMENT.INFO.AUDITOR.CODE` | `FiipmtPaymentInfo_AuditorCode` | String |  |  |
| 22 | `PAYMENT.INFO.AUDIT.DATE.TIME` | `FiipmtPaymentInfo_AuditDateTime` | String |  |  |
