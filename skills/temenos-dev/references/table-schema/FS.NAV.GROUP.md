# FS.NAV.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.NAV.GROUP` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.NAV.GROUP.DESCRIPTION` | `FsNavGroup_Description` |  |  |  |
| 2 | `FS.NAV.GROUP.FILTER.KEY` | `FsNavGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.NAV.GROUP.RECORD.ID` | `FsNavGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.NAV.GROUP.RESERVED10` | `FsNavGroup_Reserved10` | TField |  |  |
| 5 | `FS.NAV.GROUP.RESERVED9` | `FsNavGroup_Reserved9` | TField |  |  |
| 6 | `FS.NAV.GROUP.RESERVED8` | `FsNavGroup_Reserved8` | TField |  |  |
| 7 | `FS.NAV.GROUP.RESERVED7` | `FsNavGroup_Reserved7` | TField |  |  |
| 8 | `FS.NAV.GROUP.RESERVED6` | `FsNavGroup_Reserved6` | TField |  |  |
| 9 | `FS.NAV.GROUP.RESERVED5` | `FsNavGroup_Reserved5` | TField |  |  |
| 10 | `FS.NAV.GROUP.RESERVED4` | `FsNavGroup_Reserved4` | TField |  |  |
| 11 | `FS.NAV.GROUP.RESERVED3` | `FsNavGroup_Reserved3` | TField |  |  |
| 12 | `FS.NAV.GROUP.RESERVED2` | `FsNavGroup_Reserved2` | TField |  |  |
| 13 | `FS.NAV.GROUP.RESERVED1` | `FsNavGroup_Reserved1` | TField |  |  |
| 14 | `FS.NAV.GROUP.LOCAL.REF` | `FsNavGroup_LocalRef` |  |  |  |
| 15 | `FS.NAV.GROUP.OVERRIDE` | `FsNavGroup_Override` |  |  |  |
| 16 | `FS.NAV.GROUP.RECORD.STATUS` | `FsNavGroup_RecordStatus` | String |  |  |
| 17 | `FS.NAV.GROUP.CURR.NO` | `FsNavGroup_CurrNo` | String |  |  |
| 18 | `FS.NAV.GROUP.INPUTTER` | `FsNavGroup_Inputter` |  |  |  |
| 19 | `FS.NAV.GROUP.DATE.TIME` | `FsNavGroup_DateTime` |  |  |  |
| 20 | `FS.NAV.GROUP.AUTHORISER` | `FsNavGroup_Authoriser` | String |  |  |
| 21 | `FS.NAV.GROUP.CO.CODE` | `FsNavGroup_CoCode` | String |  |  |
| 22 | `FS.NAV.GROUP.DEPT.CODE` | `FsNavGroup_DeptCode` | String |  |  |
| 23 | `FS.NAV.GROUP.AUDITOR.CODE` | `FsNavGroup_AuditorCode` | String |  |  |
| 24 | `FS.NAV.GROUP.AUDIT.DATE.TIME` | `FsNavGroup_AuditDateTime` | String |  |  |
