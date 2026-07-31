# FS.INCOME.CHARACTER — Table Schema

> Source: `INSERTS/I_F.FS.INCOME.CHARACTER` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.INCOME.CHARACTER.DESCRIPTION` | `FsIncomeCharacter_Description` |  |  |  |
| 2 | `FS.INCOME.CHARACTER.FILTER.KEY` | `FsIncomeCharacter_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.INCOME.CHARACTER.RECORD.ID` | `FsIncomeCharacter_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.INCOME.CHARACTER.RESERVED10` | `FsIncomeCharacter_Reserved10` | TField |  |  |
| 5 | `FS.INCOME.CHARACTER.RESERVED9` | `FsIncomeCharacter_Reserved9` | TField |  |  |
| 6 | `FS.INCOME.CHARACTER.RESERVED8` | `FsIncomeCharacter_Reserved8` | TField |  |  |
| 7 | `FS.INCOME.CHARACTER.RESERVED7` | `FsIncomeCharacter_Reserved7` | TField |  |  |
| 8 | `FS.INCOME.CHARACTER.RESERVED6` | `FsIncomeCharacter_Reserved6` | TField |  |  |
| 9 | `FS.INCOME.CHARACTER.RESERVED5` | `FsIncomeCharacter_Reserved5` | TField |  |  |
| 10 | `FS.INCOME.CHARACTER.RESERVED4` | `FsIncomeCharacter_Reserved4` | TField |  |  |
| 11 | `FS.INCOME.CHARACTER.RESERVED3` | `FsIncomeCharacter_Reserved3` | TField |  |  |
| 12 | `FS.INCOME.CHARACTER.RESERVED2` | `FsIncomeCharacter_Reserved2` | TField |  |  |
| 13 | `FS.INCOME.CHARACTER.RESERVED1` | `FsIncomeCharacter_Reserved1` | TField |  |  |
| 14 | `FS.INCOME.CHARACTER.LOCAL.REF` | `FsIncomeCharacter_LocalRef` |  |  |  |
| 15 | `FS.INCOME.CHARACTER.OVERRIDE` | `FsIncomeCharacter_Override` |  |  |  |
| 16 | `FS.INCOME.CHARACTER.RECORD.STATUS` | `FsIncomeCharacter_RecordStatus` | String |  |  |
| 17 | `FS.INCOME.CHARACTER.CURR.NO` | `FsIncomeCharacter_CurrNo` | String |  |  |
| 18 | `FS.INCOME.CHARACTER.INPUTTER` | `FsIncomeCharacter_Inputter` |  |  |  |
| 19 | `FS.INCOME.CHARACTER.DATE.TIME` | `FsIncomeCharacter_DateTime` |  |  |  |
| 20 | `FS.INCOME.CHARACTER.AUTHORISER` | `FsIncomeCharacter_Authoriser` | String |  |  |
| 21 | `FS.INCOME.CHARACTER.CO.CODE` | `FsIncomeCharacter_CoCode` | String |  |  |
| 22 | `FS.INCOME.CHARACTER.DEPT.CODE` | `FsIncomeCharacter_DeptCode` | String |  |  |
| 23 | `FS.INCOME.CHARACTER.AUDITOR.CODE` | `FsIncomeCharacter_AuditorCode` | String |  |  |
| 24 | `FS.INCOME.CHARACTER.AUDIT.DATE.TIME` | `FsIncomeCharacter_AuditDateTime` | String |  |  |
