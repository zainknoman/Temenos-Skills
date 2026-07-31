# USCORE.PRINT.FORMAT — Table Schema

> Source: `INSERTS/I_F.USCORE.PRINT.FORMAT` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.FORM.DESCRIPTION` | `UscorePrintFormat_Description` |  |  |  |
| 2 | `USCORE.FORM.LINE.NO` | `UscorePrintFormat_LineNo` |  |  |  |
| 3 | `USCORE.FORM.VALUE.DESC` | `UscorePrintFormat_ValueDesc` |  |  |  |
| 4 | `USCORE.FORM.INDENT` | `UscorePrintFormat_Indent` |  |  |  |
| 5 | `USCORE.FORM.HANDOFF.POS` | `UscorePrintFormat_HandoffPos` |  |  |  |
| 6 | `USCORE.FORM.TEXT` | `UscorePrintFormat_Text` |  |  |  |
| 7 | `USCORE.FORM.RESERVED.13` | `UscorePrintFormat_Reserved13` |  |  |  |
| 8 | `USCORE.FORM.RESERVED.12` | `UscorePrintFormat_Reserved12` |  |  |  |
| 9 | `USCORE.FORM.RESERVED.11` | `UscorePrintFormat_Reserved11` |  |  |  |
| 10 | `USCORE.FORM.RESERVED.10` | `UscorePrintFormat_Reserved10` | TField |  |  |
| 11 | `USCORE.FORM.RESERVED.9` | `UscorePrintFormat_Reserved9` | TField |  |  |
| 12 | `USCORE.FORM.RESERVED.8` | `UscorePrintFormat_Reserved8` | TField |  |  |
| 13 | `USCORE.FORM.RESERVED.7` | `UscorePrintFormat_Reserved7` | TField |  |  |
| 14 | `USCORE.FORM.RESERVED.6` | `UscorePrintFormat_Reserved6` | TField |  |  |
| 15 | `USCORE.FORM.RESERVED.5` | `UscorePrintFormat_Reserved5` | TField |  |  |
| 16 | `USCORE.FORM.RESERVED.4` | `UscorePrintFormat_Reserved4` | TField |  |  |
| 17 | `USCORE.FORM.RESERVED.3` | `UscorePrintFormat_Reserved3` | TField |  |  |
| 18 | `USCORE.FORM.RESERVED.2` | `UscorePrintFormat_Reserved2` | TField |  |  |
| 19 | `USCORE.FORM.RESERVED.1` | `UscorePrintFormat_Reserved1` | TField |  |  |
| 20 | `USCORE.FORM.RECORD.STATUS` | `UscorePrintFormat_RecordStatus` | String |  |  |
| 21 | `USCORE.FORM.CURR.NO` | `UscorePrintFormat_CurrNo` | String |  |  |
| 22 | `USCORE.FORM.INPUTTER` | `UscorePrintFormat_Inputter` |  |  |  |
| 23 | `USCORE.FORM.DATE.TIME` | `UscorePrintFormat_DateTime` |  |  |  |
| 24 | `USCORE.FORM.AUTHORISER` | `UscorePrintFormat_Authoriser` | String |  |  |
| 25 | `USCORE.FORM.CO.CODE` | `UscorePrintFormat_CoCode` | String |  |  |
| 26 | `USCORE.FORM.DEPT.CODE` | `UscorePrintFormat_DeptCode` | String |  |  |
| 27 | `USCORE.FORM.AUDITOR.CODE` | `UscorePrintFormat_AuditorCode` | String |  |  |
| 28 | `USCORE.FORM.AUDIT.DATE.TIME` | `UscorePrintFormat_AuditDateTime` | String |  |  |
