# GLINFO.EXTRACT — Table Schema

> Source: `INSERTS/I_F.GLINFO.EXTRACT` in `EI_SupportUtilities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GLINFO.TOOL.APPLICATION` | `GlInfoExtract_Application` |  |  |  |
| 2 | `GLINFO.TOOL.SELECTION.FIELD` | `GlinfoExtract_SelectionField` |  |  |  |
| 3 | `GLINFO.TOOL.DATE` | `GlinfoExtract_Date` |  |  |  |
| 4 | `GLINFO.TOOL.DATA` | `GlinfoExtract_Data` |  |  |  |
| 5 | `GLINFO.TOOL.HOLD.IDS` | `GlinfoExtract_HoldIds` |  |  |  |
| 6 | `GLINFO.TOOL.EXECUTION.STATUS` | `GlInfoExtract_ExecutionStatus` |  |  |  |
| 7 | `GLINFO.TOOL.RESERVED.10` | `GlInfoExtract_Reserved10` |  |  |  |
| 8 | `GLINFO.TOOL.RESERVED.09` | `GlInfoExtract_Reserved09` |  |  |  |
| 9 | `GLINFO.TOOL.RESERVED.08` | `GlInfoExtract_Reserved08` |  |  |  |
| 10 | `GLINFO.TOOL.RESERVED.07` | `GlInfoExtract_Reserved07` |  |  |  |
| 11 | `GLINFO.TOOL.RESERVED.06` | `GlInfoExtract_Reserved06` |  |  |  |
| 12 | `GLINFO.TOOL.RESERVED.05` | `GlInfoExtract_Reserved05` |  |  |  |
| 13 | `GLINFO.TOOL.RESERVED.04` | `GlInfoExtract_Reserved04` |  |  |  |
| 14 | `GLINFO.TOOL.RESERVED.03` | `GlInfoExtract_Reserved03` |  |  |  |
| 15 | `GLINFO.TOOL.RESERVED.02` | `GlInfoExtract_Reserved02` |  |  |  |
| 16 | `GLINFO.TOOL.RESERVED.01` | `GlInfoExtract_Reserved01` |  |  |  |
| 17 | `GLINFO.TOOL.RECORD.STATUS` | `GlInfoExtract_RecordStatus` |  |  |  |
| 18 | `GLINFO.TOOL.CURR.NO` | `GlInfoExtract_CurrNo` |  |  |  |
| 19 | `GLINFO.TOOL.INPUTTER` | `GlInfoExtract_Inputter` |  |  |  |
| 20 | `GLINFO.TOOL.DATE.TIME` | `GlInfoExtract_DateTime` |  |  |  |
| 21 | `GLINFO.TOOL.AUTHORISER` | `GlInfoExtract_Authoriser` |  |  |  |
| 22 | `GLINFO.TOOL.CO.CODE` | `GlInfoExtract_CoCode` |  |  |  |
| 23 | `GLINFO.TOOL.DEPT.CODE` | `GlInfoExtract_DeptCode` |  |  |  |
| 24 | `GLINFO.TOOL.AUDITOR.CODE` | `GlInfoExtract_AuditorCode` |  |  |  |
| 25 | `GLINFO.TOOL.AUDIT.DATE.TIME` | `GlInfoExtract_AuditDateTime` |  |  |  |
