# AA.ACTIVITY.CHARGES — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.CHARGES` in `AA_ActivityCharges.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ACT.CHG.ACTIVITY` | `AaSimActivityCharges_Activity` |  |  |  |
| 2 | `AA.ACT.CHG.ACTION` | `AaSimActivityCharges_Action` |  |  |  |
| 3 | `AA.ACT.CHG.ACTIVITY.ID` | `AaSimActivityCharges_ActivityId` |  |  |  |
| 4 | `AA.ACT.CHG.CHARGE` | `AaSimActivityCharges_Charge` |  |  |  |
| 5 | `AA.ACT.CHG.APP.PERIOD` | `AaSimActivityCharges_AppPeriod` |  |  |  |
| 6 | `AA.ACT.CHG.APP.METHOD` | `AaSimActivityCharges_AppMethod` |  |  |  |
| 7 | `AA.ACT.CHG.CHARGE.AUTO.SETTLE` | `AaSimActivityCharges_ChargeAutoSettle` |  |  |  |
| 8 | `AA.ACT.CHG.PAYMENT.TYPE` | `AaSimActivityCharges_PaymentType` |  |  |  |
| 9 | `AA.ACT.CHG.SETTLE.ACTIVITY` | `AaSimActivityCharges_SettleActivity` |  |  |  |
| 10 | `AA.ACT.CHG.AUTO.SETTLE` | `AaSimActivityCharges_AutoSettle` |  |  |  |
| 11 | `AA.ACT.CHG.SYS.ACTIVITY.ID` | `AaSimActivityCharges_SysActivityId` |  |  |  |
| 12 | `AA.ACT.CHG.SYS.CHARGE` | `AaSimActivityCharges_SysCharge` |  |  |  |
| 13 | `AA.ACT.CHG.SYS.APP.METHOD` | `AaSimActivityCharges_SysAppMethod` |  |  |  |
| 14 | `AA.ACT.CHG.SYS.AUTO.SETTLE` | `AaSimActivityCharges_SysAutoSettle` |  |  |  |
| 15 | `AA.ACT.CHG.RESERVED3` | `AaSimActivityCharges_Reserved3` |  |  |  |
| 16 | `AA.ACT.CHG.RESERVED2` | `AaSimActivityCharges_Reserved2` |  |  |  |
| 17 | `AA.ACT.CHG.RESERVED1` | `AaSimActivityCharges_Reserved1` |  |  |  |
| 18 | `AA.ACT.CHG.LOCAL.REF` | `AaSimActivityCharges_LocalRef` |  |  |  |
| 19 | `AA.ACT.CHG.PR.ATTRIBUTE` | `AaSimActivityCharges_PrAttribute` |  |  |  |
| 20 | `AA.ACT.CHG.PR.VALUE` | `AaSimActivityCharges_PrValue` |  |  |  |
| 21 | `AA.ACT.CHG.PR.BRK.RES` | `AaSimActivityCharges_PrBrkRes` |  |  |  |
| 22 | `AA.ACT.CHG.PR.BRK.MSG` | `AaSimActivityCharges_PrBrkMsg` |  |  |  |
| 23 | `AA.ACT.CHG.PR.BRK.CHARGE` | `AaSimActivityCharges_PrBrkCharge` |  |  |  |
| 24 | `AA.ACT.CHG.PR.RESERVED.3` | `AaSimActivityCharges_PrReserved3` |  |  |  |
| 25 | `AA.ACT.CHG.PR.RESERVED.2` | `AaSimActivityCharges_PrReserved2` |  |  |  |
| 26 | `AA.ACT.CHG.PR.RESERVED.1` | `AaSimActivityCharges_PrReserved1` |  |  |  |
| 27 | `AA.ACT.CHG.PR.APP.METHOD` | `AaSimActivityCharges_PrAppMethod` |  |  |  |
| 28 | `AA.ACT.CHG.PR.APP.PERIOD` | `AaSimActivityCharges_PrAppPeriod` |  |  |  |
| 29 | `AA.ACT.CHG.SYS.RESERVE7` | `AaSimActivityCharges_SysReserve7` |  |  |  |
| 30 | `AA.ACT.CHG.SYS.RESERVE6` | `AaSimActivityCharges_SysReserve6` |  |  |  |
| 31 | `AA.ACT.CHG.OWNING.COMPANY` | `AaSimActivityCharges_OwningCompany` |  |  |  |
| 32 | `AA.ACT.CHG.API.ATTRIBUTE` | `AaSimActivityCharges_ApiAttribute` |  |  |  |
| 33 | `AA.ACT.CHG.SYS.RESERVE3` | `AaSimActivityCharges_SysReserve3` |  |  |  |
| 34 | `AA.ACT.CHG.SYS.RESERVE2` | `AaSimActivityCharges_SysReserve2` |  |  |  |
| 35 | `AA.ACT.CHG.SYS.RESERVE1` | `AaSimActivityCharges_SysReserve1` |  |  |  |
| 36 | `AA.ACT.CHG.DEFAULT.ATTR.OPTION` | `AaSimActivityCharges_DefaultAttrOption` |  |  |  |
| 37 | `AA.ACT.CHG.DEFAULT.NEGOTIABLE` | `AaSimActivityCharges_DefaultNegotiable` |  |  |  |
| 38 | `AA.ACT.CHG.NR.ATTRIBUTE` | `AaSimActivityCharges_NrAttribute` |  |  |  |
| 39 | `AA.ACT.CHG.NR.OPTIONS` | `AaSimActivityCharges_NrOptions` |  |  |  |
| 40 | `AA.ACT.CHG.NR.ATTRIBUTE.RULE` | `AaSimActivityCharges_NrAttributeRule` |  |  |  |
| 41 | `AA.ACT.CHG.NR.VALUE.SOURCE` | `AaSimActivityCharges_NrValueSource` |  |  |  |
| 42 | `AA.ACT.CHG.NR.STD.COMP` | `AaSimActivityCharges_NrStdComp` |  |  |  |
| 43 | `AA.ACT.CHG.NR.TYPE` | `AaSimActivityCharges_NrType` |  |  |  |
| 44 | `AA.ACT.CHG.NR.VALUE` | `AaSimActivityCharges_NrValue` |  |  |  |
| 45 | `AA.ACT.CHG.NR.MESSAGE` | `AaSimActivityCharges_NrMessage` |  |  |  |
| 46 | `AA.ACT.CHG.CHANGED.FIELDS` | `AaSimActivityCharges_ChangedFields` |  |  |  |
| 47 | `AA.ACT.CHG.NEGOTIATED.FLDS` | `AaSimActivityCharges_NegotiatedFlds` |  |  |  |
| 48 | `AA.ACT.CHG.ID.COMP.1` | `AaSimActivityCharges_IdComp1` |  |  |  |
| 49 | `AA.ACT.CHG.ID.COMP.2` | `AaSimActivityCharges_IdComp2` |  |  |  |
| 50 | `AA.ACT.CHG.ID.COMP.3` | `AaSimActivityCharges_IdComp3` |  |  |  |
| 51 | `AA.ACT.CHG.ID.COMP.4` | `AaSimActivityCharges_IdComp4` |  |  |  |
| 52 | `AA.ACT.CHG.ID.COMP.5` | `AaSimActivityCharges_IdComp5` |  |  |  |
| 53 | `AA.ACT.CHG.ID.COMP.6` | `AaSimActivityCharges_IdComp6` |  |  |  |
| 54 | `AA.ACT.CHG.RESERVED2.ID` | `AaSimActivityCharges_Reserved2Id` |  |  |  |
| 55 | `AA.ACT.CHG.TARGET.PRODUCT` | `AaSimActivityCharges_TargetProduct` |  |  |  |
| 56 | `AA.ACT.CHG.STMT.NOS` | `AaSimActivityCharges_StmtNos` |  |  |  |
| 57 | `AA.ACT.CHG.OVERRIDE` | `AaSimActivityCharges_Override` |  |  |  |
| 58 | `AA.ACT.CHG.RECORD.STATUS` | `AaSimActivityCharges_RecordStatus` |  |  |  |
| 59 | `AA.ACT.CHG.CURR.NO` | `AaSimActivityCharges_CurrNo` |  |  |  |
| 60 | `AA.ACT.CHG.INPUTTER` | `AaSimActivityCharges_Inputter` |  |  |  |
| 61 | `AA.ACT.CHG.DATE.TIME` | `AaSimActivityCharges_DateTime` |  |  |  |
| 62 | `AA.ACT.CHG.AUTHORISER` | `AaSimActivityCharges_Authoriser` |  |  |  |
| 63 | `AA.ACT.CHG.CO.CODE` | `AaSimActivityCharges_CoCode` |  |  |  |
| 64 | `AA.ACT.CHG.DEPT.CODE` | `AaSimActivityCharges_DeptCode` |  |  |  |
| 65 | `AA.ACT.CHG.AUDITOR.CODE` | `AaSimActivityCharges_AuditorCode` |  |  |  |
| 66 | `AA.ACT.CHG.AUDIT.DATE.TIME` | `AaSimActivityCharges_AuditDateTime` |  |  |  |
| 67 | `AA.ACT.CHG.PAYMENT.PERIOD` | `AaSimActivityCharges_PaymentPeriod` |  |  |  |
