# PO.PAYMENT.REFERENCE — Table Schema

> Source: `INSERTS/I_F.PO.PAYMENT.REFERENCE` in `PO_Cashpooling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PO.PYMT.PAYMENT.ORDER.ID` | `PoPaymentReference_PaymentOrderId` |  |  |  |
| 2 | `PO.PYMT.PAYMENT.STATUS` | `PoPaymentReference_PaymentStatus` |  |  |  |
| 3 | `PO.PYMT.RESERVED1` | `PoPaymentReference_Reserved1` |  |  |  |
| 4 | `PO.PYMT.RESERVED2` | `PoPaymentReference_Reserved2` |  |  |  |
| 5 | `PO.PYMT.RESERVED3` | `PoPaymentReference_Reserved3` |  |  |  |
| 6 | `PO.PYMT.RESERVED4` | `PoPaymentReference_Reserved4` | TField |  |  |
| 7 | `PO.PYMT.RESERVED5` | `PoPaymentReference_Reserved5` | TField |  |  |
| 8 | `PO.PYMT.RESERVED6` | `PoPaymentReference_Reserved6` | TField |  |  |
