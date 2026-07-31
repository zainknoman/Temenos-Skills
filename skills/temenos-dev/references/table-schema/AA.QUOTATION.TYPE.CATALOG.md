# AA.QUOTATION.TYPE.CATALOG — Table Schema

> Source: `INSERTS/I_F.AA.QUOTATION.TYPE.CATALOG` in `AA_Quotation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.DEFMAN.DESCRIPTION` | `AaQuotationTypeCatalog_Description` |  |  |  |
| 2 | `AA.DEFMAN.FULL.DESC` | `AaQuotationTypeCatalog_FullDesc` |  |  |  |
| 3 | `AA.DEFMAN.DOMAIN.TYPE` | `AaQuotationTypeCatalog_DomainType` | TField |  | Used for Form Definition to specify which domain type the form is used in and therefore will default the Instances (i.e. the formlets) in the domain type into the mv set. |
| 4 | `AA.DEFMAN.CLASS` | `AaQuotationTypeCatalog_Class` |  |  |  |
| 5 | `AA.DEFMAN.INSTANCE` | `AaQuotationTypeCatalog_Instance` |  |  |  |
| 6 | `AA.DEFMAN.RESERVED.15` | `AaQuotationTypeCatalog_Reserved15` |  |  |  |
| 7 | `AA.DEFMAN.RESERVED.14` | `AaQuotationTypeCatalog_Reserved14` |  |  |  |
| 8 | `AA.DEFMAN.RESERVED.13` | `AaQuotationTypeCatalog_Reserved13` |  |  |  |
| 9 | `AA.DEFMAN.RESERVED.12` | `AaQuotationTypeCatalog_Reserved12` |  |  |  |
| 10 | `AA.DEFMAN.RESERVED.11` | `AaQuotationTypeCatalog_Reserved11` |  |  |  |
| 11 | `AA.DEFMAN.CONDITION` | `AaQuotationTypeCatalog_Condition` |  |  |  |
| 12 | `AA.DEFMAN.CONDITION.VERSION` | `AaQuotationTypeCatalog_ConditionVersion` |  |  |  |
| 13 | `AA.DEFMAN.COMMON.CLASS.TYPE` | `AaQuotationTypeCatalog_CommonClassType` |  |  |  |
| 14 | `AA.DEFMAN.COMMON.CLASS` | `AaQuotationTypeCatalog_CommonClass` |  |  |  |
| 15 | `AA.DEFMAN.RESERVED.16` | `AaQuotationTypeCatalog_Reserved16` |  |  |  |
| 16 | `AA.DEFMAN.COMMON.CLASS.CONDITION` | `AaQuotationTypeCatalog_CommonClassCondition` |  |  |  |
| 17 | `AA.DEFMAN.COMMON.CONDITION.VERSION` | `AaQuotationTypeCatalog_CommonConditionVersion` |  |  |  |
| 18 | `AA.DEFMAN.SYNC.MAPPING` | `AaQuotationTypeCatalog_SyncMapping` | TField |  | This field will allow a user to specify which mapping definition to use when syncing data for the form |
| 19 | `AA.DEFMAN.RESERVED.9` | `AaQuotationTypeCatalog_Reserved9` | TField |  |  |
| 20 | `AA.DEFMAN.RESERVED.8` | `AaQuotationTypeCatalog_Reserved8` | TField |  |  |
| 21 | `AA.DEFMAN.RESERVED.7` | `AaQuotationTypeCatalog_Reserved7` | TField |  |  |
| 22 | `AA.DEFMAN.RESERVED.6` | `AaQuotationTypeCatalog_Reserved6` | TField |  |  |
| 23 | `AA.DEFMAN.RESERVED.5` | `AaQuotationTypeCatalog_Reserved5` | TField |  |  |
| 24 | `AA.DEFMAN.RESERVED.4` | `AaQuotationTypeCatalog_Reserved4` | TField |  |  |
| 25 | `AA.DEFMAN.RESERVED.3` | `AaQuotationTypeCatalog_Reserved3` | TField |  |  |
| 26 | `AA.DEFMAN.RESERVED.2` | `AaQuotationTypeCatalog_Reserved2` | TField |  |  |
| 27 | `AA.DEFMAN.RESERVED.1` | `AaQuotationTypeCatalog_Reserved1` | TField |  |  |
| 28 | `AA.DEFMAN.ACTION` | `AaQuotationTypeCatalog_Action` | TField |  | Allowed options are 1. &quot;Null&quot;- the record is simply being updated. 2. PUBLISH - record is proofed and published. |
| 29 | `AA.DEFMAN.EXPIRY.DATE` | `AaQuotationTypeCatalog_ExpiryDate` | TField |  | Date from which the Quotation type will no longer be available for use. |
| 30 | `AA.DEFMAN.PUBLISH.STATUS` | `AaQuotationTypeCatalog_PublishStatus` | TField |  | This field will contain the result of the publishing effort. Validation Rules - Non Inputtable, System Maintained, Allowed values are : Completed Successfully or Completed with Errors. |
| 31 | `AA.DEFMAN.PUBLISH.ERROR` | `AaQuotationTypeCatalog_PublishError` |  |  |  |
| 32 | `AA.DEFMAN.ERROR.SUGGESTION` | `AaQuotationTypeCatalog_ErrorSuggestion` |  |  |  |
| 33 | `AA.DEFMAN.LOCAL.REF` | `AaQuotationTypeCatalog_LocalRef` |  |  |  |
| 34 | `AA.DEFMAN.CLASS.TYPE` | `AaQuotationTypeCatalog_ClassType` | TField |  | Valid entry in AA.CLASS.TYPE. |
| 35 | `AA.DEFMAN.REFERENCE` | `AaQuotationTypeCatalog_Reference` | TField |  | ID Component 2: Is the main &quot;ID&quot; of the item being designed. For quotation this is the name of the quotation type |
| 36 | `AA.DEFMAN.VERSION` | `AaQuotationTypeCatalog_Version` | TField |  | ID Component 3: Version number identifier. |
| 37 | `AA.DEFMAN.VERSION.DATE` | `AaQuotationTypeCatalog_VersionDate` | TField |  | ID Component 4: Date when the version becomes effective. |
| 38 | `AA.DEFMAN.OVERRIDE` | `AaQuotationTypeCatalog_Override` |  |  |  |
| 39 | `AA.DEFMAN.RECORD.STATUS` | `AaQuotationTypeCatalog_RecordStatus` | String |  |  |
| 40 | `AA.DEFMAN.CURR.NO` | `AaQuotationTypeCatalog_CurrNo` | String |  |  |
| 41 | `AA.DEFMAN.INPUTTER` | `AaQuotationTypeCatalog_Inputter` |  |  |  |
| 42 | `AA.DEFMAN.DATE.TIME` | `AaQuotationTypeCatalog_DateTime` |  |  |  |
| 43 | `AA.DEFMAN.AUTHORISER` | `AaQuotationTypeCatalog_Authoriser` | String |  |  |
| 44 | `AA.DEFMAN.CO.CODE` | `AaQuotationTypeCatalog_CoCode` | String |  |  |
| 45 | `AA.DEFMAN.DEPT.CODE` | `AaQuotationTypeCatalog_DeptCode` | String |  |  |
| 46 | `AA.DEFMAN.AUDITOR.CODE` | `AaQuotationTypeCatalog_AuditorCode` | String |  |  |
| 47 | `AA.DEFMAN.AUDIT.DATE.TIME` | `AaQuotationTypeCatalog_AuditDateTime` | String |  |  |
| 48 | `AA.DEFMAN.FORM.OWNER` | `AaQuotationTypeCatalog_FormOwner` | TField |  |  |
| 49 | `AA.DEFMAN.DEFAULT.ROLE` | `AaQuotationTypeCatalog_DefaultRole` |  |  |  |
| 50 | `AA.DEFMAN.DEFAULT.PRIVILEGE` | `AaQuotationTypeCatalog_DefaultPrivilege` |  |  |  |
| 51 | `AA.DEFMAN.OWNER` | `AaQuotationTypeCatalog_Owner` |  |  |  |
| 52 | `AA.DEFMAN.ROLE` | `AaQuotationTypeCatalog_Role` |  |  |  |
| 53 | `AA.DEFMAN.PRIVILEGE` | `AaQuotationTypeCatalog_Privilege` |  |  |  |
