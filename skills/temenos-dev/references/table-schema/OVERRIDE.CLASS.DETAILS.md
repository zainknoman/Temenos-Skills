# OVERRIDE.CLASS.DETAILS — Table Schema

> Source: `INSERTS/I_F.OVERRIDE.CLASS.DETAILS` in `EB_OverrideProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.OVCLD.DATA.DEF` | `OverrideClassDetails_DataDef` |  |  |  |
| 2 | `EB.OVCLD.CLASSIFICATION` | `OverrideClassDetails_Classification` |  |  |  |
| 3 | `EB.OVCLD.DATA.DEF.NO` | `OverrideClassDetails_DataDefNo` |  |  |  |
| 4 | `EB.OVCLD.COMPARISON` | `OverrideClassDetails_Comparison` |  |  |  |
| 5 | `EB.OVCLD.DATA.FROM` | `OverrideClassDetails_DataFrom` |  |  |  |
| 6 | `EB.OVCLD.DATA.TO` | `OverrideClassDetails_DataTo` |  |  |  |
| 7 | `EB.OVCLD.RESERVED.4` | `OverrideClassDetails_Reserved4` | TField |  |  |
| 8 | `EB.OVCLD.RESERVED.3` | `OverrideClassDetails_Reserved3` | TField |  |  |
| 9 | `EB.OVCLD.LOCAL.REF` | `OverrideClassDetails_LocalRef` |  |  |  |
| 10 | `EB.OVCLD.RESERVED.1` | `OverrideClassDetails_Reserved1` | TField |  |  |
| 11 | `EB.OVCLD.RECORD.STATUS` | `OverrideClassDetails_RecordStatus` | String |  |  |
| 12 | `EB.OVCLD.CURR.NO` | `OverrideClassDetails_CurrNo` | String |  |  |
| 13 | `EB.OVCLD.INPUTTER` | `OverrideClassDetails_Inputter` |  |  |  |
| 14 | `EB.OVCLD.DATE.TIME` | `OverrideClassDetails_DateTime` |  |  |  |
| 15 | `EB.OVCLD.AUTHORISER` | `OverrideClassDetails_Authoriser` | String |  |  |
| 16 | `EB.OVCLD.CO.CODE` | `OverrideClassDetails_CoCode` | String |  |  |
| 17 | `EB.OVCLD.DEPT.CODE` | `OverrideClassDetails_DeptCode` | String |  |  |
| 18 | `EB.OVCLD.AUDITOR.CODE` | `OverrideClassDetails_AuditorCode` | String |  |  |
| 19 | `EB.OVCLD.AUDIT.DATE.TIME` | `OverrideClassDetails_AuditDateTime` | String |  |  |
