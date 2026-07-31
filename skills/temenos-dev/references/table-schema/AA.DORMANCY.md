# AA.DORMANCY — Table Schema

> Source: `INSERTS/I_F.AA.DORMANCY` in `AA_Dormancy.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.DOM.ACTIVITY` | `AaSimDormancy_Activity` |  |  |  |
| 2 | `AA.DOM.ACTION` | `AaSimDormancy_Action` |  |  |  |
| 3 | `AA.DOM.STATUS` | `AaSimDormancy_Status` |  |  |  |
| 4 | `AA.DOM.PERIOD` | `AaSimDormancy_Period` |  |  |  |
| 5 | `AA.DOM.NOTICE.DAYS` | `AaSimDormancy_NoticeDays` |  |  |  |
| 6 | `AA.DOM.NOTICE.FREQ` | `AaSimDormancy_NoticeFreq` |  |  |  |
| 7 | `AA.DOM.CHARGE.FREQUENCY` | `AaSimDormancy_ChargeFrequency` |  |  |  |
| 8 | `AA.DOM.EXCEPTION.API` | `AaSimDormancy_ExceptionApi` |  |  |  |
| 9 | `AA.DOM.EXCEPTION.RULE` | `AaSimDormancy_ExceptionRule` |  |  |  |
| 10 | `AA.DOM.AUTO.RESET.STATUS` | `AaSimDormancy_AutoResetStatus` |  |  |  |
| 11 | `AA.DOM.CDM.HANDOFF` | `AaSimDormancy_CdmHandoff` |  |  |  |
| 12 | `AA.DOM.RESERVED.8` | `AaSimDormancy_Reserved8` |  |  |  |
| 13 | `AA.DOM.RESERVED.7` | `AaSimDormancy_Reserved7` |  |  |  |
| 14 | `AA.DOM.RESERVED.6` | `AaSimDormancy_Reserved6` |  |  |  |
| 15 | `AA.DOM.ACTIVITY.INITIATION` | `AaSimDormancy_ActivityInitiation` |  |  |  |
| 16 | `AA.DOM.ACTIVITY.CLASS` | `AaSimDormancy_ActivityClass` |  |  |  |
| 17 | `AA.DOM.ACTIVITY.NAME` | `AaSimDormancy_ActivityName` |  |  |  |
| 18 | `AA.DOM.INCLUDE.INDICATOR` | `AaSimDormancy_IncludeIndicator` |  |  |  |
| 19 | `AA.DOM.AUTO.RESET.ACTIVITY` | `AaSimDormancy_AutoResetActivity` |  |  |  |
| 20 | `AA.DOM.RESERVED.4` | `AaSimDormancy_Reserved4` |  |  |  |
| 21 | `AA.DOM.RESERVED.3` | `AaSimDormancy_Reserved3` |  |  |  |
| 22 | `AA.DOM.RESERVED.2` | `AaSimDormancy_Reserved2` |  |  |  |
| 23 | `AA.DOM.RESERVED.1` | `AaSimDormancy_Reserved1` |  |  |  |
| 24 | `AA.DOM.LOCAL.REF` | `AaSimDormancy_LocalRef` |  |  |  |
| 25 | `AA.DOM.PR.ATTRIBUTE` | `AaSimDormancy_PrAttribute` |  |  |  |
| 26 | `AA.DOM.PR.VALUE` | `AaSimDormancy_PrValue` |  |  |  |
| 27 | `AA.DOM.PR.BRK.RES` | `AaSimDormancy_PrBrkRes` |  |  |  |
| 28 | `AA.DOM.PR.BRK.MSG` | `AaSimDormancy_PrBrkMsg` |  |  |  |
| 29 | `AA.DOM.PR.BRK.CHARGE` | `AaSimDormancy_PrBrkCharge` |  |  |  |
| 30 | `AA.DOM.PR.RESERVED.3` | `AaSimDormancy_PrReserved3` |  |  |  |
| 31 | `AA.DOM.PR.RESERVED.2` | `AaSimDormancy_PrReserved2` |  |  |  |
| 32 | `AA.DOM.PR.RESERVED.1` | `AaSimDormancy_PrReserved1` |  |  |  |
| 33 | `AA.DOM.PR.APP.METHOD` | `AaSimDormancy_PrAppMethod` |  |  |  |
| 34 | `AA.DOM.PR.APP.PERIOD` | `AaSimDormancy_PrAppPeriod` |  |  |  |
| 35 | `AA.DOM.SYS.RESERVE7` | `AaSimDormancy_SysReserve7` |  |  |  |
| 36 | `AA.DOM.SYS.RESERVE6` | `AaSimDormancy_SysReserve6` |  |  |  |
| 37 | `AA.DOM.OWNING.COMPANY` | `AaSimDormancy_OwningCompany` |  |  |  |
| 38 | `AA.DOM.API.ATTRIBUTE` | `AaSimDormancy_ApiAttribute` |  |  |  |
| 39 | `AA.DOM.SYS.RESERVE3` | `AaSimDormancy_SysReserve3` |  |  |  |
| 40 | `AA.DOM.SYS.RESERVE2` | `AaSimDormancy_SysReserve2` |  |  |  |
| 41 | `AA.DOM.SYS.RESERVE1` | `AaSimDormancy_SysReserve1` |  |  |  |
| 42 | `AA.DOM.DEFAULT.ATTR.OPTION` | `AaSimDormancy_DefaultAttrOption` |  |  |  |
| 43 | `AA.DOM.DEFAULT.NEGOTIABLE` | `AaSimDormancy_DefaultNegotiable` |  |  |  |
| 44 | `AA.DOM.NR.ATTRIBUTE` | `AaSimDormancy_NrAttribute` |  |  |  |
| 45 | `AA.DOM.NR.OPTIONS` | `AaSimDormancy_NrOptions` |  |  |  |
| 46 | `AA.DOM.NR.ATTRIBUTE.RULE` | `AaSimDormancy_NrAttributeRule` |  |  |  |
| 47 | `AA.DOM.NR.VALUE.SOURCE` | `AaSimDormancy_NrValueSource` |  |  |  |
| 48 | `AA.DOM.NR.STD.COMP` | `AaSimDormancy_NrStdComp` |  |  |  |
| 49 | `AA.DOM.NR.TYPE` | `AaSimDormancy_NrType` |  |  |  |
| 50 | `AA.DOM.NR.VALUE` | `AaSimDormancy_NrValue` |  |  |  |
| 51 | `AA.DOM.NR.MESSAGE` | `AaSimDormancy_NrMessage` |  |  |  |
| 52 | `AA.DOM.CHANGED.FIELDS` | `AaSimDormancy_ChangedFields` |  |  |  |
| 53 | `AA.DOM.NEGOTIATED.FLDS` | `AaSimDormancy_NegotiatedFlds` |  |  |  |
| 54 | `AA.DOM.ID.COMP.1` | `AaSimDormancy_IdComp1` |  |  |  |
| 55 | `AA.DOM.ID.COMP.2` | `AaSimDormancy_IdComp2` |  |  |  |
| 56 | `AA.DOM.ID.COMP.3` | `AaSimDormancy_IdComp3` |  |  |  |
| 57 | `AA.DOM.ID.COMP.4` | `AaSimDormancy_IdComp4` |  |  |  |
| 58 | `AA.DOM.ID.COMP.5` | `AaSimDormancy_IdComp5` |  |  |  |
| 59 | `AA.DOM.ID.COMP.6` | `AaSimDormancy_IdComp6` |  |  |  |
| 60 | `AA.DOM.RESERVED2.ID` | `AaSimDormancy_Reserved2Id` |  |  |  |
| 61 | `AA.DOM.TARGET.PRODUCT` | `AaSimDormancy_TargetProduct` |  |  |  |
| 62 | `AA.DOM.STMT.NOS` | `AaSimDormancy_StmtNos` |  |  |  |
| 63 | `AA.DOM.OVERRIDE` | `AaSimDormancy_Override` |  |  |  |
| 64 | `AA.DOM.RECORD.STATUS` | `AaSimDormancy_RecordStatus` |  |  |  |
| 65 | `AA.DOM.CURR.NO` | `AaSimDormancy_CurrNo` |  |  |  |
| 66 | `AA.DOM.INPUTTER` | `AaSimDormancy_Inputter` |  |  |  |
| 67 | `AA.DOM.DATE.TIME` | `AaSimDormancy_DateTime` |  |  |  |
| 68 | `AA.DOM.AUTHORISER` | `AaSimDormancy_Authoriser` |  |  |  |
| 69 | `AA.DOM.CO.CODE` | `AaSimDormancy_CoCode` |  |  |  |
| 70 | `AA.DOM.DEPT.CODE` | `AaSimDormancy_DeptCode` |  |  |  |
| 71 | `AA.DOM.AUDITOR.CODE` | `AaSimDormancy_AuditorCode` |  |  |  |
| 72 | `AA.DOM.AUDIT.DATE.TIME` | `AaSimDormancy_AuditDateTime` |  |  |  |
