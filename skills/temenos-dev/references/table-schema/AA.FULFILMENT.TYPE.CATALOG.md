# AA.FULFILMENT.TYPE.CATALOG — Table Schema

> Source: `INSERTS/I_F.AA.FULFILMENT.TYPE.CATALOG` in `AF_Mapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.FLC.DESCRIPTION` | `AaFulfilmentTypeCatalog_Description` |  |  |  |
| 2 | `AA.FLC.FULL.DESC` | `AaFulfilmentTypeCatalog_FullDesc` |  |  |  |
| 3 | `AA.FLC.DOMAIN.TYPE` | `AaFulfilmentTypeCatalog_DomainType` | TField |  |  |
| 4 | `AA.FLC.CLASS` | `AaFulfilmentTypeCatalog_Class` |  |  |  |
| 5 | `AA.FLC.INSTANCE` | `AaFulfilmentTypeCatalog_Instance` |  |  |  |
| 6 | `AA.FLC.RESERVED.15` | `AaFulfilmentTypeCatalog_Reserved15` |  |  |  |
| 7 | `AA.FLC.RESERVED.14` | `AaFulfilmentTypeCatalog_Reserved14` |  |  |  |
| 8 | `AA.FLC.RESERVED.13` | `AaFulfilmentTypeCatalog_Reserved13` |  |  |  |
| 9 | `AA.FLC.RESERVED.12` | `AaFulfilmentTypeCatalog_Reserved12` |  |  |  |
| 10 | `AA.FLC.RESERVED.11` | `AaFulfilmentTypeCatalog_Reserved11` |  |  |  |
| 11 | `AA.FLC.CONDITION` | `AaFulfilmentTypeCatalog_Condition` |  |  |  |
| 12 | `AA.FLC.CONDITION.VERSION` | `AaFulfilmentTypeCatalog_ConditionVersion` |  |  |  |
| 13 | `AA.FLC.COMMON.CLASS.TYPE` | `AaFulfilmentTypeCatalog_CommonClassType` |  |  |  |
| 14 | `AA.FLC.COMMON.CLASS` | `AaFulfilmentTypeCatalog_CommonClass` |  |  |  |
| 15 | `AA.FLC.RESERVED.16` | `AaFulfilmentTypeCatalog_Reserved16` |  |  |  |
| 16 | `AA.FLC.COMMON.CLASS.CONDITION` | `AaFulfilmentTypeCatalog_CommonClassCondition` |  |  |  |
| 17 | `AA.FLC.COMMON.CONDITION.VERSION` | `AaFulfilmentTypeCatalog_CommonConditionVersion` |  |  |  |
| 18 | `AA.FLC.SYNC.MAPPING` | `AaFulfilmentTypeCatalog_SyncMapping` | TField |  |  |
| 19 | `AA.FLC.RESERVED.9` | `AaFulfilmentTypeCatalog_Reserved9` | TField |  |  |
| 20 | `AA.FLC.RESERVED.8` | `AaFulfilmentTypeCatalog_Reserved8` | TField |  |  |
| 21 | `AA.FLC.RESERVED.7` | `AaFulfilmentTypeCatalog_Reserved7` | TField |  |  |
| 22 | `AA.FLC.RESERVED.6` | `AaFulfilmentTypeCatalog_Reserved6` | TField |  |  |
| 23 | `AA.FLC.RESERVED.5` | `AaFulfilmentTypeCatalog_Reserved5` | TField |  |  |
| 24 | `AA.FLC.RESERVED.4` | `AaFulfilmentTypeCatalog_Reserved4` | TField |  |  |
| 25 | `AA.FLC.RESERVED.3` | `AaFulfilmentTypeCatalog_Reserved3` | TField |  |  |
| 26 | `AA.FLC.RESERVED.2` | `AaFulfilmentTypeCatalog_Reserved2` | TField |  |  |
| 27 | `AA.FLC.RESERVED.1` | `AaFulfilmentTypeCatalog_Reserved1` | TField |  |  |
| 28 | `AA.FLC.ACTION` | `AaFulfilmentTypeCatalog_Action` | TField |  |  |
| 29 | `AA.FLC.EXPIRY.DATE` | `AaFulfilmentTypeCatalog_ExpiryDate` | TField |  |  |
| 30 | `AA.FLC.PUBLISH.STATUS` | `AaFulfilmentTypeCatalog_PublishStatus` | TField |  |  |
| 31 | `AA.FLC.PUBLISH.ERROR` | `AaFulfilmentTypeCatalog_PublishError` |  |  |  |
| 32 | `AA.FLC.ERROR.SUGGESTION` | `AaFulfilmentTypeCatalog_ErrorSuggestion` |  |  |  |
| 33 | `AA.FLC.LOCAL.REF` | `AaFulfilmentTypeCatalog_LocalRef` |  |  |  |
| 34 | `AA.FLC.CLASS.TYPE` | `AaFulfilmentTypeCatalog_ClassType` | TField |  |  |
| 35 | `AA.FLC.REFERENCE` | `AaFulfilmentTypeCatalog_Reference` | TField |  |  |
| 36 | `AA.FLC.VERSION` | `AaFulfilmentTypeCatalog_Version` | TField |  |  |
| 37 | `AA.FLC.VERSION.DATE` | `AaFulfilmentTypeCatalog_VersionDate` | TField |  |  |
| 38 | `AA.FLC.OVERRIDE` | `AaFulfilmentTypeCatalog_Override` |  |  |  |
| 39 | `AA.FLC.RECORD.STATUS` | `AaFulfilmentTypeCatalog_RecordStatus` | String |  |  |
| 40 | `AA.FLC.CURR.NO` | `AaFulfilmentTypeCatalog_CurrNo` | String |  |  |
| 41 | `AA.FLC.INPUTTER` | `AaFulfilmentTypeCatalog_Inputter` |  |  |  |
| 42 | `AA.FLC.DATE.TIME` | `AaFulfilmentTypeCatalog_DateTime` |  |  |  |
| 43 | `AA.FLC.AUTHORISER` | `AaFulfilmentTypeCatalog_Authoriser` | String |  |  |
| 44 | `AA.FLC.CO.CODE` | `AaFulfilmentTypeCatalog_CoCode` | String |  |  |
| 45 | `AA.FLC.DEPT.CODE` | `AaFulfilmentTypeCatalog_DeptCode` | String |  |  |
| 46 | `AA.FLC.AUDITOR.CODE` | `AaFulfilmentTypeCatalog_AuditorCode` | String |  |  |
| 47 | `AA.FLC.AUDIT.DATE.TIME` | `AaFulfilmentTypeCatalog_AuditDateTime` | String |  |  |
| 48 | `AA.FLC.FORM.OWNER` | `AaFulfilmentTypeCatalog_FormOwner` | TField |  |  |
| 49 | `AA.FLC.DEFAULT.ROLE` | `AaFulfilmentTypeCatalog_DefaultRole` |  |  |  |
| 50 | `AA.FLC.DEFAULT.PRIVILEGE` | `AaFulfilmentTypeCatalog_DefaultPrivilege` |  |  |  |
| 51 | `AA.FLC.OWNER` | `AaFulfilmentTypeCatalog_Owner` |  |  |  |
| 52 | `AA.FLC.ROLE` | `AaFulfilmentTypeCatalog_Role` |  |  |  |
| 53 | `AA.FLC.PRIVILEGE` | `AaFulfilmentTypeCatalog_Privilege` |  |  |  |
