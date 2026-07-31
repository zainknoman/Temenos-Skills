# AA.TC.AVAILABILITY — Table Schema

> Source: `INSERTS/I_F.AA.TC.AVAILABILITY` in `AO_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.TC.AVAIL.ACTIVITY` | `AaPrdDesTcAvailability_Activity` |  |  |  |
| 2 | `AA.TC.AVAIL.ACTION` | `AaPrdDesTcAvailability_Action` |  |  |  |
| 3 | `AA.TC.AVAIL.DAY.NAME` | `AaPrdDesTcAvailability_DayName` |  |  |  |
| 4 | `AA.TC.AVAIL.DAY.SELECT` | `AaPrdDesTcAvailability_DaySelect` |  |  |  |
| 5 | `AA.TC.AVAIL.START.TIME` | `AaPrdDesTcAvailability_StartTime` |  |  |  |
| 6 | `AA.TC.AVAIL.END.TIME` | `AaPrdDesTcAvailability_EndTime` |  |  |  |
| 7 | `AA.TC.AVAIL.MASTER.LVL.CHANGE` | `AaPrdDesTcAvailability_MasterLvlChange` |  |  |  |
| 8 | `AA.TC.AVAIL.RESERVED1` | `AaPrdDesTcAvailability_Reserved1` |  |  |  |
| 9 | `AA.TC.AVAIL.LOCAL.REF` | `AaPrdDesTcAvailability_LocalRef` |  |  |  |
| 10 | `AA.TC.AVAIL.PR.ATTRIBUTE` | `AaPrdDesTcAvailability_PrAttribute` |  |  |  |
| 11 | `AA.TC.AVAIL.PR.VALUE` | `AaPrdDesTcAvailability_PrValue` |  |  |  |
| 12 | `AA.TC.AVAIL.PR.BRK.RES` | `AaPrdDesTcAvailability_PrBrkRes` |  |  |  |
| 13 | `AA.TC.AVAIL.PR.BRK.MSG` | `AaPrdDesTcAvailability_PrBrkMsg` |  |  |  |
| 14 | `AA.TC.AVAIL.PR.BRK.CHARGE` | `AaPrdDesTcAvailability_PrBrkCharge` |  |  |  |
| 15 | `AA.TC.AVAIL.PR.RESERVED.3` | `AaPrdDesTcAvailability_PrReserved3` |  |  |  |
| 16 | `AA.TC.AVAIL.PR.RESERVED.2` | `AaPrdDesTcAvailability_PrReserved2` |  |  |  |
| 17 | `AA.TC.AVAIL.PR.RESERVED.1` | `AaPrdDesTcAvailability_PrReserved1` |  |  |  |
| 18 | `AA.TC.AVAIL.PR.APP.METHOD` | `AaPrdDesTcAvailability_PrAppMethod` |  |  |  |
| 19 | `AA.TC.AVAIL.PR.APP.PERIOD` | `AaPrdDesTcAvailability_PrAppPeriod` |  |  |  |
| 20 | `AA.TC.AVAIL.SYS.RESERVE7` | `AaPrdDesTcAvailability_SysReserve7` |  |  |  |
| 21 | `AA.TC.AVAIL.SYS.RESERVE6` | `AaPrdDesTcAvailability_SysReserve6` |  |  |  |
| 22 | `AA.TC.AVAIL.OWNING.COMPANY` | `AaPrdDesTcAvailability_OwningCompany` |  |  |  |
| 23 | `AA.TC.AVAIL.API.ATTRIBUTE` | `AaPrdDesTcAvailability_ApiAttribute` |  |  |  |
| 24 | `AA.TC.AVAIL.SYS.RESERVE3` | `AaPrdDesTcAvailability_SysReserve3` |  |  |  |
| 25 | `AA.TC.AVAIL.SYS.RESERVE2` | `AaPrdDesTcAvailability_SysReserve2` |  |  |  |
| 26 | `AA.TC.AVAIL.SYS.RESERVE1` | `AaPrdDesTcAvailability_SysReserve1` |  |  |  |
| 27 | `AA.TC.AVAIL.DEFAULT.ATTR.OPTION` | `AaPrdDesTcAvailability_DefaultAttrOption` |  |  |  |
| 28 | `AA.TC.AVAIL.DEFAULT.NEGOTIABLE` | `AaPrdDesTcAvailability_DefaultNegotiable` |  |  |  |
| 29 | `AA.TC.AVAIL.NR.ATTRIBUTE` | `AaPrdDesTcAvailability_NrAttribute` |  |  |  |
| 30 | `AA.TC.AVAIL.NR.OPTIONS` | `AaPrdDesTcAvailability_NrOptions` |  |  |  |
| 31 | `AA.TC.AVAIL.NR.ATTRIBUTE.RULE` | `AaPrdDesTcAvailability_NrAttributeRule` |  |  |  |
| 32 | `AA.TC.AVAIL.NR.VALUE.SOURCE` | `AaPrdDesTcAvailability_NrValueSource` |  |  |  |
| 33 | `AA.TC.AVAIL.NR.STD.COMP` | `AaPrdDesTcAvailability_NrStdComp` |  |  |  |
| 34 | `AA.TC.AVAIL.NR.TYPE` | `AaPrdDesTcAvailability_NrType` |  |  |  |
| 35 | `AA.TC.AVAIL.NR.VALUE` | `AaPrdDesTcAvailability_NrValue` |  |  |  |
| 36 | `AA.TC.AVAIL.NR.MESSAGE` | `AaPrdDesTcAvailability_NrMessage` |  |  |  |
| 37 | `AA.TC.AVAIL.CHANGED.FIELDS` | `AaPrdDesTcAvailability_ChangedFields` |  |  |  |
| 38 | `AA.TC.AVAIL.NEGOTIATED.FLDS` | `AaPrdDesTcAvailability_NegotiatedFlds` |  |  |  |
| 39 | `AA.TC.AVAIL.ID.COMP.1` | `AaPrdDesTcAvailability_IdComp1` |  |  |  |
| 40 | `AA.TC.AVAIL.ID.COMP.2` | `AaPrdDesTcAvailability_IdComp2` |  |  |  |
| 41 | `AA.TC.AVAIL.ID.COMP.3` | `AaPrdDesTcAvailability_IdComp3` |  |  |  |
| 42 | `AA.TC.AVAIL.ID.COMP.4` | `AaPrdDesTcAvailability_IdComp4` |  |  |  |
| 43 | `AA.TC.AVAIL.ID.COMP.5` | `AaPrdDesTcAvailability_IdComp5` |  |  |  |
| 44 | `AA.TC.AVAIL.ID.COMP.6` | `AaPrdDesTcAvailability_IdComp6` |  |  |  |
| 45 | `AA.TC.AVAIL.RESERVED2.ID` | `AaPrdDesTcAvailability_Reserved2Id` |  |  |  |
| 46 | `AA.TC.AVAIL.TARGET.PRODUCT` | `AaPrdDesTcAvailability_TargetProduct` |  |  |  |
| 47 | `AA.TC.AVAIL.STMT.NOS` | `AaPrdDesTcAvailability_StmtNos` |  |  |  |
| 48 | `AA.TC.AVAIL.OVERRIDE` | `AaPrdDesTcAvailability_Override` |  |  |  |
| 49 | `AA.TC.AVAIL.RECORD.STATUS` | `AaPrdDesTcAvailability_RecordStatus` |  |  |  |
| 50 | `AA.TC.AVAIL.CURR.NO` | `AaPrdDesTcAvailability_CurrNo` |  |  |  |
| 51 | `AA.TC.AVAIL.INPUTTER` | `AaPrdDesTcAvailability_Inputter` |  |  |  |
| 52 | `AA.TC.AVAIL.DATE.TIME` | `AaPrdDesTcAvailability_DateTime` |  |  |  |
| 53 | `AA.TC.AVAIL.AUTHORISER` | `AaPrdDesTcAvailability_Authoriser` |  |  |  |
| 54 | `AA.TC.AVAIL.CO.CODE` | `AaPrdDesTcAvailability_CoCode` |  |  |  |
| 55 | `AA.TC.AVAIL.DEPT.CODE` | `AaPrdDesTcAvailability_DeptCode` |  |  |  |
| 56 | `AA.TC.AVAIL.AUDITOR.CODE` | `AaPrdDesTcAvailability_AuditorCode` |  |  |  |
| 57 | `AA.TC.AVAIL.AUDIT.DATE.TIME` | `AaPrdDesTcAvailability_AuditDateTime` |  |  |  |
