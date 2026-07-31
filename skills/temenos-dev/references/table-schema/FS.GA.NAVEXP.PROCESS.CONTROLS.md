# FS.GA.NAVEXP.PROCESS.CONTROLS — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAVEXP.PROCESS.CONTROLS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAVEXP.PROCESS.CONTROLS.PARENT.REF.ID` | `FsGaNavexpProcessControls_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAVEXP.PROCESS.CONTROLS.ORA.ROWID` | `FsGaNavexpProcessControls_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAVEXP.PROCESS.CONTROLS.PROCESS.ID` | `FsGaNavexpProcessControls_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 4 | `FS.GA.NAVEXP.PROCESS.CONTROLS.CONTROL.NUMBER` | `FsGaNavexpProcessControls_ControlNumber` | TField |  | Control Number linked to Process Multifonds DB Column is TYP_CONTROLE. |
| 5 | `FS.GA.NAVEXP.PROCESS.CONTROLS.SEQUENCE.NO` | `FsGaNavexpProcessControls_SequenceNo` | TField |  | Sequence Number of the control Multifonds DB Column is NREGLE. |
| 6 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED10` | `FsGaNavexpProcessControls_Reserved10` | TField |  |  |
| 7 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED9` | `FsGaNavexpProcessControls_Reserved9` | TField |  |  |
| 8 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED8` | `FsGaNavexpProcessControls_Reserved8` | TField |  |  |
| 9 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED7` | `FsGaNavexpProcessControls_Reserved7` | TField |  |  |
| 10 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED6` | `FsGaNavexpProcessControls_Reserved6` | TField |  |  |
| 11 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED5` | `FsGaNavexpProcessControls_Reserved5` | TField |  |  |
| 12 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED4` | `FsGaNavexpProcessControls_Reserved4` | TField |  |  |
| 13 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED3` | `FsGaNavexpProcessControls_Reserved3` | TField |  |  |
| 14 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED2` | `FsGaNavexpProcessControls_Reserved2` | TField |  |  |
| 15 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RESERVED1` | `FsGaNavexpProcessControls_Reserved1` | TField |  |  |
| 16 | `FS.GA.NAVEXP.PROCESS.CONTROLS.LOCAL.REF` | `FsGaNavexpProcessControls_LocalRef` |  |  |  |
| 17 | `FS.GA.NAVEXP.PROCESS.CONTROLS.OVERRIDE` | `FsGaNavexpProcessControls_Override` |  |  |  |
| 18 | `FS.GA.NAVEXP.PROCESS.CONTROLS.RECORD.STATUS` | `FsGaNavexpProcessControls_RecordStatus` | String |  |  |
| 19 | `FS.GA.NAVEXP.PROCESS.CONTROLS.CURR.NO` | `FsGaNavexpProcessControls_CurrNo` | String |  |  |
| 20 | `FS.GA.NAVEXP.PROCESS.CONTROLS.INPUTTER` | `FsGaNavexpProcessControls_Inputter` |  |  |  |
| 21 | `FS.GA.NAVEXP.PROCESS.CONTROLS.DATE.TIME` | `FsGaNavexpProcessControls_DateTime` |  |  |  |
| 22 | `FS.GA.NAVEXP.PROCESS.CONTROLS.AUTHORISER` | `FsGaNavexpProcessControls_Authoriser` | String |  |  |
| 23 | `FS.GA.NAVEXP.PROCESS.CONTROLS.CO.CODE` | `FsGaNavexpProcessControls_CoCode` | String |  |  |
| 24 | `FS.GA.NAVEXP.PROCESS.CONTROLS.DEPT.CODE` | `FsGaNavexpProcessControls_DeptCode` | String |  |  |
| 25 | `FS.GA.NAVEXP.PROCESS.CONTROLS.AUDITOR.CODE` | `FsGaNavexpProcessControls_AuditorCode` | String |  |  |
| 26 | `FS.GA.NAVEXP.PROCESS.CONTROLS.AUDIT.DATE.TIME` | `FsGaNavexpProcessControls_AuditDateTime` | String |  |  |
