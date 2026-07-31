# PPL.STANDINGSETTMNTINSTRUC — Table Schema

> Source: `INSERTS/I_F.PPL.STANDINGSETTMNTINSTRUC` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSSI.CompanyID` | `PplStandingsettmntinstruc_Companyid` |  |  |  |
| 2 | `PPSSI.SSIID` | `PplStandingsettmntinstruc_Ssiid` |  |  |  |
| 3 | `PPSSI.StartDateSSI` | `PplStandingsettmntinstruc_Startdatessi` |  |  |  |
| 4 | `PPSSI.PartyBIC` | `PplStandingsettmntinstruc_Partybic` |  |  |  |
| 5 | `PPSSI.BankName` | `PplStandingsettmntinstruc_Bankname` |  |  |  |
| 6 | `PPSSI.City` | `PplStandingsettmntinstruc_City` |  |  |  |
| 7 | `PPSSI.TransactionCurrency` | `PplStandingsettmntinstruc_Transactioncurrency` |  |  |  |
| 8 | `PPSSI.RoutingProduct` | `PplStandingsettmntinstruc_Routingproduct` |  |  |  |
| 9 | `PPSSI.CurrencyCorrespondentIDType` | `PplStandingsettmntinstruc_Currencycorrespondentidtype` |  |  |  |
| 10 | `PPSSI.CurrencyCorrespondentID` | `PplStandingsettmntinstruc_Currencycorrespondentid` |  |  |  |
| 11 | `PPSSI.OverrideThroughUpload` | `PplStandingsettmntinstruc_Overridethroughupload` |  |  |  |
| 12 | `PPSSI.EndDateSSI` | `PplStandingsettmntinstruc_Enddatessi` |  |  |  |
| 13 | `PPSSI.RACStandingSettlementInstruct` | `PplStandingsettmntinstruc_Racstandingsettlementinstruct` |  |  |  |
| 14 | `PPSSI.RSCStandingSettlementInstruct` | `PplStandingsettmntinstruc_Rscstandingsettlementinstruct` |  |  |  |
| 15 | `PPSSI.EntryUserID` | `PplStandingsettmntinstruc_Entryuserid` |  |  |  |
| 16 | `PPSSI.EntryDateTime` | `PplStandingsettmntinstruc_Entrydatetime` |  |  |  |
| 17 | `PPSSI.ApproverUserID` | `PplStandingsettmntinstruc_Approveruserid` |  |  |  |
| 18 | `PPSSI.ApprovedDateTime` | `PplStandingsettmntinstruc_Approveddatetime` |  |  |  |
