# AA.CHANNEL.ACCESS — Table Schema

> Source: `INSERTS/I_F.AA.CHANNEL.ACCESS` in `AA_ChannelAccess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CHA.ACTIVITY` | `AaSimChannelAccess_Activity` |  |  |  |
| 2 | `AA.CHA.ACTION` | `AaSimChannelAccess_Action` |  |  |  |
| 3 | `AA.CHA.EB.CHANNEL` | `AaSimChannelAccess_EbChannel` |  |  |  |
| 4 | `AA.CHA.START.DATE` | `AaSimChannelAccess_StartDate` |  |  |  |
| 5 | `AA.CHA.START.TIME` | `AaSimChannelAccess_StartTime` |  |  |  |
| 6 | `AA.CHA.END.DATE` | `AaSimChannelAccess_EndDate` |  |  |  |
| 7 | `AA.CHA.END.TIME` | `AaSimChannelAccess_EndTime` |  |  |  |
| 8 | `AA.CHA.MV.RESERVED.5` | `AaSimChannelAccess_MvReserved5` |  |  |  |
| 9 | `AA.CHA.MV.RESERVED.4` | `AaSimChannelAccess_MvReserved4` |  |  |  |
| 10 | `AA.CHA.MV.RESERVED.3` | `AaSimChannelAccess_MvReserved3` |  |  |  |
| 11 | `AA.CHA.MV.RESERVED.2` | `AaSimChannelAccess_MvReserved2` |  |  |  |
| 12 | `AA.CHA.MV.RESERVED.1` | `AaSimChannelAccess_MvReserved1` |  |  |  |
| 13 | `AA.CHA.BLOCK.START.DATE` | `AaSimChannelAccess_BlockStartDate` |  |  |  |
| 14 | `AA.CHA.BLOCK.START.TIME` | `AaSimChannelAccess_BlockStartTime` |  |  |  |
| 15 | `AA.CHA.BLOCK.END.DATE` | `AaSimChannelAccess_BlockEndDate` |  |  |  |
| 16 | `AA.CHA.BLOCK.END.TIME` | `AaSimChannelAccess_BlockEndTime` |  |  |  |
| 17 | `AA.CHA.SV.RESERVED.5` | `AaSimChannelAccess_SvReserved5` |  |  |  |
| 18 | `AA.CHA.SV.RESERVED.4` | `AaSimChannelAccess_SvReserved4` |  |  |  |
| 19 | `AA.CHA.SV.RESERVED.3` | `AaSimChannelAccess_SvReserved3` |  |  |  |
| 20 | `AA.CHA.SV.RESERVED.2` | `AaSimChannelAccess_SvReserved2` |  |  |  |
| 21 | `AA.CHA.SV.RESERVED.1` | `AaSimChannelAccess_SvReserved1` |  |  |  |
| 22 | `AA.CHA.RESERVED.10` | `AaSimChannelAccess_Reserved10` |  |  |  |
| 23 | `AA.CHA.RESERVED.9` | `AaSimChannelAccess_Reserved9` |  |  |  |
| 24 | `AA.CHA.RESERVED.8` | `AaSimChannelAccess_Reserved8` |  |  |  |
| 25 | `AA.CHA.RESERVED.7` | `AaSimChannelAccess_Reserved7` |  |  |  |
| 26 | `AA.CHA.RESERVED.6` | `AaSimChannelAccess_Reserved6` |  |  |  |
| 27 | `AA.CHA.RESERVED.5` | `AaSimChannelAccess_Reserved5` |  |  |  |
| 28 | `AA.CHA.RESERVED.4` | `AaSimChannelAccess_Reserved4` |  |  |  |
| 29 | `AA.CHA.RESERVED.3` | `AaSimChannelAccess_Reserved3` |  |  |  |
| 30 | `AA.CHA.RESERVED.2` | `AaSimChannelAccess_Reserved2` |  |  |  |
| 31 | `AA.CHA.RESERVED.1` | `AaSimChannelAccess_Reserved1` |  |  |  |
| 32 | `AA.CHA.LOCAL.REF` | `AaSimChannelAccess_LocalRef` |  |  |  |
| 33 | `AA.CHA.PR.ATTRIBUTE` | `AaSimChannelAccess_PrAttribute` |  |  |  |
| 34 | `AA.CHA.PR.VALUE` | `AaSimChannelAccess_PrValue` |  |  |  |
| 35 | `AA.CHA.PR.BRK.RES` | `AaSimChannelAccess_PrBrkRes` |  |  |  |
| 36 | `AA.CHA.PR.BRK.MSG` | `AaSimChannelAccess_PrBrkMsg` |  |  |  |
| 37 | `AA.CHA.PR.BRK.CHARGE` | `AaSimChannelAccess_PrBrkCharge` |  |  |  |
| 38 | `AA.CHA.PR.RESERVED.3` | `AaSimChannelAccess_PrReserved3` |  |  |  |
| 39 | `AA.CHA.PR.RESERVED.2` | `AaSimChannelAccess_PrReserved2` |  |  |  |
| 40 | `AA.CHA.PR.RESERVED.1` | `AaSimChannelAccess_PrReserved1` |  |  |  |
| 41 | `AA.CHA.PR.APP.METHOD` | `AaSimChannelAccess_PrAppMethod` |  |  |  |
| 42 | `AA.CHA.PR.APP.PERIOD` | `AaSimChannelAccess_PrAppPeriod` |  |  |  |
| 43 | `AA.CHA.SYS.RESERVE7` | `AaSimChannelAccess_SysReserve7` |  |  |  |
| 44 | `AA.CHA.SYS.RESERVE6` | `AaSimChannelAccess_SysReserve6` |  |  |  |
| 45 | `AA.CHA.OWNING.COMPANY` | `AaSimChannelAccess_OwningCompany` |  |  |  |
| 46 | `AA.CHA.API.ATTRIBUTE` | `AaSimChannelAccess_ApiAttribute` |  |  |  |
| 47 | `AA.CHA.SYS.RESERVE3` | `AaSimChannelAccess_SysReserve3` |  |  |  |
| 48 | `AA.CHA.SYS.RESERVE2` | `AaSimChannelAccess_SysReserve2` |  |  |  |
| 49 | `AA.CHA.SYS.RESERVE1` | `AaSimChannelAccess_SysReserve1` |  |  |  |
| 50 | `AA.CHA.DEFAULT.ATTR.OPTION` | `AaSimChannelAccess_DefaultAttrOption` |  |  |  |
| 51 | `AA.CHA.DEFAULT.NEGOTIABLE` | `AaSimChannelAccess_DefaultNegotiable` |  |  |  |
| 52 | `AA.CHA.NR.ATTRIBUTE` | `AaSimChannelAccess_NrAttribute` |  |  |  |
| 53 | `AA.CHA.NR.OPTIONS` | `AaSimChannelAccess_NrOptions` |  |  |  |
| 54 | `AA.CHA.NR.ATTRIBUTE.RULE` | `AaSimChannelAccess_NrAttributeRule` |  |  |  |
| 55 | `AA.CHA.NR.VALUE.SOURCE` | `AaSimChannelAccess_NrValueSource` |  |  |  |
| 56 | `AA.CHA.NR.STD.COMP` | `AaSimChannelAccess_NrStdComp` |  |  |  |
| 57 | `AA.CHA.NR.TYPE` | `AaSimChannelAccess_NrType` |  |  |  |
| 58 | `AA.CHA.NR.VALUE` | `AaSimChannelAccess_NrValue` |  |  |  |
| 59 | `AA.CHA.NR.MESSAGE` | `AaSimChannelAccess_NrMessage` |  |  |  |
| 60 | `AA.CHA.CHANGED.FIELDS` | `AaSimChannelAccess_ChangedFields` |  |  |  |
| 61 | `AA.CHA.NEGOTIATED.FLDS` | `AaSimChannelAccess_NegotiatedFlds` |  |  |  |
| 62 | `AA.CHA.ID.COMP.1` | `AaSimChannelAccess_IdComp1` |  |  |  |
| 63 | `AA.CHA.ID.COMP.2` | `AaSimChannelAccess_IdComp2` |  |  |  |
| 64 | `AA.CHA.ID.COMP.3` | `AaSimChannelAccess_IdComp3` |  |  |  |
| 65 | `AA.CHA.ID.COMP.4` | `AaSimChannelAccess_IdComp4` |  |  |  |
| 66 | `AA.CHA.ID.COMP.5` | `AaSimChannelAccess_IdComp5` |  |  |  |
| 67 | `AA.CHA.ID.COMP.6` | `AaSimChannelAccess_IdComp6` |  |  |  |
| 68 | `AA.CHA.RESERVED2.ID` | `AaSimChannelAccess_Reserved2Id` |  |  |  |
| 69 | `AA.CHA.TARGET.PRODUCT` | `AaSimChannelAccess_TargetProduct` |  |  |  |
| 70 | `AA.CHA.STMT.NOS` | `AaSimChannelAccess_StmtNos` |  |  |  |
| 71 | `AA.CHA.OVERRIDE` | `AaSimChannelAccess_Override` |  |  |  |
| 72 | `AA.CHA.RECORD.STATUS` | `AaSimChannelAccess_RecordStatus` |  |  |  |
| 73 | `AA.CHA.CURR.NO` | `AaSimChannelAccess_CurrNo` |  |  |  |
| 74 | `AA.CHA.INPUTTER` | `AaSimChannelAccess_Inputter` |  |  |  |
| 75 | `AA.CHA.DATE.TIME` | `AaSimChannelAccess_DateTime` |  |  |  |
| 76 | `AA.CHA.AUTHORISER` | `AaSimChannelAccess_Authoriser` |  |  |  |
| 77 | `AA.CHA.CO.CODE` | `AaSimChannelAccess_CoCode` |  |  |  |
| 78 | `AA.CHA.DEPT.CODE` | `AaSimChannelAccess_DeptCode` |  |  |  |
| 79 | `AA.CHA.AUDITOR.CODE` | `AaSimChannelAccess_AuditorCode` |  |  |  |
| 80 | `AA.CHA.AUDIT.DATE.TIME` | `AaSimChannelAccess_AuditDateTime` |  |  |  |
