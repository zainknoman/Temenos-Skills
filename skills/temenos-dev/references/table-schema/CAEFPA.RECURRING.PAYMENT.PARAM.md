# CAEFPA.RECURRING.PAYMENT.PARAM — Table Schema

> Source: `INSERTS/I_F.CAEFPA.RECURRING.PAYMENT.PARAM` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RECURR.PP.LEAD.DAYS` | `RecurringPaymentParam_LeadDays` |  |  |  |
| 2 | `RECURR.PP.HOLIDAY.CALENDAR` | `RecurringPaymentParam_HolidayCalendar` |  |  |  |
| 3 | `RECURR.PP.NO.OF.RETRIES` | `RecurringPaymentParam_NoOfRetries` |  |  |  |
| 4 | `RECURR.PP.PURGE.DAYS` | `RecurringPaymentParam_PurgeDays` |  |  |  |
| 5 | `RECURR.PP.FRQUENCY.PERIOD` | `RecurringPaymentParam_FrquencyPeriod` |  |  |  |
| 6 | `RECURR.PP.FREQUENCY.VALUE` | `RecurringPaymentParam_FrequencyValue` |  |  |  |
| 7 | `RECURR.PP.API.STATUS.CODE` | `RecurringPaymentParam_ApiStatusCode` |  |  |  |
| 8 | `RECURR.PP.RESERVED.2` | `RecurringPaymentParam_Reserved2` |  |  |  |
| 9 | `RECURR.PP.RESERVED.3` | `RecurringPaymentParam_Reserved3` |  |  |  |
| 10 | `RECURR.PP.RESERVED.4` | `RecurringPaymentParam_Reserved4` |  |  |  |
| 11 | `RECURR.PP.RESERVED.5` | `RecurringPaymentParam_Reserved5` |  |  |  |
| 12 | `RECURR.PP.RESERVED.6` | `RecurringPaymentParam_Reserved6` |  |  |  |
| 13 | `RECURR.PP.RESERVED.7` | `RecurringPaymentParam_Reserved7` |  |  |  |
| 14 | `RECURR.PP.RESERVED.8` | `RecurringPaymentParam_Reserved8` |  |  |  |
| 15 | `RECURR.PP.RESERVED.9` | `RecurringPaymentParam_Reserved9` |  |  |  |
| 16 | `RECURR.PP.RESERVED.10` | `RecurringPaymentParam_Reserved10` |  |  |  |
| 17 | `RECURR.PP.LOCAL.REF` | `RecurringPaymentParam_LocalRef` |  |  |  |
| 18 | `RECURR.PP.OVERRIDE` | `RecurringPaymentParam_Override` |  |  |  |
| 19 | `RECURR.PP.RECORD.STATUS` | `RecurringPaymentParam_RecordStatus` |  |  |  |
| 20 | `RECURR.PP.CURR.NO` | `RecurringPaymentParam_CurrNo` |  |  |  |
| 21 | `RECURR.PP.INPUTTER` | `RecurringPaymentParam_Inputter` |  |  |  |
| 22 | `RECURR.PP.DATE.TIME` | `RecurringPaymentParam_DateTime` |  |  |  |
| 23 | `RECURR.PP.AUTHORISER` | `RecurringPaymentParam_Authoriser` |  |  |  |
| 24 | `RECURR.PP.CO.CODE` | `RecurringPaymentParam_CoCode` |  |  |  |
| 25 | `RECURR.PP.DEPT.CODE` | `RecurringPaymentParam_DeptCode` |  |  |  |
| 26 | `RECURR.PP.AUDITOR.CODE` | `RecurringPaymentParam_AuditorCode` |  |  |  |
| 27 | `RECURR.PP.AUDIT.DATE.TIME` | `RecurringPaymentParam_AuditDateTime` |  |  |  |
