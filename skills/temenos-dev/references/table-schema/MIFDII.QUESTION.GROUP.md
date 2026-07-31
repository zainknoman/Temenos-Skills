# MIFDII.QUESTION.GROUP — Table Schema

> Source: `INSERTS/I_F.MIFDII.QUESTION.GROUP` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFDII.QUE.GRP.GROUP.HEADING` | `MifdiiQuestionGroup_GroupHeading` |  |  |  |
| 2 | `MIFDII.QUE.GRP.MAX.VALUE` | `MifdiiQuestionGroup_MaxValue` |  |  |  |
| 3 | `MIFDII.QUE.GRP.MIN.VALUE` | `MifdiiQuestionGroup_MinValue` |  |  |  |
| 4 | `MIFDII.QUE.GRP.QUESTION.ID` | `MifdiiQuestionGroup_QuestionId` |  |  |  |
| 5 | `MIFDII.QUE.GRP.RISK.LEVEL` | `MifdiiQuestionGroup_RiskLevel` |  |  |  |
| 6 | `MIFDII.QUE.GRP.RISK.DESCRIPTION` | `MifdiiQuestionGroup_RiskDescription` |  |  |  |
| 7 | `MIFDII.QUE.GRP.MIN.RATING` | `MifdiiQuestionGroup_MinRating` |  |  |  |
| 8 | `MIFDII.QUE.GRP.MAX.RATING` | `MifdiiQuestionGroup_MaxRating` |  |  |  |
| 9 | `MIFDII.QUE.GRP.MAX.RISK.LEVEL` | `MifdiiQuestionGroup_MaxRiskLevel` |  |  |  |
| 10 | `MIFDII.QUE.GRP.LOCAL.REF` | `MifdiiQuestionGroup_LocalRef` |  |  |  |
| 11 | `MIFDII.QUE.GRP.RESERVED.10` | `MifdiiQuestionGroup_Reserved10` | TField |  |  |
| 12 | `MIFDII.QUE.GRP.RESERVED.9` | `MifdiiQuestionGroup_Reserved9` | TField |  |  |
| 13 | `MIFDII.QUE.GRP.RESERVED.8` | `MifdiiQuestionGroup_Reserved8` | TField |  |  |
| 14 | `MIFDII.QUE.GRP.RESERVED.7` | `MifdiiQuestionGroup_Reserved7` | TField |  |  |
| 15 | `MIFDII.QUE.GRP.RESERVED.6` | `MifdiiQuestionGroup_Reserved6` | TField |  |  |
| 16 | `MIFDII.QUE.GRP.RESERVED.5` | `MifdiiQuestionGroup_Reserved5` | TField |  |  |
| 17 | `MIFDII.QUE.GRP.RESERVED.4` | `MifdiiQuestionGroup_Reserved4` | TField |  |  |
| 18 | `MIFDII.QUE.GRP.RESERVED.3` | `MifdiiQuestionGroup_Reserved3` | TField |  |  |
| 19 | `MIFDII.QUE.GRP.RESERVED.2` | `MifdiiQuestionGroup_Reserved2` | TField |  |  |
| 20 | `MIFDII.QUE.GRP.RESERVED.1` | `MifdiiQuestionGroup_Reserved1` | TField |  |  |
| 21 | `MIFDII.QUE.GRP.OVERRIDE` | `MifdiiQuestionGroup_Override` |  |  |  |
| 22 | `MIFDII.QUE.GRP.RECORD.STATUS` | `MifdiiQuestionGroup_RecordStatus` | String |  |  |
| 23 | `MIFDII.QUE.GRP.CURR.NO` | `MifdiiQuestionGroup_CurrNo` | String |  |  |
| 24 | `MIFDII.QUE.GRP.INPUTTER` | `MifdiiQuestionGroup_Inputter` |  |  |  |
| 25 | `MIFDII.QUE.GRP.DATE.TIME` | `MifdiiQuestionGroup_DateTime` |  |  |  |
| 26 | `MIFDII.QUE.GRP.AUTHORISER` | `MifdiiQuestionGroup_Authoriser` | String |  |  |
| 27 | `MIFDII.QUE.GRP.CO.CODE` | `MifdiiQuestionGroup_CoCode` | String |  |  |
| 28 | `MIFDII.QUE.GRP.DEPT.CODE` | `MifdiiQuestionGroup_DeptCode` | String |  |  |
| 29 | `MIFDII.QUE.GRP.AUDITOR.CODE` | `MifdiiQuestionGroup_AuditorCode` | String |  |  |
| 30 | `MIFDII.QUE.GRP.AUDIT.DATE.TIME` | `MifdiiQuestionGroup_AuditDateTime` | String |  |  |
