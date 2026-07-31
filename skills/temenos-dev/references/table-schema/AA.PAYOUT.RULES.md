# AA.PAYOUT.RULES — Table Schema

> Source: `INSERTS/I_F.AA.PAYOUT.RULES` in `AA_PayoutRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PAYOUT.ACTIVITY` | `AaSimPayoutRules_Activity` |  |  |  |
| 2 | `AA.PAYOUT.ACTION` | `AaSimPayoutRules_Action` |  |  |  |
| 3 | `AA.PAYOUT.APPLICATION.TYPE` | `AaSimPayoutRules_ApplicationType` |  |  |  |
| 4 | `AA.PAYOUT.APPLICATION.ORDER` | `AaSimPayoutRules_ApplicationOrder` |  |  |  |
| 5 | `AA.PAYOUT.SEQUENCE` | `AaSimPayoutRules_Sequence` |  |  |  |
| 6 | `AA.PAYOUT.PROPERTY` | `AaSimPayoutRules_Property` |  |  |  |
| 7 | `AA.PAYOUT.BALANCE.TYPE` | `AaSimPayoutRules_BalanceType` |  |  |  |
| 8 | `AA.PAYOUT.PROP.APPL.TYPE` | `AaSimPayoutRules_PropApplType` |  |  |  |
| 9 | `AA.PAYOUT.PRE.BILL.ACTIVITY` | `AaSimPayoutRules_PreBillActivity` |  |  |  |
| 10 | `AA.PAYOUT.REMAINDER.ACTIVITY` | `AaSimPayoutRules_RemainderActivity` |  |  |  |
| 11 | `AA.PAYOUT.RESERVED10` | `AaSimPayoutRules_Reserved10` |  |  |  |
| 12 | `AA.PAYOUT.RESERVED9` | `AaSimPayoutRules_Reserved9` |  |  |  |
| 13 | `AA.PAYOUT.RESERVED8` | `AaSimPayoutRules_Reserved8` |  |  |  |
| 14 | `AA.PAYOUT.RESERVED7` | `AaSimPayoutRules_Reserved7` |  |  |  |
| 15 | `AA.PAYOUT.RESERVED6` | `AaSimPayoutRules_Reserved6` |  |  |  |
| 16 | `AA.PAYOUT.RESERVED5` | `AaSimPayoutRules_Reserved5` |  |  |  |
| 17 | `AA.PAYOUT.RESERVED4` | `AaSimPayoutRules_Reserved4` |  |  |  |
| 18 | `AA.PAYOUT.RESERVED3` | `AaSimPayoutRules_Reserved3` |  |  |  |
| 19 | `AA.PAYOUT.RESERVED2` | `AaSimPayoutRules_Reserved2` |  |  |  |
| 20 | `AA.PAYOUT.RESERVED1` | `AaSimPayoutRules_Reserved1` |  |  |  |
| 21 | `AA.PAYOUT.LOCAL.REF` | `AaSimPayoutRules_LocalRef` |  |  |  |
| 22 | `AA.PAYOUT.PR.ATTRIBUTE` | `AaSimPayoutRules_PrAttribute` |  |  |  |
| 23 | `AA.PAYOUT.PR.VALUE` | `AaSimPayoutRules_PrValue` |  |  |  |
| 24 | `AA.PAYOUT.PR.BRK.RES` | `AaSimPayoutRules_PrBrkRes` |  |  |  |
| 25 | `AA.PAYOUT.PR.BRK.MSG` | `AaSimPayoutRules_PrBrkMsg` |  |  |  |
| 26 | `AA.PAYOUT.PR.BRK.CHARGE` | `AaSimPayoutRules_PrBrkCharge` |  |  |  |
| 27 | `AA.PAYOUT.PR.RESERVED.3` | `AaSimPayoutRules_PrReserved3` |  |  |  |
| 28 | `AA.PAYOUT.PR.RESERVED.2` | `AaSimPayoutRules_PrReserved2` |  |  |  |
| 29 | `AA.PAYOUT.PR.RESERVED.1` | `AaSimPayoutRules_PrReserved1` |  |  |  |
| 30 | `AA.PAYOUT.PR.APP.METHOD` | `AaSimPayoutRules_PrAppMethod` |  |  |  |
| 31 | `AA.PAYOUT.PR.APP.PERIOD` | `AaSimPayoutRules_PrAppPeriod` |  |  |  |
| 32 | `AA.PAYOUT.SYS.RESERVE7` | `AaSimPayoutRules_SysReserve7` |  |  |  |
| 33 | `AA.PAYOUT.SYS.RESERVE6` | `AaSimPayoutRules_SysReserve6` |  |  |  |
| 34 | `AA.PAYOUT.OWNING.COMPANY` | `AaSimPayoutRules_OwningCompany` |  |  |  |
| 35 | `AA.PAYOUT.API.ATTRIBUTE` | `AaSimPayoutRules_ApiAttribute` |  |  |  |
| 36 | `AA.PAYOUT.SYS.RESERVE3` | `AaSimPayoutRules_SysReserve3` |  |  |  |
| 37 | `AA.PAYOUT.SYS.RESERVE2` | `AaSimPayoutRules_SysReserve2` |  |  |  |
| 38 | `AA.PAYOUT.SYS.RESERVE1` | `AaSimPayoutRules_SysReserve1` |  |  |  |
| 39 | `AA.PAYOUT.DEFAULT.ATTR.OPTION` | `AaSimPayoutRules_DefaultAttrOption` |  |  |  |
| 40 | `AA.PAYOUT.DEFAULT.NEGOTIABLE` | `AaSimPayoutRules_DefaultNegotiable` |  |  |  |
| 41 | `AA.PAYOUT.NR.ATTRIBUTE` | `AaSimPayoutRules_NrAttribute` |  |  |  |
| 42 | `AA.PAYOUT.NR.OPTIONS` | `AaSimPayoutRules_NrOptions` |  |  |  |
| 43 | `AA.PAYOUT.NR.ATTRIBUTE.RULE` | `AaSimPayoutRules_NrAttributeRule` |  |  |  |
| 44 | `AA.PAYOUT.NR.VALUE.SOURCE` | `AaSimPayoutRules_NrValueSource` |  |  |  |
| 45 | `AA.PAYOUT.NR.STD.COMP` | `AaSimPayoutRules_NrStdComp` |  |  |  |
| 46 | `AA.PAYOUT.NR.TYPE` | `AaSimPayoutRules_NrType` |  |  |  |
| 47 | `AA.PAYOUT.NR.VALUE` | `AaSimPayoutRules_NrValue` |  |  |  |
| 48 | `AA.PAYOUT.NR.MESSAGE` | `AaSimPayoutRules_NrMessage` |  |  |  |
| 49 | `AA.PAYOUT.CHANGED.FIELDS` | `AaSimPayoutRules_ChangedFields` |  |  |  |
| 50 | `AA.PAYOUT.NEGOTIATED.FLDS` | `AaSimPayoutRules_NegotiatedFlds` |  |  |  |
| 51 | `AA.PAYOUT.ID.COMP.1` | `AaSimPayoutRules_IdComp1` |  |  |  |
| 52 | `AA.PAYOUT.ID.COMP.2` | `AaSimPayoutRules_IdComp2` |  |  |  |
| 53 | `AA.PAYOUT.ID.COMP.3` | `AaSimPayoutRules_IdComp3` |  |  |  |
| 54 | `AA.PAYOUT.ID.COMP.4` | `AaSimPayoutRules_IdComp4` |  |  |  |
| 55 | `AA.PAYOUT.ID.COMP.5` | `AaSimPayoutRules_IdComp5` |  |  |  |
| 56 | `AA.PAYOUT.ID.COMP.6` | `AaSimPayoutRules_IdComp6` |  |  |  |
| 57 | `AA.PAYOUT.RESERVED2.ID` | `AaSimPayoutRules_Reserved2Id` |  |  |  |
| 58 | `AA.PAYOUT.TARGET.PRODUCT` | `AaSimPayoutRules_TargetProduct` |  |  |  |
| 59 | `AA.PAYOUT.STMT.NOS` | `AaSimPayoutRules_StmtNos` |  |  |  |
| 60 | `AA.PAYOUT.OVERRIDE` | `AaSimPayoutRules_Override` |  |  |  |
| 61 | `AA.PAYOUT.RECORD.STATUS` | `AaSimPayoutRules_RecordStatus` |  |  |  |
| 62 | `AA.PAYOUT.CURR.NO` | `AaSimPayoutRules_CurrNo` |  |  |  |
| 63 | `AA.PAYOUT.INPUTTER` | `AaSimPayoutRules_Inputter` |  |  |  |
| 64 | `AA.PAYOUT.DATE.TIME` | `AaSimPayoutRules_DateTime` |  |  |  |
| 65 | `AA.PAYOUT.AUTHORISER` | `AaSimPayoutRules_Authoriser` |  |  |  |
| 66 | `AA.PAYOUT.CO.CODE` | `AaSimPayoutRules_CoCode` |  |  |  |
| 67 | `AA.PAYOUT.DEPT.CODE` | `AaSimPayoutRules_DeptCode` |  |  |  |
| 68 | `AA.PAYOUT.AUDITOR.CODE` | `AaSimPayoutRules_AuditorCode` |  |  |  |
| 69 | `AA.PAYOUT.AUDIT.DATE.TIME` | `AaSimPayoutRules_AuditDateTime` |  |  |  |
