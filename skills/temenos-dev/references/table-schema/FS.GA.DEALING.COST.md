# FS.GA.DEALING.COST — Table Schema

> Source: `INSERTS/I_F.FS.GA.DEALING.COST` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEALING.COST.DEALING.COST.GROUP` | `FsGaDealingCost_DealingCostGroup` | TField |  | Dealing Cost Group Multifonds DB Column is DC_GROUP. |
| 2 | `DEALING.COST.MARKET` | `FsGaDealingCost_Market` | TField |  | Market Multifonds DB Column is MARKET. |
| 3 | `DEALING.COST.SECURITY.TYPE` | `FsGaDealingCost_SecurityType` | TField |  | Security type Multifonds DB Column is CGTI. |
| 4 | `DEALING.COST.INTERNAL.SECURITY.ID` | `FsGaDealingCost_SecurityId` |  |  |  |
| 5 | `DEALING.COST.EFFECTIVE.DATE` | `FsGaDealingCost_EffectiveDate` | TField |  | Effective Date Multifonds DB Column is EFFECTIVE_DATE. |
| 6 | `DEALING.COST.BID.PERCENT` | `FsGaDealingCost_BidPercent` | TField |  | Bid Percent Multifonds DB Column is BID_PCT. |
| 7 | `DEALING.COST.OFFER.PERCENT` | `FsGaDealingCost_OfferPercent` | TField |  | Offer Percent Multifonds DB Column is OFFER_PCT. |
| 8 | `DEALING.COST.RECORD.STATUS` | `FsGaDealingCost_RecordStatus` | String |  |  |
| 9 | `DEALING.COST.CURR.NO` | `FsGaDealingCost_CurrNo` | String |  |  |
| 10 | `DEALING.COST.INPUTTER` | `FsGaDealingCost_Inputter` |  |  |  |
| 11 | `DEALING.COST.DATE.TIME` | `FsGaDealingCost_DateTime` |  |  |  |
| 12 | `DEALING.COST.AUTHORISER` | `FsGaDealingCost_Authoriser` | String |  |  |
| 13 | `DEALING.COST.CO.CODE` | `FsGaDealingCost_CoCode` | String |  |  |
| 14 | `DEALING.COST.DEPT.CODE` | `FsGaDealingCost_DeptCode` | String |  |  |
| 15 | `DEALING.COST.AUDITOR.CODE` | `FsGaDealingCost_AuditorCode` | String |  |  |
| 16 | `DEALING.COST.AUDIT.DATE.TIME` | `FsGaDealingCost_AuditDateTime` | String |  |  |
