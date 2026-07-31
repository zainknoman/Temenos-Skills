# AA.CHARGEOFF — Table Schema

> Source: `INSERTS/I_F.AA.CHARGEOFF` in `AA_ChargeOff.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CF.ACTIVITY` | `AaSimChargeoff_Activity` |  |  |  |
| 2 | `AA.CF.ACTION` | `AaSimChargeoff_Action` |  |  |  |
| 3 | `AA.CF.FINANCIAL.STATUS` | `AaSimChargeoff_FinancialStatus` |  |  |  |
| 4 | `AA.CF.CHARGE.OFF.ORDER` | `AaSimChargeoff_ChargeOffOrder` |  |  |  |
| 5 | `AA.CF.WRITEOFF.ORDER` | `AaSimChargeoff_WriteoffOrder` |  |  |  |
| 6 | `AA.CF.APPLICATION.TYPE` | `AaSimChargeoff_ApplicationType` |  |  |  |
| 7 | `AA.CF.APPLICATION.ORDER` | `AaSimChargeoff_ApplicationOrder` |  |  |  |
| 8 | `AA.CF.RESERVED15` | `AaSimChargeoff_Reserved15` |  |  |  |
| 9 | `AA.CF.RESERVED14` | `AaSimChargeoff_Reserved14` |  |  |  |
| 10 | `AA.CF.RESERVED13` | `AaSimChargeoff_Reserved13` |  |  |  |
| 11 | `AA.CF.BALANCE.PROPERTY` | `AaSimChargeoff_BalanceProperty` |  |  |  |
| 12 | `AA.CF.RESERVED12` | `AaSimChargeoff_Reserved12` |  |  |  |
| 13 | `AA.CF.RESERVED11` | `AaSimChargeoff_Reserved11` |  |  |  |
| 14 | `AA.CF.RESERVED10` | `AaSimChargeoff_Reserved10` |  |  |  |
| 15 | `AA.CF.BALANCE.TYPE` | `AaSimChargeoff_BalanceType` |  |  |  |
| 16 | `AA.CF.RESERVED9` | `AaSimChargeoff_Reserved9` |  |  |  |
| 17 | `AA.CF.RESERVED8` | `AaSimChargeoff_Reserved8` |  |  |  |
| 18 | `AA.CF.RESERVED7` | `AaSimChargeoff_Reserved7` |  |  |  |
| 19 | `AA.CF.RESERVED6` | `AaSimChargeoff_Reserved6` |  |  |  |
| 20 | `AA.CF.RESERVED5` | `AaSimChargeoff_Reserved5` |  |  |  |
| 21 | `AA.CF.RESERVED4` | `AaSimChargeoff_Reserved4` |  |  |  |
| 22 | `AA.CF.RESERVED3` | `AaSimChargeoff_Reserved3` |  |  |  |
| 23 | `AA.CF.RESERVED2` | `AaSimChargeoff_Reserved2` |  |  |  |
| 24 | `AA.CF.RESERVED1` | `AaSimChargeoff_Reserved1` |  |  |  |
| 25 | `AA.CF.LOCAL.REF` | `AaSimChargeoff_LocalRef` |  |  |  |
| 26 | `AA.CF.PR.ATTRIBUTE` | `AaSimChargeoff_PrAttribute` |  |  |  |
| 27 | `AA.CF.PR.VALUE` | `AaSimChargeoff_PrValue` |  |  |  |
| 28 | `AA.CF.PR.BRK.RES` | `AaSimChargeoff_PrBrkRes` |  |  |  |
| 29 | `AA.CF.PR.BRK.MSG` | `AaSimChargeoff_PrBrkMsg` |  |  |  |
| 30 | `AA.CF.PR.BRK.CHARGE` | `AaSimChargeoff_PrBrkCharge` |  |  |  |
| 31 | `AA.CF.PR.RESERVED.3` | `AaSimChargeoff_PrReserved3` |  |  |  |
| 32 | `AA.CF.PR.RESERVED.2` | `AaSimChargeoff_PrReserved2` |  |  |  |
| 33 | `AA.CF.PR.RESERVED.1` | `AaSimChargeoff_PrReserved1` |  |  |  |
| 34 | `AA.CF.PR.APP.METHOD` | `AaSimChargeoff_PrAppMethod` |  |  |  |
| 35 | `AA.CF.PR.APP.PERIOD` | `AaSimChargeoff_PrAppPeriod` |  |  |  |
| 36 | `AA.CF.SYS.RESERVE7` | `AaSimChargeoff_SysReserve7` |  |  |  |
| 37 | `AA.CF.SYS.RESERVE6` | `AaSimChargeoff_SysReserve6` |  |  |  |
| 38 | `AA.CF.OWNING.COMPANY` | `AaSimChargeoff_OwningCompany` |  |  |  |
| 39 | `AA.CF.API.ATTRIBUTE` | `AaSimChargeoff_ApiAttribute` |  |  |  |
| 40 | `AA.CF.SYS.RESERVE3` | `AaSimChargeoff_SysReserve3` |  |  |  |
| 41 | `AA.CF.SYS.RESERVE2` | `AaSimChargeoff_SysReserve2` |  |  |  |
| 42 | `AA.CF.SYS.RESERVE1` | `AaSimChargeoff_SysReserve1` |  |  |  |
| 43 | `AA.CF.DEFAULT.ATTR.OPTION` | `AaSimChargeoff_DefaultAttrOption` |  |  |  |
| 44 | `AA.CF.DEFAULT.NEGOTIABLE` | `AaSimChargeoff_DefaultNegotiable` |  |  |  |
| 45 | `AA.CF.NR.ATTRIBUTE` | `AaSimChargeoff_NrAttribute` |  |  |  |
| 46 | `AA.CF.NR.OPTIONS` | `AaSimChargeoff_NrOptions` |  |  |  |
| 47 | `AA.CF.NR.ATTRIBUTE.RULE` | `AaSimChargeoff_NrAttributeRule` |  |  |  |
| 48 | `AA.CF.NR.VALUE.SOURCE` | `AaSimChargeoff_NrValueSource` |  |  |  |
| 49 | `AA.CF.NR.STD.COMP` | `AaSimChargeoff_NrStdComp` |  |  |  |
| 50 | `AA.CF.NR.TYPE` | `AaSimChargeoff_NrType` |  |  |  |
| 51 | `AA.CF.NR.VALUE` | `AaSimChargeoff_NrValue` |  |  |  |
| 52 | `AA.CF.NR.MESSAGE` | `AaSimChargeoff_NrMessage` |  |  |  |
| 53 | `AA.CF.CHANGED.FIELDS` | `AaSimChargeoff_ChangedFields` |  |  |  |
| 54 | `AA.CF.NEGOTIATED.FLDS` | `AaSimChargeoff_NegotiatedFlds` |  |  |  |
| 55 | `AA.CF.ID.COMP.1` | `AaSimChargeoff_IdComp1` |  |  |  |
| 56 | `AA.CF.ID.COMP.2` | `AaSimChargeoff_IdComp2` |  |  |  |
| 57 | `AA.CF.ID.COMP.3` | `AaSimChargeoff_IdComp3` |  |  |  |
| 58 | `AA.CF.ID.COMP.4` | `AaSimChargeoff_IdComp4` |  |  |  |
| 59 | `AA.CF.ID.COMP.5` | `AaSimChargeoff_IdComp5` |  |  |  |
| 60 | `AA.CF.ID.COMP.6` | `AaSimChargeoff_IdComp6` |  |  |  |
| 61 | `AA.CF.RESERVED2.ID` | `AaSimChargeoff_Reserved2Id` |  |  |  |
| 62 | `AA.CF.TARGET.PRODUCT` | `AaSimChargeoff_TargetProduct` |  |  |  |
| 63 | `AA.CF.STMT.NOS` | `AaSimChargeoff_StmtNos` |  |  |  |
| 64 | `AA.CF.OVERRIDE` | `AaSimChargeoff_Override` |  |  |  |
| 65 | `AA.CF.RECORD.STATUS` | `AaSimChargeoff_RecordStatus` |  |  |  |
| 66 | `AA.CF.CURR.NO` | `AaSimChargeoff_CurrNo` |  |  |  |
| 67 | `AA.CF.INPUTTER` | `AaSimChargeoff_Inputter` |  |  |  |
| 68 | `AA.CF.DATE.TIME` | `AaSimChargeoff_DateTime` |  |  |  |
| 69 | `AA.CF.AUTHORISER` | `AaSimChargeoff_Authoriser` |  |  |  |
| 70 | `AA.CF.CO.CODE` | `AaSimChargeoff_CoCode` |  |  |  |
| 71 | `AA.CF.DEPT.CODE` | `AaSimChargeoff_DeptCode` |  |  |  |
| 72 | `AA.CF.AUDITOR.CODE` | `AaSimChargeoff_AuditorCode` |  |  |  |
| 73 | `AA.CF.AUDIT.DATE.TIME` | `AaSimChargeoff_AuditDateTime` |  |  |  |
