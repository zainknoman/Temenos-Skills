# FS.GA.CROSS.CURRENCY.RATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.CROSS.CURRENCY.RATE` in `FS_PricesRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CROSS.CURRENCY.RATE.PARENT.REF.ID` | `FsGaCrossCurrencyRate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CROSS.CURRENCY.RATE.ORA.ROWID` | `FsGaCrossCurrencyRate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CROSS.CURRENCY.RATE.FUND.ID` | `FsGaCrossCurrencyRate_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.CROSS.CURRENCY.RATE.FX.GROUP.CODE` | `FsGaCrossCurrencyRate_FxGroupCode` | TField |  | Group Exchange Rate Mf Multifonds DB Column is CGROUPE_COURS. |
| 5 | `FS.GA.CROSS.CURRENCY.RATE.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaCrossCurrencyRate_TradeOrValueOrAccDate` | TField |  | Input Trade date or Value date or accounting date. Depends on the feature that is used Multifonds DB Column is DCTA. |
| 6 | `FS.GA.CROSS.CURRENCY.RATE.BOOK.CURRENCY` | `FsGaCrossCurrencyRate_BookCurrency` | TField |  | Currency for expressing exchange rate. Also used to denote currency for various reporting. Multifonds DB Column is CMONREF. |
| 7 | `FS.GA.CROSS.CURRENCY.RATE.LOCAL.CURRENCY` | `FsGaCrossCurrencyRate_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 8 | `FS.GA.CROSS.CURRENCY.RATE.TRANSACTION.PRICE` | `FsGaCrossCurrencyRate_TransactionPrice` | TField |  | The unit price of an instrument which is being transacted. Multifonds DB Column is TCOURS. |
| 9 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED10` | `FsGaCrossCurrencyRate_Reserved10` | TField |  |  |
| 10 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED9` | `FsGaCrossCurrencyRate_Reserved9` | TField |  |  |
| 11 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED8` | `FsGaCrossCurrencyRate_Reserved8` | TField |  |  |
| 12 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED7` | `FsGaCrossCurrencyRate_Reserved7` | TField |  |  |
| 13 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED6` | `FsGaCrossCurrencyRate_Reserved6` | TField |  |  |
| 14 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED5` | `FsGaCrossCurrencyRate_Reserved5` | TField |  |  |
| 15 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED4` | `FsGaCrossCurrencyRate_Reserved4` | TField |  |  |
| 16 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED3` | `FsGaCrossCurrencyRate_Reserved3` | TField |  |  |
| 17 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED2` | `FsGaCrossCurrencyRate_Reserved2` | TField |  |  |
| 18 | `FS.GA.CROSS.CURRENCY.RATE.RESERVED1` | `FsGaCrossCurrencyRate_Reserved1` | TField |  |  |
| 19 | `FS.GA.CROSS.CURRENCY.RATE.LOCAL.REF` | `FsGaCrossCurrencyRate_LocalRef` |  |  |  |
| 20 | `FS.GA.CROSS.CURRENCY.RATE.OVERRIDE` | `FsGaCrossCurrencyRate_Override` |  |  |  |
| 21 | `FS.GA.CROSS.CURRENCY.RATE.RECORD.STATUS` | `FsGaCrossCurrencyRate_RecordStatus` | String |  |  |
| 22 | `FS.GA.CROSS.CURRENCY.RATE.CURR.NO` | `FsGaCrossCurrencyRate_CurrNo` | String |  |  |
| 23 | `FS.GA.CROSS.CURRENCY.RATE.INPUTTER` | `FsGaCrossCurrencyRate_Inputter` |  |  |  |
| 24 | `FS.GA.CROSS.CURRENCY.RATE.DATE.TIME` | `FsGaCrossCurrencyRate_DateTime` |  |  |  |
| 25 | `FS.GA.CROSS.CURRENCY.RATE.AUTHORISER` | `FsGaCrossCurrencyRate_Authoriser` | String |  |  |
| 26 | `FS.GA.CROSS.CURRENCY.RATE.CO.CODE` | `FsGaCrossCurrencyRate_CoCode` | String |  |  |
| 27 | `FS.GA.CROSS.CURRENCY.RATE.DEPT.CODE` | `FsGaCrossCurrencyRate_DeptCode` | String |  |  |
| 28 | `FS.GA.CROSS.CURRENCY.RATE.AUDITOR.CODE` | `FsGaCrossCurrencyRate_AuditorCode` | String |  |  |
| 29 | `FS.GA.CROSS.CURRENCY.RATE.AUDIT.DATE.TIME` | `FsGaCrossCurrencyRate_AuditDateTime` | String |  |  |
