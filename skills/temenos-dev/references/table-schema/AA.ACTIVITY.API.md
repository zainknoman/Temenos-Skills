# AA.ACTIVITY.API — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.API` in `AA_ActivityAPI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.API.ACTIVITY` | `AaSimActivityApi_Activity` |  |  |  |
| 2 | `AA.API.ACTION` | `AaSimActivityApi_Action` |  |  |  |
| 3 | `AA.API.ACTIVITY.CLASS` | `AaSimActivityApi_ActivityClass` |  |  |  |
| 4 | `AA.API.ACTIVITY.ID` | `AaSimActivityApi_ActivityId` |  |  |  |
| 5 | `AA.API.PROPERTY.CLASS` | `AaSimActivityApi_PropertyClass` |  |  |  |
| 6 | `AA.API.PROPERTY` | `AaSimActivityApi_Property` |  |  |  |
| 7 | `AA.API.PC.ACTION` | `AaSimActivityApi_PcAction` |  |  |  |
| 8 | `AA.API.PRE.ROUTINE` | `AaSimActivityApi_PreRoutine` |  |  |  |
| 9 | `AA.API.POST.ROUTINE` | `AaSimActivityApi_PostRoutine` |  |  |  |
| 10 | `AA.API.RECORD.RTN` | `AaSimActivityApi_RecordRtn` |  |  |  |
| 11 | `AA.API.VALIDATE.RTN` | `AaSimActivityApi_ValidateRtn` |  |  |  |
| 12 | `AA.API.PRE.VALIDATE.RTN` | `AaSimActivityApi_PreValidateRtn` |  |  |  |
| 13 | `AA.API.RESERVED.3` | `AaSimActivityApi_Reserved3` |  |  |  |
| 14 | `AA.API.RESERVED.2` | `AaSimActivityApi_Reserved2` |  |  |  |
| 15 | `AA.API.RESERVED.1` | `AaSimActivityApi_Reserved1` |  |  |  |
| 16 | `AA.API.LOCAL.REF` | `AaSimActivityApi_LocalRef` |  |  |  |
| 17 | `AA.API.PR.ATTRIBUTE` | `AaSimActivityApi_PrAttribute` |  |  |  |
| 18 | `AA.API.PR.VALUE` | `AaSimActivityApi_PrValue` |  |  |  |
| 19 | `AA.API.PR.BRK.RES` | `AaSimActivityApi_PrBrkRes` |  |  |  |
| 20 | `AA.API.PR.BRK.MSG` | `AaSimActivityApi_PrBrkMsg` |  |  |  |
| 21 | `AA.API.PR.BRK.CHARGE` | `AaSimActivityApi_PrBrkCharge` |  |  |  |
| 22 | `AA.API.PR.RESERVED.3` | `AaSimActivityApi_PrReserved3` |  |  |  |
| 23 | `AA.API.PR.RESERVED.2` | `AaSimActivityApi_PrReserved2` |  |  |  |
| 24 | `AA.API.PR.RESERVED.1` | `AaSimActivityApi_PrReserved1` |  |  |  |
| 25 | `AA.API.PR.APP.METHOD` | `AaSimActivityApi_PrAppMethod` |  |  |  |
| 26 | `AA.API.PR.APP.PERIOD` | `AaSimActivityApi_PrAppPeriod` |  |  |  |
| 27 | `AA.API.SYS.RESERVE7` | `AaSimActivityApi_SysReserve7` |  |  |  |
| 28 | `AA.API.SYS.RESERVE6` | `AaSimActivityApi_SysReserve6` |  |  |  |
| 29 | `AA.API.OWNING.COMPANY` | `AaSimActivityApi_OwningCompany` |  |  |  |
| 30 | `AA.API.API.ATTRIBUTE` | `AaSimActivityApi_ApiAttribute` |  |  |  |
| 31 | `AA.API.SYS.RESERVE3` | `AaSimActivityApi_SysReserve3` |  |  |  |
| 32 | `AA.API.SYS.RESERVE2` | `AaSimActivityApi_SysReserve2` |  |  |  |
| 33 | `AA.API.SYS.RESERVE1` | `AaSimActivityApi_SysReserve1` |  |  |  |
| 34 | `AA.API.DEFAULT.ATTR.OPTION` | `AaSimActivityApi_DefaultAttrOption` |  |  |  |
| 35 | `AA.API.DEFAULT.NEGOTIABLE` | `AaSimActivityApi_DefaultNegotiable` |  |  |  |
| 36 | `AA.API.NR.ATTRIBUTE` | `AaSimActivityApi_NrAttribute` |  |  |  |
| 37 | `AA.API.NR.OPTIONS` | `AaSimActivityApi_NrOptions` |  |  |  |
| 38 | `AA.API.NR.ATTRIBUTE.RULE` | `AaSimActivityApi_NrAttributeRule` |  |  |  |
| 39 | `AA.API.NR.VALUE.SOURCE` | `AaSimActivityApi_NrValueSource` |  |  |  |
| 40 | `AA.API.NR.STD.COMP` | `AaSimActivityApi_NrStdComp` |  |  |  |
| 41 | `AA.API.NR.TYPE` | `AaSimActivityApi_NrType` |  |  |  |
| 42 | `AA.API.NR.VALUE` | `AaSimActivityApi_NrValue` |  |  |  |
| 43 | `AA.API.NR.MESSAGE` | `AaSimActivityApi_NrMessage` |  |  |  |
| 44 | `AA.API.CHANGED.FIELDS` | `AaSimActivityApi_ChangedFields` |  |  |  |
| 45 | `AA.API.NEGOTIATED.FLDS` | `AaSimActivityApi_NegotiatedFlds` |  |  |  |
| 46 | `AA.API.ID.COMP.1` | `AaSimActivityApi_IdComp1` |  |  |  |
| 47 | `AA.API.ID.COMP.2` | `AaSimActivityApi_IdComp2` |  |  |  |
| 48 | `AA.API.ID.COMP.3` | `AaSimActivityApi_IdComp3` |  |  |  |
| 49 | `AA.API.ID.COMP.4` | `AaSimActivityApi_IdComp4` |  |  |  |
| 50 | `AA.API.ID.COMP.5` | `AaSimActivityApi_IdComp5` |  |  |  |
| 51 | `AA.API.ID.COMP.6` | `AaSimActivityApi_IdComp6` |  |  |  |
| 52 | `AA.API.RESERVED2.ID` | `AaSimActivityApi_Reserved2Id` |  |  |  |
| 53 | `AA.API.TARGET.PRODUCT` | `AaSimActivityApi_TargetProduct` |  |  |  |
| 54 | `AA.API.STMT.NOS` | `AaSimActivityApi_StmtNos` |  |  |  |
| 55 | `AA.API.OVERRIDE` | `AaSimActivityApi_Override` |  |  |  |
| 56 | `AA.API.RECORD.STATUS` | `AaSimActivityApi_RecordStatus` |  |  |  |
| 57 | `AA.API.CURR.NO` | `AaSimActivityApi_CurrNo` |  |  |  |
| 58 | `AA.API.INPUTTER` | `AaSimActivityApi_Inputter` |  |  |  |
| 59 | `AA.API.DATE.TIME` | `AaSimActivityApi_DateTime` |  |  |  |
| 60 | `AA.API.AUTHORISER` | `AaSimActivityApi_Authoriser` |  |  |  |
| 61 | `AA.API.CO.CODE` | `AaSimActivityApi_CoCode` |  |  |  |
| 62 | `AA.API.DEPT.CODE` | `AaSimActivityApi_DeptCode` |  |  |  |
| 63 | `AA.API.AUDITOR.CODE` | `AaSimActivityApi_AuditorCode` |  |  |  |
| 64 | `AA.API.AUDIT.DATE.TIME` | `AaSimActivityApi_AuditDateTime` |  |  |  |
