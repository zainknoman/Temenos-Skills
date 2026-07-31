# NACUST.COVENANT — Table Schema

> Source: `INSERTS/I_F.NACUST.COVENANT` in `NACUST_Covenants.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COVN.DESCRIPTION` | `NacustCovenant_Description` | TField | Yes | Alphanumeric field to define the description of Convenant. Mandatory field |
| 2 | `COVN.TYPE` | `NacustCovenant_Type` |  |  |  |
| 3 | `COVN.EVAL.TYPE` | `NacustCovenant_EvalType` | TField |  | Allowed Values: DATE, RATING, AMOUNT, PERCENTAGE, RATIO Target value will be validated based on the eval type |
| 4 | `COVN.EVAL.OPERAND` | `NacustCovenant_EvalOperand` | TField |  | Allowed Values: EQ LT GT LE GE |
| 5 | `COVN.EVAL.API` | `NacustCovenant_EvalApi` | TField |  | An Infobasic routine can be attached here This routine accepts 3 arguments ArrangementId CovenantId Respose |
| 6 | `COVN.EVAL.RULE` | `NacustCovenant_EvalRule` | TField |  | Should be a valid EB.RULE Id This routine should respond TRUE or FALSE and that will be compared with Target Value |
| 7 | `COVN.REVIEW.FREQUENCY` | `NacustCovenant_ReviewFrequency` | TField |  | Frequency of review and/or due date |
| 8 | `COVN.PRE.NOTIFY.DAYS` | `NacustCovenant_PreNotifyDays` | TField |  | Number of days before the due date the covenant status prenotificed. |
| 9 | `COVN.RESERVED.5` | `NacustCovenant_Reserved5` | TField |  |  |
| 10 | `COVN.RESERVED.4` | `NacustCovenant_Reserved4` | TField |  |  |
| 11 | `COVN.RESERVED.3` | `NacustCovenant_Reserved3` | TField |  |  |
| 12 | `COVN.RESERVED.2` | `NacustCovenant_Reserved2` | TField |  |  |
| 13 | `COVN.RESERVED.1` | `NacustCovenant_Reserved1` | TField |  |  |
| 14 | `COVN.LOCAL.REF` | `NacustCovenant_LocalRef` |  |  |  |
| 15 | `COVN.OVERRIDE` | `NacustCovenant_Override` |  |  |  |
| 16 | `COVN.RECORD.STATUS` | `NacustCovenant_RecordStatus` | String |  |  |
| 17 | `COVN.CURR.NO` | `NacustCovenant_CurrNo` | String |  |  |
| 18 | `COVN.INPUTTER` | `NacustCovenant_Inputter` |  |  |  |
| 19 | `COVN.DATE.TIME` | `NacustCovenant_DateTime` |  |  |  |
| 20 | `COVN.AUTHORISER` | `NacustCovenant_Authoriser` | String |  |  |
| 21 | `COVN.CO.CODE` | `NacustCovenant_CoCode` | String |  |  |
| 22 | `COVN.DEPT.CODE` | `NacustCovenant_DeptCode` | String |  |  |
| 23 | `COVN.AUDITOR.CODE` | `NacustCovenant_AuditorCode` | String |  |  |
| 24 | `COVN.AUDIT.DATE.TIME` | `NacustCovenant_AuditDateTime` | String |  |  |
