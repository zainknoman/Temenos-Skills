# FS.ERROR.MESSAGE — Table Schema

> Source: `INSERTS/I_F.FS.ERROR.MESSAGE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ERROR.MESSAGE.DESCRIPTION` | `FsErrorMessage_Description` |  |  |  |
| 2 | `FS.ERROR.MESSAGE.FILTER.KEY` | `FsErrorMessage_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ERROR.MESSAGE.RECORD.ID` | `FsErrorMessage_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ERROR.MESSAGE.RESERVED10` | `FsErrorMessage_Reserved10` | TField |  |  |
| 5 | `FS.ERROR.MESSAGE.RESERVED9` | `FsErrorMessage_Reserved9` | TField |  |  |
| 6 | `FS.ERROR.MESSAGE.RESERVED8` | `FsErrorMessage_Reserved8` | TField |  |  |
| 7 | `FS.ERROR.MESSAGE.RESERVED7` | `FsErrorMessage_Reserved7` | TField |  |  |
| 8 | `FS.ERROR.MESSAGE.RESERVED6` | `FsErrorMessage_Reserved6` | TField |  |  |
| 9 | `FS.ERROR.MESSAGE.RESERVED5` | `FsErrorMessage_Reserved5` | TField |  |  |
| 10 | `FS.ERROR.MESSAGE.RESERVED4` | `FsErrorMessage_Reserved4` | TField |  |  |
| 11 | `FS.ERROR.MESSAGE.RESERVED3` | `FsErrorMessage_Reserved3` | TField |  |  |
| 12 | `FS.ERROR.MESSAGE.RESERVED2` | `FsErrorMessage_Reserved2` | TField |  |  |
| 13 | `FS.ERROR.MESSAGE.RESERVED1` | `FsErrorMessage_Reserved1` | TField |  |  |
| 14 | `FS.ERROR.MESSAGE.LOCAL.REF` | `FsErrorMessage_LocalRef` |  |  |  |
| 15 | `FS.ERROR.MESSAGE.OVERRIDE` | `FsErrorMessage_Override` |  |  |  |
| 16 | `FS.ERROR.MESSAGE.RECORD.STATUS` | `FsErrorMessage_RecordStatus` | String |  |  |
| 17 | `FS.ERROR.MESSAGE.CURR.NO` | `FsErrorMessage_CurrNo` | String |  |  |
| 18 | `FS.ERROR.MESSAGE.INPUTTER` | `FsErrorMessage_Inputter` |  |  |  |
| 19 | `FS.ERROR.MESSAGE.DATE.TIME` | `FsErrorMessage_DateTime` |  |  |  |
| 20 | `FS.ERROR.MESSAGE.AUTHORISER` | `FsErrorMessage_Authoriser` | String |  |  |
| 21 | `FS.ERROR.MESSAGE.CO.CODE` | `FsErrorMessage_CoCode` | String |  |  |
| 22 | `FS.ERROR.MESSAGE.DEPT.CODE` | `FsErrorMessage_DeptCode` | String |  |  |
| 23 | `FS.ERROR.MESSAGE.AUDITOR.CODE` | `FsErrorMessage_AuditorCode` | String |  |  |
| 24 | `FS.ERROR.MESSAGE.AUDIT.DATE.TIME` | `FsErrorMessage_AuditDateTime` | String |  |  |
