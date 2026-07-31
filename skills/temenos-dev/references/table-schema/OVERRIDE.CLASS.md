# OVERRIDE.CLASS — Table Schema

> Source: `INSERTS/I_F.OVERRIDE.CLASS` in `EB_OverrideProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.OVCL.OVERRIDE.TEXT` | `OverrideClass_OverrideText` |  |  |  |
| 2 | `EB.OVCL.OVERRIDE.DETAIL` | `OverrideClass_OverrideDetail` |  |  |  |
| 3 | `EB.OVCL.DEFAULT.CLASS` | `OverrideClass_DefaultClass` |  |  |  |
| 4 | `EB.OVCL.RESERVED.3` | `OverrideClass_Reserved3` | TField |  |  |
| 5 | `EB.OVCL.LOCAL.REF` | `OverrideClass_LocalRef` |  |  |  |
| 6 | `EB.OVCL.RESERVED.1` | `OverrideClass_Reserved1` | TField |  |  |
| 7 | `EB.OVCL.RECORD.STATUS` | `OverrideClass_RecordStatus` | String |  |  |
| 8 | `EB.OVCL.CURR.NO` | `OverrideClass_CurrNo` | String |  |  |
| 9 | `EB.OVCL.INPUTTER` | `OverrideClass_Inputter` |  |  |  |
| 10 | `EB.OVCL.DATE.TIME` | `OverrideClass_DateTime` |  |  |  |
| 11 | `EB.OVCL.AUTHORISER` | `OverrideClass_Authoriser` | String |  |  |
| 12 | `EB.OVCL.CO.CODE` | `OverrideClass_CoCode` | String |  |  |
| 13 | `EB.OVCL.DEPT.CODE` | `OverrideClass_DeptCode` | String |  |  |
| 14 | `EB.OVCL.AUDITOR.CODE` | `OverrideClass_AuditorCode` | String |  |  |
| 15 | `EB.OVCL.AUDIT.DATE.TIME` | `OverrideClass_AuditDateTime` | String |  |  |
