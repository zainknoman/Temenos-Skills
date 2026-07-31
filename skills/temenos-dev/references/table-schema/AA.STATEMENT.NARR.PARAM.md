# AA.STATEMENT.NARR.PARAM — Table Schema

> Source: `INSERTS/I_F.AA.STATEMENT.NARR.PARAM` in `AA_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SNP.APPLICATION` | `AaStatementNarrParam_Application` | TField |  | Application for which narrative formats are defined on this parameter record. This is the application raising the accounting entry. |
| 2 | `AA.SNP.FIELD` | `AaStatementNarrParam_Field` |  |  |  |
| 3 | `AA.SNP.OPERAND` | `AaStatementNarrParam_Operand` |  |  |  |
| 4 | `AA.SNP.VALUE` | `AaStatementNarrParam_Value` |  |  |  |
| 5 | `AA.SNP.FIELD.IDX` | `AaStatementNarrParam_FieldIdx` |  |  |  |
| 6 | `AA.SNP.FORMAT` | `AaStatementNarrParam_Format` |  |  |  |
| 7 | `AA.SNP.APP.FIELD` | `AaStatementNarrParam_AppField` | TField |  | This field defines the application field. |
| 8 | `AA.SNP.APP.FIELD.IDX` | `AaStatementNarrParam_AppFieldIdx` | TField |  | This field defines the field index of the app field. |
| 9 | `AA.SNP.APP.READ.HISTORY` | `AaStatementNarrParam_AppReadHistory` | TField |  | This field defines the application read history of the app field. |
| 10 | `AA.SNP.APP.VERSION` | `AaStatementNarrParam_AppVersion` | TField |  | This field defines the version attached to the application. |
| 11 | `AA.SNP.RESERVED.2` | `AaStatementNarrParam_Reserved2` | TField |  |  |
| 12 | `AA.SNP.RESERVED.3` | `AaStatementNarrParam_Reserved3` | TField |  |  |
| 13 | `AA.SNP.RESERVED.4` | `AaStatementNarrParam_Reserved4` | TField |  |  |
| 14 | `AA.SNP.RESERVED.5` | `AaStatementNarrParam_Reserved5` | TField |  |  |
| 15 | `AA.SNP.RESERVED.6` | `AaStatementNarrParam_Reserved6` | TField |  |  |
| 16 | `AA.SNP.RESERVED.7` | `AaStatementNarrParam_Reserved7` | TField |  |  |
| 17 | `AA.SNP.RESERVED.8` | `AaStatementNarrParam_Reserved8` | TField |  |  |
| 18 | `AA.SNP.RESERVED.9` | `AaStatementNarrParam_Reserved9` | TField |  |  |
| 19 | `AA.SNP.LOCAL.REF` | `AaStatementNarrParam_LocalRef` |  |  |  |
| 20 | `AA.SNP.OVERRIDE` | `AaStatementNarrParam_Override` |  |  |  |
| 21 | `AA.SNP.RECORD.STATUS` | `AaStatementNarrParam_RecordStatus` | String |  |  |
| 22 | `AA.SNP.CURR.NO` | `AaStatementNarrParam_CurrNo` | String |  |  |
| 23 | `AA.SNP.INPUTTER` | `AaStatementNarrParam_Inputter` |  |  |  |
| 24 | `AA.SNP.DATE.TIME` | `AaStatementNarrParam_DateTime` |  |  |  |
| 25 | `AA.SNP.AUTHORISER` | `AaStatementNarrParam_Authoriser` | String |  |  |
| 26 | `AA.SNP.CO.CODE` | `AaStatementNarrParam_CoCode` | String |  |  |
| 27 | `AA.SNP.DEPT.CODE` | `AaStatementNarrParam_DeptCode` | String |  |  |
| 28 | `AA.SNP.AUDITOR.CODE` | `AaStatementNarrParam_AuditorCode` | String |  |  |
| 29 | `AA.SNP.AUDIT.DATE.TIME` | `AaStatementNarrParam_AuditDateTime` | String |  |  |
