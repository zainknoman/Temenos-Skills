# FS.INCOME.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.INCOME.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.INCOME.TYPE.DESCRIPTION` | `FsIncomeType_Description` |  |  |  |
| 2 | `FS.INCOME.TYPE.FILTER.KEY` | `FsIncomeType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.INCOME.TYPE.RECORD.ID` | `FsIncomeType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.INCOME.TYPE.RESERVED10` | `FsIncomeType_Reserved10` | TField |  |  |
| 5 | `FS.INCOME.TYPE.RESERVED9` | `FsIncomeType_Reserved9` | TField |  |  |
| 6 | `FS.INCOME.TYPE.RESERVED8` | `FsIncomeType_Reserved8` | TField |  |  |
| 7 | `FS.INCOME.TYPE.RESERVED7` | `FsIncomeType_Reserved7` | TField |  |  |
| 8 | `FS.INCOME.TYPE.RESERVED6` | `FsIncomeType_Reserved6` | TField |  |  |
| 9 | `FS.INCOME.TYPE.RESERVED5` | `FsIncomeType_Reserved5` | TField |  |  |
| 10 | `FS.INCOME.TYPE.RESERVED4` | `FsIncomeType_Reserved4` | TField |  |  |
| 11 | `FS.INCOME.TYPE.RESERVED3` | `FsIncomeType_Reserved3` | TField |  |  |
| 12 | `FS.INCOME.TYPE.RESERVED2` | `FsIncomeType_Reserved2` | TField |  |  |
| 13 | `FS.INCOME.TYPE.RESERVED1` | `FsIncomeType_Reserved1` | TField |  |  |
| 14 | `FS.INCOME.TYPE.LOCAL.REF` | `FsIncomeType_LocalRef` |  |  |  |
| 15 | `FS.INCOME.TYPE.OVERRIDE` | `FsIncomeType_Override` |  |  |  |
| 16 | `FS.INCOME.TYPE.RECORD.STATUS` | `FsIncomeType_RecordStatus` | String |  |  |
| 17 | `FS.INCOME.TYPE.CURR.NO` | `FsIncomeType_CurrNo` | String |  |  |
| 18 | `FS.INCOME.TYPE.INPUTTER` | `FsIncomeType_Inputter` |  |  |  |
| 19 | `FS.INCOME.TYPE.DATE.TIME` | `FsIncomeType_DateTime` |  |  |  |
| 20 | `FS.INCOME.TYPE.AUTHORISER` | `FsIncomeType_Authoriser` | String |  |  |
| 21 | `FS.INCOME.TYPE.CO.CODE` | `FsIncomeType_CoCode` | String |  |  |
| 22 | `FS.INCOME.TYPE.DEPT.CODE` | `FsIncomeType_DeptCode` | String |  |  |
| 23 | `FS.INCOME.TYPE.AUDITOR.CODE` | `FsIncomeType_AuditorCode` | String |  |  |
| 24 | `FS.INCOME.TYPE.AUDIT.DATE.TIME` | `FsIncomeType_AuditDateTime` | String |  |  |
