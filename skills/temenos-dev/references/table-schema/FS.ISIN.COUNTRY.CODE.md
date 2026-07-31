# FS.ISIN.COUNTRY.CODE — Table Schema

> Source: `INSERTS/I_F.FS.ISIN.COUNTRY.CODE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ISIN.COUNTRY.CODE.DESCRIPTION` | `FsIsinCountryCode_Description` |  |  |  |
| 2 | `FS.ISIN.COUNTRY.CODE.FILTER.KEY` | `FsIsinCountryCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ISIN.COUNTRY.CODE.RECORD.ID` | `FsIsinCountryCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ISIN.COUNTRY.CODE.RESERVED10` | `FsIsinCountryCode_Reserved10` | TField |  |  |
| 5 | `FS.ISIN.COUNTRY.CODE.RESERVED9` | `FsIsinCountryCode_Reserved9` | TField |  |  |
| 6 | `FS.ISIN.COUNTRY.CODE.RESERVED8` | `FsIsinCountryCode_Reserved8` | TField |  |  |
| 7 | `FS.ISIN.COUNTRY.CODE.RESERVED7` | `FsIsinCountryCode_Reserved7` | TField |  |  |
| 8 | `FS.ISIN.COUNTRY.CODE.RESERVED6` | `FsIsinCountryCode_Reserved6` | TField |  |  |
| 9 | `FS.ISIN.COUNTRY.CODE.RESERVED5` | `FsIsinCountryCode_Reserved5` | TField |  |  |
| 10 | `FS.ISIN.COUNTRY.CODE.RESERVED4` | `FsIsinCountryCode_Reserved4` | TField |  |  |
| 11 | `FS.ISIN.COUNTRY.CODE.RESERVED3` | `FsIsinCountryCode_Reserved3` | TField |  |  |
| 12 | `FS.ISIN.COUNTRY.CODE.RESERVED2` | `FsIsinCountryCode_Reserved2` | TField |  |  |
| 13 | `FS.ISIN.COUNTRY.CODE.RESERVED1` | `FsIsinCountryCode_Reserved1` | TField |  |  |
| 14 | `FS.ISIN.COUNTRY.CODE.LOCAL.REF` | `FsIsinCountryCode_LocalRef` |  |  |  |
| 15 | `FS.ISIN.COUNTRY.CODE.OVERRIDE` | `FsIsinCountryCode_Override` |  |  |  |
| 16 | `FS.ISIN.COUNTRY.CODE.RECORD.STATUS` | `FsIsinCountryCode_RecordStatus` | String |  |  |
| 17 | `FS.ISIN.COUNTRY.CODE.CURR.NO` | `FsIsinCountryCode_CurrNo` | String |  |  |
| 18 | `FS.ISIN.COUNTRY.CODE.INPUTTER` | `FsIsinCountryCode_Inputter` |  |  |  |
| 19 | `FS.ISIN.COUNTRY.CODE.DATE.TIME` | `FsIsinCountryCode_DateTime` |  |  |  |
| 20 | `FS.ISIN.COUNTRY.CODE.AUTHORISER` | `FsIsinCountryCode_Authoriser` | String |  |  |
| 21 | `FS.ISIN.COUNTRY.CODE.CO.CODE` | `FsIsinCountryCode_CoCode` | String |  |  |
| 22 | `FS.ISIN.COUNTRY.CODE.DEPT.CODE` | `FsIsinCountryCode_DeptCode` | String |  |  |
| 23 | `FS.ISIN.COUNTRY.CODE.AUDITOR.CODE` | `FsIsinCountryCode_AuditorCode` | String |  |  |
| 24 | `FS.ISIN.COUNTRY.CODE.AUDIT.DATE.TIME` | `FsIsinCountryCode_AuditDateTime` | String |  |  |
