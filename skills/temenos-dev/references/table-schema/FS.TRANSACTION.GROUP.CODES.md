# FS.TRANSACTION.GROUP.CODES — Table Schema

> Source: `INSERTS/I_F.FS.TRANSACTION.GROUP.CODES` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.TRANSACTION.GROUP.CODES.DESCRIPTION` | `FsTransactionGroupCodes_Description` |  |  |  |
| 2 | `FS.TRANSACTION.GROUP.CODES.FILTER.KEY` | `FsTransactionGroupCodes_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.TRANSACTION.GROUP.CODES.RECORD.ID` | `FsTransactionGroupCodes_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.TRANSACTION.GROUP.CODES.RESERVED10` | `FsTransactionGroupCodes_Reserved10` | TField |  |  |
| 5 | `FS.TRANSACTION.GROUP.CODES.RESERVED9` | `FsTransactionGroupCodes_Reserved9` | TField |  |  |
| 6 | `FS.TRANSACTION.GROUP.CODES.RESERVED8` | `FsTransactionGroupCodes_Reserved8` | TField |  |  |
| 7 | `FS.TRANSACTION.GROUP.CODES.RESERVED7` | `FsTransactionGroupCodes_Reserved7` | TField |  |  |
| 8 | `FS.TRANSACTION.GROUP.CODES.RESERVED6` | `FsTransactionGroupCodes_Reserved6` | TField |  |  |
| 9 | `FS.TRANSACTION.GROUP.CODES.RESERVED5` | `FsTransactionGroupCodes_Reserved5` | TField |  |  |
| 10 | `FS.TRANSACTION.GROUP.CODES.RESERVED4` | `FsTransactionGroupCodes_Reserved4` | TField |  |  |
| 11 | `FS.TRANSACTION.GROUP.CODES.RESERVED3` | `FsTransactionGroupCodes_Reserved3` | TField |  |  |
| 12 | `FS.TRANSACTION.GROUP.CODES.RESERVED2` | `FsTransactionGroupCodes_Reserved2` | TField |  |  |
| 13 | `FS.TRANSACTION.GROUP.CODES.RESERVED1` | `FsTransactionGroupCodes_Reserved1` | TField |  |  |
| 14 | `FS.TRANSACTION.GROUP.CODES.LOCAL.REF` | `FsTransactionGroupCodes_LocalRef` |  |  |  |
| 15 | `FS.TRANSACTION.GROUP.CODES.OVERRIDE` | `FsTransactionGroupCodes_Override` |  |  |  |
| 16 | `FS.TRANSACTION.GROUP.CODES.RECORD.STATUS` | `FsTransactionGroupCodes_RecordStatus` | String |  |  |
| 17 | `FS.TRANSACTION.GROUP.CODES.CURR.NO` | `FsTransactionGroupCodes_CurrNo` | String |  |  |
| 18 | `FS.TRANSACTION.GROUP.CODES.INPUTTER` | `FsTransactionGroupCodes_Inputter` |  |  |  |
| 19 | `FS.TRANSACTION.GROUP.CODES.DATE.TIME` | `FsTransactionGroupCodes_DateTime` |  |  |  |
| 20 | `FS.TRANSACTION.GROUP.CODES.AUTHORISER` | `FsTransactionGroupCodes_Authoriser` | String |  |  |
| 21 | `FS.TRANSACTION.GROUP.CODES.CO.CODE` | `FsTransactionGroupCodes_CoCode` | String |  |  |
| 22 | `FS.TRANSACTION.GROUP.CODES.DEPT.CODE` | `FsTransactionGroupCodes_DeptCode` | String |  |  |
| 23 | `FS.TRANSACTION.GROUP.CODES.AUDITOR.CODE` | `FsTransactionGroupCodes_AuditorCode` | String |  |  |
| 24 | `FS.TRANSACTION.GROUP.CODES.AUDIT.DATE.TIME` | `FsTransactionGroupCodes_AuditDateTime` | String |  |  |
