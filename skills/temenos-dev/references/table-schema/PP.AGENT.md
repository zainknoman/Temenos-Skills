# PP.AGENT — Table Schema

> Source: `INSERTS/I_F.PP.AGENT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.AG.CompanyID` | `PpAgent_Companyid` | TField |  | Indicates the Financial Table Descriptive(FTD) company for which the record is created. This is NoInput field It gets autopopulated after validation Example : BNK,GB1 |
| 2 | `PP.AG.AgentIdentifierType` | `PpAgent_Agentidentifiertype` | TField | Yes | Indicates the type of identifier used to denote an agent. Possible values: B - When a BIC-8 or a BIC-11 is used to denote the agent. N - When NCC is used to denote the agent. Validation Rules: Mandatory field. 1 alphanumeric characters. User can assign a value based on possible values only. |
| 3 | `PP.AG.AgentIdentifier` | `PpAgent_Agentidentifier` | TField | Yes | Identifies the agent with either a BIC or a NCC. BIC value can be specified as a BIC-8 or a BIC-11 only. Example: BARCGB, BARCGB2106P Validation Rules: Mandatory field. 35 alphanumeric characters. NCC value can have alphanumeric characters which is usually of length 8. Example: SC200050 Validation Rules: Mandatory field. 35 alphanumeric characters. |
| 4 | `PP.AG.StartDate` | `PpAgent_Startdate` | TField |  |  |
| 5 | `PP.AG.EndDate` | `PpAgent_Enddate` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 6 | `PP.AG.RESERVED.5` | `PpAgent_Reserved5` | TField |  |  |
| 7 | `PP.AG.RESERVED.4` | `PpAgent_Reserved4` | TField |  |  |
| 8 | `PP.AG.RESERVED.3` | `PpAgent_Reserved3` | TField |  |  |
| 9 | `PP.AG.RESERVED.2` | `PpAgent_Reserved2` | TField |  |  |
| 10 | `PP.AG.RESERVED.1` | `PpAgent_Reserved1` | TField |  |  |
| 11 | `PP.AG.LOCAL.REF` | `PpAgent_LocalRef` |  |  |  |
| 12 | `PP.AG.OVERRIDE` | `PpAgent_Override` |  |  |  |
| 13 | `PP.AG.RECORD.STATUS` | `PpAgent_RecordStatus` | String |  |  |
| 14 | `PP.AG.CURR.NO` | `PpAgent_CurrNo` | String |  |  |
| 15 | `PP.AG.INPUTTER` | `PpAgent_Inputter` |  |  |  |
| 16 | `PP.AG.DATE.TIME` | `PpAgent_DateTime` |  |  |  |
| 17 | `PP.AG.AUTHORISER` | `PpAgent_Authoriser` | String |  |  |
| 18 | `PP.AG.CO.CODE` | `PpAgent_CoCode` | String |  |  |
| 19 | `PP.AG.DEPT.CODE` | `PpAgent_DeptCode` | String |  |  |
| 20 | `PP.AG.AUDITOR.CODE` | `PpAgent_AuditorCode` | String |  |  |
| 21 | `PP.AG.AUDIT.DATE.TIME` | `PpAgent_AuditDateTime` | String |  |  |
