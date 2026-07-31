# FS.GI.WEM.STEP.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.STEP.DEFINITION` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.STEP.DEFINITION.STEP.ID` | `FsGiWemStepDefinition_StepId` | TField |  | Unique step ID Multifonds DB Column is STEP.ID. |
| 2 | `FS.GI.WEM.STEP.DEFINITION.STEP.NAME` | `FsGiWemStepDefinition_StepName` | TField |  | Step name Multifonds DB Column is STEP.NAME. |
| 3 | `FS.GI.WEM.STEP.DEFINITION.PROCESS.ID` | `FsGiWemStepDefinition_ProcessId` |  |  |  |
| 4 | `FS.GI.WEM.STEP.DEFINITION.PROCESS.SEQUENCE` | `FsGiWemStepDefinition_ProcessSequence` |  |  |  |
| 5 | `FS.GI.WEM.STEP.DEFINITION.CONTROL.OR.REPORT.ID` | `FsGiWemStepDefinition_ControlOrReportId` |  |  |  |
| 6 | `FS.GI.WEM.STEP.DEFINITION.RESERVED10` | `FsGiWemStepDefinition_Reserved10` | TField |  |  |
| 7 | `FS.GI.WEM.STEP.DEFINITION.RESERVED9` | `FsGiWemStepDefinition_Reserved9` | TField |  |  |
| 8 | `FS.GI.WEM.STEP.DEFINITION.RESERVED8` | `FsGiWemStepDefinition_Reserved8` | TField |  |  |
| 9 | `FS.GI.WEM.STEP.DEFINITION.RESERVED7` | `FsGiWemStepDefinition_Reserved7` | TField |  |  |
| 10 | `FS.GI.WEM.STEP.DEFINITION.RESERVED6` | `FsGiWemStepDefinition_Reserved6` | TField |  |  |
| 11 | `FS.GI.WEM.STEP.DEFINITION.RESERVED5` | `FsGiWemStepDefinition_Reserved5` | TField |  |  |
| 12 | `FS.GI.WEM.STEP.DEFINITION.RESERVED4` | `FsGiWemStepDefinition_Reserved4` | TField |  |  |
| 13 | `FS.GI.WEM.STEP.DEFINITION.RESERVED3` | `FsGiWemStepDefinition_Reserved3` | TField |  |  |
| 14 | `FS.GI.WEM.STEP.DEFINITION.RESERVED2` | `FsGiWemStepDefinition_Reserved2` | TField |  |  |
| 15 | `FS.GI.WEM.STEP.DEFINITION.RESERVED1` | `FsGiWemStepDefinition_Reserved1` | TField |  |  |
| 16 | `FS.GI.WEM.STEP.DEFINITION.LOCAL.REF` | `FsGiWemStepDefinition_LocalRef` |  |  |  |
| 17 | `FS.GI.WEM.STEP.DEFINITION.OVERRIDE` | `FsGiWemStepDefinition_Override` |  |  |  |
| 18 | `FS.GI.WEM.STEP.DEFINITION.RECORD.STATUS` | `FsGiWemStepDefinition_RecordStatus` | String |  |  |
| 19 | `FS.GI.WEM.STEP.DEFINITION.CURR.NO` | `FsGiWemStepDefinition_CurrNo` | String |  |  |
| 20 | `FS.GI.WEM.STEP.DEFINITION.INPUTTER` | `FsGiWemStepDefinition_Inputter` |  |  |  |
| 21 | `FS.GI.WEM.STEP.DEFINITION.DATE.TIME` | `FsGiWemStepDefinition_DateTime` |  |  |  |
| 22 | `FS.GI.WEM.STEP.DEFINITION.AUTHORISER` | `FsGiWemStepDefinition_Authoriser` | String |  |  |
| 23 | `FS.GI.WEM.STEP.DEFINITION.CO.CODE` | `FsGiWemStepDefinition_CoCode` | String |  |  |
| 24 | `FS.GI.WEM.STEP.DEFINITION.DEPT.CODE` | `FsGiWemStepDefinition_DeptCode` | String |  |  |
| 25 | `FS.GI.WEM.STEP.DEFINITION.AUDITOR.CODE` | `FsGiWemStepDefinition_AuditorCode` | String |  |  |
| 26 | `FS.GI.WEM.STEP.DEFINITION.AUDIT.DATE.TIME` | `FsGiWemStepDefinition_AuditDateTime` | String |  |  |
