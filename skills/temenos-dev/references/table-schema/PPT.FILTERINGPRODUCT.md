# PPT.FILTERINGPRODUCT — Table Schema

> Source: `INSERTS/I_F.PPT.FILTERINGPRODUCT` in `PP_FilteringService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPFLP.CompanyID` | `PptFilteringproduct_Companyid` |  |  |  |
| 2 | `PPFLP.FilteringProduct` | `PptFilteringproduct_Filteringproduct` |  |  |  |
| 3 | `PPFLP.Description` | `PptFilteringproduct_Description` |  |  |  |
| 4 | `PPFLP.RACFilteringProduct` | `PptFilteringproduct_Racfilteringproduct` |  |  |  |
| 5 | `PPFLP.RSCFilteringProduct` | `PptFilteringproduct_Rscfilteringproduct` |  |  |  |
| 6 | `PPFLP.EntryUserID` | `PptFilteringproduct_Entryuserid` |  |  |  |
| 7 | `PPFLP.EntryDateTime` | `PptFilteringproduct_Entrydatetime` |  |  |  |
| 8 | `PPFLP.ApproverUserID` | `PptFilteringproduct_Approveruserid` |  |  |  |
| 9 | `PPFLP.ApprovedDateTime` | `PptFilteringproduct_Approveddatetime` |  |  |  |
