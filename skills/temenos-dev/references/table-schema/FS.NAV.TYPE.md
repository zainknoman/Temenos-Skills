# FS.NAV.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.NAV.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.NAV.TYPE.DESCRIPTION` | `FsNavType_Description` |  |  |  |
| 2 | `FS.NAV.TYPE.FILTER.KEY` | `FsNavType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.NAV.TYPE.RECORD.ID` | `FsNavType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.NAV.TYPE.RESERVED10` | `FsNavType_Reserved10` | TField |  |  |
| 5 | `FS.NAV.TYPE.RESERVED9` | `FsNavType_Reserved9` | TField |  |  |
| 6 | `FS.NAV.TYPE.RESERVED8` | `FsNavType_Reserved8` | TField |  |  |
| 7 | `FS.NAV.TYPE.RESERVED7` | `FsNavType_Reserved7` | TField |  |  |
| 8 | `FS.NAV.TYPE.RESERVED6` | `FsNavType_Reserved6` | TField |  |  |
| 9 | `FS.NAV.TYPE.RESERVED5` | `FsNavType_Reserved5` | TField |  |  |
| 10 | `FS.NAV.TYPE.RESERVED4` | `FsNavType_Reserved4` | TField |  |  |
| 11 | `FS.NAV.TYPE.RESERVED3` | `FsNavType_Reserved3` | TField |  |  |
| 12 | `FS.NAV.TYPE.RESERVED2` | `FsNavType_Reserved2` | TField |  |  |
| 13 | `FS.NAV.TYPE.RESERVED1` | `FsNavType_Reserved1` | TField |  |  |
| 14 | `FS.NAV.TYPE.LOCAL.REF` | `FsNavType_LocalRef` |  |  |  |
| 15 | `FS.NAV.TYPE.OVERRIDE` | `FsNavType_Override` |  |  |  |
| 16 | `FS.NAV.TYPE.RECORD.STATUS` | `FsNavType_RecordStatus` | String |  |  |
| 17 | `FS.NAV.TYPE.CURR.NO` | `FsNavType_CurrNo` | String |  |  |
| 18 | `FS.NAV.TYPE.INPUTTER` | `FsNavType_Inputter` |  |  |  |
| 19 | `FS.NAV.TYPE.DATE.TIME` | `FsNavType_DateTime` |  |  |  |
| 20 | `FS.NAV.TYPE.AUTHORISER` | `FsNavType_Authoriser` | String |  |  |
| 21 | `FS.NAV.TYPE.CO.CODE` | `FsNavType_CoCode` | String |  |  |
| 22 | `FS.NAV.TYPE.DEPT.CODE` | `FsNavType_DeptCode` | String |  |  |
| 23 | `FS.NAV.TYPE.AUDITOR.CODE` | `FsNavType_AuditorCode` | String |  |  |
| 24 | `FS.NAV.TYPE.AUDIT.DATE.TIME` | `FsNavType_AuditDateTime` | String |  |  |
