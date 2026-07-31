# SC.MARKET.INDICATOR — Table Schema

> Source: `INSERTS/I_F.SC.MARKET.INDICATOR` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MI.RULE.NAME` | `ScMarketIndicator_RuleName` |  |  |  |
| 2 | `SC.MI.DEPO.SUB.ACCOUNT` | `ScMarketIndicator_DepoSubAccount` |  |  |  |
| 3 | `SC.MI.ISIN.COUNTRY` | `ScMarketIndicator_IsinCountry` |  |  |  |
| 4 | `SC.MI.SEC.TYPE` | `ScMarketIndicator_SecType` |  |  |  |
| 5 | `SC.MI.STOCK.EXCH.DOM` | `ScMarketIndicator_StockExchDom` |  |  |  |
| 6 | `SC.MI.STOCK.EXCH` | `ScMarketIndicator_StockExch` |  |  |  |
| 7 | `SC.MI.TRANS.TYPE` | `ScMarketIndicator_TransType` |  |  |  |
| 8 | `SC.MI.APPLICATION` | `ScMarketIndicator_Application` |  |  |  |
| 9 | `SC.MI.MESSAGE.TYPE` | `ScMarketIndicator_MessageType` |  |  |  |
| 10 | `SC.MI.PSET` | `ScMarketIndicator_Pset` |  |  |  |
| 11 | `SC.MI.SUB.RESERVED1` | `ScMarketIndicator_SubReserved1` |  |  |  |
| 12 | `SC.MI.SUB.RESERVED2` | `ScMarketIndicator_SubReserved2` |  |  |  |
| 13 | `SC.MI.SUB.RESERVED3` | `ScMarketIndicator_SubReserved3` |  |  |  |
| 14 | `SC.MI.SUB.RESERVED4` | `ScMarketIndicator_SubReserved4` |  |  |  |
| 15 | `SC.MI.SUB.RESERVED5` | `ScMarketIndicator_SubReserved5` |  |  |  |
| 16 | `SC.MI.SUB.RESERVED6` | `ScMarketIndicator_SubReserved6` |  |  |  |
| 17 | `SC.MI.SUB.RESERVED7` | `ScMarketIndicator_SubReserved7` |  |  |  |
| 18 | `SC.MI.SUB.RESERVED8` | `ScMarketIndicator_SubReserved8` |  |  |  |
| 19 | `SC.MI.SUB.RESERVED9` | `ScMarketIndicator_SubReserved9` |  |  |  |
| 20 | `SC.MI.SUB.RESERVED10` | `ScMarketIndicator_SubReserved10` |  |  |  |
| 21 | `SC.MI.QUALIFIER` | `ScMarketIndicator_Qualifier` |  |  |  |
| 22 | `SC.MI.DATA.SOURCE.NAME` | `ScMarketIndicator_DataSourceName` |  |  |  |
| 23 | `SC.MI.INDICATOR` | `ScMarketIndicator_Indicator` |  |  |  |
| 24 | `SC.MI.RESERVED1` | `ScMarketIndicator_Reserved1` | TField |  |  |
| 25 | `SC.MI.RESERVED2` | `ScMarketIndicator_Reserved2` | TField |  |  |
| 26 | `SC.MI.RESERVED3` | `ScMarketIndicator_Reserved3` | TField |  |  |
| 27 | `SC.MI.RESERVED4` | `ScMarketIndicator_Reserved4` | TField |  |  |
| 28 | `SC.MI.RESERVED5` | `ScMarketIndicator_Reserved5` | TField |  |  |
| 29 | `SC.MI.RESERVED6` | `ScMarketIndicator_Reserved6` | TField |  |  |
| 30 | `SC.MI.RESERVED7` | `ScMarketIndicator_Reserved7` | TField |  |  |
| 31 | `SC.MI.RESERVED8` | `ScMarketIndicator_Reserved8` | TField |  |  |
| 32 | `SC.MI.RESERVED9` | `ScMarketIndicator_Reserved9` | TField |  |  |
| 33 | `SC.MI.RESERVED10` | `ScMarketIndicator_Reserved10` | TField |  |  |
| 34 | `SC.MI.RESERVED11` | `ScMarketIndicator_Reserved11` | TField |  |  |
| 35 | `SC.MI.RESERVED12` | `ScMarketIndicator_Reserved12` | TField |  |  |
| 36 | `SC.MI.RESERVED13` | `ScMarketIndicator_Reserved13` | TField |  |  |
| 37 | `SC.MI.RESERVED14` | `ScMarketIndicator_Reserved14` | TField |  |  |
| 38 | `SC.MI.RESERVED15` | `ScMarketIndicator_Reserved15` | TField |  |  |
| 39 | `SC.MI.RESERVED16` | `ScMarketIndicator_Reserved16` | TField |  |  |
| 40 | `SC.MI.RESERVED17` | `ScMarketIndicator_Reserved17` | TField |  |  |
| 41 | `SC.MI.RESERVED18` | `ScMarketIndicator_Reserved18` | TField |  |  |
| 42 | `SC.MI.RESERVED19` | `ScMarketIndicator_Reserved19` | TField |  |  |
| 43 | `SC.MI.RESERVED20` | `ScMarketIndicator_Reserved20` | TField |  |  |
| 44 | `SC.MI.LOCAL.REF` | `ScMarketIndicator_LocalRef` |  |  |  |
| 45 | `SC.MI.OVERRIDE` | `ScMarketIndicator_Override` |  |  |  |
| 46 | `SC.MI.RECORD.STATUS` | `ScMarketIndicator_RecordStatus` | String |  |  |
| 47 | `SC.MI.CURR.NO` | `ScMarketIndicator_CurrNo` | String |  |  |
| 48 | `SC.MI.INPUTTER` | `ScMarketIndicator_Inputter` |  |  |  |
| 49 | `SC.MI.DATE.TIME` | `ScMarketIndicator_DateTime` |  |  |  |
| 50 | `SC.MI.AUTHORISER` | `ScMarketIndicator_Authoriser` | String |  |  |
| 51 | `SC.MI.CO.CODE` | `ScMarketIndicator_CoCode` | String |  |  |
| 52 | `SC.MI.DEPT.CODE` | `ScMarketIndicator_DeptCode` | String |  |  |
| 53 | `SC.MI.AUDITOR.CODE` | `ScMarketIndicator_AuditorCode` | String |  |  |
| 54 | `SC.MI.AUDIT.DATE.TIME` | `ScMarketIndicator_AuditDateTime` | String |  |  |
