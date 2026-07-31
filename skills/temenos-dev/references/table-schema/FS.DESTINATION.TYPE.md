# FS.DESTINATION.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.DESTINATION.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.DESTINATION.TYPE.DESCRIPTION` | `FsDestinationType_Description` |  |  |  |
| 2 | `FS.DESTINATION.TYPE.FILTER.KEY` | `FsDestinationType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.DESTINATION.TYPE.RECORD.ID` | `FsDestinationType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.DESTINATION.TYPE.RESERVED10` | `FsDestinationType_Reserved10` | TField |  |  |
| 5 | `FS.DESTINATION.TYPE.RESERVED9` | `FsDestinationType_Reserved9` | TField |  |  |
| 6 | `FS.DESTINATION.TYPE.RESERVED8` | `FsDestinationType_Reserved8` | TField |  |  |
| 7 | `FS.DESTINATION.TYPE.RESERVED7` | `FsDestinationType_Reserved7` | TField |  |  |
| 8 | `FS.DESTINATION.TYPE.RESERVED6` | `FsDestinationType_Reserved6` | TField |  |  |
| 9 | `FS.DESTINATION.TYPE.RESERVED5` | `FsDestinationType_Reserved5` | TField |  |  |
| 10 | `FS.DESTINATION.TYPE.RESERVED4` | `FsDestinationType_Reserved4` | TField |  |  |
| 11 | `FS.DESTINATION.TYPE.RESERVED3` | `FsDestinationType_Reserved3` | TField |  |  |
| 12 | `FS.DESTINATION.TYPE.RESERVED2` | `FsDestinationType_Reserved2` | TField |  |  |
| 13 | `FS.DESTINATION.TYPE.RESERVED1` | `FsDestinationType_Reserved1` | TField |  |  |
| 14 | `FS.DESTINATION.TYPE.LOCAL.REF` | `FsDestinationType_LocalRef` |  |  |  |
| 15 | `FS.DESTINATION.TYPE.OVERRIDE` | `FsDestinationType_Override` |  |  |  |
| 16 | `FS.DESTINATION.TYPE.RECORD.STATUS` | `FsDestinationType_RecordStatus` | String |  |  |
| 17 | `FS.DESTINATION.TYPE.CURR.NO` | `FsDestinationType_CurrNo` | String |  |  |
| 18 | `FS.DESTINATION.TYPE.INPUTTER` | `FsDestinationType_Inputter` |  |  |  |
| 19 | `FS.DESTINATION.TYPE.DATE.TIME` | `FsDestinationType_DateTime` |  |  |  |
| 20 | `FS.DESTINATION.TYPE.AUTHORISER` | `FsDestinationType_Authoriser` | String |  |  |
| 21 | `FS.DESTINATION.TYPE.CO.CODE` | `FsDestinationType_CoCode` | String |  |  |
| 22 | `FS.DESTINATION.TYPE.DEPT.CODE` | `FsDestinationType_DeptCode` | String |  |  |
| 23 | `FS.DESTINATION.TYPE.AUDITOR.CODE` | `FsDestinationType_AuditorCode` | String |  |  |
| 24 | `FS.DESTINATION.TYPE.AUDIT.DATE.TIME` | `FsDestinationType_AuditDateTime` | String |  |  |
