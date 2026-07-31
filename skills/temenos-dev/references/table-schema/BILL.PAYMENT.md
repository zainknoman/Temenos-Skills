# BILL.PAYMENT — Table Schema

> Source: `INSERTS/I_F.BILL.PAYMENT` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BILL.PAY.PAYER` | `BillPayment_Payer` | TField |  | This is Linked to Customer Application. Either Customer/member Id to be inputted here. |
| 2 | `BILL.PAY.PRIMARY.ACCOUNT` | `BillPayment_PrimaryAccount` | TField |  | Valid Default Primary Account to be Used In case individual Accounts are not selected. |
| 3 | `BILL.PAY.PAYEE.ID` | `BillPayment_PayeeId` |  |  |  |
| 4 | `BILL.PAY.PAYEE.DESC` | `BillPayment_PayeeDesc` |  |  |  |
| 5 | `BILL.PAY.PAYER.BP.ACC.NO` | `BillPayment_PayerBpAccNo` |  |  |  |
| 6 | `BILL.PAY.PYMT.ACCT` | `BillPayment_PymtAcct` |  |  |  |
| 7 | `BILL.PAY.AMOUNT` | `BillPayment_Amount` |  |  |  |
| 8 | `BILL.PAY.EFFECTIVE.DATE` | `BillPayment_EffectiveDate` |  |  |  |
| 9 | `BILL.PAY.TRACE.NO` | `BillPayment_TraceNo` |  |  |  |
| 10 | `BILL.PAY.PAYMENT.STATUS` | `BillPayment_PaymentStatus` |  |  |  |
| 11 | `BILL.PAY.REJECTION.REASON` | `BillPayment_RejectionReason` |  |  |  |
| 12 | `BILL.PAY.UB.PAYMENT.ID` | `BillPayment_UbPaymentId` |  |  |  |
| 13 | `BILL.PAY.LOCAL.REF` | `BillPayment_LocalRef` |  |  |  |
| 14 | `BILL.PAY.RESERVED.9` | `BillPayment_Reserved9` | TField |  |  |
| 15 | `BILL.PAY.RESERVED.8` | `BillPayment_Reserved8` | TField |  |  |
| 16 | `BILL.PAY.RESERVED.7` | `BillPayment_Reserved7` | TField |  |  |
| 17 | `BILL.PAY.RESERVED.6` | `BillPayment_Reserved6` | TField |  |  |
| 18 | `BILL.PAY.RESERVED.5` | `BillPayment_Reserved5` | TField |  |  |
| 19 | `BILL.PAY.RESERVED.4` | `BillPayment_Reserved4` | TField |  |  |
| 20 | `BILL.PAY.RESERVED.3` | `BillPayment_Reserved3` | TField |  |  |
| 21 | `BILL.PAY.RESERVED.2` | `BillPayment_Reserved2` | TField |  |  |
| 22 | `BILL.PAY.OVERRIDE` | `BillPayment_Override` |  |  |  |
| 23 | `BILL.PAY.RECORD.STATUS` | `BillPayment_RecordStatus` | String |  |  |
| 24 | `BILL.PAY.CURR.NO` | `BillPayment_CurrNo` | String |  |  |
| 25 | `BILL.PAY.INPUTTER` | `BillPayment_Inputter` |  |  |  |
| 26 | `BILL.PAY.DATE.TIME` | `BillPayment_DateTime` |  |  |  |
| 27 | `BILL.PAY.AUTHORISER` | `BillPayment_Authoriser` | String |  |  |
| 28 | `BILL.PAY.CO.CODE` | `BillPayment_CoCode` | String |  |  |
| 29 | `BILL.PAY.DEPT.CODE` | `BillPayment_DeptCode` | String |  |  |
| 30 | `BILL.PAY.AUDITOR.CODE` | `BillPayment_AuditorCode` | String |  |  |
| 31 | `BILL.PAY.AUDIT.DATE.TIME` | `BillPayment_AuditDateTime` | String |  |  |
