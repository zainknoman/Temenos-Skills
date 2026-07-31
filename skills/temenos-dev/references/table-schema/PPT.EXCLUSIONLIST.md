# PPT.EXCLUSIONLIST — Table Schema

> Source: `INSERTS/I_F.PPT.EXCLUSIONLIST` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPEXL.CompanyID` | `PptExclusionlist_Companyid` |  |  |  |
| 2 | `PPEXL.CountryCode` | `PptExclusionlist_Countrycode` |  |  |  |
| 3 | `PPEXL.IBANNationalID` | `PptExclusionlist_Ibannationalid` |  |  |  |
| 4 | `PPEXL.BICCode` | `PptExclusionlist_Biccode` |  |  |  |
| 5 | `PPEXL.OverrideThroughUpload` | `PptExclusionlist_Overridethroughupload` |  |  |  |
| 6 | `PPEXL.SourceKey` | `PptExclusionlist_Sourcekey` |  |  |  |
| 7 | `PPEXL.StartDateExclusionListTable` | `PptExclusionlist_Startdateexclusionlisttable` |  |  |  |
| 8 | `PPEXL.EndDateExclusionListTable` | `PptExclusionlist_Enddateexclusionlisttable` |  |  |  |
| 9 | `PPEXL.RACExclusionListTable` | `PptExclusionlist_Racexclusionlisttable` |  |  |  |
| 10 | `PPEXL.RSCExclusionListTable` | `PptExclusionlist_Rscexclusionlisttable` |  |  |  |
| 11 | `PPEXL.EntryUserID` | `PptExclusionlist_Entryuserid` |  |  |  |
| 12 | `PPEXL.EntryDateTime` | `PptExclusionlist_Entrydatetime` |  |  |  |
| 13 | `PPEXL.ApproverUserID` | `PptExclusionlist_Approveruserid` |  |  |  |
| 14 | `PPEXL.ApprovedDateTime` | `PptExclusionlist_Approveddatetime` |  |  |  |
