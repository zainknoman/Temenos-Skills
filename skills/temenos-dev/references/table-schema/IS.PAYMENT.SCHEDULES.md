# IS.PAYMENT.SCHEDULES — Table Schema

> Source: `INSERTS/I_F.IS.PAYMENT.SCHEDULES` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.PSP.PAYMENT.REF` | `IsPaymentSchedules_PaymentRef` | TField |  | The Payment reference that initiated the payment schedule and through which the payment is executed. |
| 2 | `IS.PSP.TRANSACTION.TYPE` | `IsPaymentSchedules_TransactionType` | TField |  | The type of payment being performed. The following are the possible values: COST, VENDOR, DOWNPAYMENT, RETENTION, BROKER or REVIEW |
| 3 | `IS.PSP.TRANSACTION.REF` | `IsPaymentSchedules_TransactionRef` | TField |  | The Transaction reference involved in the payment like Asset Reference, cost Reference, etc. based on the TRANSACTION.TYPE as shown below TRANSACTION.TYPE VENDOR - Asset/Commodity Reference TRANSACTION.TYPE BROKER - Commodity Reference TRANSACTION.TYPE COST- Cost Reference TRANSACTION.TYPE DOWNPAYMENT- Asset/Commodity Reference TRANSACTION.TYPE RETENTION - Asset/Commodity Reference TRANSACTION.TYPE REVIEW - Asset/Commodity Reference |
| 4 | `IS.PSP.PURCHASE.REF` | `IsPaymentSchedules_PurchaseRef` | TField |  | The Purchase reference for which the Payment is made |
| 5 | `IS.PSP.DATE` | `IsPaymentSchedules_Date` | TField |  | Date on which the payment is executed. |
| 6 | `IS.PSP.PAYMENT.AMT` | `IsPaymentSchedules_PaymentAmt` | TField |  | The Payment amount to be paid to the Payee as defined in the IS.PAYMENT transaction |
| 7 | `IS.PSP.RETENTION.AMT` | `IsPaymentSchedules_RetentionAmt` | TField |  | The retention amount to be withheld for each of the Schedule Amount. |
| 8 | `IS.PSP.PAYMENT.METHOD` | `IsPaymentSchedules_PaymentMethod` | TField |  | The Payment Method in which the payment is executed. Valid Values are ADHOC, DD, CASH and SCHEDULE |
| 9 | `IS.PSP.RELATED.REF` | `IsPaymentSchedules_RelatedRef` | TField |  | When a scheduled payment is executed, the reference record id generated from the related application is displayed here. For example if a scheduled vendor payment is executed via Funds Transfer application, reference id of the transfer is recorded and displayed here |
| 10 | `IS.PSP.STATUS` | `IsPaymentSchedules_Status` | TField |  | Displays the status of the scheduled payment. When the scheduled payment is successfully executed status is "PAID". When a successfully executed scheduled payment is reversed status is "REVERSED". |
| 11 | `IS.PSP.REV.PAYMENT.REF` | `IsPaymentSchedules_RevPaymentRef` | TField |  | When a scheduled payment is reversed, the reference record id generated from IS.PAYMENT application is displayed here. |
| 12 | `IS.PSP.REV.RELATED.REF` | `IsPaymentSchedules_RevRelatedRef` | TField |  | When a scheduled payment is reversed, the reference record id generated from the related application is displayed here. For example if a scheduled vendor payment is reversed via Funds Transfer application, reference id of the transfer is recorded and displayed here |
