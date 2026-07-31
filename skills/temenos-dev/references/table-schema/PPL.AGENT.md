# PPL.AGENT — Table Schema

> Source: `INSERTS/I_F.PPL.AGENT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPAG.AgentID` | `PplAgent_Agentid` |  |  |  |
| 2 | `PPAG.CompanyID` | `PplAgent_Companyid` |  |  |  |
| 3 | `PPAG.PartyBIC` | `PplAgent_Partybic` |  |  |  |
| 4 | `PPAG.StartDateAgent` | `PplAgent_Startdateagent` |  |  |  |
| 5 | `PPAG.AgentIdentifierType` | `PplAgent_Agentidentifiertype` |  |  |  |
| 6 | `PPAG.AgentIdentifier` | `PplAgent_Agentidentifier` |  |  |  |
| 7 | `PPAG.EndDateAgent` | `PplAgent_Enddateagent` |  |  |  |
| 8 | `PPAG.RACAgent` | `PplAgent_Racagent` |  |  |  |
| 9 | `PPAG.RSCAgent` | `PplAgent_Rscagent` |  |  |  |
| 10 | `PPAG.EntryUserID` | `PplAgent_Entryuserid` |  |  |  |
| 11 | `PPAG.EntryDateTime` | `PplAgent_Entrydatetime` |  |  |  |
| 12 | `PPAG.ApproverUserID` | `PplAgent_Approveruserid` |  |  |  |
| 13 | `PPAG.ApprovedDateTime` | `PplAgent_Approveddatetime` |  |  |  |
