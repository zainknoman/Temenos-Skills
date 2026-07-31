# PPT.SODEODJOBLIST — Table Schema

> Source: `INSERTS/I_F.PPT.SODEODJOBLIST` in `PP_SODEODService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSEJ.CompanyID` | `PptSodeodjoblist_Companyid` |  |  |  |
| 2 | `PPSEJ.JobName` | `PptSodeodjoblist_Jobname` |  |  |  |
| 3 | `PPSEJ.DataDW` | `PptSodeodjoblist_Datadw` |  |  |  |
| 4 | `PPSEJ.ProcessCode` | `PptSodeodjoblist_Processcode` |  |  |  |
| 5 | `PPSEJ.Status` | `PptSodeodjoblist_Status` |  |  |  |
| 6 | `PPSEJ.Enabled` | `PptSodeodjoblist_Enabled` |  |  |  |
| 7 | `PPSEJ.Frequency` | `PptSodeodjoblist_Frequency` |  |  |  |
| 8 | `PPSEJ.DayInYear` | `PptSodeodjoblist_Dayinyear` |  |  |  |
| 9 | `PPSEJ.DayInMonth` | `PptSodeodjoblist_Dayinmonth` |  |  |  |
| 10 | `PPSEJ.RunMondayIndicator` | `PptSodeodjoblist_Runmondayindicator` |  |  |  |
| 11 | `PPSEJ.RunTuesdayIndicator` | `PptSodeodjoblist_Runtuesdayindicator` |  |  |  |
| 12 | `PPSEJ.RunWednesdayIndicator` | `PptSodeodjoblist_Runwednesdayindicator` |  |  |  |
| 13 | `PPSEJ.RunThursdayIndicator` | `PptSodeodjoblist_Runthursdayindicator` |  |  |  |
| 14 | `PPSEJ.RunFridayIndicator` | `PptSodeodjoblist_Runfridayindicator` |  |  |  |
| 15 | `PPSEJ.RunSaturdayIndicator` | `PptSodeodjoblist_Runsaturdayindicator` |  |  |  |
| 16 | `PPSEJ.RunSundayIndicator` | `PptSodeodjoblist_Runsundayindicator` |  |  |  |
| 17 | `PPSEJ.SkipIndicator` | `PptSodeodjoblist_Skipindicator` |  |  |  |
| 18 | `PPSEJ.StartTimestamp` | `PptSodeodjoblist_Starttimestamp` |  |  |  |
| 19 | `PPSEJ.EndTimestamp` | `PptSodeodjoblist_Endtimestamp` |  |  |  |
| 20 | `PPSEJ.EntryUserID` | `PptSodeodjoblist_Entryuserid` |  |  |  |
| 21 | `PPSEJ.EntryDateTime` | `PptSodeodjoblist_Entrydatetime` |  |  |  |
| 22 | `PPSEJ.ApproverUserID` | `PptSodeodjoblist_Approveruserid` |  |  |  |
| 23 | `PPSEJ.ApprovedDateTime` | `PptSodeodjoblist_Approveddatetime` |  |  |  |
