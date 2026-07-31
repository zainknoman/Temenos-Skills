# MIFDII.CLIENT.QUESTION.CATALOG — Table Schema

> Source: `INSERTS/I_F.MIFDII.CLIENT.QUESTION.CATALOG` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFDII.CL.QUE.CAT.QUESTION` | `MifdiiClientQuestionCatalog_Question` |  |  |  |
| 2 | `MIFDII.CL.QUE.CAT.QUESTION.ID` | `MifdiiClientQuestionCatalog_QuestionId` |  |  |  |
| 3 | `MIFDII.CL.QUE.CAT.MANDATORY` | `MifdiiClientQuestionCatalog_Mandatory` |  |  |  |
| 4 | `MIFDII.CL.QUE.CAT.IRP.MANDATORY` | `MifdiiClientQuestionCatalog_IrpMandatory` |  |  |  |
| 5 | `MIFDII.CL.QUE.CAT.ANSWER.TEXT` | `MifdiiClientQuestionCatalog_AnswerText` |  |  |  |
| 6 | `MIFDII.CL.QUE.CAT.ANSWER.VALUE` | `MifdiiClientQuestionCatalog_AnswerValue` |  |  |  |
| 7 | `MIFDII.CL.QUE.CAT.ANSWER.RATING` | `MifdiiClientQuestionCatalog_AnswerRating` |  |  |  |
| 8 | `MIFDII.CL.QUE.CAT.GROUP.HEADING` | `MifdiiClientQuestionCatalog_GroupHeading` |  |  |  |
| 9 | `MIFDII.CL.QUE.CAT.LAST.QUES.ID` | `MifdiiClientQuestionCatalog_LastQuesId` |  |  |  |
| 10 | `MIFDII.CL.QUE.CAT.GROUP.SCORE` | `MifdiiClientQuestionCatalog_GroupScore` |  |  |  |
| 11 | `MIFDII.CL.QUE.CAT.GROUP.ID` | `MifdiiClientQuestionCatalog_GroupId` | TField |  | This multi-value field is used to capture the group heading for all the groups defined in MIFDII.QUESTION.GROUP. Validation Rule: This is a NOINPUT field. |
| 12 | `MIFDII.CL.QUE.CAT.TOTAL.SCORE` | `MifdiiClientQuestionCatalog_TotalScore` | TField |  | This field is used to capture the total score for all the groups defined in MIFDII.QUESTION.GROUP. Validation Rule: This is a NOINPUT field. |
| 13 | `MIFDII.CL.QUE.CAT.CUSTOMER.IRP` | `MifdiiClientQuestionCatalog_CustomerIrp` | TField |  | This field will calculate the CUSTOMER.IRP based on the answers answered by the customer. Validation Rule: This is a NOINPUT field. |
| 14 | `MIFDII.CL.QUE.CAT.CUSTOMER.RISK.LEVEL` | `MifdiiClientQuestionCatalog_CustomerRiskLevel` | TField |  | This field will calculate the CUSTOMER.RISK.LEVEL based on the answers answered by the customer. Validation Rule: This is a NOINPUT field. |
| 15 | `MIFDII.CL.QUE.CAT.LOCAL.REF` | `MifdiiClientQuestionCatalog_LocalRef` |  |  |  |
| 16 | `MIFDII.CL.QUE.CAT.RESERVED.10` | `MifdiiClientQuestionCatalog_Reserved10` | TField |  |  |
| 17 | `MIFDII.CL.QUE.CAT.RESERVED.9` | `MifdiiClientQuestionCatalog_Reserved9` | TField |  |  |
| 18 | `MIFDII.CL.QUE.CAT.RESERVED.8` | `MifdiiClientQuestionCatalog_Reserved8` | TField |  |  |
| 19 | `MIFDII.CL.QUE.CAT.RESERVED.7` | `MifdiiClientQuestionCatalog_Reserved7` | TField |  |  |
| 20 | `MIFDII.CL.QUE.CAT.RESERVED.6` | `MifdiiClientQuestionCatalog_Reserved6` | TField |  |  |
| 21 | `MIFDII.CL.QUE.CAT.RESERVED.5` | `MifdiiClientQuestionCatalog_Reserved5` | TField |  |  |
| 22 | `MIFDII.CL.QUE.CAT.RESERVED.4` | `MifdiiClientQuestionCatalog_Reserved4` | TField |  |  |
| 23 | `MIFDII.CL.QUE.CAT.RESERVED.3` | `MifdiiClientQuestionCatalog_Reserved3` | TField |  |  |
| 24 | `MIFDII.CL.QUE.CAT.RESERVED.2` | `MifdiiClientQuestionCatalog_Reserved2` | TField |  |  |
| 25 | `MIFDII.CL.QUE.CAT.RESERVED.1` | `MifdiiClientQuestionCatalog_Reserved1` | TField |  |  |
| 26 | `MIFDII.CL.QUE.CAT.OVERRIDE` | `MifdiiClientQuestionCatalog_Override` |  |  |  |
| 27 | `MIFDII.CL.QUE.CAT.RECORD.STATUS` | `MifdiiClientQuestionCatalog_RecordStatus` | String |  |  |
| 28 | `MIFDII.CL.QUE.CAT.CURR.NO` | `MifdiiClientQuestionCatalog_CurrNo` | String |  |  |
| 29 | `MIFDII.CL.QUE.CAT.INPUTTER` | `MifdiiClientQuestionCatalog_Inputter` |  |  |  |
| 30 | `MIFDII.CL.QUE.CAT.DATE.TIME` | `MifdiiClientQuestionCatalog_DateTime` |  |  |  |
| 31 | `MIFDII.CL.QUE.CAT.AUTHORISER` | `MifdiiClientQuestionCatalog_Authoriser` | String |  |  |
| 32 | `MIFDII.CL.QUE.CAT.CO.CODE` | `MifdiiClientQuestionCatalog_CoCode` | String |  |  |
| 33 | `MIFDII.CL.QUE.CAT.DEPT.CODE` | `MifdiiClientQuestionCatalog_DeptCode` | String |  |  |
| 34 | `MIFDII.CL.QUE.CAT.AUDITOR.CODE` | `MifdiiClientQuestionCatalog_AuditorCode` | String |  |  |
| 35 | `MIFDII.CL.QUE.CAT.AUDIT.DATE.TIME` | `MifdiiClientQuestionCatalog_AuditDateTime` | String |  |  |
