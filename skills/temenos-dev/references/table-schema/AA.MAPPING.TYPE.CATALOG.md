# AA.MAPPING.TYPE.CATALOG — Table Schema

> Source: `INSERTS/I_F.AA.MAPPING.TYPE.CATALOG` in `AF_Mapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.MPC.DESCRIPTION` | `AaMappingTypeCatalog_Description` |  |  |  |
| 2 | `AA.MPC.FULL.DESC` | `AaMappingTypeCatalog_FullDesc` |  |  |  |
| 3 | `AA.MPC.DOMAIN.TYPE` | `AaMappingTypeCatalog_DomainType` | TField |  |  |
| 4 | `AA.MPC.CLASS` | `AaMappingTypeCatalog_Class` |  |  |  |
| 5 | `AA.MPC.INSTANCE` | `AaMappingTypeCatalog_Instance` |  |  |  |
| 6 | `AA.MPC.RESERVED.15` | `AaMappingTypeCatalog_Reserved15` |  |  |  |
| 7 | `AA.MPC.RESERVED.14` | `AaMappingTypeCatalog_Reserved14` |  |  |  |
| 8 | `AA.MPC.RESERVED.13` | `AaMappingTypeCatalog_Reserved13` |  |  |  |
| 9 | `AA.MPC.RESERVED.12` | `AaMappingTypeCatalog_Reserved12` |  |  |  |
| 10 | `AA.MPC.RESERVED.11` | `AaMappingTypeCatalog_Reserved11` |  |  |  |
| 11 | `AA.MPC.CONDITION` | `AaMappingTypeCatalog_Condition` |  |  |  |
| 12 | `AA.MPC.CONDITION.VERSION` | `AaMappingTypeCatalog_ConditionVersion` |  |  |  |
| 13 | `AA.MPC.COMMON.CLASS.TYPE` | `AaMappingTypeCatalog_CommonClassType` |  |  |  |
| 14 | `AA.MPC.COMMON.CLASS` | `AaMappingTypeCatalog_CommonClass` |  |  |  |
| 15 | `AA.MPC.RESERVED.16` | `AaMappingTypeCatalog_Reserved16` |  |  |  |
| 16 | `AA.MPC.COMMON.CLASS.CONDITION` | `AaMappingTypeCatalog_CommonClassCondition` |  |  |  |
| 17 | `AA.MPC.COMMON.CONDITION.VERSION` | `AaMappingTypeCatalog_CommonConditionVersion` |  |  |  |
| 18 | `AA.MPC.SYNC.MAPPING` | `AaMappingTypeCatalog_SyncMapping` | TField |  |  |
| 19 | `AA.MPC.RESERVED.9` | `AaMappingTypeCatalog_Reserved9` | TField |  |  |
| 20 | `AA.MPC.RESERVED.8` | `AaMappingTypeCatalog_Reserved8` | TField |  |  |
| 21 | `AA.MPC.RESERVED.7` | `AaMappingTypeCatalog_Reserved7` | TField |  |  |
| 22 | `AA.MPC.RESERVED.6` | `AaMappingTypeCatalog_Reserved6` | TField |  |  |
| 23 | `AA.MPC.RESERVED.5` | `AaMappingTypeCatalog_Reserved5` | TField |  |  |
| 24 | `AA.MPC.RESERVED.4` | `AaMappingTypeCatalog_Reserved4` | TField |  |  |
| 25 | `AA.MPC.RESERVED.3` | `AaMappingTypeCatalog_Reserved3` | TField |  |  |
| 26 | `AA.MPC.RESERVED.2` | `AaMappingTypeCatalog_Reserved2` | TField |  |  |
| 27 | `AA.MPC.RESERVED.1` | `AaMappingTypeCatalog_Reserved1` | TField |  |  |
| 28 | `AA.MPC.ACTION` | `AaMappingTypeCatalog_Action` | TField |  |  |
| 29 | `AA.MPC.EXPIRY.DATE` | `AaMappingTypeCatalog_ExpiryDate` | TField |  |  |
| 30 | `AA.MPC.PUBLISH.STATUS` | `AaMappingTypeCatalog_PublishStatus` | TField |  |  |
| 31 | `AA.MPC.PUBLISH.ERROR` | `AaMappingTypeCatalog_PublishError` |  |  |  |
| 32 | `AA.MPC.ERROR.SUGGESTION` | `AaMappingTypeCatalog_ErrorSuggestion` |  |  |  |
| 33 | `AA.MPC.LOCAL.REF` | `AaMappingTypeCatalog_LocalRef` |  |  |  |
| 34 | `AA.MPC.CLASS.TYPE` | `AaMappingTypeCatalog_ClassType` | TField |  |  |
| 35 | `AA.MPC.REFERENCE` | `AaMappingTypeCatalog_Reference` | TField |  |  |
| 36 | `AA.MPC.VERSION` | `AaMappingTypeCatalog_Version` | TField |  |  |
| 37 | `AA.MPC.VERSION.DATE` | `AaMappingTypeCatalog_VersionDate` | TField |  |  |
| 38 | `AA.MPC.OVERRIDE` | `AaMappingTypeCatalog_Override` |  |  |  |
| 39 | `AA.MPC.RECORD.STATUS` | `AaMappingTypeCatalog_RecordStatus` | String |  |  |
| 40 | `AA.MPC.CURR.NO` | `AaMappingTypeCatalog_CurrNo` | String |  |  |
| 41 | `AA.MPC.INPUTTER` | `AaMappingTypeCatalog_Inputter` |  |  |  |
| 42 | `AA.MPC.DATE.TIME` | `AaMappingTypeCatalog_DateTime` |  |  |  |
| 43 | `AA.MPC.AUTHORISER` | `AaMappingTypeCatalog_Authoriser` | String |  |  |
| 44 | `AA.MPC.CO.CODE` | `AaMappingTypeCatalog_CoCode` | String |  |  |
| 45 | `AA.MPC.DEPT.CODE` | `AaMappingTypeCatalog_DeptCode` | String |  |  |
| 46 | `AA.MPC.AUDITOR.CODE` | `AaMappingTypeCatalog_AuditorCode` | String |  |  |
| 47 | `AA.MPC.AUDIT.DATE.TIME` | `AaMappingTypeCatalog_AuditDateTime` | String |  |  |
| 48 | `AA.MPC.FORM.OWNER` | `AaMappingTypeCatalog_FormOwner` | TField |  |  |
| 49 | `AA.MPC.DEFAULT.ROLE` | `AaMappingTypeCatalog_DefaultRole` |  |  |  |
| 50 | `AA.MPC.DEFAULT.PRIVILEGE` | `AaMappingTypeCatalog_DefaultPrivilege` |  |  |  |
| 51 | `AA.MPC.OWNER` | `AaMappingTypeCatalog_Owner` |  |  |  |
| 52 | `AA.MPC.ROLE` | `AaMappingTypeCatalog_Role` |  |  |  |
| 53 | `AA.MPC.PRIVILEGE` | `AaMappingTypeCatalog_Privilege` |  |  |  |
