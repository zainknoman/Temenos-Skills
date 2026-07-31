# FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS — Table Schema

> Source: `INSERTS/I_F.FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.DEALING.COST.GROUP` | `FsGaDealingcostByMrktAssetclss_DealingCostGroup` | TField |  | Refers to the group previously created in CMESS table under DC_GRP table Multifonds DB Column is DC_GROUP. |
| 2 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.MARKET` | `FsGaDealingcostByMrktAssetclss_Market` | TField |  | Refers to the Market defined in screen PRMKT01 (path: Pricing/Parameters/Markets) for which the dealing cost rate requires to be applied Multifonds DB Column is MARKET. |
| 3 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.GTI.CODE` | `FsGaDealingcostByMrktAssetclss_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 4 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.INTERNAL.SECURITY.ID` | `FsGaDealingcostByMrktAssetclss_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.EFFECT.DATE` | `FsGaDealingcostByMrktAssetclss_EffectDate` | TField |  | Effective Date Multifonds DB Column is EFFECTIVE_DATE. |
| 6 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.BID.PERCENTAGE` | `FsGaDealingcostByMrktAssetclss_BidPercentage` | TField |  | Refers to the BID rate to be applied Multifonds DB Column is BID_PCT. |
| 7 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.OFFER.PERCENTAGE` | `FsGaDealingcostByMrktAssetclss_OfferPercentage` | TField |  | Refers to the Offer rate to be applied Multifonds DB Column is OFFER_PCT. |
| 8 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.RECORD.STATUS` | `FsGaDealingcostByMrktAssetclss_RecordStatus` | String |  |  |
| 9 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.CURR.NO` | `FsGaDealingcostByMrktAssetclss_CurrNo` | String |  |  |
| 10 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.INPUTTER` | `FsGaDealingcostByMrktAssetclss_Inputter` |  |  |  |
| 11 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.DATE.TIME` | `FsGaDealingcostByMrktAssetclss_DateTime` |  |  |  |
| 12 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.AUTHORISER` | `FsGaDealingcostByMrktAssetclss_Authoriser` | String |  |  |
| 13 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.CO.CODE` | `FsGaDealingcostByMrktAssetclss_CoCode` | String |  |  |
| 14 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.DEPT.CODE` | `FsGaDealingcostByMrktAssetclss_DeptCode` | String |  |  |
| 15 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.AUDITOR.CODE` | `FsGaDealingcostByMrktAssetclss_AuditorCode` | String |  |  |
| 16 | `FS.GA.DEALINGCOST.BY.MRKT.ASSETCLSS.AUDIT.DATE.TIME` | `FsGaDealingcostByMrktAssetclss_AuditDateTime` | String |  |  |
