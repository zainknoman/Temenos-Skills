# MDAL.REFERENCE — Table Schema

> Source: `INSERTS/I_F.MDAL.REFERENCE` in `SE_MDAReferenceData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDALR.FIELD.NAME` | `MdalReference_FieldName` |  |  |  |
| 2 | `MDALR.FIELD.VALUE` | `MdalReference_FieldValue` |  |  |  |
| 3 | `MDALR.RECORD.STATUS` | `MdalReference_RecordStatus` | String |  |  |
| 4 | `MDALR.CURR.NO` | `MdalReference_CurrNo` | String |  |  |
| 5 | `MDALR.INPUTTER` | `MdalReference_Inputter` |  |  |  |
| 6 | `MDALR.DATE.TIME` | `MdalReference_DateTime` |  |  |  |
| 7 | `MDALR.AUTHORISER` | `MdalReference_Authoriser` | String |  |  |
| 8 | `MDALR.CO.CODE` | `MdalReference_CoCode` | String |  |  |
| 9 | `MDALR.DEPT.CODE` | `MdalReference_DeptCode` | String |  |  |
| 10 | `MDALR.AUDITOR.CODE` | `MdalReference_AuditorCode` | String |  |  |
| 11 | `MDALR.AUDIT.DATE.TIME` | `MdalReference_AuditDateTime` | String |  |  |
