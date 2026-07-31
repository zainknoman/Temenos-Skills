# TV.COB.REPORTS.PARAM — Table Schema

> Source: `INSERTS/I_F.TV.COB.REPORTS.PARAM` in `TV_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TV.CRP.REPORT.NAME` | `TvCobReportsParam_ReportName` |  |  |  |
| 2 | `TV.CRP.RESERVED.4` | `TvCobReportsParam_Reserved4` | TField |  |  |
| 3 | `TV.CRP.RESERVED.3` | `TvCobReportsParam_Reserved3` | TField |  |  |
| 4 | `TV.CRP.RESERVED.2` | `TvCobReportsParam_Reserved2` | TField |  |  |
| 5 | `TV.CRP.RESERVED.1` | `TvCobReportsParam_Reserved1` | TField |  |  |
| 6 | `TV.CRP.RECORD.STATUS` | `TvCobReportsParam_RecordStatus` | String |  |  |
| 7 | `TV.CRP.CURR.NO` | `TvCobReportsParam_CurrNo` | String |  |  |
| 8 | `TV.CRP.INPUTTER` | `TvCobReportsParam_Inputter` |  |  |  |
| 9 | `TV.CRP.DATE.TIME` | `TvCobReportsParam_DateTime` |  |  |  |
| 10 | `TV.CRP.AUTHORISER` | `TvCobReportsParam_Authoriser` | String |  |  |
| 11 | `TV.CRP.CO.CODE` | `TvCobReportsParam_CoCode` | String |  |  |
| 12 | `TV.CRP.DEPT.CODE` | `TvCobReportsParam_DeptCode` | String |  |  |
| 13 | `TV.CRP.AUDITOR.CODE` | `TvCobReportsParam_AuditorCode` | String |  |  |
| 14 | `TV.CRP.AUDIT.DATE.TIME` | `TvCobReportsParam_AuditDateTime` | String |  |  |
