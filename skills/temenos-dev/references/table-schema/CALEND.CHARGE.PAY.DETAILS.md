# CALEND.CHARGE.PAY.DETAILS — Table Schema

> Source: `INSERTS/I_F.CALEND.CHARGE.PAY.DETAILS` in `CALEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHARGE.PAY.PAYMENT.DATE` | `CalendChargePayDetails_PaymentDate` | TField |  |  |
| 2 | `CHARGE.PAY.PROPERTY` | `CalendChargePayDetails_Property` |  |  |  |
| 3 | `CHARGE.PAY.CURRENCY` | `CalendChargePayDetails_Currency` |  |  |  |
| 4 | `CHARGE.PAY.RECV.ACCOUNT` | `CalendChargePayDetails_RecvAccount` |  |  |  |
| 5 | `CHARGE.PAY.PAID.AMOUNT` | `CalendChargePayDetails_PaidAmount` |  |  |  |
| 6 | `CHARGE.PAY.TARGET.ACCOUNT` | `CalendChargePayDetails_TargetAccount` |  |  |  |
| 7 | `CHARGE.PAY.RESERVED.15` | `CalendChargePayDetails_Reserved15` | TField |  |  |
| 8 | `CHARGE.PAY.RESERVED.14` | `CalendChargePayDetails_Reserved14` | TField |  |  |
| 9 | `CHARGE.PAY.RESERVED.13` | `CalendChargePayDetails_Reserved13` | TField |  |  |
| 10 | `CHARGE.PAY.RESERVED.12` | `CalendChargePayDetails_Reserved12` | TField |  |  |
| 11 | `CHARGE.PAY.RESERVED.11` | `CalendChargePayDetails_Reserved11` | TField |  |  |
| 12 | `CHARGE.PAY.RESERVED.10` | `CalendChargePayDetails_Reserved10` | TField |  |  |
| 13 | `CHARGE.PAY.RESERVED.9` | `CalendChargePayDetails_Reserved9` | TField |  |  |
| 14 | `CHARGE.PAY.RESERVED.8` | `CalendChargePayDetails_Reserved8` | TField |  |  |
| 15 | `CHARGE.PAY.RESERVED.7` | `CalendChargePayDetails_Reserved7` | TField |  |  |
| 16 | `CHARGE.PAY.RESERVED.6` | `CalendChargePayDetails_Reserved6` | TField |  |  |
| 17 | `CHARGE.PAY.RESERVED.5` | `CalendChargePayDetails_Reserved5` | TField |  |  |
| 18 | `CHARGE.PAY.RESERVED.4` | `CalendChargePayDetails_Reserved4` | TField |  |  |
| 19 | `CHARGE.PAY.RESERVED.3` | `CalendChargePayDetails_Reserved3` | TField |  |  |
| 20 | `CHARGE.PAY.RESERVED.2` | `CalendChargePayDetails_Reserved2` | TField |  |  |
| 21 | `CHARGE.PAY.RESERVED.1` | `CalendChargePayDetails_Reserved1` | TField |  |  |
| 22 | `CHARGE.PAY.STATUS` | `CalendChargePayDetails_Status` | TField |  |  |
| 23 | `CHARGE.PAY.REMARKS` | `CalendChargePayDetails_Remarks` | TField |  |  |
