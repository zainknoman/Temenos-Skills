# CP.PROGRAM — Table Schema

> Source: `INSERTS/I_F.CP.PROGRAM` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.PRG.PROGRAM.NAME` | `CpProgram_ProgramName` | TField | Yes | The name of the campaign program. Validation Rules :Mandatory field, any 250 characters. |
| 2 | `CP.PRG.PROGRAM.DESCRIPTION` | `CpProgram_ProgramDescription` |  |  |  |
| 3 | `CP.PRG.PROGRAM.OWNER` | `CpProgram_ProgramOwner` | TField | Yes | The name of the user who defined the campiagn program. This field links CP.PROGRAM table to the USER one. Validation Rules :Mandatory field, 100 text characters. |
| 4 | `CP.PRG.PROGRAM.STATUS` | `CpProgram_ProgramStatus` | TField | Yes | The status of the campaign program.This field links the CP.PROGRAM table to the CP.STATUS one. Validation Rules :Mandatory field, 100 text characters. |
| 5 | `CP.PRG.PLANNED.START.DATE` | `CpProgram_PlannedStartDate` | TField |  | The planned start date of the campaign program. |
| 6 | `CP.PRG.PLANNED.END.DATE` | `CpProgram_PlannedEndDate` | TField |  | The planned end date of the campaign program. |
| 7 | `CP.PRG.ACTUAL.START.DATE` | `CpProgram_ActualStartDate` | TField |  | The actual start date of the campaign program. |
| 8 | `CP.PRG.ACTUAL.END.DATE` | `CpProgram_ActualEndDate` | TField |  | The actual end date of the campaign program. |
| 9 | `CP.PRG.TARGET.COSTS` | `CpProgram_TargetCosts` | TField |  | The target cost of the campaign program. |
| 10 | `CP.PRG.ACTUAL.COSTS` | `CpProgram_ActualCosts` | TField |  | The actual cost of the campaign program. |
| 11 | `CP.PRG.TARGET.RSP.RATE` | `CpProgram_TargetRspRate` | TField |  | The target response rate of the campaign program. |
| 12 | `CP.PRG.ACTUAL.RSP.RATE` | `CpProgram_ActualRspRate` | TField |  | The actual response rate of the campaign program. |
| 13 | `CP.PRG.TARGET.ROI` | `CpProgram_TargetRoi` | TField |  | The planned return on investment of the campaign program. |
| 14 | `CP.PRG.ACTUAL.ROI` | `CpProgram_ActualRoi` | TField |  | The ACTUAL return on investment of the campaign program. |
| 15 | `CP.PRG.PARENT.ID` | `CpProgram_ParentId` | TField |  | The ID of the parent campaign program. |
| 16 | `CP.PRG.LAST.UPDATE` | `CpProgram_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 17 | `CP.PRG.WORKFLOW.ID` | `CpProgram_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 18 | `CP.PRG.RESERVED.8` | `CpProgram_Reserved8` | TField |  |  |
| 19 | `CP.PRG.RESERVED.7` | `CpProgram_Reserved7` | TField |  |  |
| 20 | `CP.PRG.RESERVED.6` | `CpProgram_Reserved6` | TField |  |  |
| 21 | `CP.PRG.RESERVED.5` | `CpProgram_Reserved5` | TField |  |  |
| 22 | `CP.PRG.RESERVED.4` | `CpProgram_Reserved4` | TField |  |  |
| 23 | `CP.PRG.RESERVED.3` | `CpProgram_Reserved3` | TField |  |  |
| 24 | `CP.PRG.RESERVED.2` | `CpProgram_Reserved2` | TField |  |  |
| 25 | `CP.PRG.RESERVED.1` | `CpProgram_Reserved1` | TField |  |  |
| 26 | `CP.PRG.LOCAL.REF` | `CpProgram_LocalRef` |  |  |  |
| 27 | `CP.PRG.OVERRIDE` | `CpProgram_Override` |  |  |  |
| 28 | `CP.PRG.RECORD.STATUS` | `CpProgram_RecordStatus` | String |  |  |
| 29 | `CP.PRG.CURR.NO` | `CpProgram_CurrNo` | String |  |  |
| 30 | `CP.PRG.INPUTTER` | `CpProgram_Inputter` |  |  |  |
| 31 | `CP.PRG.DATE.TIME` | `CpProgram_DateTime` |  |  |  |
| 32 | `CP.PRG.AUTHORISER` | `CpProgram_Authoriser` | String |  |  |
| 33 | `CP.PRG.CO.CODE` | `CpProgram_CoCode` | String |  |  |
| 34 | `CP.PRG.DEPT.CODE` | `CpProgram_DeptCode` | String |  |  |
| 35 | `CP.PRG.AUDITOR.CODE` | `CpProgram_AuditorCode` | String |  |  |
| 36 | `CP.PRG.AUDIT.DATE.TIME` | `CpProgram_AuditDateTime` | String |  |  |
