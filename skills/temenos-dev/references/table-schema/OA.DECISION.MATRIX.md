# OA.DECISION.MATRIX — Table Schema

> Source: `INSERTS/I_F.OA.DECISION.MATRIX` in `OA_Decision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DM.DESCRIPTION` | `OaDecisionMatrix_Description` |  |  |  |
| 2 | `OA.DM.FULL.DESCRIPTION` | `OaDecisionMatrix_FullDescription` |  |  |  |
| 3 | `OA.DM.RESERVED.10` | `OaDecisionMatrix_Reserved10` | TField |  |  |
| 4 | `OA.DM.RULE.DESCRIPTION` | `OaDecisionMatrix_RuleDescription` |  |  |  |
| 5 | `OA.DM.RULE` | `OaDecisionMatrix_Rule` |  |  |  |
| 6 | `OA.DM.RULE.ID` | `OaDecisionMatrix_RuleId` |  |  |  |
| 7 | `OA.DM.RESERVED.9` | `OaDecisionMatrix_Reserved9` |  |  |  |
| 8 | `OA.DM.RESERVED.8` | `OaDecisionMatrix_Reserved8` |  |  |  |
| 9 | `OA.DM.DECISION.BODY` | `OaDecisionMatrix_DecisionBody` |  |  |  |
| 10 | `OA.DM.DECISION.MATRIX` | `OaDecisionMatrix_DecisionMatrix` |  |  |  |
| 11 | `OA.DM.DECISION` | `OaDecisionMatrix_Decision` |  |  |  |
| 12 | `OA.DM.RESERVED.7` | `OaDecisionMatrix_Reserved7` |  |  |  |
| 13 | `OA.DM.RESERVED.6` | `OaDecisionMatrix_Reserved6` |  |  |  |
| 14 | `OA.DM.NEXT.BODY` | `OaDecisionMatrix_NextBody` |  |  |  |
| 15 | `OA.DM.NEXT.MATRIX` | `OaDecisionMatrix_NextMatrix` |  |  |  |
| 16 | `OA.DM.RESERVED.5` | `OaDecisionMatrix_Reserved5` | TField |  |  |
| 17 | `OA.DM.RESERVED.4` | `OaDecisionMatrix_Reserved4` | TField |  |  |
| 18 | `OA.DM.RESERVED.3` | `OaDecisionMatrix_Reserved3` | TField |  |  |
| 19 | `OA.DM.DEFAULT.BODY` | `OaDecisionMatrix_DefaultBody` | TField |  | DEFAULT.BODY, DEFAULT.MATRIX and DEFAULT.DECISION fields are mutually exclusive, Any one of the fields must be specified. Default decision body. |
| 20 | `OA.DM.DEFAULT.MATRIX` | `OaDecisionMatrix_DefaultMatrix` | TField |  | DEFAULT.BODY, DEFAULT.MATRIX and DEFAULT.DECISION fields are mutually exclusive, Any one of the fields must be specified. Default decision matrix. |
| 21 | `OA.DM.DEFAULT.DECISION` | `OaDecisionMatrix_DefaultDecision` | TField |  | DEFAULT.BODY, DEFAULT.MATRIX and DEFAULT.DECISION fields are mutually exclusive, Any one of the fields must be specified. Default decision. |
| 22 | `OA.DM.RESERVED.2` | `OaDecisionMatrix_Reserved2` | TField |  |  |
| 23 | `OA.DM.RESERVED.1` | `OaDecisionMatrix_Reserved1` | TField |  |  |
| 24 | `OA.DM.ACTION` | `OaDecisionMatrix_Action` | TField | No | This field indicates which action will be performed after the record is authorised. Optional Input Allowed values are Null or PUBLISH |
| 25 | `OA.DM.EXPIRY.DATE` | `OaDecisionMatrix_ExpiryDate` | TField |  | This is the date beyond which the DECISION.MATRIX represented by the ID of this record can no longer be used. |
| 26 | `OA.DM.PUBLISH.STATUS` | `OaDecisionMatrix_PublishStatus` | TField |  | System maintained Noinput field which will contain the result of the publishing effort. |
| 27 | `OA.DM.PUBLISH.ERROR` | `OaDecisionMatrix_PublishError` |  |  |  |
| 28 | `OA.DM.ERROR.SUGGESTION` | `OaDecisionMatrix_ErrorSuggestion` |  |  |  |
| 29 | `OA.DM.LOCAL.REF` | `OaDecisionMatrix_LocalRef` |  |  |  |
| 30 | `OA.DM.RECORD.STATUS` | `OaDecisionMatrix_RecordStatus` | String |  |  |
| 31 | `OA.DM.CURR.NO` | `OaDecisionMatrix_CurrNo` | String |  |  |
| 32 | `OA.DM.INPUTTER` | `OaDecisionMatrix_Inputter` |  |  |  |
| 33 | `OA.DM.DATE.TIME` | `OaDecisionMatrix_DateTime` |  |  |  |
| 34 | `OA.DM.AUTHORISER` | `OaDecisionMatrix_Authoriser` | String |  |  |
| 35 | `OA.DM.CO.CODE` | `OaDecisionMatrix_CoCode` | String |  |  |
| 36 | `OA.DM.DEPT.CODE` | `OaDecisionMatrix_DeptCode` | String |  |  |
| 37 | `OA.DM.AUDITOR.CODE` | `OaDecisionMatrix_AuditorCode` | String |  |  |
| 38 | `OA.DM.AUDIT.DATE.TIME` | `OaDecisionMatrix_AuditDateTime` | String |  |  |
