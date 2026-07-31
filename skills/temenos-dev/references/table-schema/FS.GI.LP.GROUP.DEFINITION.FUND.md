# FS.GI.LP.GROUP.DEFINITION.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GROUP.DEFINITION.FUND` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GROUP.DEFINITION.FUND.LP.GROUP.ID` | `FsGiLpGroupDefinitionFund_LpGroupId` | TField |  | Internal Id for the group of partners Multifonds DB Column is GROUP_ID. |
| 2 | `FS.GI.LP.GROUP.DEFINITION.FUND.LP.GROUP.TYPE` | `FsGiLpGroupDefinitionFund_LpGroupType` | TField |  | Internal partners group usage type Multifonds DB Column is GROUP_TYPE. |
| 3 | `FS.GI.LP.GROUP.DEFINITION.FUND.REGISTER.ID` | `FsGiLpGroupDefinitionFund_RegisterId` | TField |  | Partners Internal register Id Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.LP.GROUP.DEFINITION.FUND.FUND.ID` | `FsGiLpGroupDefinitionFund_FundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.LP.GROUP.DEFINITION.FUND.SHARE.CLASS.CODE` | `FsGiLpGroupDefinitionFund_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 6 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED10` | `FsGiLpGroupDefinitionFund_Reserved10` | TField |  |  |
| 7 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED9` | `FsGiLpGroupDefinitionFund_Reserved9` | TField |  |  |
| 8 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED8` | `FsGiLpGroupDefinitionFund_Reserved8` | TField |  |  |
| 9 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED7` | `FsGiLpGroupDefinitionFund_Reserved7` | TField |  |  |
| 10 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED6` | `FsGiLpGroupDefinitionFund_Reserved6` | TField |  |  |
| 11 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED5` | `FsGiLpGroupDefinitionFund_Reserved5` | TField |  |  |
| 12 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED4` | `FsGiLpGroupDefinitionFund_Reserved4` | TField |  |  |
| 13 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED3` | `FsGiLpGroupDefinitionFund_Reserved3` | TField |  |  |
| 14 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED2` | `FsGiLpGroupDefinitionFund_Reserved2` | TField |  |  |
| 15 | `FS.GI.LP.GROUP.DEFINITION.FUND.RESERVED1` | `FsGiLpGroupDefinitionFund_Reserved1` | TField |  |  |
| 16 | `FS.GI.LP.GROUP.DEFINITION.FUND.OVERRIDE` | `FsGiLpGroupDefinitionFund_Override` |  |  |  |
| 17 | `FS.GI.LP.GROUP.DEFINITION.FUND.LOCAL.REF` | `FsGiLpGroupDefinitionFund_LocalRef` |  |  |  |
| 18 | `FS.GI.LP.GROUP.DEFINITION.FUND.RECORD.STATUS` | `FsGiLpGroupDefinitionFund_RecordStatus` | String |  |  |
| 19 | `FS.GI.LP.GROUP.DEFINITION.FUND.CURR.NO` | `FsGiLpGroupDefinitionFund_CurrNo` | String |  |  |
| 20 | `FS.GI.LP.GROUP.DEFINITION.FUND.INPUTTER` | `FsGiLpGroupDefinitionFund_Inputter` |  |  |  |
| 21 | `FS.GI.LP.GROUP.DEFINITION.FUND.DATE.TIME` | `FsGiLpGroupDefinitionFund_DateTime` |  |  |  |
| 22 | `FS.GI.LP.GROUP.DEFINITION.FUND.AUTHORISER` | `FsGiLpGroupDefinitionFund_Authoriser` | String |  |  |
| 23 | `FS.GI.LP.GROUP.DEFINITION.FUND.CO.CODE` | `FsGiLpGroupDefinitionFund_CoCode` | String |  |  |
| 24 | `FS.GI.LP.GROUP.DEFINITION.FUND.DEPT.CODE` | `FsGiLpGroupDefinitionFund_DeptCode` | String |  |  |
| 25 | `FS.GI.LP.GROUP.DEFINITION.FUND.AUDITOR.CODE` | `FsGiLpGroupDefinitionFund_AuditorCode` | String |  |  |
| 26 | `FS.GI.LP.GROUP.DEFINITION.FUND.AUDIT.DATE.TIME` | `FsGiLpGroupDefinitionFund_AuditDateTime` | String |  |  |
