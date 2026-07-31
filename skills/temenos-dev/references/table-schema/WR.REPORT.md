# WR.REPORT — Table Schema

> Source: `INSERTS/I_F.WR.REPORT` in `WR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WR.RP.DESCRIPTION` | `WrReport_Description` | TField |  | 1-60 alphanumeric characters Description about the WR.Report. |
| 2 | `WR.RP.PROCESS.IDENTIFIER` | `WrReport_ProcessIdentifier` | TField |  | 1-60 alphanumeric characters Is the Orchestrate process identifier. Process with REPORT.IDENTIFIER identifier will be instantiated in orchestrate reporting engine and executed. |
| 3 | `WR.RP.REPORT.IDENTIFIER` | `WrReport_ReportIdentifier` | TField |  | 1-60 alphanumeric characters Is the Orchestrate report identifier. This will determine the loadable file list and the report to be rendered by Orchestrate. |
| 4 | `WR.RP.PARAMETER.CHANNEL` | `WrReport_ParameterChannel` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `WR.RP.REPORT.AREA` | `WrReport_ReportArea` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `WR.RP.GROUP` | `WrReport_Group` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `WR.RP.PRE.PROCESS` | `WrReport_PreProcess` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `WR.RP.POST.PROCESS` | `WrReport_PostProcess` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `WR.RP.REPORTS.STYLE` | `WrReport_ReportsStyle` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 10 | `WR.RP.OUTPUT.TYPE` | `WrReport_OutputType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 11 | `WR.RP.ID.CONF.ITEM` | `WrReport_IdConfItem` |  |  |  |
| 12 | `WR.RP.ID.ENQ` | `WrReport_IdEnq` |  |  |  |
| 13 | `WR.RP.ENQ.DESCRIPTION` | `WrReport_EnqDescription` |  |  |  |
| 14 | `WR.RP.MANUAL` | `WrReport_Manual` |  |  |  |
| 15 | `WR.RP.ID.BREAKDOWN` | `WrReport_IdBreakdown` |  |  |  |
| 16 | `WR.RP.SCHEDULE` | `WrReport_Schedule` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 17 | `WR.RP.ONLINE` | `WrReport_Online` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 18 | `WR.RP.RESERVED.5` | `WrReport_Reserved5` | TField |  |  |
| 19 | `WR.RP.RESERVED.4` | `WrReport_Reserved4` | TField |  |  |
| 20 | `WR.RP.RESERVED.3` | `WrReport_Reserved3` | TField |  |  |
| 21 | `WR.RP.RESERVED.2` | `WrReport_Reserved2` | TField |  |  |
| 22 | `WR.RP.RESERVED.1` | `WrReport_Reserved1` | TField |  |  |
| 23 | `WR.RP.RECORD.STATUS` | `WrReport_RecordStatus` | String |  |  |
| 24 | `WR.RP.CURR.NO` | `WrReport_CurrNo` | String |  |  |
| 25 | `WR.RP.INPUTTER` | `WrReport_Inputter` |  |  |  |
| 26 | `WR.RP.DATE.TIME` | `WrReport_DateTime` |  |  |  |
| 27 | `WR.RP.AUTHORISER` | `WrReport_Authoriser` | String |  |  |
| 28 | `WR.RP.CO.CODE` | `WrReport_CoCode` | String |  |  |
| 29 | `WR.RP.DEPT.CODE` | `WrReport_DeptCode` | String |  |  |
| 30 | `WR.RP.AUDITOR.CODE` | `WrReport_AuditorCode` | String |  |  |
| 31 | `WR.RP.AUDIT.DATE.TIME` | `WrReport_AuditDateTime` | String |  |  |
