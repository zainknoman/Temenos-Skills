# GET.INT.RATE.WORK — Table Schema

> Source: `INSERTS/I_F.GET.INT.RATE.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.INT.RATE.ITEM.REQ` | `GetIntRateWork_ItemReq` |  |  |  |
| 2 | `MDI.INT.RATE.ITEM.SENT` | `GetIntRateWork_ItemSent` |  |  |  |
| 3 | `MDI.INT.RATE.MORE.FLAG` | `GetIntRateWork_MoreFlag` |  |  |  |
| 4 | `MDI.INT.RATE.PAN.NO` | `GetIntRateWork_PanNo` |  |  |  |
| 5 | `MDI.INT.RATE.MEMBER.NO` | `GetIntRateWork_MemberNo` |  |  |  |
| 6 | `MDI.INT.RATE.PRODUCT.CATEGORY` | `GetIntRateWork_ProductCategory` |  |  |  |
| 7 | `MDI.INT.RATE.PRODUCT.TYPE` | `GetIntRateWork_ProductType` |  |  |  |
| 8 | `MDI.INT.RATE.PRODUCT.CURRENCY` | `GetIntRateWork_ProductCurrency` |  |  |  |
| 9 | `MDI.INT.RATE.NO.OF.RATES` | `GetIntRateWork_NoOfRates` |  |  |  |
| 10 | `MDI.INT.RATE.MIN.BALANCE` | `GetIntRateWork_MinBalance` |  |  |  |
| 11 | `MDI.INT.RATE.MAX.BALANCE` | `GetIntRateWork_MaxBalance` |  |  |  |
| 12 | `MDI.INT.RATE.INT.CALC.METHOD` | `GetIntRateWork_IntCalcMethod` |  |  |  |
| 13 | `MDI.INT.RATE.OVERDRAFT.RATE` | `GetIntRateWork_OverdraftRate` |  |  |  |
| 14 | `MDI.INT.RATE.LOC.DEL.RATE` | `GetIntRateWork_LocDelRate` |  |  |  |
| 15 | `MDI.INT.RATE.REDEM.IND` | `GetIntRateWork_RedemInd` |  |  |  |
| 16 | `MDI.INT.RATE.MIN.LENGTH` | `GetIntRateWork_MinLength` |  |  |  |
| 17 | `MDI.INT.RATE.MIN.FREQ` | `GetIntRateWork_MinFreq` |  |  |  |
| 18 | `MDI.INT.RATE.LEVEL.CUTOFF` | `GetIntRateWork_LevelCutoff` |  |  |  |
| 19 | `MDI.INT.RATE.NO.RATE.LEVEL` | `GetIntRateWork_NoRateLevel` |  |  |  |
| 20 | `MDI.INT.RATE.LEVEL.CUTOFF.AMT` | `GetIntRateWork_LevelCutoffAmt` |  |  |  |
| 21 | `MDI.INT.RATE.INTRATE` | `GetIntRateWork_Intrate` |  |  |  |
| 22 | `MDI.INT.RATE.LENGTH` | `GetIntRateWork_Length` |  |  |  |
| 23 | `MDI.INT.RATE.FREQ` | `GetIntRateWork_Freq` |  |  |  |
| 24 | `MDI.INT.RATE.RESERVED.10` | `GetIntRateWork_Reserved10` |  |  |  |
| 25 | `MDI.INT.RATE.RESERVED.9` | `GetIntRateWork_Reserved9` |  |  |  |
| 26 | `MDI.INT.RATE.RESERVED.8` | `GetIntRateWork_Reserved8` |  |  |  |
| 27 | `MDI.INT.RATE.RESERVED.7` | `GetIntRateWork_Reserved7` |  |  |  |
| 28 | `MDI.INT.RATE.RESERVED.6` | `GetIntRateWork_Reserved6` |  |  |  |
| 29 | `MDI.INT.RATE.RESERVED.5` | `GetIntRateWork_Reserved5` |  |  |  |
| 30 | `MDI.INT.RATE.RESERVED.4` | `GetIntRateWork_Reserved4` |  |  |  |
| 31 | `MDI.INT.RATE.RESERVED.3` | `GetIntRateWork_Reserved3` |  |  |  |
| 32 | `MDI.INT.RATE.RESERVED.2` | `GetIntRateWork_Reserved2` |  |  |  |
| 33 | `MDI.INT.RATE.RESERVED.1` | `GetIntRateWork_Reserved1` |  |  |  |
| 34 | `MDI.INT.RATE.LOCAL.REF` | `GetIntRateWork_LocalRef` |  |  |  |
| 35 | `MDI.INT.RATE.OVERRIDE` | `GetIntRateWork_Override` |  |  |  |
