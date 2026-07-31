# MT.TENANT.CLEANUP — Table Schema

> Source: `INSERTS/I_F.MT.TENANT.CLEANUP` in `MT_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MT.CLN.OPERATION.MODE` | `MtTenantCleanup_OperationMode` | TField |  | Mode of operation based on which the MT operator can either; just view report of tenant data before removal or can effect the removal operation. Validation Rules: Acceptable values are: 1. REPORT - used to view report of tenant data before removal process by populating it into the MT.TENANT.CLEANUP table fields. Mode possible for both activated and deactivated tenants 2. REMOVE - used to remove or update MT tables records which are associated with subject tenant (off-boarded). Mode Possible only for deactivated tenants. Mode change not allowed after successful remove operation (MT.TENANT.CLEANUP record authorized with REMOVE mode). |
| 2 | `MT.CLN.TENANT.ID` | `MtTenantCleanup_TenantId` | TField |  | This represents the tenant id being processed, for the report or removal process being performed. Validation Rules: Noinput field. Value gets populated from TENANT.CLEANUP.ID (Key field of MT.TENANT.CLEANUP table). Must be a valid entry in MT.TENANT table - unless the tenant has been removed previously. |
| 3 | `MT.CLN.TENANT.NAME` | `MtTenantCleanup_TenantName` | TField |  | Gives a visual confirmation of the name of the tenant. Validation Rules: Value gets populated from MT.TENANT table record of subject tenant. Noinput field |
| 4 | `MT.CLN.TENANT.TYPE` | `MtTenantCleanup_TenantType` | TField |  | Gives a visual confirmation of the type of tenant system e.g. LIVE, DEMO, TRAINING, UAT etc. Validation Rules: Value gets populated from MT.TENANT table record of subject tenant. Noinput field |
| 5 | `MT.CLN.TENANT.STATUS` | `MtTenantCleanup_TenantStatus` | TField |  | Gives a visual confirmation of the status of the tenant being off-boarded. A report run can be made on an active tenant but only a deactivated tenant can be removed by this process. Validation Rules: Noinput field. Value gets populated from MT.TENANT table record of subject tenant. Values are: 1. ACTIVATED - for activated tenant only OPERATION.MODE allowed is REPORT. 2. DEACTIVATED - for deactivated tenant both REMOVE and REPORT mode is allowed. |
| 6 | `MT.CLN.DATA.PRESENT` | `MtTenantCleanup_DataPresent` | TField |  | Indicates the presence of data, related to the tenant id, which is eligible for removal. Validation Rules: Noinput Field. System generated values are: YES - Set when data associated to the tenant is found. Or if the MT.TENANT is the only data and this is set as de-activated. NO - Set when no data associated to the tenant is found. Or if the MT.TENANT is the only data and this is set as activated (Records for tenants who have an activated status cannot be removed by this process). Note - data can be removed only if MT.TENANT is deactivated. Data presence check is made for any status or mode. |
| 7 | `MT.CLN.TENANT.GROUPS` | `MtTenantCleanup_TenantGroups` |  |  |  |
| 8 | `MT.CLN.SERVICE.CONSOLE.RECS` | `MtTenantCleanup_ServiceConsoleRecs` |  |  |  |
| 9 | `MT.CLN.REPLICATE.CONSOLE.RECS` | `MtTenantCleanup_ReplicateConsoleRecs` |  |  |  |
| 10 | `MT.CLN.TENANT.CONTACTS` | `MtTenantCleanup_TenantContacts` |  |  |  |
| 11 | `MT.CLN.UNAUTH.RECS` | `MtTenantCleanup_UnauthRecs` |  |  |  |
| 12 | `MT.CLN.RESERVED.13` | `MtTenantCleanup_Reserved13` | TField |  |  |
| 13 | `MT.CLN.RESERVED.12` | `MtTenantCleanup_Reserved12` | TField |  |  |
| 14 | `MT.CLN.RESERVED.11` | `MtTenantCleanup_Reserved11` | TField |  |  |
| 15 | `MT.CLN.LAST.RUN.DATE` | `MtTenantCleanup_LastRunDate` | TField |  | The date when the report or removal process was last run. Validation Rules: Noinput field. System populates the processing date. Display format: DD MMM YYYY, for e.g: 11 MAY 2015 |
| 16 | `MT.CLN.RESERVED.10` | `MtTenantCleanup_Reserved10` | TField |  |  |
| 17 | `MT.CLN.RESERVED.9` | `MtTenantCleanup_Reserved9` | TField |  |  |
| 18 | `MT.CLN.RESERVED.8` | `MtTenantCleanup_Reserved8` | TField |  |  |
| 19 | `MT.CLN.RESERVED.7` | `MtTenantCleanup_Reserved7` | TField |  |  |
| 20 | `MT.CLN.RESERVED.6` | `MtTenantCleanup_Reserved6` | TField |  |  |
| 21 | `MT.CLN.RESERVED.5` | `MtTenantCleanup_Reserved5` | TField |  |  |
| 22 | `MT.CLN.RESERVED.4` | `MtTenantCleanup_Reserved4` | TField |  |  |
| 23 | `MT.CLN.RESERVED.3` | `MtTenantCleanup_Reserved3` | TField |  |  |
| 24 | `MT.CLN.RESERVED.2` | `MtTenantCleanup_Reserved2` | TField |  |  |
| 25 | `MT.CLN.RESERVED.1` | `MtTenantCleanup_Reserved1` | TField |  |  |
| 26 | `MT.CLN.LOCAL.REF` | `MtTenantCleanup_LocalRef` |  |  |  |
| 27 | `MT.CLN.OVERRIDE` | `MtTenantCleanup_Override` |  |  |  |
| 28 | `MT.CLN.RECORD.STATUS` | `MtTenantCleanup_RecordStatus` | String |  |  |
| 29 | `MT.CLN.CURR.NO` | `MtTenantCleanup_CurrNo` | String |  |  |
| 30 | `MT.CLN.INPUTTER` | `MtTenantCleanup_Inputter` |  |  |  |
| 31 | `MT.CLN.DATE.TIME` | `MtTenantCleanup_DateTime` |  |  |  |
| 32 | `MT.CLN.AUTHORISER` | `MtTenantCleanup_Authoriser` | String |  |  |
| 33 | `MT.CLN.CO.CODE` | `MtTenantCleanup_CoCode` | String |  |  |
| 34 | `MT.CLN.DEPT.CODE` | `MtTenantCleanup_DeptCode` | String |  |  |
| 35 | `MT.CLN.AUDITOR.CODE` | `MtTenantCleanup_AuditorCode` | String |  |  |
| 36 | `MT.CLN.AUDIT.DATE.TIME` | `MtTenantCleanup_AuditDateTime` | String |  |  |
