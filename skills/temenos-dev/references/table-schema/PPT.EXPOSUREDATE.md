# PPT.EXPOSUREDATE — Table Schema

> Source: `INSERTS/I_F.PPT.EXPOSUREDATE` in `PP_DateDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPEXD.CompanyID` | `PptExposuredate_Companyid` |  |  |  |
| 2 | `PPEXD.ProductCode` | `PptExposuredate_Productcode` |  |  |  |
| 3 | `PPEXD.StartDateExposureDate` | `PptExposuredate_Startdateexposuredate` |  |  |  |
| 4 | `PPEXD.Ranking` | `PptExposuredate_Ranking` |  |  |  |
| 5 | `PPEXD.ExposureDateBase` | `PptExposuredate_Exposuredatebase` |  |  |  |
| 6 | `PPEXD.OffsetDays` | `PptExposuredate_Offsetdays` |  |  |  |
| 7 | `PPEXD.EndDateExposureDate` | `PptExposuredate_Enddateexposuredate` |  |  |  |
| 8 | `PPEXD.RACExposureDate` | `PptExposuredate_Racexposuredate` |  |  |  |
| 9 | `PPEXD.RSCExposureDate` | `PptExposuredate_Rscexposuredate` |  |  |  |
| 10 | `PPEXD.EntryUserID` | `PptExposuredate_Entryuserid` |  |  |  |
| 11 | `PPEXD.EntryDateTime` | `PptExposuredate_Entrydatetime` |  |  |  |
| 12 | `PPEXD.ApproverUserID` | `PptExposuredate_Approveruserid` |  |  |  |
| 13 | `PPEXD.ApprovedDateTime` | `PptExposuredate_Approveddatetime` |  |  |  |
