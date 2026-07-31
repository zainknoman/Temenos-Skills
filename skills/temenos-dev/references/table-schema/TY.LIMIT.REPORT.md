# TY.LIMIT.REPORT — Table Schema

> Source: `INSERTS/I_F.TY.LIMIT.REPORT` in `TY_Limits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.LIMIT.REPORT.CURRENCY` | `TyLimitReport_Currency` | TField |  | This field contains the currency in which a breach is raised. |
| 2 | `TY.LIMIT.REPORT.LIMIT.EXPOSURE` | `TyLimitReport_LimitExposure` | TField |  | This field contains the limit amount that is breached by an incoming transaction. |
| 3 | `TY.LIMIT.REPORT.LIMIT.UTIL.BEFORE` | `TyLimitReport_LimitUtilBefore` | TField |  | This field contains the limit utilization amount before a breach was encountered. |
| 4 | `TY.LIMIT.REPORT.LIMIT.UTIL.AFTER` | `TyLimitReport_LimitUtilAfter` | TField |  | This field contains the limit utilization amount after a breach is encountered. |
| 5 | `TY.LIMIT.REPORT.EXCEEDED.BY` | `TyLimitReport_ExceededBy` | TField |  | This field contains the amount by which the current transaction is breached. |
| 6 | `TY.LIMIT.REPORT.DEALER.DESK` | `TyLimitReport_DealerDesk` | TField |  | This field contains the dealer desk that input a transaction that has led to a limit breach. |
| 7 | `TY.LIMIT.REPORT.DEALER.NOTES` | `TyLimitReport_DealerNotes` | TField |  | This field contains any additional notes entered by the dealer at the time of transaction input when a breach was encountered. |
| 8 | `TY.LIMIT.REPORT.LIMIT.BREACH.TIME` | `TyLimitReport_LimitBreachTime` | TField |  | This field contains the time at which the limit breach was encountered. |
| 9 | `TY.LIMIT.REPORT.DEAL.REF` | `TyLimitReport_DealRef` | TField |  | This field contain the transaction reference during the input of which a breach was encountered. |
| 10 | `TY.LIMIT.REPORT.DEAL.DATE` | `TyLimitReport_DealDate` | TField |  | This field contains the date on which the transaction was input and a breach was raised. |
| 11 | `TY.LIMIT.REPORT.DEAL.AMT` | `TyLimitReport_DealAmt` | TField |  | This field contains the transaction amount when a breach was raised. |
| 12 | `TY.LIMIT.REPORT.PRODUCT` | `TyLimitReport_Product` | TField |  | This field contains the product reference of the transaction that raised a limit breach. Could take values as either SP, FW or any valid limit references. |
| 13 | `TY.LIMIT.REPORT.REPORT.DATE` | `TyLimitReport_ReportDate` | TField |  | This field contains the date at which the report has been generated. |
| 14 | `TY.LIMIT.REPORT.RESERVED.9` | `TyLimitReport_Reserved9` | TField |  |  |
| 15 | `TY.LIMIT.REPORT.RESERVED.8` | `TyLimitReport_Reserved8` | TField |  |  |
| 16 | `TY.LIMIT.REPORT.RESERVED.7` | `TyLimitReport_Reserved7` | TField |  |  |
| 17 | `TY.LIMIT.REPORT.RESERVED.6` | `TyLimitReport_Reserved6` | TField |  |  |
| 18 | `TY.LIMIT.REPORT.RESERVED.5` | `TyLimitReport_Reserved5` | TField |  |  |
| 19 | `TY.LIMIT.REPORT.RESERVED.4` | `TyLimitReport_Reserved4` | TField |  |  |
| 20 | `TY.LIMIT.REPORT.RESERVED.3` | `TyLimitReport_Reserved3` | TField |  |  |
| 21 | `TY.LIMIT.REPORT.RESERVED.2` | `TyLimitReport_Reserved2` | TField |  |  |
| 22 | `TY.LIMIT.REPORT.RESERVED.1` | `TyLimitReport_Reserved1` | TField |  |  |
| 23 | `TY.LIMIT.REPORT.LOCAL.REF` | `TyLimitReport_LocalRef` |  |  |  |
