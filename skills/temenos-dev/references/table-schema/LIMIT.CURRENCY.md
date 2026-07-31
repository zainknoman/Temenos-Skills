# LIMIT.CURRENCY — Table Schema

> Source: `INSERTS/I_F.LIMIT.CURRENCY` in `LI_LimitTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.CCY.DESCRIPTION` | `LimitCurrency_Description` |  |  |  |
| 2 | `LI.CCY.GRADE.CURRENCY` | `LimitCurrency_GradeCurrency` | TField | No | Allows a status to be associated with a Currency Limit. Validation Rules: Up to 4 numeric characters CUSTOMER.STATUS code. (Optional Input; No Default value). Any input must be a valid code on the CUSTOMER.STATUS table. |
| 3 | `LI.CCY.PRODUCT.GROUP` | `LimitCurrency_ProductGroup` |  |  |  |
| 4 | `LI.CCY.LIMIT.AMOUNT` | `LimitCurrency_LimitAmount` |  |  |  |
| 5 | `LI.CCY.GRADE.PRODUCT` | `LimitCurrency_GradeProduct` |  |  |  |
| 6 | `LI.CCY.REPORT.PROD.GRP` | `LimitCurrency_ReportProdGrp` |  |  |  |
| 7 | `LI.CCY.REPRT.LIMIT.AMT` | `LimitCurrency_ReprtLimitAmt` |  |  |  |
| 8 | `LI.CCY.REPRT.OUTSTANDG` | `LimitCurrency_ReprtOutstandg` |  |  |  |
| 9 | `LI.CCY.REPRT.AVAILABLE` | `LimitCurrency_ReprtAvailable` |  |  |  |
| 10 | `LI.CCY.RESERVED.1` | `LimitCurrency_Reserved1` | TField |  |  |
| 11 | `LI.CCY.RESERVED.2` | `LimitCurrency_Reserved2` | TField |  |  |
| 12 | `LI.CCY.RESERVED.3` | `LimitCurrency_Reserved3` | TField |  |  |
| 13 | `LI.CCY.RESERVED.4` | `LimitCurrency_Reserved4` | TField |  |  |
| 14 | `LI.CCY.LOCAL.REF` | `LimitCurrency_LocalRef` |  |  |  |
| 15 | `LI.CCY.OVERRIDE` | `LimitCurrency_Override` |  |  |  |
| 16 | `LI.CCY.RECORD.STATUS` | `LimitCurrency_RecordStatus` | String |  |  |
| 17 | `LI.CCY.CURR.NO` | `LimitCurrency_CurrNo` | String |  |  |
| 18 | `LI.CCY.INPUTTER` | `LimitCurrency_Inputter` |  |  |  |
| 19 | `LI.CCY.DATE.TIME` | `LimitCurrency_DateTime` |  |  |  |
| 20 | `LI.CCY.AUTHORISER` | `LimitCurrency_Authoriser` | String |  |  |
| 21 | `LI.CCY.CO.CODE` | `LimitCurrency_CoCode` | String |  |  |
| 22 | `LI.CCY.DEPT.CODE` | `LimitCurrency_DeptCode` | String |  |  |
| 23 | `LI.CCY.AUDITOR.CODE` | `LimitCurrency_AuditorCode` | String |  |  |
| 24 | `LI.CCY.AUDIT.DATE.TIME` | `LimitCurrency_AuditDateTime` | String |  |  |
