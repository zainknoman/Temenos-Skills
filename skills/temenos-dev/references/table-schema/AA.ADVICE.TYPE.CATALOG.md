# AA.ADVICE.TYPE.CATALOG — Table Schema

> Source: `INSERTS/I_F.AA.ADVICE.TYPE.CATALOG` in `AF_Advice.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ADVT.DESCRIPTION` | `AaAdviceTypeCatalog_Description` |  |  |  |
| 2 | `AA.ADVT.FULL.DESC` | `AaAdviceTypeCatalog_FullDesc` |  |  |  |
| 3 | `AA.ADVT.DOMAIN.TYPE` | `AaAdviceTypeCatalog_DomainType` | TField |  | Used for Form Definition to specify which domain type the form is used in and therefore will default the Instances (i.e. the formlets) in the domain type into the mv set. |
| 4 | `AA.ADVT.CLASS` | `AaAdviceTypeCatalog_Class` |  |  |  |
| 5 | `AA.ADVT.INSTANCE` | `AaAdviceTypeCatalog_Instance` |  |  |  |
| 6 | `AA.ADVT.RESERVED.15` | `AaAdviceTypeCatalog_Reserved15` |  |  |  |
| 7 | `AA.ADVT.RESERVED.14` | `AaAdviceTypeCatalog_Reserved14` |  |  |  |
| 8 | `AA.ADVT.RESERVED.13` | `AaAdviceTypeCatalog_Reserved13` |  |  |  |
| 9 | `AA.ADVT.RESERVED.12` | `AaAdviceTypeCatalog_Reserved12` |  |  |  |
| 10 | `AA.ADVT.RESERVED.11` | `AaAdviceTypeCatalog_Reserved11` |  |  |  |
| 11 | `AA.ADVT.CONDITION` | `AaAdviceTypeCatalog_Condition` |  |  |  |
| 12 | `AA.ADVT.CONDITION.VERSION` | `AaAdviceTypeCatalog_ConditionVersion` |  |  |  |
| 13 | `AA.ADVT.COMMON.CLASS.TYPE` | `AaAdviceTypeCatalog_CommonClassType` |  |  |  |
| 14 | `AA.ADVT.COMMON.CLASS` | `AaAdviceTypeCatalog_CommonClass` |  |  |  |
| 15 | `AA.ADVT.RESERVED.16` | `AaAdviceTypeCatalog_Reserved16` |  |  |  |
| 16 | `AA.ADVT.COMMON.CLASS.CONDITION` | `AaAdviceTypeCatalog_CommonClassCondition` |  |  |  |
| 17 | `AA.ADVT.COMMON.CONDITION.VERSION` | `AaAdviceTypeCatalog_CommonConditionVersion` |  |  |  |
| 18 | `AA.ADVT.SYNC.MAPPING` | `AaAdviceTypeCatalog_SyncMapping` | TField |  |  |
| 19 | `AA.ADVT.RESERVED.9` | `AaAdviceTypeCatalog_Reserved9` | TField |  |  |
| 20 | `AA.ADVT.RESERVED.8` | `AaAdviceTypeCatalog_Reserved8` | TField |  |  |
| 21 | `AA.ADVT.RESERVED.7` | `AaAdviceTypeCatalog_Reserved7` | TField |  |  |
| 22 | `AA.ADVT.RESERVED.6` | `AaAdviceTypeCatalog_Reserved6` | TField |  |  |
| 23 | `AA.ADVT.RESERVED.5` | `AaAdviceTypeCatalog_Reserved5` | TField |  |  |
| 24 | `AA.ADVT.RESERVED.4` | `AaAdviceTypeCatalog_Reserved4` | TField |  |  |
| 25 | `AA.ADVT.RESERVED.3` | `AaAdviceTypeCatalog_Reserved3` | TField |  |  |
| 26 | `AA.ADVT.RESERVED.2` | `AaAdviceTypeCatalog_Reserved2` | TField |  |  |
| 27 | `AA.ADVT.RESERVED.1` | `AaAdviceTypeCatalog_Reserved1` | TField |  |  |
| 28 | `AA.ADVT.ACTION` | `AaAdviceTypeCatalog_Action` | TField |  | Allowed options are :Null or PUBLISH If null, the record is simply being updated. PUBLISH will cause proofing and publishing to be initiated on commit. |
| 29 | `AA.ADVT.EXPIRY.DATE` | `AaAdviceTypeCatalog_ExpiryDate` | TField |  | Date from which the resultant Advice will no longer be available for use. |
| 30 | `AA.ADVT.PUBLISH.STATUS` | `AaAdviceTypeCatalog_PublishStatus` | TField |  | Status of publishing effort. |
| 31 | `AA.ADVT.PUBLISH.ERROR` | `AaAdviceTypeCatalog_PublishError` |  |  |  |
| 32 | `AA.ADVT.ERROR.SUGGESTION` | `AaAdviceTypeCatalog_ErrorSuggestion` |  |  |  |
| 33 | `AA.ADVT.LOCAL.REF` | `AaAdviceTypeCatalog_LocalRef` |  |  |  |
| 34 | `AA.ADVT.CLASS.TYPE` | `AaAdviceTypeCatalog_ClassType` | TField |  | Valid entry in AA.CLASS.TYPE. |
| 35 | `AA.ADVT.REFERENCE` | `AaAdviceTypeCatalog_Reference` | TField |  | ID Component 2. Is the main "ID" of the item being designed. For evidence this is the name of the Advice type |
| 36 | `AA.ADVT.VERSION` | `AaAdviceTypeCatalog_Version` | TField |  | ID Component 3: Version number identifier. |
| 37 | `AA.ADVT.VERSION.DATE` | `AaAdviceTypeCatalog_VersionDate` | TField |  | ID Component 4: Date of the version becomes effective. |
| 38 | `AA.ADVT.OVERRIDE` | `AaAdviceTypeCatalog_Override` |  |  |  |
| 39 | `AA.ADVT.RECORD.STATUS` | `AaAdviceTypeCatalog_RecordStatus` | String |  |  |
| 40 | `AA.ADVT.CURR.NO` | `AaAdviceTypeCatalog_CurrNo` | String |  |  |
| 41 | `AA.ADVT.INPUTTER` | `AaAdviceTypeCatalog_Inputter` |  |  |  |
| 42 | `AA.ADVT.DATE.TIME` | `AaAdviceTypeCatalog_DateTime` |  |  |  |
| 43 | `AA.ADVT.AUTHORISER` | `AaAdviceTypeCatalog_Authoriser` | String |  |  |
| 44 | `AA.ADVT.CO.CODE` | `AaAdviceTypeCatalog_CoCode` | String |  |  |
| 45 | `AA.ADVT.DEPT.CODE` | `AaAdviceTypeCatalog_DeptCode` | String |  |  |
| 46 | `AA.ADVT.AUDITOR.CODE` | `AaAdviceTypeCatalog_AuditorCode` | String |  |  |
| 47 | `AA.ADVT.AUDIT.DATE.TIME` | `AaAdviceTypeCatalog_AuditDateTime` | String |  |  |
| 48 | `AA.ADVT.FORM.OWNER` | `AaAdviceTypeCatalog_FormOwner` | TField |  |  |
| 49 | `AA.ADVT.DEFAULT.ROLE` | `AaAdviceTypeCatalog_DefaultRole` |  |  |  |
| 50 | `AA.ADVT.DEFAULT.PRIVILEGE` | `AaAdviceTypeCatalog_DefaultPrivilege` |  |  |  |
| 51 | `AA.ADVT.OWNER` | `AaAdviceTypeCatalog_Owner` |  |  |  |
| 52 | `AA.ADVT.ROLE` | `AaAdviceTypeCatalog_Role` |  |  |  |
| 53 | `AA.ADVT.PRIVILEGE` | `AaAdviceTypeCatalog_Privilege` |  |  |  |
