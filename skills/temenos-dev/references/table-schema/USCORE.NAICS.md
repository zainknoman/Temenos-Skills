# USCORE.NAICS — Table Schema

> Source: `INSERTS/I_F.USCORE.NAICS` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.DESCRIPTION` | `UscoreNaics_Description` |  |  |  |
| 2 | `USCORE.RESERVED.1` | `UscoreNaics_Reserved1` |  |  |  |
| 3 | `USCORE.RESERVED.2` | `UscoreNaics_Reserved2` |  |  |  |
| 4 | `USCORE.RESERVED.3` | `UscoreNaics_Reserved3` |  |  |  |
| 5 | `USCORE.RESERVED.4` | `UscoreNaics_Reserved4` |  |  |  |
| 6 | `USCORE.RESERVED.5` | `UscoreNaics_Reserved5` |  |  |  |
| 7 | `USCORE.RECORD.STATUS` | `UscoreNaics_RecordStatus` |  |  |  |
| 8 | `USCORE.CURR.NO` | `UscoreNaics_CurrNo` |  |  |  |
| 9 | `USCORE.INPUTTER` | `UscoreNaics_Inputter` |  |  |  |
| 10 | `USCORE.DATE.TIME` | `UscoreNaics_DateTime` |  |  |  |
| 11 | `USCORE.AUTHORISER` | `UscoreNaics_Authoriser` |  |  |  |
| 12 | `USCORE.CO.CODE` | `UscoreNaics_CoCode` |  |  |  |
| 13 | `USCORE.DEPT.CODE` | `UscoreNaics_DeptCode` |  |  |  |
| 14 | `USCORE.AUDITOR.CODE` | `UscoreNaics_AuditorCode` |  |  |  |
| 15 | `USCORE.AUDIT.DATE.TIME` | `UscoreNaics_AuditDateTime` |  |  |  |
