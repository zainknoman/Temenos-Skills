# TNFCOP.TRADE.TITLE.REPORT — Table Schema

> Source: `INSERTS/I_F.TNFCOP.TRADE.TITLE.REPORT` in `TNFCOP_TradeTitle.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TITLE.RPT.CLEARANCE.MONTH` | `TnfcopTradeTitleReport_ClearanceMonth` | TField |  | This field denotes the Month and Year of Clearance. The format should be MMYYYY. |
| 2 | `TITLE.RPT.LAST.CLEAR.MONTH` | `TnfcopTradeTitleReport_LastClearMonth` | TField |  | This field denotes the last Month and Year of Clearance i.e file sent to Central Bank. The format should be MMYYYY. |
| 3 | `TITLE.RPT.CLEAR.MONTH.REJECT` | `TnfcopTradeTitleReport_ClearMonthReject` | TField |  | This field denotes the Month and Year of Clearance for generation of report for rejected Titles. The format should be MMYYYY. |
| 4 | `TITLE.RPT.LAST.CLEAR.MON.RJT` | `TnfcopTradeTitleReport_LastClearMonRjt` | TField |  | This field denotes the Last Month and Year of Clearance of the Report generated for rejected Titles. The format should be MMYYYY. |
| 5 | `TITLE.RPT.REPORT.TYPE` | `TnfcopTradeTitleReport_ReportType` | TField |  | This field is informational field to indicate if the extract is for Initial report generation or Regeneration of report for rejected trade titles. |
| 6 | `TITLE.RPT.LOCAL.REF` | `TnfcopTradeTitleReport_LocalRef` |  |  |  |
| 7 | `TITLE.RPT.RESERVED.1` | `TnfcopTradeTitleReport_Reserved1` | TField |  |  |
| 8 | `TITLE.RPT.RESERVED.2` | `TnfcopTradeTitleReport_Reserved2` | TField |  |  |
| 9 | `TITLE.RPT.RESERVED.3` | `TnfcopTradeTitleReport_Reserved3` | TField |  |  |
| 10 | `TITLE.RPT.RESERVED.4` | `TnfcopTradeTitleReport_Reserved4` | TField |  |  |
| 11 | `TITLE.RPT.RESERVED.5` | `TnfcopTradeTitleReport_Reserved5` | TField |  |  |
| 12 | `TITLE.RPT.RESERVED.6` | `TnfcopTradeTitleReport_Reserved6` | TField |  |  |
| 13 | `TITLE.RPT.RESERVED.7` | `TnfcopTradeTitleReport_Reserved7` | TField |  |  |
| 14 | `TITLE.RPT.RESERVED.8` | `TnfcopTradeTitleReport_Reserved8` | TField |  |  |
| 15 | `TITLE.RPT.RESERVED.9` | `TnfcopTradeTitleReport_Reserved9` | TField |  |  |
| 16 | `TITLE.RPT.RESERVED.10` | `TnfcopTradeTitleReport_Reserved10` | TField |  |  |
| 17 | `TITLE.RPT.OVERRIDE` | `TnfcopTradeTitleReport_Override` |  |  |  |
| 18 | `TITLE.RPT.RECORD.STATUS` | `TnfcopTradeTitleReport_RecordStatus` | String |  |  |
| 19 | `TITLE.RPT.CURR.NO` | `TnfcopTradeTitleReport_CurrNo` | String |  |  |
| 20 | `TITLE.RPT.INPUTTER` | `TnfcopTradeTitleReport_Inputter` |  |  |  |
| 21 | `TITLE.RPT.DATE.TIME` | `TnfcopTradeTitleReport_DateTime` |  |  |  |
| 22 | `TITLE.RPT.AUTHORISER` | `TnfcopTradeTitleReport_Authoriser` | String |  |  |
| 23 | `TITLE.RPT.CO.CODE` | `TnfcopTradeTitleReport_CoCode` | String |  |  |
| 24 | `TITLE.RPT.DEPT.CODE` | `TnfcopTradeTitleReport_DeptCode` | String |  |  |
| 25 | `TITLE.RPT.AUDITOR.CODE` | `TnfcopTradeTitleReport_AuditorCode` | String |  |  |
| 26 | `TITLE.RPT.AUDIT.DATE.TIME` | `TnfcopTradeTitleReport_AuditDateTime` | String |  |  |
