# PSD.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PSD.PARAMETER` in `PX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PSD.PAR.COMPANY` | `PsdParameter_Company` | TField |  |  |
| 2 | `PSD.PAR.MODULE` | `PsdParameter_Module` |  |  |  |
| 3 | `PSD.PAR.AREA` | `PsdParameter_Area` | TField |  |  |
| 4 | `PSD.PAR.SUBAREA` | `PsdParameter_Subarea` | TField |  |  |
| 5 | `PSD.PAR.DESCRIPTION` | `PsdParameter_Description` |  |  |  |
| 6 | `PSD.PAR.VALUE` | `PsdParameter_Value` |  |  |  |
| 7 | `PSD.PAR.RESERVED10` | `PsdParameter_Reserved10` | TField |  |  |
| 8 | `PSD.PAR.RESERVED09` | `PsdParameter_Reserved09` | TField |  |  |
| 9 | `PSD.PAR.RESERVED08` | `PsdParameter_Reserved08` | TField |  |  |
| 10 | `PSD.PAR.RESERVED07` | `PsdParameter_Reserved07` | TField |  |  |
| 11 | `PSD.PAR.RESERVED06` | `PsdParameter_Reserved06` | TField |  |  |
| 12 | `PSD.PAR.RESERVED05` | `PsdParameter_Reserved05` | TField |  |  |
| 13 | `PSD.PAR.RESERVED04` | `PsdParameter_Reserved04` | TField |  |  |
| 14 | `PSD.PAR.RESERVED03` | `PsdParameter_Reserved03` | TField |  |  |
| 15 | `PSD.PAR.RESERVED02` | `PsdParameter_Reserved02` | TField |  |  |
| 16 | `PSD.PAR.RESERVED01` | `PsdParameter_Reserved01` | TField |  |  |
| 17 | `PSD.PAR.LOCAL.REF` | `PsdParameter_LocalRef` |  |  |  |
| 18 | `PSD.PAR.OVERRIDE` | `PsdParameter_Override` |  |  |  |
| 19 | `PSD.PAR.RECORD.STATUS` | `PsdParameter_RecordStatus` | String |  |  |
| 20 | `PSD.PAR.CURR.NO` | `PsdParameter_CurrNo` | String |  |  |
| 21 | `PSD.PAR.INPUTTER` | `PsdParameter_Inputter` |  |  |  |
| 22 | `PSD.PAR.DATE.TIME` | `PsdParameter_DateTime` |  |  |  |
| 23 | `PSD.PAR.AUTHORISER` | `PsdParameter_Authoriser` | String |  |  |
| 24 | `PSD.PAR.CO.CODE` | `PsdParameter_CoCode` | String |  |  |
| 25 | `PSD.PAR.DEPT.CODE` | `PsdParameter_DeptCode` | String |  |  |
| 26 | `PSD.PAR.AUDITOR.CODE` | `PsdParameter_AuditorCode` | String |  |  |
| 27 | `PSD.PAR.AUDIT.DATE.TIME` | `PsdParameter_AuditDateTime` | String |  |  |
