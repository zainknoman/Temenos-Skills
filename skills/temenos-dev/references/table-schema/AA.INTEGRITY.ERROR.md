# AA.INTEGRITY.ERROR — Table Schema

> Source: `INSERTS/I_F.AA.INTEGRITY.ERROR` in `AA_Util.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.IE.DESCRIPTION` | `AaIntegrityError_Description` |  |  |  |
| 2 | `AA.IE.INTEGRITY.ERROR` | `AaIntegrityError_IntegrityError` | TField |  | Used to store the integrity error. |
| 3 | `AA.IE.TABLE.NAME` | `AaIntegrityError_TableName` |  |  |  |
| 4 | `AA.IE.FIELD.NAME` | `AaIntegrityError_FieldName` |  |  |  |
| 5 | `AA.IE.FIELD.MVPOSITION` | `AaIntegrityError_FieldMvposition` |  |  |  |
| 6 | `AA.IE.FIELD.SVPOSITION` | `AaIntegrityError_FieldSvposition` |  |  |  |
| 7 | `AA.IE.FIELD.VALUE` | `AaIntegrityError_FieldValue` |  |  |  |
| 8 | `AA.IE.RESERVED6` | `AaIntegrityError_Reserved6` |  |  |  |
| 9 | `AA.IE.RESERVED5` | `AaIntegrityError_Reserved5` |  |  |  |
| 10 | `AA.IE.RESERVED4` | `AaIntegrityError_Reserved4` |  |  |  |
| 11 | `AA.IE.RESERVED3` | `AaIntegrityError_Reserved3` |  |  |  |
| 12 | `AA.IE.RESERVED2` | `AaIntegrityError_Reserved2` |  |  |  |
| 13 | `AA.IE.RECORD.STATUS` | `AaIntegrityError_RecordStatus` | String |  |  |
| 14 | `AA.IE.CURR.NO` | `AaIntegrityError_CurrNo` | String |  |  |
| 15 | `AA.IE.INPUTTER` | `AaIntegrityError_Inputter` |  |  |  |
| 16 | `AA.IE.DATE.TIME` | `AaIntegrityError_DateTime` |  |  |  |
| 17 | `AA.IE.AUTHORISER` | `AaIntegrityError_Authoriser` | String |  |  |
| 18 | `AA.IE.CO.CODE` | `AaIntegrityError_CoCode` | String |  |  |
| 19 | `AA.IE.DEPT.CODE` | `AaIntegrityError_DeptCode` | String |  |  |
| 20 | `AA.IE.AUDITOR.CODE` | `AaIntegrityError_AuditorCode` | String |  |  |
| 21 | `AA.IE.AUDIT.DATE.TIME` | `AaIntegrityError_AuditDateTime` | String |  |  |
