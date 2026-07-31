# AA.INTERFACE.TYPE.CATALOG — Table Schema

> Source: `INSERTS/I_F.AA.INTERFACE.TYPE.CATALOG` in `AF_ClassInterfaces.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.INTC.DESCRIPTION` | `AaInterfaceTypeCatalog_Description` |  |  |  |
| 2 | `AA.INTC.FULL.DESC` | `AaInterfaceTypeCatalog_FullDesc` |  |  |  |
| 3 | `AA.INTC.DOMAIN.TYPE` | `AaInterfaceTypeCatalog_DomainType` | TField |  | If the object being designed requires a link to existing Domain TYpe, this field will contain the ID to the table OA.DOMAIN.TYPE. Validation Rules: 1) Input should be a valid OA.DOMAIN.TYPE ID. |
| 4 | `AA.INTC.CLASS` | `AaInterfaceTypeCatalog_Class` |  |  |  |
| 5 | `AA.INTC.INSTANCE` | `AaInterfaceTypeCatalog_Instance` |  |  |  |
| 6 | `AA.INTC.RESERVED.15` | `AaInterfaceTypeCatalog_Reserved15` |  |  |  |
| 7 | `AA.INTC.RESERVED.14` | `AaInterfaceTypeCatalog_Reserved14` |  |  |  |
| 8 | `AA.INTC.RESERVED.13` | `AaInterfaceTypeCatalog_Reserved13` |  |  |  |
| 9 | `AA.INTC.RESERVED.12` | `AaInterfaceTypeCatalog_Reserved12` |  |  |  |
| 10 | `AA.INTC.RESERVED.11` | `AaInterfaceTypeCatalog_Reserved11` |  |  |  |
| 11 | `AA.INTC.CONDITION` | `AaInterfaceTypeCatalog_Condition` |  |  |  |
| 12 | `AA.INTC.CONDITION.VERSION` | `AaInterfaceTypeCatalog_ConditionVersion` |  |  |  |
| 13 | `AA.INTC.COMMON.CLASS.TYPE` | `AaInterfaceTypeCatalog_CommonClassType` |  |  |  |
| 14 | `AA.INTC.COMMON.CLASS` | `AaInterfaceTypeCatalog_CommonClass` |  |  |  |
| 15 | `AA.INTC.RESERVED.16` | `AaInterfaceTypeCatalog_Reserved16` |  |  |  |
| 16 | `AA.INTC.COMMON.CLASS.CONDITION` | `AaInterfaceTypeCatalog_CommonClassCondition` |  |  |  |
| 17 | `AA.INTC.COMMON.CONDITION.VERSION` | `AaInterfaceTypeCatalog_CommonConditionVersion` |  |  |  |
| 18 | `AA.INTC.SYNC.MAPPING` | `AaInterfaceTypeCatalog_SyncMapping` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 19 | `AA.INTC.RESERVED.9` | `AaInterfaceTypeCatalog_Reserved9` | TField |  |  |
| 20 | `AA.INTC.RESERVED.8` | `AaInterfaceTypeCatalog_Reserved8` | TField |  |  |
| 21 | `AA.INTC.RESERVED.7` | `AaInterfaceTypeCatalog_Reserved7` | TField |  |  |
| 22 | `AA.INTC.RESERVED.6` | `AaInterfaceTypeCatalog_Reserved6` | TField |  |  |
| 23 | `AA.INTC.RESERVED.5` | `AaInterfaceTypeCatalog_Reserved5` | TField |  |  |
| 24 | `AA.INTC.RESERVED.4` | `AaInterfaceTypeCatalog_Reserved4` | TField |  |  |
| 25 | `AA.INTC.RESERVED.3` | `AaInterfaceTypeCatalog_Reserved3` | TField |  |  |
| 26 | `AA.INTC.RESERVED.2` | `AaInterfaceTypeCatalog_Reserved2` | TField |  |  |
| 27 | `AA.INTC.RESERVED.1` | `AaInterfaceTypeCatalog_Reserved1` | TField |  |  |
| 28 | `AA.INTC.ACTION` | `AaInterfaceTypeCatalog_Action` | TField | No | This field indicates which action will be performed after the record is authorised 2)Optional Input 3) Validation Rules a. Allowed values are Null of PUBLISH : If action is null the definition is simply being saved on file after authorization. If PUBLISH is specified , this will have similar effect as PROOF AND PUBLISH actions of FORM.DESIGNER.The specific meaning of the PUBLISH action depends on the CLASS.TYPE of the object being defined. b.T24 string Input |
| 29 | `AA.INTC.EXPIRY.DATE` | `AaInterfaceTypeCatalog_ExpiryDate` | TField | No | Once defined , the definition Manager Object can be PUBLISHED as many times as needed until it is expired. The definition Manager record is expired by providing a future date in the EXPIRY.DATE field 2)Optional Input 3) Validation Rules a. Date provided should be in the future. b.T24 Date Input |
| 30 | `AA.INTC.PUBLISH.STATUS` | `AaInterfaceTypeCatalog_PublishStatus` | TField |  | This field will contain the result of the publishing effort 1) Validation Rules a. Non Input. b. System Maintained c. Allowed values are : Completed Successfully or Completed with Errors |
| 31 | `AA.INTC.PUBLISH.ERROR` | `AaInterfaceTypeCatalog_PublishError` |  |  |  |
| 32 | `AA.INTC.ERROR.SUGGESTION` | `AaInterfaceTypeCatalog_ErrorSuggestion` |  |  |  |
| 33 | `AA.INTC.LOCAL.REF` | `AaInterfaceTypeCatalog_LocalRef` |  |  |  |
| 34 | `AA.INTC.CLASS.TYPE` | `AaInterfaceTypeCatalog_ClassType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 35 | `AA.INTC.REFERENCE` | `AaInterfaceTypeCatalog_Reference` | TField |  |  |
| 36 | `AA.INTC.VERSION` | `AaInterfaceTypeCatalog_Version` | TField |  | The Version being defined (PRODUCT, FORM) is always &quot;VERSIONNED&quot; . This means that more than one version of the same exist in the system. Depending on the nature of the object, updates may be performed on existing version without the need to advance the object to its NEXT VERSION in the sequence. 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part between the second &quot;-&quot; character and the third &apos;-&apos; character in the ID is the VERSION |
| 37 | `AA.INTC.VERSION.DATE` | `AaInterfaceTypeCatalog_VersionDate` | TField |  | This field indicates the EFFECTIVE.DATE for the VERSION of the object being defined (PRODUCT, FORM etc.). Where more than one record exist on file for the object , the run-time processing will refer to the VERSION.DATE in order to determine which version of the OBJECT is applicable on the day 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part after the last &quot;-&quot; character in the ID is the VERSION.DATE |
| 38 | `AA.INTC.OVERRIDE` | `AaInterfaceTypeCatalog_Override` |  |  |  |
| 39 | `AA.INTC.RECORD.STATUS` | `AaInterfaceTypeCatalog_RecordStatus` | String |  |  |
| 40 | `AA.INTC.CURR.NO` | `AaInterfaceTypeCatalog_CurrNo` | String |  | By default, the form owner has input, submit and see privileges. This field allows for input and/or see privileges to be given to the associated roles by default for the entire form. Input allowed only if the CLASS.TYPE is FORMLET.CLASS |
| 41 | `AA.INTC.INPUTTER` | `AaInterfaceTypeCatalog_Inputter` |  |  |  |
| 42 | `AA.INTC.DATE.TIME` | `AaInterfaceTypeCatalog_DateTime` |  |  |  |
| 43 | `AA.INTC.AUTHORISER` | `AaInterfaceTypeCatalog_Authoriser` | String |  | This field indicates the name of the Definition Manager Object. The Nature of the Object depends on the CLASS.TYPE that the object uses. For Example if the class type is PROPERTY.CLASS , the object will be a PRODUCT .If the class type is FORMLET.CLASS the object will be a FORM 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part between the first &quot;-&quot; character and the Second &apos;-&apos; character in the ID is the REFERENCE c. Input should be a valid AA.CLASS.TYPE record |
| 44 | `AA.INTC.CO.CODE` | `AaInterfaceTypeCatalog_CoCode` | String |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 45 | `AA.INTC.DEPT.CODE` | `AaInterfaceTypeCatalog_DeptCode` | String |  |  |
| 46 | `AA.INTC.AUDITOR.CODE` | `AaInterfaceTypeCatalog_AuditorCode` | String |  |  |
| 47 | `AA.INTC.AUDIT.DATE.TIME` | `AaInterfaceTypeCatalog_AuditDateTime` | String |  |  |
| 48 | `AA.INTC.FORM.OWNER` | `AaInterfaceTypeCatalog_FormOwner` | TField |  | By default, this Role will be the owner of the entire form.Must be valid ID from OA.ROLE.Input allowed only if the CLASS.TYPE is FORMLET.CLASS |
| 49 | `AA.INTC.DEFAULT.ROLE` | `AaInterfaceTypeCatalog_DefaultRole` |  |  |  |
| 50 | `AA.INTC.DEFAULT.PRIVILEGE` | `AaInterfaceTypeCatalog_DefaultPrivilege` |  |  |  |
| 51 | `AA.INTC.OWNER` | `AaInterfaceTypeCatalog_Owner` |  |  |  |
| 52 | `AA.INTC.ROLE` | `AaInterfaceTypeCatalog_Role` |  |  |  |
| 53 | `AA.INTC.PRIVILEGE` | `AaInterfaceTypeCatalog_Privilege` |  |  |  |
