# BPM.CONTEXT.REF — Table Schema

> Source: `INSERTS/I_F.BPM.CONTEXT.REF` in `JP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `JP.BPM.TASK.ID` | `BpmContextRef_TaskId` | TField |  | BPM.CONTEXT.REF TASK.ID The system creates the Taskid for each activity when they are committed Validation Rules System Maintained. No-input. |
| 2 | `JP.BPM.TASK.TARGET` | `BpmContextRef_TaskTarget` | TField |  | BPM.CONTEXT.REF TASK.TARGET This field holds the T24 Application/Version/Enquiry and Function which should be presented to the USER upon the execution of the Activity i.e. the Application/version/Enquiry associated with the Activity. Validation Rules System Maintained. No-input. |
| 3 | `JP.BPM.TASK.STATUS` | `BpmContextRef_TaskStatus` | TField |  | BPM.CONTEXT.REF TASK.STATUS This field indicates the status of the activity executed Validation Rules System Maintained. No-input. |
| 4 | `JP.BPM.PROCESS.NO` | `BpmContextRef_ProcessNo` | TField |  |  |
| 5 | `JP.BPM.RESERVED.5` | `BpmContextRef_Reserved5` | TField |  |  |
| 6 | `JP.BPM.RESERVED.4` | `BpmContextRef_Reserved4` | TField |  |  |
| 7 | `JP.BPM.RESERVED.3` | `BpmContextRef_Reserved3` | TField |  |  |
| 8 | `JP.BPM.RESERVED.2` | `BpmContextRef_Reserved2` | TField |  |  |
| 9 | `JP.BPM.RESERVED.1` | `BpmContextRef_Reserved1` | TField |  |  |
