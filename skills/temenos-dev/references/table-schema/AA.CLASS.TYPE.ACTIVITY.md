# AA.CLASS.TYPE.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.AA.CLASS.TYPE.ACTIVITY` in `AF_ClassFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CTACT.DESCRIPTION` | `AaClassTypeActivity_Description` |  |  |  |
| 2 | `AA.CTACT.FULL.DESC` | `AaClassTypeActivity_FullDesc` |  |  |  |
| 3 | `AA.CTACT.LINKED.ACTIVITY` | `AaClassTypeActivity_LinkedActivity` | TField |  |  |
| 4 | `AA.CTACT.ACTIVITY.CLASS` | `AaClassTypeActivity_ActivityClass` | TField |  |  |
| 5 | `AA.CTACT.RESERVED.1` | `AaClassTypeActivity_Reserved1` | TField |  |  |
| 6 | `AA.CTACT.RESERVED.2` | `AaClassTypeActivity_Reserved2` | TField |  |  |
| 7 | `AA.CTACT.SYSTEM.ACTIVITY` | `AaClassTypeActivity_SystemActivity` | TField |  |  |
| 8 | `AA.CTACT.ACTIVITY.TYPE` | `AaClassTypeActivity_ActivityType` | TField |  |  |
| 9 | `AA.CTACT.PROCESS.ID` | `AaClassTypeActivity_ProcessId` | TField |  |  |
| 10 | `AA.CTACT.ENTITY` | `AaClassTypeActivity_Entity` | TField |  |  |
| 11 | `AA.CTACT.RECORD.STATUS` | `AaClassTypeActivity_RecordStatus` | String |  |  |
| 12 | `AA.CTACT.CURR.NO` | `AaClassTypeActivity_CurrNo` | String |  |  |
| 13 | `AA.CTACT.INPUTTER` | `AaClassTypeActivity_Inputter` |  |  |  |
| 14 | `AA.CTACT.DATE.TIME` | `AaClassTypeActivity_DateTime` |  |  |  |
| 15 | `AA.CTACT.AUTHORISER` | `AaClassTypeActivity_Authoriser` | String |  |  |
| 16 | `AA.CTACT.CO.CODE` | `AaClassTypeActivity_CoCode` | String |  |  |
| 17 | `AA.CTACT.DEPT.CODE` | `AaClassTypeActivity_DeptCode` | String |  |  |
| 18 | `AA.CTACT.AUDITOR.CODE` | `AaClassTypeActivity_AuditorCode` | String |  |  |
| 19 | `AA.CTACT.AUDIT.DATE.TIME` | `AaClassTypeActivity_AuditDateTime` | String |  |  |
