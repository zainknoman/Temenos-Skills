# PPT.REJECTRESPONSEACTION — Table Schema

> Source: `INSERTS/I_F.PPT.REJECTRESPONSEACTION` in `PP_BalanceCheckService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPRRA.CompanyID` | `PptRejectresponseaction_Companyid` |  |  |  |
| 2 | `PPRRA.Ranking` | `PptRejectresponseaction_Ranking` |  |  |  |
| 3 | `PPRRA.BusinessLine` | `PptRejectresponseaction_Businessline` |  |  |  |
| 4 | `PPRRA.OriginatingWorkflow` | `PptRejectresponseaction_Originatingworkflow` |  |  |  |
| 5 | `PPRRA.OriginatingSource` | `PptRejectresponseaction_Originatingsource` |  |  |  |
| 6 | `PPRRA.MessagePriority` | `PptRejectresponseaction_Messagepriority` |  |  |  |
| 7 | `PPRRA.BankingPriority` | `PptRejectresponseaction_Bankingpriority` |  |  |  |
| 8 | `PPRRA.TransactionAmountUpperLimit` | `PptRejectresponseaction_Transactionamountupperlimit` |  |  |  |
| 9 | `PPRRA.IncomingMessageType` | `PptRejectresponseaction_Incomingmessagetype` |  |  |  |
| 10 | `PPRRA.ClearingNatureCode` | `PptRejectresponseaction_Clearingnaturecode` |  |  |  |
| 11 | `PPRRA.StartDateRejectResponseAction` | `PptRejectresponseaction_Startdaterejectresponseaction` |  |  |  |
| 12 | `PPRRA.ManualRejectResponseAction` | `PptRejectresponseaction_Manualrejectresponseaction` |  |  |  |
| 13 | `PPRRA.EndDateRejectResponseAction` | `PptRejectresponseaction_Enddaterejectresponseaction` |  |  |  |
| 14 | `PPRRA.RACRejectResponseAction` | `PptRejectresponseaction_Racrejectresponseaction` |  |  |  |
| 15 | `PPRRA.RSCRejectResponseAction` | `PptRejectresponseaction_Rscrejectresponseaction` |  |  |  |
| 16 | `PPRRA.EntryUserID` | `PptRejectresponseaction_Entryuserid` |  |  |  |
| 17 | `PPRRA.EntryDateTime` | `PptRejectresponseaction_Entrydatetime` |  |  |  |
| 18 | `PPRRA.ApproverUserID` | `PptRejectresponseaction_Approveruserid` |  |  |  |
| 19 | `PPRRA.ApprovedDateTime` | `PptRejectresponseaction_Approveddatetime` |  |  |  |
