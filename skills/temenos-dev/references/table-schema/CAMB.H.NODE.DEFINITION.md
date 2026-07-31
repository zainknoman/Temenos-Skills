# CAMB.H.NODE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.CAMB.H.NODE.DEFINITION` in `CACBRT_CreditBureau.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NOD.DEF.DESCRIPTION` | `CambHNodeDefinition_Description` |  |  |  |
| 2 | `NOD.DEF.FILE.NAME` | `CambHNodeDefinition_FileName` | TField |  |  |
| 3 | `NOD.DEF.FIELD.NAMES` | `CambHNodeDefinition_FieldNames` |  |  |  |
| 4 | `NOD.DEF.NODE.VALUES` | `CambHNodeDefinition_NodeValues` |  |  |  |
| 5 | `NOD.DEF.HEADER.TAG` | `CambHNodeDefinition_HeaderTag` | TField |  |  |
| 6 | `NOD.DEF.SPLIT.TAG` | `CambHNodeDefinition_SplitTag` | TField |  |  |
| 7 | `NOD.DEF.RECORD.STATUS` | `CambHNodeDefinition_RecordStatus` | String |  |  |
| 8 | `NOD.DEF.CURR.NO` | `CambHNodeDefinition_CurrNo` | String |  |  |
| 9 | `NOD.DEF.INPUTTER` | `CambHNodeDefinition_Inputter` |  |  |  |
| 10 | `NOD.DEF.DATE.TIME` | `CambHNodeDefinition_DateTime` |  |  |  |
| 11 | `NOD.DEF.AUTHORISER` | `CambHNodeDefinition_Authoriser` | String |  |  |
| 12 | `NOD.DEF.CO.CODE` | `CambHNodeDefinition_CoCode` | String |  |  |
| 13 | `NOD.DEF.DEPT.CODE` | `CambHNodeDefinition_DeptCode` | String |  |  |
| 14 | `NOD.DEF.AUDITOR.CODE` | `CambHNodeDefinition_AuditorCode` | String |  |  |
| 15 | `NOD.DEF.AUDIT.DATE.TIME` | `CambHNodeDefinition_AuditDateTime` | String |  |  |
