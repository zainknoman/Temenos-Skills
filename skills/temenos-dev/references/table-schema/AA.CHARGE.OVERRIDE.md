# AA.CHARGE.OVERRIDE — Table Schema

> Source: `INSERTS/I_F.AA.CHARGE.OVERRIDE` in `AA_ChargeOverride.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CO.ACTIVITY` | `AaSimChargeOverride_Activity` |  |  |  |
| 2 | `AA.CO.ACTION` | `AaSimChargeOverride_Action` |  |  |  |
| 3 | `AA.CO.PROPERTY` | `AaSimChargeOverride_Property` |  |  |  |
| 4 | `AA.CO.CHG.AMT` | `AaSimChargeOverride_ChgAmt` |  |  |  |
| 5 | `AA.CO.CHG.ACT.AMT` | `AaSimChargeOverride_ChgActAmt` |  |  |  |
| 6 | `AA.CO.CHG.DESC` | `AaSimChargeOverride_ChgDesc` |  |  |  |
| 7 | `AA.CO.CHG.TYPE` | `AaSimChargeOverride_ChgType` |  |  |  |
| 8 | `AA.CO.RESERVED.3` | `AaSimChargeOverride_Reserved3` |  |  |  |
| 9 | `AA.CO.RESERVED.2` | `AaSimChargeOverride_Reserved2` |  |  |  |
| 10 | `AA.CO.RESERVED.1` | `AaSimChargeOverride_Reserved1` |  |  |  |
| 11 | `AA.CO.RESERVED.6` | `AaSimChargeOverride_Reserved6` |  |  |  |
| 12 | `AA.CO.RESERVED.5` | `AaSimChargeOverride_Reserved5` |  |  |  |
| 13 | `AA.CO.RESERVED.4` | `AaSimChargeOverride_Reserved4` |  |  |  |
| 14 | `AA.CO.TOT.DEF.AMT` | `AaSimChargeOverride_TotDefAmt` |  |  |  |
| 15 | `AA.CO.TOT.ACT.AMT` | `AaSimChargeOverride_TotActAmt` |  |  |  |
| 16 | `AA.CO.RESERVED.7` | `AaSimChargeOverride_Reserved7` |  |  |  |
| 17 | `AA.CO.RESERVED.8` | `AaSimChargeOverride_Reserved8` |  |  |  |
| 18 | `AA.CO.RESERVED.9` | `AaSimChargeOverride_Reserved9` |  |  |  |
| 19 | `AA.CO.LOCAL.REF` | `AaSimChargeOverride_LocalRef` |  |  |  |
| 20 | `AA.CO.PR.ATTRIBUTE` | `AaSimChargeOverride_PrAttribute` |  |  |  |
| 21 | `AA.CO.PR.VALUE` | `AaSimChargeOverride_PrValue` |  |  |  |
| 22 | `AA.CO.PR.BRK.RES` | `AaSimChargeOverride_PrBrkRes` |  |  |  |
| 23 | `AA.CO.PR.BRK.MSG` | `AaSimChargeOverride_PrBrkMsg` |  |  |  |
| 24 | `AA.CO.PR.BRK.CHARGE` | `AaSimChargeOverride_PrBrkCharge` |  |  |  |
| 25 | `AA.CO.PR.RESERVED.3` | `AaSimChargeOverride_PrReserved3` |  |  |  |
| 26 | `AA.CO.PR.RESERVED.2` | `AaSimChargeOverride_PrReserved2` |  |  |  |
| 27 | `AA.CO.PR.RESERVED.1` | `AaSimChargeOverride_PrReserved1` |  |  |  |
| 28 | `AA.CO.PR.APP.METHOD` | `AaSimChargeOverride_PrAppMethod` |  |  |  |
| 29 | `AA.CO.PR.APP.PERIOD` | `AaSimChargeOverride_PrAppPeriod` |  |  |  |
| 30 | `AA.CO.SYS.RESERVE7` | `AaSimChargeOverride_SysReserve7` |  |  |  |
| 31 | `AA.CO.SYS.RESERVE6` | `AaSimChargeOverride_SysReserve6` |  |  |  |
| 32 | `AA.CO.OWNING.COMPANY` | `AaSimChargeOverride_OwningCompany` |  |  |  |
| 33 | `AA.CO.API.ATTRIBUTE` | `AaSimChargeOverride_ApiAttribute` |  |  |  |
| 34 | `AA.CO.SYS.RESERVE3` | `AaSimChargeOverride_SysReserve3` |  |  |  |
| 35 | `AA.CO.SYS.RESERVE2` | `AaSimChargeOverride_SysReserve2` |  |  |  |
| 36 | `AA.CO.SYS.RESERVE1` | `AaSimChargeOverride_SysReserve1` |  |  |  |
| 37 | `AA.CO.DEFAULT.ATTR.OPTION` | `AaSimChargeOverride_DefaultAttrOption` |  |  |  |
| 38 | `AA.CO.DEFAULT.NEGOTIABLE` | `AaSimChargeOverride_DefaultNegotiable` |  |  |  |
| 39 | `AA.CO.NR.ATTRIBUTE` | `AaSimChargeOverride_NrAttribute` |  |  |  |
| 40 | `AA.CO.NR.OPTIONS` | `AaSimChargeOverride_NrOptions` |  |  |  |
| 41 | `AA.CO.NR.ATTRIBUTE.RULE` | `AaSimChargeOverride_NrAttributeRule` |  |  |  |
| 42 | `AA.CO.NR.VALUE.SOURCE` | `AaSimChargeOverride_NrValueSource` |  |  |  |
| 43 | `AA.CO.NR.STD.COMP` | `AaSimChargeOverride_NrStdComp` |  |  |  |
| 44 | `AA.CO.NR.TYPE` | `AaSimChargeOverride_NrType` |  |  |  |
| 45 | `AA.CO.NR.VALUE` | `AaSimChargeOverride_NrValue` |  |  |  |
| 46 | `AA.CO.NR.MESSAGE` | `AaSimChargeOverride_NrMessage` |  |  |  |
| 47 | `AA.CO.CHANGED.FIELDS` | `AaSimChargeOverride_ChangedFields` |  |  |  |
| 48 | `AA.CO.NEGOTIATED.FLDS` | `AaSimChargeOverride_NegotiatedFlds` |  |  |  |
| 49 | `AA.CO.ID.COMP.1` | `AaSimChargeOverride_IdComp1` |  |  |  |
| 50 | `AA.CO.ID.COMP.2` | `AaSimChargeOverride_IdComp2` |  |  |  |
| 51 | `AA.CO.ID.COMP.3` | `AaSimChargeOverride_IdComp3` |  |  |  |
| 52 | `AA.CO.ID.COMP.4` | `AaSimChargeOverride_IdComp4` |  |  |  |
| 53 | `AA.CO.ID.COMP.5` | `AaSimChargeOverride_IdComp5` |  |  |  |
| 54 | `AA.CO.ID.COMP.6` | `AaSimChargeOverride_IdComp6` |  |  |  |
| 55 | `AA.CO.RESERVED2.ID` | `AaSimChargeOverride_Reserved2Id` |  |  |  |
| 56 | `AA.CO.TARGET.PRODUCT` | `AaSimChargeOverride_TargetProduct` |  |  |  |
| 57 | `AA.CO.STMT.NOS` | `AaSimChargeOverride_StmtNos` |  |  |  |
| 58 | `AA.CO.OVERRIDE` | `AaSimChargeOverride_Override` |  |  |  |
| 59 | `AA.CO.RECORD.STATUS` | `AaSimChargeOverride_RecordStatus` |  |  |  |
| 60 | `AA.CO.CURR.NO` | `AaSimChargeOverride_CurrNo` |  |  |  |
| 61 | `AA.CO.INPUTTER` | `AaSimChargeOverride_Inputter` |  |  |  |
| 62 | `AA.CO.DATE.TIME` | `AaSimChargeOverride_DateTime` |  |  |  |
| 63 | `AA.CO.AUTHORISER` | `AaSimChargeOverride_Authoriser` |  |  |  |
| 64 | `AA.CO.CO.CODE` | `AaSimChargeOverride_CoCode` |  |  |  |
| 65 | `AA.CO.DEPT.CODE` | `AaSimChargeOverride_DeptCode` |  |  |  |
| 66 | `AA.CO.AUDITOR.CODE` | `AaSimChargeOverride_AuditorCode` |  |  |  |
| 67 | `AA.CO.AUDIT.DATE.TIME` | `AaSimChargeOverride_AuditDateTime` |  |  |  |
