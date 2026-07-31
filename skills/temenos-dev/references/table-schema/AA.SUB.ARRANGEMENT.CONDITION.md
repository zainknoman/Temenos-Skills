# AA.SUB.ARRANGEMENT.CONDITION — Table Schema

> Source: `INSERTS/I_F.AA.SUB.ARRANGEMENT.CONDITION` in `AA_SubArrangementCondition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SAC.ACTIVITY` | `AaSimSubArrangementCondition_Activity` |  |  |  |
| 2 | `AA.SAC.ACTION` | `AaSimSubArrangementCondition_Action` |  |  |  |
| 3 | `AA.SAC.PRODUCT.LINE` | `AaSimSubArrangementCondition_ProductLine` |  |  |  |
| 4 | `AA.SAC.PRODUCT.GROUP` | `AaSimSubArrangementCondition_ProductGroup` |  |  |  |
| 5 | `AA.SAC.PRODUCT` | `AaSimSubArrangementCondition_Product` |  |  |  |
| 6 | `AA.SAC.CURRENCY` | `AaSimSubArrangementCondition_Currency` |  |  |  |
| 7 | `AA.SAC.PROPERTY` | `AaSimSubArrangementCondition_Property` |  |  |  |
| 8 | `AA.SAC.RESERVED.1` | `AaSimSubArrangementCondition_Reserved1` |  |  |  |
| 9 | `AA.SAC.RESERVED.2` | `AaSimSubArrangementCondition_Reserved2` |  |  |  |
| 10 | `AA.SAC.ATTRIBUTE` | `AaSimSubArrangementCondition_Attribute` |  |  |  |
| 11 | `AA.SAC.VALUE` | `AaSimSubArrangementCondition_Value` |  |  |  |
| 12 | `AA.SAC.MESSAGE` | `AaSimSubArrangementCondition_Message` |  |  |  |
| 13 | `AA.SAC.RESERVED.3` | `AaSimSubArrangementCondition_Reserved3` |  |  |  |
| 14 | `AA.SAC.RESERVED.4` | `AaSimSubArrangementCondition_Reserved4` |  |  |  |
| 15 | `AA.SAC.PROPERTY.CLASS` | `AaSimSubArrangementCondition_PropertyClass` |  |  |  |
| 16 | `AA.SAC.SYS.ATTRIBUTE` | `AaSimSubArrangementCondition_SysAttribute` |  |  |  |
| 17 | `AA.SAC.TYPE` | `AaSimSubArrangementCondition_Type` |  |  |  |
| 18 | `AA.SAC.LINK` | `AaSimSubArrangementCondition_Link` |  |  |  |
| 19 | `AA.SAC.RESERVED.5` | `AaSimSubArrangementCondition_Reserved5` |  |  |  |
| 20 | `AA.SAC.LOCAL.REF` | `AaSimSubArrangementCondition_LocalRef` |  |  |  |
| 21 | `AA.SAC.PR.ATTRIBUTE` | `AaSimSubArrangementCondition_PrAttribute` |  |  |  |
| 22 | `AA.SAC.PR.VALUE` | `AaSimSubArrangementCondition_PrValue` |  |  |  |
| 23 | `AA.SAC.PR.BRK.RES` | `AaSimSubArrangementCondition_PrBrkRes` |  |  |  |
| 24 | `AA.SAC.PR.BRK.MSG` | `AaSimSubArrangementCondition_PrBrkMsg` |  |  |  |
| 25 | `AA.SAC.PR.BRK.CHARGE` | `AaSimSubArrangementCondition_PrBrkCharge` |  |  |  |
| 26 | `AA.SAC.PR.RESERVED.3` | `AaSimSubArrangementCondition_PrReserved3` |  |  |  |
| 27 | `AA.SAC.PR.RESERVED.2` | `AaSimSubArrangementCondition_PrReserved2` |  |  |  |
| 28 | `AA.SAC.PR.RESERVED.1` | `AaSimSubArrangementCondition_PrReserved1` |  |  |  |
| 29 | `AA.SAC.PR.APP.METHOD` | `AaSimSubArrangementCondition_PrAppMethod` |  |  |  |
| 30 | `AA.SAC.PR.APP.PERIOD` | `AaSimSubArrangementCondition_PrAppPeriod` |  |  |  |
| 31 | `AA.SAC.SYS.RESERVE7` | `AaSimSubArrangementCondition_SysReserve7` |  |  |  |
| 32 | `AA.SAC.SYS.RESERVE6` | `AaSimSubArrangementCondition_SysReserve6` |  |  |  |
| 33 | `AA.SAC.OWNING.COMPANY` | `AaSimSubArrangementCondition_OwningCompany` |  |  |  |
| 34 | `AA.SAC.API.ATTRIBUTE` | `AaSimSubArrangementCondition_ApiAttribute` |  |  |  |
| 35 | `AA.SAC.SYS.RESERVE3` | `AaSimSubArrangementCondition_SysReserve3` |  |  |  |
| 36 | `AA.SAC.SYS.RESERVE2` | `AaSimSubArrangementCondition_SysReserve2` |  |  |  |
| 37 | `AA.SAC.SYS.RESERVE1` | `AaSimSubArrangementCondition_SysReserve1` |  |  |  |
| 38 | `AA.SAC.DEFAULT.ATTR.OPTION` | `AaSimSubArrangementCondition_DefaultAttrOption` |  |  |  |
| 39 | `AA.SAC.DEFAULT.NEGOTIABLE` | `AaSimSubArrangementCondition_DefaultNegotiable` |  |  |  |
| 40 | `AA.SAC.NR.ATTRIBUTE` | `AaSimSubArrangementCondition_NrAttribute` |  |  |  |
| 41 | `AA.SAC.NR.OPTIONS` | `AaSimSubArrangementCondition_NrOptions` |  |  |  |
| 42 | `AA.SAC.NR.ATTRIBUTE.RULE` | `AaSimSubArrangementCondition_NrAttributeRule` |  |  |  |
| 43 | `AA.SAC.NR.VALUE.SOURCE` | `AaSimSubArrangementCondition_NrValueSource` |  |  |  |
| 44 | `AA.SAC.NR.STD.COMP` | `AaSimSubArrangementCondition_NrStdComp` |  |  |  |
| 45 | `AA.SAC.NR.TYPE` | `AaSimSubArrangementCondition_NrType` |  |  |  |
| 46 | `AA.SAC.NR.VALUE` | `AaSimSubArrangementCondition_NrValue` |  |  |  |
| 47 | `AA.SAC.NR.MESSAGE` | `AaSimSubArrangementCondition_NrMessage` |  |  |  |
| 48 | `AA.SAC.CHANGED.FIELDS` | `AaSimSubArrangementCondition_ChangedFields` |  |  |  |
| 49 | `AA.SAC.NEGOTIATED.FLDS` | `AaSimSubArrangementCondition_NegotiatedFlds` |  |  |  |
| 50 | `AA.SAC.ID.COMP.1` | `AaSimSubArrangementCondition_IdComp1` |  |  |  |
| 51 | `AA.SAC.ID.COMP.2` | `AaSimSubArrangementCondition_IdComp2` |  |  |  |
| 52 | `AA.SAC.ID.COMP.3` | `AaSimSubArrangementCondition_IdComp3` |  |  |  |
| 53 | `AA.SAC.ID.COMP.4` | `AaSimSubArrangementCondition_IdComp4` |  |  |  |
| 54 | `AA.SAC.ID.COMP.5` | `AaSimSubArrangementCondition_IdComp5` |  |  |  |
| 55 | `AA.SAC.ID.COMP.6` | `AaSimSubArrangementCondition_IdComp6` |  |  |  |
| 56 | `AA.SAC.RESERVED2.ID` | `AaSimSubArrangementCondition_Reserved2Id` |  |  |  |
| 57 | `AA.SAC.TARGET.PRODUCT` | `AaSimSubArrangementCondition_TargetProduct` |  |  |  |
| 58 | `AA.SAC.STMT.NOS` | `AaSimSubArrangementCondition_StmtNos` |  |  |  |
| 59 | `AA.SAC.OVERRIDE` | `AaSimSubArrangementCondition_Override` |  |  |  |
| 60 | `AA.SAC.RECORD.STATUS` | `AaSimSubArrangementCondition_RecordStatus` |  |  |  |
| 61 | `AA.SAC.CURR.NO` | `AaSimSubArrangementCondition_CurrNo` |  |  |  |
| 62 | `AA.SAC.INPUTTER` | `AaSimSubArrangementCondition_Inputter` |  |  |  |
| 63 | `AA.SAC.DATE.TIME` | `AaSimSubArrangementCondition_DateTime` |  |  |  |
| 64 | `AA.SAC.AUTHORISER` | `AaSimSubArrangementCondition_Authoriser` |  |  |  |
| 65 | `AA.SAC.CO.CODE` | `AaSimSubArrangementCondition_CoCode` |  |  |  |
| 66 | `AA.SAC.DEPT.CODE` | `AaSimSubArrangementCondition_DeptCode` |  |  |  |
| 67 | `AA.SAC.AUDITOR.CODE` | `AaSimSubArrangementCondition_AuditorCode` |  |  |  |
| 68 | `AA.SAC.AUDIT.DATE.TIME` | `AaSimSubArrangementCondition_AuditDateTime` |  |  |  |
