# PPT.RMA — Table Schema

> Source: `INSERTS/I_F.PPT.RMA` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPRMA.RMAID` | `PptRma_Rmaid` |  |  |  |
| 2 | `PPRMA.CompanyID` | `PptRma_Companyid` |  |  |  |
| 3 | `PPRMA.BICCode` | `PptRma_Biccode` |  |  |  |
| 4 | `PPRMA.StartDateRMA` | `PptRma_Startdaterma` |  |  |  |
| 5 | `PPRMA.SwiftService` | `PptRma_Swiftservice` |  |  |  |
| 6 | `PPRMA.MessageTypeInclude` | `PptRma_Messagetypeinclude` |  |  |  |
| 7 | `PPRMA.MessageTypeExclude` | `PptRma_Messagetypeexclude` |  |  |  |
| 8 | `PPRMA.OverrideThroughUpload` | `PptRma_Overridethroughupload` |  |  |  |
| 9 | `PPRMA.EndDateRMA` | `PptRma_Enddaterma` |  |  |  |
| 10 | `PPRMA.RACRMA` | `PptRma_Racrma` |  |  |  |
| 11 | `PPRMA.RSCRMA` | `PptRma_Rscrma` |  |  |  |
| 12 | `PPRMA.EntryUserID` | `PptRma_Entryuserid` |  |  |  |
| 13 | `PPRMA.EntryDateTime` | `PptRma_Entrydatetime` |  |  |  |
| 14 | `PPRMA.ApproverUserID` | `PptRma_Approveruserid` |  |  |  |
| 15 | `PPRMA.ApprovedDateTime` | `PptRma_Approveddatetime` |  |  |  |
