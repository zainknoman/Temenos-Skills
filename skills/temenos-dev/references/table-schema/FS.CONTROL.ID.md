# FS.CONTROL.ID — Table Schema

> Source: `INSERTS/I_F.FS.CONTROL.ID` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.CONTROL.ID.DESCRIPTION` | `FsControlId_Description` |  |  |  |
| 2 | `FS.CONTROL.ID.FILTER.KEY` | `FsControlId_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.CONTROL.ID.RECORD.ID` | `FsControlId_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.CONTROL.ID.RESERVED10` | `FsControlId_Reserved10` | TField |  |  |
| 5 | `FS.CONTROL.ID.RESERVED9` | `FsControlId_Reserved9` | TField |  |  |
| 6 | `FS.CONTROL.ID.RESERVED8` | `FsControlId_Reserved8` | TField |  |  |
| 7 | `FS.CONTROL.ID.RESERVED7` | `FsControlId_Reserved7` | TField |  |  |
| 8 | `FS.CONTROL.ID.RESERVED6` | `FsControlId_Reserved6` | TField |  |  |
| 9 | `FS.CONTROL.ID.RESERVED5` | `FsControlId_Reserved5` | TField |  |  |
| 10 | `FS.CONTROL.ID.RESERVED4` | `FsControlId_Reserved4` | TField |  |  |
| 11 | `FS.CONTROL.ID.RESERVED3` | `FsControlId_Reserved3` | TField |  |  |
| 12 | `FS.CONTROL.ID.RESERVED2` | `FsControlId_Reserved2` | TField |  |  |
| 13 | `FS.CONTROL.ID.RESERVED1` | `FsControlId_Reserved1` | TField |  |  |
| 14 | `FS.CONTROL.ID.LOCAL.REF` | `FsControlId_LocalRef` |  |  |  |
| 15 | `FS.CONTROL.ID.OVERRIDE` | `FsControlId_Override` |  |  |  |
| 16 | `FS.CONTROL.ID.RECORD.STATUS` | `FsControlId_RecordStatus` | String |  |  |
| 17 | `FS.CONTROL.ID.CURR.NO` | `FsControlId_CurrNo` | String |  |  |
| 18 | `FS.CONTROL.ID.INPUTTER` | `FsControlId_Inputter` |  |  |  |
| 19 | `FS.CONTROL.ID.DATE.TIME` | `FsControlId_DateTime` |  |  |  |
| 20 | `FS.CONTROL.ID.AUTHORISER` | `FsControlId_Authoriser` | String |  |  |
| 21 | `FS.CONTROL.ID.CO.CODE` | `FsControlId_CoCode` | String |  |  |
| 22 | `FS.CONTROL.ID.DEPT.CODE` | `FsControlId_DeptCode` | String |  |  |
| 23 | `FS.CONTROL.ID.AUDITOR.CODE` | `FsControlId_AuditorCode` | String |  |  |
| 24 | `FS.CONTROL.ID.AUDIT.DATE.TIME` | `FsControlId_AuditDateTime` | String |  |  |
