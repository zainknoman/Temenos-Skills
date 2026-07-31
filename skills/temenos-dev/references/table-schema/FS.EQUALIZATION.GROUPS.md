# FS.EQUALIZATION.GROUPS — Table Schema

> Source: `INSERTS/I_F.FS.EQUALIZATION.GROUPS` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.EQUALIZATION.GROUPS.DESCRIPTION` | `FsEqualizationGroups_Description` |  |  |  |
| 2 | `FS.EQUALIZATION.GROUPS.FILTER.KEY` | `FsEqualizationGroups_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.EQUALIZATION.GROUPS.RECORD.ID` | `FsEqualizationGroups_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.EQUALIZATION.GROUPS.RESERVED10` | `FsEqualizationGroups_Reserved10` | TField |  |  |
| 5 | `FS.EQUALIZATION.GROUPS.RESERVED9` | `FsEqualizationGroups_Reserved9` | TField |  |  |
| 6 | `FS.EQUALIZATION.GROUPS.RESERVED8` | `FsEqualizationGroups_Reserved8` | TField |  |  |
| 7 | `FS.EQUALIZATION.GROUPS.RESERVED7` | `FsEqualizationGroups_Reserved7` | TField |  |  |
| 8 | `FS.EQUALIZATION.GROUPS.RESERVED6` | `FsEqualizationGroups_Reserved6` | TField |  |  |
| 9 | `FS.EQUALIZATION.GROUPS.RESERVED5` | `FsEqualizationGroups_Reserved5` | TField |  |  |
| 10 | `FS.EQUALIZATION.GROUPS.RESERVED4` | `FsEqualizationGroups_Reserved4` | TField |  |  |
| 11 | `FS.EQUALIZATION.GROUPS.RESERVED3` | `FsEqualizationGroups_Reserved3` | TField |  |  |
| 12 | `FS.EQUALIZATION.GROUPS.RESERVED2` | `FsEqualizationGroups_Reserved2` | TField |  |  |
| 13 | `FS.EQUALIZATION.GROUPS.RESERVED1` | `FsEqualizationGroups_Reserved1` | TField |  |  |
| 14 | `FS.EQUALIZATION.GROUPS.LOCAL.REF` | `FsEqualizationGroups_LocalRef` |  |  |  |
| 15 | `FS.EQUALIZATION.GROUPS.OVERRIDE` | `FsEqualizationGroups_Override` |  |  |  |
| 16 | `FS.EQUALIZATION.GROUPS.RECORD.STATUS` | `FsEqualizationGroups_RecordStatus` | String |  |  |
| 17 | `FS.EQUALIZATION.GROUPS.CURR.NO` | `FsEqualizationGroups_CurrNo` | String |  |  |
| 18 | `FS.EQUALIZATION.GROUPS.INPUTTER` | `FsEqualizationGroups_Inputter` |  |  |  |
| 19 | `FS.EQUALIZATION.GROUPS.DATE.TIME` | `FsEqualizationGroups_DateTime` |  |  |  |
| 20 | `FS.EQUALIZATION.GROUPS.AUTHORISER` | `FsEqualizationGroups_Authoriser` | String |  |  |
| 21 | `FS.EQUALIZATION.GROUPS.CO.CODE` | `FsEqualizationGroups_CoCode` | String |  |  |
| 22 | `FS.EQUALIZATION.GROUPS.DEPT.CODE` | `FsEqualizationGroups_DeptCode` | String |  |  |
| 23 | `FS.EQUALIZATION.GROUPS.AUDITOR.CODE` | `FsEqualizationGroups_AuditorCode` | String |  |  |
| 24 | `FS.EQUALIZATION.GROUPS.AUDIT.DATE.TIME` | `FsEqualizationGroups_AuditDateTime` | String |  |  |
