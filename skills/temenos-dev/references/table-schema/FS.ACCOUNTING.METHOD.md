# FS.ACCOUNTING.METHOD — Table Schema

> Source: `INSERTS/I_F.FS.ACCOUNTING.METHOD` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ACCOUNTING.METHOD.DESCRIPTION` | `FsAccountingMethod_Description` |  |  |  |
| 2 | `FS.ACCOUNTING.METHOD.FILTER.KEY` | `FsAccountingMethod_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ACCOUNTING.METHOD.RECORD.ID` | `FsAccountingMethod_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ACCOUNTING.METHOD.RESERVED10` | `FsAccountingMethod_Reserved10` | TField |  |  |
| 5 | `FS.ACCOUNTING.METHOD.RESERVED9` | `FsAccountingMethod_Reserved9` | TField |  |  |
| 6 | `FS.ACCOUNTING.METHOD.RESERVED8` | `FsAccountingMethod_Reserved8` | TField |  |  |
| 7 | `FS.ACCOUNTING.METHOD.RESERVED7` | `FsAccountingMethod_Reserved7` | TField |  |  |
| 8 | `FS.ACCOUNTING.METHOD.RESERVED6` | `FsAccountingMethod_Reserved6` | TField |  |  |
| 9 | `FS.ACCOUNTING.METHOD.RESERVED5` | `FsAccountingMethod_Reserved5` | TField |  |  |
| 10 | `FS.ACCOUNTING.METHOD.RESERVED4` | `FsAccountingMethod_Reserved4` | TField |  |  |
| 11 | `FS.ACCOUNTING.METHOD.RESERVED3` | `FsAccountingMethod_Reserved3` | TField |  |  |
| 12 | `FS.ACCOUNTING.METHOD.RESERVED2` | `FsAccountingMethod_Reserved2` | TField |  |  |
| 13 | `FS.ACCOUNTING.METHOD.RESERVED1` | `FsAccountingMethod_Reserved1` | TField |  |  |
| 14 | `FS.ACCOUNTING.METHOD.LOCAL.REF` | `FsAccountingMethod_LocalRef` |  |  |  |
| 15 | `FS.ACCOUNTING.METHOD.OVERRIDE` | `FsAccountingMethod_Override` |  |  |  |
| 16 | `FS.ACCOUNTING.METHOD.RECORD.STATUS` | `FsAccountingMethod_RecordStatus` | String |  |  |
| 17 | `FS.ACCOUNTING.METHOD.CURR.NO` | `FsAccountingMethod_CurrNo` | String |  |  |
| 18 | `FS.ACCOUNTING.METHOD.INPUTTER` | `FsAccountingMethod_Inputter` |  |  |  |
| 19 | `FS.ACCOUNTING.METHOD.DATE.TIME` | `FsAccountingMethod_DateTime` |  |  |  |
| 20 | `FS.ACCOUNTING.METHOD.AUTHORISER` | `FsAccountingMethod_Authoriser` | String |  |  |
| 21 | `FS.ACCOUNTING.METHOD.CO.CODE` | `FsAccountingMethod_CoCode` | String |  |  |
| 22 | `FS.ACCOUNTING.METHOD.DEPT.CODE` | `FsAccountingMethod_DeptCode` | String |  |  |
| 23 | `FS.ACCOUNTING.METHOD.AUDITOR.CODE` | `FsAccountingMethod_AuditorCode` | String |  |  |
| 24 | `FS.ACCOUNTING.METHOD.AUDIT.DATE.TIME` | `FsAccountingMethod_AuditDateTime` | String |  |  |
