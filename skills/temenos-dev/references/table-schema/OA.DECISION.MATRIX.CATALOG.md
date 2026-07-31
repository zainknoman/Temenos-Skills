# OA.DECISION.MATRIX.CATALOG — Table Schema

> Source: `INSERTS/I_F.OA.DECISION.MATRIX.CATALOG` in `OA_Decision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DMC.DESCRIPTION` | `OaDecisionMatrixCatalog_Description` |  |  |  |
| 2 | `OA.DMC.FULL.DESCRIPTION` | `OaDecisionMatrixCatalog_FullDescription` |  |  |  |
| 3 | `OA.DMC.RESERVED.10` | `OaDecisionMatrixCatalog_Reserved10` | TField |  |  |
| 4 | `OA.DMC.RULE.DESCRIPTION` | `OaDecisionMatrixCatalog_RuleDescription` |  |  |  |
| 5 | `OA.DMC.RULE` | `OaDecisionMatrixCatalog_Rule` |  |  |  |
| 6 | `OA.DMC.RULE.ID` | `OaDecisionMatrixCatalog_RuleId` |  |  |  |
| 7 | `OA.DMC.RESERVED.9` | `OaDecisionMatrixCatalog_Reserved9` |  |  |  |
| 8 | `OA.DMC.RESERVED.8` | `OaDecisionMatrixCatalog_Reserved8` |  |  |  |
| 9 | `OA.DMC.DECISION.BODY` | `OaDecisionMatrixCatalog_DecisionBody` |  |  |  |
| 10 | `OA.DMC.DECISION.MATRIX` | `OaDecisionMatrixCatalog_DecisionMatrix` |  |  |  |
| 11 | `OA.DMC.DECISION` | `OaDecisionMatrixCatalog_Decision` |  |  |  |
| 12 | `OA.DMC.RESERVED.7` | `OaDecisionMatrixCatalog_Reserved7` |  |  |  |
| 13 | `OA.DMC.RESERVED.6` | `OaDecisionMatrixCatalog_Reserved6` |  |  |  |
| 14 | `OA.DMC.NEXT.BODY` | `OaDecisionMatrixCatalog_NextBody` |  |  |  |
| 15 | `OA.DMC.NEXT.MATRIX` | `OaDecisionMatrixCatalog_NextMatrix` |  |  |  |
| 16 | `OA.DMC.RESERVED.5` | `OaDecisionMatrixCatalog_Reserved5` | TField |  |  |
| 17 | `OA.DMC.RESERVED.4` | `OaDecisionMatrixCatalog_Reserved4` | TField |  |  |
| 18 | `OA.DMC.RESERVED.3` | `OaDecisionMatrixCatalog_Reserved3` | TField |  |  |
| 19 | `OA.DMC.DEFAULT.BODY` | `OaDecisionMatrixCatalog_DefaultBody` | TField |  | DEFAULT.BODY, DEFAULT.MATRIX and DEFAULT.DECISION fields are mutually exclusive, Any one of the fields must be specified. Default decision body. |
| 20 | `OA.DMC.DEFAULT.MATRIX` | `OaDecisionMatrixCatalog_DefaultMatrix` | TField |  | DEFAULT.BODY, DEFAULT.MATRIX and DEFAULT.DECISION fields are mutually exclusive, Any one of the fields must be specified. Default decision matrix. |
| 21 | `OA.DMC.DEFAULT.DECISION` | `OaDecisionMatrixCatalog_DefaultDecision` | TField |  | DEFAULT.BODY, DEFAULT.MATRIX and DEFAULT.DECISION fields are mutually exclusive, Any one of the fields must be specified. Default decision. |
| 22 | `OA.DMC.RESERVED.2` | `OaDecisionMatrixCatalog_Reserved2` | TField |  |  |
| 23 | `OA.DMC.RESERVED.1` | `OaDecisionMatrixCatalog_Reserved1` | TField |  |  |
| 24 | `OA.DMC.ACTION` | `OaDecisionMatrixCatalog_Action` | TField | No | This field indicates which action will be performed after the record is authorised. Optional Input Allowed values are Null or PUBLISH |
| 25 | `OA.DMC.EXPIRY.DATE` | `OaDecisionMatrixCatalog_ExpiryDate` | TField |  | This is the date beyond which the DECISION.MATRIX represented by the ID of this record can no longer be used. |
| 26 | `OA.DMC.PUBLISH.STATUS` | `OaDecisionMatrixCatalog_PublishStatus` | TField |  | System maintained Noinput field which will contain the result of the publishing effort. |
| 27 | `OA.DMC.PUBLISH.ERROR` | `OaDecisionMatrixCatalog_PublishError` |  |  |  |
| 28 | `OA.DMC.ERROR.SUGGESTION` | `OaDecisionMatrixCatalog_ErrorSuggestion` |  |  |  |
| 29 | `OA.DMC.LOCAL.REF` | `OaDecisionMatrixCatalog_LocalRef` |  |  |  |
| 30 | `OA.DMC.RECORD.STATUS` | `OaDecisionMatrixCatalog_RecordStatus` | String |  |  |
| 31 | `OA.DMC.CURR.NO` | `OaDecisionMatrixCatalog_CurrNo` | String |  |  |
| 32 | `OA.DMC.INPUTTER` | `OaDecisionMatrixCatalog_Inputter` |  |  |  |
| 33 | `OA.DMC.DATE.TIME` | `OaDecisionMatrixCatalog_DateTime` |  |  |  |
| 34 | `OA.DMC.AUTHORISER` | `OaDecisionMatrixCatalog_Authoriser` | String |  |  |
| 35 | `OA.DMC.CO.CODE` | `OaDecisionMatrixCatalog_CoCode` | String |  |  |
| 36 | `OA.DMC.DEPT.CODE` | `OaDecisionMatrixCatalog_DeptCode` | String |  |  |
| 37 | `OA.DMC.AUDITOR.CODE` | `OaDecisionMatrixCatalog_AuditorCode` | String |  |  |
| 38 | `OA.DMC.AUDIT.DATE.TIME` | `OaDecisionMatrixCatalog_AuditDateTime` | String |  |  |
