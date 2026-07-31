# FS.GA.CURRENCY.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GA.CURRENCY.GROUP` in `FS_ExchangeRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CURRENCY.GROUP.PARENT.REF.ID` | `FsGaCurrencyGroup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CURRENCY.GROUP.ORA.ROWID` | `FsGaCurrencyGroup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CURRENCY.GROUP.EUROPEAN.CURRENCY.GROUP` | `FsGaCurrencyGroup_EuropeanCurrencyGroup` | TField |  | European currency group Multifonds DB Column is CSMON. |
| 4 | `FS.GA.CURRENCY.GROUP.LOCAL.CURRENCY` | `FsGaCurrencyGroup_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 5 | `FS.GA.CURRENCY.GROUP.RESERVED10` | `FsGaCurrencyGroup_Reserved10` | TField |  |  |
| 6 | `FS.GA.CURRENCY.GROUP.RESERVED9` | `FsGaCurrencyGroup_Reserved9` | TField |  |  |
| 7 | `FS.GA.CURRENCY.GROUP.RESERVED8` | `FsGaCurrencyGroup_Reserved8` | TField |  |  |
| 8 | `FS.GA.CURRENCY.GROUP.RESERVED7` | `FsGaCurrencyGroup_Reserved7` | TField |  |  |
| 9 | `FS.GA.CURRENCY.GROUP.RESERVED6` | `FsGaCurrencyGroup_Reserved6` | TField |  |  |
| 10 | `FS.GA.CURRENCY.GROUP.RESERVED5` | `FsGaCurrencyGroup_Reserved5` | TField |  |  |
| 11 | `FS.GA.CURRENCY.GROUP.RESERVED4` | `FsGaCurrencyGroup_Reserved4` | TField |  |  |
| 12 | `FS.GA.CURRENCY.GROUP.RESERVED3` | `FsGaCurrencyGroup_Reserved3` | TField |  |  |
| 13 | `FS.GA.CURRENCY.GROUP.RESERVED2` | `FsGaCurrencyGroup_Reserved2` | TField |  |  |
| 14 | `FS.GA.CURRENCY.GROUP.RESERVED1` | `FsGaCurrencyGroup_Reserved1` | TField |  |  |
| 15 | `FS.GA.CURRENCY.GROUP.LOCAL.REF` | `FsGaCurrencyGroup_LocalRef` |  |  |  |
| 16 | `FS.GA.CURRENCY.GROUP.OVERRIDE` | `FsGaCurrencyGroup_Override` |  |  |  |
| 17 | `FS.GA.CURRENCY.GROUP.RECORD.STATUS` | `FsGaCurrencyGroup_RecordStatus` | String |  |  |
| 18 | `FS.GA.CURRENCY.GROUP.CURR.NO` | `FsGaCurrencyGroup_CurrNo` | String |  |  |
| 19 | `FS.GA.CURRENCY.GROUP.INPUTTER` | `FsGaCurrencyGroup_Inputter` |  |  |  |
| 20 | `FS.GA.CURRENCY.GROUP.DATE.TIME` | `FsGaCurrencyGroup_DateTime` |  |  |  |
| 21 | `FS.GA.CURRENCY.GROUP.AUTHORISER` | `FsGaCurrencyGroup_Authoriser` | String |  |  |
| 22 | `FS.GA.CURRENCY.GROUP.CO.CODE` | `FsGaCurrencyGroup_CoCode` | String |  |  |
| 23 | `FS.GA.CURRENCY.GROUP.DEPT.CODE` | `FsGaCurrencyGroup_DeptCode` | String |  |  |
| 24 | `FS.GA.CURRENCY.GROUP.AUDITOR.CODE` | `FsGaCurrencyGroup_AuditorCode` | String |  |  |
| 25 | `FS.GA.CURRENCY.GROUP.AUDIT.DATE.TIME` | `FsGaCurrencyGroup_AuditDateTime` | String |  |  |
