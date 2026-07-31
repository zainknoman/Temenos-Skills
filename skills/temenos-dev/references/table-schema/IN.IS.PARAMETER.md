# IN.IS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.IN.IS.PARAMETER` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.IS.PAR.LAST.UPDATE` | `InIsParameter_LastUpdate` | TField |  | Holds the last uploaded date of the IN.IBAN.STRUCTURE file. |
| 2 | `IN.IS.PAR.RESERVED.5` | `InIsParameter_Reserved5` | TField |  |  |
| 3 | `IN.IS.PAR.RESERVED.4` | `InIsParameter_Reserved4` | TField |  |  |
| 4 | `IN.IS.PAR.RESERVED.3` | `InIsParameter_Reserved3` | TField |  |  |
| 5 | `IN.IS.PAR.LOCAL.REF` | `InIsParameter_LocalRef` |  |  |  |
| 6 | `IN.IS.PAR.RESERVED.1` | `InIsParameter_Reserved1` | TField |  |  |
| 7 | `IN.IS.PAR.RECORD.STATUS` | `InIsParameter_RecordStatus` | String |  |  |
| 8 | `IN.IS.PAR.CURR.NO` | `InIsParameter_CurrNo` | String |  |  |
| 9 | `IN.IS.PAR.INPUTTER` | `InIsParameter_Inputter` |  |  |  |
| 10 | `IN.IS.PAR.DATE.TIME` | `InIsParameter_DateTime` |  |  |  |
| 11 | `IN.IS.PAR.AUTHORISER` | `InIsParameter_Authoriser` | String |  |  |
| 12 | `IN.IS.PAR.CO.CODE` | `InIsParameter_CoCode` | String |  |  |
| 13 | `IN.IS.PAR.DEPT.CODE` | `InIsParameter_DeptCode` | String |  |  |
| 14 | `IN.IS.PAR.AUDITOR.CODE` | `InIsParameter_AuditorCode` | String |  |  |
| 15 | `IN.IS.PAR.AUDIT.DATE.TIME` | `InIsParameter_AuditDateTime` | String |  |  |
