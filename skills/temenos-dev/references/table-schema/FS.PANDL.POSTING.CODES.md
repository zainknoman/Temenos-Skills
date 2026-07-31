# FS.PANDL.POSTING.CODES — Table Schema

> Source: `INSERTS/I_F.FS.PANDL.POSTING.CODES` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.PANDL.POSTING.CODES.DESCRIPTION` | `FsPandlPostingCodes_Description` |  |  |  |
| 2 | `FS.PANDL.POSTING.CODES.FILTER.KEY` | `FsPandlPostingCodes_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.PANDL.POSTING.CODES.RECORD.ID` | `FsPandlPostingCodes_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.PANDL.POSTING.CODES.RESERVED10` | `FsPandlPostingCodes_Reserved10` | TField |  |  |
| 5 | `FS.PANDL.POSTING.CODES.RESERVED9` | `FsPandlPostingCodes_Reserved9` | TField |  |  |
| 6 | `FS.PANDL.POSTING.CODES.RESERVED8` | `FsPandlPostingCodes_Reserved8` | TField |  |  |
| 7 | `FS.PANDL.POSTING.CODES.RESERVED7` | `FsPandlPostingCodes_Reserved7` | TField |  |  |
| 8 | `FS.PANDL.POSTING.CODES.RESERVED6` | `FsPandlPostingCodes_Reserved6` | TField |  |  |
| 9 | `FS.PANDL.POSTING.CODES.RESERVED5` | `FsPandlPostingCodes_Reserved5` | TField |  |  |
| 10 | `FS.PANDL.POSTING.CODES.RESERVED4` | `FsPandlPostingCodes_Reserved4` | TField |  |  |
| 11 | `FS.PANDL.POSTING.CODES.RESERVED3` | `FsPandlPostingCodes_Reserved3` | TField |  |  |
| 12 | `FS.PANDL.POSTING.CODES.RESERVED2` | `FsPandlPostingCodes_Reserved2` | TField |  |  |
| 13 | `FS.PANDL.POSTING.CODES.RESERVED1` | `FsPandlPostingCodes_Reserved1` | TField |  |  |
| 14 | `FS.PANDL.POSTING.CODES.LOCAL.REF` | `FsPandlPostingCodes_LocalRef` |  |  |  |
| 15 | `FS.PANDL.POSTING.CODES.OVERRIDE` | `FsPandlPostingCodes_Override` |  |  |  |
| 16 | `FS.PANDL.POSTING.CODES.RECORD.STATUS` | `FsPandlPostingCodes_RecordStatus` | String |  |  |
| 17 | `FS.PANDL.POSTING.CODES.CURR.NO` | `FsPandlPostingCodes_CurrNo` | String |  |  |
| 18 | `FS.PANDL.POSTING.CODES.INPUTTER` | `FsPandlPostingCodes_Inputter` |  |  |  |
| 19 | `FS.PANDL.POSTING.CODES.DATE.TIME` | `FsPandlPostingCodes_DateTime` |  |  |  |
| 20 | `FS.PANDL.POSTING.CODES.AUTHORISER` | `FsPandlPostingCodes_Authoriser` | String |  |  |
| 21 | `FS.PANDL.POSTING.CODES.CO.CODE` | `FsPandlPostingCodes_CoCode` | String |  |  |
| 22 | `FS.PANDL.POSTING.CODES.DEPT.CODE` | `FsPandlPostingCodes_DeptCode` | String |  |  |
| 23 | `FS.PANDL.POSTING.CODES.AUDITOR.CODE` | `FsPandlPostingCodes_AuditorCode` | String |  |  |
| 24 | `FS.PANDL.POSTING.CODES.AUDIT.DATE.TIME` | `FsPandlPostingCodes_AuditDateTime` | String |  |  |
