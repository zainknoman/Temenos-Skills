# FS.RELATION.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.RELATION.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.RELATION.TYPE.DESCRIPTION` | `FsRelationType_Description` |  |  |  |
| 2 | `FS.RELATION.TYPE.FILTER.KEY` | `FsRelationType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.RELATION.TYPE.RECORD.ID` | `FsRelationType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.RELATION.TYPE.RESERVED10` | `FsRelationType_Reserved10` | TField |  |  |
| 5 | `FS.RELATION.TYPE.RESERVED9` | `FsRelationType_Reserved9` | TField |  |  |
| 6 | `FS.RELATION.TYPE.RESERVED8` | `FsRelationType_Reserved8` | TField |  |  |
| 7 | `FS.RELATION.TYPE.RESERVED7` | `FsRelationType_Reserved7` | TField |  |  |
| 8 | `FS.RELATION.TYPE.RESERVED6` | `FsRelationType_Reserved6` | TField |  |  |
| 9 | `FS.RELATION.TYPE.RESERVED5` | `FsRelationType_Reserved5` | TField |  |  |
| 10 | `FS.RELATION.TYPE.RESERVED4` | `FsRelationType_Reserved4` | TField |  |  |
| 11 | `FS.RELATION.TYPE.RESERVED3` | `FsRelationType_Reserved3` | TField |  |  |
| 12 | `FS.RELATION.TYPE.RESERVED2` | `FsRelationType_Reserved2` | TField |  |  |
| 13 | `FS.RELATION.TYPE.RESERVED1` | `FsRelationType_Reserved1` | TField |  |  |
| 14 | `FS.RELATION.TYPE.LOCAL.REF` | `FsRelationType_LocalRef` |  |  |  |
| 15 | `FS.RELATION.TYPE.OVERRIDE` | `FsRelationType_Override` |  |  |  |
| 16 | `FS.RELATION.TYPE.RECORD.STATUS` | `FsRelationType_RecordStatus` | String |  |  |
| 17 | `FS.RELATION.TYPE.CURR.NO` | `FsRelationType_CurrNo` | String |  |  |
| 18 | `FS.RELATION.TYPE.INPUTTER` | `FsRelationType_Inputter` |  |  |  |
| 19 | `FS.RELATION.TYPE.DATE.TIME` | `FsRelationType_DateTime` |  |  |  |
| 20 | `FS.RELATION.TYPE.AUTHORISER` | `FsRelationType_Authoriser` | String |  |  |
| 21 | `FS.RELATION.TYPE.CO.CODE` | `FsRelationType_CoCode` | String |  |  |
| 22 | `FS.RELATION.TYPE.DEPT.CODE` | `FsRelationType_DeptCode` | String |  |  |
| 23 | `FS.RELATION.TYPE.AUDITOR.CODE` | `FsRelationType_AuditorCode` | String |  |  |
| 24 | `FS.RELATION.TYPE.AUDIT.DATE.TIME` | `FsRelationType_AuditDateTime` | String |  |  |
