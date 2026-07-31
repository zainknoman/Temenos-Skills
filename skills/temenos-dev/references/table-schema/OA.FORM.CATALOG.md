# OA.FORM.CATALOG — Table Schema

> Source: `INSERTS/I_F.OA.FORM.CATALOG` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.FCAT.DESCRIPTION` | `OaFormCatalog_Description` |  |  |  |
| 2 | `OA.FCAT.FULL.DESC` | `OaFormCatalog_FullDesc` |  |  |  |
| 3 | `OA.FCAT.DOMAIN.TYPE` | `OaFormCatalog_DomainType` | TField |  | Used for Form Definition to specify which domain type the form is used in and therefore will default the Instances (i.e. the formlets) in the domain type into the mv set. |
| 4 | `OA.FCAT.CLASS` | `OaFormCatalog_Class` |  |  |  |
| 5 | `OA.FCAT.INSTANCE` | `OaFormCatalog_Instance` |  |  |  |
| 6 | `OA.FCAT.RESERVED.15` | `OaFormCatalog_Reserved15` |  |  |  |
| 7 | `OA.FCAT.RESERVED.14` | `OaFormCatalog_Reserved14` |  |  |  |
| 8 | `OA.FCAT.RESERVED.13` | `OaFormCatalog_Reserved13` |  |  |  |
| 9 | `OA.FCAT.RESERVED.12` | `OaFormCatalog_Reserved12` |  |  |  |
| 10 | `OA.FCAT.RESERVED.11` | `OaFormCatalog_Reserved11` |  |  |  |
| 11 | `OA.FCAT.CONDITION` | `OaFormCatalog_Condition` |  |  |  |
| 12 | `OA.FCAT.CONDITION.VERSION` | `OaFormCatalog_ConditionVersion` |  |  |  |
| 13 | `OA.FCAT.COMMON.CLASS.TYPE` | `OaFormCatalog_CommonClassType` |  |  |  |
| 14 | `OA.FCAT.COMMON.CLASS` | `OaFormCatalog_CommonClass` |  |  |  |
| 15 | `OA.FCAT.RESERVED.16` | `OaFormCatalog_Reserved16` |  |  |  |
| 16 | `OA.FCAT.COMMON.CLASS.CONDITION` | `OaFormCatalog_CommonClassCondition` |  |  |  |
| 17 | `OA.FCAT.COMMON.CONDITION.VERSION` | `OaFormCatalog_CommonConditionVersion` |  |  |  |
| 18 | `OA.FCAT.SYNC.MAPPING` | `OaFormCatalog_SyncMapping` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 19 | `OA.FCAT.RESERVED.9` | `OaFormCatalog_Reserved9` | TField |  |  |
| 20 | `OA.FCAT.RESERVED.8` | `OaFormCatalog_Reserved8` | TField |  |  |
| 21 | `OA.FCAT.RESERVED.7` | `OaFormCatalog_Reserved7` | TField |  |  |
| 22 | `OA.FCAT.RESERVED.6` | `OaFormCatalog_Reserved6` | TField |  |  |
| 23 | `OA.FCAT.RESERVED.5` | `OaFormCatalog_Reserved5` | TField |  |  |
| 24 | `OA.FCAT.RESERVED.4` | `OaFormCatalog_Reserved4` | TField |  |  |
| 25 | `OA.FCAT.RESERVED.3` | `OaFormCatalog_Reserved3` | TField |  |  |
| 26 | `OA.FCAT.RESERVED.2` | `OaFormCatalog_Reserved2` | TField |  |  |
| 27 | `OA.FCAT.RESERVED.1` | `OaFormCatalog_Reserved1` | TField |  |  |
| 28 | `OA.FCAT.ACTION` | `OaFormCatalog_Action` | TField | No | This field indicates which action will be performed after the record is authorised 2)Optional Input 3) Validation Rules a. Allowed values are Null of PUBLISH : If action is null the definition is simply being saved on file after authorization. If PUBLISH is specified , this will have similar effect as PROOF AND PUBLISH actions of FORM.DESIGNER.The specific meaning of the PUBLISH action depends on the CLASS.TYPE of the object being defined. b.T24 string Input |
| 29 | `OA.FCAT.EXPIRY.DATE` | `OaFormCatalog_ExpiryDate` | TField |  | Date from which the resultant form will no longer be available for use. |
| 30 | `OA.FCAT.PUBLISH.STATUS` | `OaFormCatalog_PublishStatus` | TField |  | This field will contain the result of the publishing effort. Validation Rules - Non Inputtable, System Maintained, Allowed values are : Completed Successfully or Completed with Errors. |
| 31 | `OA.FCAT.PUBLISH.ERROR` | `OaFormCatalog_PublishError` |  |  |  |
| 32 | `OA.FCAT.ERROR.SUGGESTION` | `OaFormCatalog_ErrorSuggestion` |  |  |  |
| 33 | `OA.FCAT.LOCAL.REF` | `OaFormCatalog_LocalRef` |  |  |  |
| 34 | `OA.FCAT.CLASS.TYPE` | `OaFormCatalog_ClassType` | TField |  | Valid entry in AA.CLASS.TYPE. |
| 35 | `OA.FCAT.REFERENCE` | `OaFormCatalog_Reference` | TField |  | ID Component 2: Is the main &quot;ID&quot; of the item being designed. For questionnaire this is the name of the questionnaire type |
| 36 | `OA.FCAT.VERSION` | `OaFormCatalog_Version` | TField |  | ID Component 3: Version number identifier. |
| 37 | `OA.FCAT.VERSION.DATE` | `OaFormCatalog_VersionDate` | TField |  | ID Component 4: Date when the version becomes effective. |
| 38 | `OA.FCAT.OVERRIDE` | `OaFormCatalog_Override` |  |  |  |
| 39 | `OA.FCAT.RECORD.STATUS` | `OaFormCatalog_RecordStatus` | String |  |  |
| 40 | `OA.FCAT.CURR.NO` | `OaFormCatalog_CurrNo` | String |  |  |
| 41 | `OA.FCAT.INPUTTER` | `OaFormCatalog_Inputter` |  |  |  |
| 42 | `OA.FCAT.DATE.TIME` | `OaFormCatalog_DateTime` |  |  |  |
| 43 | `OA.FCAT.AUTHORISER` | `OaFormCatalog_Authoriser` | String |  |  |
| 44 | `OA.FCAT.CO.CODE` | `OaFormCatalog_CoCode` | String |  |  |
| 45 | `OA.FCAT.DEPT.CODE` | `OaFormCatalog_DeptCode` | String |  |  |
| 46 | `OA.FCAT.AUDITOR.CODE` | `OaFormCatalog_AuditorCode` | String |  |  |
| 47 | `OA.FCAT.AUDIT.DATE.TIME` | `OaFormCatalog_AuditDateTime` | String |  |  |
| 48 | `OA.FCAT.FORM.OWNER` | `OaFormCatalog_FormOwner` | TField |  |  |
| 49 | `OA.FCAT.DEFAULT.ROLE` | `OaFormCatalog_DefaultRole` |  |  |  |
| 50 | `OA.FCAT.DEFAULT.PRIVILEGE` | `OaFormCatalog_DefaultPrivilege` |  |  |  |
| 51 | `OA.FCAT.OWNER` | `OaFormCatalog_Owner` |  |  |  |
| 52 | `OA.FCAT.ROLE` | `OaFormCatalog_Role` |  |  |  |
| 53 | `OA.FCAT.PRIVILEGE` | `OaFormCatalog_Privilege` |  |  |  |
