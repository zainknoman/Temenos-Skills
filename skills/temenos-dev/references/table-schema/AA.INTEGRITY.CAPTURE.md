# AA.INTEGRITY.CAPTURE — Table Schema

> Source: `INSERTS/I_F.AA.INTEGRITY.CAPTURE` in `AA_Util.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.IC.INTEGRITY.CHECK` | `AaIntegrityCapture_IntegrityCheck` |  |  |  |
| 2 | `AA.IC.RESERVED7` | `AaIntegrityCapture_Reserved7` |  |  |  |
| 3 | `AA.IC.ARRANGEMENT.ID` | `AaIntegrityCapture_ArrangementId` |  |  |  |
| 4 | `AA.IC.ACCOUNT.ID` | `AaIntegrityCapture_AccountId` |  |  |  |
| 5 | `AA.IC.RESERVED2` | `AaIntegrityCapture_Reserved2` |  |  |  |
| 6 | `AA.IC.RESERVED1` | `AaIntegrityCapture_Reserved1` |  |  |  |
| 7 | `AA.IC.TABLE.NAME` | `AaIntegrityCapture_TableName` |  |  |  |
| 8 | `AA.IC.RECORD.ID` | `AaIntegrityCapture_RecordId` |  |  |  |
| 9 | `AA.IC.FIELD.NAME` | `AaIntegrityCapture_FieldName` |  |  |  |
| 10 | `AA.IC.FIELD.MVPOSITION` | `AaIntegrityCapture_FieldMvposition` |  |  |  |
| 11 | `AA.IC.FIELD.SVPOSITION` | `AaIntegrityCapture_FieldSvposition` |  |  |  |
| 12 | `AA.IC.FIELD.VALUE` | `AaIntegrityCapture_FieldValue` |  |  |  |
| 13 | `AA.IC.RESERVED6` | `AaIntegrityCapture_Reserved6` |  |  |  |
| 14 | `AA.IC.RESERVED5` | `AaIntegrityCapture_Reserved5` |  |  |  |
| 15 | `AA.IC.RESERVED4` | `AaIntegrityCapture_Reserved4` |  |  |  |
| 16 | `AA.IC.RESERVED3` | `AaIntegrityCapture_Reserved3` |  |  |  |
| 17 | `AA.IC.RESULT` | `AaIntegrityCapture_Result` |  |  |  |
| 18 | `AA.IC.RUN.STATUS` | `AaIntegrityCapture_RunStatus` | TField |  | This field will be defaulted to NEW. This field will be updated as PROCESSED after the record is picked up by the AA.INTEGRITY.CAPTURE.SERVICE |
| 19 | `AA.IC.RECORD.STATUS` | `AaIntegrityCapture_RecordStatus` | String |  |  |
| 20 | `AA.IC.CURR.NO` | `AaIntegrityCapture_CurrNo` | String |  |  |
| 21 | `AA.IC.INPUTTER` | `AaIntegrityCapture_Inputter` |  |  |  |
| 22 | `AA.IC.DATE.TIME` | `AaIntegrityCapture_DateTime` |  |  |  |
| 23 | `AA.IC.AUTHORISER` | `AaIntegrityCapture_Authoriser` | String |  |  |
| 24 | `AA.IC.CO.CODE` | `AaIntegrityCapture_CoCode` | String |  |  |
| 25 | `AA.IC.DEPT.CODE` | `AaIntegrityCapture_DeptCode` | String |  |  |
| 26 | `AA.IC.AUDITOR.CODE` | `AaIntegrityCapture_AuditorCode` | String |  |  |
| 27 | `AA.IC.AUDIT.DATE.TIME` | `AaIntegrityCapture_AuditDateTime` | String |  |  |
