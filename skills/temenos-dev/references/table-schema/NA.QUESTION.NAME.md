# NA.QUESTION.NAME — Table Schema

> Source: `INSERTS/I_F.NA.QUESTION.NAME` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.QN.NEEDS.CLASS.NAME` | `NaQuestionName_NeedsClassName` | TField |  | The class name used in AA.CLASS.DEFINITION. |
| 2 | `NA.QN.RECORD.STATUS` | `NaQuestionName_RecordStatus` | String |  |  |
| 3 | `NA.QN.CURR.NO` | `NaQuestionName_CurrNo` | String |  |  |
| 4 | `NA.QN.INPUTTER` | `NaQuestionName_Inputter` |  |  |  |
| 5 | `NA.QN.DATE.TIME` | `NaQuestionName_DateTime` |  |  |  |
| 6 | `NA.QN.AUTHORISER` | `NaQuestionName_Authoriser` | String |  |  |
| 7 | `NA.QN.CO.CODE` | `NaQuestionName_CoCode` | String |  |  |
| 8 | `NA.QN.DEPT.CODE` | `NaQuestionName_DeptCode` | String |  |  |
| 9 | `NA.QN.AUDITOR.CODE` | `NaQuestionName_AuditorCode` | String |  |  |
| 10 | `NA.QN.AUDIT.DATE.TIME` | `NaQuestionName_AuditDateTime` | String |  |  |
