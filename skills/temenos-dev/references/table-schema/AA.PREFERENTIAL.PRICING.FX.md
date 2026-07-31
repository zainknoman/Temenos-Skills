# AA.PREFERENTIAL.PRICING.FX — Table Schema

> Source: `INSERTS/I_F.AA.PREFERENTIAL.PRICING.FX` in `AA_PreferentialPricingFx.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.FX.ACTIVITY` | `AaSimPreferentialPricingFx_Activity` |  |  |  |
| 2 | `AA.FX.ACTION` | `AaSimPreferentialPricingFx_Action` |  |  |  |
| 3 | `AA.FX.RATE.TYPE` | `AaSimPreferentialPricingFx_RateType` |  |  |  |
| 4 | `AA.FX.CURRENCY1` | `AaSimPreferentialPricingFx_Currency1` |  |  |  |
| 5 | `AA.FX.CURRENCY2` | `AaSimPreferentialPricingFx_Currency2` |  |  |  |
| 6 | `AA.FX.CURRENCY.PAIR` | `AaSimPreferentialPricingFx_CurrencyPair` |  |  |  |
| 7 | `AA.FX.BUY.RATE` | `AaSimPreferentialPricingFx_BuyRate` |  |  |  |
| 8 | `AA.FX.SELL.RATE` | `AaSimPreferentialPricingFx_SellRate` |  |  |  |
| 9 | `AA.FX.MID.RATE` | `AaSimPreferentialPricingFx_MidRate` |  |  |  |
| 10 | `AA.FX.SPREAD` | `AaSimPreferentialPricingFx_Spread` |  |  |  |
| 11 | `AA.FX.RESERVED.5` | `AaSimPreferentialPricingFx_Reserved5` |  |  |  |
| 12 | `AA.FX.RESERVED.4` | `AaSimPreferentialPricingFx_Reserved4` |  |  |  |
| 13 | `AA.FX.RESERVED.3` | `AaSimPreferentialPricingFx_Reserved3` |  |  |  |
| 14 | `AA.FX.RESERVED.2` | `AaSimPreferentialPricingFx_Reserved2` |  |  |  |
| 15 | `AA.FX.RESERVED.1` | `AaSimPreferentialPricingFx_Reserved1` |  |  |  |
| 16 | `AA.FX.LOCAL.REF` | `AaSimPreferentialPricingFx_LocalRef` |  |  |  |
| 17 | `AA.FX.PR.ATTRIBUTE` | `AaSimPreferentialPricingFx_PrAttribute` |  |  |  |
| 18 | `AA.FX.PR.VALUE` | `AaSimPreferentialPricingFx_PrValue` |  |  |  |
| 19 | `AA.FX.PR.BRK.RES` | `AaSimPreferentialPricingFx_PrBrkRes` |  |  |  |
| 20 | `AA.FX.PR.BRK.MSG` | `AaSimPreferentialPricingFx_PrBrkMsg` |  |  |  |
| 21 | `AA.FX.PR.BRK.CHARGE` | `AaSimPreferentialPricingFx_PrBrkCharge` |  |  |  |
| 22 | `AA.FX.PR.RESERVED.3` | `AaSimPreferentialPricingFx_PrReserved3` |  |  |  |
| 23 | `AA.FX.PR.RESERVED.2` | `AaSimPreferentialPricingFx_PrReserved2` |  |  |  |
| 24 | `AA.FX.PR.RESERVED.1` | `AaSimPreferentialPricingFx_PrReserved1` |  |  |  |
| 25 | `AA.FX.PR.APP.METHOD` | `AaSimPreferentialPricingFx_PrAppMethod` |  |  |  |
| 26 | `AA.FX.PR.APP.PERIOD` | `AaSimPreferentialPricingFx_PrAppPeriod` |  |  |  |
| 27 | `AA.FX.SYS.RESERVE7` | `AaSimPreferentialPricingFx_SysReserve7` |  |  |  |
| 28 | `AA.FX.SYS.RESERVE6` | `AaSimPreferentialPricingFx_SysReserve6` |  |  |  |
| 29 | `AA.FX.OWNING.COMPANY` | `AaSimPreferentialPricingFx_OwningCompany` |  |  |  |
| 30 | `AA.FX.API.ATTRIBUTE` | `AaSimPreferentialPricingFx_ApiAttribute` |  |  |  |
| 31 | `AA.FX.SYS.RESERVE3` | `AaSimPreferentialPricingFx_SysReserve3` |  |  |  |
| 32 | `AA.FX.SYS.RESERVE2` | `AaSimPreferentialPricingFx_SysReserve2` |  |  |  |
| 33 | `AA.FX.SYS.RESERVE1` | `AaSimPreferentialPricingFx_SysReserve1` |  |  |  |
| 34 | `AA.FX.DEFAULT.ATTR.OPTION` | `AaSimPreferentialPricingFx_DefaultAttrOption` |  |  |  |
| 35 | `AA.FX.DEFAULT.NEGOTIABLE` | `AaSimPreferentialPricingFx_DefaultNegotiable` |  |  |  |
| 36 | `AA.FX.NR.ATTRIBUTE` | `AaSimPreferentialPricingFx_NrAttribute` |  |  |  |
| 37 | `AA.FX.NR.OPTIONS` | `AaSimPreferentialPricingFx_NrOptions` |  |  |  |
| 38 | `AA.FX.NR.ATTRIBUTE.RULE` | `AaSimPreferentialPricingFx_NrAttributeRule` |  |  |  |
| 39 | `AA.FX.NR.VALUE.SOURCE` | `AaSimPreferentialPricingFx_NrValueSource` |  |  |  |
| 40 | `AA.FX.NR.STD.COMP` | `AaSimPreferentialPricingFx_NrStdComp` |  |  |  |
| 41 | `AA.FX.NR.TYPE` | `AaSimPreferentialPricingFx_NrType` |  |  |  |
| 42 | `AA.FX.NR.VALUE` | `AaSimPreferentialPricingFx_NrValue` |  |  |  |
| 43 | `AA.FX.NR.MESSAGE` | `AaSimPreferentialPricingFx_NrMessage` |  |  |  |
| 44 | `AA.FX.CHANGED.FIELDS` | `AaSimPreferentialPricingFx_ChangedFields` |  |  |  |
| 45 | `AA.FX.NEGOTIATED.FLDS` | `AaSimPreferentialPricingFx_NegotiatedFlds` |  |  |  |
| 46 | `AA.FX.ID.COMP.1` | `AaSimPreferentialPricingFx_IdComp1` |  |  |  |
| 47 | `AA.FX.ID.COMP.2` | `AaSimPreferentialPricingFx_IdComp2` |  |  |  |
| 48 | `AA.FX.ID.COMP.3` | `AaSimPreferentialPricingFx_IdComp3` |  |  |  |
| 49 | `AA.FX.ID.COMP.4` | `AaSimPreferentialPricingFx_IdComp4` |  |  |  |
| 50 | `AA.FX.ID.COMP.5` | `AaSimPreferentialPricingFx_IdComp5` |  |  |  |
| 51 | `AA.FX.ID.COMP.6` | `AaSimPreferentialPricingFx_IdComp6` |  |  |  |
| 52 | `AA.FX.RESERVED2.ID` | `AaSimPreferentialPricingFx_Reserved2Id` |  |  |  |
| 53 | `AA.FX.TARGET.PRODUCT` | `AaSimPreferentialPricingFx_TargetProduct` |  |  |  |
| 54 | `AA.FX.STMT.NOS` | `AaSimPreferentialPricingFx_StmtNos` |  |  |  |
| 55 | `AA.FX.OVERRIDE` | `AaSimPreferentialPricingFx_Override` |  |  |  |
| 56 | `AA.FX.RECORD.STATUS` | `AaSimPreferentialPricingFx_RecordStatus` |  |  |  |
| 57 | `AA.FX.CURR.NO` | `AaSimPreferentialPricingFx_CurrNo` |  |  |  |
| 58 | `AA.FX.INPUTTER` | `AaSimPreferentialPricingFx_Inputter` |  |  |  |
| 59 | `AA.FX.DATE.TIME` | `AaSimPreferentialPricingFx_DateTime` |  |  |  |
| 60 | `AA.FX.AUTHORISER` | `AaSimPreferentialPricingFx_Authoriser` |  |  |  |
| 61 | `AA.FX.CO.CODE` | `AaSimPreferentialPricingFx_CoCode` |  |  |  |
| 62 | `AA.FX.DEPT.CODE` | `AaSimPreferentialPricingFx_DeptCode` |  |  |  |
| 63 | `AA.FX.AUDITOR.CODE` | `AaSimPreferentialPricingFx_AuditorCode` |  |  |  |
| 64 | `AA.FX.AUDIT.DATE.TIME` | `AaSimPreferentialPricingFx_AuditDateTime` |  |  |  |
