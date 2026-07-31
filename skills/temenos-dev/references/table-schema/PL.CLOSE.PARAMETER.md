# PL.CLOSE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PL.CLOSE.PARAMETER` in `RE_YearEnd.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PL.PAR.REPORT.TYPE` | `PlCloseParameter_ReportType` |  |  |  |
| 2 | `PL.PAR.REPORT` | `PlCloseParameter_Report` |  |  |  |
| 3 | `PL.PAR.REPORT.DATA` | `PlCloseParameter_ReportData` |  |  |  |
| 4 | `PL.PAR.CLOSE.FREQ.DATE` | `PlCloseParameter_CloseFreqDate` | TField | Yes | The year end and subsequent cycle frequency for this particular company. When this is set the field FINANCIAL.YEAR.END on the COMPANY record is changed to match this date. This field is in two parts: 1) Next Financial Year End: 1-9 Date characters. Default value calculated by the system from the Frequency. 2) Frequency: 2-5 type FQU (standard frequency format). Validation Rules: Mandatory input Must be a month end date. Frequency must be Monthly, Quarterly, Half-yearly or Yearly. The frequency cycle must start with M12. The day in the date and the day in the frequency (last two digits) must be the same. The date cannot be more than twelve months in front of the run date. |
| 5 | `PL.PAR.TYPES.TO.EXCLUDE` | `PlCloseParameter_TypesToExclude` |  |  |  |
| 6 | `PL.PAR.AL.GROUPING` | `PlCloseParameter_AlGrouping` |  |  |  |
| 7 | `PL.PAR.CLOSE.HLT.PRCSS` | `PlCloseParameter_CloseHltPrcss` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `PL.PAR.PROCESSING.DATE` | `PlCloseParameter_ProcessingDate` | TField |  | System field updated when the close out has been run. It contains the date as of which the close out is being run and will have 'CL' appended to it. For example if the close out is to be run as year end December 2007 then the PL.PROCESSING.DATE will hold a value of '20071231CL'. |
| 9 | `PL.PAR.CLOSE.OUT.RUN` | `PlCloseParameter_CloseOutRun` | TField |  | System field set to 'Y' when PL.CLOSE.OUT has been run during the cob. It will be set to 'Y' when the job is launched and set to 'N' once the job has been completed. |
| 10 | `PL.PAR.LAST.RUN.DATE` | `PlCloseParameter_LastRunDate` | TField |  | The date the PL to AL process was last run. |
| 11 | `PL.PAR.LAST.HALT.DATE` | `PlCloseParameter_LastHaltDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 12 | `PL.PAR.ITEMS.TO.EXCLUDE` | `PlCloseParameter_ItemsToExclude` |  |  |  |
| 13 | `PL.PAR.POSITION.TYPE` | `PlCloseParameter_PositionType` |  |  |  |
| 14 | `PL.PAR.CLOSE.CATEGORY` | `PlCloseParameter_CloseCategory` |  |  |  |
| 15 | `PL.PAR.RESERVED.3` | `PlCloseParameter_Reserved3` | TField |  |  |
| 16 | `PL.PAR.RESERVED.2` | `PlCloseParameter_Reserved2` | TField |  |  |
| 17 | `PL.PAR.LOCAL.REF` | `PlCloseParameter_LocalRef` |  |  |  |
| 18 | `PL.PAR.OVERRIDE` | `PlCloseParameter_Override` |  |  |  |
| 19 | `PL.PAR.RECORD.STATUS` | `PlCloseParameter_RecordStatus` | String |  |  |
| 20 | `PL.PAR.CURR.NO` | `PlCloseParameter_CurrNo` | String |  |  |
| 21 | `PL.PAR.INPUTTER` | `PlCloseParameter_Inputter` |  |  |  |
| 22 | `PL.PAR.DATE.TIME` | `PlCloseParameter_DateTime` |  |  |  |
| 23 | `PL.PAR.AUTHORISER` | `PlCloseParameter_Authoriser` | String |  |  |
| 24 | `PL.PAR.CO.CODE` | `PlCloseParameter_CoCode` | String |  |  |
| 25 | `PL.PAR.DEPT.CODE` | `PlCloseParameter_DeptCode` | String |  |  |
| 26 | `PL.PAR.AUDITOR.CODE` | `PlCloseParameter_AuditorCode` | String |  |  |
| 27 | `PL.PAR.AUDIT.DATE.TIME` | `PlCloseParameter_AuditDateTime` | String |  |  |
