# AA.RESTRUCTURE.RULES — Table Schema

> Source: `INSERTS/I_F.AA.RESTRUCTURE.RULES` in `AA_RestructureRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.RSR.ACTIVITY` | `AaSimRestructureRules_Activity` |  |  |  |
| 2 | `AA.RSR.ACTION` | `AaSimRestructureRules_Action` |  |  |  |
| 3 | `AA.RSR.RULE.STATUS.TYPE` | `AaSimRestructureRules_RuleStatusType` |  |  |  |
| 4 | `AA.RSR.RULE.STATUS` | `AaSimRestructureRules_RuleStatus` |  |  |  |
| 5 | `AA.RSR.RESERVED.8` | `AaSimRestructureRules_Reserved8` |  |  |  |
| 6 | `AA.RSR.RESERVED.7` | `AaSimRestructureRules_Reserved7` |  |  |  |
| 7 | `AA.RSR.PROPERTY.CLASS` | `AaSimRestructureRules_PropertyClass` |  |  |  |
| 8 | `AA.RSR.PROPERTY` | `AaSimRestructureRules_Property` |  |  |  |
| 9 | `AA.RSR.RULE.ACTION` | `AaSimRestructureRules_RuleAction` |  |  |  |
| 10 | `AA.RSR.RESERVED.6` | `AaSimRestructureRules_Reserved6` |  |  |  |
| 11 | `AA.RSR.EFFECTIVE.DATE` | `AaSimRestructureRules_EffectiveDate` |  |  |  |
| 12 | `AA.RSR.RESERVED.5` | `AaSimRestructureRules_Reserved5` |  |  |  |
| 13 | `AA.RSR.RESERVED.4` | `AaSimRestructureRules_Reserved4` |  |  |  |
| 14 | `AA.RSR.RESERVED.3` | `AaSimRestructureRules_Reserved3` |  |  |  |
| 15 | `AA.RSR.RESERVED.2` | `AaSimRestructureRules_Reserved2` |  |  |  |
| 16 | `AA.RSR.RESERVED.1` | `AaSimRestructureRules_Reserved1` |  |  |  |
| 17 | `AA.RSR.LOCAL.REF` | `AaSimRestructureRules_LocalRef` |  |  |  |
| 18 | `AA.RSR.PR.ATTRIBUTE` | `AaSimRestructureRules_PrAttribute` |  |  |  |
| 19 | `AA.RSR.PR.VALUE` | `AaSimRestructureRules_PrValue` |  |  |  |
| 20 | `AA.RSR.PR.BRK.RES` | `AaSimRestructureRules_PrBrkRes` |  |  |  |
| 21 | `AA.RSR.PR.BRK.MSG` | `AaSimRestructureRules_PrBrkMsg` |  |  |  |
| 22 | `AA.RSR.PR.BRK.CHARGE` | `AaSimRestructureRules_PrBrkCharge` |  |  |  |
| 23 | `AA.RSR.PR.RESERVED.3` | `AaSimRestructureRules_PrReserved3` |  |  |  |
| 24 | `AA.RSR.PR.RESERVED.2` | `AaSimRestructureRules_PrReserved2` |  |  |  |
| 25 | `AA.RSR.PR.RESERVED.1` | `AaSimRestructureRules_PrReserved1` |  |  |  |
| 26 | `AA.RSR.PR.APP.METHOD` | `AaSimRestructureRules_PrAppMethod` |  |  |  |
| 27 | `AA.RSR.PR.APP.PERIOD` | `AaSimRestructureRules_PrAppPeriod` |  |  |  |
| 28 | `AA.RSR.SYS.RESERVE7` | `AaSimRestructureRules_SysReserve7` |  |  |  |
| 29 | `AA.RSR.SYS.RESERVE6` | `AaSimRestructureRules_SysReserve6` |  |  |  |
| 30 | `AA.RSR.OWNING.COMPANY` | `AaSimRestructureRules_OwningCompany` |  |  |  |
| 31 | `AA.RSR.API.ATTRIBUTE` | `AaSimRestructureRules_ApiAttribute` |  |  |  |
| 32 | `AA.RSR.SYS.RESERVE3` | `AaSimRestructureRules_SysReserve3` |  |  |  |
| 33 | `AA.RSR.SYS.RESERVE2` | `AaSimRestructureRules_SysReserve2` |  |  |  |
| 34 | `AA.RSR.SYS.RESERVE1` | `AaSimRestructureRules_SysReserve1` |  |  |  |
| 35 | `AA.RSR.DEFAULT.ATTR.OPTION` | `AaSimRestructureRules_DefaultAttrOption` |  |  |  |
| 36 | `AA.RSR.DEFAULT.NEGOTIABLE` | `AaSimRestructureRules_DefaultNegotiable` |  |  |  |
| 37 | `AA.RSR.NR.ATTRIBUTE` | `AaSimRestructureRules_NrAttribute` |  |  |  |
| 38 | `AA.RSR.NR.OPTIONS` | `AaSimRestructureRules_NrOptions` |  |  |  |
| 39 | `AA.RSR.NR.ATTRIBUTE.RULE` | `AaSimRestructureRules_NrAttributeRule` |  |  |  |
| 40 | `AA.RSR.NR.VALUE.SOURCE` | `AaSimRestructureRules_NrValueSource` |  |  |  |
| 41 | `AA.RSR.NR.STD.COMP` | `AaSimRestructureRules_NrStdComp` |  |  |  |
| 42 | `AA.RSR.NR.TYPE` | `AaSimRestructureRules_NrType` |  |  |  |
| 43 | `AA.RSR.NR.VALUE` | `AaSimRestructureRules_NrValue` |  |  |  |
| 44 | `AA.RSR.NR.MESSAGE` | `AaSimRestructureRules_NrMessage` |  |  |  |
| 45 | `AA.RSR.CHANGED.FIELDS` | `AaSimRestructureRules_ChangedFields` |  |  |  |
| 46 | `AA.RSR.NEGOTIATED.FLDS` | `AaSimRestructureRules_NegotiatedFlds` |  |  |  |
| 47 | `AA.RSR.ID.COMP.1` | `AaSimRestructureRules_IdComp1` |  |  |  |
| 48 | `AA.RSR.ID.COMP.2` | `AaSimRestructureRules_IdComp2` |  |  |  |
| 49 | `AA.RSR.ID.COMP.3` | `AaSimRestructureRules_IdComp3` |  |  |  |
| 50 | `AA.RSR.ID.COMP.4` | `AaSimRestructureRules_IdComp4` |  |  |  |
| 51 | `AA.RSR.ID.COMP.5` | `AaSimRestructureRules_IdComp5` |  |  |  |
| 52 | `AA.RSR.ID.COMP.6` | `AaSimRestructureRules_IdComp6` |  |  |  |
| 53 | `AA.RSR.RESERVED2.ID` | `AaSimRestructureRules_Reserved2Id` |  |  |  |
| 54 | `AA.RSR.TARGET.PRODUCT` | `AaSimRestructureRules_TargetProduct` |  |  |  |
| 55 | `AA.RSR.STMT.NOS` | `AaSimRestructureRules_StmtNos` |  |  |  |
| 56 | `AA.RSR.OVERRIDE` | `AaSimRestructureRules_Override` |  |  |  |
| 57 | `AA.RSR.RECORD.STATUS` | `AaSimRestructureRules_RecordStatus` |  |  |  |
| 58 | `AA.RSR.CURR.NO` | `AaSimRestructureRules_CurrNo` |  |  |  |
| 59 | `AA.RSR.INPUTTER` | `AaSimRestructureRules_Inputter` |  |  |  |
| 60 | `AA.RSR.DATE.TIME` | `AaSimRestructureRules_DateTime` |  |  |  |
| 61 | `AA.RSR.AUTHORISER` | `AaSimRestructureRules_Authoriser` |  |  |  |
| 62 | `AA.RSR.CO.CODE` | `AaSimRestructureRules_CoCode` |  |  |  |
| 63 | `AA.RSR.DEPT.CODE` | `AaSimRestructureRules_DeptCode` |  |  |  |
| 64 | `AA.RSR.AUDITOR.CODE` | `AaSimRestructureRules_AuditorCode` |  |  |  |
| 65 | `AA.RSR.AUDIT.DATE.TIME` | `AaSimRestructureRules_AuditDateTime` |  |  |  |
