# AA.TAX — Table Schema

> Source: `INSERTS/I_F.AA.TAX` in `AA_Tax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.TAX.ACTIVITY` | `AaSimTax_Activity` |  |  |  |
| 2 | `AA.TAX.ACTION` | `AaSimTax_Action` |  |  |  |
| 3 | `AA.TAX.PROPERTY.CLASS` | `AaSimTax_PropertyClass` |  |  |  |
| 4 | `AA.TAX.TAX.CODE` | `AaSimTax_TaxCode` |  |  |  |
| 5 | `AA.TAX.TAX.CONDITION` | `AaSimTax_TaxCondition` |  |  |  |
| 6 | `AA.TAX.PROPERTY` | `AaSimTax_Property` |  |  |  |
| 7 | `AA.TAX.PROP.TAX.CODE` | `AaSimTax_PropTaxCode` |  |  |  |
| 8 | `AA.TAX.PROP.TAX.COND` | `AaSimTax_PropTaxCond` |  |  |  |
| 9 | `AA.TAX.NET.TAX` | `AaSimTax_NetTax` |  |  |  |
| 10 | `AA.TAX.PROP.NET.TAX` | `AaSimTax_PropNetTax` |  |  |  |
| 11 | `AA.TAX.RESERVED.5` | `AaSimTax_Reserved5` |  |  |  |
| 12 | `AA.TAX.RESERVED.4` | `AaSimTax_Reserved4` |  |  |  |
| 13 | `AA.TAX.RESERVED.3` | `AaSimTax_Reserved3` |  |  |  |
| 14 | `AA.TAX.RESERVED.2` | `AaSimTax_Reserved2` |  |  |  |
| 15 | `AA.TAX.RESERVED.1` | `AaSimTax_Reserved1` |  |  |  |
| 16 | `AA.TAX.LOCAL.REF` | `AaSimTax_LocalRef` |  |  |  |
| 17 | `AA.TAX.PR.ATTRIBUTE` | `AaSimTax_PrAttribute` |  |  |  |
| 18 | `AA.TAX.PR.VALUE` | `AaSimTax_PrValue` |  |  |  |
| 19 | `AA.TAX.PR.BRK.RES` | `AaSimTax_PrBrkRes` |  |  |  |
| 20 | `AA.TAX.PR.BRK.MSG` | `AaSimTax_PrBrkMsg` |  |  |  |
| 21 | `AA.TAX.PR.BRK.CHARGE` | `AaSimTax_PrBrkCharge` |  |  |  |
| 22 | `AA.TAX.PR.RESERVED.3` | `AaSimTax_PrReserved3` |  |  |  |
| 23 | `AA.TAX.PR.RESERVED.2` | `AaSimTax_PrReserved2` |  |  |  |
| 24 | `AA.TAX.PR.RESERVED.1` | `AaSimTax_PrReserved1` |  |  |  |
| 25 | `AA.TAX.PR.APP.METHOD` | `AaSimTax_PrAppMethod` |  |  |  |
| 26 | `AA.TAX.PR.APP.PERIOD` | `AaSimTax_PrAppPeriod` |  |  |  |
| 27 | `AA.TAX.SYS.RESERVE7` | `AaSimTax_SysReserve7` |  |  |  |
| 28 | `AA.TAX.SYS.RESERVE6` | `AaSimTax_SysReserve6` |  |  |  |
| 29 | `AA.TAX.OWNING.COMPANY` | `AaSimTax_OwningCompany` |  |  |  |
| 30 | `AA.TAX.API.ATTRIBUTE` | `AaSimTax_ApiAttribute` |  |  |  |
| 31 | `AA.TAX.SYS.RESERVE3` | `AaSimTax_SysReserve3` |  |  |  |
| 32 | `AA.TAX.SYS.RESERVE2` | `AaSimTax_SysReserve2` |  |  |  |
| 33 | `AA.TAX.SYS.RESERVE1` | `AaSimTax_SysReserve1` |  |  |  |
| 34 | `AA.TAX.DEFAULT.ATTR.OPTION` | `AaSimTax_DefaultAttrOption` |  |  |  |
| 35 | `AA.TAX.DEFAULT.NEGOTIABLE` | `AaSimTax_DefaultNegotiable` |  |  |  |
| 36 | `AA.TAX.NR.ATTRIBUTE` | `AaSimTax_NrAttribute` |  |  |  |
| 37 | `AA.TAX.NR.OPTIONS` | `AaSimTax_NrOptions` |  |  |  |
| 38 | `AA.TAX.NR.ATTRIBUTE.RULE` | `AaSimTax_NrAttributeRule` |  |  |  |
| 39 | `AA.TAX.NR.VALUE.SOURCE` | `AaSimTax_NrValueSource` |  |  |  |
| 40 | `AA.TAX.NR.STD.COMP` | `AaSimTax_NrStdComp` |  |  |  |
| 41 | `AA.TAX.NR.TYPE` | `AaSimTax_NrType` |  |  |  |
| 42 | `AA.TAX.NR.VALUE` | `AaSimTax_NrValue` |  |  |  |
| 43 | `AA.TAX.NR.MESSAGE` | `AaSimTax_NrMessage` |  |  |  |
| 44 | `AA.TAX.CHANGED.FIELDS` | `AaSimTax_ChangedFields` |  |  |  |
| 45 | `AA.TAX.NEGOTIATED.FLDS` | `AaSimTax_NegotiatedFlds` |  |  |  |
| 46 | `AA.TAX.ID.COMP.1` | `AaSimTax_IdComp1` |  |  |  |
| 47 | `AA.TAX.ID.COMP.2` | `AaSimTax_IdComp2` |  |  |  |
| 48 | `AA.TAX.ID.COMP.3` | `AaSimTax_IdComp3` |  |  |  |
| 49 | `AA.TAX.ID.COMP.4` | `AaSimTax_IdComp4` |  |  |  |
| 50 | `AA.TAX.ID.COMP.5` | `AaSimTax_IdComp5` |  |  |  |
| 51 | `AA.TAX.ID.COMP.6` | `AaSimTax_IdComp6` |  |  |  |
| 52 | `AA.TAX.RESERVED2.ID` | `AaSimTax_Reserved2Id` |  |  |  |
| 53 | `AA.TAX.TARGET.PRODUCT` | `AaSimTax_TargetProduct` |  |  |  |
| 54 | `AA.TAX.STMT.NOS` | `AaSimTax_StmtNos` |  |  |  |
| 55 | `AA.TAX.OVERRIDE` | `AaSimTax_Override` |  |  |  |
| 56 | `AA.TAX.RECORD.STATUS` | `AaSimTax_RecordStatus` |  |  |  |
| 57 | `AA.TAX.CURR.NO` | `AaSimTax_CurrNo` |  |  |  |
| 58 | `AA.TAX.INPUTTER` | `AaSimTax_Inputter` |  |  |  |
| 59 | `AA.TAX.DATE.TIME` | `AaSimTax_DateTime` |  |  |  |
| 60 | `AA.TAX.AUTHORISER` | `AaSimTax_Authoriser` |  |  |  |
| 61 | `AA.TAX.CO.CODE` | `AaSimTax_CoCode` |  |  |  |
| 62 | `AA.TAX.DEPT.CODE` | `AaSimTax_DeptCode` |  |  |  |
| 63 | `AA.TAX.AUDITOR.CODE` | `AaSimTax_AuditorCode` |  |  |  |
| 64 | `AA.TAX.AUDIT.DATE.TIME` | `AaSimTax_AuditDateTime` |  |  |  |
