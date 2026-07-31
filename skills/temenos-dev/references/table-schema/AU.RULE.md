# AU.RULE — Table Schema

> Source: `INSERTS/I_F.AU.RULE` in `AU_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AU.RUL.APPLICATION` | `AuRule_Application` | TField |  | Application to which AU rules applies Must be valid T24 application |
| 2 | `AU.RUL.FIELD` | `AuRule_Field` |  |  |  |
| 3 | `AU.RUL.OPERAND` | `AuRule_Operand` |  |  |  |
| 4 | `AU.RUL.VALUE` | `AuRule_Value` |  |  |  |
| 5 | `AU.RUL.VALUE.START` | `AuRule_ValueStart` |  |  |  |
| 6 | `AU.RUL.VALUE.END` | `AuRule_ValueEnd` |  |  |  |
| 7 | `AU.RUL.CONV.RTN` | `AuRule_ConvRtn` |  |  |  |
| 8 | `AU.RUL.LOCAL.ROUTINE` | `AuRule_LocalRoutine` | TField |  | A field to provide a local routine which can be used instead of the decision fields |
| 9 | `AU.RUL.RESERVED.8` | `AuRule_Reserved8` | TField |  |  |
| 10 | `AU.RUL.RESERVED.7` | `AuRule_Reserved7` | TField |  |  |
| 11 | `AU.RUL.RESERVED.6` | `AuRule_Reserved6` | TField |  |  |
| 12 | `AU.RUL.RESERVED.5` | `AuRule_Reserved5` | TField |  |  |
| 13 | `AU.RUL.RESERVED.4` | `AuRule_Reserved4` | TField |  |  |
| 14 | `AU.RUL.RESERVED.3` | `AuRule_Reserved3` | TField |  |  |
| 15 | `AU.RUL.LOCAL.REF` | `AuRule_LocalRef` |  |  |  |
| 16 | `AU.RUL.OVERRIDE` | `AuRule_Override` |  |  |  |
| 17 | `AU.RUL.RECORD.STATUS` | `AuRule_RecordStatus` | String |  |  |
| 18 | `AU.RUL.CURR.NO` | `AuRule_CurrNo` | String |  |  |
| 19 | `AU.RUL.INPUTTER` | `AuRule_Inputter` |  |  |  |
| 20 | `AU.RUL.DATE.TIME` | `AuRule_DateTime` |  |  |  |
| 21 | `AU.RUL.AUTHORISER` | `AuRule_Authoriser` | String |  |  |
| 22 | `AU.RUL.CO.CODE` | `AuRule_CoCode` | String |  |  |
| 23 | `AU.RUL.DEPT.CODE` | `AuRule_DeptCode` | String |  |  |
| 24 | `AU.RUL.AUDITOR.CODE` | `AuRule_AuditorCode` | String |  |  |
| 25 | `AU.RUL.AUDIT.DATE.TIME` | `AuRule_AuditDateTime` | String |  |  |
