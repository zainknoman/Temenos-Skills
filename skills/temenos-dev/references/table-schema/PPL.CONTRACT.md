# PPL.CONTRACT — Table Schema

> Source: `INSERTS/I_F.PPL.CONTRACT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCN.ContractID` | `PplContract_Contractid` |  |  |  |
| 2 | `PPCN.CompanyID` | `PplContract_Companyid` |  |  |  |
| 3 | `PPCN.StartDateContract` | `PplContract_Startdatecontract` |  |  |  |
| 4 | `PPCN.BusinessLine` | `PplContract_Businessline` |  |  |  |
| 5 | `PPCN.ContractType` | `PplContract_Contracttype` |  |  |  |
| 6 | `PPCN.RoutingProduct` | `PplContract_Routingproduct` |  |  |  |
| 7 | `PPCN.PartyIDType` | `PplContract_Partyidtype` |  |  |  |
| 8 | `PPCN.PartyID` | `PplContract_Partyid` |  |  |  |
| 9 | `PPCN.Destination` | `PplContract_Destination` |  |  |  |
| 10 | `PPCN.EndDateContract` | `PplContract_Enddatecontract` |  |  |  |
| 11 | `PPCN.RACContract` | `PplContract_Raccontract` |  |  |  |
| 12 | `PPCN.RSCContract` | `PplContract_Rsccontract` |  |  |  |
| 13 | `PPCN.EntryUserID` | `PplContract_Entryuserid` |  |  |  |
| 14 | `PPCN.EntryDateTime` | `PplContract_Entrydatetime` |  |  |  |
| 15 | `PPCN.ApproverUserID` | `PplContract_Approveruserid` |  |  |  |
| 16 | `PPCN.ApprovedDateTime` | `PplContract_Approveddatetime` |  |  |  |
