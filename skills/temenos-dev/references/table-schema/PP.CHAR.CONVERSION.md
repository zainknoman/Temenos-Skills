# PP.CHAR.CONVERSION — Table Schema

> Source: `INSERTS/I_F.PP.CHAR.CONVERSION` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCHC.Source` | `PpCharConversion_Source` |  |  |  |
| 2 | `PPCHC.Target` | `PpCharConversion_Target` |  |  |  |
| 3 | `PPCHC.RESERVED.5` | `PpCharConversion_Reserved5` | TField |  |  |
| 4 | `PPCHC.RESERVED.4` | `PpCharConversion_Reserved4` | TField |  |  |
| 5 | `PPCHC.RESERVED.3` | `PpCharConversion_Reserved3` | TField |  |  |
| 6 | `PPCHC.RESERVED.2` | `PpCharConversion_Reserved2` | TField |  |  |
| 7 | `PPCHC.RESERVED.1` | `PpCharConversion_Reserved1` | TField |  |  |
| 8 | `PPCHC.LOCAL.REF` | `PpCharConversion_LocalRef` |  |  |  |
| 9 | `PPCHC.OVERRIDE` | `PpCharConversion_Override` |  |  |  |
| 10 | `PPCHC.RECORD.STATUS` | `PpCharConversion_RecordStatus` | String |  |  |
| 11 | `PPCHC.CURR.NO` | `PpCharConversion_CurrNo` | String |  |  |
| 12 | `PPCHC.INPUTTER` | `PpCharConversion_Inputter` |  |  |  |
| 13 | `PPCHC.DATE.TIME` | `PpCharConversion_DateTime` |  |  |  |
| 14 | `PPCHC.AUTHORISER` | `PpCharConversion_Authoriser` | String |  |  |
| 15 | `PPCHC.CO.CODE` | `PpCharConversion_CoCode` | String |  |  |
| 16 | `PPCHC.DEPT.CODE` | `PpCharConversion_DeptCode` | String |  |  |
| 17 | `PPCHC.AUDITOR.CODE` | `PpCharConversion_AuditorCode` | String |  |  |
| 18 | `PPCHC.AUDIT.DATE.TIME` | `PpCharConversion_AuditDateTime` | String |  |  |
