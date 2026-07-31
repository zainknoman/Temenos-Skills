# DLM.IS.CONTROL.FIELDS — Table Schema

> Source: `INSERTS/I_F.DLM.IS.CONTROL.FIELDS` in `DL_Separation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DLM.CF.PURGE.DATE.FIELD` | `DlmIsControlFields_PurgeDateField` |  |  |  |
| 2 | `DLM.CF.EXTRACT.VALUE` | `DlmIsControlFields_ExtractValue` |  |  |  |
| 3 | `DLM.CF.RESERVED.10` | `DlmIsControlFields_Reserved10` | TField |  |  |
| 4 | `DLM.CF.RESERVED.9` | `DlmIsControlFields_Reserved9` | TField |  |  |
| 5 | `DLM.CF.RESERVED.8` | `DlmIsControlFields_Reserved8` | TField |  |  |
| 6 | `DLM.CF.RESERVED.7` | `DlmIsControlFields_Reserved7` | TField |  |  |
| 7 | `DLM.CF.RESERVED.6` | `DlmIsControlFields_Reserved6` | TField |  |  |
| 8 | `DLM.CF.RESERVED.5` | `DlmIsControlFields_Reserved5` | TField |  |  |
| 9 | `DLM.CF.RESERVED.4` | `DlmIsControlFields_Reserved4` | TField |  |  |
| 10 | `DLM.CF.RESERVED.3` | `DlmIsControlFields_Reserved3` | TField |  |  |
| 11 | `DLM.CF.RESERVED.2` | `DlmIsControlFields_Reserved2` | TField |  |  |
| 12 | `DLM.CF.RESERVED.1` | `DlmIsControlFields_Reserved1` | TField |  |  |
| 13 | `DLM.CF.OVERRIDE` | `DlmIsControlFields_Override` |  |  |  |
| 14 | `DLM.CF.RECORD.STATUS` | `DlmIsControlFields_RecordStatus` | String |  |  |
| 15 | `DLM.CF.CURR.NO` | `DlmIsControlFields_CurrNo` | String |  |  |
| 16 | `DLM.CF.INPUTTER` | `DlmIsControlFields_Inputter` |  |  |  |
| 17 | `DLM.CF.DATE.TIME` | `DlmIsControlFields_DateTime` |  |  |  |
| 18 | `DLM.CF.AUTHORISER` | `DlmIsControlFields_Authoriser` | String |  |  |
| 19 | `DLM.CF.CO.CODE` | `DlmIsControlFields_CoCode` | String |  |  |
| 20 | `DLM.CF.DEPT.CODE` | `DlmIsControlFields_DeptCode` | String |  |  |
| 21 | `DLM.CF.AUDITOR.CODE` | `DlmIsControlFields_AuditorCode` | String |  |  |
| 22 | `DLM.CF.AUDIT.DATE.TIME` | `DlmIsControlFields_AuditDateTime` | String |  |  |
