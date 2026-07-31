# AA.CRA.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AA.CRA.PARAMETER` in `AA_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CRA.RELATION.CODE` | `AaCraParameter_RelationCode` |  |  |  |
| 2 | `AA.CRA.RELATION.CRA.METHOD` | `AaCraParameter_RelationCraMethod` |  |  |  |
| 3 | `AA.CRA.NON.RELATION.CRA.METHOD` | `AaCraParameter_NonRelationCraMethod` | TField |  | Denotes if unrelated customer are allowed for pricing benefit. Values allowed are �Restricted/Null/Manual�. Option Null/Restricted indicates CRA customers can be added based on valid relation codes only.Non-related customer can also be included if option is set to �Manual�. |
| 4 | `AA.CRA.RESERVED.4` | `AaCraParameter_Reserved4` | TField |  |  |
| 5 | `AA.CRA.RESERVED.3` | `AaCraParameter_Reserved3` | TField |  |  |
| 6 | `AA.CRA.RESERVED.2` | `AaCraParameter_Reserved2` | TField |  |  |
| 7 | `AA.CRA.RESERVED.1` | `AaCraParameter_Reserved1` | TField |  |  |
| 8 | `AA.CRA.RECORD.STATUS` | `AaCraParameter_RecordStatus` | String |  |  |
| 9 | `AA.CRA.CURR.NO` | `AaCraParameter_CurrNo` | String |  |  |
| 10 | `AA.CRA.INPUTTER` | `AaCraParameter_Inputter` |  |  |  |
| 11 | `AA.CRA.DATE.TIME` | `AaCraParameter_DateTime` |  |  |  |
| 12 | `AA.CRA.AUTHORISER` | `AaCraParameter_Authoriser` | String |  |  |
| 13 | `AA.CRA.CO.CODE` | `AaCraParameter_CoCode` | String |  |  |
| 14 | `AA.CRA.DEPT.CODE` | `AaCraParameter_DeptCode` | String |  |  |
| 15 | `AA.CRA.AUDITOR.CODE` | `AaCraParameter_AuditorCode` | String |  |  |
| 16 | `AA.CRA.AUDIT.DATE.TIME` | `AaCraParameter_AuditDateTime` | String |  |  |
