# FS.GA.CURRENCY.BY.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GA.CURRENCY.BY.GROUP` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CURRENCY.BY.GROUP.PARENT.REF.ID` | `FsGaCurrencyByGroup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CURRENCY.BY.GROUP.ORA.ROWID` | `FsGaCurrencyByGroup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CURRENCY.BY.GROUP.BOOK.CURRENCY` | `FsGaCurrencyByGroup_BookCurrency` | TField |  | Currency for expressing exchange rate. Also used to denote currency for various reporting. Multifonds DB Column is CMONREF. |
| 4 | `FS.GA.CURRENCY.BY.GROUP.GROUP` | `FsGaCurrencyByGroup_Group` | TField |  | Group Multifonds DB Column is GROUPE. |
| 5 | `FS.GA.CURRENCY.BY.GROUP.CURRENCY.CODE` | `FsGaCurrencyByGroup_CurrencyCode` | TField |  | Currency Code like USD, EUR Multifonds DB Column is CODMON. |
| 6 | `FS.GA.CURRENCY.BY.GROUP.TRANSACTION.PRICE` | `FsGaCurrencyByGroup_TransactionPrice` | TField |  | The unit price of an instrument which is being transacted. Multifonds DB Column is TCOURS. |
| 7 | `FS.GA.CURRENCY.BY.GROUP.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaCurrencyByGroup_TradeOrValueOrAccDate` | TField |  | Input Trade date or Value date or accounting date. Depends on the feature that is used Multifonds DB Column is DCTA. |
| 8 | `FS.GA.CURRENCY.BY.GROUP.RATE.DATE` | `FsGaCurrencyByGroup_RateDate` | TField |  | Exchange, Interest Rate date Multifonds DB Column is DCTA_TCHG. |
| 9 | `FS.GA.CURRENCY.BY.GROUP.USER.NAMES` | `FsGaCurrencyByGroup_UserNames` | TField |  | User Name. Multifonds DB Column is CUSER. |
| 10 | `FS.GA.CURRENCY.BY.GROUP.RESERVED10` | `FsGaCurrencyByGroup_Reserved10` | TField |  |  |
| 11 | `FS.GA.CURRENCY.BY.GROUP.RESERVED9` | `FsGaCurrencyByGroup_Reserved9` | TField |  |  |
| 12 | `FS.GA.CURRENCY.BY.GROUP.RESERVED8` | `FsGaCurrencyByGroup_Reserved8` | TField |  |  |
| 13 | `FS.GA.CURRENCY.BY.GROUP.RESERVED7` | `FsGaCurrencyByGroup_Reserved7` | TField |  |  |
| 14 | `FS.GA.CURRENCY.BY.GROUP.RESERVED6` | `FsGaCurrencyByGroup_Reserved6` | TField |  |  |
| 15 | `FS.GA.CURRENCY.BY.GROUP.RESERVED5` | `FsGaCurrencyByGroup_Reserved5` | TField |  |  |
| 16 | `FS.GA.CURRENCY.BY.GROUP.RESERVED4` | `FsGaCurrencyByGroup_Reserved4` | TField |  |  |
| 17 | `FS.GA.CURRENCY.BY.GROUP.RESERVED3` | `FsGaCurrencyByGroup_Reserved3` | TField |  |  |
| 18 | `FS.GA.CURRENCY.BY.GROUP.RESERVED2` | `FsGaCurrencyByGroup_Reserved2` | TField |  |  |
| 19 | `FS.GA.CURRENCY.BY.GROUP.RESERVED1` | `FsGaCurrencyByGroup_Reserved1` | TField |  |  |
| 20 | `FS.GA.CURRENCY.BY.GROUP.LOCAL.REF` | `FsGaCurrencyByGroup_LocalRef` |  |  |  |
| 21 | `FS.GA.CURRENCY.BY.GROUP.OVERRIDE` | `FsGaCurrencyByGroup_Override` |  |  |  |
| 22 | `FS.GA.CURRENCY.BY.GROUP.RECORD.STATUS` | `FsGaCurrencyByGroup_RecordStatus` | String |  |  |
| 23 | `FS.GA.CURRENCY.BY.GROUP.CURR.NO` | `FsGaCurrencyByGroup_CurrNo` | String |  |  |
| 24 | `FS.GA.CURRENCY.BY.GROUP.INPUTTER` | `FsGaCurrencyByGroup_Inputter` |  |  |  |
| 25 | `FS.GA.CURRENCY.BY.GROUP.DATE.TIME` | `FsGaCurrencyByGroup_DateTime` |  |  |  |
| 26 | `FS.GA.CURRENCY.BY.GROUP.AUTHORISER` | `FsGaCurrencyByGroup_Authoriser` | String |  |  |
| 27 | `FS.GA.CURRENCY.BY.GROUP.CO.CODE` | `FsGaCurrencyByGroup_CoCode` | String |  |  |
| 28 | `FS.GA.CURRENCY.BY.GROUP.DEPT.CODE` | `FsGaCurrencyByGroup_DeptCode` | String |  |  |
| 29 | `FS.GA.CURRENCY.BY.GROUP.AUDITOR.CODE` | `FsGaCurrencyByGroup_AuditorCode` | String |  |  |
| 30 | `FS.GA.CURRENCY.BY.GROUP.AUDIT.DATE.TIME` | `FsGaCurrencyByGroup_AuditDateTime` | String |  |  |
