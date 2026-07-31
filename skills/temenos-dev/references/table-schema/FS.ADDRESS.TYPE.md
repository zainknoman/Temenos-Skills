# FS.ADDRESS.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.ADDRESS.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ADDRESS.TYPE.DESCRIPTION` | `FsAddressType_Description` |  |  |  |
| 2 | `FS.ADDRESS.TYPE.FILTER.KEY` | `FsAddressType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ADDRESS.TYPE.RECORD.ID` | `FsAddressType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ADDRESS.TYPE.RESERVED10` | `FsAddressType_Reserved10` | TField |  |  |
| 5 | `FS.ADDRESS.TYPE.RESERVED9` | `FsAddressType_Reserved9` | TField |  |  |
| 6 | `FS.ADDRESS.TYPE.RESERVED8` | `FsAddressType_Reserved8` | TField |  |  |
| 7 | `FS.ADDRESS.TYPE.RESERVED7` | `FsAddressType_Reserved7` | TField |  |  |
| 8 | `FS.ADDRESS.TYPE.RESERVED6` | `FsAddressType_Reserved6` | TField |  |  |
| 9 | `FS.ADDRESS.TYPE.RESERVED5` | `FsAddressType_Reserved5` | TField |  |  |
| 10 | `FS.ADDRESS.TYPE.RESERVED4` | `FsAddressType_Reserved4` | TField |  |  |
| 11 | `FS.ADDRESS.TYPE.RESERVED3` | `FsAddressType_Reserved3` | TField |  |  |
| 12 | `FS.ADDRESS.TYPE.RESERVED2` | `FsAddressType_Reserved2` | TField |  |  |
| 13 | `FS.ADDRESS.TYPE.RESERVED1` | `FsAddressType_Reserved1` | TField |  |  |
| 14 | `FS.ADDRESS.TYPE.LOCAL.REF` | `FsAddressType_LocalRef` |  |  |  |
| 15 | `FS.ADDRESS.TYPE.OVERRIDE` | `FsAddressType_Override` |  |  |  |
| 16 | `FS.ADDRESS.TYPE.RECORD.STATUS` | `FsAddressType_RecordStatus` | String |  |  |
| 17 | `FS.ADDRESS.TYPE.CURR.NO` | `FsAddressType_CurrNo` | String |  |  |
| 18 | `FS.ADDRESS.TYPE.INPUTTER` | `FsAddressType_Inputter` |  |  |  |
| 19 | `FS.ADDRESS.TYPE.DATE.TIME` | `FsAddressType_DateTime` |  |  |  |
| 20 | `FS.ADDRESS.TYPE.AUTHORISER` | `FsAddressType_Authoriser` | String |  |  |
| 21 | `FS.ADDRESS.TYPE.CO.CODE` | `FsAddressType_CoCode` | String |  |  |
| 22 | `FS.ADDRESS.TYPE.DEPT.CODE` | `FsAddressType_DeptCode` | String |  |  |
| 23 | `FS.ADDRESS.TYPE.AUDITOR.CODE` | `FsAddressType_AuditorCode` | String |  |  |
| 24 | `FS.ADDRESS.TYPE.AUDIT.DATE.TIME` | `FsAddressType_AuditDateTime` | String |  |  |
