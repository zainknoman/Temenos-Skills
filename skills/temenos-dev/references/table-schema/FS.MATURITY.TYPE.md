# FS.MATURITY.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.MATURITY.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.MATURITY.TYPE.DESCRIPTION` | `FsMaturityType_Description` |  |  |  |
| 2 | `FS.MATURITY.TYPE.FILTER.KEY` | `FsMaturityType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.MATURITY.TYPE.RECORD.ID` | `FsMaturityType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.MATURITY.TYPE.RESERVED10` | `FsMaturityType_Reserved10` | TField |  |  |
| 5 | `FS.MATURITY.TYPE.RESERVED9` | `FsMaturityType_Reserved9` | TField |  |  |
| 6 | `FS.MATURITY.TYPE.RESERVED8` | `FsMaturityType_Reserved8` | TField |  |  |
| 7 | `FS.MATURITY.TYPE.RESERVED7` | `FsMaturityType_Reserved7` | TField |  |  |
| 8 | `FS.MATURITY.TYPE.RESERVED6` | `FsMaturityType_Reserved6` | TField |  |  |
| 9 | `FS.MATURITY.TYPE.RESERVED5` | `FsMaturityType_Reserved5` | TField |  |  |
| 10 | `FS.MATURITY.TYPE.RESERVED4` | `FsMaturityType_Reserved4` | TField |  |  |
| 11 | `FS.MATURITY.TYPE.RESERVED3` | `FsMaturityType_Reserved3` | TField |  |  |
| 12 | `FS.MATURITY.TYPE.RESERVED2` | `FsMaturityType_Reserved2` | TField |  |  |
| 13 | `FS.MATURITY.TYPE.RESERVED1` | `FsMaturityType_Reserved1` | TField |  |  |
| 14 | `FS.MATURITY.TYPE.LOCAL.REF` | `FsMaturityType_LocalRef` |  |  |  |
| 15 | `FS.MATURITY.TYPE.OVERRIDE` | `FsMaturityType_Override` |  |  |  |
| 16 | `FS.MATURITY.TYPE.RECORD.STATUS` | `FsMaturityType_RecordStatus` | String |  |  |
| 17 | `FS.MATURITY.TYPE.CURR.NO` | `FsMaturityType_CurrNo` | String |  |  |
| 18 | `FS.MATURITY.TYPE.INPUTTER` | `FsMaturityType_Inputter` |  |  |  |
| 19 | `FS.MATURITY.TYPE.DATE.TIME` | `FsMaturityType_DateTime` |  |  |  |
| 20 | `FS.MATURITY.TYPE.AUTHORISER` | `FsMaturityType_Authoriser` | String |  |  |
| 21 | `FS.MATURITY.TYPE.CO.CODE` | `FsMaturityType_CoCode` | String |  |  |
| 22 | `FS.MATURITY.TYPE.DEPT.CODE` | `FsMaturityType_DeptCode` | String |  |  |
| 23 | `FS.MATURITY.TYPE.AUDITOR.CODE` | `FsMaturityType_AuditorCode` | String |  |  |
| 24 | `FS.MATURITY.TYPE.AUDIT.DATE.TIME` | `FsMaturityType_AuditDateTime` | String |  |  |
