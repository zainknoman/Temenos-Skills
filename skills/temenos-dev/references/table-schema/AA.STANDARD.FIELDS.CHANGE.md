# AA.STANDARD.FIELDS.CHANGE — Table Schema

> Source: `INSERTS/I_F.AA.STANDARD.FIELDS.CHANGE` in `AA_ProductFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SFC.DESCRIPTION` | `AaStandardFieldsChange_Description` |  |  |  |
| 2 | `AA.SFC.STANDARD.FIELD.TYPE` | `AaStandardFieldsChange_StandardFieldType` |  |  |  |
| 3 | `AA.SFC.T24.RELEASE` | `AaStandardFieldsChange_T24Release` | TField |  | Holds the release information of the AA.STANDARD.FIELDS.CHANGE record. Validation Rules: 1. Allows up to three characters. 2. The RELEASE must be in 'Rnn' (e.g. R18) |
| 4 | `AA.SFC.VERIFIED` | `AaStandardFieldsChange_Verified` | TField |  | System maintained field. It will be auto populated with YES after verifying the record. |
| 5 | `AA.SFC.RESERVED.5` | `AaStandardFieldsChange_Reserved5` | TField |  |  |
| 6 | `AA.SFC.RESERVED.4` | `AaStandardFieldsChange_Reserved4` | TField |  |  |
| 7 | `AA.SFC.RESERVED.3` | `AaStandardFieldsChange_Reserved3` | TField |  |  |
| 8 | `AA.SFC.RESERVED.2` | `AaStandardFieldsChange_Reserved2` | TField |  |  |
| 9 | `AA.SFC.RESERVED.1` | `AaStandardFieldsChange_Reserved1` | TField |  |  |
| 10 | `AA.SFC.RECORD.STATUS` | `AaStandardFieldsChange_RecordStatus` | String |  |  |
| 11 | `AA.SFC.CURR.NO` | `AaStandardFieldsChange_CurrNo` | String |  |  |
| 12 | `AA.SFC.INPUTTER` | `AaStandardFieldsChange_Inputter` |  |  |  |
| 13 | `AA.SFC.DATE.TIME` | `AaStandardFieldsChange_DateTime` |  |  |  |
| 14 | `AA.SFC.AUTHORISER` | `AaStandardFieldsChange_Authoriser` | String |  |  |
| 15 | `AA.SFC.CO.CODE` | `AaStandardFieldsChange_CoCode` | String |  |  |
| 16 | `AA.SFC.DEPT.CODE` | `AaStandardFieldsChange_DeptCode` | String |  |  |
| 17 | `AA.SFC.AUDITOR.CODE` | `AaStandardFieldsChange_AuditorCode` | String |  |  |
| 18 | `AA.SFC.AUDIT.DATE.TIME` | `AaStandardFieldsChange_AuditDateTime` | String |  |  |
