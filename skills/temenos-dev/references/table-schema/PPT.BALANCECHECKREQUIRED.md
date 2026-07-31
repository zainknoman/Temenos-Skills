# PPT.BALANCECHECKREQUIRED — Table Schema

> Source: `INSERTS/I_F.PPT.BALANCECHECKREQUIRED` in `PP_BalanceCheckService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCR.CompanyID` | `PptBalancecheckrequired_Companyid` |  |  |  |
| 2 | `PPBCR.Ranking` | `PptBalancecheckrequired_Ranking` |  |  |  |
| 3 | `PPBCR.OriginatingSource` | `PptBalancecheckrequired_Originatingsource` |  |  |  |
| 4 | `PPBCR.AccountType` | `PptBalancecheckrequired_Accounttype` |  |  |  |
| 5 | `PPBCR.IncomingMessageType` | `PptBalancecheckrequired_Incomingmessagetype` |  |  |  |
| 6 | `PPBCR.ClearingNatureCode` | `PptBalancecheckrequired_Clearingnaturecode` |  |  |  |
| 7 | `PPBCR.StartDateBalanceCheckRequired` | `PptBalancecheckrequired_Startdatebalancecheckrequired` |  |  |  |
| 8 | `PPBCR.BalanceCheckRequiredFlag` | `PptBalancecheckrequired_Balancecheckrequiredflag` |  |  |  |
| 9 | `PPBCR.SettlementTransactionIndicator` | `PptBalancecheckrequired_Settlementtransactionindicator` |  |  |  |
| 10 | `PPBCR.EndDateBalanceCheckRequired` | `PptBalancecheckrequired_Enddatebalancecheckrequired` |  |  |  |
| 11 | `PPBCR.RACBalanceCheckRequired` | `PptBalancecheckrequired_Racbalancecheckrequired` |  |  |  |
| 12 | `PPBCR.RSCBalanceCheckRequired` | `PptBalancecheckrequired_Rscbalancecheckrequired` |  |  |  |
| 13 | `PPBCR.EntryUserID` | `PptBalancecheckrequired_Entryuserid` |  |  |  |
| 14 | `PPBCR.EntryDateTime` | `PptBalancecheckrequired_Entrydatetime` |  |  |  |
| 15 | `PPBCR.ApproverUserID` | `PptBalancecheckrequired_Approveruserid` |  |  |  |
| 16 | `PPBCR.ApprovedDateTime` | `PptBalancecheckrequired_Approveddatetime` |  |  |  |
