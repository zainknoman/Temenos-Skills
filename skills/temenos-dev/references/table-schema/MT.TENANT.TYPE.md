# MT.TENANT.TYPE — Table Schema

> Source: `INSERTS/I_F.MT.TENANT.TYPE` in `MT_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MT.TT.DESCRIPTION` | `MtTenantType_Description` |  |  |  |
| 2 | `MT.TT.TENANT.TYPE.GROUP` | `MtTenantType_TenantTypeGroup` | TField |  | Specifies the group under which the tenant type can be categorized Valid values are: 1. LIVE - Indicates the t24 instance(tenant system) used is a LIVE or PRODUCTION system. 2. NON-LIVE - Indicates the t24 instance(tenant system) is used for other purposes like DEMO, UAT, TRAINING etc. |
| 3 | `MT.TT.RESERVED.5` | `MtTenantType_Reserved5` | TField |  |  |
| 4 | `MT.TT.RESERVED.4` | `MtTenantType_Reserved4` | TField |  |  |
| 5 | `MT.TT.RESERVED.3` | `MtTenantType_Reserved3` | TField |  |  |
| 6 | `MT.TT.RESERVED.2` | `MtTenantType_Reserved2` | TField |  |  |
| 7 | `MT.TT.RESERVED.1` | `MtTenantType_Reserved1` | TField |  |  |
| 8 | `MT.TT.LOCAL.REF` | `MtTenantType_LocalRef` |  |  |  |
| 9 | `MT.TT.OVERRIDE` | `MtTenantType_Override` |  |  |  |
| 10 | `MT.TT.RECORD.STATUS` | `MtTenantType_RecordStatus` | String |  |  |
| 11 | `MT.TT.CURR.NO` | `MtTenantType_CurrNo` | String |  |  |
| 12 | `MT.TT.INPUTTER` | `MtTenantType_Inputter` |  |  |  |
| 13 | `MT.TT.DATE.TIME` | `MtTenantType_DateTime` |  |  |  |
| 14 | `MT.TT.AUTHORISER` | `MtTenantType_Authoriser` | String |  |  |
| 15 | `MT.TT.CO.CODE` | `MtTenantType_CoCode` | String |  |  |
| 16 | `MT.TT.DEPT.CODE` | `MtTenantType_DeptCode` | String |  |  |
| 17 | `MT.TT.AUDITOR.CODE` | `MtTenantType_AuditorCode` | String |  |  |
| 18 | `MT.TT.AUDIT.DATE.TIME` | `MtTenantType_AuditDateTime` | String |  |  |
