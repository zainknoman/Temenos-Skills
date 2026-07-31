# ID.EVALUATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.ID.EVALUATION.DETAILS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.EVD.EVALUATION.DATE` | `IdEvaluationDetails_EvaluationDate` | TField |  | This field is used to store the evaluation date on which the minimum balance and transaction exclusion criteria is processed. Validation Rules: 1. Standard T24 Date field. |
| 2 | `ID.EVD.EXCLUSION.EVAL.CYCLE` | `IdEvaluationDetails_ExclusionEvalCycle` | TField |  | This field is used to store the exclusion evaluation cycle configured for the relevant Account product in ID.ACCOUNT.CONDITION. |
| 3 | `ID.EVD.CONDITION.EVAL.PERIOD` | `IdEvaluationDetails_ConditionEvalPeriod` | TField |  | This field is used to store the condition evaluation period configured for the relevant Account product in ID.ACCOUNT.CONDITION. |
| 4 | `ID.EVD.PDS.CATEGORY` | `IdEvaluationDetails_PdsCategory` | TField |  | This field is used to store the PDS Category configured in ID.ACCOUNT.CONDITION for the relevant Account product. |
| 5 | `ID.EVD.MIN.BALANCE.EVAL.ST.DATE` | `IdEvaluationDetails_MinBalanceEvalStDate` | TField |  | This field is used to store the minimum balance evaluation start date configuration setup in ID.ACCOUNT.CONDITION for the relevant Account product. |
| 6 | `ID.EVD.RULE.VALUE.CURRENCY` | `IdEvaluationDetails_RuleValueCurrency` |  |  |  |
| 7 | `ID.EVD.RULE.VALUE.AMOUNT` | `IdEvaluationDetails_RuleValueAmount` |  |  |  |
| 8 | `ID.EVD.RULE.TRANSACTION.INITIATION` | `IdEvaluationDetails_RuleTransactionInitiation` | TField |  | This field is used to store the transaction initiation field value from ID.ACCOUNT.CONDITION for the relevant Account product. |
| 9 | `ID.EVD.RULE.ACTIVITY.CLASS` | `IdEvaluationDetails_RuleActivityClass` | TField |  | This field is used to store the Activity class field value from ID.ACCOUNT.CONDITION for the relevant Account product. |
| 10 | `ID.EVD.RULE.VALUE.ACTIVITY` | `IdEvaluationDetails_RuleValueActivity` |  |  |  |
| 11 | `ID.EVD.RULE.EXCLUDE` | `IdEvaluationDetails_RuleExclude` |  |  |  |
| 12 | `ID.EVD.THRESHOLD.COUNT` | `IdEvaluationDetails_ThresholdCount` | TField |  | This field is used to store the threshold count for configured activities in ID.ACCOUNT.CONDITION for the relevant Account product. |
| 13 | `ID.EVD.ACCOUNT.CURRENCY` | `IdEvaluationDetails_AccountCurrency` | TField |  | This field is used to store the currency of the account. |
| 14 | `ID.EVD.EVALUATION.PERIOD.FROM` | `IdEvaluationDetails_EvaluationPeriodFrom` |  |  |  |
| 15 | `ID.EVD.EVALUATION.PERIOD.TO` | `IdEvaluationDetails_EvaluationPeriodTo` |  |  |  |
| 16 | `ID.EVD.NUMBER.OF.DAYS` | `IdEvaluationDetails_NumberOfDays` |  |  |  |
| 17 | `ID.EVD.BALANCE.AMOUNT` | `IdEvaluationDetails_BalanceAmount` |  |  |  |
| 18 | `ID.EVD.EVALUATED.BALANCE` | `IdEvaluationDetails_EvaluatedBalance` |  |  |  |
| 19 | `ID.EVD.TRANSACTION.COUNT` | `IdEvaluationDetails_TransactionCount` | TField |  | This field is used to store the evaluated transaction count based upon the configured activities. |
| 20 | `ID.EVD.RULE.RESULT` | `IdEvaluationDetails_RuleResult` | TField |  | This field is used to store whether the evaluation criteria is PASS/ FAIL for the evaluation period. |
| 21 | `ID.EVD.ACCT.FUNDED.VALUE.DATE` | `IdEvaluationDetails_AcctFundedValueDate` | TField |  | This field is used to display the date on which the account was funded only for the account opened month. For the subsequent months this field value would be null. |
