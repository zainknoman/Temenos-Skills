# PPT.REGION — Table Schema

> Source: `INSERTS/I_F.PPT.REGION` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTRG.CountryCode` | `PptRegion_Countrycode` |  |  |  |
| 2 | `PPTRG.Region` | `PptRegion_Region` |  |  |  |
| 3 | `PPTRG.RACRegion` | `PptRegion_Racregion` |  |  |  |
| 4 | `PPTRG.RSCRegion` | `PptRegion_Rscregion` |  |  |  |
| 5 | `PPTRG.EntryUserID` | `PptRegion_Entryuserid` |  |  |  |
| 6 | `PPTRG.EntryDateTime` | `PptRegion_Entrydatetime` |  |  |  |
| 7 | `PPTRG.ApproverUserID` | `PptRegion_Approveruserid` |  |  |  |
| 8 | `PPTRG.ApprovedDateTime` | `PptRegion_Approveddatetime` |  |  |  |
