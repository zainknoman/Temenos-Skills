# FS.GA.CURRENCIES — Table Schema

> Source: `INSERTS/I_F.FS.GA.CURRENCIES` in `FS_ExchangeRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CURRENCIES.PARENT.REF.ID` | `FsGaCurrencies_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CURRENCIES.ORA.ROWID` | `FsGaCurrencies_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CURRENCIES.BOOK.CURRENCY` | `FsGaCurrencies_BookCurrency` | TField |  | Currency for expressing exchange rate. Also used to denote currency for various reporting. Multifonds DB Column is CMONREF. |
| 4 | `FS.GA.CURRENCIES.CURRENCY.CODE` | `FsGaCurrencies_CurrencyCode` | TField |  | Currency Code like USD, EUR Multifonds DB Column is CODMON. |
| 5 | `FS.GA.CURRENCIES.TRANSACTION.PRICE` | `FsGaCurrencies_TransactionPrice` | TField |  | The unit price of an instrument which is being transacted. Multifonds DB Column is TCOURS. |
| 6 | `FS.GA.CURRENCIES.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaCurrencies_TradeOrValueOrAccDate` | TField |  | Input Trade date or Value date or accounting date. Depends on the feature that is used Multifonds DB Column is DCTA. |
| 7 | `FS.GA.CURRENCIES.RATE.DATE` | `FsGaCurrencies_RateDate` | TField |  | Exchange, Interest Rate date Multifonds DB Column is DCTA_TCHG. |
| 8 | `FS.GA.CURRENCIES.USER.NAMES` | `FsGaCurrencies_UserNames` | TField |  | User Name. Multifonds DB Column is CUSER. |
| 9 | `FS.GA.CURRENCIES.RESERVED10` | `FsGaCurrencies_Reserved10` | TField |  |  |
| 10 | `FS.GA.CURRENCIES.RESERVED9` | `FsGaCurrencies_Reserved9` | TField |  |  |
| 11 | `FS.GA.CURRENCIES.RESERVED8` | `FsGaCurrencies_Reserved8` | TField |  |  |
| 12 | `FS.GA.CURRENCIES.RESERVED7` | `FsGaCurrencies_Reserved7` | TField |  |  |
| 13 | `FS.GA.CURRENCIES.RESERVED6` | `FsGaCurrencies_Reserved6` | TField |  |  |
| 14 | `FS.GA.CURRENCIES.RESERVED5` | `FsGaCurrencies_Reserved5` | TField |  |  |
| 15 | `FS.GA.CURRENCIES.RESERVED4` | `FsGaCurrencies_Reserved4` | TField |  |  |
| 16 | `FS.GA.CURRENCIES.RESERVED3` | `FsGaCurrencies_Reserved3` | TField |  |  |
| 17 | `FS.GA.CURRENCIES.RESERVED2` | `FsGaCurrencies_Reserved2` | TField |  |  |
| 18 | `FS.GA.CURRENCIES.RESERVED1` | `FsGaCurrencies_Reserved1` | TField |  |  |
| 19 | `FS.GA.CURRENCIES.LOCAL.REF` | `FsGaCurrencies_LocalRef` |  |  |  |
| 20 | `FS.GA.CURRENCIES.OVERRIDE` | `FsGaCurrencies_Override` |  |  |  |
| 21 | `FS.GA.CURRENCIES.RECORD.STATUS` | `FsGaCurrencies_RecordStatus` | String |  |  |
| 22 | `FS.GA.CURRENCIES.CURR.NO` | `FsGaCurrencies_CurrNo` | String |  |  |
| 23 | `FS.GA.CURRENCIES.INPUTTER` | `FsGaCurrencies_Inputter` |  |  |  |
| 24 | `FS.GA.CURRENCIES.DATE.TIME` | `FsGaCurrencies_DateTime` |  |  |  |
| 25 | `FS.GA.CURRENCIES.AUTHORISER` | `FsGaCurrencies_Authoriser` | String |  |  |
| 26 | `FS.GA.CURRENCIES.CO.CODE` | `FsGaCurrencies_CoCode` | String |  |  |
| 27 | `FS.GA.CURRENCIES.DEPT.CODE` | `FsGaCurrencies_DeptCode` | String |  |  |
| 28 | `FS.GA.CURRENCIES.AUDITOR.CODE` | `FsGaCurrencies_AuditorCode` | String |  |  |
| 29 | `FS.GA.CURRENCIES.AUDIT.DATE.TIME` | `FsGaCurrencies_AuditDateTime` | String |  |  |
