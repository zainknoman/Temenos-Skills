# FATCA.BASE.MANUAL.UPDATE — Table Schema

> Source: `INSERTS/I_F.FATCA.BASE.MANUAL.UPDATE` in `FE_FatcaReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FE.BMU.ACTION` | `FatcaBaseManualUpdate_Action` | TField |  | The field is used to identify the action to be performed on the base. NEW will be used to add records to the base for clients missing from the base; Amend will be for amending the records in the base; Delete will be for deleting the entire record from the base. For Amend and Delete the record should already exist in the base. Validation Rules: NEW, AMEND or DELETE. |
| 2 | `FE.BMU.FIELD.NAME` | `FatcaBaseManualUpdate_FieldName` |  |  |  |
| 3 | `FE.BMU.FIELD.VALUE` | `FatcaBaseManualUpdate_FieldValue` |  |  |  |
| 4 | `FE.BMU.FIELD.NAME.MV` | `FatcaBaseManualUpdate_FieldNameMv` |  |  |  |
| 5 | `FE.BMU.FIELD.VALUE.MV` | `FatcaBaseManualUpdate_FieldValueMv` |  |  |  |
| 6 | `FE.BMU.ASSOC.FIELD.NAME` | `FatcaBaseManualUpdate_AssocFieldName` |  |  |  |
| 7 | `FE.BMU.ASSOC.FIELD.VAL` | `FatcaBaseManualUpdate_AssocFieldVal` |  |  |  |
| 8 | `FE.BMU.FIELD.ACTION` | `FatcaBaseManualUpdate_FieldAction` |  |  |  |
| 9 | `FE.BMU.OVERRIDE` | `FatcaBaseManualUpdate_Override` |  |  |  |
| 10 | `FE.BMU.RECORD.STATUS` | `FatcaBaseManualUpdate_RecordStatus` | String |  |  |
| 11 | `FE.BMU.CURR.NO` | `FatcaBaseManualUpdate_CurrNo` | String |  |  |
| 12 | `FE.BMU.INPUTTER` | `FatcaBaseManualUpdate_Inputter` |  |  |  |
| 13 | `FE.BMU.DATE.TIME` | `FatcaBaseManualUpdate_DateTime` |  |  |  |
| 14 | `FE.BMU.AUTHORISER` | `FatcaBaseManualUpdate_Authoriser` | String |  |  |
| 15 | `FE.BMU.CO.CODE` | `FatcaBaseManualUpdate_CoCode` | String |  |  |
| 16 | `FE.BMU.DEPT.CODE` | `FatcaBaseManualUpdate_DeptCode` | String |  |  |
| 17 | `FE.BMU.AUDITOR.CODE` | `FatcaBaseManualUpdate_AuditorCode` | String |  |  |
| 18 | `FE.BMU.AUDIT.DATE.TIME` | `FatcaBaseManualUpdate_AuditDateTime` | String |  |  |
