# FS.GA.JOB.SUBMIT — Table Schema

> Source: `INSERTS/I_F.FS.GA.JOB.SUBMIT` in `FS_Processing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.JOB.SUBMIT.PARENT.REF.ID` | `FsGaJobSubmit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.JOB.SUBMIT.ORA.ROWID` | `FsGaJobSubmit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.JOB.SUBMIT.JOB.NAME` | `FsGaJobSubmit_JobName` | TField |  | Assign job name to execute the specific task or Job Multifonds DB Column is JOB. |
| 4 | `FS.GA.JOB.SUBMIT.NAV.GROUP.CODE` | `FsGaJobSubmit_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 5 | `FS.GA.JOB.SUBMIT.PROCESS.ID` | `FsGaJobSubmit_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 6 | `FS.GA.JOB.SUBMIT.RESERVED10` | `FsGaJobSubmit_Reserved10` | TField |  |  |
| 7 | `FS.GA.JOB.SUBMIT.RESERVED9` | `FsGaJobSubmit_Reserved9` | TField |  |  |
| 8 | `FS.GA.JOB.SUBMIT.RESERVED8` | `FsGaJobSubmit_Reserved8` | TField |  |  |
| 9 | `FS.GA.JOB.SUBMIT.RESERVED7` | `FsGaJobSubmit_Reserved7` | TField |  |  |
| 10 | `FS.GA.JOB.SUBMIT.RESERVED6` | `FsGaJobSubmit_Reserved6` | TField |  |  |
| 11 | `FS.GA.JOB.SUBMIT.RESERVED5` | `FsGaJobSubmit_Reserved5` | TField |  |  |
| 12 | `FS.GA.JOB.SUBMIT.RESERVED4` | `FsGaJobSubmit_Reserved4` | TField |  |  |
| 13 | `FS.GA.JOB.SUBMIT.RESERVED3` | `FsGaJobSubmit_Reserved3` | TField |  |  |
| 14 | `FS.GA.JOB.SUBMIT.RESERVED2` | `FsGaJobSubmit_Reserved2` | TField |  |  |
| 15 | `FS.GA.JOB.SUBMIT.RESERVED1` | `FsGaJobSubmit_Reserved1` | TField |  |  |
| 16 | `FS.GA.JOB.SUBMIT.LOCAL.REF` | `FsGaJobSubmit_LocalRef` |  |  |  |
| 17 | `FS.GA.JOB.SUBMIT.OVERRIDE` | `FsGaJobSubmit_Override` |  |  |  |
| 18 | `FS.GA.JOB.SUBMIT.RECORD.STATUS` | `FsGaJobSubmit_RecordStatus` | String |  |  |
| 19 | `FS.GA.JOB.SUBMIT.CURR.NO` | `FsGaJobSubmit_CurrNo` | String |  |  |
| 20 | `FS.GA.JOB.SUBMIT.INPUTTER` | `FsGaJobSubmit_Inputter` |  |  |  |
| 21 | `FS.GA.JOB.SUBMIT.DATE.TIME` | `FsGaJobSubmit_DateTime` |  |  |  |
| 22 | `FS.GA.JOB.SUBMIT.AUTHORISER` | `FsGaJobSubmit_Authoriser` | String |  |  |
| 23 | `FS.GA.JOB.SUBMIT.CO.CODE` | `FsGaJobSubmit_CoCode` | String |  |  |
| 24 | `FS.GA.JOB.SUBMIT.DEPT.CODE` | `FsGaJobSubmit_DeptCode` | String |  |  |
| 25 | `FS.GA.JOB.SUBMIT.AUDITOR.CODE` | `FsGaJobSubmit_AuditorCode` | String |  |  |
| 26 | `FS.GA.JOB.SUBMIT.AUDIT.DATE.TIME` | `FsGaJobSubmit_AuditDateTime` | String |  |  |
