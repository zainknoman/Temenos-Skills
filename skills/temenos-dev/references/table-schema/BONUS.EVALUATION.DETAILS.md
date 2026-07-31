# BONUS.EVALUATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.BONUS.EVALUATION.DETAILS` in `USRETL_Bonus.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BED.PERIOD.START.DATE` | `BonusEvaluationDetails_PeriodStartDate` | TField |  | Bonus period start date. |
| 2 | `BED.PERIOD.END.DATE` | `BonusEvaluationDetails_PeriodEndDate` | TField |  | Bonus period end date; i.e. Bonus payout date. |
| 3 | `BED.EVAL.RULE` | `BonusEvaluationDetails_EvalRule` |  |  |  |
| 4 | `BED.EVAL.DATE` | `BonusEvaluationDetails_EvalDate` |  |  |  |
| 5 | `BED.EVAL.PERIOD.START` | `BonusEvaluationDetails_EvalPeriodStart` |  |  |  |
| 6 | `BED.EVAL.PERIOD.END` | `BonusEvaluationDetails_EvalPeriodEnd` |  |  |  |
| 7 | `BED.PROD.ACTIVITY` | `BonusEvaluationDetails_ProdActivity` |  |  |  |
| 8 | `BED.COUNT` | `BonusEvaluationDetails_Count` |  |  |  |
| 9 | `BED.RESULT` | `BonusEvaluationDetails_Result` |  |  |  |
| 10 | `BED.RESERVED.15` | `BonusEvaluationDetails_Reserved15` |  |  |  |
| 11 | `BED.RESERVED.14` | `BonusEvaluationDetails_Reserved14` |  |  |  |
| 12 | `BED.RESERVED.13` | `BonusEvaluationDetails_Reserved13` |  |  |  |
| 13 | `BED.RESERVED.12` | `BonusEvaluationDetails_Reserved12` |  |  |  |
| 14 | `BED.RESERVED.11` | `BonusEvaluationDetails_Reserved11` |  |  |  |
| 15 | `BED.RULE.STATUS` | `BonusEvaluationDetails_RuleStatus` |  |  |  |
| 16 | `BED.EVAL.TYPE` | `BonusEvaluationDetails_EvalType` |  |  |  |
| 17 | `BED.BREAK.MESSAGE` | `BonusEvaluationDetails_BreakMessage` |  |  |  |
| 18 | `BED.RESERVED.10` | `BonusEvaluationDetails_Reserved10` |  |  |  |
| 19 | `BED.RESERVED.9` | `BonusEvaluationDetails_Reserved9` |  |  |  |
| 20 | `BED.RESERVED.8` | `BonusEvaluationDetails_Reserved8` |  |  |  |
| 21 | `BED.RESERVED.7` | `BonusEvaluationDetails_Reserved7` |  |  |  |
| 22 | `BED.RESERVED.6` | `BonusEvaluationDetails_Reserved6` |  |  |  |
| 23 | `BED.CUMULATIVE.STATUS` | `BonusEvaluationDetails_CumulativeStatus` | TField |  | Consolidated status of all EVAL.RULE. |
| 24 | `BED.REASON` | `BonusEvaluationDetails_Reason` | TField |  | Reason for withholding Bonus payout. |
| 25 | `BED.BONUS.AMOUNT` | `BonusEvaluationDetails_BonusAmount` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 26 | `BED.RESERVED.5` | `BonusEvaluationDetails_Reserved5` | TField |  |  |
| 27 | `BED.RESERVED.4` | `BonusEvaluationDetails_Reserved4` | TField |  |  |
| 28 | `BED.RESERVED.3` | `BonusEvaluationDetails_Reserved3` | TField |  |  |
| 29 | `BED.RESERVED.2` | `BonusEvaluationDetails_Reserved2` | TField |  |  |
| 30 | `BED.RESERVED.1` | `BonusEvaluationDetails_Reserved1` | TField |  |  |
