# PPT.MANUALAUTHREQUIRED — Table Schema

> Source: `INSERTS/I_F.PPT.MANUALAUTHREQUIRED` in `PP_BalanceCheckService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPMAR.CompanyID` | `PptManualauthrequired_Companyid` |  |  |  |
| 2 | `PPMAR.Ranking` | `PptManualauthrequired_Ranking` |  |  |  |
| 3 | `PPMAR.BusinessLine` | `PptManualauthrequired_Businessline` |  |  |  |
| 4 | `PPMAR.OriginatingWorkflow` | `PptManualauthrequired_Originatingworkflow` |  |  |  |
| 5 | `PPMAR.OriginatingSource` | `PptManualauthrequired_Originatingsource` |  |  |  |
| 6 | `PPMAR.MessagePriority` | `PptManualauthrequired_Messagepriority` |  |  |  |
| 7 | `PPMAR.BankingPriority` | `PptManualauthrequired_Bankingpriority` |  |  |  |
| 8 | `PPMAR.TransactionAmountUpperLimit` | `PptManualauthrequired_Transactionamountupperlimit` |  |  |  |
| 9 | `PPMAR.IncomingMessageType` | `PptManualauthrequired_Incomingmessagetype` |  |  |  |
| 10 | `PPMAR.ClearingNatureCode` | `PptManualauthrequired_Clearingnaturecode` |  |  |  |
| 11 | `PPMAR.StartDateAuthRequired` | `PptManualauthrequired_Startdateauthrequired` |  |  |  |
| 12 | `PPMAR.ManualAuthRequiredFlag` | `PptManualauthrequired_Manualauthrequiredflag` |  |  |  |
| 13 | `PPMAR.EndDateAuthRequired` | `PptManualauthrequired_Enddateauthrequired` |  |  |  |
| 14 | `PPMAR.RACAuthRequired` | `PptManualauthrequired_Racauthrequired` |  |  |  |
| 15 | `PPMAR.RSCAuthRequired` | `PptManualauthrequired_Rscauthrequired` |  |  |  |
| 16 | `PPMAR.EntryUserID` | `PptManualauthrequired_Entryuserid` |  |  |  |
| 17 | `PPMAR.EntryDateTime` | `PptManualauthrequired_Entrydatetime` |  |  |  |
| 18 | `PPMAR.ApproverUserID` | `PptManualauthrequired_Approveruserid` |  |  |  |
| 19 | `PPMAR.ApprovedDateTime` | `PptManualauthrequired_Approveddatetime` |  |  |  |
