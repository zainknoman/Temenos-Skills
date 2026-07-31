# AA.EXCHANGE.RATE — Table Schema

> Source: `INSERTS/I_F.AA.EXCHANGE.RATE` in `AA_ExchangeRate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.EXC.ACTIVITY` | `AaSimExchangeRate_Activity` |  |  |  |
| 2 | `AA.EXC.ACTION` | `AaSimExchangeRate_Action` |  |  |  |
| 3 | `AA.EXC.EXCHANGE.RATE` | `AaSimExchangeRate_ExchangeRate` |  |  |  |
| 4 | `AA.EXC.PRIOR.DAYS` | `AaSimExchangeRate_PriorDays` |  |  |  |
| 5 | `AA.EXC.INITIATION.TYPE` | `AaSimExchangeRate_InitiationType` |  |  |  |
| 6 | `AA.EXC.EXCH.TOLERANCE.PERC` | `AaSimExchangeRate_ExchTolerancePerc` |  |  |  |
| 7 | `AA.EXC.EXCH.TOLERANCE.VALUE` | `AaSimExchangeRate_ExchToleranceValue` |  |  |  |
| 8 | `AA.EXC.RESERVED.18` | `AaSimExchangeRate_Reserved18` |  |  |  |
| 9 | `AA.EXC.RESERVED.17` | `AaSimExchangeRate_Reserved17` |  |  |  |
| 10 | `AA.EXC.RESERVED.16` | `AaSimExchangeRate_Reserved16` |  |  |  |
| 11 | `AA.EXC.ON.ACTIVITY` | `AaSimExchangeRate_OnActivity` |  |  |  |
| 12 | `AA.EXC.RECALCULATE` | `AaSimExchangeRate_Recalculate` |  |  |  |
| 13 | `AA.EXC.RESERVED.15` | `AaSimExchangeRate_Reserved15` |  |  |  |
| 14 | `AA.EXC.RESERVED.14` | `AaSimExchangeRate_Reserved14` |  |  |  |
| 15 | `AA.EXC.RESERVED.13` | `AaSimExchangeRate_Reserved13` |  |  |  |
| 16 | `AA.EXC.RESERVED.12` | `AaSimExchangeRate_Reserved12` |  |  |  |
| 17 | `AA.EXC.RESERVED.11` | `AaSimExchangeRate_Reserved11` |  |  |  |
| 18 | `AA.EXC.RESERVED.10` | `AaSimExchangeRate_Reserved10` |  |  |  |
| 19 | `AA.EXC.RESERVED.9` | `AaSimExchangeRate_Reserved9` |  |  |  |
| 20 | `AA.EXC.RESERVED.8` | `AaSimExchangeRate_Reserved8` |  |  |  |
| 21 | `AA.EXC.RESERVED.7` | `AaSimExchangeRate_Reserved7` |  |  |  |
| 22 | `AA.EXC.RESERVED.6` | `AaSimExchangeRate_Reserved6` |  |  |  |
| 23 | `AA.EXC.RESERVED.5` | `AaSimExchangeRate_Reserved5` |  |  |  |
| 24 | `AA.EXC.RESERVED.4` | `AaSimExchangeRate_Reserved4` |  |  |  |
| 25 | `AA.EXC.RESERVED.3` | `AaSimExchangeRate_Reserved3` |  |  |  |
| 26 | `AA.EXC.RESERVED.2` | `AaSimExchangeRate_Reserved2` |  |  |  |
| 27 | `AA.EXC.RESERVED.1` | `AaSimExchangeRate_Reserved1` |  |  |  |
| 28 | `AA.EXC.LOCAL.REF` | `AaSimExchangeRate_LocalRef` |  |  |  |
| 29 | `AA.EXC.PR.ATTRIBUTE` | `AaSimExchangeRate_PrAttribute` |  |  |  |
| 30 | `AA.EXC.PR.VALUE` | `AaSimExchangeRate_PrValue` |  |  |  |
| 31 | `AA.EXC.PR.BRK.RES` | `AaSimExchangeRate_PrBrkRes` |  |  |  |
| 32 | `AA.EXC.PR.BRK.MSG` | `AaSimExchangeRate_PrBrkMsg` |  |  |  |
| 33 | `AA.EXC.PR.BRK.CHARGE` | `AaSimExchangeRate_PrBrkCharge` |  |  |  |
| 34 | `AA.EXC.PR.RESERVED.3` | `AaSimExchangeRate_PrReserved3` |  |  |  |
| 35 | `AA.EXC.PR.RESERVED.2` | `AaSimExchangeRate_PrReserved2` |  |  |  |
| 36 | `AA.EXC.PR.RESERVED.1` | `AaSimExchangeRate_PrReserved1` |  |  |  |
| 37 | `AA.EXC.PR.APP.METHOD` | `AaSimExchangeRate_PrAppMethod` |  |  |  |
| 38 | `AA.EXC.PR.APP.PERIOD` | `AaSimExchangeRate_PrAppPeriod` |  |  |  |
| 39 | `AA.EXC.SYS.RESERVE7` | `AaSimExchangeRate_SysReserve7` |  |  |  |
| 40 | `AA.EXC.SYS.RESERVE6` | `AaSimExchangeRate_SysReserve6` |  |  |  |
| 41 | `AA.EXC.OWNING.COMPANY` | `AaSimExchangeRate_OwningCompany` |  |  |  |
| 42 | `AA.EXC.API.ATTRIBUTE` | `AaSimExchangeRate_ApiAttribute` |  |  |  |
| 43 | `AA.EXC.SYS.RESERVE3` | `AaSimExchangeRate_SysReserve3` |  |  |  |
| 44 | `AA.EXC.SYS.RESERVE2` | `AaSimExchangeRate_SysReserve2` |  |  |  |
| 45 | `AA.EXC.SYS.RESERVE1` | `AaSimExchangeRate_SysReserve1` |  |  |  |
| 46 | `AA.EXC.DEFAULT.ATTR.OPTION` | `AaSimExchangeRate_DefaultAttrOption` |  |  |  |
| 47 | `AA.EXC.DEFAULT.NEGOTIABLE` | `AaSimExchangeRate_DefaultNegotiable` |  |  |  |
| 48 | `AA.EXC.NR.ATTRIBUTE` | `AaSimExchangeRate_NrAttribute` |  |  |  |
| 49 | `AA.EXC.NR.OPTIONS` | `AaSimExchangeRate_NrOptions` |  |  |  |
| 50 | `AA.EXC.NR.ATTRIBUTE.RULE` | `AaSimExchangeRate_NrAttributeRule` |  |  |  |
| 51 | `AA.EXC.NR.VALUE.SOURCE` | `AaSimExchangeRate_NrValueSource` |  |  |  |
| 52 | `AA.EXC.NR.STD.COMP` | `AaSimExchangeRate_NrStdComp` |  |  |  |
| 53 | `AA.EXC.NR.TYPE` | `AaSimExchangeRate_NrType` |  |  |  |
| 54 | `AA.EXC.NR.VALUE` | `AaSimExchangeRate_NrValue` |  |  |  |
| 55 | `AA.EXC.NR.MESSAGE` | `AaSimExchangeRate_NrMessage` |  |  |  |
| 56 | `AA.EXC.CHANGED.FIELDS` | `AaSimExchangeRate_ChangedFields` |  |  |  |
| 57 | `AA.EXC.NEGOTIATED.FLDS` | `AaSimExchangeRate_NegotiatedFlds` |  |  |  |
| 58 | `AA.EXC.ID.COMP.1` | `AaSimExchangeRate_IdComp1` |  |  |  |
| 59 | `AA.EXC.ID.COMP.2` | `AaSimExchangeRate_IdComp2` |  |  |  |
| 60 | `AA.EXC.ID.COMP.3` | `AaSimExchangeRate_IdComp3` |  |  |  |
| 61 | `AA.EXC.ID.COMP.4` | `AaSimExchangeRate_IdComp4` |  |  |  |
| 62 | `AA.EXC.ID.COMP.5` | `AaSimExchangeRate_IdComp5` |  |  |  |
| 63 | `AA.EXC.ID.COMP.6` | `AaSimExchangeRate_IdComp6` |  |  |  |
| 64 | `AA.EXC.RESERVED2.ID` | `AaSimExchangeRate_Reserved2Id` |  |  |  |
| 65 | `AA.EXC.TARGET.PRODUCT` | `AaSimExchangeRate_TargetProduct` |  |  |  |
| 66 | `AA.EXC.STMT.NOS` | `AaSimExchangeRate_StmtNos` |  |  |  |
| 67 | `AA.EXC.OVERRIDE` | `AaSimExchangeRate_Override` |  |  |  |
| 68 | `AA.EXC.RECORD.STATUS` | `AaSimExchangeRate_RecordStatus` |  |  |  |
| 69 | `AA.EXC.CURR.NO` | `AaSimExchangeRate_CurrNo` |  |  |  |
| 70 | `AA.EXC.INPUTTER` | `AaSimExchangeRate_Inputter` |  |  |  |
| 71 | `AA.EXC.DATE.TIME` | `AaSimExchangeRate_DateTime` |  |  |  |
| 72 | `AA.EXC.AUTHORISER` | `AaSimExchangeRate_Authoriser` |  |  |  |
| 73 | `AA.EXC.CO.CODE` | `AaSimExchangeRate_CoCode` |  |  |  |
| 74 | `AA.EXC.DEPT.CODE` | `AaSimExchangeRate_DeptCode` |  |  |  |
| 75 | `AA.EXC.AUDITOR.CODE` | `AaSimExchangeRate_AuditorCode` |  |  |  |
| 76 | `AA.EXC.AUDIT.DATE.TIME` | `AaSimExchangeRate_AuditDateTime` |  |  |  |
