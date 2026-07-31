# ER.MATCHING.CONDITION — Table Schema

> Source: `INSERTS/I_F.ER.MATCHING.CONDITION` in `ER_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ERMC.MATCHING.FIELD` | `ErMatchingCondition_MatchingField` |  |  |  |
| 2 | `ERMC.MATCHING.WITH.FIELD` | `ErMatchingCondition_MatchingWithField` |  |  |  |
| 3 | `ERMC.MATCHING.FIELD.API` | `ErMatchingCondition_MatchingFieldApi` |  |  |  |
| 4 | `ERMC.TOLERANCE` | `ErMatchingCondition_Tolerance` |  |  |  |
| 5 | `ERMC.AUTO.PART.MATCH` | `ErMatchingCondition_AutoPartMatch` |  |  |  |
| 6 | `ERMC.DESCRIPTION` | `ErMatchingCondition_Description` | TField |  | Capture a description of the Matching Condition. The value for this field is a free-text with the maximum length of 70. |
| 7 | `ERMC.RESERVED.4` | `ErMatchingCondition_Reserved4` | TField |  | This field is reserved for future use. |
| 8 | `ERMC.RESERVED.3` | `ErMatchingCondition_Reserved3` | TField |  | This field is reserved for future use. |
| 9 | `ERMC.RESERVED.2` | `ErMatchingCondition_Reserved2` | TField |  | This field is reserved for future use. |
| 10 | `ERMC.RESERVED.1` | `ErMatchingCondition_Reserved1` | TField |  | This field is reserved for future use. |
| 11 | `ERMC.LOCAL.REF` | `ErMatchingCondition_LocalRef` |  |  |  |
| 12 | `ERMC.OVERRIDE` | `ErMatchingCondition_Override` |  |  |  |
| 13 | `ERMC.RECORD.STATUS` | `ErMatchingCondition_RecordStatus` | String |  |  |
| 14 | `ERMC.CURR.NO` | `ErMatchingCondition_CurrNo` | String |  |  |
| 15 | `ERMC.INPUTTER` | `ErMatchingCondition_Inputter` |  |  |  |
| 16 | `ERMC.DATE.TIME` | `ErMatchingCondition_DateTime` |  |  |  |
| 17 | `ERMC.AUTHORISER` | `ErMatchingCondition_Authoriser` | String |  |  |
| 18 | `ERMC.CO.CODE` | `ErMatchingCondition_CoCode` | String |  |  |
| 19 | `ERMC.DEPT.CODE` | `ErMatchingCondition_DeptCode` | String |  |  |
| 20 | `ERMC.AUDITOR.CODE` | `ErMatchingCondition_AuditorCode` | String |  |  |
| 21 | `ERMC.AUDIT.DATE.TIME` | `ErMatchingCondition_AuditDateTime` | String |  |  |
