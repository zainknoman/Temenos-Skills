# AA.AGENT.COMMISSION — Table Schema

> Source: `INSERTS/I_F.AA.AGENT.COMMISSION` in `AA_AgentCommission.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AGCOMM.ACTIVITY` | `AaSimAgentCommission_Activity` |  |  |  |
| 2 | `AA.AGCOMM.ACTION` | `AaSimAgentCommission_Action` |  |  |  |
| 3 | `AA.AGCOMM.AGENT.ID` | `AaSimAgentCommission_AgentId` |  |  |  |
| 4 | `AA.AGCOMM.AGENT.ARR.ID` | `AaSimAgentCommission_AgentArrId` |  |  |  |
| 5 | `AA.AGCOMM.AGENT.ROLE` | `AaSimAgentCommission_AgentRole` |  |  |  |
| 6 | `AA.AGCOMM.ONLINE.EVENT` | `AaSimAgentCommission_OnlineEvent` |  |  |  |
| 7 | `AA.AGCOMM.SCHEDULED.EVENT` | `AaSimAgentCommission_ScheduledEvent` |  |  |  |
| 8 | `AA.AGCOMM.FIXED.AMOUNT` | `AaSimAgentCommission_FixedAmount` |  |  |  |
| 9 | `AA.AGCOMM.MARGIN.OPERAND` | `AaSimAgentCommission_MarginOperand` |  |  |  |
| 10 | `AA.AGCOMM.MARGIN.RATE` | `AaSimAgentCommission_MarginRate` |  |  |  |
| 11 | `AA.AGCOMM.MARGIN.PERCENT` | `AaSimAgentCommission_MarginPercent` |  |  |  |
| 12 | `AA.AGCOMM.SCHEDULE.CHARGE` | `AaSimAgentCommission_ScheduleCharge` |  |  |  |
| 13 | `AA.AGCOMM.LINKED.PROPERTY` | `AaSimAgentCommission_LinkedProperty` |  |  |  |
| 14 | `AA.AGCOMM.SCHEDULE.FREQUENCY` | `AaSimAgentCommission_ScheduleFrequency` |  |  |  |
| 15 | `AA.AGCOMM.DRAWBACK.TYPE` | `AaSimAgentCommission_DrawbackType` |  |  |  |
| 16 | `AA.AGCOMM.DEFER.DAYS` | `AaSimAgentCommission_DeferDays` |  |  |  |
| 17 | `AA.AGCOMM.BASE.DATE.TYPE` | `AaSimAgentCommission_BaseDateType` |  |  |  |
| 18 | `AA.AGCOMM.RESERVED5` | `AaSimAgentCommission_Reserved5` |  |  |  |
| 19 | `AA.AGCOMM.RESERVED4` | `AaSimAgentCommission_Reserved4` |  |  |  |
| 20 | `AA.AGCOMM.COMMISSION.TYPE` | `AaSimAgentCommission_CommissionType` |  |  |  |
| 21 | `AA.AGCOMM.LINK.TYPE` | `AaSimAgentCommission_LinkType` |  |  |  |
| 22 | `AA.AGCOMM.RESERVED3` | `AaSimAgentCommission_Reserved3` |  |  |  |
| 23 | `AA.AGCOMM.RESERVED2` | `AaSimAgentCommission_Reserved2` |  |  |  |
| 24 | `AA.AGCOMM.RESERVED1` | `AaSimAgentCommission_Reserved1` |  |  |  |
| 25 | `AA.AGCOMM.LOCAL.REF` | `AaSimAgentCommission_LocalRef` |  |  |  |
| 26 | `AA.AGCOMM.PR.ATTRIBUTE` | `AaSimAgentCommission_PrAttribute` |  |  |  |
| 27 | `AA.AGCOMM.PR.VALUE` | `AaSimAgentCommission_PrValue` |  |  |  |
| 28 | `AA.AGCOMM.PR.BRK.RES` | `AaSimAgentCommission_PrBrkRes` |  |  |  |
| 29 | `AA.AGCOMM.PR.BRK.MSG` | `AaSimAgentCommission_PrBrkMsg` |  |  |  |
| 30 | `AA.AGCOMM.PR.BRK.CHARGE` | `AaSimAgentCommission_PrBrkCharge` |  |  |  |
| 31 | `AA.AGCOMM.PR.RESERVED.3` | `AaSimAgentCommission_PrReserved3` |  |  |  |
| 32 | `AA.AGCOMM.PR.RESERVED.2` | `AaSimAgentCommission_PrReserved2` |  |  |  |
| 33 | `AA.AGCOMM.PR.RESERVED.1` | `AaSimAgentCommission_PrReserved1` |  |  |  |
| 34 | `AA.AGCOMM.PR.APP.METHOD` | `AaSimAgentCommission_PrAppMethod` |  |  |  |
| 35 | `AA.AGCOMM.PR.APP.PERIOD` | `AaSimAgentCommission_PrAppPeriod` |  |  |  |
| 36 | `AA.AGCOMM.SYS.RESERVE7` | `AaSimAgentCommission_SysReserve7` |  |  |  |
| 37 | `AA.AGCOMM.SYS.RESERVE6` | `AaSimAgentCommission_SysReserve6` |  |  |  |
| 38 | `AA.AGCOMM.OWNING.COMPANY` | `AaSimAgentCommission_OwningCompany` |  |  |  |
| 39 | `AA.AGCOMM.API.ATTRIBUTE` | `AaSimAgentCommission_ApiAttribute` |  |  |  |
| 40 | `AA.AGCOMM.SYS.RESERVE3` | `AaSimAgentCommission_SysReserve3` |  |  |  |
| 41 | `AA.AGCOMM.SYS.RESERVE2` | `AaSimAgentCommission_SysReserve2` |  |  |  |
| 42 | `AA.AGCOMM.SYS.RESERVE1` | `AaSimAgentCommission_SysReserve1` |  |  |  |
| 43 | `AA.AGCOMM.DEFAULT.ATTR.OPTION` | `AaSimAgentCommission_DefaultAttrOption` |  |  |  |
| 44 | `AA.AGCOMM.DEFAULT.NEGOTIABLE` | `AaSimAgentCommission_DefaultNegotiable` |  |  |  |
| 45 | `AA.AGCOMM.NR.ATTRIBUTE` | `AaSimAgentCommission_NrAttribute` |  |  |  |
| 46 | `AA.AGCOMM.NR.OPTIONS` | `AaSimAgentCommission_NrOptions` |  |  |  |
| 47 | `AA.AGCOMM.NR.ATTRIBUTE.RULE` | `AaSimAgentCommission_NrAttributeRule` |  |  |  |
| 48 | `AA.AGCOMM.NR.VALUE.SOURCE` | `AaSimAgentCommission_NrValueSource` |  |  |  |
| 49 | `AA.AGCOMM.NR.STD.COMP` | `AaSimAgentCommission_NrStdComp` |  |  |  |
| 50 | `AA.AGCOMM.NR.TYPE` | `AaSimAgentCommission_NrType` |  |  |  |
| 51 | `AA.AGCOMM.NR.VALUE` | `AaSimAgentCommission_NrValue` |  |  |  |
| 52 | `AA.AGCOMM.NR.MESSAGE` | `AaSimAgentCommission_NrMessage` |  |  |  |
| 53 | `AA.AGCOMM.CHANGED.FIELDS` | `AaSimAgentCommission_ChangedFields` |  |  |  |
| 54 | `AA.AGCOMM.NEGOTIATED.FLDS` | `AaSimAgentCommission_NegotiatedFlds` |  |  |  |
| 55 | `AA.AGCOMM.ID.COMP.1` | `AaSimAgentCommission_IdComp1` |  |  |  |
| 56 | `AA.AGCOMM.ID.COMP.2` | `AaSimAgentCommission_IdComp2` |  |  |  |
| 57 | `AA.AGCOMM.ID.COMP.3` | `AaSimAgentCommission_IdComp3` |  |  |  |
| 58 | `AA.AGCOMM.ID.COMP.4` | `AaSimAgentCommission_IdComp4` |  |  |  |
| 59 | `AA.AGCOMM.ID.COMP.5` | `AaSimAgentCommission_IdComp5` |  |  |  |
| 60 | `AA.AGCOMM.ID.COMP.6` | `AaSimAgentCommission_IdComp6` |  |  |  |
| 61 | `AA.AGCOMM.RESERVED2.ID` | `AaSimAgentCommission_Reserved2Id` |  |  |  |
| 62 | `AA.AGCOMM.TARGET.PRODUCT` | `AaSimAgentCommission_TargetProduct` |  |  |  |
| 63 | `AA.AGCOMM.STMT.NOS` | `AaSimAgentCommission_StmtNos` |  |  |  |
| 64 | `AA.AGCOMM.OVERRIDE` | `AaSimAgentCommission_Override` |  |  |  |
| 65 | `AA.AGCOMM.RECORD.STATUS` | `AaSimAgentCommission_RecordStatus` |  |  |  |
| 66 | `AA.AGCOMM.CURR.NO` | `AaSimAgentCommission_CurrNo` |  |  |  |
| 67 | `AA.AGCOMM.INPUTTER` | `AaSimAgentCommission_Inputter` |  |  |  |
| 68 | `AA.AGCOMM.DATE.TIME` | `AaSimAgentCommission_DateTime` |  |  |  |
| 69 | `AA.AGCOMM.AUTHORISER` | `AaSimAgentCommission_Authoriser` |  |  |  |
| 70 | `AA.AGCOMM.CO.CODE` | `AaSimAgentCommission_CoCode` |  |  |  |
| 71 | `AA.AGCOMM.DEPT.CODE` | `AaSimAgentCommission_DeptCode` |  |  |  |
| 72 | `AA.AGCOMM.AUDITOR.CODE` | `AaSimAgentCommission_AuditorCode` |  |  |  |
| 73 | `AA.AGCOMM.AUDIT.DATE.TIME` | `AaSimAgentCommission_AuditDateTime` |  |  |  |
