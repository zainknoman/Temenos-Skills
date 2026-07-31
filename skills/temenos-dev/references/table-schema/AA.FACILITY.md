# AA.FACILITY — Table Schema

> Source: `INSERTS/I_F.AA.FACILITY` in `AA_Facility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.FAC.ACTIVITY` | `AaSimFacility_Activity` |  |  |  |
| 2 | `AA.FAC.ACTION` | `AaSimFacility_Action` |  |  |  |
| 3 | `AA.FAC.SERVICE` | `AaSimFacility_Service` |  |  |  |
| 4 | `AA.FAC.SERVICE.AVAILABILITY` | `AaSimFacility_ServiceAvailability` |  |  |  |
| 5 | `AA.FAC.CUSTOMER.OPTION` | `AaSimFacility_CustomerOption` |  |  |  |
| 6 | `AA.FAC.RESERVED.10` | `AaSimFacility_Reserved10` |  |  |  |
| 7 | `AA.FAC.RESERVED.9` | `AaSimFacility_Reserved9` |  |  |  |
| 8 | `AA.FAC.RESERVED.8` | `AaSimFacility_Reserved8` |  |  |  |
| 9 | `AA.FAC.RESERVED.7` | `AaSimFacility_Reserved7` |  |  |  |
| 10 | `AA.FAC.RESERVED.6` | `AaSimFacility_Reserved6` |  |  |  |
| 11 | `AA.FAC.RESERVED.5` | `AaSimFacility_Reserved5` |  |  |  |
| 12 | `AA.FAC.RESERVED.4` | `AaSimFacility_Reserved4` |  |  |  |
| 13 | `AA.FAC.RESERVED.3` | `AaSimFacility_Reserved3` |  |  |  |
| 14 | `AA.FAC.RESERVED.2` | `AaSimFacility_Reserved2` |  |  |  |
| 15 | `AA.FAC.RESERVED.1` | `AaSimFacility_Reserved1` |  |  |  |
| 16 | `AA.FAC.LOCAL.REF` | `AaSimFacility_LocalRef` |  |  |  |
| 17 | `AA.FAC.PR.ATTRIBUTE` | `AaSimFacility_PrAttribute` |  |  |  |
| 18 | `AA.FAC.PR.VALUE` | `AaSimFacility_PrValue` |  |  |  |
| 19 | `AA.FAC.PR.BRK.RES` | `AaSimFacility_PrBrkRes` |  |  |  |
| 20 | `AA.FAC.PR.BRK.MSG` | `AaSimFacility_PrBrkMsg` |  |  |  |
| 21 | `AA.FAC.PR.BRK.CHARGE` | `AaSimFacility_PrBrkCharge` |  |  |  |
| 22 | `AA.FAC.PR.RESERVED.3` | `AaSimFacility_PrReserved3` |  |  |  |
| 23 | `AA.FAC.PR.RESERVED.2` | `AaSimFacility_PrReserved2` |  |  |  |
| 24 | `AA.FAC.PR.RESERVED.1` | `AaSimFacility_PrReserved1` |  |  |  |
| 25 | `AA.FAC.PR.APP.METHOD` | `AaSimFacility_PrAppMethod` |  |  |  |
| 26 | `AA.FAC.PR.APP.PERIOD` | `AaSimFacility_PrAppPeriod` |  |  |  |
| 27 | `AA.FAC.SYS.RESERVE7` | `AaSimFacility_SysReserve7` |  |  |  |
| 28 | `AA.FAC.SYS.RESERVE6` | `AaSimFacility_SysReserve6` |  |  |  |
| 29 | `AA.FAC.OWNING.COMPANY` | `AaSimFacility_OwningCompany` |  |  |  |
| 30 | `AA.FAC.API.ATTRIBUTE` | `AaSimFacility_ApiAttribute` |  |  |  |
| 31 | `AA.FAC.SYS.RESERVE3` | `AaSimFacility_SysReserve3` |  |  |  |
| 32 | `AA.FAC.SYS.RESERVE2` | `AaSimFacility_SysReserve2` |  |  |  |
| 33 | `AA.FAC.SYS.RESERVE1` | `AaSimFacility_SysReserve1` |  |  |  |
| 34 | `AA.FAC.DEFAULT.ATTR.OPTION` | `AaSimFacility_DefaultAttrOption` |  |  |  |
| 35 | `AA.FAC.DEFAULT.NEGOTIABLE` | `AaSimFacility_DefaultNegotiable` |  |  |  |
| 36 | `AA.FAC.NR.ATTRIBUTE` | `AaSimFacility_NrAttribute` |  |  |  |
| 37 | `AA.FAC.NR.OPTIONS` | `AaSimFacility_NrOptions` |  |  |  |
| 38 | `AA.FAC.NR.ATTRIBUTE.RULE` | `AaSimFacility_NrAttributeRule` |  |  |  |
| 39 | `AA.FAC.NR.VALUE.SOURCE` | `AaSimFacility_NrValueSource` |  |  |  |
| 40 | `AA.FAC.NR.STD.COMP` | `AaSimFacility_NrStdComp` |  |  |  |
| 41 | `AA.FAC.NR.TYPE` | `AaSimFacility_NrType` |  |  |  |
| 42 | `AA.FAC.NR.VALUE` | `AaSimFacility_NrValue` |  |  |  |
| 43 | `AA.FAC.NR.MESSAGE` | `AaSimFacility_NrMessage` |  |  |  |
| 44 | `AA.FAC.CHANGED.FIELDS` | `AaSimFacility_ChangedFields` |  |  |  |
| 45 | `AA.FAC.NEGOTIATED.FLDS` | `AaSimFacility_NegotiatedFlds` |  |  |  |
| 46 | `AA.FAC.ID.COMP.1` | `AaSimFacility_IdComp1` |  |  |  |
| 47 | `AA.FAC.ID.COMP.2` | `AaSimFacility_IdComp2` |  |  |  |
| 48 | `AA.FAC.ID.COMP.3` | `AaSimFacility_IdComp3` |  |  |  |
| 49 | `AA.FAC.ID.COMP.4` | `AaSimFacility_IdComp4` |  |  |  |
| 50 | `AA.FAC.ID.COMP.5` | `AaSimFacility_IdComp5` |  |  |  |
| 51 | `AA.FAC.ID.COMP.6` | `AaSimFacility_IdComp6` |  |  |  |
| 52 | `AA.FAC.RESERVED2.ID` | `AaSimFacility_Reserved2Id` |  |  |  |
| 53 | `AA.FAC.TARGET.PRODUCT` | `AaSimFacility_TargetProduct` |  |  |  |
| 54 | `AA.FAC.STMT.NOS` | `AaSimFacility_StmtNos` |  |  |  |
| 55 | `AA.FAC.OVERRIDE` | `AaSimFacility_Override` |  |  |  |
| 56 | `AA.FAC.RECORD.STATUS` | `AaSimFacility_RecordStatus` |  |  |  |
| 57 | `AA.FAC.CURR.NO` | `AaSimFacility_CurrNo` |  |  |  |
| 58 | `AA.FAC.INPUTTER` | `AaSimFacility_Inputter` |  |  |  |
| 59 | `AA.FAC.DATE.TIME` | `AaSimFacility_DateTime` |  |  |  |
| 60 | `AA.FAC.AUTHORISER` | `AaSimFacility_Authoriser` |  |  |  |
| 61 | `AA.FAC.CO.CODE` | `AaSimFacility_CoCode` |  |  |  |
| 62 | `AA.FAC.DEPT.CODE` | `AaSimFacility_DeptCode` |  |  |  |
| 63 | `AA.FAC.AUDITOR.CODE` | `AaSimFacility_AuditorCode` |  |  |  |
| 64 | `AA.FAC.AUDIT.DATE.TIME` | `AaSimFacility_AuditDateTime` |  |  |  |
