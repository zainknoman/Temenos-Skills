# FS.ACCOUNT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.ACCOUNT.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ACCOUNT.TYPE.DESCRIPTION` | `FsAccountType_Description` |  |  |  |
| 2 | `FS.ACCOUNT.TYPE.FILTER.KEY` | `FsAccountType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ACCOUNT.TYPE.RECORD.ID` | `FsAccountType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ACCOUNT.TYPE.RESERVED10` | `FsAccountType_Reserved10` | TField |  |  |
| 5 | `FS.ACCOUNT.TYPE.RESERVED9` | `FsAccountType_Reserved9` | TField |  |  |
| 6 | `FS.ACCOUNT.TYPE.RESERVED8` | `FsAccountType_Reserved8` | TField |  |  |
| 7 | `FS.ACCOUNT.TYPE.RESERVED7` | `FsAccountType_Reserved7` | TField |  |  |
| 8 | `FS.ACCOUNT.TYPE.RESERVED6` | `FsAccountType_Reserved6` | TField |  |  |
| 9 | `FS.ACCOUNT.TYPE.RESERVED5` | `FsAccountType_Reserved5` | TField |  |  |
| 10 | `FS.ACCOUNT.TYPE.RESERVED4` | `FsAccountType_Reserved4` | TField |  |  |
| 11 | `FS.ACCOUNT.TYPE.RESERVED3` | `FsAccountType_Reserved3` | TField |  |  |
| 12 | `FS.ACCOUNT.TYPE.RESERVED2` | `FsAccountType_Reserved2` | TField |  |  |
| 13 | `FS.ACCOUNT.TYPE.RESERVED1` | `FsAccountType_Reserved1` | TField |  |  |
| 14 | `FS.ACCOUNT.TYPE.LOCAL.REF` | `FsAccountType_LocalRef` |  |  |  |
| 15 | `FS.ACCOUNT.TYPE.OVERRIDE` | `FsAccountType_Override` |  |  |  |
| 16 | `FS.ACCOUNT.TYPE.RECORD.STATUS` | `FsAccountType_RecordStatus` | String |  |  |
| 17 | `FS.ACCOUNT.TYPE.CURR.NO` | `FsAccountType_CurrNo` | String |  |  |
| 18 | `FS.ACCOUNT.TYPE.INPUTTER` | `FsAccountType_Inputter` |  |  |  |
| 19 | `FS.ACCOUNT.TYPE.DATE.TIME` | `FsAccountType_DateTime` |  |  |  |
| 20 | `FS.ACCOUNT.TYPE.AUTHORISER` | `FsAccountType_Authoriser` | String |  |  |
| 21 | `FS.ACCOUNT.TYPE.CO.CODE` | `FsAccountType_CoCode` | String |  |  |
| 22 | `FS.ACCOUNT.TYPE.DEPT.CODE` | `FsAccountType_DeptCode` | String |  |  |
| 23 | `FS.ACCOUNT.TYPE.AUDITOR.CODE` | `FsAccountType_AuditorCode` | String |  |  |
| 24 | `FS.ACCOUNT.TYPE.AUDIT.DATE.TIME` | `FsAccountType_AuditDateTime` | String |  |  |
