# NA.QUESTIONNAIRE.RECOMMENDATION — Table Schema

> Source: `INSERTS/I_F.NA.QUESTIONNAIRE.RECOMMENDATION` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.QREC.RECOMMENDATION` | `NaQuestionnaireRecommendation_Recommendation` |  |  |  |
| 2 | `NA.QREC.RECORD.STATUS` | `NaQuestionnaireRecommendation_RecordStatus` |  |  |  |
| 3 | `NA.QREC.CURR.NO` | `NaQuestionnaireRecommendation_CurrNo` |  |  |  |
| 4 | `NA.QREC.INPUTTER` | `NaQuestionnaireRecommendation_Inputter` |  |  |  |
| 5 | `NA.QREC.DATE.TIME` | `NaQuestionnaireRecommendation_DateTime` |  |  |  |
| 6 | `NA.QREC.AUTHORISER` | `NaQuestionnaireRecommendation_Authoriser` |  |  |  |
| 7 | `NA.QREC.CO.CODE` | `NaQuestionnaireRecommendation_CoCode` |  |  |  |
| 8 | `NA.QREC.DEPT.CODE` | `NaQuestionnaireRecommendation_DeptCode` |  |  |  |
| 9 | `NA.QREC.AUDITOR.CODE` | `NaQuestionnaireRecommendation_AuditorCode` |  |  |  |
| 10 | `NA.QREC.AUDIT.DATE.TIME` | `NaQuestionnaireRecommendation_AuditDateTime` |  |  |  |
