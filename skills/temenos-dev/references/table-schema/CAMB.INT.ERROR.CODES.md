# CAMB.INT.ERROR.CODES — Table Schema

> Source: `INSERTS/I_F.CAMB.INT.ERROR.CODES` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GLRE.DESCRIPTION` | `CambIntErrorCodes_Description` |  |  |  |
| 2 | `GLRE.RESERVED.10` | `CambIntErrorCodes_Reserved10` | TField |  |  |
| 3 | `GLRE.RESERVED.9` | `CambIntErrorCodes_Reserved9` | TField |  |  |
| 4 | `GLRE.RESERVED.8` | `CambIntErrorCodes_Reserved8` | TField |  |  |
| 5 | `GLRE.RESERVED.7` | `CambIntErrorCodes_Reserved7` | TField |  |  |
| 6 | `GLRE.RESERVED.6` | `CambIntErrorCodes_Reserved6` | TField |  |  |
| 7 | `GLRE.RESERVED.5` | `CambIntErrorCodes_Reserved5` | TField |  |  |
| 8 | `GLRE.RESERVED.4` | `CambIntErrorCodes_Reserved4` | TField |  |  |
| 9 | `GLRE.RESERVED.3` | `CambIntErrorCodes_Reserved3` | TField |  |  |
| 10 | `GLRE.RESERVED.2` | `CambIntErrorCodes_Reserved2` | TField |  |  |
| 11 | `GLRE.RESERVED.1` | `CambIntErrorCodes_Reserved1` | TField |  |  |
| 12 | `GLRE.RECORD.STATUS` | `CambIntErrorCodes_RecordStatus` | String |  |  |
| 13 | `GLRE.CURR.NO` | `CambIntErrorCodes_CurrNo` | String |  |  |
| 14 | `GLRE.INPUTTER` | `CambIntErrorCodes_Inputter` |  |  |  |
| 15 | `GLRE.DATE.TIME` | `CambIntErrorCodes_DateTime` |  |  |  |
| 16 | `GLRE.AUTHORISER` | `CambIntErrorCodes_Authoriser` | String |  |  |
| 17 | `GLRE.CO.CODE` | `CambIntErrorCodes_CoCode` | String |  |  |
| 18 | `GLRE.DEPT.CODE` | `CambIntErrorCodes_DeptCode` | String |  |  |
| 19 | `GLRE.AUDITOR.CODE` | `CambIntErrorCodes_AuditorCode` | String |  |  |
| 20 | `GLRE.AUDIT.DATE.TIME` | `CambIntErrorCodes_AuditDateTime` | String |  |  |
