# FS.GI.LP.GROUP.DEFINITION.REGISTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GROUP.DEFINITION.REGISTER` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.LP.GROUP.ID` | `FsGiLpGroupDefinitionRegister_LpGroupId` | TField |  | Internal Id for the group of partners. Multifonds DB Column is GROUP_ID. |
| 2 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.LP.GROUP.TYPE` | `FsGiLpGroupDefinitionRegister_LpGroupType` | TField |  | Internal partners group usage type . Multifonds DB Column is GROUP_TYPE. |
| 3 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.REGISTER.ID` | `FsGiLpGroupDefinitionRegister_RegisterId` | TField |  | Partners Internal register Id. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED10` | `FsGiLpGroupDefinitionRegister_Reserved10` | TField |  |  |
| 5 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED9` | `FsGiLpGroupDefinitionRegister_Reserved9` | TField |  |  |
| 6 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED8` | `FsGiLpGroupDefinitionRegister_Reserved8` | TField |  |  |
| 7 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED7` | `FsGiLpGroupDefinitionRegister_Reserved7` | TField |  |  |
| 8 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED6` | `FsGiLpGroupDefinitionRegister_Reserved6` | TField |  |  |
| 9 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED5` | `FsGiLpGroupDefinitionRegister_Reserved5` | TField |  |  |
| 10 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED4` | `FsGiLpGroupDefinitionRegister_Reserved4` | TField |  |  |
| 11 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED3` | `FsGiLpGroupDefinitionRegister_Reserved3` | TField |  |  |
| 12 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED2` | `FsGiLpGroupDefinitionRegister_Reserved2` | TField |  |  |
| 13 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RESERVED1` | `FsGiLpGroupDefinitionRegister_Reserved1` | TField |  |  |
| 14 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.OVERRIDE` | `FsGiLpGroupDefinitionRegister_Override` |  |  |  |
| 15 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.LOCAL.REF` | `FsGiLpGroupDefinitionRegister_LocalRef` |  |  |  |
| 16 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.RECORD.STATUS` | `FsGiLpGroupDefinitionRegister_RecordStatus` | String |  |  |
| 17 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.CURR.NO` | `FsGiLpGroupDefinitionRegister_CurrNo` | String |  |  |
| 18 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.INPUTTER` | `FsGiLpGroupDefinitionRegister_Inputter` |  |  |  |
| 19 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.DATE.TIME` | `FsGiLpGroupDefinitionRegister_DateTime` |  |  |  |
| 20 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.AUTHORISER` | `FsGiLpGroupDefinitionRegister_Authoriser` | String |  |  |
| 21 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.CO.CODE` | `FsGiLpGroupDefinitionRegister_CoCode` | String |  |  |
| 22 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.DEPT.CODE` | `FsGiLpGroupDefinitionRegister_DeptCode` | String |  |  |
| 23 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.AUDITOR.CODE` | `FsGiLpGroupDefinitionRegister_AuditorCode` | String |  |  |
| 24 | `FS.GI.LP.GROUP.DEFINITION.REGISTER.AUDIT.DATE.TIME` | `FsGiLpGroupDefinitionRegister_AuditDateTime` | String |  |  |
