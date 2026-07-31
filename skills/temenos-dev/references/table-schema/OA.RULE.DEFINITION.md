# OA.RULE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.OA.RULE.DEFINITION` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.RD.DESCRIPTION` | `OaRuleDefinition_Description` |  |  |  |
| 2 | `OA.RD.FULL.DESCRIPTION` | `OaRuleDefinition_FullDescription` |  |  |  |
| 3 | `OA.RD.RESERVED.14` | `OaRuleDefinition_Reserved14` | TField |  |  |
| 4 | `OA.RD.RESERVED.13` | `OaRuleDefinition_Reserved13` | TField |  |  |
| 5 | `OA.RD.RULE.NAME` | `OaRuleDefinition_RuleName` |  |  |  |
| 6 | `OA.RD.CONTEXT.TYPE` | `OaRuleDefinition_ContextType` |  |  |  |
| 7 | `OA.RD.CONTEXT` | `OaRuleDefinition_Context` |  |  |  |
| 8 | `OA.RD.CONTEXT.INSTANCE` | `OaRuleDefinition_ContextInstance` |  |  |  |
| 9 | `OA.RD.RULE.VARIABLE` | `OaRuleDefinition_RuleVariable` |  |  |  |
| 10 | `OA.RD.RESERVED.12` | `OaRuleDefinition_Reserved12` |  |  |  |
| 11 | `OA.RD.RESERVED.11` | `OaRuleDefinition_Reserved11` |  |  |  |
| 12 | `OA.RD.RESERVED.10` | `OaRuleDefinition_Reserved10` |  |  |  |
| 13 | `OA.RD.RESERVED.9` | `OaRuleDefinition_Reserved9` |  |  |  |
| 14 | `OA.RD.RULE.EXPRESSION` | `OaRuleDefinition_RuleExpression` |  |  |  |
| 15 | `OA.RD.RESERVED.8` | `OaRuleDefinition_Reserved8` |  |  |  |
| 16 | `OA.RD.RESERVED.7` | `OaRuleDefinition_Reserved7` | TField |  |  |
| 17 | `OA.RD.RESERVED.6` | `OaRuleDefinition_Reserved6` | TField |  |  |
| 18 | `OA.RD.CONSOLIDATE.EXPRESSION` | `OaRuleDefinition_ConsolidateExpression` |  |  |  |
| 19 | `OA.RD.DEVIATION.CALCULATOR` | `OaRuleDefinition_DeviationCalculator` | TField |  | The Deviation calculator would be in the form of arithmetic Expression. Where the Key words of the Rule either numbers or key words from the above Rule Expressions. For Example � MIN.AGE-AGE, (SALARY/MIN.SALARY)*100. |
| 20 | `OA.RD.RESERVED.4` | `OaRuleDefinition_Reserved4` | TField |  |  |
| 21 | `OA.RD.RESERVED.3` | `OaRuleDefinition_Reserved3` | TField |  |  |
| 22 | `OA.RD.RESERVED.2` | `OaRuleDefinition_Reserved2` | TField |  |  |
| 23 | `OA.RD.RESERVED.1` | `OaRuleDefinition_Reserved1` | TField |  |  |
| 24 | `OA.RD.LOCAL.REF` | `OaRuleDefinition_LocalRef` |  |  |  |
| 25 | `OA.RD.OVERRIDE` | `OaRuleDefinition_Override` |  |  |  |
| 26 | `OA.RD.RECORD.STATUS` | `OaRuleDefinition_RecordStatus` | String |  |  |
| 27 | `OA.RD.CURR.NO` | `OaRuleDefinition_CurrNo` | String |  |  |
| 28 | `OA.RD.INPUTTER` | `OaRuleDefinition_Inputter` |  |  |  |
| 29 | `OA.RD.DATE.TIME` | `OaRuleDefinition_DateTime` |  |  |  |
| 30 | `OA.RD.AUTHORISER` | `OaRuleDefinition_Authoriser` | String |  |  |
| 31 | `OA.RD.CO.CODE` | `OaRuleDefinition_CoCode` | String |  |  |
| 32 | `OA.RD.DEPT.CODE` | `OaRuleDefinition_DeptCode` | String |  |  |
| 33 | `OA.RD.AUDITOR.CODE` | `OaRuleDefinition_AuditorCode` | String |  |  |
| 34 | `OA.RD.AUDIT.DATE.TIME` | `OaRuleDefinition_AuditDateTime` | String |  |  |
