# AA.AGENT.COMMISSION.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.AGENT.COMMISSION.DETAILS` in `AA_AgentCommission.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AGCOM.DET.ARRANGEMENT` | `AaAgentCommissionDetails_Arrangement` |  |  |  |
| 2 | `AA.AGCOM.DET.AMOUNT` | `AaAgentCommissionDetails_Amount` |  |  |  |
| 3 | `AA.AGCOM.DET.MARGIN.AMOUNT` | `AaAgentCommissionDetails_MarginAmount` | TField |  |  |
| 4 | `AA.AGCOM.DET.MARGIN.RATE` | `AaAgentCommissionDetails_MarginRate` | TField |  |  |
| 5 | `AA.AGCOM.DET.MARGIN.PERCENT` | `AaAgentCommissionDetails_MarginPercent` | TField |  |  |
| 6 | `AA.AGCOM.DET.AGENT.EVENT` | `AaAgentCommissionDetails_AgentEvent` |  |  |  |
| 7 | `AA.AGCOM.DET.COMMISSION.NATURE` | `AaAgentCommissionDetails_CommissionNature` | TField |  |  |
| 8 | `AA.AGCOM.DET.RESERVED.8` | `AaAgentCommissionDetails_Reserved8` | TField |  |  |
| 9 | `AA.AGCOM.DET.RESERVED.7` | `AaAgentCommissionDetails_Reserved7` | TField |  |  |
| 10 | `AA.AGCOM.DET.RESERVED.6` | `AaAgentCommissionDetails_Reserved6` | TField |  |  |
| 11 | `AA.AGCOM.DET.RESERVED.5` | `AaAgentCommissionDetails_Reserved5` | TField |  |  |
| 12 | `AA.AGCOM.DET.RESERVED.4` | `AaAgentCommissionDetails_Reserved4` | TField |  |  |
| 13 | `AA.AGCOM.DET.RESERVED.3` | `AaAgentCommissionDetails_Reserved3` | TField |  |  |
| 14 | `AA.AGCOM.DET.RESERVED.2` | `AaAgentCommissionDetails_Reserved2` | TField |  |  |
| 15 | `AA.AGCOM.DET.RESERVED.1` | `AaAgentCommissionDetails_Reserved1` | TField |  |  |
