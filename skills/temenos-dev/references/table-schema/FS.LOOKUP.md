# FS.LOOKUP — Table Schema

> Source: `INSERTS/I_F.FS.LOOKUP` in `FS_ApplicationFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.LU.DESCRIPTION` | `FsLookup_Description` |  |  |  |
| 2 | `FS.LU.OTHER.INFO` | `FsLookup_OtherInfo` | TField |  | Specifies the other information about the lookup. |
| 3 | `FS.LU.DATA.NAME` | `FsLookup_DataName` |  |  |  |
| 4 | `FS.LU.DATA.VALUE` | `FsLookup_DataValue` |  |  |  |
| 5 | `FS.LU.VIRTUAL.TABLE` | `FsLookup_VirtualTable` | TField |  | The first part of the ID (before the asterix-*) will be automatically populated in this non-input field. This is being done to enable the selection on FS.LOOKUP based on the virtual table name |
| 6 | `FS.LU.LOOKUP.ID` | `FsLookup_LookupId` | TField |  | The second part of the ID (after the asterix-*) will be automatically populated in this non-input field. This is being done to enable the selection on FS.LOOKUP based on the field value |
| 7 | `FS.LU.RECORD.ID` | `FsLookup_RecordId` | TField |  |  |
| 8 | `FS.LU.RESERVED.9` | `FsLookup_Reserved9` | TField |  |  |
| 9 | `FS.LU.RESERVED.8` | `FsLookup_Reserved8` | TField |  |  |
| 10 | `FS.LU.RESERVED.7` | `FsLookup_Reserved7` | TField |  |  |
| 11 | `FS.LU.RESERVED.6` | `FsLookup_Reserved6` | TField |  |  |
| 12 | `FS.LU.RESERVED.5` | `FsLookup_Reserved5` | TField |  |  |
| 13 | `FS.LU.RESERVED.4` | `FsLookup_Reserved4` | TField |  |  |
| 14 | `FS.LU.RESERVED.3` | `FsLookup_Reserved3` | TField |  |  |
| 15 | `FS.LU.RESERVED.2` | `FsLookup_Reserved2` | TField |  |  |
| 16 | `FS.LU.RESERVED.1` | `FsLookup_Reserved1` | TField |  |  |
| 17 | `FS.LU.LOCAL.REF` | `FsLookup_LocalRef` |  |  |  |
| 18 | `FS.LU.RECORD.STATUS` | `FsLookup_RecordStatus` | String |  |  |
| 19 | `FS.LU.CURR.NO` | `FsLookup_CurrNo` | String |  |  |
| 20 | `FS.LU.INPUTTER` | `FsLookup_Inputter` |  |  |  |
| 21 | `FS.LU.DATE.TIME` | `FsLookup_DateTime` |  |  |  |
| 22 | `FS.LU.AUTHORISER` | `FsLookup_Authoriser` | String |  |  |
| 23 | `FS.LU.CO.CODE` | `FsLookup_CoCode` | String |  |  |
| 24 | `FS.LU.DEPT.CODE` | `FsLookup_DeptCode` | String |  |  |
| 25 | `FS.LU.AUDITOR.CODE` | `FsLookup_AuditorCode` | String |  |  |
| 26 | `FS.LU.AUDIT.DATE.TIME` | `FsLookup_AuditDateTime` | String |  |  |
