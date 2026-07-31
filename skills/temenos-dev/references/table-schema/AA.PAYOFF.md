# AA.PAYOFF — Table Schema

> Source: `INSERTS/I_F.AA.PAYOFF` in `AA_Payoff.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.POFF.ACTIVITY` | `AaSimPayoff_Activity` |  |  |  |
| 2 | `AA.POFF.ACTION` | `AaSimPayoff_Action` |  |  |  |
| 3 | `AA.POFF.EXPIRY.DAYS` | `AaSimPayoff_ExpiryDays` |  |  |  |
| 4 | `AA.POFF.SETTLE.ACT` | `AaSimPayoff_SettleAct` |  |  |  |
| 5 | `AA.POFF.SETTLE.DUES` | `AaSimPayoff_SettleDues` |  |  |  |
| 6 | `AA.POFF.SETTLE.DUE.ACT` | `AaSimPayoff_SettleDueAct` |  |  |  |
| 7 | `AA.POFF.TOLERANCE.PERCENT` | `AaSimPayoff_TolerancePercent` |  |  |  |
| 8 | `AA.POFF.TOLERANCE.CCY` | `AaSimPayoff_ToleranceCcy` |  |  |  |
| 9 | `AA.POFF.TOLERANCE.AMOUNT` | `AaSimPayoff_ToleranceAmount` |  |  |  |
| 10 | `AA.POFF.TOLERANCE.ACTION` | `AaSimPayoff_ToleranceAction` |  |  |  |
| 11 | `AA.POFF.SEND.EVENT` | `AaSimPayoff_SendEvent` |  |  |  |
| 12 | `AA.POFF.LOCAL.REF` | `AaSimPayoff_LocalRef` |  |  |  |
| 13 | `AA.POFF.PR.ATTRIBUTE` | `AaSimPayoff_PrAttribute` |  |  |  |
| 14 | `AA.POFF.PR.VALUE` | `AaSimPayoff_PrValue` |  |  |  |
| 15 | `AA.POFF.PR.BRK.RES` | `AaSimPayoff_PrBrkRes` |  |  |  |
| 16 | `AA.POFF.PR.BRK.MSG` | `AaSimPayoff_PrBrkMsg` |  |  |  |
| 17 | `AA.POFF.PR.BRK.CHARGE` | `AaSimPayoff_PrBrkCharge` |  |  |  |
| 18 | `AA.POFF.PR.RESERVED.3` | `AaSimPayoff_PrReserved3` |  |  |  |
| 19 | `AA.POFF.PR.RESERVED.2` | `AaSimPayoff_PrReserved2` |  |  |  |
| 20 | `AA.POFF.PR.RESERVED.1` | `AaSimPayoff_PrReserved1` |  |  |  |
| 21 | `AA.POFF.PR.APP.METHOD` | `AaSimPayoff_PrAppMethod` |  |  |  |
| 22 | `AA.POFF.PR.APP.PERIOD` | `AaSimPayoff_PrAppPeriod` |  |  |  |
| 23 | `AA.POFF.SYS.RESERVE7` | `AaSimPayoff_SysReserve7` |  |  |  |
| 24 | `AA.POFF.SYS.RESERVE6` | `AaSimPayoff_SysReserve6` |  |  |  |
| 25 | `AA.POFF.OWNING.COMPANY` | `AaSimPayoff_OwningCompany` |  |  |  |
| 26 | `AA.POFF.API.ATTRIBUTE` | `AaSimPayoff_ApiAttribute` |  |  |  |
| 27 | `AA.POFF.SYS.RESERVE3` | `AaSimPayoff_SysReserve3` |  |  |  |
| 28 | `AA.POFF.SYS.RESERVE2` | `AaSimPayoff_SysReserve2` |  |  |  |
| 29 | `AA.POFF.SYS.RESERVE1` | `AaSimPayoff_SysReserve1` |  |  |  |
| 30 | `AA.POFF.DEFAULT.ATTR.OPTION` | `AaSimPayoff_DefaultAttrOption` |  |  |  |
| 31 | `AA.POFF.DEFAULT.NEGOTIABLE` | `AaSimPayoff_DefaultNegotiable` |  |  |  |
| 32 | `AA.POFF.NR.ATTRIBUTE` | `AaSimPayoff_NrAttribute` |  |  |  |
| 33 | `AA.POFF.NR.OPTIONS` | `AaSimPayoff_NrOptions` |  |  |  |
| 34 | `AA.POFF.NR.ATTRIBUTE.RULE` | `AaSimPayoff_NrAttributeRule` |  |  |  |
| 35 | `AA.POFF.NR.VALUE.SOURCE` | `AaSimPayoff_NrValueSource` |  |  |  |
| 36 | `AA.POFF.NR.STD.COMP` | `AaSimPayoff_NrStdComp` |  |  |  |
| 37 | `AA.POFF.NR.TYPE` | `AaSimPayoff_NrType` |  |  |  |
| 38 | `AA.POFF.NR.VALUE` | `AaSimPayoff_NrValue` |  |  |  |
| 39 | `AA.POFF.NR.MESSAGE` | `AaSimPayoff_NrMessage` |  |  |  |
| 40 | `AA.POFF.CHANGED.FIELDS` | `AaSimPayoff_ChangedFields` |  |  |  |
| 41 | `AA.POFF.NEGOTIATED.FLDS` | `AaSimPayoff_NegotiatedFlds` |  |  |  |
| 42 | `AA.POFF.ID.COMP.1` | `AaSimPayoff_IdComp1` |  |  |  |
| 43 | `AA.POFF.ID.COMP.2` | `AaSimPayoff_IdComp2` |  |  |  |
| 44 | `AA.POFF.ID.COMP.3` | `AaSimPayoff_IdComp3` |  |  |  |
| 45 | `AA.POFF.ID.COMP.4` | `AaSimPayoff_IdComp4` |  |  |  |
| 46 | `AA.POFF.ID.COMP.5` | `AaSimPayoff_IdComp5` |  |  |  |
| 47 | `AA.POFF.ID.COMP.6` | `AaSimPayoff_IdComp6` |  |  |  |
| 48 | `AA.POFF.RESERVED2.ID` | `AaSimPayoff_Reserved2Id` |  |  |  |
| 49 | `AA.POFF.TARGET.PRODUCT` | `AaSimPayoff_TargetProduct` |  |  |  |
| 50 | `AA.POFF.STMT.NOS` | `AaSimPayoff_StmtNos` |  |  |  |
| 51 | `AA.POFF.OVERRIDE` | `AaSimPayoff_Override` |  |  |  |
| 52 | `AA.POFF.RECORD.STATUS` | `AaSimPayoff_RecordStatus` |  |  |  |
| 53 | `AA.POFF.CURR.NO` | `AaSimPayoff_CurrNo` |  |  |  |
| 54 | `AA.POFF.INPUTTER` | `AaSimPayoff_Inputter` |  |  |  |
| 55 | `AA.POFF.DATE.TIME` | `AaSimPayoff_DateTime` |  |  |  |
| 56 | `AA.POFF.AUTHORISER` | `AaSimPayoff_Authoriser` |  |  |  |
| 57 | `AA.POFF.CO.CODE` | `AaSimPayoff_CoCode` |  |  |  |
| 58 | `AA.POFF.DEPT.CODE` | `AaSimPayoff_DeptCode` |  |  |  |
| 59 | `AA.POFF.AUDITOR.CODE` | `AaSimPayoff_AuditorCode` |  |  |  |
| 60 | `AA.POFF.AUDIT.DATE.TIME` | `AaSimPayoff_AuditDateTime` |  |  |  |
