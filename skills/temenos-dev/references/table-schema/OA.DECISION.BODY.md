# OA.DECISION.BODY — Table Schema

> Source: `INSERTS/I_F.OA.DECISION.BODY` in `OA_Decision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DB.DESCRIPTION` | `OaDecisionBody_Description` |  |  |  |
| 2 | `OA.DB.FULL.DESCRIPTION` | `OaDecisionBody_FullDescription` |  |  |  |
| 3 | `OA.DB.ROLE` | `OaDecisionBody_Role` |  |  |  |
| 4 | `OA.DB.USER` | `OaDecisionBody_User` |  |  |  |
| 5 | `OA.DB.DEPARTMENT` | `OaDecisionBody_Department` |  |  |  |
| 6 | `OA.DB.REFER.ALLOWED` | `OaDecisionBody_ReferAllowed` | TField |  | This field will indicate whether referral would be allowed for this body. |
| 7 | `OA.DB.RESERVED.5` | `OaDecisionBody_Reserved5` | TField |  |  |
| 8 | `OA.DB.RESERVED.4` | `OaDecisionBody_Reserved4` | TField |  |  |
| 9 | `OA.DB.DECISION` | `OaDecisionBody_Decision` |  |  |  |
| 10 | `OA.DB.DECISION.RULE` | `OaDecisionBody_DecisionRule` |  |  |  |
| 11 | `OA.DB.RESERVED.3` | `OaDecisionBody_Reserved3` | TField |  |  |
| 12 | `OA.DB.RESERVED.2` | `OaDecisionBody_Reserved2` | TField |  |  |
| 13 | `OA.DB.RESERVED.1` | `OaDecisionBody_Reserved1` | TField |  |  |
| 14 | `OA.DB.ACTION` | `OaDecisionBody_Action` | TField | No | This field indicates which action will be performed after the record is authorised. Optional Input Allowed values are Null or PUBLISH |
| 15 | `OA.DB.EXPIRY.DATE` | `OaDecisionBody_ExpiryDate` | TField |  | This is the date beyond which the DECISION.BODY represented by the ID of this record can no longer be used. T24 Date Input |
| 16 | `OA.DB.PUBLISH.STATUS` | `OaDecisionBody_PublishStatus` | TField |  | System maintained Noinput field which will contain the result of the publishing effort. |
| 17 | `OA.DB.PUBLISH.ERROR` | `OaDecisionBody_PublishError` |  |  |  |
| 18 | `OA.DB.ERROR.SUGGESTION` | `OaDecisionBody_ErrorSuggestion` |  |  |  |
| 19 | `OA.DB.LOCAL.REF` | `OaDecisionBody_LocalRef` |  |  |  |
| 20 | `OA.DB.RECORD.STATUS` | `OaDecisionBody_RecordStatus` | String |  |  |
| 21 | `OA.DB.CURR.NO` | `OaDecisionBody_CurrNo` | String |  |  |
| 22 | `OA.DB.INPUTTER` | `OaDecisionBody_Inputter` |  |  |  |
| 23 | `OA.DB.DATE.TIME` | `OaDecisionBody_DateTime` |  |  |  |
| 24 | `OA.DB.AUTHORISER` | `OaDecisionBody_Authoriser` | String |  |  |
| 25 | `OA.DB.CO.CODE` | `OaDecisionBody_CoCode` | String |  |  |
| 26 | `OA.DB.DEPT.CODE` | `OaDecisionBody_DeptCode` | String |  |  |
| 27 | `OA.DB.AUDITOR.CODE` | `OaDecisionBody_AuditorCode` | String |  |  |
| 28 | `OA.DB.AUDIT.DATE.TIME` | `OaDecisionBody_AuditDateTime` | String |  |  |
