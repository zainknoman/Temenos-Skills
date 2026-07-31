# CM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CM.PARAMETER` in `CM_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CM.PAR.DAYS.TILL.ARCHIVE` | `CmParameter_DaysTillArchive` | N (Numeric) | Yes | This field holds number of days. It will be used as part of the end of day processing to remove any matured messages and or those that have a status of WOF(Write off file), and copy them from CM.MESSAGE to the history file. Validation Rules: 1-4 type N (Numeric) characters. (Mandatory input). |
| 2 | `CM.PAR.OWN.MATCH.ROUTINE` | `CmParameter_OwnMatchRoutine` | TField |  | This field is used to call any user defined SUBROUTINE / API's. This field will accept only valid subroutine that is previously defined by the user. |
| 3 | `CM.PAR.LOCAL.REF` | `CmParameter_LocalRef` |  |  |  |
| 4 | `CM.PAR.RESERVED8` | `CmParameter_Reserved8` | TField |  |  |
| 5 | `CM.PAR.RESERVED7` | `CmParameter_Reserved7` | TField |  |  |
| 6 | `CM.PAR.RESERVED6` | `CmParameter_Reserved6` | TField |  |  |
| 7 | `CM.PAR.RESERVED5` | `CmParameter_Reserved5` | TField |  |  |
| 8 | `CM.PAR.RESERVED4` | `CmParameter_Reserved4` | TField |  |  |
| 9 | `CM.PAR.RESERVED3` | `CmParameter_Reserved3` | TField |  |  |
| 10 | `CM.PAR.RESERVED2` | `CmParameter_Reserved2` | TField |  |  |
| 11 | `CM.PAR.OVERRIDE` | `CmParameter_Override` |  |  |  |
| 12 | `CM.PAR.RECORD.STATUS` | `CmParameter_RecordStatus` | String |  |  |
| 13 | `CM.PAR.CURR.NO` | `CmParameter_CurrNo` | String |  |  |
| 14 | `CM.PAR.INPUTTER` | `CmParameter_Inputter` |  |  |  |
| 15 | `CM.PAR.DATE.TIME` | `CmParameter_DateTime` |  |  |  |
| 16 | `CM.PAR.AUTHORISER` | `CmParameter_Authoriser` | String |  |  |
| 17 | `CM.PAR.CO.CODE` | `CmParameter_CoCode` | String |  |  |
| 18 | `CM.PAR.DEPT.CODE` | `CmParameter_DeptCode` | String |  |  |
| 19 | `CM.PAR.AUDITOR.CODE` | `CmParameter_AuditorCode` | String |  |  |
| 20 | `CM.PAR.AUDIT.DATE.TIME` | `CmParameter_AuditDateTime` | String |  |  |
