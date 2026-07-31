# CAEFPA.RECURRING.PAYMENT.RETRY — Table Schema

> Source: `INSERTS/I_F.CAEFPA.RECURRING.PAYMENT.RETRY` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RECURR.PYMT.RETRY.RETRY.COUNT` | `RecurringPaymentRetry_RetryCount` |  |  |  |
| 2 | `RECURR.PYMT.RETRY.PROCESSING.DATE` | `RecurringPaymentRetry_ProcessingDate` |  |  |  |
| 3 | `RECURR.PYMT.RETRY.MESSAGE` | `RecurringPaymentRetry_Message` |  |  |  |
| 4 | `RECURR.PYMT.RETRY.STATUS` | `RecurringPaymentRetry_Status` |  |  |  |
| 5 | `RECURR.PYMT.RETRY.RESERVED.1` | `RecurringPaymentRetry_Reserved1` |  |  |  |
| 6 | `RECURR.PYMT.RETRY.RESERVED.2` | `RecurringPaymentRetry_Reserved2` |  |  |  |
| 7 | `RECURR.PYMT.RETRY.RESERVED.3` | `RecurringPaymentRetry_Reserved3` |  |  |  |
| 8 | `RECURR.PYMT.RETRY.RESERVED.4` | `RecurringPaymentRetry_Reserved4` |  |  |  |
| 9 | `RECURR.PYMT.RETRY.RESERVED.5` | `RecurringPaymentRetry_Reserved5` |  |  |  |
| 10 | `RECURR.PYMT.RETRY.RESERVED.6` | `RecurringPaymentRetry_Reserved6` |  |  |  |
| 11 | `RECURR.PYMT.RETRY.RESERVED.7` | `RecurringPaymentRetry_Reserved7` |  |  |  |
| 12 | `RECURR.PYMT.RETRY.RESERVED.8` | `RecurringPaymentRetry_Reserved8` |  |  |  |
| 13 | `RECURR.PYMT.RETRY.RESERVED.9` | `RecurringPaymentRetry_Reserved9` |  |  |  |
| 14 | `RECURR.PYMT.RETRY.RESERVED.10` | `RecurringPaymentRetry_Reserved10` |  |  |  |
| 15 | `RECURR.PYMT.RETRY.LOCAL.REF` | `RecurringPaymentRetry_LocalRef` |  |  |  |
| 16 | `RECURR.PYMT.RETRY.OVERRIDE` | `RecurringPaymentRetry_Override` |  |  |  |
