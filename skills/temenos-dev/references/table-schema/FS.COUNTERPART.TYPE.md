# FS.COUNTERPART.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.COUNTERPART.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COUNTERPART.TYPE.DESCRIPTION` | `FsCounterpartType_Description` |  |  |  |
| 2 | `FS.COUNTERPART.TYPE.FILTER.KEY` | `FsCounterpartType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COUNTERPART.TYPE.RECORD.ID` | `FsCounterpartType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COUNTERPART.TYPE.RESERVED10` | `FsCounterpartType_Reserved10` | TField |  |  |
| 5 | `FS.COUNTERPART.TYPE.RESERVED9` | `FsCounterpartType_Reserved9` | TField |  |  |
| 6 | `FS.COUNTERPART.TYPE.RESERVED8` | `FsCounterpartType_Reserved8` | TField |  |  |
| 7 | `FS.COUNTERPART.TYPE.RESERVED7` | `FsCounterpartType_Reserved7` | TField |  |  |
| 8 | `FS.COUNTERPART.TYPE.RESERVED6` | `FsCounterpartType_Reserved6` | TField |  |  |
| 9 | `FS.COUNTERPART.TYPE.RESERVED5` | `FsCounterpartType_Reserved5` | TField |  |  |
| 10 | `FS.COUNTERPART.TYPE.RESERVED4` | `FsCounterpartType_Reserved4` | TField |  |  |
| 11 | `FS.COUNTERPART.TYPE.RESERVED3` | `FsCounterpartType_Reserved3` | TField |  |  |
| 12 | `FS.COUNTERPART.TYPE.RESERVED2` | `FsCounterpartType_Reserved2` | TField |  |  |
| 13 | `FS.COUNTERPART.TYPE.RESERVED1` | `FsCounterpartType_Reserved1` | TField |  |  |
| 14 | `FS.COUNTERPART.TYPE.LOCAL.REF` | `FsCounterpartType_LocalRef` |  |  |  |
| 15 | `FS.COUNTERPART.TYPE.OVERRIDE` | `FsCounterpartType_Override` |  |  |  |
| 16 | `FS.COUNTERPART.TYPE.RECORD.STATUS` | `FsCounterpartType_RecordStatus` | String |  |  |
| 17 | `FS.COUNTERPART.TYPE.CURR.NO` | `FsCounterpartType_CurrNo` | String |  |  |
| 18 | `FS.COUNTERPART.TYPE.INPUTTER` | `FsCounterpartType_Inputter` |  |  |  |
| 19 | `FS.COUNTERPART.TYPE.DATE.TIME` | `FsCounterpartType_DateTime` |  |  |  |
| 20 | `FS.COUNTERPART.TYPE.AUTHORISER` | `FsCounterpartType_Authoriser` | String |  |  |
| 21 | `FS.COUNTERPART.TYPE.CO.CODE` | `FsCounterpartType_CoCode` | String |  |  |
| 22 | `FS.COUNTERPART.TYPE.DEPT.CODE` | `FsCounterpartType_DeptCode` | String |  |  |
| 23 | `FS.COUNTERPART.TYPE.AUDITOR.CODE` | `FsCounterpartType_AuditorCode` | String |  |  |
| 24 | `FS.COUNTERPART.TYPE.AUDIT.DATE.TIME` | `FsCounterpartType_AuditDateTime` | String |  |  |
