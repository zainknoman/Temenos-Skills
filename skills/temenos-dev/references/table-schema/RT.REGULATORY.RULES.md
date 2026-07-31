# RT.REGULATORY.RULES — Table Schema

> Source: `INSERTS/I_F.RT.REGULATORY.RULES` in `RT_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RTRL.DESC` | `RtRegulatoryRules_Desc` |  |  |  |
| 2 | `RTRL.BASE.ID.TABLE` | `RtRegulatoryRules_BaseIdTable` | TField | Yes | This field holds the base table that is used by the process. Validation Rules: Mandatory Input Should be a valid record in PGM.FILE |
| 3 | `RTRL.RULE.TYPE` | `RtRegulatoryRules_RuleType` |  |  |  |
| 4 | `RTRL.RULE.NUM` | `RtRegulatoryRules_RuleNum` |  |  |  |
| 5 | `RTRL.RULE.API` | `RtRegulatoryRules_RuleApi` |  |  |  |
| 6 | `RTRL.RULE.VERIFN` | `RtRegulatoryRules_RuleVerifn` |  |  |  |
| 7 | `RTRL.RULE.FIELD` | `RtRegulatoryRules_RuleField` |  |  |  |
| 8 | `RTRL.RULE.OPERAND` | `RtRegulatoryRules_RuleOperand` |  |  |  |
| 9 | `RTRL.RULE.VALUE` | `RtRegulatoryRules_RuleValue` |  |  |  |
| 10 | `RTRL.RULE.RESULT` | `RtRegulatoryRules_RuleResult` |  |  |  |
| 11 | `RTRL.RETURN.RESULT` | `RtRegulatoryRules_ReturnResult` |  |  |  |
| 12 | `RTRL.RL.RESERVED.15` | `RtRegulatoryRules_RlReserved15` |  |  |  |
| 13 | `RTRL.RL.RESERVED.14` | `RtRegulatoryRules_RlReserved14` |  |  |  |
| 14 | `RTRL.RL.RESERVED.13` | `RtRegulatoryRules_RlReserved13` |  |  |  |
| 15 | `RTRL.RL.RESERVED.12` | `RtRegulatoryRules_RlReserved12` |  |  |  |
| 16 | `RTRL.RL.RESERVED.11` | `RtRegulatoryRules_RlReserved11` |  |  |  |
| 17 | `RTRL.RL.RESERVED.10` | `RtRegulatoryRules_RlReserved10` |  |  |  |
| 18 | `RTRL.RL.RESERVED.09` | `RtRegulatoryRules_RlReserved09` |  |  |  |
| 19 | `RTRL.RL.RESERVED.08` | `RtRegulatoryRules_RlReserved08` |  |  |  |
| 20 | `RTRL.RL.RESERVED.07` | `RtRegulatoryRules_RlReserved07` |  |  |  |
| 21 | `RTRL.RL.RESERVED.06` | `RtRegulatoryRules_RlReserved06` |  |  |  |
| 22 | `RTRL.RL.RESERVED.05` | `RtRegulatoryRules_RlReserved05` |  |  |  |
| 23 | `RTRL.RL.RESERVED.04` | `RtRegulatoryRules_RlReserved04` |  |  |  |
| 24 | `RTRL.RL.RESERVED.03` | `RtRegulatoryRules_RlReserved03` |  |  |  |
| 25 | `RTRL.RL.RESERVED.02` | `RtRegulatoryRules_RlReserved02` |  |  |  |
| 26 | `RTRL.RL.RESERVED.01` | `RtRegulatoryRules_RlReserved01` |  |  |  |
| 27 | `RTRL.SYS.LINKED.APP` | `RtRegulatoryRules_SysLinkedApp` |  |  |  |
| 28 | `RTRL.USER.LINKED.APP` | `RtRegulatoryRules_UserLinkedApp` |  |  |  |
| 29 | `RTRL.BASE.TABLE.KEY` | `RtRegulatoryRules_BaseTableKey` |  |  |  |
| 30 | `RTRL.RESERVED.15` | `RtRegulatoryRules_Reserved15` | TField |  |  |
| 31 | `RTRL.RESERVED.14` | `RtRegulatoryRules_Reserved14` | TField |  |  |
| 32 | `RTRL.RESERVED.13` | `RtRegulatoryRules_Reserved13` | TField |  |  |
| 33 | `RTRL.RESERVED.12` | `RtRegulatoryRules_Reserved12` | TField |  |  |
| 34 | `RTRL.RESERVED.11` | `RtRegulatoryRules_Reserved11` | TField |  |  |
| 35 | `RTRL.RESERVED.10` | `RtRegulatoryRules_Reserved10` | TField |  |  |
| 36 | `RTRL.RESERVED.09` | `RtRegulatoryRules_Reserved09` | TField |  |  |
| 37 | `RTRL.RESERVED.08` | `RtRegulatoryRules_Reserved08` | TField |  |  |
| 38 | `RTRL.RESERVED.07` | `RtRegulatoryRules_Reserved07` | TField |  |  |
| 39 | `RTRL.RESERVED.06` | `RtRegulatoryRules_Reserved06` | TField |  |  |
| 40 | `RTRL.RESERVED.05` | `RtRegulatoryRules_Reserved05` | TField |  |  |
| 41 | `RTRL.RESERVED.04` | `RtRegulatoryRules_Reserved04` | TField |  |  |
| 42 | `RTRL.RESERVED.03` | `RtRegulatoryRules_Reserved03` | TField |  |  |
| 43 | `RTRL.RESERVED.02` | `RtRegulatoryRules_Reserved02` | TField |  |  |
| 44 | `RTRL.RESERVED.01` | `RtRegulatoryRules_Reserved01` | TField |  |  |
| 45 | `RTRL.LOCAL.REF` | `RtRegulatoryRules_LocalRef` |  |  |  |
| 46 | `RTRL.OVERRIDE` | `RtRegulatoryRules_Override` |  |  |  |
| 47 | `RTRL.RECORD.STATUS` | `RtRegulatoryRules_RecordStatus` | String |  |  |
| 48 | `RTRL.CURR.NO` | `RtRegulatoryRules_CurrNo` | String |  |  |
| 49 | `RTRL.INPUTTER` | `RtRegulatoryRules_Inputter` |  |  |  |
| 50 | `RTRL.DATE.TIME` | `RtRegulatoryRules_DateTime` |  |  |  |
| 51 | `RTRL.AUTHORISER` | `RtRegulatoryRules_Authoriser` | String |  |  |
| 52 | `RTRL.CO.CODE` | `RtRegulatoryRules_CoCode` | String |  |  |
| 53 | `RTRL.DEPT.CODE` | `RtRegulatoryRules_DeptCode` | String |  |  |
| 54 | `RTRL.AUDITOR.CODE` | `RtRegulatoryRules_AuditorCode` | String |  |  |
| 55 | `RTRL.AUDIT.DATE.TIME` | `RtRegulatoryRules_AuditDateTime` | String |  |  |
