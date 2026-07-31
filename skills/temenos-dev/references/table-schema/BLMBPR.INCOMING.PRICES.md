# BLMBPR.INCOMING.PRICES — Table Schema

> Source: `INSERTS/I_F.BLMBPR.INCOMING.PRICES` in `BLMBPR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLMBPR.INCOMPRI.SEC.NO` | `BlmbprIncomingPrices_SecNo` | TField |  | The ID of the security in GLOBUS.This id will be SECURITY.MASTER id. |
| 2 | `BLMBPR.INCOMPRI.ERR.STATUS` | `BlmbprIncomingPrices_ErrStatus` | TField |  | This field will be update in the Error message. |
| 3 | `BLMBPR.INCOMPRI.RETURN.CODE` | `BlmbprIncomingPrices_ReturnCode` | TField |  | The return code from Bloomberg for success or error messages. |
| 4 | `BLMBPR.INCOMPRI.NO.OF.FIELDS` | `BlmbprIncomingPrices_NoOfFields` | TField |  | The number of fields requested and received to be used to get the different values in the reply line. |
| 5 | `BLMBPR.INCOMPRI.SEC.NAME` | `BlmbprIncomingPrices_SecName` | TField |  | The name of the security. |
| 6 | `BLMBPR.INCOMPRI.CURRENCY` | `BlmbprIncomingPrices_Currency` | TField |  | The currency of the security from the feed. |
| 7 | `BLMBPR.INCOMPRI.EXCHANGE.RATE` | `BlmbprIncomingPrices_ExchangeRate` | TField |  | A value of 1 if the currency in the feed is the same as the currency in GLOBUS for that security and the actual exchange rate if between the two currencies if they are different. |
| 8 | `BLMBPR.INCOMPRI.LAST.PRICE` | `BlmbprIncomingPrices_LastPrice` | TField |  | The contents of the last price field for this security in the feed. |
| 9 | `BLMBPR.INCOMPRI.LAST.UPD.DATE` | `BlmbprIncomingPrices_LastUpdDate` | TField |  | PeThe date of the last price update. |
| 10 | `BLMBPR.INCOMPRI.LAST.UPD.TIME` | `BlmbprIncomingPrices_LastUpdTime` | TField |  | The time if the last price update was today or the date if it was before today. |
| 11 | `BLMBPR.INCOMPRI.DATE.OF.FEED` | `BlmbprIncomingPrices_DateOfFeed` | TField |  | Date on which this record was created. |
| 12 | `BLMBPR.INCOMPRI.NO.OF.DAYS.REJECT` | `BlmbprIncomingPrices_NoOfDaysReject` | TField |  | Number of days that the security has been rejected by Bloomberg. |
| 13 | `BLMBPR.INCOMPRI.YEST.CLOS.PRICE` | `BlmbprIncomingPrices_YestClosPrice` | TField |  |  |
| 14 | `BLMBPR.INCOMPRI.HIS.MID.CLOS.PR` | `BlmbprIncomingPrices_HisMidClosPr` | TField |  |  |
| 15 | `BLMBPR.INCOMPRI.PR.MID.CLOS.PR` | `BlmbprIncomingPrices_PrMidClosPr` | TField |  |  |
| 16 | `BLMBPR.INCOMPRI.OPEN.PRICE` | `BlmbprIncomingPrices_OpenPrice` | TField |  |  |
| 17 | `BLMBPR.INCOMPRI.HIGH.PRICE` | `BlmbprIncomingPrices_HighPrice` | TField |  |  |
| 18 | `BLMBPR.INCOMPRI.LOW.PRICE` | `BlmbprIncomingPrices_LowPrice` | TField |  |  |
| 19 | `BLMBPR.INCOMPRI.BID.PRICE` | `BlmbprIncomingPrices_BidPrice` | TField |  |  |
| 20 | `BLMBPR.INCOMPRI.ASK.PRICE` | `BlmbprIncomingPrices_AskPrice` | TField |  |  |
| 21 | `BLMBPR.INCOMPRI.VOLUME.OF.TRADE` | `BlmbprIncomingPrices_VolumeOfTrade` | TField |  |  |
| 22 | `BLMBPR.INCOMPRI.PRICE.SOURCE` | `BlmbprIncomingPrices_PriceSource` | TField |  |  |
| 23 | `BLMBPR.INCOMPRI.LAST.TR.DT.OR.TIME` | `BlmbprIncomingPrices_LastTrDtOrTime` | TField |  |  |
| 24 | `BLMBPR.INCOMPRI.GLOBUS.UPD.DATE` | `BlmbprIncomingPrices_GlobusUpdDate` | TField |  |  |
| 25 | `BLMBPR.INCOMPRI.COUPON.DATE` | `BlmbprIncomingPrices_CouponDate` | TField |  |  |
| 26 | `BLMBPR.INCOMPRI.COUPON.RATE` | `BlmbprIncomingPrices_CouponRate` | TField |  |  |
| 27 | `BLMBPR.INCOMPRI.CAP.RATE` | `BlmbprIncomingPrices_CapRate` | TField |  |  |
| 28 | `BLMBPR.INCOMPRI.FACTOR` | `BlmbprIncomingPrices_Factor` | TField |  |  |
| 29 | `BLMBPR.INCOMPRI.MOODY.RATING` | `BlmbprIncomingPrices_MoodyRating` | TField |  |  |
| 30 | `BLMBPR.INCOMPRI.RESERVED.5` | `BlmbprIncomingPrices_Reserved5` | TField |  |  |
| 31 | `BLMBPR.INCOMPRI.RESERVED.4` | `BlmbprIncomingPrices_Reserved4` | TField |  |  |
| 32 | `BLMBPR.INCOMPRI.RESERVED.3` | `BlmbprIncomingPrices_Reserved3` | TField |  |  |
| 33 | `BLMBPR.INCOMPRI.RESERVED.2` | `BlmbprIncomingPrices_Reserved2` | TField |  |  |
| 34 | `BLMBPR.INCOMPRI.RESERVED.1` | `BlmbprIncomingPrices_Reserved1` | TField |  |  |
| 35 | `BLMBPR.INCOMPRI.LOCAL.REF` | `BlmbprIncomingPrices_LocalRef` |  |  |  |
| 36 | `BLMBPR.INCOMPRI.OVERRIDE` | `BlmbprIncomingPrices_Override` |  |  |  |
| 37 | `BLMBPR.INCOMPRI.RECORD.STATUS` | `BlmbprIncomingPrices_RecordStatus` | String |  |  |
| 38 | `BLMBPR.INCOMPRI.CURR.NO` | `BlmbprIncomingPrices_CurrNo` | String |  |  |
| 39 | `BLMBPR.INCOMPRI.INPUTTER` | `BlmbprIncomingPrices_Inputter` |  |  |  |
| 40 | `BLMBPR.INCOMPRI.DATE.TIME` | `BlmbprIncomingPrices_DateTime` |  |  |  |
| 41 | `BLMBPR.INCOMPRI.AUTHORISER` | `BlmbprIncomingPrices_Authoriser` | String |  |  |
| 42 | `BLMBPR.INCOMPRI.CO.CODE` | `BlmbprIncomingPrices_CoCode` | String |  |  |
| 43 | `BLMBPR.INCOMPRI.DEPT.CODE` | `BlmbprIncomingPrices_DeptCode` | String |  |  |
| 44 | `BLMBPR.INCOMPRI.AUDITOR.CODE` | `BlmbprIncomingPrices_AuditorCode` | String |  |  |
| 45 | `BLMBPR.INCOMPRI.AUDIT.DATE.TIME` | `BlmbprIncomingPrices_AuditDateTime` | String |  |  |
