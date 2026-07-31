# MT.TENANT.GROUP — Table Schema

> Source: `INSERTS/I_F.MT.TENANT.GROUP` in `MT_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MT.GRP.DESCRIPTION` | `MtTenantGroup_Description` |  |  |  |
| 2 | `MT.GRP.TENANT.GROUP.TYPE` | `MtTenantGroup_TenantGroupType` | TField | Yes | Defines the type of tenant grouping, either LIVE or NON-LIVE tenant(s) grouping. This value will be used by the MT.REPLICATE.CONSOLE and MT.TSA.SERVICE.CONSOLE for a safety check (when trying to execute COB or Service or replicating table record in tenant system) to ensure that the correct group has been selected. Validation Rules: Acceptable values are: 1. LIVE - Indicates LIVE tenant grouping. 2. NON-LIVE - indicates grouping of non-live tenants such as DEMO, TRAINING, UAT etc. Mandatory field. |
| 3 | `MT.GRP.TENANT.GROUP.LEVEL` | `MtTenantGroup_TenantGroupLevel` | TField | Yes | This field is to define the level of tenant grouping. Whether the grouping is for COB settings or Service or a generic group for replicating t24 table records. Validation Rules: Acceptable values are: 1. COB :- indicates the COB level tenant grouping which can be used in MT.TSA.SERVICE.CONSOLE designed to run COB for group of tenants. 2. SERVICE :- indicates the SERVICE level tenant grouping which can be used in MT.TSA.SERVICE.CONSOLE designed to run SERVICE for group of tenants. 3. GENERIC :- indicates the generic tenant grouping which can be used in MT.REPLICATE.CONSOLE designed to replicate table content for group of tenants. If this field has value but no COB or Service related fields given, then this tenant grouping can be considered for standard COB or Service. Mandatory field |
| 4 | `MT.GRP.TENANT.ID` | `MtTenantGroup_TenantId` |  |  |  |
| 5 | `MT.GRP.COB.STYLE` | `MtTenantGroup_CobStyle` |  |  |  |
| 6 | `MT.GRP.COMPANY.GROUP.ID` | `MtTenantGroup_CompanyGroupId` |  |  |  |
| 7 | `MT.GRP.COMPANY.ID` | `MtTenantGroup_CompanyId` |  |  |  |
| 8 | `MT.GRP.SERVICE.COMP.MNE` | `MtTenantGroup_ServiceCompMne` |  |  |  |
| 9 | `MT.GRP.RESERVED.10` | `MtTenantGroup_Reserved10` | TField |  |  |
| 10 | `MT.GRP.RESERVED.9` | `MtTenantGroup_Reserved9` | TField |  |  |
| 11 | `MT.GRP.RESERVED.8` | `MtTenantGroup_Reserved8` | TField |  |  |
| 12 | `MT.GRP.RESERVED.7` | `MtTenantGroup_Reserved7` | TField |  |  |
| 13 | `MT.GRP.RESERVED.6` | `MtTenantGroup_Reserved6` | TField |  |  |
| 14 | `MT.GRP.RESERVED.5` | `MtTenantGroup_Reserved5` | TField |  |  |
| 15 | `MT.GRP.RESERVED.4` | `MtTenantGroup_Reserved4` | TField |  |  |
| 16 | `MT.GRP.RESERVED.3` | `MtTenantGroup_Reserved3` | TField |  |  |
| 17 | `MT.GRP.RESERVED.2` | `MtTenantGroup_Reserved2` | TField |  |  |
| 18 | `MT.GRP.RESERVED.1` | `MtTenantGroup_Reserved1` | TField |  |  |
| 19 | `MT.GRP.LOCAL.REF` | `MtTenantGroup_LocalRef` |  |  |  |
| 20 | `MT.GRP.OVERRIDE` | `MtTenantGroup_Override` |  |  |  |
| 21 | `MT.GRP.RECORD.STATUS` | `MtTenantGroup_RecordStatus` | String |  |  |
| 22 | `MT.GRP.CURR.NO` | `MtTenantGroup_CurrNo` | String |  |  |
| 23 | `MT.GRP.INPUTTER` | `MtTenantGroup_Inputter` |  |  |  |
| 24 | `MT.GRP.DATE.TIME` | `MtTenantGroup_DateTime` |  |  |  |
| 25 | `MT.GRP.AUTHORISER` | `MtTenantGroup_Authoriser` | String |  |  |
| 26 | `MT.GRP.CO.CODE` | `MtTenantGroup_CoCode` | String |  |  |
| 27 | `MT.GRP.DEPT.CODE` | `MtTenantGroup_DeptCode` | String |  |  |
| 28 | `MT.GRP.AUDITOR.CODE` | `MtTenantGroup_AuditorCode` | String |  |  |
| 29 | `MT.GRP.AUDIT.DATE.TIME` | `MtTenantGroup_AuditDateTime` | String |  |  |
