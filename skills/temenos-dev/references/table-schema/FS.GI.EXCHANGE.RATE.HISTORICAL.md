# FS.GI.EXCHANGE.RATE.HISTORICAL — Table Schema

> Source: `INSERTS/I_F.FS.GI.EXCHANGE.RATE.HISTORICAL` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.EXCHANGE.RATE.HISTORICAL.PARENT.REF.ID` | `FsGiExchangeRateHistorical_ParentRefId` |  |  |  |
| 2 | `FS.GI.EXCHANGE.RATE.HISTORICAL.ORA.ROWID` | `FsGiExchangeRateHistorical_OraRowid` |  |  |  |
| 3 | `FS.GI.EXCHANGE.RATE.HISTORICAL.ACCOUNTING.DATE.MF` | `FsGiExchangeRateHistorical_AccountingDateMf` |  |  |  |
| 4 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RATE.DATE` | `FsGiExchangeRateHistorical_RateDate` |  |  |  |
| 5 | `FS.GI.EXCHANGE.RATE.HISTORICAL.FUND.MASTER.CCY` | `FsGiExchangeRateHistorical_FundMasterCcy` |  |  |  |
| 6 | `FS.GI.EXCHANGE.RATE.HISTORICAL.CCY` | `FsGiExchangeRateHistorical_Ccy` |  |  |  |
| 7 | `FS.GI.EXCHANGE.RATE.HISTORICAL.EXCHANGE.RATE` | `FsGiExchangeRateHistorical_ExchangeRate` |  |  |  |
| 8 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED10` | `FsGiExchangeRateHistorical_Reserved10` |  |  |  |
| 9 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED9` | `FsGiExchangeRateHistorical_Reserved9` |  |  |  |
| 10 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED8` | `FsGiExchangeRateHistorical_Reserved8` |  |  |  |
| 11 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED7` | `FsGiExchangeRateHistorical_Reserved7` |  |  |  |
| 12 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED6` | `FsGiExchangeRateHistorical_Reserved6` |  |  |  |
| 13 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED5` | `FsGiExchangeRateHistorical_Reserved5` |  |  |  |
| 14 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED4` | `FsGiExchangeRateHistorical_Reserved4` |  |  |  |
| 15 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED3` | `FsGiExchangeRateHistorical_Reserved3` |  |  |  |
| 16 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED2` | `FsGiExchangeRateHistorical_Reserved2` |  |  |  |
| 17 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RESERVED1` | `FsGiExchangeRateHistorical_Reserved1` |  |  |  |
| 18 | `FS.GI.EXCHANGE.RATE.HISTORICAL.LOCAL.REF` | `FsGiExchangeRateHistorical_LocalRef` |  |  |  |
| 19 | `FS.GI.EXCHANGE.RATE.HISTORICAL.OVERRIDE` | `FsGiExchangeRateHistorical_Override` |  |  |  |
| 20 | `FS.GI.EXCHANGE.RATE.HISTORICAL.RECORD.STATUS` | `FsGiExchangeRateHistorical_RecordStatus` |  |  |  |
| 21 | `FS.GI.EXCHANGE.RATE.HISTORICAL.CURR.NO` | `FsGiExchangeRateHistorical_CurrNo` |  |  |  |
| 22 | `FS.GI.EXCHANGE.RATE.HISTORICAL.INPUTTER` | `FsGiExchangeRateHistorical_Inputter` |  |  |  |
| 23 | `FS.GI.EXCHANGE.RATE.HISTORICAL.DATE.TIME` | `FsGiExchangeRateHistorical_DateTime` |  |  |  |
| 24 | `FS.GI.EXCHANGE.RATE.HISTORICAL.AUTHORISER` | `FsGiExchangeRateHistorical_Authoriser` |  |  |  |
| 25 | `FS.GI.EXCHANGE.RATE.HISTORICAL.CO.CODE` | `FsGiExchangeRateHistorical_CoCode` |  |  |  |
| 26 | `FS.GI.EXCHANGE.RATE.HISTORICAL.DEPT.CODE` | `FsGiExchangeRateHistorical_DeptCode` |  |  |  |
| 27 | `FS.GI.EXCHANGE.RATE.HISTORICAL.AUDITOR.CODE` | `FsGiExchangeRateHistorical_AuditorCode` |  |  |  |
| 28 | `FS.GI.EXCHANGE.RATE.HISTORICAL.AUDIT.DATE.TIME` | `FsGiExchangeRateHistorical_AuditDateTime` |  |  |  |
