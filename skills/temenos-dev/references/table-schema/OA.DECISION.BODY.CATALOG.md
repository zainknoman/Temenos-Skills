# OA.DECISION.BODY.CATALOG — Table Schema

> Source: `INSERTS/I_F.OA.DECISION.BODY.CATALOG` in `OA_Decision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DBC.DESCRIPTION` | `OaDecisionBodyCatalog_Description` |  |  |  |
| 2 | `OA.DBC.FULL.DESCRIPTION` | `OaDecisionBodyCatalog_FullDescription` |  |  |  |
| 3 | `OA.DBC.ROLE` | `OaDecisionBodyCatalog_Role` |  |  |  |
| 4 | `OA.DBC.USER` | `OaDecisionBodyCatalog_User` |  |  |  |
| 5 | `OA.DBC.DEPARTMENT` | `OaDecisionBodyCatalog_Department` |  |  |  |
| 6 | `OA.DBC.REFER.ALLOWED` | `OaDecisionBodyCatalog_ReferAllowed` | TField |  |  |
| 7 | `OA.DBC.RESERVED.5` | `OaDecisionBodyCatalog_Reserved5` | TField |  |  |
| 8 | `OA.DBC.RESERVED.4` | `OaDecisionBodyCatalog_Reserved4` | TField |  |  |
| 9 | `OA.DBC.DECISION` | `OaDecisionBodyCatalog_Decision` |  |  |  |
| 10 | `OA.DBC.DECISION.RULE` | `OaDecisionBodyCatalog_DecisionRule` |  |  |  |
| 11 | `OA.DBC.RESERVED.3` | `OaDecisionBodyCatalog_Reserved3` | TField |  |  |
| 12 | `OA.DBC.RESERVED.2` | `OaDecisionBodyCatalog_Reserved2` | TField |  |  |
| 13 | `OA.DBC.RESERVED.1` | `OaDecisionBodyCatalog_Reserved1` | TField |  |  |
| 14 | `OA.DBC.ACTION` | `OaDecisionBodyCatalog_Action` | TField | No | This field indicates which action will be performed after the record is authorised. Optional Input Allowed values are Null or PUBLISH |
| 15 | `OA.DBC.EXPIRY.DATE` | `OaDecisionBodyCatalog_ExpiryDate` | TField |  | This is the date beyond which the DECISION.BODY represented by the ID of this record can no longer be used. T24 Date Input |
| 16 | `OA.DBC.PUBLISH.STATUS` | `OaDecisionBodyCatalog_PublishStatus` | TField |  | System maintained Noinput field which will contain the result of the publishing effort. |
| 17 | `OA.DBC.PUBLISH.ERROR` | `OaDecisionBodyCatalog_PublishError` |  |  |  |
| 18 | `OA.DBC.ERROR.SUGGESTION` | `OaDecisionBodyCatalog_ErrorSuggestion` |  |  |  |
| 19 | `OA.DBC.LOCAL.REF` | `OaDecisionBodyCatalog_LocalRef` |  |  |  |
| 20 | `OA.DBC.RECORD.STATUS` | `OaDecisionBodyCatalog_RecordStatus` | String |  |  |
| 21 | `OA.DBC.CURR.NO` | `OaDecisionBodyCatalog_CurrNo` | String |  |  |
| 22 | `OA.DBC.INPUTTER` | `OaDecisionBodyCatalog_Inputter` |  |  |  |
| 23 | `OA.DBC.DATE.TIME` | `OaDecisionBodyCatalog_DateTime` |  |  |  |
| 24 | `OA.DBC.AUTHORISER` | `OaDecisionBodyCatalog_Authoriser` | String |  |  |
| 25 | `OA.DBC.CO.CODE` | `OaDecisionBodyCatalog_CoCode` | String |  |  |
| 26 | `OA.DBC.DEPT.CODE` | `OaDecisionBodyCatalog_DeptCode` | String |  |  |
| 27 | `OA.DBC.AUDITOR.CODE` | `OaDecisionBodyCatalog_AuditorCode` | String |  |  |
| 28 | `OA.DBC.AUDIT.DATE.TIME` | `OaDecisionBodyCatalog_AuditDateTime` | String |  |  |
