# LIMIT.COMMODITY — Table Schema

> Source: `INSERTS/I_F.LIMIT.COMMODITY` in `LI_Reports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.COM.DESCRIPTION` | `LimitCommodity_Description` |  |  |  |
| 2 | `LI.COM.GRADE.COMMODITY` | `LimitCommodity_GradeCommodity` | TField | No | Allows a status to be associated with a Commodity Limit. Validation Rules: Up to 4 numeric characters CUSTOMER.STATUS code. (Optional Input; No Default value). Any input must be a valid code on the CUSTOMER.STATUS table. |
| 3 | `LI.COM.PRODUCT.GROUP` | `LimitCommodity_ProductGroup` |  |  |  |
| 4 | `LI.COM.LIMIT.CURRENCY` | `LimitCommodity_LimitCurrency` |  |  |  |
| 5 | `LI.COM.LIMIT.AMOUNT` | `LimitCommodity_LimitAmount` |  |  |  |
| 6 | `LI.COM.GRADE.PRODUCT` | `LimitCommodity_GradeProduct` |  |  |  |
| 7 | `LI.COM.REPORT.PROD.GRP` | `LimitCommodity_ReportProdGrp` |  |  |  |
| 8 | `LI.COM.REPORT.CURRENCY` | `LimitCommodity_ReportCurrency` |  |  |  |
| 9 | `LI.COM.REPRT.LIMIT.AMT` | `LimitCommodity_ReprtLimitAmt` |  |  |  |
| 10 | `LI.COM.REPRT.OUTSTANDG` | `LimitCommodity_ReprtOutstandg` |  |  |  |
| 11 | `LI.COM.REPRT.AVAILABLE` | `LimitCommodity_ReprtAvailable` |  |  |  |
| 12 | `LI.COM.OS.CURRENCY` | `LimitCommodity_OsCurrency` |  |  |  |
| 13 | `LI.COM.OS.AMOUNT` | `LimitCommodity_OsAmount` |  |  |  |
| 14 | `LI.COM.RESERVED.1` | `LimitCommodity_Reserved1` | TField |  |  |
| 15 | `LI.COM.RESERVED.2` | `LimitCommodity_Reserved2` | TField |  |  |
| 16 | `LI.COM.RESERVED.3` | `LimitCommodity_Reserved3` | TField |  |  |
| 17 | `LI.COM.RESERVED.4` | `LimitCommodity_Reserved4` | TField |  |  |
| 18 | `LI.COM.LOCAL.REF` | `LimitCommodity_LocalRef` |  |  |  |
| 19 | `LI.COM.OVERRIDE` | `LimitCommodity_Override` |  |  |  |
| 20 | `LI.COM.RECORD.STATUS` | `LimitCommodity_RecordStatus` | String |  |  |
| 21 | `LI.COM.CURR.NO` | `LimitCommodity_CurrNo` | String |  |  |
| 22 | `LI.COM.INPUTTER` | `LimitCommodity_Inputter` |  |  |  |
| 23 | `LI.COM.DATE.TIME` | `LimitCommodity_DateTime` |  |  |  |
| 24 | `LI.COM.AUTHORISER` | `LimitCommodity_Authoriser` | String |  |  |
| 25 | `LI.COM.CO.CODE` | `LimitCommodity_CoCode` | String |  |  |
| 26 | `LI.COM.DEPT.CODE` | `LimitCommodity_DeptCode` | String |  |  |
| 27 | `LI.COM.AUDITOR.CODE` | `LimitCommodity_AuditorCode` | String |  |  |
| 28 | `LI.COM.AUDIT.DATE.TIME` | `LimitCommodity_AuditDateTime` | String |  |  |
