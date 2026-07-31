# FS.THIRDPARTY.CODE — Table Schema

> Source: `INSERTS/I_F.FS.THIRDPARTY.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.THIRDPARTY.CODE.DESCRIPTION` | `FsThirdpartyCode_Description` |  |  |  |
| 2 | `FS.THIRDPARTY.CODE.FILTER.KEY` | `FsThirdpartyCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.THIRDPARTY.CODE.RECORD.ID` | `FsThirdpartyCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.THIRDPARTY.CODE.RESERVED10` | `FsThirdpartyCode_Reserved10` | TField |  |  |
| 5 | `FS.THIRDPARTY.CODE.RESERVED9` | `FsThirdpartyCode_Reserved9` | TField |  |  |
| 6 | `FS.THIRDPARTY.CODE.RESERVED8` | `FsThirdpartyCode_Reserved8` | TField |  |  |
| 7 | `FS.THIRDPARTY.CODE.RESERVED7` | `FsThirdpartyCode_Reserved7` | TField |  |  |
| 8 | `FS.THIRDPARTY.CODE.RESERVED6` | `FsThirdpartyCode_Reserved6` | TField |  |  |
| 9 | `FS.THIRDPARTY.CODE.RESERVED5` | `FsThirdpartyCode_Reserved5` | TField |  |  |
| 10 | `FS.THIRDPARTY.CODE.RESERVED4` | `FsThirdpartyCode_Reserved4` | TField |  |  |
| 11 | `FS.THIRDPARTY.CODE.RESERVED3` | `FsThirdpartyCode_Reserved3` | TField |  |  |
| 12 | `FS.THIRDPARTY.CODE.RESERVED2` | `FsThirdpartyCode_Reserved2` | TField |  |  |
| 13 | `FS.THIRDPARTY.CODE.RESERVED1` | `FsThirdpartyCode_Reserved1` | TField |  |  |
| 14 | `FS.THIRDPARTY.CODE.LOCAL.REF` | `FsThirdpartyCode_LocalRef` |  |  |  |
| 15 | `FS.THIRDPARTY.CODE.OVERRIDE` | `FsThirdpartyCode_Override` |  |  |  |
| 16 | `FS.THIRDPARTY.CODE.RECORD.STATUS` | `FsThirdpartyCode_RecordStatus` | String |  |  |
| 17 | `FS.THIRDPARTY.CODE.CURR.NO` | `FsThirdpartyCode_CurrNo` | String |  |  |
| 18 | `FS.THIRDPARTY.CODE.INPUTTER` | `FsThirdpartyCode_Inputter` |  |  |  |
| 19 | `FS.THIRDPARTY.CODE.DATE.TIME` | `FsThirdpartyCode_DateTime` |  |  |  |
| 20 | `FS.THIRDPARTY.CODE.AUTHORISER` | `FsThirdpartyCode_Authoriser` | String |  |  |
| 21 | `FS.THIRDPARTY.CODE.CO.CODE` | `FsThirdpartyCode_CoCode` | String |  |  |
| 22 | `FS.THIRDPARTY.CODE.DEPT.CODE` | `FsThirdpartyCode_DeptCode` | String |  |  |
| 23 | `FS.THIRDPARTY.CODE.AUDITOR.CODE` | `FsThirdpartyCode_AuditorCode` | String |  |  |
| 24 | `FS.THIRDPARTY.CODE.AUDIT.DATE.TIME` | `FsThirdpartyCode_AuditDateTime` | String |  |  |
