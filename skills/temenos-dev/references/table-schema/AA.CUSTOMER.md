# AA.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.AA.CUSTOMER` in `AA_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CUS.ACTIVITY` | `AaSimCustomer_Activity` |  |  |  |
| 2 | `AA.CUS.ACTION` | `AaSimCustomer_Action` |  |  |  |
| 3 | `AA.CUS.CUSTOMER` | `AaSimCustomer_Customer` |  |  |  |
| 4 | `AA.CUS.CUSTOMER.ROLE` | `AaSimCustomer_CustomerRole` |  |  |  |
| 5 | `AA.CUS.TAX.LIABILITY.PERC` | `AaSimCustomer_TaxLiabilityPerc` |  |  |  |
| 6 | `AA.CUS.LIMIT.ALLOC.PERC` | `AaSimCustomer_LimitAllocPerc` |  |  |  |
| 7 | `AA.CUS.GL.ALLOC.PERC` | `AaSimCustomer_GlAllocPerc` |  |  |  |
| 8 | `AA.CUS.DELIVERY.REQD` | `AaSimCustomer_DeliveryReqd` |  |  |  |
| 9 | `AA.CUS.RESERVED.9` | `AaSimCustomer_Reserved9` |  |  |  |
| 10 | `AA.CUS.RESERVED.8` | `AaSimCustomer_Reserved8` |  |  |  |
| 11 | `AA.CUS.RESERVED.7` | `AaSimCustomer_Reserved7` |  |  |  |
| 12 | `AA.CUS.JS.LIABLE` | `AaSimCustomer_JsLiable` |  |  |  |
| 13 | `AA.CUS.OTHER.PARTY` | `AaSimCustomer_OtherParty` |  |  |  |
| 14 | `AA.CUS.ROLE` | `AaSimCustomer_Role` |  |  |  |
| 15 | `AA.CUS.NOTES` | `AaSimCustomer_Notes` |  |  |  |
| 16 | `AA.CUS.CRA.CUSTOMER` | `AaSimCustomer_CraCustomer` |  |  |  |
| 17 | `AA.CUS.RESERVED.4` | `AaSimCustomer_Reserved4` |  |  |  |
| 18 | `AA.CUS.RESERVED.3` | `AaSimCustomer_Reserved3` |  |  |  |
| 19 | `AA.CUS.RESERVED.2` | `AaSimCustomer_Reserved2` |  |  |  |
| 20 | `AA.CUS.RESERVED.1` | `AaSimCustomer_Reserved1` |  |  |  |
| 21 | `AA.CUS.LOCAL.REF` | `AaSimCustomer_LocalRef` |  |  |  |
| 22 | `AA.CUS.PR.ATTRIBUTE` | `AaSimCustomer_PrAttribute` |  |  |  |
| 23 | `AA.CUS.PR.VALUE` | `AaSimCustomer_PrValue` |  |  |  |
| 24 | `AA.CUS.PR.BRK.RES` | `AaSimCustomer_PrBrkRes` |  |  |  |
| 25 | `AA.CUS.PR.BRK.MSG` | `AaSimCustomer_PrBrkMsg` |  |  |  |
| 26 | `AA.CUS.PR.BRK.CHARGE` | `AaSimCustomer_PrBrkCharge` |  |  |  |
| 27 | `AA.CUS.PR.RESERVED.3` | `AaSimCustomer_PrReserved3` |  |  |  |
| 28 | `AA.CUS.PR.RESERVED.2` | `AaSimCustomer_PrReserved2` |  |  |  |
| 29 | `AA.CUS.PR.RESERVED.1` | `AaSimCustomer_PrReserved1` |  |  |  |
| 30 | `AA.CUS.PR.APP.METHOD` | `AaSimCustomer_PrAppMethod` |  |  |  |
| 31 | `AA.CUS.PR.APP.PERIOD` | `AaSimCustomer_PrAppPeriod` |  |  |  |
| 32 | `AA.CUS.SYS.RESERVE7` | `AaSimCustomer_SysReserve7` |  |  |  |
| 33 | `AA.CUS.SYS.RESERVE6` | `AaSimCustomer_SysReserve6` |  |  |  |
| 34 | `AA.CUS.OWNING.COMPANY` | `AaSimCustomer_OwningCompany` |  |  |  |
| 35 | `AA.CUS.API.ATTRIBUTE` | `AaSimCustomer_ApiAttribute` |  |  |  |
| 36 | `AA.CUS.SYS.RESERVE3` | `AaSimCustomer_SysReserve3` |  |  |  |
| 37 | `AA.CUS.SYS.RESERVE2` | `AaSimCustomer_SysReserve2` |  |  |  |
| 38 | `AA.CUS.SYS.RESERVE1` | `AaSimCustomer_SysReserve1` |  |  |  |
| 39 | `AA.CUS.DEFAULT.ATTR.OPTION` | `AaSimCustomer_DefaultAttrOption` |  |  |  |
| 40 | `AA.CUS.DEFAULT.NEGOTIABLE` | `AaSimCustomer_DefaultNegotiable` |  |  |  |
| 41 | `AA.CUS.NR.ATTRIBUTE` | `AaSimCustomer_NrAttribute` |  |  |  |
| 42 | `AA.CUS.NR.OPTIONS` | `AaSimCustomer_NrOptions` |  |  |  |
| 43 | `AA.CUS.NR.ATTRIBUTE.RULE` | `AaSimCustomer_NrAttributeRule` |  |  |  |
| 44 | `AA.CUS.NR.VALUE.SOURCE` | `AaSimCustomer_NrValueSource` |  |  |  |
| 45 | `AA.CUS.NR.STD.COMP` | `AaSimCustomer_NrStdComp` |  |  |  |
| 46 | `AA.CUS.NR.TYPE` | `AaSimCustomer_NrType` |  |  |  |
| 47 | `AA.CUS.NR.VALUE` | `AaSimCustomer_NrValue` |  |  |  |
| 48 | `AA.CUS.NR.MESSAGE` | `AaSimCustomer_NrMessage` |  |  |  |
| 49 | `AA.CUS.CHANGED.FIELDS` | `AaSimCustomer_ChangedFields` |  |  |  |
| 50 | `AA.CUS.NEGOTIATED.FLDS` | `AaSimCustomer_NegotiatedFlds` |  |  |  |
| 51 | `AA.CUS.ID.COMP.1` | `AaSimCustomer_IdComp1` |  |  |  |
| 52 | `AA.CUS.ID.COMP.2` | `AaSimCustomer_IdComp2` |  |  |  |
| 53 | `AA.CUS.ID.COMP.3` | `AaSimCustomer_IdComp3` |  |  |  |
| 54 | `AA.CUS.ID.COMP.4` | `AaSimCustomer_IdComp4` |  |  |  |
| 55 | `AA.CUS.ID.COMP.5` | `AaSimCustomer_IdComp5` |  |  |  |
| 56 | `AA.CUS.ID.COMP.6` | `AaSimCustomer_IdComp6` |  |  |  |
| 57 | `AA.CUS.RESERVED2.ID` | `AaSimCustomer_Reserved2Id` |  |  |  |
| 58 | `AA.CUS.TARGET.PRODUCT` | `AaSimCustomer_TargetProduct` |  |  |  |
| 59 | `AA.CUS.STMT.NOS` | `AaSimCustomer_StmtNos` |  |  |  |
| 60 | `AA.CUS.OVERRIDE` | `AaSimCustomer_Override` |  |  |  |
| 61 | `AA.CUS.RECORD.STATUS` | `AaSimCustomer_RecordStatus` |  |  |  |
| 62 | `AA.CUS.CURR.NO` | `AaSimCustomer_CurrNo` |  |  |  |
| 63 | `AA.CUS.INPUTTER` | `AaSimCustomer_Inputter` |  |  |  |
| 64 | `AA.CUS.DATE.TIME` | `AaSimCustomer_DateTime` |  |  |  |
| 65 | `AA.CUS.AUTHORISER` | `AaSimCustomer_Authoriser` |  |  |  |
| 66 | `AA.CUS.CO.CODE` | `AaSimCustomer_CoCode` |  |  |  |
| 67 | `AA.CUS.DEPT.CODE` | `AaSimCustomer_DeptCode` |  |  |  |
| 68 | `AA.CUS.AUDITOR.CODE` | `AaSimCustomer_AuditorCode` |  |  |  |
| 69 | `AA.CUS.AUDIT.DATE.TIME` | `AaSimCustomer_AuditDateTime` |  |  |  |
