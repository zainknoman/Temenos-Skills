# DW.EXTRACT.PARAM — Table Schema

> Source: `INSERTS/I_F.DW.EXTRACT.PARAM` in `DW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.EXP.PAR.DESCRIPTION` | `DwExtractParam_Description` |  |  |  |
| 2 | `DW.EXP.PAR.RULES.ROUTINE` | `DwExtractParam_RulesRoutine` | TField |  | This is the routine which holds rules engine and checks for any condition and gets back with a flag saying whether we are interested in that particular record update or not. Validation Rules 1.The routine should have an entry defined in EB.API2. Input not allowed if the ID is �SYSTEM� |
| 3 | `DW.EXP.PAR.ENABLE` | `DwExtractParam_Enable` | TField |  | This Field enables the ETL Extraction Process.To trigger the Extraction Process,DW.EXTRACT.PARAM should contain a record � SYSTEM in which the field ENABLE should be set to YES. Validation Rules :1. Can be YES,NO or NULL2. Input allowed if Key is SYSTEM |
| 4 | `DW.EXP.PAR.BATCH.UPDATE` | `DwExtractParam_BatchUpdate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `DW.EXP.PAR.RESERVED.9` | `DwExtractParam_Reserved9` | TField |  |  |
| 6 | `DW.EXP.PAR.RESERVED.8` | `DwExtractParam_Reserved8` | TField |  |  |
| 7 | `DW.EXP.PAR.RESERVED.7` | `DwExtractParam_Reserved7` | TField |  |  |
| 8 | `DW.EXP.PAR.RESERVED.6` | `DwExtractParam_Reserved6` | TField |  |  |
| 9 | `DW.EXP.PAR.RESERVED.5` | `DwExtractParam_Reserved5` | TField |  |  |
| 10 | `DW.EXP.PAR.RESERVED.4` | `DwExtractParam_Reserved4` | TField |  |  |
| 11 | `DW.EXP.PAR.RESERVED.3` | `DwExtractParam_Reserved3` | TField |  |  |
| 12 | `DW.EXP.PAR.RESERVED.2` | `DwExtractParam_Reserved2` | TField |  |  |
| 13 | `DW.EXP.PAR.RESERVED.1` | `DwExtractParam_Reserved1` | TField |  |  |
| 14 | `DW.EXP.PAR.LOCAL.REF` | `DwExtractParam_LocalRef` |  |  |  |
| 15 | `DW.EXP.PAR.RECORD.STATUS` | `DwExtractParam_RecordStatus` | String |  |  |
| 16 | `DW.EXP.PAR.CURR.NO` | `DwExtractParam_CurrNo` | String |  |  |
| 17 | `DW.EXP.PAR.INPUTTER` | `DwExtractParam_Inputter` |  |  |  |
| 18 | `DW.EXP.PAR.DATE.TIME` | `DwExtractParam_DateTime` |  |  |  |
| 19 | `DW.EXP.PAR.AUTHORISER` | `DwExtractParam_Authoriser` | String |  |  |
| 20 | `DW.EXP.PAR.CO.CODE` | `DwExtractParam_CoCode` | String |  |  |
| 21 | `DW.EXP.PAR.DEPT.CODE` | `DwExtractParam_DeptCode` | String |  |  |
| 22 | `DW.EXP.PAR.AUDITOR.CODE` | `DwExtractParam_AuditorCode` | String |  |  |
| 23 | `DW.EXP.PAR.AUDIT.DATE.TIME` | `DwExtractParam_AuditDateTime` | String |  |  |
