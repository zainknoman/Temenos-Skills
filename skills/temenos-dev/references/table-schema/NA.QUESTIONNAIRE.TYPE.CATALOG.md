# NA.QUESTIONNAIRE.TYPE.CATALOG — Table Schema

> Source: `INSERTS/I_F.NA.QUESTIONNAIRE.TYPE.CATALOG` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.QTCAT.DESCRIPTION` | `NaQuestionnaireTypeCatalog_Description` |  |  |  |
| 2 | `NA.QTCAT.FULL.DESC` | `NaQuestionnaireTypeCatalog_FullDesc` |  |  |  |
| 3 | `NA.QTCAT.DOMAIN.TYPE` | `NaQuestionnaireTypeCatalog_DomainType` | TField |  | Used for Form Definition to specify which domain type the form is used in and therefore will default the Instances (i.e. the formlets) in the domain type into the mv set. |
| 4 | `NA.QTCAT.CLASS` | `NaQuestionnaireTypeCatalog_Class` |  |  |  |
| 5 | `NA.QTCAT.INSTANCE` | `NaQuestionnaireTypeCatalog_Instance` |  |  |  |
| 6 | `NA.QTCAT.RESERVED.15` | `NaQuestionnaireTypeCatalog_Reserved15` |  |  |  |
| 7 | `NA.QTCAT.RESERVED.14` | `NaQuestionnaireTypeCatalog_Reserved14` |  |  |  |
| 8 | `NA.QTCAT.RESERVED.13` | `NaQuestionnaireTypeCatalog_Reserved13` |  |  |  |
| 9 | `NA.QTCAT.RESERVED.12` | `NaQuestionnaireTypeCatalog_Reserved12` |  |  |  |
| 10 | `NA.QTCAT.RESERVED.11` | `NaQuestionnaireTypeCatalog_Reserved11` |  |  |  |
| 11 | `NA.QTCAT.CONDITION` | `NaQuestionnaireTypeCatalog_Condition` |  |  |  |
| 12 | `NA.QTCAT.CONDITION.VERSION` | `NaQuestionnaireTypeCatalog_ConditionVersion` |  |  |  |
| 13 | `NA.QTCAT.COMMON.CLASS.TYPE` | `NaQuestionnaireTypeCatalog_CommonClassType` |  |  |  |
| 14 | `NA.QTCAT.COMMON.CLASS` | `NaQuestionnaireTypeCatalog_CommonClass` |  |  |  |
| 15 | `NA.QTCAT.RESERVED.16` | `NaQuestionnaireTypeCatalog_Reserved16` |  |  |  |
| 16 | `NA.QTCAT.COMMON.CLASS.CONDITION` | `NaQuestionnaireTypeCatalog_CommonClassCondition` |  |  |  |
| 17 | `NA.QTCAT.COMMON.CONDITION.VERSION` | `NaQuestionnaireTypeCatalog_CommonConditionVersion` |  |  |  |
| 18 | `NA.QTCAT.SYNC.MAPPING` | `NaQuestionnaireTypeCatalog_SyncMapping` | TField |  | This field will allow a user to specify which mapping definition to use when syncing data for the form. |
| 19 | `NA.QTCAT.RESERVED.9` | `NaQuestionnaireTypeCatalog_Reserved9` | TField |  |  |
| 20 | `NA.QTCAT.RESERVED.8` | `NaQuestionnaireTypeCatalog_Reserved8` | TField |  |  |
| 21 | `NA.QTCAT.RESERVED.7` | `NaQuestionnaireTypeCatalog_Reserved7` | TField |  |  |
| 22 | `NA.QTCAT.RESERVED.6` | `NaQuestionnaireTypeCatalog_Reserved6` | TField |  |  |
| 23 | `NA.QTCAT.RESERVED.5` | `NaQuestionnaireTypeCatalog_Reserved5` | TField |  |  |
| 24 | `NA.QTCAT.RESERVED.4` | `NaQuestionnaireTypeCatalog_Reserved4` | TField |  |  |
| 25 | `NA.QTCAT.RESERVED.3` | `NaQuestionnaireTypeCatalog_Reserved3` | TField |  |  |
| 26 | `NA.QTCAT.RESERVED.2` | `NaQuestionnaireTypeCatalog_Reserved2` | TField |  |  |
| 27 | `NA.QTCAT.RESERVED.1` | `NaQuestionnaireTypeCatalog_Reserved1` | TField |  |  |
| 28 | `NA.QTCAT.ACTION` | `NaQuestionnaireTypeCatalog_Action` | TField |  | Allowed options are 1. &quot;Null&quot;- the record is simply being updated. 2. PUBLISH - record is proofed and published. |
| 29 | `NA.QTCAT.EXPIRY.DATE` | `NaQuestionnaireTypeCatalog_ExpiryDate` | TField |  | Date from which the resultant Questionnaire type will no longer be available for use. |
| 30 | `NA.QTCAT.PUBLISH.STATUS` | `NaQuestionnaireTypeCatalog_PublishStatus` | TField |  | This field will contain the result of the publishing effort. Validation Rules - Non Inputtable, System Maintained, Allowed values are : Completed Successfully or Completed with Errors. |
| 31 | `NA.QTCAT.PUBLISH.ERROR` | `NaQuestionnaireTypeCatalog_PublishError` |  |  |  |
| 32 | `NA.QTCAT.ERROR.SUGGESTION` | `NaQuestionnaireTypeCatalog_ErrorSuggestion` |  |  |  |
| 33 | `NA.QTCAT.LOCAL.REF` | `NaQuestionnaireTypeCatalog_LocalRef` |  |  |  |
| 34 | `NA.QTCAT.CLASS.TYPE` | `NaQuestionnaireTypeCatalog_ClassType` | TField |  | Valid entry in AA.CLASS.TYPE. |
| 35 | `NA.QTCAT.REFERENCE` | `NaQuestionnaireTypeCatalog_Reference` | TField |  | ID Component 2: Is the main &quot;ID&quot; of the item being designed. For questionnaire this is the name of the questionnaire type |
| 36 | `NA.QTCAT.VERSION` | `NaQuestionnaireTypeCatalog_Version` | TField |  | ID Component 3: Version number identifier. |
| 37 | `NA.QTCAT.VERSION.DATE` | `NaQuestionnaireTypeCatalog_VersionDate` | TField |  | ID Component 4: Date when the version becomes effective. |
| 38 | `NA.QTCAT.OVERRIDE` | `NaQuestionnaireTypeCatalog_Override` |  |  |  |
| 39 | `NA.QTCAT.RECORD.STATUS` | `NaQuestionnaireTypeCatalog_RecordStatus` | String |  |  |
| 40 | `NA.QTCAT.CURR.NO` | `NaQuestionnaireTypeCatalog_CurrNo` | String |  |  |
| 41 | `NA.QTCAT.INPUTTER` | `NaQuestionnaireTypeCatalog_Inputter` |  |  |  |
| 42 | `NA.QTCAT.DATE.TIME` | `NaQuestionnaireTypeCatalog_DateTime` |  |  |  |
| 43 | `NA.QTCAT.AUTHORISER` | `NaQuestionnaireTypeCatalog_Authoriser` | String |  |  |
| 44 | `NA.QTCAT.CO.CODE` | `NaQuestionnaireTypeCatalog_CoCode` | String |  |  |
| 45 | `NA.QTCAT.DEPT.CODE` | `NaQuestionnaireTypeCatalog_DeptCode` | String |  |  |
| 46 | `NA.QTCAT.AUDITOR.CODE` | `NaQuestionnaireTypeCatalog_AuditorCode` | String |  |  |
| 47 | `NA.QTCAT.AUDIT.DATE.TIME` | `NaQuestionnaireTypeCatalog_AuditDateTime` | String |  |  |
| 48 | `NA.QTCAT.FORM.OWNER` | `NaQuestionnaireTypeCatalog_FormOwner` | TField |  |  |
| 49 | `NA.QTCAT.DEFAULT.ROLE` | `NaQuestionnaireTypeCatalog_DefaultRole` |  |  |  |
| 50 | `NA.QTCAT.DEFAULT.PRIVILEGE` | `NaQuestionnaireTypeCatalog_DefaultPrivilege` |  |  |  |
| 51 | `NA.QTCAT.OWNER` | `NaQuestionnaireTypeCatalog_Owner` |  |  |  |
| 52 | `NA.QTCAT.ROLE` | `NaQuestionnaireTypeCatalog_Role` |  |  |  |
| 53 | `NA.QTCAT.PRIVILEGE` | `NaQuestionnaireTypeCatalog_Privilege` |  |  |  |
