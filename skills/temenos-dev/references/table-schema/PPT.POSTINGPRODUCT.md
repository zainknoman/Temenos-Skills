# PPT.POSTINGPRODUCT — Table Schema

> Source: `INSERTS/I_F.PPT.POSTINGPRODUCT` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPOP.CompanyID` | `PptPostingproduct_Companyid` |  |  |  |
| 2 | `PPPOP.PostingProduct` | `PptPostingproduct_Postingproduct` |  |  |  |
| 3 | `PPPOP.Description` | `PptPostingproduct_Description` |  |  |  |
| 4 | `PPPOP.RACPostingProduct` | `PptPostingproduct_Racpostingproduct` |  |  |  |
| 5 | `PPPOP.RSCPostingProduct` | `PptPostingproduct_Rscpostingproduct` |  |  |  |
| 6 | `PPPOP.EntryUserID` | `PptPostingproduct_Entryuserid` |  |  |  |
| 7 | `PPPOP.EntryDateTime` | `PptPostingproduct_Entrydatetime` |  |  |  |
| 8 | `PPPOP.ApproverUserID` | `PptPostingproduct_Approveruserid` |  |  |  |
| 9 | `PPPOP.ApprovedDateTime` | `PptPostingproduct_Approveddatetime` |  |  |  |
