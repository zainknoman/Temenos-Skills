# AA.OFFICERS — Table Schema

> Source: `INSERTS/I_F.AA.OFFICERS` in `AA_Officers.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.OFF.ACTIVITY` | `AaSimOfficers_Activity` |  |  |  |
| 2 | `AA.OFF.ACTION` | `AaSimOfficers_Action` |  |  |  |
| 3 | `AA.OFF.PRIMARY.OFFICER` | `AaSimOfficers_PrimaryOfficer` |  |  |  |
| 4 | `AA.OFF.OTHER.OFFICER` | `AaSimOfficers_OtherOfficer` |  |  |  |
| 5 | `AA.OFF.OFFICER.ROLE` | `AaSimOfficers_OfficerRole` |  |  |  |
| 6 | `AA.OFF.NOTES` | `AaSimOfficers_Notes` |  |  |  |
| 7 | `AA.OFF.RESERVED10` | `AaSimOfficers_Reserved10` |  |  |  |
| 8 | `AA.OFF.RESERVED9` | `AaSimOfficers_Reserved9` |  |  |  |
| 9 | `AA.OFF.RESERVED8` | `AaSimOfficers_Reserved8` |  |  |  |
| 10 | `AA.OFF.RESERVED7` | `AaSimOfficers_Reserved7` |  |  |  |
| 11 | `AA.OFF.RESERVED6` | `AaSimOfficers_Reserved6` |  |  |  |
| 12 | `AA.OFF.RESERVED5` | `AaSimOfficers_Reserved5` |  |  |  |
| 13 | `AA.OFF.RESERVED4` | `AaSimOfficers_Reserved4` |  |  |  |
| 14 | `AA.OFF.RESERVED3` | `AaSimOfficers_Reserved3` |  |  |  |
| 15 | `AA.OFF.RESERVED2` | `AaSimOfficers_Reserved2` |  |  |  |
| 16 | `AA.OFF.RESERVED1` | `AaSimOfficers_Reserved1` |  |  |  |
| 17 | `AA.OFF.LOCAL.REF` | `AaSimOfficers_LocalRef` |  |  |  |
| 18 | `AA.OFF.PR.ATTRIBUTE` | `AaSimOfficers_PrAttribute` |  |  |  |
| 19 | `AA.OFF.PR.VALUE` | `AaSimOfficers_PrValue` |  |  |  |
| 20 | `AA.OFF.PR.BRK.RES` | `AaSimOfficers_PrBrkRes` |  |  |  |
| 21 | `AA.OFF.PR.BRK.MSG` | `AaSimOfficers_PrBrkMsg` |  |  |  |
| 22 | `AA.OFF.PR.BRK.CHARGE` | `AaSimOfficers_PrBrkCharge` |  |  |  |
| 23 | `AA.OFF.PR.RESERVED.3` | `AaSimOfficers_PrReserved3` |  |  |  |
| 24 | `AA.OFF.PR.RESERVED.2` | `AaSimOfficers_PrReserved2` |  |  |  |
| 25 | `AA.OFF.PR.RESERVED.1` | `AaSimOfficers_PrReserved1` |  |  |  |
| 26 | `AA.OFF.PR.APP.METHOD` | `AaSimOfficers_PrAppMethod` |  |  |  |
| 27 | `AA.OFF.PR.APP.PERIOD` | `AaSimOfficers_PrAppPeriod` |  |  |  |
| 28 | `AA.OFF.SYS.RESERVE7` | `AaSimOfficers_SysReserve7` |  |  |  |
| 29 | `AA.OFF.SYS.RESERVE6` | `AaSimOfficers_SysReserve6` |  |  |  |
| 30 | `AA.OFF.OWNING.COMPANY` | `AaSimOfficers_OwningCompany` |  |  |  |
| 31 | `AA.OFF.API.ATTRIBUTE` | `AaSimOfficers_ApiAttribute` |  |  |  |
| 32 | `AA.OFF.SYS.RESERVE3` | `AaSimOfficers_SysReserve3` |  |  |  |
| 33 | `AA.OFF.SYS.RESERVE2` | `AaSimOfficers_SysReserve2` |  |  |  |
| 34 | `AA.OFF.SYS.RESERVE1` | `AaSimOfficers_SysReserve1` |  |  |  |
| 35 | `AA.OFF.DEFAULT.ATTR.OPTION` | `AaSimOfficers_DefaultAttrOption` |  |  |  |
| 36 | `AA.OFF.DEFAULT.NEGOTIABLE` | `AaSimOfficers_DefaultNegotiable` |  |  |  |
| 37 | `AA.OFF.NR.ATTRIBUTE` | `AaSimOfficers_NrAttribute` |  |  |  |
| 38 | `AA.OFF.NR.OPTIONS` | `AaSimOfficers_NrOptions` |  |  |  |
| 39 | `AA.OFF.NR.ATTRIBUTE.RULE` | `AaSimOfficers_NrAttributeRule` |  |  |  |
| 40 | `AA.OFF.NR.VALUE.SOURCE` | `AaSimOfficers_NrValueSource` |  |  |  |
| 41 | `AA.OFF.NR.STD.COMP` | `AaSimOfficers_NrStdComp` |  |  |  |
| 42 | `AA.OFF.NR.TYPE` | `AaSimOfficers_NrType` |  |  |  |
| 43 | `AA.OFF.NR.VALUE` | `AaSimOfficers_NrValue` |  |  |  |
| 44 | `AA.OFF.NR.MESSAGE` | `AaSimOfficers_NrMessage` |  |  |  |
| 45 | `AA.OFF.CHANGED.FIELDS` | `AaSimOfficers_ChangedFields` |  |  |  |
| 46 | `AA.OFF.NEGOTIATED.FLDS` | `AaSimOfficers_NegotiatedFlds` |  |  |  |
| 47 | `AA.OFF.ID.COMP.1` | `AaSimOfficers_IdComp1` |  |  |  |
| 48 | `AA.OFF.ID.COMP.2` | `AaSimOfficers_IdComp2` |  |  |  |
| 49 | `AA.OFF.ID.COMP.3` | `AaSimOfficers_IdComp3` |  |  |  |
| 50 | `AA.OFF.ID.COMP.4` | `AaSimOfficers_IdComp4` |  |  |  |
| 51 | `AA.OFF.ID.COMP.5` | `AaSimOfficers_IdComp5` |  |  |  |
| 52 | `AA.OFF.ID.COMP.6` | `AaSimOfficers_IdComp6` |  |  |  |
| 53 | `AA.OFF.RESERVED2.ID` | `AaSimOfficers_Reserved2Id` |  |  |  |
| 54 | `AA.OFF.TARGET.PRODUCT` | `AaSimOfficers_TargetProduct` |  |  |  |
| 55 | `AA.OFF.STMT.NOS` | `AaSimOfficers_StmtNos` |  |  |  |
| 56 | `AA.OFF.OVERRIDE` | `AaSimOfficers_Override` |  |  |  |
| 57 | `AA.OFF.RECORD.STATUS` | `AaSimOfficers_RecordStatus` |  |  |  |
| 58 | `AA.OFF.CURR.NO` | `AaSimOfficers_CurrNo` |  |  |  |
| 59 | `AA.OFF.INPUTTER` | `AaSimOfficers_Inputter` |  |  |  |
| 60 | `AA.OFF.DATE.TIME` | `AaSimOfficers_DateTime` |  |  |  |
| 61 | `AA.OFF.AUTHORISER` | `AaSimOfficers_Authoriser` |  |  |  |
| 62 | `AA.OFF.CO.CODE` | `AaSimOfficers_CoCode` |  |  |  |
| 63 | `AA.OFF.DEPT.CODE` | `AaSimOfficers_DeptCode` |  |  |  |
| 64 | `AA.OFF.AUDITOR.CODE` | `AaSimOfficers_AuditorCode` |  |  |  |
| 65 | `AA.OFF.AUDIT.DATE.TIME` | `AaSimOfficers_AuditDateTime` |  |  |  |
