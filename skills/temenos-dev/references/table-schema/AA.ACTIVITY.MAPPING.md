# AA.ACTIVITY.MAPPING — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.MAPPING` in `AA_ActivityMapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ACM.ACTIVITY` | `AaSimActivityMapping_Activity` |  |  |  |
| 2 | `AA.ACM.ACTION` | `AaSimActivityMapping_Action` |  |  |  |
| 3 | `AA.ACM.TRANSACTION` | `AaSimActivityMapping_Transaction` |  |  |  |
| 4 | `AA.ACM.RESERVED5` | `AaSimActivityMapping_Reserved5` |  |  |  |
| 5 | `AA.ACM.RESERVED7` | `AaSimActivityMapping_Reserved7` |  |  |  |
| 6 | `AA.ACM.TXN.SERVICE.GROUP` | `AaSimActivityMapping_TxnServiceGroup` |  |  |  |
| 7 | `AA.ACM.TXN.ACTIVITY` | `AaSimActivityMapping_TxnActivity` |  |  |  |
| 8 | `AA.ACM.DEF.CR.ACTIVITY` | `AaSimActivityMapping_DefCrActivity` |  |  |  |
| 9 | `AA.ACM.DEF.DB.ACTIVITY` | `AaSimActivityMapping_DefDbActivity` |  |  |  |
| 10 | `AA.ACM.DEF.CR.SERVICE.GROUP` | `AaSimActivityMapping_DefCrServiceGroup` |  |  |  |
| 11 | `AA.ACM.DEF.DB.SERVICE.GROUP` | `AaSimActivityMapping_DefDbServiceGroup` |  |  |  |
| 12 | `AA.ACM.RESERVED2` | `AaSimActivityMapping_Reserved2` |  |  |  |
| 13 | `AA.ACM.EVENT.REF` | `AaSimActivityMapping_EventRef` |  |  |  |
| 14 | `AA.ACM.EVENT.ACTIVITY` | `AaSimActivityMapping_EventActivity` |  |  |  |
| 15 | `AA.ACM.EVENT.SERVICE.GROUP` | `AaSimActivityMapping_EventServiceGroup` |  |  |  |
| 16 | `AA.ACM.DEF.EVENT.ACTIVITY` | `AaSimActivityMapping_DefEventActivity` |  |  |  |
| 17 | `AA.ACM.DEF.EVENT.SERVICE.GROUP` | `AaSimActivityMapping_DefEventServiceGroup` |  |  |  |
| 18 | `AA.ACM.RESERVED1` | `AaSimActivityMapping_Reserved1` |  |  |  |
| 19 | `AA.ACM.LOCAL.REF` | `AaSimActivityMapping_LocalRef` |  |  |  |
| 20 | `AA.ACM.PR.ATTRIBUTE` | `AaSimActivityMapping_PrAttribute` |  |  |  |
| 21 | `AA.ACM.PR.VALUE` | `AaSimActivityMapping_PrValue` |  |  |  |
| 22 | `AA.ACM.PR.BRK.RES` | `AaSimActivityMapping_PrBrkRes` |  |  |  |
| 23 | `AA.ACM.PR.BRK.MSG` | `AaSimActivityMapping_PrBrkMsg` |  |  |  |
| 24 | `AA.ACM.PR.BRK.CHARGE` | `AaSimActivityMapping_PrBrkCharge` |  |  |  |
| 25 | `AA.ACM.PR.RESERVED.3` | `AaSimActivityMapping_PrReserved3` |  |  |  |
| 26 | `AA.ACM.PR.RESERVED.2` | `AaSimActivityMapping_PrReserved2` |  |  |  |
| 27 | `AA.ACM.PR.RESERVED.1` | `AaSimActivityMapping_PrReserved1` |  |  |  |
| 28 | `AA.ACM.PR.APP.METHOD` | `AaSimActivityMapping_PrAppMethod` |  |  |  |
| 29 | `AA.ACM.PR.APP.PERIOD` | `AaSimActivityMapping_PrAppPeriod` |  |  |  |
| 30 | `AA.ACM.SYS.RESERVE7` | `AaSimActivityMapping_SysReserve7` |  |  |  |
| 31 | `AA.ACM.SYS.RESERVE6` | `AaSimActivityMapping_SysReserve6` |  |  |  |
| 32 | `AA.ACM.OWNING.COMPANY` | `AaSimActivityMapping_OwningCompany` |  |  |  |
| 33 | `AA.ACM.API.ATTRIBUTE` | `AaSimActivityMapping_ApiAttribute` |  |  |  |
| 34 | `AA.ACM.SYS.RESERVE3` | `AaSimActivityMapping_SysReserve3` |  |  |  |
| 35 | `AA.ACM.SYS.RESERVE2` | `AaSimActivityMapping_SysReserve2` |  |  |  |
| 36 | `AA.ACM.SYS.RESERVE1` | `AaSimActivityMapping_SysReserve1` |  |  |  |
| 37 | `AA.ACM.DEFAULT.ATTR.OPTION` | `AaSimActivityMapping_DefaultAttrOption` |  |  |  |
| 38 | `AA.ACM.DEFAULT.NEGOTIABLE` | `AaSimActivityMapping_DefaultNegotiable` |  |  |  |
| 39 | `AA.ACM.NR.ATTRIBUTE` | `AaSimActivityMapping_NrAttribute` |  |  |  |
| 40 | `AA.ACM.NR.OPTIONS` | `AaSimActivityMapping_NrOptions` |  |  |  |
| 41 | `AA.ACM.NR.ATTRIBUTE.RULE` | `AaSimActivityMapping_NrAttributeRule` |  |  |  |
| 42 | `AA.ACM.NR.VALUE.SOURCE` | `AaSimActivityMapping_NrValueSource` |  |  |  |
| 43 | `AA.ACM.NR.STD.COMP` | `AaSimActivityMapping_NrStdComp` |  |  |  |
| 44 | `AA.ACM.NR.TYPE` | `AaSimActivityMapping_NrType` |  |  |  |
| 45 | `AA.ACM.NR.VALUE` | `AaSimActivityMapping_NrValue` |  |  |  |
| 46 | `AA.ACM.NR.MESSAGE` | `AaSimActivityMapping_NrMessage` |  |  |  |
| 47 | `AA.ACM.CHANGED.FIELDS` | `AaSimActivityMapping_ChangedFields` |  |  |  |
| 48 | `AA.ACM.NEGOTIATED.FLDS` | `AaSimActivityMapping_NegotiatedFlds` |  |  |  |
| 49 | `AA.ACM.ID.COMP.1` | `AaSimActivityMapping_IdComp1` |  |  |  |
| 50 | `AA.ACM.ID.COMP.2` | `AaSimActivityMapping_IdComp2` |  |  |  |
| 51 | `AA.ACM.ID.COMP.3` | `AaSimActivityMapping_IdComp3` |  |  |  |
| 52 | `AA.ACM.ID.COMP.4` | `AaSimActivityMapping_IdComp4` |  |  |  |
| 53 | `AA.ACM.ID.COMP.5` | `AaSimActivityMapping_IdComp5` |  |  |  |
| 54 | `AA.ACM.ID.COMP.6` | `AaSimActivityMapping_IdComp6` |  |  |  |
| 55 | `AA.ACM.RESERVED2.ID` | `AaSimActivityMapping_Reserved2Id` |  |  |  |
| 56 | `AA.ACM.TARGET.PRODUCT` | `AaSimActivityMapping_TargetProduct` |  |  |  |
| 57 | `AA.ACM.STMT.NOS` | `AaSimActivityMapping_StmtNos` |  |  |  |
| 58 | `AA.ACM.OVERRIDE` | `AaSimActivityMapping_Override` |  |  |  |
| 59 | `AA.ACM.RECORD.STATUS` | `AaSimActivityMapping_RecordStatus` |  |  |  |
| 60 | `AA.ACM.CURR.NO` | `AaSimActivityMapping_CurrNo` |  |  |  |
| 61 | `AA.ACM.INPUTTER` | `AaSimActivityMapping_Inputter` |  |  |  |
| 62 | `AA.ACM.DATE.TIME` | `AaSimActivityMapping_DateTime` |  |  |  |
| 63 | `AA.ACM.AUTHORISER` | `AaSimActivityMapping_Authoriser` |  |  |  |
| 64 | `AA.ACM.CO.CODE` | `AaSimActivityMapping_CoCode` |  |  |  |
| 65 | `AA.ACM.DEPT.CODE` | `AaSimActivityMapping_DeptCode` |  |  |  |
| 66 | `AA.ACM.AUDITOR.CODE` | `AaSimActivityMapping_AuditorCode` |  |  |  |
| 67 | `AA.ACM.AUDIT.DATE.TIME` | `AaSimActivityMapping_AuditDateTime` |  |  |  |
