# AA.ACTIVITY.PRESENTATION — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.PRESENTATION` in `AA_ActivityPresentation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ACTP.ACTIVITY` | `AaSimActivityPresentation_Activity` |  |  |  |
| 2 | `AA.ACTP.ACTION` | `AaSimActivityPresentation_Action` |  |  |  |
| 3 | `AA.ACTP.PROPERTY.CLASS` | `AaSimActivityPresentation_PropertyClass` |  |  |  |
| 4 | `AA.ACTP.CLASS.VERSION` | `AaSimActivityPresentation_ClassVersion` |  |  |  |
| 5 | `AA.ACTP.CLASS.SIM.VER` | `AaSimActivityPresentation_ClassSimVer` |  |  |  |
| 6 | `AA.ACTP.PROPERTY` | `AaSimActivityPresentation_Property` |  |  |  |
| 7 | `AA.ACTP.PROP.VERSION` | `AaSimActivityPresentation_PropVersion` |  |  |  |
| 8 | `AA.ACTP.PROP.SIM.VER` | `AaSimActivityPresentation_PropSimVer` |  |  |  |
| 9 | `AA.ACTP.ACTIVITY.ID` | `AaSimActivityPresentation_ActivityId` |  |  |  |
| 10 | `AA.ACTP.ACT.PROPERTY` | `AaSimActivityPresentation_ActProperty` |  |  |  |
| 11 | `AA.ACTP.ACT.VERSION` | `AaSimActivityPresentation_ActVersion` |  |  |  |
| 12 | `AA.ACTP.ACT.SIM.VER` | `AaSimActivityPresentation_ActSimVer` |  |  |  |
| 13 | `AA.ACTP.SUPPRESS.SEE.MODE` | `AaSimActivityPresentation_SuppressSeeMode` |  |  |  |
| 14 | `AA.ACTP.HIDE.ACTIVITY` | `AaSimActivityPresentation_HideActivity` |  |  |  |
| 15 | `AA.ACTP.HIDE.PROPERTY` | `AaSimActivityPresentation_HideProperty` |  |  |  |
| 16 | `AA.ACTP.RESERVED.2` | `AaSimActivityPresentation_Reserved2` |  |  |  |
| 17 | `AA.ACTP.RESERVED.1` | `AaSimActivityPresentation_Reserved1` |  |  |  |
| 18 | `AA.ACTP.LOCAL.REF` | `AaSimActivityPresentation_LocalRef` |  |  |  |
| 19 | `AA.ACTP.PR.ATTRIBUTE` | `AaSimActivityPresentation_PrAttribute` |  |  |  |
| 20 | `AA.ACTP.PR.VALUE` | `AaSimActivityPresentation_PrValue` |  |  |  |
| 21 | `AA.ACTP.PR.BRK.RES` | `AaSimActivityPresentation_PrBrkRes` |  |  |  |
| 22 | `AA.ACTP.PR.BRK.MSG` | `AaSimActivityPresentation_PrBrkMsg` |  |  |  |
| 23 | `AA.ACTP.PR.BRK.CHARGE` | `AaSimActivityPresentation_PrBrkCharge` |  |  |  |
| 24 | `AA.ACTP.PR.RESERVED.3` | `AaSimActivityPresentation_PrReserved3` |  |  |  |
| 25 | `AA.ACTP.PR.RESERVED.2` | `AaSimActivityPresentation_PrReserved2` |  |  |  |
| 26 | `AA.ACTP.PR.RESERVED.1` | `AaSimActivityPresentation_PrReserved1` |  |  |  |
| 27 | `AA.ACTP.PR.APP.METHOD` | `AaSimActivityPresentation_PrAppMethod` |  |  |  |
| 28 | `AA.ACTP.PR.APP.PERIOD` | `AaSimActivityPresentation_PrAppPeriod` |  |  |  |
| 29 | `AA.ACTP.SYS.RESERVE7` | `AaSimActivityPresentation_SysReserve7` |  |  |  |
| 30 | `AA.ACTP.SYS.RESERVE6` | `AaSimActivityPresentation_SysReserve6` |  |  |  |
| 31 | `AA.ACTP.OWNING.COMPANY` | `AaSimActivityPresentation_OwningCompany` |  |  |  |
| 32 | `AA.ACTP.API.ATTRIBUTE` | `AaSimActivityPresentation_ApiAttribute` |  |  |  |
| 33 | `AA.ACTP.SYS.RESERVE3` | `AaSimActivityPresentation_SysReserve3` |  |  |  |
| 34 | `AA.ACTP.SYS.RESERVE2` | `AaSimActivityPresentation_SysReserve2` |  |  |  |
| 35 | `AA.ACTP.SYS.RESERVE1` | `AaSimActivityPresentation_SysReserve1` |  |  |  |
| 36 | `AA.ACTP.DEFAULT.ATTR.OPTION` | `AaSimActivityPresentation_DefaultAttrOption` |  |  |  |
| 37 | `AA.ACTP.DEFAULT.NEGOTIABLE` | `AaSimActivityPresentation_DefaultNegotiable` |  |  |  |
| 38 | `AA.ACTP.NR.ATTRIBUTE` | `AaSimActivityPresentation_NrAttribute` |  |  |  |
| 39 | `AA.ACTP.NR.OPTIONS` | `AaSimActivityPresentation_NrOptions` |  |  |  |
| 40 | `AA.ACTP.NR.ATTRIBUTE.RULE` | `AaSimActivityPresentation_NrAttributeRule` |  |  |  |
| 41 | `AA.ACTP.NR.VALUE.SOURCE` | `AaSimActivityPresentation_NrValueSource` |  |  |  |
| 42 | `AA.ACTP.NR.STD.COMP` | `AaSimActivityPresentation_NrStdComp` |  |  |  |
| 43 | `AA.ACTP.NR.TYPE` | `AaSimActivityPresentation_NrType` |  |  |  |
| 44 | `AA.ACTP.NR.VALUE` | `AaSimActivityPresentation_NrValue` |  |  |  |
| 45 | `AA.ACTP.NR.MESSAGE` | `AaSimActivityPresentation_NrMessage` |  |  |  |
| 46 | `AA.ACTP.CHANGED.FIELDS` | `AaSimActivityPresentation_ChangedFields` |  |  |  |
| 47 | `AA.ACTP.NEGOTIATED.FLDS` | `AaSimActivityPresentation_NegotiatedFlds` |  |  |  |
| 48 | `AA.ACTP.ID.COMP.1` | `AaSimActivityPresentation_IdComp1` |  |  |  |
| 49 | `AA.ACTP.ID.COMP.2` | `AaSimActivityPresentation_IdComp2` |  |  |  |
| 50 | `AA.ACTP.ID.COMP.3` | `AaSimActivityPresentation_IdComp3` |  |  |  |
| 51 | `AA.ACTP.ID.COMP.4` | `AaSimActivityPresentation_IdComp4` |  |  |  |
| 52 | `AA.ACTP.ID.COMP.5` | `AaSimActivityPresentation_IdComp5` |  |  |  |
| 53 | `AA.ACTP.ID.COMP.6` | `AaSimActivityPresentation_IdComp6` |  |  |  |
| 54 | `AA.ACTP.RESERVED2.ID` | `AaSimActivityPresentation_Reserved2Id` |  |  |  |
| 55 | `AA.ACTP.TARGET.PRODUCT` | `AaSimActivityPresentation_TargetProduct` |  |  |  |
| 56 | `AA.ACTP.STMT.NOS` | `AaSimActivityPresentation_StmtNos` |  |  |  |
| 57 | `AA.ACTP.OVERRIDE` | `AaSimActivityPresentation_Override` |  |  |  |
| 58 | `AA.ACTP.RECORD.STATUS` | `AaSimActivityPresentation_RecordStatus` |  |  |  |
| 59 | `AA.ACTP.CURR.NO` | `AaSimActivityPresentation_CurrNo` |  |  |  |
| 60 | `AA.ACTP.INPUTTER` | `AaSimActivityPresentation_Inputter` |  |  |  |
| 61 | `AA.ACTP.DATE.TIME` | `AaSimActivityPresentation_DateTime` |  |  |  |
| 62 | `AA.ACTP.AUTHORISER` | `AaSimActivityPresentation_Authoriser` |  |  |  |
| 63 | `AA.ACTP.CO.CODE` | `AaSimActivityPresentation_CoCode` |  |  |  |
| 64 | `AA.ACTP.DEPT.CODE` | `AaSimActivityPresentation_DeptCode` |  |  |  |
| 65 | `AA.ACTP.AUDITOR.CODE` | `AaSimActivityPresentation_AuditorCode` |  |  |  |
| 66 | `AA.ACTP.AUDIT.DATE.TIME` | `AaSimActivityPresentation_AuditDateTime` |  |  |  |
