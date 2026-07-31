# BLMBRT.TRADING.PLATFORM — Table Schema

> Source: `INSERTS/I_F.BLMBRT.TRADING.PLATFORM` in `BLMBRT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLMBRT.TRADE.FIX.VERSION` | `BlmbrtTradingPlatform_FixVersion` | TField |  | The version of fix message being used.Example : Fix4.2,Fix4.4 |
| 2 | `BLMBRT.TRADE.DESCRIPTION` | `BlmbrtTradingPlatform_Description` | TField |  | This contains the short description of the table. |
| 3 | `BLMBRT.TRADE.FIX.MAP.ID` | `BlmbrtTradingPlatform_FixMapId` |  |  |  |
| 4 | `BLMBRT.TRADE.DFE.PARAM.ID` | `BlmbrtTradingPlatform_DfeParamId` | TField | Yes | This field contains a valid DFE.PARAMETER id with DFE.MAPPING which can be used to map the values of SEC TRADE and fix messageThis field is mandatory |
| 5 | `BLMBRT.TRADE.BLOOMBERG.UUID` | `BlmbrtTradingPlatform_BloombergUuid` |  |  |  |
| 6 | `BLMBRT.TRADE.SEC.ACCT.MASTER` | `BlmbrtTradingPlatform_SecAcctMaster` |  |  |  |
| 7 | `BLMBRT.TRADE.LOCAL.REF` | `BlmbrtTradingPlatform_LocalRef` |  |  |  |
| 8 | `BLMBRT.TRADE.RESERVED.10` | `BlmbrtTradingPlatform_Reserved10` | TField |  | Reserved field for future use |
| 9 | `BLMBRT.TRADE.RESERVED.9` | `BlmbrtTradingPlatform_Reserved9` | TField |  | Reserved field for future use |
| 10 | `BLMBRT.TRADE.RESERVED.8` | `BlmbrtTradingPlatform_Reserved8` | TField |  | Reserved field for future use |
| 11 | `BLMBRT.TRADE.RESERVED.7` | `BlmbrtTradingPlatform_Reserved7` | TField |  | Reserved field for future use |
| 12 | `BLMBRT.TRADE.RESERVED.6` | `BlmbrtTradingPlatform_Reserved6` | TField |  | Reserved field for future use |
| 13 | `BLMBRT.TRADE.RESERVED.5` | `BlmbrtTradingPlatform_Reserved5` | TField |  | Reserved field for future use |
| 14 | `BLMBRT.TRADE.RESERVED.4` | `BlmbrtTradingPlatform_Reserved4` | TField |  | Reserved field for future use |
| 15 | `BLMBRT.TRADE.RESERVED.3` | `BlmbrtTradingPlatform_Reserved3` | TField |  | Reserved field for future use |
| 16 | `BLMBRT.TRADE.RESERVED.2` | `BlmbrtTradingPlatform_Reserved2` | TField |  | Reserved field for future use |
| 17 | `BLMBRT.TRADE.RESERVED.1` | `BlmbrtTradingPlatform_Reserved1` | TField |  | Reserved field for future use |
| 18 | `BLMBRT.TRADE.OVERRIDE` | `BlmbrtTradingPlatform_Override` |  |  |  |
| 19 | `BLMBRT.TRADE.RECORD.STATUS` | `BlmbrtTradingPlatform_RecordStatus` | String |  |  |
| 20 | `BLMBRT.TRADE.CURR.NO` | `BlmbrtTradingPlatform_CurrNo` | String |  |  |
| 21 | `BLMBRT.TRADE.INPUTTER` | `BlmbrtTradingPlatform_Inputter` |  |  |  |
| 22 | `BLMBRT.TRADE.DATE.TIME` | `BlmbrtTradingPlatform_DateTime` |  |  |  |
| 23 | `BLMBRT.TRADE.AUTHORISER` | `BlmbrtTradingPlatform_Authoriser` | String |  |  |
| 24 | `BLMBRT.TRADE.CO.CODE` | `BlmbrtTradingPlatform_CoCode` | String |  |  |
| 25 | `BLMBRT.TRADE.DEPT.CODE` | `BlmbrtTradingPlatform_DeptCode` | String |  |  |
| 26 | `BLMBRT.TRADE.AUDITOR.CODE` | `BlmbrtTradingPlatform_AuditorCode` | String |  |  |
| 27 | `BLMBRT.TRADE.AUDIT.DATE.TIME` | `BlmbrtTradingPlatform_AuditDateTime` | String |  |  |
