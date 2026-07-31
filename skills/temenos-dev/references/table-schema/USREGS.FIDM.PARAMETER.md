# USREGS.FIDM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USREGS.FIDM.PARAMETER` in `USREGS_FIDM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIDM.PARAM.EXCLUDE.CATEGORY` | `UsregsFidmParameter_ExcludeCategory` |  |  |  |
| 2 | `FIDM.PARAM.EXCLUDE.SECTOR` | `UsregsFidmParameter_ExcludeSector` |  |  |  |
| 3 | `FIDM.PARAM.EXCL.PRODUCT.LINE` | `UsregsFidmParameter_ExclProductLine` |  |  |  |
| 4 | `FIDM.PARAM.REPORTING.METHOD` | `UsregsFidmParameter_ReportingMethod` | TField |  | Values Allowed: All Accounts Method and Matched Accounts Method. |
| 5 | `FIDM.PARAM.AC.TYPE.CODE` | `UsregsFidmParameter_AcTypeCode` |  |  |  |
| 6 | `FIDM.PARAM.AC.CATEGORY` | `UsregsFidmParameter_AcCategory` |  |  |  |
| 7 | `FIDM.PARAM.TRUST.CODE` | `UsregsFidmParameter_TrustCode` |  |  |  |
| 8 | `FIDM.PARAM.TRUST.CATEGORY` | `UsregsFidmParameter_TrustCategory` |  |  |  |
| 9 | `FIDM.PARAM.OVERRIDE` | `UsregsFidmParameter_Override` |  |  |  |
| 10 | `FIDM.PARAM.RECORD.STATUS` | `UsregsFidmParameter_RecordStatus` | String |  |  |
| 11 | `FIDM.PARAM.CURR.NO` | `UsregsFidmParameter_CurrNo` | String |  |  |
| 12 | `FIDM.PARAM.INPUTTER` | `UsregsFidmParameter_Inputter` |  |  |  |
| 13 | `FIDM.PARAM.DATE.TIME` | `UsregsFidmParameter_DateTime` |  |  |  |
| 14 | `FIDM.PARAM.AUTHORISER` | `UsregsFidmParameter_Authoriser` | String |  |  |
| 15 | `FIDM.PARAM.CO.CODE` | `UsregsFidmParameter_CoCode` | String |  |  |
| 16 | `FIDM.PARAM.DEPT.CODE` | `UsregsFidmParameter_DeptCode` | String |  |  |
| 17 | `FIDM.PARAM.AUDITOR.CODE` | `UsregsFidmParameter_AuditorCode` | String |  |  |
| 18 | `FIDM.PARAM.AUDIT.DATE.TIME` | `UsregsFidmParameter_AuditDateTime` | String |  |  |
