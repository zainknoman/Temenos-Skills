# FS.GA.FORWARD.EXCHANGE.RATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.FORWARD.EXCHANGE.RATE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FORWARD.EXCHANGE.RATE.PARENT.REF.ID` | `FsGaForwardExchangeRate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FORWARD.EXCHANGE.RATE.ORA.ROWID` | `FsGaForwardExchangeRate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FORWARD.EXCHANGE.RATE.INTEREST.RATE.TYPE` | `FsGaForwardExchangeRate_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 4 | `FS.GA.FORWARD.EXCHANGE.RATE.BOOK.CURRENCY` | `FsGaForwardExchangeRate_BookCurrency` | TField |  | Currency for expressing exchange rate. Also used to denote currency for various reporting. Multifonds DB Column is CMONREF. |
| 5 | `FS.GA.FORWARD.EXCHANGE.RATE.LOCAL.CURRENCY` | `FsGaForwardExchangeRate_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 6 | `FS.GA.FORWARD.EXCHANGE.RATE.MATURITY.CODE` | `FsGaForwardExchangeRate_MaturityCode` | TField |  | Maturity code of the floating interest rate that needs to be applied for commission accrual on a lending/borrowing transaction Multifonds DB Column is CODE_MOIS. |
| 7 | `FS.GA.FORWARD.EXCHANGE.RATE.VALUE.DATE` | `FsGaForwardExchangeRate_ValueDate` | TField |  | Value date of the Forward Interest/exchange rate Multifonds DB Column is DFIXING. |
| 8 | `FS.GA.FORWARD.EXCHANGE.RATE.RATE.DATE` | `FsGaForwardExchangeRate_RateDate` | TField |  | Exchange, Interest Rate date Multifonds DB Column is DCTA_TCHG. |
| 9 | `FS.GA.FORWARD.EXCHANGE.RATE.PRICE.IN.LOCAL.CURRENCY` | `FsGaForwardExchangeRate_PriceInLocalCurrency` | TField |  | It reflects Price, Market Price,security price.effective unit price Multifonds DB Column is COURS. |
| 10 | `FS.GA.FORWARD.EXCHANGE.RATE.SPOT.RATE` | `FsGaForwardExchangeRate_SpotRate` | TField |  | Spot Exchange rate Multifonds DB Column is SPOT_RATE. |
| 11 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED10` | `FsGaForwardExchangeRate_Reserved10` | TField |  |  |
| 12 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED9` | `FsGaForwardExchangeRate_Reserved9` | TField |  |  |
| 13 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED8` | `FsGaForwardExchangeRate_Reserved8` | TField |  |  |
| 14 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED7` | `FsGaForwardExchangeRate_Reserved7` | TField |  |  |
| 15 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED6` | `FsGaForwardExchangeRate_Reserved6` | TField |  |  |
| 16 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED5` | `FsGaForwardExchangeRate_Reserved5` | TField |  |  |
| 17 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED4` | `FsGaForwardExchangeRate_Reserved4` | TField |  |  |
| 18 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED3` | `FsGaForwardExchangeRate_Reserved3` | TField |  |  |
| 19 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED2` | `FsGaForwardExchangeRate_Reserved2` | TField |  |  |
| 20 | `FS.GA.FORWARD.EXCHANGE.RATE.RESERVED1` | `FsGaForwardExchangeRate_Reserved1` | TField |  |  |
| 21 | `FS.GA.FORWARD.EXCHANGE.RATE.LOCAL.REF` | `FsGaForwardExchangeRate_LocalRef` |  |  |  |
| 22 | `FS.GA.FORWARD.EXCHANGE.RATE.OVERRIDE` | `FsGaForwardExchangeRate_Override` |  |  |  |
| 23 | `FS.GA.FORWARD.EXCHANGE.RATE.RECORD.STATUS` | `FsGaForwardExchangeRate_RecordStatus` | String |  |  |
| 24 | `FS.GA.FORWARD.EXCHANGE.RATE.CURR.NO` | `FsGaForwardExchangeRate_CurrNo` | String |  |  |
| 25 | `FS.GA.FORWARD.EXCHANGE.RATE.INPUTTER` | `FsGaForwardExchangeRate_Inputter` |  |  |  |
| 26 | `FS.GA.FORWARD.EXCHANGE.RATE.DATE.TIME` | `FsGaForwardExchangeRate_DateTime` |  |  |  |
| 27 | `FS.GA.FORWARD.EXCHANGE.RATE.AUTHORISER` | `FsGaForwardExchangeRate_Authoriser` | String |  |  |
| 28 | `FS.GA.FORWARD.EXCHANGE.RATE.CO.CODE` | `FsGaForwardExchangeRate_CoCode` | String |  |  |
| 29 | `FS.GA.FORWARD.EXCHANGE.RATE.DEPT.CODE` | `FsGaForwardExchangeRate_DeptCode` | String |  |  |
| 30 | `FS.GA.FORWARD.EXCHANGE.RATE.AUDITOR.CODE` | `FsGaForwardExchangeRate_AuditorCode` | String |  |  |
| 31 | `FS.GA.FORWARD.EXCHANGE.RATE.AUDIT.DATE.TIME` | `FsGaForwardExchangeRate_AuditDateTime` | String |  |  |
