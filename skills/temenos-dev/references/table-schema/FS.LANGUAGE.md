# FS.LANGUAGE — Table Schema

> Source: `INSERTS/I_F.FS.LANGUAGE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.LANGUAGE.DESCRIPTION` | `FsLanguage_Description` |  |  |  |
| 2 | `FS.LANGUAGE.FILTER.KEY` | `FsLanguage_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.LANGUAGE.RECORD.ID` | `FsLanguage_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.LANGUAGE.RESERVED10` | `FsLanguage_Reserved10` | TField |  |  |
| 5 | `FS.LANGUAGE.RESERVED9` | `FsLanguage_Reserved9` | TField |  |  |
| 6 | `FS.LANGUAGE.RESERVED8` | `FsLanguage_Reserved8` | TField |  |  |
| 7 | `FS.LANGUAGE.RESERVED7` | `FsLanguage_Reserved7` | TField |  |  |
| 8 | `FS.LANGUAGE.RESERVED6` | `FsLanguage_Reserved6` | TField |  |  |
| 9 | `FS.LANGUAGE.RESERVED5` | `FsLanguage_Reserved5` | TField |  |  |
| 10 | `FS.LANGUAGE.RESERVED4` | `FsLanguage_Reserved4` | TField |  |  |
| 11 | `FS.LANGUAGE.RESERVED3` | `FsLanguage_Reserved3` | TField |  |  |
| 12 | `FS.LANGUAGE.RESERVED2` | `FsLanguage_Reserved2` | TField |  |  |
| 13 | `FS.LANGUAGE.RESERVED1` | `FsLanguage_Reserved1` | TField |  |  |
| 14 | `FS.LANGUAGE.LOCAL.REF` | `FsLanguage_LocalRef` |  |  |  |
| 15 | `FS.LANGUAGE.OVERRIDE` | `FsLanguage_Override` |  |  |  |
| 16 | `FS.LANGUAGE.RECORD.STATUS` | `FsLanguage_RecordStatus` | String |  |  |
| 17 | `FS.LANGUAGE.CURR.NO` | `FsLanguage_CurrNo` | String |  |  |
| 18 | `FS.LANGUAGE.INPUTTER` | `FsLanguage_Inputter` |  |  |  |
| 19 | `FS.LANGUAGE.DATE.TIME` | `FsLanguage_DateTime` |  |  |  |
| 20 | `FS.LANGUAGE.AUTHORISER` | `FsLanguage_Authoriser` | String |  |  |
| 21 | `FS.LANGUAGE.CO.CODE` | `FsLanguage_CoCode` | String |  |  |
| 22 | `FS.LANGUAGE.DEPT.CODE` | `FsLanguage_DeptCode` | String |  |  |
| 23 | `FS.LANGUAGE.AUDITOR.CODE` | `FsLanguage_AuditorCode` | String |  |  |
| 24 | `FS.LANGUAGE.AUDIT.DATE.TIME` | `FsLanguage_AuditDateTime` | String |  |  |
