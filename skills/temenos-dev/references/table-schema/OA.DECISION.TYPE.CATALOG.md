# OA.DECISION.TYPE.CATALOG — Table Schema

> Source: `INSERTS/I_F.OA.DECISION.TYPE.CATALOG` in `OA_Decision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DTC.DESCRIPTION` | `OaDecisionTypeCatalog_Description` |  |  |  |
| 2 | `OA.DTC.FULL.DESC` | `OaDecisionTypeCatalog_FullDesc` |  |  |  |
| 3 | `OA.DTC.DOMAIN.TYPE` | `OaDecisionTypeCatalog_DomainType` | TField |  | Used for Form Definition to specify which domain type the form is used in and therefore will default the Instances (i.e. the formlets) in the domain type into the mv set. |
| 4 | `OA.DTC.CLASS` | `OaDecisionTypeCatalog_Class` |  |  |  |
| 5 | `OA.DTC.INSTANCE` | `OaDecisionTypeCatalog_Instance` |  |  |  |
| 6 | `OA.DTC.RESERVED.15` | `OaDecisionTypeCatalog_Reserved15` |  |  |  |
| 7 | `OA.DTC.RESERVED.14` | `OaDecisionTypeCatalog_Reserved14` |  |  |  |
| 8 | `OA.DTC.RESERVED.13` | `OaDecisionTypeCatalog_Reserved13` |  |  |  |
| 9 | `OA.DTC.RESERVED.12` | `OaDecisionTypeCatalog_Reserved12` |  |  |  |
| 10 | `OA.DTC.RESERVED.11` | `OaDecisionTypeCatalog_Reserved11` |  |  |  |
| 11 | `OA.DTC.CONDITION` | `OaDecisionTypeCatalog_Condition` |  |  |  |
| 12 | `OA.DTC.CONDITION.VERSION` | `OaDecisionTypeCatalog_ConditionVersion` |  |  |  |
| 13 | `OA.DTC.COMMON.CLASS.TYPE` | `OaDecisionTypeCatalog_CommonClassType` |  |  |  |
| 14 | `OA.DTC.COMMON.CLASS` | `OaDecisionTypeCatalog_CommonClass` |  |  |  |
| 15 | `OA.DTC.RESERVED.16` | `OaDecisionTypeCatalog_Reserved16` |  |  |  |
| 16 | `OA.DTC.COMMON.CLASS.CONDITION` | `OaDecisionTypeCatalog_CommonClassCondition` |  |  |  |
| 17 | `OA.DTC.COMMON.CONDITION.VERSION` | `OaDecisionTypeCatalog_CommonConditionVersion` |  |  |  |
| 18 | `OA.DTC.SYNC.MAPPING` | `OaDecisionTypeCatalog_SyncMapping` | TField |  | This field will allow a user to specify which mapping definition to use when syncing data for the form. |
| 19 | `OA.DTC.RESERVED.9` | `OaDecisionTypeCatalog_Reserved9` | TField |  |  |
| 20 | `OA.DTC.RESERVED.8` | `OaDecisionTypeCatalog_Reserved8` | TField |  |  |
| 21 | `OA.DTC.RESERVED.7` | `OaDecisionTypeCatalog_Reserved7` | TField |  |  |
| 22 | `OA.DTC.RESERVED.6` | `OaDecisionTypeCatalog_Reserved6` | TField |  |  |
| 23 | `OA.DTC.RESERVED.5` | `OaDecisionTypeCatalog_Reserved5` | TField |  |  |
| 24 | `OA.DTC.RESERVED.4` | `OaDecisionTypeCatalog_Reserved4` | TField |  |  |
| 25 | `OA.DTC.RESERVED.3` | `OaDecisionTypeCatalog_Reserved3` | TField |  |  |
| 26 | `OA.DTC.RESERVED.2` | `OaDecisionTypeCatalog_Reserved2` | TField |  |  |
| 27 | `OA.DTC.RESERVED.1` | `OaDecisionTypeCatalog_Reserved1` | TField |  |  |
| 28 | `OA.DTC.ACTION` | `OaDecisionTypeCatalog_Action` | TField |  | Allowed options are 1. &quot;Null&quot;- the record is simply being updated. 2. PUBLISH - record is proofed and published. |
| 29 | `OA.DTC.EXPIRY.DATE` | `OaDecisionTypeCatalog_ExpiryDate` | TField |  | Date from which the Decision type will no longer be available for use. |
| 30 | `OA.DTC.PUBLISH.STATUS` | `OaDecisionTypeCatalog_PublishStatus` | TField |  | This field will contain the result of the publishing effort. Validation Rules - Non Inputtable, System Maintained, Allowed values are : Completed Successfully or Completed with Errors. |
| 31 | `OA.DTC.PUBLISH.ERROR` | `OaDecisionTypeCatalog_PublishError` |  |  |  |
| 32 | `OA.DTC.ERROR.SUGGESTION` | `OaDecisionTypeCatalog_ErrorSuggestion` |  |  |  |
| 33 | `OA.DTC.LOCAL.REF` | `OaDecisionTypeCatalog_LocalRef` |  |  |  |
| 34 | `OA.DTC.CLASS.TYPE` | `OaDecisionTypeCatalog_ClassType` | TField |  | Valid entry in AA.CLASS.TYPE. |
| 35 | `OA.DTC.REFERENCE` | `OaDecisionTypeCatalog_Reference` | TField |  | ID Component 2: Is the main &quot;ID&quot; of the item being designed. For decision this is the name of the decision type. |
| 36 | `OA.DTC.VERSION` | `OaDecisionTypeCatalog_Version` | TField |  | ID Component 3: Version number identifier. |
| 37 | `OA.DTC.VERSION.DATE` | `OaDecisionTypeCatalog_VersionDate` | TField |  | ID Component 4: Date when the version becomes effective. |
| 38 | `OA.DTC.OVERRIDE` | `OaDecisionTypeCatalog_Override` |  |  |  |
| 39 | `OA.DTC.RECORD.STATUS` | `OaDecisionTypeCatalog_RecordStatus` | String |  |  |
| 40 | `OA.DTC.CURR.NO` | `OaDecisionTypeCatalog_CurrNo` | String |  |  |
| 41 | `OA.DTC.INPUTTER` | `OaDecisionTypeCatalog_Inputter` |  |  |  |
| 42 | `OA.DTC.DATE.TIME` | `OaDecisionTypeCatalog_DateTime` |  |  |  |
| 43 | `OA.DTC.AUTHORISER` | `OaDecisionTypeCatalog_Authoriser` | String |  |  |
| 44 | `OA.DTC.CO.CODE` | `OaDecisionTypeCatalog_CoCode` | String |  |  |
| 45 | `OA.DTC.DEPT.CODE` | `OaDecisionTypeCatalog_DeptCode` | String |  |  |
| 46 | `OA.DTC.AUDITOR.CODE` | `OaDecisionTypeCatalog_AuditorCode` | String |  |  |
| 47 | `OA.DTC.AUDIT.DATE.TIME` | `OaDecisionTypeCatalog_AuditDateTime` | String |  |  |
| 48 | `OA.DTC.FORM.OWNER` | `OaDecisionTypeCatalog_FormOwner` | TField |  |  |
| 49 | `OA.DTC.DEFAULT.ROLE` | `OaDecisionTypeCatalog_DefaultRole` |  |  |  |
| 50 | `OA.DTC.DEFAULT.PRIVILEGE` | `OaDecisionTypeCatalog_DefaultPrivilege` |  |  |  |
| 51 | `OA.DTC.OWNER` | `OaDecisionTypeCatalog_Owner` |  |  |  |
| 52 | `OA.DTC.ROLE` | `OaDecisionTypeCatalog_Role` |  |  |  |
| 53 | `OA.DTC.PRIVILEGE` | `OaDecisionTypeCatalog_Privilege` |  |  |  |
