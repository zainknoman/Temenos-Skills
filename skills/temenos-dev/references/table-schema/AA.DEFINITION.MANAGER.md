# AA.DEFINITION.MANAGER — Table Schema

> Source: `INSERTS/I_F.AA.DEFINITION.MANAGER` in `AF_ClassFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.DEFMAN.DESCRIPTION` | `AaDefinitionManager_Description` |  |  |  |
| 2 | `AA.DEFMAN.FULL.DESC` | `AaDefinitionManager_FullDesc` |  |  |  |
| 3 | `AA.DEFMAN.DOMAIN.TYPE` | `AaDefinitionManager_DomainType` | TField |  | If the object being designed requires a link to existing Domain TYpe, this field will contain the ID to the table OA.DOMAIN.TYPE. Validation Rules: 1) Input should be a valid OA.DOMAIN.TYPE ID. |
| 4 | `AA.DEFMAN.CLASS` | `AaDefinitionManager_Class` |  |  |  |
| 5 | `AA.DEFMAN.INSTANCE` | `AaDefinitionManager_Instance` |  |  |  |
| 6 | `AA.DEFMAN.RESERVED.15` | `AaDefinitionManager_Reserved15` |  |  |  |
| 7 | `AA.DEFMAN.RESERVED.14` | `AaDefinitionManager_Reserved14` |  |  |  |
| 8 | `AA.DEFMAN.RESERVED.13` | `AaDefinitionManager_Reserved13` |  |  |  |
| 9 | `AA.DEFMAN.RESERVED.12` | `AaDefinitionManager_Reserved12` |  |  |  |
| 10 | `AA.DEFMAN.RESERVED.11` | `AaDefinitionManager_Reserved11` |  |  |  |
| 11 | `AA.DEFMAN.CONDITION` | `AaDefinitionManager_Condition` |  |  |  |
| 12 | `AA.DEFMAN.CONDITION.VERSION` | `AaDefinitionManager_ConditionVersion` |  |  |  |
| 13 | `AA.DEFMAN.COMMON.CLASS.TYPE` | `AaDefinitionManager_CommonClassType` |  |  |  |
| 14 | `AA.DEFMAN.COMMON.CLASS` | `AaDefinitionManager_CommonClass` |  |  |  |
| 15 | `AA.DEFMAN.RESERVED.16` | `AaDefinitionManager_Reserved16` |  |  |  |
| 16 | `AA.DEFMAN.COMMON.CLASS.CONDITION` | `AaDefinitionManager_CommonClassCondition` |  |  |  |
| 17 | `AA.DEFMAN.COMMON.CONDITION.VERSION` | `AaDefinitionManager_CommonConditionVersion` |  |  |  |
| 18 | `AA.DEFMAN.SYNC.MAPPING` | `AaDefinitionManager_SyncMapping` | TField |  | This field will allow a user to specify mapping definition used for sync mapping. This field holds a value from AA.MAPPING.TYPE. |
| 19 | `AA.DEFMAN.RESERVED.9` | `AaDefinitionManager_Reserved9` | TField |  |  |
| 20 | `AA.DEFMAN.RESERVED.8` | `AaDefinitionManager_Reserved8` | TField |  |  |
| 21 | `AA.DEFMAN.RESERVED.7` | `AaDefinitionManager_Reserved7` | TField |  |  |
| 22 | `AA.DEFMAN.RESERVED.6` | `AaDefinitionManager_Reserved6` | TField |  |  |
| 23 | `AA.DEFMAN.RESERVED.5` | `AaDefinitionManager_Reserved5` | TField |  |  |
| 24 | `AA.DEFMAN.RESERVED.4` | `AaDefinitionManager_Reserved4` | TField |  |  |
| 25 | `AA.DEFMAN.RESERVED.3` | `AaDefinitionManager_Reserved3` | TField |  |  |
| 26 | `AA.DEFMAN.RESERVED.2` | `AaDefinitionManager_Reserved2` | TField |  |  |
| 27 | `AA.DEFMAN.RESERVED.1` | `AaDefinitionManager_Reserved1` | TField |  |  |
| 28 | `AA.DEFMAN.ACTION` | `AaDefinitionManager_Action` | TField | No | This field indicates action to be performed after the record is authorised 1)Optional Input 2) Validation Rules a. Allowed values are Null of PUBLISH : If action is null the definition is simply being saved on file after authorization.If the Action is PUBLISH then the published record is written in catalog file. |
| 29 | `AA.DEFMAN.EXPIRY.DATE` | `AaDefinitionManager_ExpiryDate` | TField | No | Once defined , the definition Manager Object can be PUBLISHED as many times as needed until it is expired. The definition Manager record is expired by providing a future date in the EXPIRY.DATE field 2)Optional Input 3) Validation Rules a. Date provided should be in the future. b.T24 Date Input |
| 30 | `AA.DEFMAN.PUBLISH.STATUS` | `AaDefinitionManager_PublishStatus` | TField |  | This field will contain the result of the publishing effort 1) Validation Rules a. Non Input. b. System Maintained c. Allowed values are : Completed Successfully or Completed with Errors |
| 31 | `AA.DEFMAN.PUBLISH.ERROR` | `AaDefinitionManager_PublishError` |  |  |  |
| 32 | `AA.DEFMAN.ERROR.SUGGESTION` | `AaDefinitionManager_ErrorSuggestion` |  |  |  |
| 33 | `AA.DEFMAN.LOCAL.REF` | `AaDefinitionManager_LocalRef` |  |  |  |
| 34 | `AA.DEFMAN.CLASS.TYPE` | `AaDefinitionManager_ClassType` | TField |  | Valid entry in AA.CLASS.TYPE. |
| 35 | `AA.DEFMAN.REFERENCE` | `AaDefinitionManager_Reference` | TField |  | This field indicates the name of the Definition Manager Object. The Nature of the Object depends on the CLASS.TYPE that the object uses. For Example if the class type is PROPERTY.CLASS , the object will be a PRODUCT .If the class type is FORMLET.CLASS the object will be a FORM 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part between the first &quot;-&quot; character and the Second &apos;-&apos; character in the ID is the REFERENCE c. Input should be a valid AA.CLASS.TYPE record |
| 36 | `AA.DEFMAN.VERSION` | `AaDefinitionManager_Version` | TField |  | The Version being defined (PRODUCT, FORM) is always &quot;VERSIONNED&quot; . This means that more than one version of the same exist in the system. Depending on the nature of the object, updates may be performed on existing version without the need to advance the object to its NEXT VERSION in the sequence. 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part between the second &quot;-&quot; character and the third &apos;-&apos; character in the ID is the VERSION |
| 37 | `AA.DEFMAN.VERSION.DATE` | `AaDefinitionManager_VersionDate` | TField |  | This field indicates the EFFECTIVE.DATE for the VERSION of the object being defined (PRODUCT, FORM etc.). Where more than one record exist on file for the object , the run-time processing will refer to the VERSION.DATE in order to determine which version of the OBJECT is applicable on the day 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part after the last &quot;-&quot; character in the ID is the VERSION.DATE |
| 38 | `AA.DEFMAN.OVERRIDE` | `AaDefinitionManager_Override` |  |  |  |
| 39 | `AA.DEFMAN.RECORD.STATUS` | `AaDefinitionManager_RecordStatus` | String |  |  |
| 40 | `AA.DEFMAN.CURR.NO` | `AaDefinitionManager_CurrNo` | String |  |  |
| 41 | `AA.DEFMAN.INPUTTER` | `AaDefinitionManager_Inputter` |  |  |  |
| 42 | `AA.DEFMAN.DATE.TIME` | `AaDefinitionManager_DateTime` |  |  |  |
| 43 | `AA.DEFMAN.AUTHORISER` | `AaDefinitionManager_Authoriser` | String |  |  |
| 44 | `AA.DEFMAN.CO.CODE` | `AaDefinitionManager_CoCode` | String |  |  |
| 45 | `AA.DEFMAN.DEPT.CODE` | `AaDefinitionManager_DeptCode` | String |  |  |
| 46 | `AA.DEFMAN.AUDITOR.CODE` | `AaDefinitionManager_AuditorCode` | String |  |  |
| 47 | `AA.DEFMAN.AUDIT.DATE.TIME` | `AaDefinitionManager_AuditDateTime` | String |  |  |
| 48 | `AA.DEFMAN.FORM.OWNER` | `AaDefinitionManager_FormOwner` | TField |  | By default, this Role will be the owner of the entire form.Must be valid ID from OA.ROLE.Input allowed only if the CLASS.TYPE is FORMLET.CLASS |
| 49 | `AA.DEFMAN.DEFAULT.ROLE` | `AaDefinitionManager_DefaultRole` |  |  |  |
| 50 | `AA.DEFMAN.DEFAULT.PRIVILEGE` | `AaDefinitionManager_DefaultPrivilege` |  |  |  |
| 51 | `AA.DEFMAN.OWNER` | `AaDefinitionManager_Owner` |  |  |  |
| 52 | `AA.DEFMAN.ROLE` | `AaDefinitionManager_Role` |  |  |  |
| 53 | `AA.DEFMAN.PRIVILEGE` | `AaDefinitionManager_Privilege` |  |  |  |
