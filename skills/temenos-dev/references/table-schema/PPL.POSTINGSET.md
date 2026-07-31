# PPL.POSTINGSET — Table Schema

> Source: `INSERTS/I_F.PPL.POSTINGSET` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPST.PostingSetId` | `PplPostingset_Postingsetid` |  |  |  |
| 2 | `PPST.CompanyID` | `PplPostingset_Companyid` |  |  |  |
| 3 | `PPST.PostingProduct` | `PplPostingset_Postingproduct` |  |  |  |
| 4 | `PPST.Ranking` | `PplPostingset_Ranking` |  |  |  |
| 5 | `PPST.StartDatePostingSet` | `PplPostingset_Startdatepostingset` |  |  |  |
| 6 | `PPST.ChargePostingSeparately` | `PplPostingset_Chargepostingseparately` |  |  |  |
| 7 | `PPST.ChargePostingDetail` | `PplPostingset_Chargepostingdetail` |  |  |  |
| 8 | `PPST.VATONPrincipal` | `PplPostingset_Vatonprincipal` |  |  |  |
| 9 | `PPST.VATOnCharge` | `PplPostingset_Vatoncharge` |  |  |  |
| 10 | `PPST.OCPPostingFlag` | `PplPostingset_Ocppostingflag` |  |  |  |
| 11 | `PPST.EndDatePostingSet` | `PplPostingset_Enddatepostingset` |  |  |  |
| 12 | `PPST.RACPostingSet` | `PplPostingset_Racpostingset` |  |  |  |
| 13 | `PPST.RSCPostingSet` | `PplPostingset_Rscpostingset` |  |  |  |
| 14 | `PPST.EntryUserID` | `PplPostingset_Entryuserid` |  |  |  |
| 15 | `PPST.EntryDateTime` | `PplPostingset_Entrydatetime` |  |  |  |
| 16 | `PPST.ApproverUserID` | `PplPostingset_Approveruserid` |  |  |  |
| 17 | `PPST.ApprovedDateTime` | `PplPostingset_Approveddatetime` |  |  |  |
