# PP.CLR.REPORTS.FILE — Table Schema

> Source: `INSERTS/I_F.PP.CLR.REPORTS.FILE` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCRF.Clearing` | `PpClrReportsFile_Clearing` | TField |  |  |
| 2 | `PPCRF.FileType` | `PpClrReportsFile_Filetype` | TField |  |  |
| 3 | `PPCRF.FileReference` | `PpClrReportsFile_Filereference` | TField |  |  |
| 4 | `PPCRF.DateTime` | `PpClrReportsFile_Datetime` | TField |  |  |
| 5 | `PPCRF.InterBankSettlementDate` | `PpClrReportsFile_Interbanksettlementdate` | TField |  |  |
| 6 | `PPCRF.FieldName` | `PpClrReportsFile_Fieldname` |  |  |  |
| 7 | `PPCRF.FieldContent` | `PpClrReportsFile_Fieldcontent` |  |  |  |
| 8 | `PPCRF.RESERVED.5` | `PpClrReportsFile_Reserved5` | TField |  |  |
| 9 | `PPCRF.RESERVED.4` | `PpClrReportsFile_Reserved4` | TField |  |  |
| 10 | `PPCRF.RESERVED.3` | `PpClrReportsFile_Reserved3` | TField |  |  |
| 11 | `PPCRF.RESERVED.2` | `PpClrReportsFile_Reserved2` | TField |  |  |
| 12 | `PPCRF.RESERVED.1` | `PpClrReportsFile_Reserved1` | TField |  |  |
| 13 | `PPCRF.RECORD.STATUS` | `PpClrReportsFile_RecordStatus` | String |  |  |
| 14 | `PPCRF.CURR.NO` | `PpClrReportsFile_CurrNo` | String |  |  |
| 15 | `PPCRF.INPUTTER` | `PpClrReportsFile_Inputter` |  |  |  |
| 16 | `PPCRF.DATE.TIME` | `PpClrReportsFile_DateTime` |  |  |  |
| 17 | `PPCRF.AUTHORISER` | `PpClrReportsFile_Authoriser` | String |  |  |
| 18 | `PPCRF.CO.CODE` | `PpClrReportsFile_CoCode` | String |  |  |
| 19 | `PPCRF.DEPT.CODE` | `PpClrReportsFile_DeptCode` | String |  |  |
| 20 | `PPCRF.AUDITOR.CODE` | `PpClrReportsFile_AuditorCode` | String |  |  |
| 21 | `PPCRF.AUDIT.DATE.TIME` | `PpClrReportsFile_AuditDateTime` | String |  |  |
