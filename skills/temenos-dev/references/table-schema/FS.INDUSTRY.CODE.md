# FS.INDUSTRY.CODE — Table Schema

> Source: `INSERTS/I_F.FS.INDUSTRY.CODE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.INDUSTRY.CODE.DESCRIPTION` | `FsIndustryCode_Description` |  |  |  |
| 2 | `FS.INDUSTRY.CODE.FILTER.KEY` | `FsIndustryCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.INDUSTRY.CODE.RECORD.ID` | `FsIndustryCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.INDUSTRY.CODE.RESERVED10` | `FsIndustryCode_Reserved10` | TField |  |  |
| 5 | `FS.INDUSTRY.CODE.RESERVED9` | `FsIndustryCode_Reserved9` | TField |  |  |
| 6 | `FS.INDUSTRY.CODE.RESERVED8` | `FsIndustryCode_Reserved8` | TField |  |  |
| 7 | `FS.INDUSTRY.CODE.RESERVED7` | `FsIndustryCode_Reserved7` | TField |  |  |
| 8 | `FS.INDUSTRY.CODE.RESERVED6` | `FsIndustryCode_Reserved6` | TField |  |  |
| 9 | `FS.INDUSTRY.CODE.RESERVED5` | `FsIndustryCode_Reserved5` | TField |  |  |
| 10 | `FS.INDUSTRY.CODE.RESERVED4` | `FsIndustryCode_Reserved4` | TField |  |  |
| 11 | `FS.INDUSTRY.CODE.RESERVED3` | `FsIndustryCode_Reserved3` | TField |  |  |
| 12 | `FS.INDUSTRY.CODE.RESERVED2` | `FsIndustryCode_Reserved2` | TField |  |  |
| 13 | `FS.INDUSTRY.CODE.RESERVED1` | `FsIndustryCode_Reserved1` | TField |  |  |
| 14 | `FS.INDUSTRY.CODE.LOCAL.REF` | `FsIndustryCode_LocalRef` |  |  |  |
| 15 | `FS.INDUSTRY.CODE.OVERRIDE` | `FsIndustryCode_Override` |  |  |  |
| 16 | `FS.INDUSTRY.CODE.RECORD.STATUS` | `FsIndustryCode_RecordStatus` | String |  |  |
| 17 | `FS.INDUSTRY.CODE.CURR.NO` | `FsIndustryCode_CurrNo` | String |  |  |
| 18 | `FS.INDUSTRY.CODE.INPUTTER` | `FsIndustryCode_Inputter` |  |  |  |
| 19 | `FS.INDUSTRY.CODE.DATE.TIME` | `FsIndustryCode_DateTime` |  |  |  |
| 20 | `FS.INDUSTRY.CODE.AUTHORISER` | `FsIndustryCode_Authoriser` | String |  |  |
| 21 | `FS.INDUSTRY.CODE.CO.CODE` | `FsIndustryCode_CoCode` | String |  |  |
| 22 | `FS.INDUSTRY.CODE.DEPT.CODE` | `FsIndustryCode_DeptCode` | String |  |  |
| 23 | `FS.INDUSTRY.CODE.AUDITOR.CODE` | `FsIndustryCode_AuditorCode` | String |  |  |
| 24 | `FS.INDUSTRY.CODE.AUDIT.DATE.TIME` | `FsIndustryCode_AuditDateTime` | String |  |  |
