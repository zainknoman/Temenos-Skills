# AA.EVALUATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.EVALUATION.DETAILS` in `AA_PricingRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.EVD.OWNER` | `AaEvaluationDetails_Owner` |  |  |  |
| 2 | `AA.EVD.ARRANGEMENT.ID` | `AaEvaluationDetails_ArrangementId` | TField |  | Stores Arrangement reference for which evaluation is done |
| 3 | `AA.EVD.ACTIVITY.ID` | `AaEvaluationDetails_ActivityId` | TField |  | Stores AA.ARRANGEMENT.ACTIVITY id during which evaluation is done. |
| 4 | `AA.EVD.DATE` | `AaEvaluationDetails_Date` | TField |  | Indicates the date on which evaluation is done. |
| 5 | `AA.EVD.RULE.TYPE` | `AaEvaluationDetails_RuleType` | TField |  | Indicates if the rule has been evaluated as part of Pricing rules or Activity restriction. Allowed values are a) Pricing Rules b) Activity restriction |
| 6 | `AA.EVD.PROGRAM.LIMIT` | `AaEvaluationDetails_ProgramLimit` | TField |  | Maximum number of Program whose benefit can be applied is specified. This is updated only when rule type is Pricing rules. |
| 7 | `AA.EVD.SELECTED.PROGRAM` | `AaEvaluationDetails_SelectedProgram` |  |  |  |
| 8 | `AA.EVD.PRICING.PROPERTY` | `AaEvaluationDetails_PricingProperty` | TField |  | Property for which Pricing Benefit rule evaluation was done. |
| 9 | `AA.EVD.TRIGGER` | `AaEvaluationDetails_Trigger` | TField |  | Specifies during what stage the rules were run i.e. whether during the pricing property assessment or after assessment or on accrual. When rule type is Activity restriction then this will always be updated as On assessment |
| 10 | `AA.EVD.PRICING.BENEFIT` | `AaEvaluationDetails_PricingBenefit` |  |  |  |
| 11 | `AA.EVD.PRICING.PROGRAM` | `AaEvaluationDetails_PricingProgram` |  |  |  |
| 12 | `AA.EVD.PRICING.RULE.NAME` | `AaEvaluationDetails_PricingRuleName` |  |  |  |
| 13 | `AA.EVD.PERIODIC.ATTRIBUTE` | `AaEvaluationDetails_PeriodicAttribute` |  |  |  |
| 14 | `AA.EVD.BALANCE.TYPE` | `AaEvaluationDetails_BalanceType` |  |  |  |
| 15 | `AA.EVD.RULE.VALUE` | `AaEvaluationDetails_RuleValue` |  |  |  |
| 16 | `AA.EVD.SOURCE.TYPE` | `AaEvaluationDetails_SourceType` |  |  |  |
| 17 | `AA.EVD.SOURCE` | `AaEvaluationDetails_Source` |  |  |  |
| 18 | `AA.EVD.ACTUAL.VALUE` | `AaEvaluationDetails_ActualValue` |  |  |  |
| 19 | `AA.EVD.RULE.RESULT` | `AaEvaluationDetails_RuleResult` |  |  |  |
| 20 | `AA.EVD.LOGICAL.OPERAND` | `AaEvaluationDetails_LogicalOperand` |  |  |  |
| 21 | `AA.EVD.EVALUATION` | `AaEvaluationDetails_Evaluation` |  |  |  |
| 22 | `AA.EVD.EVALUATION.RESULT` | `AaEvaluationDetails_EvaluationResult` |  |  |  |
| 23 | `AA.EVD.ADJUST.OPERAND` | `AaEvaluationDetails_AdjustOperand` |  |  |  |
| 24 | `AA.EVD.ADJUST.PERCENTAGE` | `AaEvaluationDetails_AdjustPercentage` |  |  |  |
| 25 | `AA.EVD.ADJUST.AMOUNT` | `AaEvaluationDetails_AdjustAmount` |  |  |  |
| 26 | `AA.EVD.OVERRIDE.AMOUNT` | `AaEvaluationDetails_OverrideAmount` |  |  |  |
| 27 | `AA.EVD.FILTER.BY.PRODUCT` | `AaEvaluationDetails_FilterByProduct` |  |  |  |
| 28 | `AA.EVD.RESERVED.6` | `AaEvaluationDetails_Reserved6` |  |  |  |
| 29 | `AA.EVD.RESERVED.5` | `AaEvaluationDetails_Reserved5` | TField |  |  |
| 30 | `AA.EVD.RESERVED.4` | `AaEvaluationDetails_Reserved4` | TField |  |  |
| 31 | `AA.EVD.RESERVED.3` | `AaEvaluationDetails_Reserved3` | TField |  |  |
| 32 | `AA.EVD.RESERVED.2` | `AaEvaluationDetails_Reserved2` | TField |  |  |
| 33 | `AA.EVD.RESERVED.1` | `AaEvaluationDetails_Reserved1` | TField |  |  |
| 34 | `AA.EVD.PQ.RULE.SET` | `AaEvaluationDetails_PqRuleSet` |  |  |  |
| 35 | `AA.EVD.PQ.RULE.EXPRESSION` | `AaEvaluationDetails_PqRuleExpression` |  |  |  |
| 36 | `AA.EVD.PQ.RULE.SET.EVALUATION.RESULT` | `AaEvaluationDetails_PqRuleSetEvaluationResult` |  |  |  |
| 37 | `AA.EVD.PQ.DEFINED.EVALUATION.RESULT` | `AaEvaluationDetails_PqDefinedEvaluationResult` |  |  |  |
| 38 | `AA.EVD.PQ.DEFAULT.RESULT` | `AaEvaluationDetails_PqDefaultResult` |  |  |  |
| 39 | `AA.EVD.PQ.RULE.NAME` | `AaEvaluationDetails_PqRuleName` |  |  |  |
| 40 | `AA.EVD.PQ.PERIODIC.ATTRIBUTE` | `AaEvaluationDetails_PqPeriodicAttribute` |  |  |  |
| 41 | `AA.EVD.PQ.SOURCE` | `AaEvaluationDetails_PqSource` |  |  |  |
| 42 | `AA.EVD.PQ.FILTER.BY.PRODUCT` | `AaEvaluationDetails_PqFilterByProduct` |  |  |  |
| 43 | `AA.EVD.PQ.PERIODIC.VALUE` | `AaEvaluationDetails_PqPeriodicValue` |  |  |  |
| 44 | `AA.EVD.PQ.ACTUAL.VALUE` | `AaEvaluationDetails_PqActualValue` |  |  |  |
| 45 | `AA.EVD.PQ.RULE.EVALUATION.RESULT` | `AaEvaluationDetails_PqRuleEvaluationResult` |  |  |  |
| 46 | `AA.EVD.PQ.RULE.SET.TRIGGER` | `AaEvaluationDetails_PqRuleSetTrigger` | TField |  | Free Text maintained in activity restriction that is mapped to an action. |
| 47 | `AA.EVD.PQ.TRIGGER.ACTION` | `AaEvaluationDetails_PqTriggerAction` | TField |  | Action that needs to taken when the evaluation meets rule.evaluation specified in activity restriction.Action is defined in AA.ACTION. |
| 48 | `AA.EVD.PG.PROPERTY` | `AaEvaluationDetails_PgProperty` | TField |  | Denotes the property name of Pricing Grid class whose evaluation resulted in the evaluation record. |
| 49 | `AA.EVD.PG.TARGET.PROPERTY` | `AaEvaluationDetails_PgTargetProperty` |  |  |  |
| 50 | `AA.EVD.PG.CRITERION` | `AaEvaluationDetails_PgCriterion` |  |  |  |
| 51 | `AA.EVD.PG.CRITERION.VALUE` | `AaEvaluationDetails_PgCriterionValue` |  |  |  |
| 52 | `AA.EVD.PG.TARGET` | `AaEvaluationDetails_PgTarget` |  |  |  |
| 53 | `AA.EVD.PG.TARGET.VALUE` | `AaEvaluationDetails_PgTargetValue` |  |  |  |
| 54 | `AA.EVD.PG.TIER.UPTO.AMT` | `AaEvaluationDetails_PgTierUptoAmt` |  |  |  |
| 55 | `AA.EVD.PG.TIER.TYPE` | `AaEvaluationDetails_PgTierType` |  |  |  |
| 56 | `AA.EVD.VERSION` | `AaEvaluationDetails_Version` |  |  |  |
| 57 | `AA.EVD.PRICING.BENEFIT.PROGRAM` | `AaEvaluationDetails_PricingBenefitProgram` |  |  |  |
| 58 | `AA.EVD.RE.RULE.PARTY.ROLE` | `AaEvaluationDetails_ReRulePartyRole` |  |  |  |
| 59 | `AA.EVD.RE.RULE.EXPRESSION` | `AaEvaluationDetails_ReRuleExpression` |  |  |  |
| 60 | `AA.EVD.RESERVED.11` | `AaEvaluationDetails_Reserved11` |  |  |  |
| 61 | `AA.EVD.RESERVED.10` | `AaEvaluationDetails_Reserved10` |  |  |  |
| 62 | `AA.EVD.RESERVED.9` | `AaEvaluationDetails_Reserved9` |  |  |  |
| 63 | `AA.EVD.RESERVED.8` | `AaEvaluationDetails_Reserved8` |  |  |  |
| 64 | `AA.EVD.RESERVED.7` | `AaEvaluationDetails_Reserved7` |  |  |  |
| 65 | `AA.EVD.RE.RULE.EXP.EVALUATION.RESULT` | `AaEvaluationDetails_ReRuleExpEvaluationResult` |  |  |  |
| 66 | `AA.EVD.RE.RULE` | `AaEvaluationDetails_ReRule` |  |  |  |
| 67 | `AA.EVD.RESERVED.16` | `AaEvaluationDetails_Reserved16` |  |  |  |
| 68 | `AA.EVD.RESERVED.15` | `AaEvaluationDetails_Reserved15` |  |  |  |
| 69 | `AA.EVD.RESERVED.14` | `AaEvaluationDetails_Reserved14` |  |  |  |
| 70 | `AA.EVD.RESERVED.13` | `AaEvaluationDetails_Reserved13` |  |  |  |
| 71 | `AA.EVD.RESERVED.12` | `AaEvaluationDetails_Reserved12` |  |  |  |
| 72 | `AA.EVD.RE.RULE.EVALUATION.RESULT` | `AaEvaluationDetails_ReRuleEvaluationResult` |  |  |  |
| 73 | `AA.EVD.RE.FAILURE.ACTION` | `AaEvaluationDetails_ReFailureAction` |  |  |  |
| 74 | `AA.EVD.RE.FAILURE.ACTION.CONTEXT` | `AaEvaluationDetails_ReFailureActionContext` | TField |  | Specifies the product to which the contract should switch in case of failure action is change product. |
| 75 | `AA.EVD.PQ.PROMOTION.BENEFIT.TYPE` | `AaEvaluationDetails_PqPromotionBenefitType` |  |  |  |
