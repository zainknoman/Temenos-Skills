# FS.TRANSACTION.POSTING.CODES — Table Schema

> Source: `INSERTS/I_F.FS.TRANSACTION.POSTING.CODES` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.TRANSACTION.POSTING.CODES.DESCRIPTION` | `FsTransactionPostingCodes_Description` |  |  |  |
| 2 | `FS.TRANSACTION.POSTING.CODES.FILTER.KEY` | `FsTransactionPostingCodes_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.TRANSACTION.POSTING.CODES.RECORD.ID` | `FsTransactionPostingCodes_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.TRANSACTION.POSTING.CODES.RESERVED10` | `FsTransactionPostingCodes_Reserved10` | TField |  |  |
| 5 | `FS.TRANSACTION.POSTING.CODES.RESERVED9` | `FsTransactionPostingCodes_Reserved9` | TField |  |  |
| 6 | `FS.TRANSACTION.POSTING.CODES.RESERVED8` | `FsTransactionPostingCodes_Reserved8` | TField |  |  |
| 7 | `FS.TRANSACTION.POSTING.CODES.RESERVED7` | `FsTransactionPostingCodes_Reserved7` | TField |  |  |
| 8 | `FS.TRANSACTION.POSTING.CODES.RESERVED6` | `FsTransactionPostingCodes_Reserved6` | TField |  |  |
| 9 | `FS.TRANSACTION.POSTING.CODES.RESERVED5` | `FsTransactionPostingCodes_Reserved5` | TField |  |  |
| 10 | `FS.TRANSACTION.POSTING.CODES.RESERVED4` | `FsTransactionPostingCodes_Reserved4` | TField |  |  |
| 11 | `FS.TRANSACTION.POSTING.CODES.RESERVED3` | `FsTransactionPostingCodes_Reserved3` | TField |  |  |
| 12 | `FS.TRANSACTION.POSTING.CODES.RESERVED2` | `FsTransactionPostingCodes_Reserved2` | TField |  |  |
| 13 | `FS.TRANSACTION.POSTING.CODES.RESERVED1` | `FsTransactionPostingCodes_Reserved1` | TField |  |  |
| 14 | `FS.TRANSACTION.POSTING.CODES.LOCAL.REF` | `FsTransactionPostingCodes_LocalRef` |  |  |  |
| 15 | `FS.TRANSACTION.POSTING.CODES.OVERRIDE` | `FsTransactionPostingCodes_Override` |  |  |  |
| 16 | `FS.TRANSACTION.POSTING.CODES.RECORD.STATUS` | `FsTransactionPostingCodes_RecordStatus` | String |  |  |
| 17 | `FS.TRANSACTION.POSTING.CODES.CURR.NO` | `FsTransactionPostingCodes_CurrNo` | String |  |  |
| 18 | `FS.TRANSACTION.POSTING.CODES.INPUTTER` | `FsTransactionPostingCodes_Inputter` |  |  |  |
| 19 | `FS.TRANSACTION.POSTING.CODES.DATE.TIME` | `FsTransactionPostingCodes_DateTime` |  |  |  |
| 20 | `FS.TRANSACTION.POSTING.CODES.AUTHORISER` | `FsTransactionPostingCodes_Authoriser` | String |  |  |
| 21 | `FS.TRANSACTION.POSTING.CODES.CO.CODE` | `FsTransactionPostingCodes_CoCode` | String |  |  |
| 22 | `FS.TRANSACTION.POSTING.CODES.DEPT.CODE` | `FsTransactionPostingCodes_DeptCode` | String |  |  |
| 23 | `FS.TRANSACTION.POSTING.CODES.AUDITOR.CODE` | `FsTransactionPostingCodes_AuditorCode` | String |  |  |
| 24 | `FS.TRANSACTION.POSTING.CODES.AUDIT.DATE.TIME` | `FsTransactionPostingCodes_AuditDateTime` | String |  |  |
