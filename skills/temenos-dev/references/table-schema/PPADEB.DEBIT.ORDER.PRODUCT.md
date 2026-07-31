# PPADEB.DEBIT.ORDER.PRODUCT — Table Schema

> Source: `INSERTS/I_F.PPADEB.DEBIT.ORDER.PRODUCT` in `PPADEB_DebitOrder.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPADEB.DOP.DESCRIPTION` | `PpadebDebitOrderProduct_Description` |  |  |  |
| 2 | `PPADEB.DOP.ALLOW.FX` | `PpadebDebitOrderProduct_AllowFx` | TField |  | Indicator to state whether FX transaction is allowed for the product Values Allowed: Y,N,Null Y and Null - Multi currency is allowed N - Multi currency is restricted |
| 3 | `PPADEB.DOP.ALLOWED.CURRENCY` | `PpadebDebitOrderProduct_AllowedCurrency` |  |  |  |
| 4 | `PPADEB.DOP.MINIMUM.EXPIRY` | `PpadebDebitOrderProduct_MinimumExpiry` | TField |  | Minimum period of validity (in minutes)for the transaction under the above product. |
| 5 | `PPADEB.DOP.MAXIMUM.EXPIRY` | `PpadebDebitOrderProduct_MaximumExpiry` | TField |  | Maximum period of validity (in minutes)for the transaction under the above product. |
| 6 | `PPADEB.DOP.VALIDATION.API` | `PpadebDebitOrderProduct_ValidationApi` |  |  |  |
| 7 | `PPADEB.DOP.CLEARING.TIME.ZONE` | `PpadebDebitOrderProduct_ClearingTimeZone` | TField |  |  |
| 8 | `PPADEB.DOP.AUTO.ACCEPTANCE.API` | `PpadebDebitOrderProduct_AutoAcceptanceApi` | TField |  | Field to attach conditions for auto-accepting an incoming debit order. Validation Rules:Valid EB.API record of type 'Basic', if the hook is of JBCroutine An EB.API record of type METHOD which implements an interface defined in the EB.API record DEBIT.PRODUCT.AUTO.ACCEPTANCE.HOOK. |
| 9 | `PPADEB.DOP.ALLOWED.DAYS.FOR.CHARGEBACK` | `PpadebDebitOrderProduct_AllowedDaysForChargeback` | TField |  | Field to indicate upto which date the transaction can be reversed. |
| 10 | `PPADEB.DOP.RETENTION.PERIOD` | `PpadebDebitOrderProduct_RetentionPeriod` | TField |  | Field to mention the Retention period to move records from Live to $HIS |
| 11 | `PPADEB.DOP.RESERVED.3` | `PpadebDebitOrderProduct_Reserved3` |  |  |  |
| 12 | `PPADEB.DOP.RESERVED.4` | `PpadebDebitOrderProduct_Reserved4` | TField |  |  |
| 13 | `PPADEB.DOP.RESERVED.5` | `PpadebDebitOrderProduct_Reserved5` | TField |  |  |
| 14 | `PPADEB.DOP.RESERVED.6` | `PpadebDebitOrderProduct_Reserved6` | TField |  |  |
| 15 | `PPADEB.DOP.RESERVED.7` | `PpadebDebitOrderProduct_Reserved7` | TField |  |  |
| 16 | `PPADEB.DOP.RESERVED.8` | `PpadebDebitOrderProduct_Reserved8` | TField |  |  |
| 17 | `PPADEB.DOP.RESERVED.9` | `PpadebDebitOrderProduct_Reserved9` | TField |  |  |
| 18 | `PPADEB.DOP.RESERVED.10` | `PpadebDebitOrderProduct_Reserved10` | TField |  |  |
| 19 | `PPADEB.DOP.LOCAL.REF` | `PpadebDebitOrderProduct_LocalRef` |  |  |  |
| 20 | `PPADEB.DOP.OVERRIDE` | `PpadebDebitOrderProduct_Override` |  |  |  |
| 21 | `PPADEB.DOP.RECORD.STATUS` | `PpadebDebitOrderProduct_RecordStatus` | String |  |  |
| 22 | `PPADEB.DOP.CURR.NO` | `PpadebDebitOrderProduct_CurrNo` | String |  |  |
| 23 | `PPADEB.DOP.INPUTTER` | `PpadebDebitOrderProduct_Inputter` |  |  |  |
| 24 | `PPADEB.DOP.DATE.TIME` | `PpadebDebitOrderProduct_DateTime` |  |  |  |
| 25 | `PPADEB.DOP.AUTHORISER` | `PpadebDebitOrderProduct_Authoriser` | String |  |  |
| 26 | `PPADEB.DOP.CO.CODE` | `PpadebDebitOrderProduct_CoCode` | String |  |  |
| 27 | `PPADEB.DOP.DEPT.CODE` | `PpadebDebitOrderProduct_DeptCode` | String |  |  |
| 28 | `PPADEB.DOP.AUDITOR.CODE` | `PpadebDebitOrderProduct_AuditorCode` | String |  |  |
| 29 | `PPADEB.DOP.AUDIT.DATE.TIME` | `PpadebDebitOrderProduct_AuditDateTime` | String |  |  |
