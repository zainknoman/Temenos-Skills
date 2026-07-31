# FS.STATE.CODES — Table Schema

> Source: `INSERTS/I_F.FS.STATE.CODES` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.STATE.CODES.DESCRIPTION` | `FsStateCodes_Description` |  |  |  |
| 2 | `FS.STATE.CODES.FILTER.KEY` | `FsStateCodes_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.STATE.CODES.RECORD.ID` | `FsStateCodes_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.STATE.CODES.RESERVED10` | `FsStateCodes_Reserved10` | TField |  |  |
| 5 | `FS.STATE.CODES.RESERVED9` | `FsStateCodes_Reserved9` | TField |  |  |
| 6 | `FS.STATE.CODES.RESERVED8` | `FsStateCodes_Reserved8` | TField |  |  |
| 7 | `FS.STATE.CODES.RESERVED7` | `FsStateCodes_Reserved7` | TField |  |  |
| 8 | `FS.STATE.CODES.RESERVED6` | `FsStateCodes_Reserved6` | TField |  |  |
| 9 | `FS.STATE.CODES.RESERVED5` | `FsStateCodes_Reserved5` | TField |  |  |
| 10 | `FS.STATE.CODES.RESERVED4` | `FsStateCodes_Reserved4` | TField |  |  |
| 11 | `FS.STATE.CODES.RESERVED3` | `FsStateCodes_Reserved3` | TField |  |  |
| 12 | `FS.STATE.CODES.RESERVED2` | `FsStateCodes_Reserved2` | TField |  |  |
| 13 | `FS.STATE.CODES.RESERVED1` | `FsStateCodes_Reserved1` | TField |  |  |
| 14 | `FS.STATE.CODES.LOCAL.REF` | `FsStateCodes_LocalRef` |  |  |  |
| 15 | `FS.STATE.CODES.OVERRIDE` | `FsStateCodes_Override` |  |  |  |
| 16 | `FS.STATE.CODES.RECORD.STATUS` | `FsStateCodes_RecordStatus` | String |  |  |
| 17 | `FS.STATE.CODES.CURR.NO` | `FsStateCodes_CurrNo` | String |  |  |
| 18 | `FS.STATE.CODES.INPUTTER` | `FsStateCodes_Inputter` |  |  |  |
| 19 | `FS.STATE.CODES.DATE.TIME` | `FsStateCodes_DateTime` |  |  |  |
| 20 | `FS.STATE.CODES.AUTHORISER` | `FsStateCodes_Authoriser` | String |  |  |
| 21 | `FS.STATE.CODES.CO.CODE` | `FsStateCodes_CoCode` | String |  |  |
| 22 | `FS.STATE.CODES.DEPT.CODE` | `FsStateCodes_DeptCode` | String |  |  |
| 23 | `FS.STATE.CODES.AUDITOR.CODE` | `FsStateCodes_AuditorCode` | String |  |  |
| 24 | `FS.STATE.CODES.AUDIT.DATE.TIME` | `FsStateCodes_AuditDateTime` | String |  |  |
