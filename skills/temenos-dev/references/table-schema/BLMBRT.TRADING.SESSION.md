# BLMBRT.TRADING.SESSION — Table Schema

> Source: `INSERTS/I_F.BLMBRT.TRADING.SESSION` in `BLMBRT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLMBRT.SESSION.TRADING.ID` | `BlmbrtTradingSession_TradingId` | TField |  | This field contains the Id of the trading center(stock exchange). |
| 2 | `BLMBRT.SESSION.FIX.CONV.ID` | `BlmbrtTradingSession_FixConvId` | TField |  | This field has the tag numbers required to form the mapping id. |
| 3 | `BLMBRT.SESSION.LOCAL.REF` | `BlmbrtTradingSession_LocalRef` |  |  |  |
| 4 | `BLMBRT.SESSION.RESERVED.10` | `BlmbrtTradingSession_Reserved10` | TField |  | Reserved field for future use |
| 5 | `BLMBRT.SESSION.RESERVED.9` | `BlmbrtTradingSession_Reserved9` | TField |  | Reserved field for future use |
| 6 | `BLMBRT.SESSION.RESERVED.8` | `BlmbrtTradingSession_Reserved8` | TField |  | Reserved field for future use |
| 7 | `BLMBRT.SESSION.RESERVED.7` | `BlmbrtTradingSession_Reserved7` | TField |  | Reserved field for future use |
| 8 | `BLMBRT.SESSION.RESERVED.6` | `BlmbrtTradingSession_Reserved6` | TField |  | Reserved field for future use |
| 9 | `BLMBRT.SESSION.RESERVED.5` | `BlmbrtTradingSession_Reserved5` | TField |  | Reserved field for future use |
| 10 | `BLMBRT.SESSION.RESERVED.4` | `BlmbrtTradingSession_Reserved4` | TField |  | Reserved field for future use |
| 11 | `BLMBRT.SESSION.RESERVED.3` | `BlmbrtTradingSession_Reserved3` | TField |  | Reserved field for future use |
| 12 | `BLMBRT.SESSION.RESERVED.2` | `BlmbrtTradingSession_Reserved2` | TField |  | Reserved field for future use |
| 13 | `BLMBRT.SESSION.RESERVED.1` | `BlmbrtTradingSession_Reserved1` | TField |  | Reserved field for future use |
| 14 | `BLMBRT.SESSION.OVERRIDE` | `BlmbrtTradingSession_Override` |  |  |  |
| 15 | `BLMBRT.SESSION.RECORD.STATUS` | `BlmbrtTradingSession_RecordStatus` | String |  |  |
| 16 | `BLMBRT.SESSION.CURR.NO` | `BlmbrtTradingSession_CurrNo` | String |  |  |
| 17 | `BLMBRT.SESSION.INPUTTER` | `BlmbrtTradingSession_Inputter` |  |  |  |
| 18 | `BLMBRT.SESSION.DATE.TIME` | `BlmbrtTradingSession_DateTime` |  |  |  |
| 19 | `BLMBRT.SESSION.AUTHORISER` | `BlmbrtTradingSession_Authoriser` | String |  |  |
| 20 | `BLMBRT.SESSION.CO.CODE` | `BlmbrtTradingSession_CoCode` | String |  |  |
| 21 | `BLMBRT.SESSION.DEPT.CODE` | `BlmbrtTradingSession_DeptCode` | String |  |  |
| 22 | `BLMBRT.SESSION.AUDITOR.CODE` | `BlmbrtTradingSession_AuditorCode` | String |  |  |
| 23 | `BLMBRT.SESSION.AUDIT.DATE.TIME` | `BlmbrtTradingSession_AuditDateTime` | String |  |  |
