# USCORE.EMAIL.ALERT — Table Schema

> Source: `INSERTS/I_F.USCORE.EMAIL.ALERT` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EMAIL.DESCRIPTION` | `UscoreEmailAlert_Description` | TField |  |  |
| 2 | `EMAIL.ALERT.FUNCTION` | `UscoreEmailAlert_AlertFunction` |  |  |  |
| 3 | `EMAIL.TEC.ITEM` | `UscoreEmailAlert_TecItem` |  |  |  |
| 4 | `EMAIL.RESERVED.1` | `UscoreEmailAlert_Reserved1` |  |  |  |
| 5 | `EMAIL.RESERVED.2` | `UscoreEmailAlert_Reserved2` |  |  |  |
| 6 | `EMAIL.RESERVED.12` | `UscoreEmailAlert_Reserved12` | TField |  |  |
| 7 | `EMAIL.RESERVED.11` | `UscoreEmailAlert_Reserved11` | TField |  |  |
| 8 | `EMAIL.RESERVED.10` | `UscoreEmailAlert_Reserved10` | TField |  |  |
| 9 | `EMAIL.RESERVED.9` | `UscoreEmailAlert_Reserved9` | TField |  |  |
| 10 | `EMAIL.RESERVED.8` | `UscoreEmailAlert_Reserved8` | TField |  |  |
| 11 | `EMAIL.RESERVED.7` | `UscoreEmailAlert_Reserved7` | TField |  |  |
| 12 | `EMAIL.RESERVED.6` | `UscoreEmailAlert_Reserved6` | TField |  |  |
| 13 | `EMAIL.RESERVED.5` | `UscoreEmailAlert_Reserved5` | TField |  |  |
| 14 | `EMAIL.RESERVED.4` | `UscoreEmailAlert_Reserved4` | TField |  |  |
| 15 | `EMAIL.RESERVED.3` | `UscoreEmailAlert_Reserved3` | TField |  |  |
| 16 | `EMAIL.RECORD.STATUS` | `UscoreEmailAlert_RecordStatus` | String |  |  |
| 17 | `EMAIL.CURR.NO` | `UscoreEmailAlert_CurrNo` | String |  |  |
| 18 | `EMAIL.INPUTTER` | `UscoreEmailAlert_Inputter` |  |  |  |
| 19 | `EMAIL.DATE.TIME` | `UscoreEmailAlert_DateTime` |  |  |  |
| 20 | `EMAIL.AUTHORISER` | `UscoreEmailAlert_Authoriser` | String |  |  |
| 21 | `EMAIL.CO.CODE` | `UscoreEmailAlert_CoCode` | String |  |  |
| 22 | `EMAIL.DEPT.CODE` | `UscoreEmailAlert_DeptCode` | String |  |  |
| 23 | `EMAIL.AUDITOR.CODE` | `UscoreEmailAlert_AuditorCode` | String |  |  |
| 24 | `EMAIL.AUDIT.DATE.TIME` | `UscoreEmailAlert_AuditDateTime` | String |  |  |
