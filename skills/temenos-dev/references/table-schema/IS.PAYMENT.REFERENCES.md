# IS.PAYMENT.REFERENCES — Table Schema

> Source: `INSERTS/I_F.IS.PAYMENT.REFERENCES` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.IPR.PAYMENT.REF` | `IsPaymentReferences_PaymentRef` |  |  |  |
| 2 | `IS.IPR.RETENTION.REF` | `IsPaymentReferences_RetentionRef` |  |  |  |
| 3 | `IS.IPR.REV.PAYMENT.REF` | `IsPaymentReferences_RevPaymentRef` |  |  |  |
| 4 | `IS.IPR.REVIEW.PAY.REF` | `IsPaymentReferences_ReviewPayRef` | TField |  | It displays the reference record id of the application the review payment is made. |
| 5 | `IS.IPR.REVIEW.REV.REF` | `IsPaymentReferences_ReviewRevRef` | TField |  | This field will be updated only if the reviewer payment is reversed with the reference record id of the reversed application. |
