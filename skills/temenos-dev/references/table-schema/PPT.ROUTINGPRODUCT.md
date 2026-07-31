# PPT.ROUTINGPRODUCT — Table Schema

> Source: `INSERTS/I_F.PPT.ROUTINGPRODUCT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPROP.CompanyID` | `PptRoutingproduct_Companyid` |  |  |  |
| 2 | `PPROP.RoutingProduct` | `PptRoutingproduct_Routingproduct` |  |  |  |
| 3 | `PPROP.Description` | `PptRoutingproduct_Description` |  |  |  |
| 4 | `PPROP.RACRoutingProduct` | `PptRoutingproduct_Racroutingproduct` |  |  |  |
| 5 | `PPROP.RSCRoutingProduct` | `PptRoutingproduct_Rscroutingproduct` |  |  |  |
| 6 | `PPROP.EntryUserID` | `PptRoutingproduct_Entryuserid` |  |  |  |
| 7 | `PPROP.EntryDateTime` | `PptRoutingproduct_Entrydatetime` |  |  |  |
| 8 | `PPROP.ApproverUserID` | `PptRoutingproduct_Approveruserid` |  |  |  |
| 9 | `PPROP.ApprovedDateTime` | `PptRoutingproduct_Approveddatetime` |  |  |  |
