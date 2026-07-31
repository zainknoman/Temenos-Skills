# FS.INTEREST.RATE.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.INTEREST.RATE.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.INTEREST.RATE.TYPE.DESCRIPTION` | `FsInterestRateType_Description` |  |  |  |
| 2 | `FS.INTEREST.RATE.TYPE.FILTER.KEY` | `FsInterestRateType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.INTEREST.RATE.TYPE.RECORD.ID` | `FsInterestRateType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.INTEREST.RATE.TYPE.RESERVED10` | `FsInterestRateType_Reserved10` | TField |  |  |
| 5 | `FS.INTEREST.RATE.TYPE.RESERVED9` | `FsInterestRateType_Reserved9` | TField |  |  |
| 6 | `FS.INTEREST.RATE.TYPE.RESERVED8` | `FsInterestRateType_Reserved8` | TField |  |  |
| 7 | `FS.INTEREST.RATE.TYPE.RESERVED7` | `FsInterestRateType_Reserved7` | TField |  |  |
| 8 | `FS.INTEREST.RATE.TYPE.RESERVED6` | `FsInterestRateType_Reserved6` | TField |  |  |
| 9 | `FS.INTEREST.RATE.TYPE.RESERVED5` | `FsInterestRateType_Reserved5` | TField |  |  |
| 10 | `FS.INTEREST.RATE.TYPE.RESERVED4` | `FsInterestRateType_Reserved4` | TField |  |  |
| 11 | `FS.INTEREST.RATE.TYPE.RESERVED3` | `FsInterestRateType_Reserved3` | TField |  |  |
| 12 | `FS.INTEREST.RATE.TYPE.RESERVED2` | `FsInterestRateType_Reserved2` | TField |  |  |
| 13 | `FS.INTEREST.RATE.TYPE.RESERVED1` | `FsInterestRateType_Reserved1` | TField |  |  |
| 14 | `FS.INTEREST.RATE.TYPE.LOCAL.REF` | `FsInterestRateType_LocalRef` |  |  |  |
| 15 | `FS.INTEREST.RATE.TYPE.OVERRIDE` | `FsInterestRateType_Override` |  |  |  |
| 16 | `FS.INTEREST.RATE.TYPE.RECORD.STATUS` | `FsInterestRateType_RecordStatus` | String |  |  |
| 17 | `FS.INTEREST.RATE.TYPE.CURR.NO` | `FsInterestRateType_CurrNo` | String |  |  |
| 18 | `FS.INTEREST.RATE.TYPE.INPUTTER` | `FsInterestRateType_Inputter` |  |  |  |
| 19 | `FS.INTEREST.RATE.TYPE.DATE.TIME` | `FsInterestRateType_DateTime` |  |  |  |
| 20 | `FS.INTEREST.RATE.TYPE.AUTHORISER` | `FsInterestRateType_Authoriser` | String |  |  |
| 21 | `FS.INTEREST.RATE.TYPE.CO.CODE` | `FsInterestRateType_CoCode` | String |  |  |
| 22 | `FS.INTEREST.RATE.TYPE.DEPT.CODE` | `FsInterestRateType_DeptCode` | String |  |  |
| 23 | `FS.INTEREST.RATE.TYPE.AUDITOR.CODE` | `FsInterestRateType_AuditorCode` | String |  |  |
| 24 | `FS.INTEREST.RATE.TYPE.AUDIT.DATE.TIME` | `FsInterestRateType_AuditDateTime` | String |  |  |
