# FS.TRANSACTION.STATUS — Table Schema

> Source: `INSERTS/I_F.FS.TRANSACTION.STATUS` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.TRANSACTION.STATUS.DESCRIPTION` | `FsTransactionStatus_Description` |  |  |  |
| 2 | `FS.TRANSACTION.STATUS.FILTER.KEY` | `FsTransactionStatus_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.TRANSACTION.STATUS.RECORD.ID` | `FsTransactionStatus_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.TRANSACTION.STATUS.RESERVED10` | `FsTransactionStatus_Reserved10` | TField |  |  |
| 5 | `FS.TRANSACTION.STATUS.RESERVED9` | `FsTransactionStatus_Reserved9` | TField |  |  |
| 6 | `FS.TRANSACTION.STATUS.RESERVED8` | `FsTransactionStatus_Reserved8` | TField |  |  |
| 7 | `FS.TRANSACTION.STATUS.RESERVED7` | `FsTransactionStatus_Reserved7` | TField |  |  |
| 8 | `FS.TRANSACTION.STATUS.RESERVED6` | `FsTransactionStatus_Reserved6` | TField |  |  |
| 9 | `FS.TRANSACTION.STATUS.RESERVED5` | `FsTransactionStatus_Reserved5` | TField |  |  |
| 10 | `FS.TRANSACTION.STATUS.RESERVED4` | `FsTransactionStatus_Reserved4` | TField |  |  |
| 11 | `FS.TRANSACTION.STATUS.RESERVED3` | `FsTransactionStatus_Reserved3` | TField |  |  |
| 12 | `FS.TRANSACTION.STATUS.RESERVED2` | `FsTransactionStatus_Reserved2` | TField |  |  |
| 13 | `FS.TRANSACTION.STATUS.RESERVED1` | `FsTransactionStatus_Reserved1` | TField |  |  |
| 14 | `FS.TRANSACTION.STATUS.LOCAL.REF` | `FsTransactionStatus_LocalRef` |  |  |  |
| 15 | `FS.TRANSACTION.STATUS.OVERRIDE` | `FsTransactionStatus_Override` |  |  |  |
| 16 | `FS.TRANSACTION.STATUS.RECORD.STATUS` | `FsTransactionStatus_RecordStatus` | String |  |  |
| 17 | `FS.TRANSACTION.STATUS.CURR.NO` | `FsTransactionStatus_CurrNo` | String |  |  |
| 18 | `FS.TRANSACTION.STATUS.INPUTTER` | `FsTransactionStatus_Inputter` |  |  |  |
| 19 | `FS.TRANSACTION.STATUS.DATE.TIME` | `FsTransactionStatus_DateTime` |  |  |  |
| 20 | `FS.TRANSACTION.STATUS.AUTHORISER` | `FsTransactionStatus_Authoriser` | String |  |  |
| 21 | `FS.TRANSACTION.STATUS.CO.CODE` | `FsTransactionStatus_CoCode` | String |  |  |
| 22 | `FS.TRANSACTION.STATUS.DEPT.CODE` | `FsTransactionStatus_DeptCode` | String |  |  |
| 23 | `FS.TRANSACTION.STATUS.AUDITOR.CODE` | `FsTransactionStatus_AuditorCode` | String |  |  |
| 24 | `FS.TRANSACTION.STATUS.AUDIT.DATE.TIME` | `FsTransactionStatus_AuditDateTime` | String |  |  |
