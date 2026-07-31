# FS.CASH.ACCOUNT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.CASH.ACCOUNT.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.CASH.ACCOUNT.TYPE.DESCRIPTION` | `FsCashAccountType_Description` |  |  |  |
| 2 | `FS.CASH.ACCOUNT.TYPE.FILTER.KEY` | `FsCashAccountType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.CASH.ACCOUNT.TYPE.RECORD.ID` | `FsCashAccountType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.CASH.ACCOUNT.TYPE.RESERVED10` | `FsCashAccountType_Reserved10` | TField |  |  |
| 5 | `FS.CASH.ACCOUNT.TYPE.RESERVED9` | `FsCashAccountType_Reserved9` | TField |  |  |
| 6 | `FS.CASH.ACCOUNT.TYPE.RESERVED8` | `FsCashAccountType_Reserved8` | TField |  |  |
| 7 | `FS.CASH.ACCOUNT.TYPE.RESERVED7` | `FsCashAccountType_Reserved7` | TField |  |  |
| 8 | `FS.CASH.ACCOUNT.TYPE.RESERVED6` | `FsCashAccountType_Reserved6` | TField |  |  |
| 9 | `FS.CASH.ACCOUNT.TYPE.RESERVED5` | `FsCashAccountType_Reserved5` | TField |  |  |
| 10 | `FS.CASH.ACCOUNT.TYPE.RESERVED4` | `FsCashAccountType_Reserved4` | TField |  |  |
| 11 | `FS.CASH.ACCOUNT.TYPE.RESERVED3` | `FsCashAccountType_Reserved3` | TField |  |  |
| 12 | `FS.CASH.ACCOUNT.TYPE.RESERVED2` | `FsCashAccountType_Reserved2` | TField |  |  |
| 13 | `FS.CASH.ACCOUNT.TYPE.RESERVED1` | `FsCashAccountType_Reserved1` | TField |  |  |
| 14 | `FS.CASH.ACCOUNT.TYPE.LOCAL.REF` | `FsCashAccountType_LocalRef` |  |  |  |
| 15 | `FS.CASH.ACCOUNT.TYPE.OVERRIDE` | `FsCashAccountType_Override` |  |  |  |
| 16 | `FS.CASH.ACCOUNT.TYPE.RECORD.STATUS` | `FsCashAccountType_RecordStatus` | String |  |  |
| 17 | `FS.CASH.ACCOUNT.TYPE.CURR.NO` | `FsCashAccountType_CurrNo` | String |  |  |
| 18 | `FS.CASH.ACCOUNT.TYPE.INPUTTER` | `FsCashAccountType_Inputter` |  |  |  |
| 19 | `FS.CASH.ACCOUNT.TYPE.DATE.TIME` | `FsCashAccountType_DateTime` |  |  |  |
| 20 | `FS.CASH.ACCOUNT.TYPE.AUTHORISER` | `FsCashAccountType_Authoriser` | String |  |  |
| 21 | `FS.CASH.ACCOUNT.TYPE.CO.CODE` | `FsCashAccountType_CoCode` | String |  |  |
| 22 | `FS.CASH.ACCOUNT.TYPE.DEPT.CODE` | `FsCashAccountType_DeptCode` | String |  |  |
| 23 | `FS.CASH.ACCOUNT.TYPE.AUDITOR.CODE` | `FsCashAccountType_AuditorCode` | String |  |  |
| 24 | `FS.CASH.ACCOUNT.TYPE.AUDIT.DATE.TIME` | `FsCashAccountType_AuditDateTime` | String |  |  |
