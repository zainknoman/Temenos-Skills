# AA.SUB.ARRANGEMENT.RULES — Table Schema

> Source: `INSERTS/I_F.AA.SUB.ARRANGEMENT.RULES` in `AA_SubArrangementRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SAR.ACTIVITY` | `AaSimSubArrangementRules_Activity` |  |  |  |
| 2 | `AA.SAR.ACTION` | `AaSimSubArrangementRules_Action` |  |  |  |
| 3 | `AA.SAR.CUSTOMER` | `AaSimSubArrangementRules_Customer` |  |  |  |
| 4 | `AA.SAR.REQUIRED.CUSTOMER` | `AaSimSubArrangementRules_RequiredCustomer` |  |  |  |
| 5 | `AA.SAR.ALLOWED.CUSTOMER` | `AaSimSubArrangementRules_AllowedCustomer` |  |  |  |
| 6 | `AA.SAR.ALLOWED.ARR.PER.CCY` | `AaSimSubArrangementRules_AllowedArrPerCcy` |  |  |  |
| 7 | `AA.SAR.BASE.CCY.PRODUCT` | `AaSimSubArrangementRules_BaseCcyProduct` |  |  |  |
| 8 | `AA.SAR.CURRENCY` | `AaSimSubArrangementRules_Currency` |  |  |  |
| 9 | `AA.SAR.ALLOWED.CURRENCY` | `AaSimSubArrangementRules_AllowedCurrency` |  |  |  |
| 10 | `AA.SAR.RESERVED.3` | `AaSimSubArrangementRules_Reserved3` |  |  |  |
| 11 | `AA.SAR.RESERVED.4` | `AaSimSubArrangementRules_Reserved4` |  |  |  |
| 12 | `AA.SAR.PRODUCT` | `AaSimSubArrangementRules_Product` |  |  |  |
| 13 | `AA.SAR.ALLOWED.PRD.GROUP` | `AaSimSubArrangementRules_AllowedPrdGroup` |  |  |  |
| 14 | `AA.SAR.ALLOWED.PRODUCT` | `AaSimSubArrangementRules_AllowedProduct` |  |  |  |
| 15 | `AA.SAR.RESERVED.5` | `AaSimSubArrangementRules_Reserved5` |  |  |  |
| 16 | `AA.SAR.RESERVED.6` | `AaSimSubArrangementRules_Reserved6` |  |  |  |
| 17 | `AA.SAR.TERM.RECALCULATION` | `AaSimSubArrangementRules_TermRecalculation` |  |  |  |
| 18 | `AA.SAR.RESERVED.7` | `AaSimSubArrangementRules_Reserved7` |  |  |  |
| 19 | `AA.SAR.RESERVED.8` | `AaSimSubArrangementRules_Reserved8` |  |  |  |
| 20 | `AA.SAR.CURRENCY.MARKET` | `AaSimSubArrangementRules_CurrencyMarket` |  |  |  |
| 21 | `AA.SAR.EXCH.RATE.TYPE` | `AaSimSubArrangementRules_ExchRateType` |  |  |  |
| 22 | `AA.SAR.RESERVED.11` | `AaSimSubArrangementRules_Reserved11` |  |  |  |
| 23 | `AA.SAR.RESERVED.12` | `AaSimSubArrangementRules_Reserved12` |  |  |  |
| 24 | `AA.SAR.RESERVED.13` | `AaSimSubArrangementRules_Reserved13` |  |  |  |
| 25 | `AA.SAR.RESERVED.14` | `AaSimSubArrangementRules_Reserved14` |  |  |  |
| 26 | `AA.SAR.RESERVED.15` | `AaSimSubArrangementRules_Reserved15` |  |  |  |
| 27 | `AA.SAR.RESERVED.16` | `AaSimSubArrangementRules_Reserved16` |  |  |  |
| 28 | `AA.SAR.LOCAL.REF` | `AaSimSubArrangementRules_LocalRef` |  |  |  |
| 29 | `AA.SAR.PR.ATTRIBUTE` | `AaSimSubArrangementRules_PrAttribute` |  |  |  |
| 30 | `AA.SAR.PR.VALUE` | `AaSimSubArrangementRules_PrValue` |  |  |  |
| 31 | `AA.SAR.PR.BRK.RES` | `AaSimSubArrangementRules_PrBrkRes` |  |  |  |
| 32 | `AA.SAR.PR.BRK.MSG` | `AaSimSubArrangementRules_PrBrkMsg` |  |  |  |
| 33 | `AA.SAR.PR.BRK.CHARGE` | `AaSimSubArrangementRules_PrBrkCharge` |  |  |  |
| 34 | `AA.SAR.PR.RESERVED.3` | `AaSimSubArrangementRules_PrReserved3` |  |  |  |
| 35 | `AA.SAR.PR.RESERVED.2` | `AaSimSubArrangementRules_PrReserved2` |  |  |  |
| 36 | `AA.SAR.PR.RESERVED.1` | `AaSimSubArrangementRules_PrReserved1` |  |  |  |
| 37 | `AA.SAR.PR.APP.METHOD` | `AaSimSubArrangementRules_PrAppMethod` |  |  |  |
| 38 | `AA.SAR.PR.APP.PERIOD` | `AaSimSubArrangementRules_PrAppPeriod` |  |  |  |
| 39 | `AA.SAR.SYS.RESERVE7` | `AaSimSubArrangementRules_SysReserve7` |  |  |  |
| 40 | `AA.SAR.SYS.RESERVE6` | `AaSimSubArrangementRules_SysReserve6` |  |  |  |
| 41 | `AA.SAR.OWNING.COMPANY` | `AaSimSubArrangementRules_OwningCompany` |  |  |  |
| 42 | `AA.SAR.API.ATTRIBUTE` | `AaSimSubArrangementRules_ApiAttribute` |  |  |  |
| 43 | `AA.SAR.SYS.RESERVE3` | `AaSimSubArrangementRules_SysReserve3` |  |  |  |
| 44 | `AA.SAR.SYS.RESERVE2` | `AaSimSubArrangementRules_SysReserve2` |  |  |  |
| 45 | `AA.SAR.SYS.RESERVE1` | `AaSimSubArrangementRules_SysReserve1` |  |  |  |
| 46 | `AA.SAR.DEFAULT.ATTR.OPTION` | `AaSimSubArrangementRules_DefaultAttrOption` |  |  |  |
| 47 | `AA.SAR.DEFAULT.NEGOTIABLE` | `AaSimSubArrangementRules_DefaultNegotiable` |  |  |  |
| 48 | `AA.SAR.NR.ATTRIBUTE` | `AaSimSubArrangementRules_NrAttribute` |  |  |  |
| 49 | `AA.SAR.NR.OPTIONS` | `AaSimSubArrangementRules_NrOptions` |  |  |  |
| 50 | `AA.SAR.NR.ATTRIBUTE.RULE` | `AaSimSubArrangementRules_NrAttributeRule` |  |  |  |
| 51 | `AA.SAR.NR.VALUE.SOURCE` | `AaSimSubArrangementRules_NrValueSource` |  |  |  |
| 52 | `AA.SAR.NR.STD.COMP` | `AaSimSubArrangementRules_NrStdComp` |  |  |  |
| 53 | `AA.SAR.NR.TYPE` | `AaSimSubArrangementRules_NrType` |  |  |  |
| 54 | `AA.SAR.NR.VALUE` | `AaSimSubArrangementRules_NrValue` |  |  |  |
| 55 | `AA.SAR.NR.MESSAGE` | `AaSimSubArrangementRules_NrMessage` |  |  |  |
| 56 | `AA.SAR.CHANGED.FIELDS` | `AaSimSubArrangementRules_ChangedFields` |  |  |  |
| 57 | `AA.SAR.NEGOTIATED.FLDS` | `AaSimSubArrangementRules_NegotiatedFlds` |  |  |  |
| 58 | `AA.SAR.ID.COMP.1` | `AaSimSubArrangementRules_IdComp1` |  |  |  |
| 59 | `AA.SAR.ID.COMP.2` | `AaSimSubArrangementRules_IdComp2` |  |  |  |
| 60 | `AA.SAR.ID.COMP.3` | `AaSimSubArrangementRules_IdComp3` |  |  |  |
| 61 | `AA.SAR.ID.COMP.4` | `AaSimSubArrangementRules_IdComp4` |  |  |  |
| 62 | `AA.SAR.ID.COMP.5` | `AaSimSubArrangementRules_IdComp5` |  |  |  |
| 63 | `AA.SAR.ID.COMP.6` | `AaSimSubArrangementRules_IdComp6` |  |  |  |
| 64 | `AA.SAR.RESERVED2.ID` | `AaSimSubArrangementRules_Reserved2Id` |  |  |  |
| 65 | `AA.SAR.TARGET.PRODUCT` | `AaSimSubArrangementRules_TargetProduct` |  |  |  |
| 66 | `AA.SAR.STMT.NOS` | `AaSimSubArrangementRules_StmtNos` |  |  |  |
| 67 | `AA.SAR.OVERRIDE` | `AaSimSubArrangementRules_Override` |  |  |  |
| 68 | `AA.SAR.RECORD.STATUS` | `AaSimSubArrangementRules_RecordStatus` |  |  |  |
| 69 | `AA.SAR.CURR.NO` | `AaSimSubArrangementRules_CurrNo` |  |  |  |
| 70 | `AA.SAR.INPUTTER` | `AaSimSubArrangementRules_Inputter` |  |  |  |
| 71 | `AA.SAR.DATE.TIME` | `AaSimSubArrangementRules_DateTime` |  |  |  |
| 72 | `AA.SAR.AUTHORISER` | `AaSimSubArrangementRules_Authoriser` |  |  |  |
| 73 | `AA.SAR.CO.CODE` | `AaSimSubArrangementRules_CoCode` |  |  |  |
| 74 | `AA.SAR.DEPT.CODE` | `AaSimSubArrangementRules_DeptCode` |  |  |  |
| 75 | `AA.SAR.AUDITOR.CODE` | `AaSimSubArrangementRules_AuditorCode` |  |  |  |
| 76 | `AA.SAR.AUDIT.DATE.TIME` | `AaSimSubArrangementRules_AuditDateTime` |  |  |  |
