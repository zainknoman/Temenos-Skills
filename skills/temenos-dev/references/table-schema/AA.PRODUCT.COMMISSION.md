# AA.PRODUCT.COMMISSION — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.COMMISSION` in `AA_ProductCommission.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PROD.COMM.ACTIVITY` | `AaSimProductCommission_Activity` |  |  |  |
| 2 | `AA.PROD.COMM.ACTION` | `AaSimProductCommission_Action` |  |  |  |
| 3 | `AA.PROD.COMM.PRODUCT.LINE` | `AaSimProductCommission_ProductLine` |  |  |  |
| 4 | `AA.PROD.COMM.PRODUCT.GROUP` | `AaSimProductCommission_ProductGroup` |  |  |  |
| 5 | `AA.PROD.COMM.PRODUCT` | `AaSimProductCommission_Product` |  |  |  |
| 6 | `AA.PROD.COMM.ONLINE.ACT` | `AaSimProductCommission_OnlineAct` |  |  |  |
| 7 | `AA.PROD.COMM.ONLINE.CHG` | `AaSimProductCommission_OnlineChg` |  |  |  |
| 8 | `AA.PROD.COMM.DRAWBACK.TYPE` | `AaSimProductCommission_DrawbackType` |  |  |  |
| 9 | `AA.PROD.COMM.DEFER.DAYS` | `AaSimProductCommission_DeferDays` |  |  |  |
| 10 | `AA.PROD.COMM.RESERVED8` | `AaSimProductCommission_Reserved8` |  |  |  |
| 11 | `AA.PROD.COMM.RESERVED7` | `AaSimProductCommission_Reserved7` |  |  |  |
| 12 | `AA.PROD.COMM.ONLINE.COMMISSION.TYPE` | `AaSimProductCommission_OnlineCommissionType` |  |  |  |
| 13 | `AA.PROD.COMM.SCHD.PRODUCT.LINE` | `AaSimProductCommission_SchdProductLine` |  |  |  |
| 14 | `AA.PROD.COMM.SCHD.PRODUCT.GROUP` | `AaSimProductCommission_SchdProductGroup` |  |  |  |
| 15 | `AA.PROD.COMM.SCHD.PRODUCT` | `AaSimProductCommission_SchdProduct` |  |  |  |
| 16 | `AA.PROD.COMM.SCHEDULE.NAME` | `AaSimProductCommission_ScheduleName` |  |  |  |
| 17 | `AA.PROD.COMM.SCHEDULE.CHARGE` | `AaSimProductCommission_ScheduleCharge` |  |  |  |
| 18 | `AA.PROD.COMM.LINKED.PROPERTY` | `AaSimProductCommission_LinkedProperty` |  |  |  |
| 19 | `AA.PROD.COMM.SCHEDULE.FREQUENCY` | `AaSimProductCommission_ScheduleFrequency` |  |  |  |
| 20 | `AA.PROD.COMM.BASE.DATE.TYPE` | `AaSimProductCommission_BaseDateType` |  |  |  |
| 21 | `AA.PROD.COMM.RESERVED5` | `AaSimProductCommission_Reserved5` |  |  |  |
| 22 | `AA.PROD.COMM.SCHEDULE.COMMISSION.TYPE` | `AaSimProductCommission_ScheduleCommissionType` |  |  |  |
| 23 | `AA.PROD.COMM.RESERVED3` | `AaSimProductCommission_Reserved3` |  |  |  |
| 24 | `AA.PROD.COMM.RESERVED2` | `AaSimProductCommission_Reserved2` |  |  |  |
| 25 | `AA.PROD.COMM.RESERVED1` | `AaSimProductCommission_Reserved1` |  |  |  |
| 26 | `AA.PROD.COMM.LOCAL.REF` | `AaSimProductCommission_LocalRef` |  |  |  |
| 27 | `AA.PROD.COMM.PR.ATTRIBUTE` | `AaSimProductCommission_PrAttribute` |  |  |  |
| 28 | `AA.PROD.COMM.PR.VALUE` | `AaSimProductCommission_PrValue` |  |  |  |
| 29 | `AA.PROD.COMM.PR.BRK.RES` | `AaSimProductCommission_PrBrkRes` |  |  |  |
| 30 | `AA.PROD.COMM.PR.BRK.MSG` | `AaSimProductCommission_PrBrkMsg` |  |  |  |
| 31 | `AA.PROD.COMM.PR.BRK.CHARGE` | `AaSimProductCommission_PrBrkCharge` |  |  |  |
| 32 | `AA.PROD.COMM.PR.RESERVED.3` | `AaSimProductCommission_PrReserved3` |  |  |  |
| 33 | `AA.PROD.COMM.PR.RESERVED.2` | `AaSimProductCommission_PrReserved2` |  |  |  |
| 34 | `AA.PROD.COMM.PR.RESERVED.1` | `AaSimProductCommission_PrReserved1` |  |  |  |
| 35 | `AA.PROD.COMM.PR.APP.METHOD` | `AaSimProductCommission_PrAppMethod` |  |  |  |
| 36 | `AA.PROD.COMM.PR.APP.PERIOD` | `AaSimProductCommission_PrAppPeriod` |  |  |  |
| 37 | `AA.PROD.COMM.SYS.RESERVE7` | `AaSimProductCommission_SysReserve7` |  |  |  |
| 38 | `AA.PROD.COMM.SYS.RESERVE6` | `AaSimProductCommission_SysReserve6` |  |  |  |
| 39 | `AA.PROD.COMM.OWNING.COMPANY` | `AaSimProductCommission_OwningCompany` |  |  |  |
| 40 | `AA.PROD.COMM.API.ATTRIBUTE` | `AaSimProductCommission_ApiAttribute` |  |  |  |
| 41 | `AA.PROD.COMM.SYS.RESERVE3` | `AaSimProductCommission_SysReserve3` |  |  |  |
| 42 | `AA.PROD.COMM.SYS.RESERVE2` | `AaSimProductCommission_SysReserve2` |  |  |  |
| 43 | `AA.PROD.COMM.SYS.RESERVE1` | `AaSimProductCommission_SysReserve1` |  |  |  |
| 44 | `AA.PROD.COMM.DEFAULT.ATTR.OPTION` | `AaSimProductCommission_DefaultAttrOption` |  |  |  |
| 45 | `AA.PROD.COMM.DEFAULT.NEGOTIABLE` | `AaSimProductCommission_DefaultNegotiable` |  |  |  |
| 46 | `AA.PROD.COMM.NR.ATTRIBUTE` | `AaSimProductCommission_NrAttribute` |  |  |  |
| 47 | `AA.PROD.COMM.NR.OPTIONS` | `AaSimProductCommission_NrOptions` |  |  |  |
| 48 | `AA.PROD.COMM.NR.ATTRIBUTE.RULE` | `AaSimProductCommission_NrAttributeRule` |  |  |  |
| 49 | `AA.PROD.COMM.NR.VALUE.SOURCE` | `AaSimProductCommission_NrValueSource` |  |  |  |
| 50 | `AA.PROD.COMM.NR.STD.COMP` | `AaSimProductCommission_NrStdComp` |  |  |  |
| 51 | `AA.PROD.COMM.NR.TYPE` | `AaSimProductCommission_NrType` |  |  |  |
| 52 | `AA.PROD.COMM.NR.VALUE` | `AaSimProductCommission_NrValue` |  |  |  |
| 53 | `AA.PROD.COMM.NR.MESSAGE` | `AaSimProductCommission_NrMessage` |  |  |  |
| 54 | `AA.PROD.COMM.CHANGED.FIELDS` | `AaSimProductCommission_ChangedFields` |  |  |  |
| 55 | `AA.PROD.COMM.NEGOTIATED.FLDS` | `AaSimProductCommission_NegotiatedFlds` |  |  |  |
| 56 | `AA.PROD.COMM.ID.COMP.1` | `AaSimProductCommission_IdComp1` |  |  |  |
| 57 | `AA.PROD.COMM.ID.COMP.2` | `AaSimProductCommission_IdComp2` |  |  |  |
| 58 | `AA.PROD.COMM.ID.COMP.3` | `AaSimProductCommission_IdComp3` |  |  |  |
| 59 | `AA.PROD.COMM.ID.COMP.4` | `AaSimProductCommission_IdComp4` |  |  |  |
| 60 | `AA.PROD.COMM.ID.COMP.5` | `AaSimProductCommission_IdComp5` |  |  |  |
| 61 | `AA.PROD.COMM.ID.COMP.6` | `AaSimProductCommission_IdComp6` |  |  |  |
| 62 | `AA.PROD.COMM.RESERVED2.ID` | `AaSimProductCommission_Reserved2Id` |  |  |  |
| 63 | `AA.PROD.COMM.TARGET.PRODUCT` | `AaSimProductCommission_TargetProduct` |  |  |  |
| 64 | `AA.PROD.COMM.STMT.NOS` | `AaSimProductCommission_StmtNos` |  |  |  |
| 65 | `AA.PROD.COMM.OVERRIDE` | `AaSimProductCommission_Override` |  |  |  |
| 66 | `AA.PROD.COMM.RECORD.STATUS` | `AaSimProductCommission_RecordStatus` |  |  |  |
| 67 | `AA.PROD.COMM.CURR.NO` | `AaSimProductCommission_CurrNo` |  |  |  |
| 68 | `AA.PROD.COMM.INPUTTER` | `AaSimProductCommission_Inputter` |  |  |  |
| 69 | `AA.PROD.COMM.DATE.TIME` | `AaSimProductCommission_DateTime` |  |  |  |
| 70 | `AA.PROD.COMM.AUTHORISER` | `AaSimProductCommission_Authoriser` |  |  |  |
| 71 | `AA.PROD.COMM.CO.CODE` | `AaSimProductCommission_CoCode` |  |  |  |
| 72 | `AA.PROD.COMM.DEPT.CODE` | `AaSimProductCommission_DeptCode` |  |  |  |
| 73 | `AA.PROD.COMM.AUDITOR.CODE` | `AaSimProductCommission_AuditorCode` |  |  |  |
| 74 | `AA.PROD.COMM.AUDIT.DATE.TIME` | `AaSimProductCommission_AuditDateTime` |  |  |  |
