# MDI.DEMAND.INT.RATE.WORK — Table Schema

> Source: `INSERTS/I_F.MDI.DEMAND.INT.RATE.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.DEMAND.INT.ITEM.REQ` | `MdiDemandIntRateWork_ItemReq` |  |  |  |
| 2 | `MDI.DEMAND.INT.ITEM.SENT` | `MdiDemandIntRateWork_ItemSent` |  |  |  |
| 3 | `MDI.DEMAND.INT.MORE.FLAG` | `MdiDemandIntRateWork_MoreFlag` |  |  |  |
| 4 | `MDI.DEMAND.INT.PAN.NO` | `MdiDemandIntRateWork_PanNo` |  |  |  |
| 5 | `MDI.DEMAND.INT.MEMBER.NO` | `MdiDemandIntRateWork_MemberNo` |  |  |  |
| 6 | `MDI.DEMAND.INT.PRODUCT.CATEGORY` | `MdiDemandIntRateWork_ProductCategory` |  |  |  |
| 7 | `MDI.DEMAND.INT.PRODUCT.TYPE` | `MdiDemandIntRateWork_ProductType` |  |  |  |
| 8 | `MDI.DEMAND.INT.PRODUCT.CURRENCY` | `MdiDemandIntRateWork_ProductCurrency` |  |  |  |
| 9 | `MDI.DEMAND.INT.NO.OF.RATES` | `MdiDemandIntRateWork_NoOfRates` |  |  |  |
| 10 | `MDI.DEMAND.INT.MIN.BALANCE` | `MdiDemandIntRateWork_MinBalance` |  |  |  |
| 11 | `MDI.DEMAND.INT.MAX.BALANCE` | `MdiDemandIntRateWork_MaxBalance` |  |  |  |
| 12 | `MDI.DEMAND.INT.INT.CALC.METHOD` | `MdiDemandIntRateWork_IntCalcMethod` |  |  |  |
| 13 | `MDI.DEMAND.INT.OVERDRAFT.RATE` | `MdiDemandIntRateWork_OverdraftRate` |  |  |  |
| 14 | `MDI.DEMAND.INT.LOC.DEL.RATE` | `MdiDemandIntRateWork_LocDelRate` |  |  |  |
| 15 | `MDI.DEMAND.INT.NO.RATE.LEVEL` | `MdiDemandIntRateWork_NoRateLevel` |  |  |  |
| 16 | `MDI.DEMAND.INT.LEVEL.CUTOFF.AMT` | `MdiDemandIntRateWork_LevelCutoffAmt` |  |  |  |
| 17 | `MDI.DEMAND.INT.INTRATE` | `MdiDemandIntRateWork_Intrate` |  |  |  |
| 18 | `MDI.DEMAND.INT.RESERVED.10` | `MdiDemandIntRateWork_Reserved10` |  |  |  |
| 19 | `MDI.DEMAND.INT.RESERVED.9` | `MdiDemandIntRateWork_Reserved9` |  |  |  |
| 20 | `MDI.DEMAND.INT.RESERVED.8` | `MdiDemandIntRateWork_Reserved8` |  |  |  |
| 21 | `MDI.DEMAND.INT.RESERVED.7` | `MdiDemandIntRateWork_Reserved7` |  |  |  |
| 22 | `MDI.DEMAND.INT.RESERVED.6` | `MdiDemandIntRateWork_Reserved6` |  |  |  |
| 23 | `MDI.DEMAND.INT.RESERVED.5` | `MdiDemandIntRateWork_Reserved5` |  |  |  |
| 24 | `MDI.DEMAND.INT.RESERVED.4` | `MdiDemandIntRateWork_Reserved4` |  |  |  |
| 25 | `MDI.DEMAND.INT.RESERVED.3` | `MdiDemandIntRateWork_Reserved3` |  |  |  |
| 26 | `MDI.DEMAND.INT.RESERVED.2` | `MdiDemandIntRateWork_Reserved2` |  |  |  |
| 27 | `MDI.DEMAND.INT.RESERVED.1` | `MdiDemandIntRateWork_Reserved1` |  |  |  |
