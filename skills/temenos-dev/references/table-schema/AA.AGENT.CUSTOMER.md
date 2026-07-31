# AA.AGENT.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.AA.AGENT.CUSTOMER` in `AA_AgentCommission.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AGCU.ARRANGEMENT` | `AaAgentCustomer_Arrangement` |  |  |  |
| 2 | `AA.AGCU.ACCRUAL.ID` | `AaAgentCustomer_AccrualId` |  |  |  |
| 3 | `AA.AGCU.COMMISSION.PROPERTY` | `AaAgentCustomer_CommissionProperty` |  |  |  |
| 4 | `AA.AGCU.RESERVED.7` | `AaAgentCustomer_Reserved7` |  |  |  |
| 5 | `AA.AGCU.RESERVED.6` | `AaAgentCustomer_Reserved6` | TField |  |  |
| 6 | `AA.AGCU.RESERVED.5` | `AaAgentCustomer_Reserved5` | TField |  |  |
| 7 | `AA.AGCU.RESERVED.4` | `AaAgentCustomer_Reserved4` | TField |  |  |
| 8 | `AA.AGCU.RESERVED.3` | `AaAgentCustomer_Reserved3` | TField |  |  |
| 9 | `AA.AGCU.FIN.ARRANGEMENT` | `AaAgentCustomer_FinArrangement` |  |  |  |
| 10 | `AA.AGCU.AGENT.LINK.DATE` | `AaAgentCustomer_AgentLinkDate` |  |  |  |
