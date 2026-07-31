# FS.GA.FAIR.VALUE.MARKET.TRIGGER — Table Schema

> Source: `INSERTS/I_F.FS.GA.FAIR.VALUE.MARKET.TRIGGER` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.NAV.GROUP.CODE` | `FsGaFairValueMarketTrigger_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 2 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.FUND.ID` | `FsGaFairValueMarketTrigger_FundId` |  |  |  |
| 3 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.INTERNAL.SECURITY.ID` | `FsGaFairValueMarketTrigger_InternalSecurityId` |  |  |  |
| 4 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.MARKET.PLACE` | `FsGaFairValueMarketTrigger_MarketPlace` | TField |  | Market place where quotation place is linked Multifonds DB Column is MAIN_MKT. |
| 5 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.TOLERANCE` | `FsGaFairValueMarketTrigger_Tolerance` | TField |  | The tolerance will be the minimum change necessary to bring into effect. E.g, Tolerance for Fair value price or NAV / Fixed tolerance group or APS account rebalancing Multifonds DB Column is TOLERANCE. |
| 6 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.PRICE.SOURCE` | `FsGaFairValueMarketTrigger_PriceSource` |  |  |  |
| 7 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.OTHER.PROVIDER` | `FsGaFairValueMarketTrigger_OtherProvider` | TField |  | Enter the sec price prov. Acc to the price sltn algorithm defined in the pricing rule, MF will attmpt to find a price from the pref prov before proceeding with the search for a price from the sec Prov Multifonds DB Column is CORC_2. |
| 8 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED10` | `FsGaFairValueMarketTrigger_Reserved10` | TField |  |  |
| 9 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED9` | `FsGaFairValueMarketTrigger_Reserved9` | TField |  |  |
| 10 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED8` | `FsGaFairValueMarketTrigger_Reserved8` | TField |  |  |
| 11 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED7` | `FsGaFairValueMarketTrigger_Reserved7` | TField |  |  |
| 12 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED6` | `FsGaFairValueMarketTrigger_Reserved6` | TField |  |  |
| 13 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED5` | `FsGaFairValueMarketTrigger_Reserved5` | TField |  |  |
| 14 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED4` | `FsGaFairValueMarketTrigger_Reserved4` | TField |  |  |
| 15 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED3` | `FsGaFairValueMarketTrigger_Reserved3` | TField |  |  |
| 16 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED2` | `FsGaFairValueMarketTrigger_Reserved2` | TField |  |  |
| 17 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RESERVED1` | `FsGaFairValueMarketTrigger_Reserved1` | TField |  |  |
| 18 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.RECORD.STATUS` | `FsGaFairValueMarketTrigger_RecordStatus` | String |  |  |
| 19 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.CURR.NO` | `FsGaFairValueMarketTrigger_CurrNo` | String |  |  |
| 20 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.INPUTTER` | `FsGaFairValueMarketTrigger_Inputter` |  |  |  |
| 21 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.DATE.TIME` | `FsGaFairValueMarketTrigger_DateTime` |  |  |  |
| 22 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.AUTHORISER` | `FsGaFairValueMarketTrigger_Authoriser` | String |  |  |
| 23 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.CO.CODE` | `FsGaFairValueMarketTrigger_CoCode` | String |  |  |
| 24 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.DEPT.CODE` | `FsGaFairValueMarketTrigger_DeptCode` | String |  |  |
| 25 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.AUDITOR.CODE` | `FsGaFairValueMarketTrigger_AuditorCode` | String |  |  |
| 26 | `FS.GA.FAIR.VALUE.MARKET.TRIGGER.AUDIT.DATE.TIME` | `FsGaFairValueMarketTrigger_AuditDateTime` | String |  |  |
