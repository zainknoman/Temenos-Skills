# NA.PRODUCT.RECOMMENDATION — Table Schema

> Source: `INSERTS/I_F.NA.PRODUCT.RECOMMENDATION` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.PR.RESERVED.7` | `NaProductRecommendation_Reserved7` | TField |  |  |
| 2 | `NA.PR.FIT.METHOD` | `NaProductRecommendation_FitMethod` | TField |  | The purpose code which specifies which fit method is being used. |
| 3 | `NA.PR.FIT.METHOD.VERSION` | `NaProductRecommendation_FitMethodVersion` | TField |  | Version of the product fit definition Method |
| 4 | `NA.PR.PRODUCT` | `NaProductRecommendation_Product` |  |  |  |
| 5 | `NA.PR.MC.FIELD` | `NaProductRecommendation_McField` |  |  |  |
| 6 | `NA.PR.VALUE` | `NaProductRecommendation_Value` |  |  |  |
| 7 | `NA.PR.VALUE.TYPE` | `NaProductRecommendation_ValueType` |  |  |  |
| 8 | `NA.PR.FIT.TYPE` | `NaProductRecommendation_FitType` |  |  |  |
| 9 | `NA.PR.QUESTION` | `NaProductRecommendation_Question` |  |  |  |
| 10 | `NA.PR.ANSWER` | `NaProductRecommendation_Answer` |  |  |  |
| 11 | `NA.PR.WEIGHT` | `NaProductRecommendation_Weight` |  |  |  |
| 12 | `NA.PR.KNOCKOUT.METRIC` | `NaProductRecommendation_KnockoutMetric` |  |  |  |
| 13 | `NA.PR.STANDARDIZE.METRIC` | `NaProductRecommendation_StandardizeMetric` |  |  |  |
| 14 | `NA.PR.RAW.SCORE` | `NaProductRecommendation_RawScore` |  |  |  |
| 15 | `NA.PR.STANDARD.SCORE` | `NaProductRecommendation_StandardScore` |  |  |  |
| 16 | `NA.PR.WEIGHTED.SCORE` | `NaProductRecommendation_WeightedScore` |  |  |  |
| 17 | `NA.PR.KNOCKOUT` | `NaProductRecommendation_Knockout` |  |  |  |
| 18 | `NA.PR.TOTAL.WEIGHTS` | `NaProductRecommendation_TotalWeights` |  |  |  |
| 19 | `NA.PR.TOTAL.SCORE` | `NaProductRecommendation_TotalScore` |  |  |  |
| 20 | `NA.PR.PERCENTAGE.FIT` | `NaProductRecommendation_PercentageFit` |  |  |  |
| 21 | `NA.PR.TOTAL.KNOCKOUTS` | `NaProductRecommendation_TotalKnockouts` |  |  |  |
| 22 | `NA.PR.ACTION` | `NaProductRecommendation_Action` | TField |  | Total of all Weighted Scores. |
| 23 | `NA.PR.MC.OUT.PRODUCT` | `NaProductRecommendation_McOutProduct` |  |  |  |
| 24 | `NA.PR.MC.OUT.FIELD` | `NaProductRecommendation_McOutField` |  |  |  |
| 25 | `NA.PR.MC.OUT.VALUE` | `NaProductRecommendation_McOutValue` |  |  |  |
| 26 | `NA.PR.RESERVED.6` | `NaProductRecommendation_Reserved6` | TField |  |  |
| 27 | `NA.PR.RESERVED.5` | `NaProductRecommendation_Reserved5` | TField |  |  |
| 28 | `NA.PR.RESERVED.4` | `NaProductRecommendation_Reserved4` | TField |  |  |
| 29 | `NA.PR.RESERVED.3` | `NaProductRecommendation_Reserved3` | TField |  |  |
| 30 | `NA.PR.RESERVED.2` | `NaProductRecommendation_Reserved2` | TField |  |  |
| 31 | `NA.PR.RESERVED.1` | `NaProductRecommendation_Reserved1` | TField |  |  |
| 32 | `NA.PR.LOCAL.REF` | `NaProductRecommendation_LocalRef` |  |  |  |
| 33 | `NA.PR.OVERRIDE` | `NaProductRecommendation_Override` |  |  |  |
| 34 | `NA.PR.RECORD.STATUS` | `NaProductRecommendation_RecordStatus` | String |  |  |
| 35 | `NA.PR.CURR.NO` | `NaProductRecommendation_CurrNo` | String |  |  |
| 36 | `NA.PR.INPUTTER` | `NaProductRecommendation_Inputter` |  |  |  |
| 37 | `NA.PR.DATE.TIME` | `NaProductRecommendation_DateTime` |  |  |  |
| 38 | `NA.PR.AUTHORISER` | `NaProductRecommendation_Authoriser` | String |  |  |
| 39 | `NA.PR.CO.CODE` | `NaProductRecommendation_CoCode` | String |  |  |
| 40 | `NA.PR.DEPT.CODE` | `NaProductRecommendation_DeptCode` | String |  |  |
| 41 | `NA.PR.AUDITOR.CODE` | `NaProductRecommendation_AuditorCode` | String |  |  |
| 42 | `NA.PR.AUDIT.DATE.TIME` | `NaProductRecommendation_AuditDateTime` | String |  |  |
