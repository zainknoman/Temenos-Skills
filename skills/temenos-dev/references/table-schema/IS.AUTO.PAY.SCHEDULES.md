# IS.AUTO.PAY.SCHEDULES — Table Schema

> Source: `INSERTS/I_F.IS.AUTO.PAY.SCHEDULES` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.APS.PAYMENT.REFERENCE` | `IsAutoPaySchedules_PaymentReference` | TField |  | The payment reference for which the payment has to be processed. (ID of the file IS.PAYMENT) |
| 2 | `IS.APS.BILL.DATE` | `IsAutoPaySchedules_BillDate` | TField |  | The schedule date on which the vendor or cost payment has to be processed. |
| 3 | `IS.APS.PAYMENT.AMT` | `IsAutoPaySchedules_PaymentAmt` | TField |  | The vendor or cost amount to be paid on the scheduled date |
| 4 | `IS.APS.RETENTION.AMT` | `IsAutoPaySchedules_RetentionAmt` | TField |  | The retention amount to be retained on the scheduled date. |
