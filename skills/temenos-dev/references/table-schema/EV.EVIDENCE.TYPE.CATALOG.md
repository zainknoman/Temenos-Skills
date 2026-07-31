# EV.EVIDENCE.TYPE.CATALOG — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE.TYPE.CATALOG` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVTC.DESCRIPTION` | `EvEvidenceTypeCatalog_Description` |  |  |  |
| 2 | `EV.EVTC.FULL.DESC` | `EvEvidenceTypeCatalog_FullDesc` |  |  |  |
| 3 | `EV.EVTC.DOMAIN.TYPE` | `EvEvidenceTypeCatalog_DomainType` | TField |  | Used for Form Definition to specify which domain type the form is used in and therefore will default the Instances (i.e. the formlets) in the domain type into the mv set. |
| 4 | `EV.EVTC.CLASS` | `EvEvidenceTypeCatalog_Class` |  |  |  |
| 5 | `EV.EVTC.INSTANCE` | `EvEvidenceTypeCatalog_Instance` |  |  |  |
| 6 | `EV.EVTC.RESERVED.15` | `EvEvidenceTypeCatalog_Reserved15` |  |  |  |
| 7 | `EV.EVTC.RESERVED.14` | `EvEvidenceTypeCatalog_Reserved14` |  |  |  |
| 8 | `EV.EVTC.RESERVED.13` | `EvEvidenceTypeCatalog_Reserved13` |  |  |  |
| 9 | `EV.EVTC.RESERVED.12` | `EvEvidenceTypeCatalog_Reserved12` |  |  |  |
| 10 | `EV.EVTC.RESERVED.11` | `EvEvidenceTypeCatalog_Reserved11` |  |  |  |
| 11 | `EV.EVTC.CONDITION` | `EvEvidenceTypeCatalog_Condition` |  |  |  |
| 12 | `EV.EVTC.CONDITION.VERSION` | `EvEvidenceTypeCatalog_ConditionVersion` |  |  |  |
| 13 | `EV.EVTC.COMMON.CLASS.TYPE` | `EvEvidenceTypeCatalog_CommonClassType` |  |  |  |
| 14 | `EV.EVTC.COMMON.CLASS` | `EvEvidenceTypeCatalog_CommonClass` |  |  |  |
| 15 | `EV.EVTC.RESERVED.16` | `EvEvidenceTypeCatalog_Reserved16` |  |  |  |
| 16 | `EV.EVTC.COMMON.CLASS.CONDITION` | `EvEvidenceTypeCatalog_CommonClassCondition` |  |  |  |
| 17 | `EV.EVTC.COMMON.CONDITION.VERSION` | `EvEvidenceTypeCatalog_CommonConditionVersion` |  |  |  |
| 18 | `EV.EVTC.SYNC.MAPPING` | `EvEvidenceTypeCatalog_SyncMapping` | TField |  | This field will allow a user to specify which mapping definition to use when syncing data for the form. |
| 19 | `EV.EVTC.RESERVED.9` | `EvEvidenceTypeCatalog_Reserved9` | TField |  |  |
| 20 | `EV.EVTC.RESERVED.8` | `EvEvidenceTypeCatalog_Reserved8` | TField |  |  |
| 21 | `EV.EVTC.RESERVED.7` | `EvEvidenceTypeCatalog_Reserved7` | TField |  |  |
| 22 | `EV.EVTC.RESERVED.6` | `EvEvidenceTypeCatalog_Reserved6` | TField |  |  |
| 23 | `EV.EVTC.RESERVED.5` | `EvEvidenceTypeCatalog_Reserved5` | TField |  |  |
| 24 | `EV.EVTC.RESERVED.4` | `EvEvidenceTypeCatalog_Reserved4` | TField |  |  |
| 25 | `EV.EVTC.RESERVED.3` | `EvEvidenceTypeCatalog_Reserved3` | TField |  |  |
| 26 | `EV.EVTC.RESERVED.2` | `EvEvidenceTypeCatalog_Reserved2` | TField |  |  |
| 27 | `EV.EVTC.RESERVED.1` | `EvEvidenceTypeCatalog_Reserved1` | TField |  |  |
| 28 | `EV.EVTC.ACTION` | `EvEvidenceTypeCatalog_Action` | TField |  | Allowed options are :Null or PUBLISH If null, the record is simply being updated. PUBLISH will cause proofing and publishing to be initiated on commit. |
| 29 | `EV.EVTC.EXPIRY.DATE` | `EvEvidenceTypeCatalog_ExpiryDate` | TField |  | Date from which the resultant Evidence will no longer be available for use. |
| 30 | `EV.EVTC.PUBLISH.STATUS` | `EvEvidenceTypeCatalog_PublishStatus` | TField |  | Status of publishing effort. |
| 31 | `EV.EVTC.PUBLISH.ERROR` | `EvEvidenceTypeCatalog_PublishError` |  |  |  |
| 32 | `EV.EVTC.ERROR.SUGGESTION` | `EvEvidenceTypeCatalog_ErrorSuggestion` |  |  |  |
| 33 | `EV.EVTC.LOCAL.REF` | `EvEvidenceTypeCatalog_LocalRef` |  |  |  |
| 34 | `EV.EVTC.CLASS.TYPE` | `EvEvidenceTypeCatalog_ClassType` | TField |  | Valid entry in AA.CLASS.TYPE. |
| 35 | `EV.EVTC.REFERENCE` | `EvEvidenceTypeCatalog_Reference` | TField |  | ID Component 2. Is the main &quot;ID&quot; of the item being designed. For evidence this is the name of the evidence type (e.g. PASSPORT.US). |
| 36 | `EV.EVTC.VERSION` | `EvEvidenceTypeCatalog_Version` | TField |  | ID Component 3: Version number identifier. |
| 37 | `EV.EVTC.VERSION.DATE` | `EvEvidenceTypeCatalog_VersionDate` | TField |  | ID Component 4: Date of the version becomes effective. |
| 38 | `EV.EVTC.OVERRIDE` | `EvEvidenceTypeCatalog_Override` |  |  |  |
| 39 | `EV.EVTC.RECORD.STATUS` | `EvEvidenceTypeCatalog_RecordStatus` | String |  |  |
| 40 | `EV.EVTC.CURR.NO` | `EvEvidenceTypeCatalog_CurrNo` | String |  |  |
| 41 | `EV.EVTC.INPUTTER` | `EvEvidenceTypeCatalog_Inputter` |  |  |  |
| 42 | `EV.EVTC.DATE.TIME` | `EvEvidenceTypeCatalog_DateTime` |  |  |  |
| 43 | `EV.EVTC.AUTHORISER` | `EvEvidenceTypeCatalog_Authoriser` | String |  |  |
| 44 | `EV.EVTC.CO.CODE` | `EvEvidenceTypeCatalog_CoCode` | String |  |  |
| 45 | `EV.EVTC.DEPT.CODE` | `EvEvidenceTypeCatalog_DeptCode` | String |  |  |
| 46 | `EV.EVTC.AUDITOR.CODE` | `EvEvidenceTypeCatalog_AuditorCode` | String |  |  |
| 47 | `EV.EVTC.AUDIT.DATE.TIME` | `EvEvidenceTypeCatalog_AuditDateTime` | String |  |  |
| 48 | `EV.EVTC.FORM.OWNER` | `EvEvidenceTypeCatalog_FormOwner` | TField |  |  |
| 49 | `EV.EVTC.DEFAULT.ROLE` | `EvEvidenceTypeCatalog_DefaultRole` |  |  |  |
| 50 | `EV.EVTC.DEFAULT.PRIVILEGE` | `EvEvidenceTypeCatalog_DefaultPrivilege` |  |  |  |
| 51 | `EV.EVTC.OWNER` | `EvEvidenceTypeCatalog_Owner` |  |  |  |
| 52 | `EV.EVTC.ROLE` | `EvEvidenceTypeCatalog_Role` |  |  |  |
| 53 | `EV.EVTC.PRIVILEGE` | `EvEvidenceTypeCatalog_Privilege` |  |  |  |
