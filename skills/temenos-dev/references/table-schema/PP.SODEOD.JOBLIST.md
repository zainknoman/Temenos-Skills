# PP.SODEOD.JOBLIST — Table Schema

> Source: `INSERTS/I_F.PP.SODEOD.JOBLIST` in `PP_SODEODService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SEJ.CompanyID` | `PpSodeodJoblist_Companyid` |  |  |  |
| 2 | `PP.SEJ.JobName` | `PpSodeodJoblist_Jobname` |  |  |  |
| 3 | `PP.SEJ.Data` | `PpSodeodJoblist_Data` |  |  |  |
| 4 | `PP.SEJ.ProcessCode` | `PpSodeodJoblist_Processcode` |  |  |  |
| 5 | `PP.SEJ.Status` | `PpSodeodJoblist_Status` |  |  |  |
| 6 | `PP.SEJ.Enabled` | `PpSodeodJoblist_Enabled` |  |  |  |
| 7 | `PP.SEJ.Frequency` | `PpSodeodJoblist_Frequency` |  |  |  |
| 8 | `PP.SEJ.DayInYear` | `PpSodeodJoblist_Dayinyear` |  |  |  |
| 9 | `PP.SEJ.DayInMonth` | `PpSodeodJoblist_Dayinmonth` |  |  |  |
| 10 | `PP.SEJ.RunMondayIndicator` | `PpSodeodJoblist_Runmondayindicator` |  |  |  |
| 11 | `PP.SEJ.RunTuesdayIndicator` | `PpSodeodJoblist_Runtuesdayindicator` |  |  |  |
| 12 | `PP.SEJ.RunWednesdayIndicator` | `PpSodeodJoblist_Runwednesdayindicator` |  |  |  |
| 13 | `PP.SEJ.RunThursdayIndicator` | `PpSodeodJoblist_Runthursdayindicator` |  |  |  |
| 14 | `PP.SEJ.RunFridayIndicator` | `PpSodeodJoblist_Runfridayindicator` |  |  |  |
| 15 | `PP.SEJ.RunSaturdayIndicator` | `PpSodeodJoblist_Runsaturdayindicator` |  |  |  |
| 16 | `PP.SEJ.RunSundayIndicator` | `PpSodeodJoblist_Runsundayindicator` |  |  |  |
| 17 | `PP.SEJ.SkipIndicator` | `PpSodeodJoblist_Skipindicator` |  |  |  |
| 18 | `PP.SEJ.Action` | `PpSodeodJoblist_Action` |  |  |  |
| 19 | `PP.SEJ.OldID` | `PpSodeodJoblist_Oldid` |  |  |  |
| 20 | `PP.SEJ.CurrentID` | `PpSodeodJoblist_Currentid` |  |  |  |
| 21 | `PP.SEJ.EntryTimeStamp` | `PpSodeodJoblist_Entrytimestamp` |  |  |  |
| 22 | `PP.SEJ.OVERRIDE` | `PpSodeodJoblist_Override` |  |  |  |
| 23 | `PP.SEJ.RECORD.STATUS` | `PpSodeodJoblist_RecordStatus` |  |  |  |
| 24 | `PP.SEJ.CURR.NO` | `PpSodeodJoblist_CurrNo` |  |  |  |
| 25 | `PP.SEJ.INPUTTER` | `PpSodeodJoblist_Inputter` |  |  |  |
| 26 | `PP.SEJ.DATE.TIME` | `PpSodeodJoblist_DateTime` |  |  |  |
| 27 | `PP.SEJ.AUTHORISER` | `PpSodeodJoblist_Authoriser` |  |  |  |
| 28 | `PP.SEJ.CO.CODE` | `PpSodeodJoblist_CoCode` |  |  |  |
| 29 | `PP.SEJ.DEPT.CODE` | `PpSodeodJoblist_DeptCode` |  |  |  |
| 30 | `PP.SEJ.AUDITOR.CODE` | `PpSodeodJoblist_AuditorCode` |  |  |  |
| 31 | `PP.SEJ.AUDIT.DATE.TIME` | `PpSodeodJoblist_AuditDateTime` |  |  |  |
