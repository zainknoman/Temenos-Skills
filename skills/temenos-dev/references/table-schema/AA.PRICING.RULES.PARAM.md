# AA.PRICING.RULES.PARAM — Table Schema

> Source: `INSERTS/I_F.AA.PRICING.RULES.PARAM` in `AA_PricingRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRP.MUTUALLY.EXCLUSIVE` | `AaPricingRulesParam_MutuallyExclusive` |  |  |  |
| 2 | `AA.PRP.RECORD.STATUS` | `AaPricingRulesParam_RecordStatus` | String |  |  |
| 3 | `AA.PRP.CURR.NO` | `AaPricingRulesParam_CurrNo` | String |  |  |
| 4 | `AA.PRP.INPUTTER` | `AaPricingRulesParam_Inputter` |  |  |  |
| 5 | `AA.PRP.DATE.TIME` | `AaPricingRulesParam_DateTime` |  |  |  |
| 6 | `AA.PRP.AUTHORISER` | `AaPricingRulesParam_Authoriser` | String |  |  |
| 7 | `AA.PRP.CO.CODE` | `AaPricingRulesParam_CoCode` | String |  |  |
| 8 | `AA.PRP.DEPT.CODE` | `AaPricingRulesParam_DeptCode` | String |  |  |
| 9 | `AA.PRP.AUDITOR.CODE` | `AaPricingRulesParam_AuditorCode` | String |  |  |
| 10 | `AA.PRP.AUDIT.DATE.TIME` | `AaPricingRulesParam_AuditDateTime` | String |  |  |
