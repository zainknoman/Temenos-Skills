# ILSCPR.INSTRUM.PORTFOLIO.PRICE.FEED — Table Schema

> Source: `INSERTS/I_F.ILSCPR.INSTRUM.PORTFOLIO.PRICE.FEED` in `ILSCPR_PriceFeed.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRICE.FEED.PORTFOLIO` | `IlscprInstrumPortfolioPriceFeed_Portfolio` | TField |  | The portfolio associated with this record. Either a valid SEC.ACC.MASTER record or "ALL". |
| 2 | `PRICE.FEED.INSTRUMENT` | `IlscprInstrumPortfolioPriceFeed_Instrument` | TField |  | The sub-asset type or the security master associated with this record. Either a valid SEC.ACC.MASTER record or S-SUB.ASSET.TYPE or "ALL". |
| 3 | `PRICE.FEED.EXPIRY.DATE` | `IlscprInstrumPortfolioPriceFeed_ExpiryDate` | TField |  | The expiry date associated with the price feed source selection. |
| 4 | `PRICE.FEED.PRICE.FEED.SOURCE` | `IlscprInstrumPortfolioPriceFeed_PriceFeedSource` | TField |  | This indicates, the price feed source for the selected record. |
| 5 | `PRICE.FEED.LOCAL.REF` | `IlscprInstrumPortfolioPriceFeed_LocalRef` |  |  |  |
| 6 | `PRICE.FEED.RESERVED.1` | `IlscprInstrumPortfolioPriceFeed_Reserved1` | TField |  |  |
| 7 | `PRICE.FEED.RESERVED.2` | `IlscprInstrumPortfolioPriceFeed_Reserved2` | TField |  |  |
| 8 | `PRICE.FEED.RESERVED.3` | `IlscprInstrumPortfolioPriceFeed_Reserved3` | TField |  |  |
| 9 | `PRICE.FEED.RESERVED.4` | `IlscprInstrumPortfolioPriceFeed_Reserved4` | TField |  |  |
| 10 | `PRICE.FEED.RESERVED.5` | `IlscprInstrumPortfolioPriceFeed_Reserved5` | TField |  |  |
| 11 | `PRICE.FEED.RESERVED.6` | `IlscprInstrumPortfolioPriceFeed_Reserved6` | TField |  |  |
| 12 | `PRICE.FEED.RESERVED.7` | `IlscprInstrumPortfolioPriceFeed_Reserved7` | TField |  |  |
| 13 | `PRICE.FEED.RESERVED.8` | `IlscprInstrumPortfolioPriceFeed_Reserved8` | TField |  |  |
| 14 | `PRICE.FEED.RESERVED.9` | `IlscprInstrumPortfolioPriceFeed_Reserved9` | TField |  |  |
| 15 | `PRICE.FEED.RESERVED.10` | `IlscprInstrumPortfolioPriceFeed_Reserved10` | TField |  |  |
| 16 | `PRICE.FEED.OVERRIDE` | `IlscprInstrumPortfolioPriceFeed_Override` |  |  |  |
| 17 | `PRICE.FEED.RECORD.STATUS` | `IlscprInstrumPortfolioPriceFeed_RecordStatus` | String |  |  |
| 18 | `PRICE.FEED.CURR.NO` | `IlscprInstrumPortfolioPriceFeed_CurrNo` | String |  |  |
| 19 | `PRICE.FEED.INPUTTER` | `IlscprInstrumPortfolioPriceFeed_Inputter` |  |  |  |
| 20 | `PRICE.FEED.DATE.TIME` | `IlscprInstrumPortfolioPriceFeed_DateTime` |  |  |  |
| 21 | `PRICE.FEED.AUTHORISER` | `IlscprInstrumPortfolioPriceFeed_Authoriser` | String |  |  |
| 22 | `PRICE.FEED.CO.CODE` | `IlscprInstrumPortfolioPriceFeed_CoCode` | String |  |  |
| 23 | `PRICE.FEED.DEPT.CODE` | `IlscprInstrumPortfolioPriceFeed_DeptCode` | String |  |  |
| 24 | `PRICE.FEED.AUDITOR.CODE` | `IlscprInstrumPortfolioPriceFeed_AuditorCode` | String |  |  |
| 25 | `PRICE.FEED.AUDIT.DATE.TIME` | `IlscprInstrumPortfolioPriceFeed_AuditDateTime` | String |  |  |
