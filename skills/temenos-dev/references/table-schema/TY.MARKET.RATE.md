# TY.MARKET.RATE — Table Schema

> Source: `INSERTS/I_F.TY.MARKET.RATE` in `TY_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.MR.DESCRIPTION` | `TyMarketRate_Description` |  |  |  |
| 2 | `TY.MR.INSTRUMENT.CODE` | `TyMarketRate_InstrumentCode` |  |  |  |
| 3 | `TY.MR.RATECODE` | `TyMarketRate_Ratecode` |  |  |  |
| 4 | `TY.MR.REST.DATE` | `TyMarketRate_RestDate` |  |  |  |
| 5 | `TY.MR.DAYS.SINCE.TODAY` | `TyMarketRate_DaysSinceToday` |  |  |  |
| 6 | `TY.MR.BID.ID` | `TyMarketRate_BidId` |  |  |  |
| 7 | `TY.MR.OFFER.ID` | `TyMarketRate_OfferId` |  |  |  |
| 8 | `TY.MR.BID.RATE` | `TyMarketRate_BidRate` |  |  |  |
| 9 | `TY.MR.OFFER.RATE` | `TyMarketRate_OfferRate` |  |  |  |
| 10 | `TY.MR.BID.TREND` | `TyMarketRate_BidTrend` |  |  |  |
| 11 | `TY.MR.OFFER.TREND` | `TyMarketRate_OfferTrend` |  |  |  |
| 12 | `TY.MR.RESERVED.15` | `TyMarketRate_Reserved15` |  |  |  |
| 13 | `TY.MR.RESERVED.14` | `TyMarketRate_Reserved14` |  |  |  |
| 14 | `TY.MR.RESERVED.13` | `TyMarketRate_Reserved13` |  |  |  |
| 15 | `TY.MR.RESERVED.12` | `TyMarketRate_Reserved12` |  |  |  |
| 16 | `TY.MR.RESERVED.11` | `TyMarketRate_Reserved11` |  |  |  |
| 17 | `TY.MR.RESERVED.10` | `TyMarketRate_Reserved10` | TField |  |  |
| 18 | `TY.MR.RESERVED.9` | `TyMarketRate_Reserved9` | TField |  |  |
| 19 | `TY.MR.RESERVED.8` | `TyMarketRate_Reserved8` | TField |  |  |
| 20 | `TY.MR.RESERVED.7` | `TyMarketRate_Reserved7` | TField |  |  |
| 21 | `TY.MR.RESERVED.6` | `TyMarketRate_Reserved6` | TField |  |  |
| 22 | `TY.MR.RESERVED.5` | `TyMarketRate_Reserved5` | TField |  |  |
| 23 | `TY.MR.RESERVED.4` | `TyMarketRate_Reserved4` | TField |  |  |
| 24 | `TY.MR.RESERVED.3` | `TyMarketRate_Reserved3` | TField |  |  |
| 25 | `TY.MR.RESERVED.2` | `TyMarketRate_Reserved2` | TField |  |  |
| 26 | `TY.MR.RESERVED.1` | `TyMarketRate_Reserved1` | TField |  |  |
| 27 | `TY.MR.LOCAL.REF` | `TyMarketRate_LocalRef` |  |  |  |
| 28 | `TY.MR.OVERRIDE` | `TyMarketRate_Override` |  |  |  |
| 29 | `TY.MR.RECORD.STATUS` | `TyMarketRate_RecordStatus` | String |  |  |
| 30 | `TY.MR.CURR.NO` | `TyMarketRate_CurrNo` | String |  |  |
| 31 | `TY.MR.INPUTTER` | `TyMarketRate_Inputter` |  |  |  |
| 32 | `TY.MR.DATE.TIME` | `TyMarketRate_DateTime` |  |  |  |
| 33 | `TY.MR.AUTHORISER` | `TyMarketRate_Authoriser` | String |  |  |
| 34 | `TY.MR.CO.CODE` | `TyMarketRate_CoCode` | String |  |  |
| 35 | `TY.MR.DEPT.CODE` | `TyMarketRate_DeptCode` | String |  |  |
| 36 | `TY.MR.AUDITOR.CODE` | `TyMarketRate_AuditorCode` | String |  |  |
| 37 | `TY.MR.AUDIT.DATE.TIME` | `TyMarketRate_AuditDateTime` | String |  |  |
