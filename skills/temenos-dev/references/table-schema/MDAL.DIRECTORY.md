# MDAL.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.MDAL.DIRECTORY` in `SE_MDAReferenceDirectory.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDALA.FIELD.NAME` | `MdalDirectory_FieldName` |  |  |  |
| 2 | `MDALA.FIELD.VALUE` | `MdalDirectory_FieldValue` |  |  |  |
| 3 | `MDALA.RECORD.STATUS` | `MdalDirectory_RecordStatus` | String |  |  |
| 4 | `MDALA.CURR.NO` | `MdalDirectory_CurrNo` | String |  |  |
| 5 | `MDALA.INPUTTER` | `MdalDirectory_Inputter` |  |  |  |
| 6 | `MDALA.DATE.TIME` | `MdalDirectory_DateTime` |  |  |  |
| 7 | `MDALA.AUTHORISER` | `MdalDirectory_Authoriser` | String |  |  |
| 8 | `MDALA.CO.CODE` | `MdalDirectory_CoCode` | String |  |  |
| 9 | `MDALA.DEPT.CODE` | `MdalDirectory_DeptCode` | String |  |  |
| 10 | `MDALA.AUDITOR.CODE` | `MdalDirectory_AuditorCode` | String |  |  |
| 11 | `MDALA.AUDIT.DATE.TIME` | `MdalDirectory_AuditDateTime` | String |  |  |
