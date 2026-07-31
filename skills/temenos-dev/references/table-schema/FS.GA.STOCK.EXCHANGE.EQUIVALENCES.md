# FS.GA.STOCK.EXCHANGE.EQUIVALENCES — Table Schema

> Source: `INSERTS/I_F.FS.GA.STOCK.EXCHANGE.EQUIVALENCES` in `FS_StaticEquivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.PARENT.REF.ID` | `FsGaStockExchangeEquivalences_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.ORA.ROWID` | `FsGaStockExchangeEquivalences_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.MULTIFONDS.STOCK.EXCHANGE.CODE` | `FsGaStockExchangeEquivalences_MultifondsStockExchangeCode` | TField |  | Multifonds Stock Exchange Code Multifonds DB Column is CPLACE_MULTIFONDS. |
| 4 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.TELEKURS.STOCK.EXCHANGE.CODE` | `FsGaStockExchangeEquivalences_TelekursStockExchangeCode` | TField |  | Telekurs Stock Exchange Code Multifonds DB Column is CPLACE_TELEKURS. |
| 5 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.BLOOMBERG.STOCK.EXCHANGE.CODE` | `FsGaStockExchangeEquivalences_BloombergStockExchangeCode` | TField |  | Bloomberg Stock Exchange Code Multifonds DB Column is CPLACE_BLOOMBERG. |
| 6 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.REUTERS.STOCK.EXCHANGE.CODE` | `FsGaStockExchangeEquivalences_ReutersStockExchangeCode` | TField |  | Reuters Stock Exchange Code Multifonds DB Column is CPLACE_REUTERS. |
| 7 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.CUSTOMER.STOCK.EXCHANGE.CODE` | `FsGaStockExchangeEquivalences_CustomerStockExchangeCode` | TField |  | Customer Stock Exchange Code Multifonds DB Column is CPLACE_REPRISE. |
| 8 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.COUNTERPARTY.MARKET.ID` | `FsGaStockExchangeEquivalences_CounterpartyMarketId` | TField |  | Market identifier tagged to a counterparty definition Multifonds DB Column is CODE_CPLACE_ID. |
| 9 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED10` | `FsGaStockExchangeEquivalences_Reserved10` | TField |  |  |
| 10 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED9` | `FsGaStockExchangeEquivalences_Reserved9` | TField |  |  |
| 11 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED8` | `FsGaStockExchangeEquivalences_Reserved8` | TField |  |  |
| 12 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED7` | `FsGaStockExchangeEquivalences_Reserved7` | TField |  |  |
| 13 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED6` | `FsGaStockExchangeEquivalences_Reserved6` | TField |  |  |
| 14 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED5` | `FsGaStockExchangeEquivalences_Reserved5` | TField |  |  |
| 15 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED4` | `FsGaStockExchangeEquivalences_Reserved4` | TField |  |  |
| 16 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED3` | `FsGaStockExchangeEquivalences_Reserved3` | TField |  |  |
| 17 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED2` | `FsGaStockExchangeEquivalences_Reserved2` | TField |  |  |
| 18 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RESERVED1` | `FsGaStockExchangeEquivalences_Reserved1` | TField |  |  |
| 19 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.LOCAL.REF` | `FsGaStockExchangeEquivalences_LocalRef` |  |  |  |
| 20 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.OVERRIDE` | `FsGaStockExchangeEquivalences_Override` |  |  |  |
| 21 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.RECORD.STATUS` | `FsGaStockExchangeEquivalences_RecordStatus` | String |  |  |
| 22 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.CURR.NO` | `FsGaStockExchangeEquivalences_CurrNo` | String |  |  |
| 23 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.INPUTTER` | `FsGaStockExchangeEquivalences_Inputter` |  |  |  |
| 24 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.DATE.TIME` | `FsGaStockExchangeEquivalences_DateTime` |  |  |  |
| 25 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.AUTHORISER` | `FsGaStockExchangeEquivalences_Authoriser` | String |  |  |
| 26 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.CO.CODE` | `FsGaStockExchangeEquivalences_CoCode` | String |  |  |
| 27 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.DEPT.CODE` | `FsGaStockExchangeEquivalences_DeptCode` | String |  |  |
| 28 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.AUDITOR.CODE` | `FsGaStockExchangeEquivalences_AuditorCode` | String |  |  |
| 29 | `FS.GA.STOCK.EXCHANGE.EQUIVALENCES.AUDIT.DATE.TIME` | `FsGaStockExchangeEquivalences_AuditDateTime` | String |  |  |
