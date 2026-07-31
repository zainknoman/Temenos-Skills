# LIMIT.COUNTRY — Table Schema

> Source: `INSERTS/I_F.LIMIT.COUNTRY` in `LI_Reports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.COU.DESCRIPTION` | `LimitCountry_Description` |  |  |  |
| 2 | `LI.COU.GRADE.COUNTRY` | `LimitCountry_GradeCountry` | TField | No | Allows a status to be associated with a Country Limit. Validation Rules: Up to 4 numeric characters CUSTOMER.STATUS code. (Optional Input; No Default value). Any input must be a valid code on the CUSTOMER.STATUS table. |
| 3 | `LI.COU.PRODUCT.GROUP` | `LimitCountry_ProductGroup` |  |  |  |
| 4 | `LI.COU.LIMIT.CURRENCY` | `LimitCountry_LimitCurrency` |  |  |  |
| 5 | `LI.COU.LIMIT.AMOUNT` | `LimitCountry_LimitAmount` |  |  |  |
| 6 | `LI.COU.GRADE.PRODUCT` | `LimitCountry_GradeProduct` |  |  |  |
| 7 | `LI.COU.REPORT.PROD.GRP` | `LimitCountry_ReportProdGrp` |  |  |  |
| 8 | `LI.COU.REPORT.CURRENCY` | `LimitCountry_ReportCurrency` |  |  |  |
| 9 | `LI.COU.REPRT.LIMIT.AMT` | `LimitCountry_ReprtLimitAmt` |  |  |  |
| 10 | `LI.COU.REPRT.OUTSTANDG` | `LimitCountry_ReprtOutstandg` |  |  |  |
| 11 | `LI.COU.REPRT.AVAILABLE` | `LimitCountry_ReprtAvailable` |  |  |  |
| 12 | `LI.COU.OS.CURRENCY` | `LimitCountry_OsCurrency` |  |  |  |
| 13 | `LI.COU.OS.AMOUNT` | `LimitCountry_OsAmount` |  |  |  |
| 14 | `LI.COU.RESERVED.1` | `LimitCountry_Reserved1` | TField |  |  |
| 15 | `LI.COU.RESERVED.2` | `LimitCountry_Reserved2` | TField |  |  |
| 16 | `LI.COU.RESERVED.3` | `LimitCountry_Reserved3` | TField |  |  |
| 17 | `LI.COU.RESERVED.4` | `LimitCountry_Reserved4` | TField |  |  |
| 18 | `LI.COU.LOCAL.REF` | `LimitCountry_LocalRef` |  |  |  |
| 19 | `LI.COU.OVERRIDE` | `LimitCountry_Override` |  |  |  |
| 20 | `LI.COU.RECORD.STATUS` | `LimitCountry_RecordStatus` | String |  |  |
| 21 | `LI.COU.CURR.NO` | `LimitCountry_CurrNo` | String |  |  |
| 22 | `LI.COU.INPUTTER` | `LimitCountry_Inputter` |  |  |  |
| 23 | `LI.COU.DATE.TIME` | `LimitCountry_DateTime` |  |  |  |
| 24 | `LI.COU.AUTHORISER` | `LimitCountry_Authoriser` | String |  |  |
| 25 | `LI.COU.CO.CODE` | `LimitCountry_CoCode` | String |  |  |
| 26 | `LI.COU.DEPT.CODE` | `LimitCountry_DeptCode` | String |  |  |
| 27 | `LI.COU.AUDITOR.CODE` | `LimitCountry_AuditorCode` | String |  |  |
| 28 | `LI.COU.AUDIT.DATE.TIME` | `LimitCountry_AuditDateTime` | String |  |  |
