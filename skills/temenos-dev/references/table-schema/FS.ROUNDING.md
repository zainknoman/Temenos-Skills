# FS.ROUNDING — Table Schema

> Source: `INSERTS/I_F.FS.ROUNDING` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ROUNDING.DESCRIPTION` | `FsRounding_Description` |  |  |  |
| 2 | `FS.ROUNDING.FILTER.KEY` | `FsRounding_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ROUNDING.RECORD.ID` | `FsRounding_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ROUNDING.RESERVED10` | `FsRounding_Reserved10` | TField |  |  |
| 5 | `FS.ROUNDING.RESERVED9` | `FsRounding_Reserved9` | TField |  |  |
| 6 | `FS.ROUNDING.RESERVED8` | `FsRounding_Reserved8` | TField |  |  |
| 7 | `FS.ROUNDING.RESERVED7` | `FsRounding_Reserved7` | TField |  |  |
| 8 | `FS.ROUNDING.RESERVED6` | `FsRounding_Reserved6` | TField |  |  |
| 9 | `FS.ROUNDING.RESERVED5` | `FsRounding_Reserved5` | TField |  |  |
| 10 | `FS.ROUNDING.RESERVED4` | `FsRounding_Reserved4` | TField |  |  |
| 11 | `FS.ROUNDING.RESERVED3` | `FsRounding_Reserved3` | TField |  |  |
| 12 | `FS.ROUNDING.RESERVED2` | `FsRounding_Reserved2` | TField |  |  |
| 13 | `FS.ROUNDING.RESERVED1` | `FsRounding_Reserved1` | TField |  |  |
| 14 | `FS.ROUNDING.LOCAL.REF` | `FsRounding_LocalRef` |  |  |  |
| 15 | `FS.ROUNDING.OVERRIDE` | `FsRounding_Override` |  |  |  |
| 16 | `FS.ROUNDING.RECORD.STATUS` | `FsRounding_RecordStatus` | String |  |  |
| 17 | `FS.ROUNDING.CURR.NO` | `FsRounding_CurrNo` | String |  |  |
| 18 | `FS.ROUNDING.INPUTTER` | `FsRounding_Inputter` |  |  |  |
| 19 | `FS.ROUNDING.DATE.TIME` | `FsRounding_DateTime` |  |  |  |
| 20 | `FS.ROUNDING.AUTHORISER` | `FsRounding_Authoriser` | String |  |  |
| 21 | `FS.ROUNDING.CO.CODE` | `FsRounding_CoCode` | String |  |  |
| 22 | `FS.ROUNDING.DEPT.CODE` | `FsRounding_DeptCode` | String |  |  |
| 23 | `FS.ROUNDING.AUDITOR.CODE` | `FsRounding_AuditorCode` | String |  |  |
| 24 | `FS.ROUNDING.AUDIT.DATE.TIME` | `FsRounding_AuditDateTime` | String |  |  |
