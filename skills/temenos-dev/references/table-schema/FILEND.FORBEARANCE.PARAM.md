# FILEND.FORBEARANCE.PARAM — Table Schema

> Source: `INSERTS/I_F.FILEND.FORBEARANCE.PARAM` in `FILEND_ForbearanceProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FILEND.FORB.PARAM.FORB.STAGE.INDICATIOR` | `FilendForbearanceParam_ForbStageIndicatior` |  |  |  |
| 2 | `FILEND.FORB.PARAM.OVERDUE.DAYS` | `FilendForbearanceParam_OverdueDays` |  |  |  |
| 3 | `FILEND.FORB.PARAM.PROBATION.PERIOD` | `FilendForbearanceParam_ProbationPeriod` |  |  |  |
| 4 | `FILEND.FORB.PARAM.PROB.STAGE.MVMT` | `FilendForbearanceParam_ProbStageMvmt` |  |  |  |
| 5 | `FILEND.FORB.PARAM.PROB.OVERDUE.CHECK` | `FilendForbearanceParam_ProbOverdueCheck` |  |  |  |
| 6 | `FILEND.FORB.PARAM.PROB.STAGE` | `FilendForbearanceParam_ProbStage` |  |  |  |
| 7 | `FILEND.FORB.PARAM.COND.MET.MVMT` | `FilendForbearanceParam_CondMetMvmt` |  |  |  |
| 8 | `FILEND.FORB.PARAM.COND.STAGE` | `FilendForbearanceParam_CondStage` |  |  |  |
| 9 | `FILEND.FORB.PARAM.ON.EVENT` | `FilendForbearanceParam_OnEvent` |  |  |  |
| 10 | `FILEND.FORB.PARAM.REPORTING.PERIOD` | `FilendForbearanceParam_ReportingPeriod` | TField |  | Period of reporting date to be configured. |
| 11 | `FILEND.FORB.PARAM.RESTRICT.ARRANGEMENT` | `FilendForbearanceParam_RestrictArrangement` |  |  |  |
| 12 | `FILEND.FORB.PARAM.LOCAL.REF` | `FilendForbearanceParam_LocalRef` |  |  |  |
| 13 | `FILEND.FORB.PARAM.OVERRIDE` | `FilendForbearanceParam_Override` |  |  |  |
| 14 | `FILEND.FORB.PARAM.RECORD.STATUS` | `FilendForbearanceParam_RecordStatus` | String |  |  |
| 15 | `FILEND.FORB.PARAM.CURR.NO` | `FilendForbearanceParam_CurrNo` | String |  |  |
| 16 | `FILEND.FORB.PARAM.INPUTTER` | `FilendForbearanceParam_Inputter` |  |  |  |
| 17 | `FILEND.FORB.PARAM.DATE.TIME` | `FilendForbearanceParam_DateTime` |  |  |  |
| 18 | `FILEND.FORB.PARAM.AUTHORISER` | `FilendForbearanceParam_Authoriser` | String |  |  |
| 19 | `FILEND.FORB.PARAM.CO.CODE` | `FilendForbearanceParam_CoCode` | String |  |  |
| 20 | `FILEND.FORB.PARAM.DEPT.CODE` | `FilendForbearanceParam_DeptCode` | String |  |  |
| 21 | `FILEND.FORB.PARAM.AUDITOR.CODE` | `FilendForbearanceParam_AuditorCode` | String |  |  |
| 22 | `FILEND.FORB.PARAM.AUDIT.DATE.TIME` | `FilendForbearanceParam_AuditDateTime` | String |  |  |
