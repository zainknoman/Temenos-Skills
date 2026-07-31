# CAMB.PRODUCT.APPLICATION — Table Schema

> Source: `INSERTS/I_F.CAMB.PRODUCT.APPLICATION` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `APPL.PROD.PRODUCT.CODE` | `CambProductApplication_ProductCode` |  |  |  |
| 2 | `APPL.PROD.APPLICATION.NAME` | `CambProductApplication_ApplicationName` |  |  |  |
| 3 | `APPL.PROD.RECORD.STATUS` | `CambProductApplication_RecordStatus` | String |  |  |
| 4 | `APPL.PROD.CURR.NO` | `CambProductApplication_CurrNo` | String |  |  |
| 5 | `APPL.PROD.INPUTTER` | `CambProductApplication_Inputter` |  |  |  |
| 6 | `APPL.PROD.DATE.TIME` | `CambProductApplication_DateTime` |  |  |  |
| 7 | `APPL.PROD.AUTHORISER` | `CambProductApplication_Authoriser` | String |  |  |
| 8 | `APPL.PROD.CO.CODE` | `CambProductApplication_CoCode` | String |  |  |
| 9 | `APPL.PROD.DEPT.CODE` | `CambProductApplication_DeptCode` | String |  |  |
| 10 | `APPL.PROD.AUDITOR.CODE` | `CambProductApplication_AuditorCode` | String |  |  |
| 11 | `APPL.PROD.AUDIT.DATE.TIME` | `CambProductApplication_AuditDateTime` | String |  |  |
