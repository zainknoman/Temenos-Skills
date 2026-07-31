# CRS.BASE.MANUAL.UPDATE — Table Schema

> Source: `INSERTS/I_F.CRS.BASE.MANUAL.UPDATE` in `CE_CrsReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CE.BMU.ACTION` | `CrsBaseManualUpdate_Action` | TField |  | The field is used to identify the action to be performed on the base. NEW - will be used to add records to the base for clients missing from the base AMEND - will be for amending the records in the base. DELETE - will be for deleting the entire record from the base. DELETE-AMEND - will be for changing the OECD value alone. Record will not be deleted For Amend and Delete the record should already exist in the base. Validation rules: NEW, AMEND, DELETE or DELETE-AMEND |
| 2 | `CE.BMU.FIELD.NAME` | `CrsBaseManualUpdate_FieldName` |  |  |  |
| 3 | `CE.BMU.FIELD.VALUE` | `CrsBaseManualUpdate_FieldValue` |  |  |  |
| 4 | `CE.BMU.FIELD.NAME.MV` | `CrsBaseManualUpdate_FieldNameMv` |  |  |  |
| 5 | `CE.BMU.FIELD.VALUE.MV` | `CrsBaseManualUpdate_FieldValueMv` |  |  |  |
| 6 | `CE.BMU.ASSOC.FIELD.NAME` | `CrsBaseManualUpdate_AssocFieldName` |  |  |  |
| 7 | `CE.BMU.ASSOC.FIELD.VAL` | `CrsBaseManualUpdate_AssocFieldVal` |  |  |  |
| 8 | `CE.BMU.FIELD.ACTION` | `CrsBaseManualUpdate_FieldAction` |  |  |  |
| 9 | `CE.BMU.OVERRIDE` | `CrsBaseManualUpdate_Override` |  |  |  |
| 10 | `CE.BMU.RECORD.STATUS` | `CrsBaseManualUpdate_RecordStatus` | String |  |  |
| 11 | `CE.BMU.CURR.NO` | `CrsBaseManualUpdate_CurrNo` | String |  |  |
| 12 | `CE.BMU.INPUTTER` | `CrsBaseManualUpdate_Inputter` |  |  |  |
| 13 | `CE.BMU.DATE.TIME` | `CrsBaseManualUpdate_DateTime` |  |  |  |
| 14 | `CE.BMU.AUTHORISER` | `CrsBaseManualUpdate_Authoriser` | String |  |  |
| 15 | `CE.BMU.CO.CODE` | `CrsBaseManualUpdate_CoCode` | String |  |  |
| 16 | `CE.BMU.DEPT.CODE` | `CrsBaseManualUpdate_DeptCode` | String |  |  |
| 17 | `CE.BMU.AUDITOR.CODE` | `CrsBaseManualUpdate_AuditorCode` | String |  |  |
| 18 | `CE.BMU.AUDIT.DATE.TIME` | `CrsBaseManualUpdate_AuditDateTime` | String |  |  |
