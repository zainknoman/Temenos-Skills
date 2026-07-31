# FS.GA.CURRENCY.CONVERSION — Table Schema

> Source: `INSERTS/I_F.FS.GA.CURRENCY.CONVERSION` in `FS_PricesRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CURRENCY.CONVERSION.EQUIVALENCE.TYPE` | `FsGaCurrencyConversion_EquivalenceType` | TField |  | Interfacing of transactions, corporate actions, static data, and migration positions is supported by different equivalence types. Multifonds DB Column is EQUI_TYPE. |
| 2 | `FS.GA.CURRENCY.CONVERSION.FUND.ID` | `FsGaCurrencyConversion_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 3 | `FS.GA.CURRENCY.CONVERSION.QUOTATION.PLACE` | `FsGaCurrencyConversion_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 4 | `FS.GA.CURRENCY.CONVERSION.BOOK.CURRENCY` | `FsGaCurrencyConversion_BookCurrency` | TField |  | Currency for expressing exchange rate. Also used to denote currency for various reporting. Multifonds DB Column is CMONREF. |
| 5 | `FS.GA.CURRENCY.CONVERSION.DOMICILE` | `FsGaCurrencyConversion_Domicile` | TField |  | Domicile of correspondent Multifonds DB Column is CDOMICI. |
| 6 | `FS.GA.CURRENCY.CONVERSION.CURRENCY.EQUIVALENCE` | `FsGaCurrencyConversion_CurrencyEquivalence` | TField |  | Currency to be used if all the parameters are met. This is typically the offshore currency in which the transaction / prices etc are recorded. Multifonds DB Column is CMON_EQUI. |
| 7 | `FS.GA.CURRENCY.CONVERSION.RESERVED10` | `FsGaCurrencyConversion_Reserved10` | TField |  |  |
| 8 | `FS.GA.CURRENCY.CONVERSION.RESERVED9` | `FsGaCurrencyConversion_Reserved9` | TField |  |  |
| 9 | `FS.GA.CURRENCY.CONVERSION.RESERVED8` | `FsGaCurrencyConversion_Reserved8` | TField |  |  |
| 10 | `FS.GA.CURRENCY.CONVERSION.RESERVED7` | `FsGaCurrencyConversion_Reserved7` | TField |  |  |
| 11 | `FS.GA.CURRENCY.CONVERSION.RESERVED6` | `FsGaCurrencyConversion_Reserved6` | TField |  |  |
| 12 | `FS.GA.CURRENCY.CONVERSION.RESERVED5` | `FsGaCurrencyConversion_Reserved5` | TField |  |  |
| 13 | `FS.GA.CURRENCY.CONVERSION.RESERVED4` | `FsGaCurrencyConversion_Reserved4` | TField |  |  |
| 14 | `FS.GA.CURRENCY.CONVERSION.RESERVED3` | `FsGaCurrencyConversion_Reserved3` | TField |  |  |
| 15 | `FS.GA.CURRENCY.CONVERSION.RESERVED2` | `FsGaCurrencyConversion_Reserved2` | TField |  |  |
| 16 | `FS.GA.CURRENCY.CONVERSION.RESERVED1` | `FsGaCurrencyConversion_Reserved1` | TField |  |  |
| 17 | `FS.GA.CURRENCY.CONVERSION.RECORD.STATUS` | `FsGaCurrencyConversion_RecordStatus` | String |  |  |
| 18 | `FS.GA.CURRENCY.CONVERSION.CURR.NO` | `FsGaCurrencyConversion_CurrNo` | String |  |  |
| 19 | `FS.GA.CURRENCY.CONVERSION.INPUTTER` | `FsGaCurrencyConversion_Inputter` |  |  |  |
| 20 | `FS.GA.CURRENCY.CONVERSION.DATE.TIME` | `FsGaCurrencyConversion_DateTime` |  |  |  |
| 21 | `FS.GA.CURRENCY.CONVERSION.AUTHORISER` | `FsGaCurrencyConversion_Authoriser` | String |  |  |
| 22 | `FS.GA.CURRENCY.CONVERSION.CO.CODE` | `FsGaCurrencyConversion_CoCode` | String |  |  |
| 23 | `FS.GA.CURRENCY.CONVERSION.DEPT.CODE` | `FsGaCurrencyConversion_DeptCode` | String |  |  |
| 24 | `FS.GA.CURRENCY.CONVERSION.AUDITOR.CODE` | `FsGaCurrencyConversion_AuditorCode` | String |  |  |
| 25 | `FS.GA.CURRENCY.CONVERSION.AUDIT.DATE.TIME` | `FsGaCurrencyConversion_AuditDateTime` | String |  |  |
