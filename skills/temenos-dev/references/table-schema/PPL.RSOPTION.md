# PPL.RSOPTION — Table Schema

> Source: `INSERTS/I_F.PPL.RSOPTION` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPRSO.ContractOptionID` | `PplRsoption_Contractoptionid` |  |  |  |
| 2 | `PPRSO.ContractCategoryID` | `PplRsoption_Contractcategoryid` |  |  |  |
| 3 | `PPRSO.OptionRanking` | `PplRsoption_Optionranking` |  |  |  |
| 4 | `PPRSO.RSOption` | `PplRsoption_Rsoption` |  |  |  |
| 5 | `PPRSO.PartyIDType` | `PplRsoption_Partyidtype` |  |  |  |
| 6 | `PPRSO.PartyID` | `PplRsoption_Partyid` |  |  |  |
| 7 | `PPRSO.AccountCompany` | `PplRsoption_Accountcompany` |  |  |  |
| 8 | `PPRSO.AccountNumber` | `PplRsoption_Accountnumber` |  |  |  |
| 9 | `PPRSO.AccountCurrency` | `PplRsoption_Accountcurrency` |  |  |  |
| 10 | `PPRSO.MessageChannel` | `PplRsoption_Messagechannel` |  |  |  |
| 11 | `PPRSO.CoverIndicator` | `PplRsoption_Coverindicator` |  |  |  |
| 12 | `PPRSO.LeadTime` | `PplRsoption_Leadtime` |  |  |  |
| 13 | `PPRSO.AlternativeForCutoff` | `PplRsoption_Alternativeforcutoff` |  |  |  |
| 14 | `PPRSO.AlternativeForRS` | `PplRsoption_Alternativeforrs` |  |  |  |
