# FS.COUNTRY.CODE — Table Schema

> Source: `INSERTS/I_F.FS.COUNTRY.CODE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COUNTRY.CODE.DESCRIPTION` | `FsCountryCode_Description` |  |  |  |
| 2 | `FS.COUNTRY.CODE.FILTER.KEY` | `FsCountryCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COUNTRY.CODE.RECORD.ID` | `FsCountryCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COUNTRY.CODE.RESERVED10` | `FsCountryCode_Reserved10` | TField |  |  |
| 5 | `FS.COUNTRY.CODE.RESERVED9` | `FsCountryCode_Reserved9` | TField |  |  |
| 6 | `FS.COUNTRY.CODE.RESERVED8` | `FsCountryCode_Reserved8` | TField |  |  |
| 7 | `FS.COUNTRY.CODE.RESERVED7` | `FsCountryCode_Reserved7` | TField |  |  |
| 8 | `FS.COUNTRY.CODE.RESERVED6` | `FsCountryCode_Reserved6` | TField |  |  |
| 9 | `FS.COUNTRY.CODE.RESERVED5` | `FsCountryCode_Reserved5` | TField |  |  |
| 10 | `FS.COUNTRY.CODE.RESERVED4` | `FsCountryCode_Reserved4` | TField |  |  |
| 11 | `FS.COUNTRY.CODE.RESERVED3` | `FsCountryCode_Reserved3` | TField |  |  |
| 12 | `FS.COUNTRY.CODE.RESERVED2` | `FsCountryCode_Reserved2` | TField |  |  |
| 13 | `FS.COUNTRY.CODE.RESERVED1` | `FsCountryCode_Reserved1` | TField |  |  |
| 14 | `FS.COUNTRY.CODE.LOCAL.REF` | `FsCountryCode_LocalRef` |  |  |  |
| 15 | `FS.COUNTRY.CODE.OVERRIDE` | `FsCountryCode_Override` |  |  |  |
| 16 | `FS.COUNTRY.CODE.RECORD.STATUS` | `FsCountryCode_RecordStatus` | String |  |  |
| 17 | `FS.COUNTRY.CODE.CURR.NO` | `FsCountryCode_CurrNo` | String |  |  |
| 18 | `FS.COUNTRY.CODE.INPUTTER` | `FsCountryCode_Inputter` |  |  |  |
| 19 | `FS.COUNTRY.CODE.DATE.TIME` | `FsCountryCode_DateTime` |  |  |  |
| 20 | `FS.COUNTRY.CODE.AUTHORISER` | `FsCountryCode_Authoriser` | String |  |  |
| 21 | `FS.COUNTRY.CODE.CO.CODE` | `FsCountryCode_CoCode` | String |  |  |
| 22 | `FS.COUNTRY.CODE.DEPT.CODE` | `FsCountryCode_DeptCode` | String |  |  |
| 23 | `FS.COUNTRY.CODE.AUDITOR.CODE` | `FsCountryCode_AuditorCode` | String |  |  |
| 24 | `FS.COUNTRY.CODE.AUDIT.DATE.TIME` | `FsCountryCode_AuditDateTime` | String |  |  |
