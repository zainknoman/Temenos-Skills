# OA.STATUS.RULES — Table Schema

> Source: `INSERTS/I_F.OA.STATUS.RULES` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.SR.DESCRIPTION` | `OaStatusRules_Description` |  |  |  |
| 2 | `OA.SR.FULL.DESCRIPTION` | `OaStatusRules_FullDescription` |  |  |  |
| 3 | `OA.SR.RESERVED.14` | `OaStatusRules_Reserved14` | TField |  |  |
| 4 | `OA.SR.RESERVED.13` | `OaStatusRules_Reserved13` | TField |  |  |
| 5 | `OA.SR.RESERVED.12` | `OaStatusRules_Reserved12` | TField |  |  |
| 6 | `OA.SR.RESERVED.11` | `OaStatusRules_Reserved11` | TField |  |  |
| 7 | `OA.SR.RESERVED.10` | `OaStatusRules_Reserved10` | TField |  |  |
| 8 | `OA.SR.RESERVED.9` | `OaStatusRules_Reserved9` | TField |  |  |
| 9 | `OA.SR.RESERVED.8` | `OaStatusRules_Reserved8` | TField |  |  |
| 10 | `OA.SR.RULE.DESCRIPTION` | `OaStatusRules_RuleDescription` |  |  |  |
| 11 | `OA.SR.RULE` | `OaStatusRules_Rule` |  |  |  |
| 12 | `OA.SR.RESERVED.7` | `OaStatusRules_Reserved7` |  |  |  |
| 13 | `OA.SR.TRUE.RESULT` | `OaStatusRules_TrueResult` |  |  |  |
| 14 | `OA.SR.RESERVED.6` | `OaStatusRules_Reserved6` | TField |  |  |
| 15 | `OA.SR.RESERVED.5` | `OaStatusRules_Reserved5` | TField |  |  |
| 16 | `OA.SR.RESERVED.4` | `OaStatusRules_Reserved4` | TField |  |  |
| 17 | `OA.SR.RESERVED.3` | `OaStatusRules_Reserved3` | TField |  |  |
| 18 | `OA.SR.RESERVED.2` | `OaStatusRules_Reserved2` | TField |  |  |
| 19 | `OA.SR.RESERVED.1` | `OaStatusRules_Reserved1` | TField |  |  |
| 20 | `OA.SR.LOCAL.REF` | `OaStatusRules_LocalRef` |  |  |  |
| 21 | `OA.SR.OVERRIDE` | `OaStatusRules_Override` |  |  |  |
| 22 | `OA.SR.RECORD.STATUS` | `OaStatusRules_RecordStatus` | String |  |  |
| 23 | `OA.SR.CURR.NO` | `OaStatusRules_CurrNo` | String |  |  |
| 24 | `OA.SR.INPUTTER` | `OaStatusRules_Inputter` |  |  |  |
| 25 | `OA.SR.DATE.TIME` | `OaStatusRules_DateTime` |  |  |  |
| 26 | `OA.SR.AUTHORISER` | `OaStatusRules_Authoriser` | String |  |  |
| 27 | `OA.SR.CO.CODE` | `OaStatusRules_CoCode` | String |  |  |
| 28 | `OA.SR.DEPT.CODE` | `OaStatusRules_DeptCode` | String |  |  |
| 29 | `OA.SR.AUDITOR.CODE` | `OaStatusRules_AuditorCode` | String |  |  |
| 30 | `OA.SR.AUDIT.DATE.TIME` | `OaStatusRules_AuditDateTime` | String |  |  |
