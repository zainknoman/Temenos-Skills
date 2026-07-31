# BATCH.NEW.COMPANY — Table Schema

> Source: `INSERTS/I_F.BATCH.NEW.COMPANY` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.BNC.LEVEL` | `BatchNewCompany_Level` | TField | Yes | Validation Rules: Mandatory input. A maximum of 3 characters may be entered. The following values are permitted: FIN CUS INT NOS CCY |
| 2 | `EB.BNC.PRODUCT` | `BatchNewCompany_Product` | TField | Yes | Standard T24 alphanumeric field. Validation Rules: Mandatory input. A maximum of 2 characters may be entered. |
| 3 | `EB.BNC.RECORD.STATUS` | `BatchNewCompany_RecordStatus` | String |  |  |
| 4 | `EB.BNC.CURR.NO` | `BatchNewCompany_CurrNo` | String |  |  |
| 5 | `EB.BNC.INPUTTER` | `BatchNewCompany_Inputter` |  |  |  |
| 6 | `EB.BNC.DATE.TIME` | `BatchNewCompany_DateTime` |  |  |  |
| 7 | `EB.BNC.AUTHORISER` | `BatchNewCompany_Authoriser` | String |  |  |
| 8 | `EB.BNC.CO.CODE` | `BatchNewCompany_CoCode` | String |  |  |
| 9 | `EB.BNC.DEPT.CODE` | `BatchNewCompany_DeptCode` | String |  |  |
| 10 | `EB.BNC.AUDITOR.CODE` | `BatchNewCompany_AuditorCode` | String |  |  |
| 11 | `EB.BNC.AUDIT.DATE.TIME` | `BatchNewCompany_AuditDateTime` | String |  |  |
| 12 | `EB.BNC.DESCRIPTION` | `BatchNewCompany_Description` |  |  |  |
| 13 | `EB.BNC.EXCLUDE.MODULE` | `BatchNewCompany_ExcludeModule` |  |  |  |
| 14 | `EB.BNC.LOCAL.REF` | `BatchNewCompany_LocalRef` |  |  |  |
