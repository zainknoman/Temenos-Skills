# FS.GA.WEM.FAMILY.NAVGROUPLINK — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.FAMILY.NAVGROUPLINK` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.PARENT.REF.ID` | `FsGaWemFamilyNavgrouplink_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.ORA.ROWID` | `FsGaWemFamilyNavgrouplink_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.FAMILY.ID` | `FsGaWemFamilyNavgrouplink_FamilyId` | TField |  | ID of the Family Multifonds DB Column is FAMILY_ID. |
| 4 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.NAV.GROUP` | `FsGaWemFamilyNavgrouplink_NavGroup` | TField |  | NAV Group Multifonds DB Column is NAV_GROUP. |
| 5 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED10` | `FsGaWemFamilyNavgrouplink_Reserved10` | TField |  |  |
| 6 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED9` | `FsGaWemFamilyNavgrouplink_Reserved9` | TField |  |  |
| 7 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED8` | `FsGaWemFamilyNavgrouplink_Reserved8` | TField |  |  |
| 8 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED7` | `FsGaWemFamilyNavgrouplink_Reserved7` | TField |  |  |
| 9 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED6` | `FsGaWemFamilyNavgrouplink_Reserved6` | TField |  |  |
| 10 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED5` | `FsGaWemFamilyNavgrouplink_Reserved5` | TField |  |  |
| 11 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED4` | `FsGaWemFamilyNavgrouplink_Reserved4` | TField |  |  |
| 12 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED3` | `FsGaWemFamilyNavgrouplink_Reserved3` | TField |  |  |
| 13 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED2` | `FsGaWemFamilyNavgrouplink_Reserved2` | TField |  |  |
| 14 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RESERVED1` | `FsGaWemFamilyNavgrouplink_Reserved1` | TField |  |  |
| 15 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.LOCAL.REF` | `FsGaWemFamilyNavgrouplink_LocalRef` |  |  |  |
| 16 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.OVERRIDE` | `FsGaWemFamilyNavgrouplink_Override` |  |  |  |
| 17 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.RECORD.STATUS` | `FsGaWemFamilyNavgrouplink_RecordStatus` | String |  |  |
| 18 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.CURR.NO` | `FsGaWemFamilyNavgrouplink_CurrNo` | String |  |  |
| 19 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.INPUTTER` | `FsGaWemFamilyNavgrouplink_Inputter` |  |  |  |
| 20 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.DATE.TIME` | `FsGaWemFamilyNavgrouplink_DateTime` |  |  |  |
| 21 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.AUTHORISER` | `FsGaWemFamilyNavgrouplink_Authoriser` | String |  |  |
| 22 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.CO.CODE` | `FsGaWemFamilyNavgrouplink_CoCode` | String |  |  |
| 23 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.DEPT.CODE` | `FsGaWemFamilyNavgrouplink_DeptCode` | String |  |  |
| 24 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.AUDITOR.CODE` | `FsGaWemFamilyNavgrouplink_AuditorCode` | String |  |  |
| 25 | `FS.GA.WEM.FAMILY.NAVGROUPLINK.AUDIT.DATE.TIME` | `FsGaWemFamilyNavgrouplink_AuditDateTime` | String |  |  |
