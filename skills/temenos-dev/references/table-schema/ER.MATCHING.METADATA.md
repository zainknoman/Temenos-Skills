# ER.MATCHING.METADATA — Table Schema

> Source: `INSERTS/I_F.ER.MATCHING.METADATA` in `ER_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ERMD.MATCHING.FIELD` | `ErMatchingMetadata_MatchingField` |  |  |  |
| 2 | `ERMD.REQUIRED` | `ErMatchingMetadata_Required` |  |  |  |
| 3 | `ERMD.MATCH.FIELD.LOC.API` | `ErMatchingMetadata_MatchFieldLocApi` |  |  |  |
| 4 | `ERMD.LOCAL.REF` | `ErMatchingMetadata_LocalRef` |  |  |  |
| 5 | `ERMD.OVERRIDE` | `ErMatchingMetadata_Override` |  |  |  |
| 6 | `ERMD.RECORD.STATUS` | `ErMatchingMetadata_RecordStatus` | String |  |  |
| 7 | `ERMD.CURR.NO` | `ErMatchingMetadata_CurrNo` | String |  |  |
| 8 | `ERMD.INPUTTER` | `ErMatchingMetadata_Inputter` |  |  |  |
| 9 | `ERMD.DATE.TIME` | `ErMatchingMetadata_DateTime` |  |  |  |
| 10 | `ERMD.AUTHORISER` | `ErMatchingMetadata_Authoriser` | String |  |  |
| 11 | `ERMD.CO.CODE` | `ErMatchingMetadata_CoCode` | String |  |  |
| 12 | `ERMD.DEPT.CODE` | `ErMatchingMetadata_DeptCode` | String |  |  |
| 13 | `ERMD.AUDITOR.CODE` | `ErMatchingMetadata_AuditorCode` | String |  |  |
| 14 | `ERMD.AUDIT.DATE.TIME` | `ErMatchingMetadata_AuditDateTime` | String |  |  |
