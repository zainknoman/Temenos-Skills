# AA.ACTIVITY.MESSAGING — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.MESSAGING` in `AA_ActivityMessaging.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AM.ACTIVITY` | `AaSimActivityMessaging_Activity` |  |  |  |
| 2 | `AA.AM.ACTION` | `AaSimActivityMessaging_Action` |  |  |  |
| 3 | `AA.AM.ADVICE` | `AaSimActivityMessaging_Advice` |  |  |  |
| 4 | `AA.AM.ACTIVITY.CLASS` | `AaSimActivityMessaging_ActivityClass` |  |  |  |
| 5 | `AA.AM.ACTIVITY.ID` | `AaSimActivityMessaging_ActivityId` |  |  |  |
| 6 | `AA.AM.MSG.CONTENT` | `AaSimActivityMessaging_MsgContent` |  |  |  |
| 7 | `AA.AM.SEND.ADVICE` | `AaSimActivityMessaging_SendAdvice` |  |  |  |
| 8 | `AA.AM.PRE.NOTICE.ACTIVITY` | `AaSimActivityMessaging_PreNoticeActivity` |  |  |  |
| 9 | `AA.AM.PRE.NOTICE.DAYS` | `AaSimActivityMessaging_PreNoticeDays` |  |  |  |
| 10 | `AA.AM.RESERVED2` | `AaSimActivityMessaging_Reserved2` |  |  |  |
| 11 | `AA.AM.RESERVED1` | `AaSimActivityMessaging_Reserved1` |  |  |  |
| 12 | `AA.AM.LOCAL.REF` | `AaSimActivityMessaging_LocalRef` |  |  |  |
| 13 | `AA.AM.PR.ATTRIBUTE` | `AaSimActivityMessaging_PrAttribute` |  |  |  |
| 14 | `AA.AM.PR.VALUE` | `AaSimActivityMessaging_PrValue` |  |  |  |
| 15 | `AA.AM.PR.BRK.RES` | `AaSimActivityMessaging_PrBrkRes` |  |  |  |
| 16 | `AA.AM.PR.BRK.MSG` | `AaSimActivityMessaging_PrBrkMsg` |  |  |  |
| 17 | `AA.AM.PR.BRK.CHARGE` | `AaSimActivityMessaging_PrBrkCharge` |  |  |  |
| 18 | `AA.AM.PR.RESERVED.3` | `AaSimActivityMessaging_PrReserved3` |  |  |  |
| 19 | `AA.AM.PR.RESERVED.2` | `AaSimActivityMessaging_PrReserved2` |  |  |  |
| 20 | `AA.AM.PR.RESERVED.1` | `AaSimActivityMessaging_PrReserved1` |  |  |  |
| 21 | `AA.AM.PR.APP.METHOD` | `AaSimActivityMessaging_PrAppMethod` |  |  |  |
| 22 | `AA.AM.PR.APP.PERIOD` | `AaSimActivityMessaging_PrAppPeriod` |  |  |  |
| 23 | `AA.AM.SYS.RESERVE7` | `AaSimActivityMessaging_SysReserve7` |  |  |  |
| 24 | `AA.AM.SYS.RESERVE6` | `AaSimActivityMessaging_SysReserve6` |  |  |  |
| 25 | `AA.AM.OWNING.COMPANY` | `AaSimActivityMessaging_OwningCompany` |  |  |  |
| 26 | `AA.AM.API.ATTRIBUTE` | `AaSimActivityMessaging_ApiAttribute` |  |  |  |
| 27 | `AA.AM.SYS.RESERVE3` | `AaSimActivityMessaging_SysReserve3` |  |  |  |
| 28 | `AA.AM.SYS.RESERVE2` | `AaSimActivityMessaging_SysReserve2` |  |  |  |
| 29 | `AA.AM.SYS.RESERVE1` | `AaSimActivityMessaging_SysReserve1` |  |  |  |
| 30 | `AA.AM.DEFAULT.ATTR.OPTION` | `AaSimActivityMessaging_DefaultAttrOption` |  |  |  |
| 31 | `AA.AM.DEFAULT.NEGOTIABLE` | `AaSimActivityMessaging_DefaultNegotiable` |  |  |  |
| 32 | `AA.AM.NR.ATTRIBUTE` | `AaSimActivityMessaging_NrAttribute` |  |  |  |
| 33 | `AA.AM.NR.OPTIONS` | `AaSimActivityMessaging_NrOptions` |  |  |  |
| 34 | `AA.AM.NR.ATTRIBUTE.RULE` | `AaSimActivityMessaging_NrAttributeRule` |  |  |  |
| 35 | `AA.AM.NR.VALUE.SOURCE` | `AaSimActivityMessaging_NrValueSource` |  |  |  |
| 36 | `AA.AM.NR.STD.COMP` | `AaSimActivityMessaging_NrStdComp` |  |  |  |
| 37 | `AA.AM.NR.TYPE` | `AaSimActivityMessaging_NrType` |  |  |  |
| 38 | `AA.AM.NR.VALUE` | `AaSimActivityMessaging_NrValue` |  |  |  |
| 39 | `AA.AM.NR.MESSAGE` | `AaSimActivityMessaging_NrMessage` |  |  |  |
| 40 | `AA.AM.CHANGED.FIELDS` | `AaSimActivityMessaging_ChangedFields` |  |  |  |
| 41 | `AA.AM.NEGOTIATED.FLDS` | `AaSimActivityMessaging_NegotiatedFlds` |  |  |  |
| 42 | `AA.AM.ID.COMP.1` | `AaSimActivityMessaging_IdComp1` |  |  |  |
| 43 | `AA.AM.ID.COMP.2` | `AaSimActivityMessaging_IdComp2` |  |  |  |
| 44 | `AA.AM.ID.COMP.3` | `AaSimActivityMessaging_IdComp3` |  |  |  |
| 45 | `AA.AM.ID.COMP.4` | `AaSimActivityMessaging_IdComp4` |  |  |  |
| 46 | `AA.AM.ID.COMP.5` | `AaSimActivityMessaging_IdComp5` |  |  |  |
| 47 | `AA.AM.ID.COMP.6` | `AaSimActivityMessaging_IdComp6` |  |  |  |
| 48 | `AA.AM.RESERVED2.ID` | `AaSimActivityMessaging_Reserved2Id` |  |  |  |
| 49 | `AA.AM.TARGET.PRODUCT` | `AaSimActivityMessaging_TargetProduct` |  |  |  |
| 50 | `AA.AM.STMT.NOS` | `AaSimActivityMessaging_StmtNos` |  |  |  |
| 51 | `AA.AM.OVERRIDE` | `AaSimActivityMessaging_Override` |  |  |  |
| 52 | `AA.AM.RECORD.STATUS` | `AaSimActivityMessaging_RecordStatus` |  |  |  |
| 53 | `AA.AM.CURR.NO` | `AaSimActivityMessaging_CurrNo` |  |  |  |
| 54 | `AA.AM.INPUTTER` | `AaSimActivityMessaging_Inputter` |  |  |  |
| 55 | `AA.AM.DATE.TIME` | `AaSimActivityMessaging_DateTime` |  |  |  |
| 56 | `AA.AM.AUTHORISER` | `AaSimActivityMessaging_Authoriser` |  |  |  |
| 57 | `AA.AM.CO.CODE` | `AaSimActivityMessaging_CoCode` |  |  |  |
| 58 | `AA.AM.DEPT.CODE` | `AaSimActivityMessaging_DeptCode` |  |  |  |
| 59 | `AA.AM.AUDITOR.CODE` | `AaSimActivityMessaging_AuditorCode` |  |  |  |
| 60 | `AA.AM.AUDIT.DATE.TIME` | `AaSimActivityMessaging_AuditDateTime` |  |  |  |
| 61 | `AA.AM.ROLE` | `AaSimActivityMessaging_Role` |  |  |  |
| 62 | `AA.AM.ROLE.ADVICE` | `AaSimActivityMessaging_RoleAdvice` |  |  |  |
| 63 | `AA.AM.ROLE.SEND.ADVICE` | `AaSimActivityMessaging_RoleSendAdvice` |  |  |  |
