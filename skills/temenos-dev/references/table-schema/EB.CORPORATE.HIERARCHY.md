# EB.CORPORATE.HIERARCHY — Table Schema

> Source: `INSERTS/I_F.EB.CORPORATE.HIERARCHY` in `EB_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.COR61.REPORTER` | `EbCorporateHierarchy_Reporter` |  |  |  |
| 2 | `EB.COR61.REPORTEE` | `EbCorporateHierarchy_Reportee` |  |  |  |
| 3 | `EB.COR61.REPORTEE.DESC` | `EbCorporateHierarchy_ReporteeDesc` |  |  |  |
| 4 | `EB.COR61.OVERRIDE` | `EbCorporateHierarchy_Override` |  |  |  |
| 5 | `EB.COR61.RECORD.STATUS` | `EbCorporateHierarchy_RecordStatus` |  |  |  |
| 6 | `EB.COR61.CURR.NO` | `EbCorporateHierarchy_CurrNo` |  |  |  |
| 7 | `EB.COR61.INPUTTER` | `EbCorporateHierarchy_Inputter` |  |  |  |
| 8 | `EB.COR61.DATE.TIME` | `EbCorporateHierarchy_DateTime` |  |  |  |
| 9 | `EB.COR61.AUTHORISER` | `EbCorporateHierarchy_Authoriser` |  |  |  |
| 10 | `EB.COR61.CO.CODE` | `EbCorporateHierarchy_CoCode` |  |  |  |
| 11 | `EB.COR61.DEPT.CODE` | `EbCorporateHierarchy_DeptCode` |  |  |  |
| 12 | `EB.COR61.AUDITOR.CODE` | `EbCorporateHierarchy_AuditorCode` |  |  |  |
| 13 | `EB.COR61.AUDIT.DATE.TIME` | `EbCorporateHierarchy_AuditDateTime` |  |  |  |
