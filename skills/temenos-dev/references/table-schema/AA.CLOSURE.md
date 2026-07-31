# AA.CLOSURE — Table Schema

> Source: `INSERTS/I_F.AA.CLOSURE` in `AA_Closure.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CLS.ACTIVITY` | `AaSimClosure_Activity` |  |  |  |
| 2 | `AA.CLS.ACTION` | `AaSimClosure_Action` |  |  |  |
| 3 | `AA.CLS.CLOSURE.TYPE` | `AaSimClosure_ClosureType` |  |  |  |
| 4 | `AA.CLS.CLOSURE.PERIOD` | `AaSimClosure_ClosurePeriod` |  |  |  |
| 5 | `AA.CLS.CLOSURE.METHOD` | `AaSimClosure_ClosureMethod` |  |  |  |
| 6 | `AA.CLS.POSTING.RESTRICT` | `AaSimClosure_PostingRestrict` |  |  |  |
| 7 | `AA.CLS.CLOSURE.ACTIVITY` | `AaSimClosure_ClosureActivity` |  |  |  |
| 8 | `AA.CLS.CLOSE.ONLINE` | `AaSimClosure_CloseOnline` |  |  |  |
| 9 | `AA.CLS.COOLING.PERIOD` | `AaSimClosure_CoolingPeriod` |  |  |  |
| 10 | `AA.CLS.COOLING.DATE.ADJ` | `AaSimClosure_CoolingDateAdj` |  |  |  |
| 11 | `AA.CLS.DEFER.CLOSURE.PERIOD` | `AaSimClosure_DeferClosurePeriod` |  |  |  |
| 12 | `AA.CLS.LOCAL.REF` | `AaSimClosure_LocalRef` |  |  |  |
| 13 | `AA.CLS.PR.ATTRIBUTE` | `AaSimClosure_PrAttribute` |  |  |  |
| 14 | `AA.CLS.PR.VALUE` | `AaSimClosure_PrValue` |  |  |  |
| 15 | `AA.CLS.PR.BRK.RES` | `AaSimClosure_PrBrkRes` |  |  |  |
| 16 | `AA.CLS.PR.BRK.MSG` | `AaSimClosure_PrBrkMsg` |  |  |  |
| 17 | `AA.CLS.PR.BRK.CHARGE` | `AaSimClosure_PrBrkCharge` |  |  |  |
| 18 | `AA.CLS.PR.RESERVED.3` | `AaSimClosure_PrReserved3` |  |  |  |
| 19 | `AA.CLS.PR.RESERVED.2` | `AaSimClosure_PrReserved2` |  |  |  |
| 20 | `AA.CLS.PR.RESERVED.1` | `AaSimClosure_PrReserved1` |  |  |  |
| 21 | `AA.CLS.PR.APP.METHOD` | `AaSimClosure_PrAppMethod` |  |  |  |
| 22 | `AA.CLS.PR.APP.PERIOD` | `AaSimClosure_PrAppPeriod` |  |  |  |
| 23 | `AA.CLS.SYS.RESERVE7` | `AaSimClosure_SysReserve7` |  |  |  |
| 24 | `AA.CLS.SYS.RESERVE6` | `AaSimClosure_SysReserve6` |  |  |  |
| 25 | `AA.CLS.OWNING.COMPANY` | `AaSimClosure_OwningCompany` |  |  |  |
| 26 | `AA.CLS.API.ATTRIBUTE` | `AaSimClosure_ApiAttribute` |  |  |  |
| 27 | `AA.CLS.SYS.RESERVE3` | `AaSimClosure_SysReserve3` |  |  |  |
| 28 | `AA.CLS.SYS.RESERVE2` | `AaSimClosure_SysReserve2` |  |  |  |
| 29 | `AA.CLS.SYS.RESERVE1` | `AaSimClosure_SysReserve1` |  |  |  |
| 30 | `AA.CLS.DEFAULT.ATTR.OPTION` | `AaSimClosure_DefaultAttrOption` |  |  |  |
| 31 | `AA.CLS.DEFAULT.NEGOTIABLE` | `AaSimClosure_DefaultNegotiable` |  |  |  |
| 32 | `AA.CLS.NR.ATTRIBUTE` | `AaSimClosure_NrAttribute` |  |  |  |
| 33 | `AA.CLS.NR.OPTIONS` | `AaSimClosure_NrOptions` |  |  |  |
| 34 | `AA.CLS.NR.ATTRIBUTE.RULE` | `AaSimClosure_NrAttributeRule` |  |  |  |
| 35 | `AA.CLS.NR.VALUE.SOURCE` | `AaSimClosure_NrValueSource` |  |  |  |
| 36 | `AA.CLS.NR.STD.COMP` | `AaSimClosure_NrStdComp` |  |  |  |
| 37 | `AA.CLS.NR.TYPE` | `AaSimClosure_NrType` |  |  |  |
| 38 | `AA.CLS.NR.VALUE` | `AaSimClosure_NrValue` |  |  |  |
| 39 | `AA.CLS.NR.MESSAGE` | `AaSimClosure_NrMessage` |  |  |  |
| 40 | `AA.CLS.CHANGED.FIELDS` | `AaSimClosure_ChangedFields` |  |  |  |
| 41 | `AA.CLS.NEGOTIATED.FLDS` | `AaSimClosure_NegotiatedFlds` |  |  |  |
| 42 | `AA.CLS.ID.COMP.1` | `AaSimClosure_IdComp1` |  |  |  |
| 43 | `AA.CLS.ID.COMP.2` | `AaSimClosure_IdComp2` |  |  |  |
| 44 | `AA.CLS.ID.COMP.3` | `AaSimClosure_IdComp3` |  |  |  |
| 45 | `AA.CLS.ID.COMP.4` | `AaSimClosure_IdComp4` |  |  |  |
| 46 | `AA.CLS.ID.COMP.5` | `AaSimClosure_IdComp5` |  |  |  |
| 47 | `AA.CLS.ID.COMP.6` | `AaSimClosure_IdComp6` |  |  |  |
| 48 | `AA.CLS.RESERVED2.ID` | `AaSimClosure_Reserved2Id` |  |  |  |
| 49 | `AA.CLS.TARGET.PRODUCT` | `AaSimClosure_TargetProduct` |  |  |  |
| 50 | `AA.CLS.STMT.NOS` | `AaSimClosure_StmtNos` |  |  |  |
| 51 | `AA.CLS.OVERRIDE` | `AaSimClosure_Override` |  |  |  |
| 52 | `AA.CLS.RECORD.STATUS` | `AaSimClosure_RecordStatus` |  |  |  |
| 53 | `AA.CLS.CURR.NO` | `AaSimClosure_CurrNo` |  |  |  |
| 54 | `AA.CLS.INPUTTER` | `AaSimClosure_Inputter` |  |  |  |
| 55 | `AA.CLS.DATE.TIME` | `AaSimClosure_DateTime` |  |  |  |
| 56 | `AA.CLS.AUTHORISER` | `AaSimClosure_Authoriser` |  |  |  |
| 57 | `AA.CLS.CO.CODE` | `AaSimClosure_CoCode` |  |  |  |
| 58 | `AA.CLS.DEPT.CODE` | `AaSimClosure_DeptCode` |  |  |  |
| 59 | `AA.CLS.AUDITOR.CODE` | `AaSimClosure_AuditorCode` |  |  |  |
| 60 | `AA.CLS.AUDIT.DATE.TIME` | `AaSimClosure_AuditDateTime` |  |  |  |
| 61 | `AA.CLS.COOLING.WAIVE.CLASS` | `AaSimClosure_CoolingWaiveClass` |  |  |  |
| 62 | `AA.CLS.COOLING.WAIVE.PROP` | `AaSimClosure_CoolingWaiveProp` |  |  |  |
| 63 | `AA.CLS.WAIVE.BILL.TYPE` | `AaSimClosure_WaiveBillType` |  |  |  |
| 64 | `AA.CLS.COOLING.CONVENTION` | `AaSimClosure_CoolingConvention` |  |  |  |
