# AA.AGENT.EVENT — Table Schema

> Source: `INSERTS/I_F.AA.AGENT.EVENT` in `AA_AgentCommission.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AGEV.ARRANGEMENT` | `AaAgentEvent_Arrangement` |  |  |  |
| 2 | `AA.AGEV.EVENT.ACTIVITY` | `AaAgentEvent_EventActivity` |  |  |  |
| 3 | `AA.AGEV.AGENT.ARR.ID` | `AaAgentEvent_AgentArrId` |  |  |  |
| 4 | `AA.AGEV.AGENT.ACT.ID` | `AaAgentEvent_AgentActId` |  |  |  |
| 5 | `AA.AGEV.FIXED.AMOUNT` | `AaAgentEvent_FixedAmount` |  |  |  |
| 6 | `AA.AGEV.MARGIN` | `AaAgentEvent_Margin` |  |  |  |
| 7 | `AA.AGEV.BASE.BALANCE` | `AaAgentEvent_BaseBalance` |  |  |  |
| 8 | `AA.AGEV.BASE.BALANCE.DATE` | `AaAgentEvent_BaseBalanceDate` |  |  |  |
| 9 | `AA.AGEV.EVENT.TYPE` | `AaAgentEvent_EventType` |  |  |  |
| 10 | `AA.AGEV.EVENT.FUNCTION` | `AaAgentEvent_EventFunction` |  |  |  |
| 11 | `AA.AGEV.EVENT.STATUS` | `AaAgentEvent_EventStatus` |  |  |  |
| 12 | `AA.AGEV.ERR.SOURCE` | `AaAgentEvent_ErrSource` |  |  |  |
| 13 | `AA.AGEV.ERR.MESSAGE` | `AaAgentEvent_ErrMessage` |  |  |  |
| 14 | `AA.AGEV.AMORT.END.DATE` | `AaAgentEvent_AmortEndDate` |  |  |  |
| 15 | `AA.AGEV.EFFECTIVE.DATE` | `AaAgentEvent_EffectiveDate` |  |  |  |
| 16 | `AA.AGEV.FINANCIAL.CUSTOMER` | `AaAgentEvent_FinancialCustomer` |  |  |  |
| 17 | `AA.AGEV.CALC.AMOUNT` | `AaAgentEvent_CalcAmount` |  |  |  |
| 18 | `AA.AGEV.RETRY.EVENT` | `AaAgentEvent_RetryEvent` |  |  |  |
| 19 | `AA.AGEV.CONTEXT.NAME` | `AaAgentEvent_ContextName` |  |  |  |
| 20 | `AA.AGEV.CONTEXT.VALUE` | `AaAgentEvent_ContextValue` |  |  |  |
| 21 | `AA.AGEV.COMMISSION.PROPERTY` | `AaAgentEvent_CommissionProperty` |  |  |  |
| 22 | `AA.AGEV.ACCRUAL.ID` | `AaAgentEvent_AccrualId` |  |  |  |
| 23 | `AA.AGEV.RESERVED.4` | `AaAgentEvent_Reserved4` |  |  |  |
| 24 | `AA.AGEV.RESERVED.3` | `AaAgentEvent_Reserved3` | TField |  |  |
| 25 | `AA.AGEV.RESERVED.2` | `AaAgentEvent_Reserved2` | TField |  |  |
| 26 | `AA.AGEV.RESERVED.1` | `AaAgentEvent_Reserved1` | TField |  |  |
| 27 | `AA.AGEV.RECORD.STATUS` | `AaAgentEvent_RecordStatus` | String |  |  |
| 28 | `AA.AGEV.CURR.NO` | `AaAgentEvent_CurrNo` | String |  |  |
| 29 | `AA.AGEV.INPUTTER` | `AaAgentEvent_Inputter` |  |  |  |
| 30 | `AA.AGEV.DATE.TIME` | `AaAgentEvent_DateTime` |  |  |  |
| 31 | `AA.AGEV.AUTHORISER` | `AaAgentEvent_Authoriser` | String |  |  |
| 32 | `AA.AGEV.CO.CODE` | `AaAgentEvent_CoCode` | String |  |  |
| 33 | `AA.AGEV.DEPT.CODE` | `AaAgentEvent_DeptCode` | String |  |  |
| 34 | `AA.AGEV.AUDITOR.CODE` | `AaAgentEvent_AuditorCode` | String |  |  |
| 35 | `AA.AGEV.AUDIT.DATE.TIME` | `AaAgentEvent_AuditDateTime` | String |  |  |
