# FS.GA.FAIR.VALUE.MARKET — Table Schema

> Source: `INSERTS/I_F.FS.GA.FAIR.VALUE.MARKET` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FAIR.VALUE.MARKET.QUOTATION.PLACE` | `FsGaFairValueMarket_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 2 | `FS.GA.FAIR.VALUE.MARKET.COUNTRY.ID.CODE` | `FsGaFairValueMarket_CountryIdCode` | TField |  | Allows the user to input Country defined in CMESS table under the table name "PAYS" Multifonds DB Column is CPAYS. |
| 3 | `FS.GA.FAIR.VALUE.MARKET.MARKET.PLACE` | `FsGaFairValueMarket_MarketPlace` | TField |  | Market place where quotation place is linked Multifonds DB Column is MAIN_MKT. |
| 4 | `FS.GA.FAIR.VALUE.MARKET.RESERVED10` | `FsGaFairValueMarket_Reserved10` | TField |  |  |
| 5 | `FS.GA.FAIR.VALUE.MARKET.RESERVED9` | `FsGaFairValueMarket_Reserved9` | TField |  |  |
| 6 | `FS.GA.FAIR.VALUE.MARKET.RESERVED8` | `FsGaFairValueMarket_Reserved8` | TField |  |  |
| 7 | `FS.GA.FAIR.VALUE.MARKET.RESERVED7` | `FsGaFairValueMarket_Reserved7` | TField |  |  |
| 8 | `FS.GA.FAIR.VALUE.MARKET.RESERVED6` | `FsGaFairValueMarket_Reserved6` | TField |  |  |
| 9 | `FS.GA.FAIR.VALUE.MARKET.RESERVED5` | `FsGaFairValueMarket_Reserved5` | TField |  |  |
| 10 | `FS.GA.FAIR.VALUE.MARKET.RESERVED4` | `FsGaFairValueMarket_Reserved4` | TField |  |  |
| 11 | `FS.GA.FAIR.VALUE.MARKET.RESERVED3` | `FsGaFairValueMarket_Reserved3` | TField |  |  |
| 12 | `FS.GA.FAIR.VALUE.MARKET.RESERVED2` | `FsGaFairValueMarket_Reserved2` | TField |  |  |
| 13 | `FS.GA.FAIR.VALUE.MARKET.RESERVED1` | `FsGaFairValueMarket_Reserved1` | TField |  |  |
| 14 | `FS.GA.FAIR.VALUE.MARKET.RECORD.STATUS` | `FsGaFairValueMarket_RecordStatus` | String |  |  |
| 15 | `FS.GA.FAIR.VALUE.MARKET.CURR.NO` | `FsGaFairValueMarket_CurrNo` | String |  |  |
| 16 | `FS.GA.FAIR.VALUE.MARKET.INPUTTER` | `FsGaFairValueMarket_Inputter` |  |  |  |
| 17 | `FS.GA.FAIR.VALUE.MARKET.DATE.TIME` | `FsGaFairValueMarket_DateTime` |  |  |  |
| 18 | `FS.GA.FAIR.VALUE.MARKET.AUTHORISER` | `FsGaFairValueMarket_Authoriser` | String |  |  |
| 19 | `FS.GA.FAIR.VALUE.MARKET.CO.CODE` | `FsGaFairValueMarket_CoCode` | String |  |  |
| 20 | `FS.GA.FAIR.VALUE.MARKET.DEPT.CODE` | `FsGaFairValueMarket_DeptCode` | String |  |  |
| 21 | `FS.GA.FAIR.VALUE.MARKET.AUDITOR.CODE` | `FsGaFairValueMarket_AuditorCode` | String |  |  |
| 22 | `FS.GA.FAIR.VALUE.MARKET.AUDIT.DATE.TIME` | `FsGaFairValueMarket_AuditDateTime` | String |  |  |
