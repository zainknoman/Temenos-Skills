# TZ.PAYMENT.REGULATORY.REPORT — Table Schema

> Source: `INSERTS/I_F.TZ.PAYMENT.REGULATORY.REPORT` in `TZ_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TZ.PRR.CUSTOMER.NO` | `TzPaymentRegulatoryReport_CustomerNo` | TField | Yes | The id of the customer which initiated the payment.Must be a T24 Customer Customer number is a mandatory field. |
| 2 | `TZ.PRR.ACCOUNT` | `TzPaymentRegulatoryReport_Account` | TField |  | The id of the customer account from where the payment has been initiated Could be an external account as well so this must not be validated against T24 accounts |
| 3 | `TZ.PRR.PAYMENT.REF` | `TzPaymentRegulatoryReport_PaymentRef` | TField |  | The payment unique reference |
| 4 | `TZ.PRR.PAYMENT.COUNTRY` | `TzPaymentRegulatoryReport_PaymentCountry` | TField |  | This will identify the country code of the bank where the beneficiary account is maintained ( also referred as Account With Institution ) |
| 5 | `TZ.PRR.EXECUTION.DATE` | `TzPaymentRegulatoryReport_ExecutionDate` | TField |  | The payment execution date |
| 6 | `TZ.PRR.SOURCE.APPLN` | `TzPaymentRegulatoryReport_SourceAppln` | TField |  | The Business Application from where the details are extracted |
| 7 | `TZ.PRR.STATUS` | `TzPaymentRegulatoryReport_Status` | TField |  | Blank/Processed status will be updated by ST.CREATE.INDICIA service after the CRS/FATCA processed this PAYMENT.REGULATORY.REPORT record. |
| 8 | `TZ.PRR.PROCESSED.DATE` | `TzPaymentRegulatoryReport_ProcessedDate` | TField |  | When the status get updated as Processed status by ST.CREATE.INDICIA service after the CRS/FATCA processed this PAYMENT.REGULATORY.REPORT record the date of updation will be updated. |
| 9 | `TZ.PRR.LOCAL.REF` | `TzPaymentRegulatoryReport_LocalRef` |  |  |  |
| 10 | `TZ.PRR.OVERRIDE` | `TzPaymentRegulatoryReport_Override` |  |  |  |
| 11 | `TZ.PRR.RESERVED.10` | `TzPaymentRegulatoryReport_Reserved10` | TField |  |  |
| 12 | `TZ.PRR.RESERVED.9` | `TzPaymentRegulatoryReport_Reserved9` | TField |  |  |
| 13 | `TZ.PRR.RESERVED.8` | `TzPaymentRegulatoryReport_Reserved8` | TField |  |  |
| 14 | `TZ.PRR.RESERVED.7` | `TzPaymentRegulatoryReport_Reserved7` | TField |  |  |
| 15 | `TZ.PRR.RESERVED.6` | `TzPaymentRegulatoryReport_Reserved6` | TField |  |  |
| 16 | `TZ.PRR.RESERVED.5` | `TzPaymentRegulatoryReport_Reserved5` | TField |  |  |
| 17 | `TZ.PRR.RESERVED.4` | `TzPaymentRegulatoryReport_Reserved4` | TField |  |  |
| 18 | `TZ.PRR.RESERVED.3` | `TzPaymentRegulatoryReport_Reserved3` | TField |  |  |
| 19 | `TZ.PRR.RESERVED.2` | `TzPaymentRegulatoryReport_Reserved2` | TField |  |  |
| 20 | `TZ.PRR.RESERVED.1` | `TzPaymentRegulatoryReport_Reserved1` | TField |  |  |
| 21 | `TZ.PRR.RECORD.STATUS` | `TzPaymentRegulatoryReport_RecordStatus` | String |  |  |
| 22 | `TZ.PRR.CURR.NO` | `TzPaymentRegulatoryReport_CurrNo` | String |  |  |
| 23 | `TZ.PRR.INPUTTER` | `TzPaymentRegulatoryReport_Inputter` |  |  |  |
| 24 | `TZ.PRR.DATE.TIME` | `TzPaymentRegulatoryReport_DateTime` |  |  |  |
| 25 | `TZ.PRR.AUTHORISER` | `TzPaymentRegulatoryReport_Authoriser` | String |  |  |
| 26 | `TZ.PRR.CO.CODE` | `TzPaymentRegulatoryReport_CoCode` | String |  |  |
| 27 | `TZ.PRR.DEPT.CODE` | `TzPaymentRegulatoryReport_DeptCode` | String |  |  |
| 28 | `TZ.PRR.AUDITOR.CODE` | `TzPaymentRegulatoryReport_AuditorCode` | String |  |  |
| 29 | `TZ.PRR.AUDIT.DATE.TIME` | `TzPaymentRegulatoryReport_AuditDateTime` | String |  |  |
