# USCORE.GL.LINE — Table Schema

> Source: `INSERTS/I_F.USCORE.GL.LINE` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.DEF.DESC` | `UscoreGlLine_Desc` |  |  |  |
| 2 | `USCORE.DEF.LINE.NO` | `UscoreGlLine_LineNo` |  |  |  |
| 3 | `USCORE.DEF.IFRS.NO` | `UscoreGlLine_IfrsNo` |  |  |  |
| 4 | `USCORE.DEF.EXTERNAL.REF` | `UscoreGlLine_ExternalRef` |  |  |  |
| 5 | `USCORE.DEF.RESERVED.13` | `UscoreGlLine_Reserved13` |  |  |  |
| 6 | `USCORE.DEF.RESERVED.12` | `UscoreGlLine_Reserved12` |  |  |  |
| 7 | `USCORE.DEF.RESERVED.11` | `UscoreGlLine_Reserved11` |  |  |  |
| 8 | `USCORE.DEF.REPORT.DESC` | `UscoreGlLine_ReportDesc` | TField |  |  |
| 9 | `USCORE.DEF.LINE.HEAD` | `UscoreGlLine_LineHead` |  |  |  |
| 10 | `USCORE.DEF.RESERVED.9` | `UscoreGlLine_Reserved9` | TField |  |  |
| 11 | `USCORE.DEF.RESERVED.8` | `UscoreGlLine_Reserved8` | TField |  |  |
| 12 | `USCORE.DEF.RESERVED.7` | `UscoreGlLine_Reserved7` | TField |  |  |
| 13 | `USCORE.DEF.RESERVED.6` | `UscoreGlLine_Reserved6` | TField |  |  |
| 14 | `USCORE.DEF.RESERVED.5` | `UscoreGlLine_Reserved5` | TField |  |  |
| 15 | `USCORE.DEF.RESERVED.4` | `UscoreGlLine_Reserved4` | TField |  |  |
| 16 | `USCORE.DEF.RESERVED.3` | `UscoreGlLine_Reserved3` | TField |  |  |
| 17 | `USCORE.DEF.RESERVED.2` | `UscoreGlLine_Reserved2` | TField |  |  |
| 18 | `USCORE.DEF.RESERVED.1` | `UscoreGlLine_Reserved1` | TField |  |  |
| 19 | `USCORE.DEF.RECORD.STATUS` | `UscoreGlLine_RecordStatus` | String |  |  |
| 20 | `USCORE.DEF.CURR.NO` | `UscoreGlLine_CurrNo` | String |  |  |
| 21 | `USCORE.DEF.INPUTTER` | `UscoreGlLine_Inputter` |  |  |  |
| 22 | `USCORE.DEF.DATE.TIME` | `UscoreGlLine_DateTime` |  |  |  |
| 23 | `USCORE.DEF.AUTHORISER` | `UscoreGlLine_Authoriser` | String |  |  |
| 24 | `USCORE.DEF.CO.CODE` | `UscoreGlLine_CoCode` | String |  |  |
| 25 | `USCORE.DEF.DEPT.CODE` | `UscoreGlLine_DeptCode` | String |  |  |
| 26 | `USCORE.DEF.AUDITOR.CODE` | `UscoreGlLine_AuditorCode` | String |  |  |
| 27 | `USCORE.DEF.AUDIT.DATE.TIME` | `UscoreGlLine_AuditDateTime` | String |  |  |
