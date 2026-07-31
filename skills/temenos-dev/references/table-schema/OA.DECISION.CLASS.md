# OA.DECISION.CLASS — Table Schema

> Source: `INSERTS/I_F.OA.DECISION.CLASS` in `OA_Decision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DC.DESCRIPTION` | `OaDecisionClass_Description` |  |  |  |
| 2 | `OA.DC.FULL.DESC` | `OaDecisionClass_FullDesc` |  |  |  |
| 3 | `OA.DC.TYPE` | `OaDecisionClass_Type` |  |  |  |
| 4 | `OA.DC.RESERVED.10` | `OaDecisionClass_Reserved10` | TField |  |  |
| 5 | `OA.DC.RESERVED.9` | `OaDecisionClass_Reserved9` | TField |  |  |
| 6 | `OA.DC.RESERVED.8` | `OaDecisionClass_Reserved8` | TField |  |  |
| 7 | `OA.DC.RESERVED.7` | `OaDecisionClass_Reserved7` | TField |  |  |
| 8 | `OA.DC.RESERVED.6` | `OaDecisionClass_Reserved6` | TField |  |  |
| 9 | `OA.DC.RESERVED.5` | `OaDecisionClass_Reserved5` | TField |  |  |
| 10 | `OA.DC.RESERVED.4` | `OaDecisionClass_Reserved4` | TField |  |  |
| 11 | `OA.DC.RESERVED.3` | `OaDecisionClass_Reserved3` | TField |  |  |
| 12 | `OA.DC.RESERVED.2` | `OaDecisionClass_Reserved2` | TField |  |  |
| 13 | `OA.DC.RESERVED.1` | `OaDecisionClass_Reserved1` | TField |  |  |
| 14 | `OA.DC.LOCAL.REF` | `OaDecisionClass_LocalRef` |  |  |  |
| 15 | `OA.DC.OVERRIDE` | `OaDecisionClass_Override` |  |  |  |
| 16 | `OA.DC.RECORD.STATUS` | `OaDecisionClass_RecordStatus` | String |  |  |
| 17 | `OA.DC.CURR.NO` | `OaDecisionClass_CurrNo` | String |  |  |
| 18 | `OA.DC.INPUTTER` | `OaDecisionClass_Inputter` |  |  |  |
| 19 | `OA.DC.DATE.TIME` | `OaDecisionClass_DateTime` |  |  |  |
| 20 | `OA.DC.AUTHORISER` | `OaDecisionClass_Authoriser` | String |  |  |
| 21 | `OA.DC.CO.CODE` | `OaDecisionClass_CoCode` | String |  |  |
| 22 | `OA.DC.DEPT.CODE` | `OaDecisionClass_DeptCode` | String |  |  |
| 23 | `OA.DC.AUDITOR.CODE` | `OaDecisionClass_AuditorCode` | String |  |  |
| 24 | `OA.DC.AUDIT.DATE.TIME` | `OaDecisionClass_AuditDateTime` | String |  |  |
