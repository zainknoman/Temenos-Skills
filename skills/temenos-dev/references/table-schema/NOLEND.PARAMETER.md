# NOLEND.PARAMETER — Table Schema

> Source: `INSERTS/I_F.NOLEND.PARAMETER` in `NOLEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NOLEND.PARAM.DESCRIPTION` | `NolendParameter_Description` |  |  |  |
| 2 | `NOLEND.PARAM.PRODUCT.GROUP` | `NolendParameter_ProductGroup` |  |  |  |
| 3 | `NOLEND.PARAM.PRINCIPAL.INT.PROP` | `NolendParameter_PrincipalIntProp` |  |  |  |
| 4 | `NOLEND.PARAM.FIXED.RATE.INDEX` | `NolendParameter_FixedRateIndex` |  |  |  |
| 5 | `NOLEND.PARAM.FIXED.RATE.PERIOD` | `NolendParameter_FixedRatePeriod` | TField |  | Specifies the arrangement change period. |
| 6 | `NOLEND.PARAM.LOCAL.REF` | `NolendParameter_LocalRef` |  |  |  |
| 7 | `NOLEND.PARAM.OVERRIDE` | `NolendParameter_Override` |  |  |  |
| 8 | `NOLEND.PARAM.RECORD.STATUS` | `NolendParameter_RecordStatus` | String |  |  |
| 9 | `NOLEND.PARAM.CURR.NO` | `NolendParameter_CurrNo` | String |  |  |
| 10 | `NOLEND.PARAM.INPUTTER` | `NolendParameter_Inputter` |  |  |  |
| 11 | `NOLEND.PARAM.DATE.TIME` | `NolendParameter_DateTime` |  |  |  |
| 12 | `NOLEND.PARAM.AUTHORISER` | `NolendParameter_Authoriser` | String |  |  |
| 13 | `NOLEND.PARAM.CO.CODE` | `NolendParameter_CoCode` | String |  |  |
| 14 | `NOLEND.PARAM.DEPT.CODE` | `NolendParameter_DeptCode` | String |  |  |
| 15 | `NOLEND.PARAM.AUDITOR.CODE` | `NolendParameter_AuditorCode` | String |  |  |
| 16 | `NOLEND.PARAM.AUDIT.DATE.TIME` | `NolendParameter_AuditDateTime` | String |  |  |
