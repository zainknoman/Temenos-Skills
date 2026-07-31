# FS.NAV.POSTING.CODE — Table Schema

> Source: `INSERTS/I_F.FS.NAV.POSTING.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.NAV.POSTING.CODE.DESCRIPTION` | `FsNavPostingCode_Description` |  |  |  |
| 2 | `FS.NAV.POSTING.CODE.FILTER.KEY` | `FsNavPostingCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.NAV.POSTING.CODE.RECORD.ID` | `FsNavPostingCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.NAV.POSTING.CODE.RESERVED10` | `FsNavPostingCode_Reserved10` | TField |  |  |
| 5 | `FS.NAV.POSTING.CODE.RESERVED9` | `FsNavPostingCode_Reserved9` | TField |  |  |
| 6 | `FS.NAV.POSTING.CODE.RESERVED8` | `FsNavPostingCode_Reserved8` | TField |  |  |
| 7 | `FS.NAV.POSTING.CODE.RESERVED7` | `FsNavPostingCode_Reserved7` | TField |  |  |
| 8 | `FS.NAV.POSTING.CODE.RESERVED6` | `FsNavPostingCode_Reserved6` | TField |  |  |
| 9 | `FS.NAV.POSTING.CODE.RESERVED5` | `FsNavPostingCode_Reserved5` | TField |  |  |
| 10 | `FS.NAV.POSTING.CODE.RESERVED4` | `FsNavPostingCode_Reserved4` | TField |  |  |
| 11 | `FS.NAV.POSTING.CODE.RESERVED3` | `FsNavPostingCode_Reserved3` | TField |  |  |
| 12 | `FS.NAV.POSTING.CODE.RESERVED2` | `FsNavPostingCode_Reserved2` | TField |  |  |
| 13 | `FS.NAV.POSTING.CODE.RESERVED1` | `FsNavPostingCode_Reserved1` | TField |  |  |
| 14 | `FS.NAV.POSTING.CODE.LOCAL.REF` | `FsNavPostingCode_LocalRef` |  |  |  |
| 15 | `FS.NAV.POSTING.CODE.OVERRIDE` | `FsNavPostingCode_Override` |  |  |  |
| 16 | `FS.NAV.POSTING.CODE.RECORD.STATUS` | `FsNavPostingCode_RecordStatus` | String |  |  |
| 17 | `FS.NAV.POSTING.CODE.CURR.NO` | `FsNavPostingCode_CurrNo` | String |  |  |
| 18 | `FS.NAV.POSTING.CODE.INPUTTER` | `FsNavPostingCode_Inputter` |  |  |  |
| 19 | `FS.NAV.POSTING.CODE.DATE.TIME` | `FsNavPostingCode_DateTime` |  |  |  |
| 20 | `FS.NAV.POSTING.CODE.AUTHORISER` | `FsNavPostingCode_Authoriser` | String |  |  |
| 21 | `FS.NAV.POSTING.CODE.CO.CODE` | `FsNavPostingCode_CoCode` | String |  |  |
| 22 | `FS.NAV.POSTING.CODE.DEPT.CODE` | `FsNavPostingCode_DeptCode` | String |  |  |
| 23 | `FS.NAV.POSTING.CODE.AUDITOR.CODE` | `FsNavPostingCode_AuditorCode` | String |  |  |
| 24 | `FS.NAV.POSTING.CODE.AUDIT.DATE.TIME` | `FsNavPostingCode_AuditDateTime` | String |  |  |
