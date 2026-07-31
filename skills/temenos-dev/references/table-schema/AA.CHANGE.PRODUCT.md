# AA.CHANGE.PRODUCT — Table Schema

> Source: `INSERTS/I_F.AA.CHANGE.PRODUCT` in `AA_ChangeProduct.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CP.ACTIVITY` | `AaSimChangeProduct_Activity` |  |  |  |
| 2 | `AA.CP.ACTION` | `AaSimChangeProduct_Action` |  |  |  |
| 3 | `AA.CP.CHANGE.DATE.TYPE` | `AaSimChangeProduct_ChangeDateType` |  |  |  |
| 4 | `AA.CP.CHANGE.PERIOD` | `AaSimChangeProduct_ChangePeriod` |  |  |  |
| 5 | `AA.CP.CHANGE.DATE` | `AaSimChangeProduct_ChangeDate` |  |  |  |
| 6 | `AA.CP.CHANGE.ACTIVITY` | `AaSimChangeProduct_ChangeActivity` |  |  |  |
| 7 | `AA.CP.PRIOR.DAYS` | `AaSimChangeProduct_PriorDays` |  |  |  |
| 8 | `AA.CP.CHG.TO.PRODUCT` | `AaSimChangeProduct_ChgToProduct` |  |  |  |
| 9 | `AA.CP.ALLOWED.PRODUCT` | `AaSimChangeProduct_AllowedProduct` |  |  |  |
| 10 | `AA.CP.RESERVED.6` | `AaSimChangeProduct_Reserved6` |  |  |  |
| 11 | `AA.CP.RESERVED.5` | `AaSimChangeProduct_Reserved5` |  |  |  |
| 12 | `AA.CP.INITIATION.TYPE` | `AaSimChangeProduct_InitiationType` |  |  |  |
| 13 | `AA.CP.DEFAULT.ACTIVITY` | `AaSimChangeProduct_DefaultActivity` |  |  |  |
| 14 | `AA.CP.RESERVED.4` | `AaSimChangeProduct_Reserved4` |  |  |  |
| 15 | `AA.CP.RESERVED.3` | `AaSimChangeProduct_Reserved3` |  |  |  |
| 16 | `AA.CP.RESERVED.2` | `AaSimChangeProduct_Reserved2` |  |  |  |
| 17 | `AA.CP.RESERVED.1` | `AaSimChangeProduct_Reserved1` |  |  |  |
| 18 | `AA.CP.LOCAL.REF` | `AaSimChangeProduct_LocalRef` |  |  |  |
| 19 | `AA.CP.PR.ATTRIBUTE` | `AaSimChangeProduct_PrAttribute` |  |  |  |
| 20 | `AA.CP.PR.VALUE` | `AaSimChangeProduct_PrValue` |  |  |  |
| 21 | `AA.CP.PR.BRK.RES` | `AaSimChangeProduct_PrBrkRes` |  |  |  |
| 22 | `AA.CP.PR.BRK.MSG` | `AaSimChangeProduct_PrBrkMsg` |  |  |  |
| 23 | `AA.CP.PR.BRK.CHARGE` | `AaSimChangeProduct_PrBrkCharge` |  |  |  |
| 24 | `AA.CP.PR.RESERVED.3` | `AaSimChangeProduct_PrReserved3` |  |  |  |
| 25 | `AA.CP.PR.RESERVED.2` | `AaSimChangeProduct_PrReserved2` |  |  |  |
| 26 | `AA.CP.PR.RESERVED.1` | `AaSimChangeProduct_PrReserved1` |  |  |  |
| 27 | `AA.CP.PR.APP.METHOD` | `AaSimChangeProduct_PrAppMethod` |  |  |  |
| 28 | `AA.CP.PR.APP.PERIOD` | `AaSimChangeProduct_PrAppPeriod` |  |  |  |
| 29 | `AA.CP.SYS.RESERVE7` | `AaSimChangeProduct_SysReserve7` |  |  |  |
| 30 | `AA.CP.SYS.RESERVE6` | `AaSimChangeProduct_SysReserve6` |  |  |  |
| 31 | `AA.CP.OWNING.COMPANY` | `AaSimChangeProduct_OwningCompany` |  |  |  |
| 32 | `AA.CP.API.ATTRIBUTE` | `AaSimChangeProduct_ApiAttribute` |  |  |  |
| 33 | `AA.CP.SYS.RESERVE3` | `AaSimChangeProduct_SysReserve3` |  |  |  |
| 34 | `AA.CP.SYS.RESERVE2` | `AaSimChangeProduct_SysReserve2` |  |  |  |
| 35 | `AA.CP.SYS.RESERVE1` | `AaSimChangeProduct_SysReserve1` |  |  |  |
| 36 | `AA.CP.DEFAULT.ATTR.OPTION` | `AaSimChangeProduct_DefaultAttrOption` |  |  |  |
| 37 | `AA.CP.DEFAULT.NEGOTIABLE` | `AaSimChangeProduct_DefaultNegotiable` |  |  |  |
| 38 | `AA.CP.NR.ATTRIBUTE` | `AaSimChangeProduct_NrAttribute` |  |  |  |
| 39 | `AA.CP.NR.OPTIONS` | `AaSimChangeProduct_NrOptions` |  |  |  |
| 40 | `AA.CP.NR.ATTRIBUTE.RULE` | `AaSimChangeProduct_NrAttributeRule` |  |  |  |
| 41 | `AA.CP.NR.VALUE.SOURCE` | `AaSimChangeProduct_NrValueSource` |  |  |  |
| 42 | `AA.CP.NR.STD.COMP` | `AaSimChangeProduct_NrStdComp` |  |  |  |
| 43 | `AA.CP.NR.TYPE` | `AaSimChangeProduct_NrType` |  |  |  |
| 44 | `AA.CP.NR.VALUE` | `AaSimChangeProduct_NrValue` |  |  |  |
| 45 | `AA.CP.NR.MESSAGE` | `AaSimChangeProduct_NrMessage` |  |  |  |
| 46 | `AA.CP.CHANGED.FIELDS` | `AaSimChangeProduct_ChangedFields` |  |  |  |
| 47 | `AA.CP.NEGOTIATED.FLDS` | `AaSimChangeProduct_NegotiatedFlds` |  |  |  |
| 48 | `AA.CP.ID.COMP.1` | `AaSimChangeProduct_IdComp1` |  |  |  |
| 49 | `AA.CP.ID.COMP.2` | `AaSimChangeProduct_IdComp2` |  |  |  |
| 50 | `AA.CP.ID.COMP.3` | `AaSimChangeProduct_IdComp3` |  |  |  |
| 51 | `AA.CP.ID.COMP.4` | `AaSimChangeProduct_IdComp4` |  |  |  |
| 52 | `AA.CP.ID.COMP.5` | `AaSimChangeProduct_IdComp5` |  |  |  |
| 53 | `AA.CP.ID.COMP.6` | `AaSimChangeProduct_IdComp6` |  |  |  |
| 54 | `AA.CP.RESERVED2.ID` | `AaSimChangeProduct_Reserved2Id` |  |  |  |
| 55 | `AA.CP.TARGET.PRODUCT` | `AaSimChangeProduct_TargetProduct` |  |  |  |
| 56 | `AA.CP.STMT.NOS` | `AaSimChangeProduct_StmtNos` |  |  |  |
| 57 | `AA.CP.OVERRIDE` | `AaSimChangeProduct_Override` |  |  |  |
| 58 | `AA.CP.RECORD.STATUS` | `AaSimChangeProduct_RecordStatus` |  |  |  |
| 59 | `AA.CP.CURR.NO` | `AaSimChangeProduct_CurrNo` |  |  |  |
| 60 | `AA.CP.INPUTTER` | `AaSimChangeProduct_Inputter` |  |  |  |
| 61 | `AA.CP.DATE.TIME` | `AaSimChangeProduct_DateTime` |  |  |  |
| 62 | `AA.CP.AUTHORISER` | `AaSimChangeProduct_Authoriser` |  |  |  |
| 63 | `AA.CP.CO.CODE` | `AaSimChangeProduct_CoCode` |  |  |  |
| 64 | `AA.CP.DEPT.CODE` | `AaSimChangeProduct_DeptCode` |  |  |  |
| 65 | `AA.CP.AUDITOR.CODE` | `AaSimChangeProduct_AuditorCode` |  |  |  |
| 66 | `AA.CP.AUDIT.DATE.TIME` | `AaSimChangeProduct_AuditDateTime` |  |  |  |
