# FS.GA.ISSUER.RATING — Table Schema

> Source: `INSERTS/I_F.FS.GA.ISSUER.RATING` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ISSUER.RATING.CORRESPONDENT` | `FsGaIssuerRating_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 2 | `FS.GA.ISSUER.RATING.RATING.FOR.SHORT` | `FsGaIssuerRating_RatingForShort` | TField |  | Rating For Short Multifonds DB Column is CRATING_S. |
| 3 | `FS.GA.ISSUER.RATING.RATING.TYPE.FOR.SHORT` | `FsGaIssuerRating_RatingTypeForShort` | TField |  | Rating Type For Short Multifonds DB Column is TYP_RATING_S. |
| 4 | `FS.GA.ISSUER.RATING.WATCH.LIST.FOR.SHORT.TERM` | `FsGaIssuerRating_WatchListForShortTerm` | TField |  | Watch List For Short Term Multifonds DB Column is WATCH_LIST_S. |
| 5 | `FS.GA.ISSUER.RATING.OUT.LOOK.FOR.SHORT.TERM` | `FsGaIssuerRating_OutLookForShortTerm` | TField |  | Out Look For Short Term Multifonds DB Column is OUT_LOOK_S. |
| 6 | `FS.GA.ISSUER.RATING.ANALY.STS.OF.ST.CREDIT.RISK` | `FsGaIssuerRating_AnalyStsOfStCreditRisk` | TField |  | Analysis Status Of Short Term Credit Risk Multifonds DB Column is STAT_RATE_S. |
| 7 | `FS.GA.ISSUER.RATING.ANALY.DATE.OF.ST.CREDIT.RISK` | `FsGaIssuerRating_AnalyDateOfStCreditRisk` | TField |  | Analysis Date Of Short Term Credit Risk Multifonds DB Column is ANALYSIS_DATE_S. |
| 8 | `FS.GA.ISSUER.RATING.ANALY.RECOM.OF.ST.CREDIT.RISK` | `FsGaIssuerRating_AnalyRecomOfStCreditRisk` | TField |  | Analysis Recommendation Of Short Term Credit Risk Multifonds DB Column is RECOMMENDATION_S. |
| 9 | `FS.GA.ISSUER.RATING.RATING.FOR.LONG` | `FsGaIssuerRating_RatingForLong` | TField |  | Rating For Long Multifonds DB Column is CRATING_L. |
| 10 | `FS.GA.ISSUER.RATING.RATING.TYPE.FOR.LONG` | `FsGaIssuerRating_RatingTypeForLong` | TField |  | Rating Type For Long Multifonds DB Column is TYP_RATING_L. |
| 11 | `FS.GA.ISSUER.RATING.WATCH.LIST.FOR.LONG.TERM` | `FsGaIssuerRating_WatchListForLongTerm` | TField |  | Watch List For Long Term Multifonds DB Column is WATCH_LIST_L. |
| 12 | `FS.GA.ISSUER.RATING.OUT.LOOK.FOR.LONG.TERM` | `FsGaIssuerRating_OutLookForLongTerm` | TField |  | Out Look For Long Term Multifonds DB Column is OUT_LOOK_L. |
| 13 | `FS.GA.ISSUER.RATING.ANALY.STS.OF.LT.CREDIT.RISK` | `FsGaIssuerRating_AnalyStsOfLtCreditRisk` | TField |  | Analysis Status Of Long Term Credit Risk Multifonds DB Column is STAT_RATE_L. |
| 14 | `FS.GA.ISSUER.RATING.ANALY.DATE.OF.LT.CREDIT.RISK` | `FsGaIssuerRating_AnalyDateOfLtCreditRisk` | TField |  | Analysis Date Of Long Term Credit Risk Multifonds DB Column is ANALYSIS_DATE_L. |
| 15 | `FS.GA.ISSUER.RATING.ANALY.RECOM.OF.LT.CREDIT.RISK` | `FsGaIssuerRating_AnalyRecomOfLtCreditRisk` | TField |  | Analysis Recommendation Of Long Term Credit Risk Multifonds DB Column is RECOMMENDATION_L. |
| 16 | `FS.GA.ISSUER.RATING.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaIssuerRating_TradeOrValueOrAccDate` | TField |  | Input Trade date or Value date or accounting date. Depends on the feature that is used Multifonds DB Column is DCTA. |
| 17 | `FS.GA.ISSUER.RATING.RATING.NUMBER` | `FsGaIssuerRating_RatingNumber` | TField |  | Rating Number Multifonds DB Column is RATING_NO. |
| 18 | `FS.GA.ISSUER.RATING.RESERVED10` | `FsGaIssuerRating_Reserved10` | TField |  |  |
| 19 | `FS.GA.ISSUER.RATING.RESERVED9` | `FsGaIssuerRating_Reserved9` | TField |  |  |
| 20 | `FS.GA.ISSUER.RATING.RESERVED8` | `FsGaIssuerRating_Reserved8` | TField |  |  |
| 21 | `FS.GA.ISSUER.RATING.RESERVED7` | `FsGaIssuerRating_Reserved7` | TField |  |  |
| 22 | `FS.GA.ISSUER.RATING.RESERVED6` | `FsGaIssuerRating_Reserved6` | TField |  |  |
| 23 | `FS.GA.ISSUER.RATING.RESERVED5` | `FsGaIssuerRating_Reserved5` | TField |  |  |
| 24 | `FS.GA.ISSUER.RATING.RESERVED4` | `FsGaIssuerRating_Reserved4` | TField |  |  |
| 25 | `FS.GA.ISSUER.RATING.RESERVED3` | `FsGaIssuerRating_Reserved3` | TField |  |  |
| 26 | `FS.GA.ISSUER.RATING.RESERVED2` | `FsGaIssuerRating_Reserved2` | TField |  |  |
| 27 | `FS.GA.ISSUER.RATING.RESERVED1` | `FsGaIssuerRating_Reserved1` | TField |  |  |
| 28 | `FS.GA.ISSUER.RATING.RECORD.STATUS` | `FsGaIssuerRating_RecordStatus` | String |  |  |
| 29 | `FS.GA.ISSUER.RATING.CURR.NO` | `FsGaIssuerRating_CurrNo` | String |  |  |
| 30 | `FS.GA.ISSUER.RATING.INPUTTER` | `FsGaIssuerRating_Inputter` |  |  |  |
| 31 | `FS.GA.ISSUER.RATING.DATE.TIME` | `FsGaIssuerRating_DateTime` |  |  |  |
| 32 | `FS.GA.ISSUER.RATING.AUTHORISER` | `FsGaIssuerRating_Authoriser` | String |  |  |
| 33 | `FS.GA.ISSUER.RATING.CO.CODE` | `FsGaIssuerRating_CoCode` | String |  |  |
| 34 | `FS.GA.ISSUER.RATING.DEPT.CODE` | `FsGaIssuerRating_DeptCode` | String |  |  |
| 35 | `FS.GA.ISSUER.RATING.AUDITOR.CODE` | `FsGaIssuerRating_AuditorCode` | String |  |  |
| 36 | `FS.GA.ISSUER.RATING.AUDIT.DATE.TIME` | `FsGaIssuerRating_AuditDateTime` | String |  |  |
