# FS.GA.WEM.ESCALATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.ESCALATION` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.ESCALATION.PARENT.REF.ID` | `FsGaWemEscalation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.ESCALATION.ORA.ROWID` | `FsGaWemEscalation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.ESCALATION.CONTROL.ID` | `FsGaWemEscalation_ControlId` | TField |  | Control ID Multifonds DB Column is CONTROL_ID. |
| 4 | `FS.GA.WEM.ESCALATION.OPERATOR` | `FsGaWemEscalation_Operator` | TField |  | Operator for Threshold Multifonds DB Column is OPERATOR. |
| 5 | `FS.GA.WEM.ESCALATION.THRESHOLD` | `FsGaWemEscalation_Threshold` | TField |  | Threshold Multifonds DB Column is THRESHOLD. |
| 6 | `FS.GA.WEM.ESCALATION.NAME.OF.THE.USER` | `FsGaWemEscalation_NameOfTheUser` | TField |  | Name Of The User Multifonds DB Column is USERNAME. |
| 7 | `FS.GA.WEM.ESCALATION.RESERVED10` | `FsGaWemEscalation_Reserved10` | TField |  |  |
| 8 | `FS.GA.WEM.ESCALATION.RESERVED9` | `FsGaWemEscalation_Reserved9` | TField |  |  |
| 9 | `FS.GA.WEM.ESCALATION.RESERVED8` | `FsGaWemEscalation_Reserved8` | TField |  |  |
| 10 | `FS.GA.WEM.ESCALATION.RESERVED7` | `FsGaWemEscalation_Reserved7` | TField |  |  |
| 11 | `FS.GA.WEM.ESCALATION.RESERVED6` | `FsGaWemEscalation_Reserved6` | TField |  |  |
| 12 | `FS.GA.WEM.ESCALATION.RESERVED5` | `FsGaWemEscalation_Reserved5` | TField |  |  |
| 13 | `FS.GA.WEM.ESCALATION.RESERVED4` | `FsGaWemEscalation_Reserved4` | TField |  |  |
| 14 | `FS.GA.WEM.ESCALATION.RESERVED3` | `FsGaWemEscalation_Reserved3` | TField |  |  |
| 15 | `FS.GA.WEM.ESCALATION.RESERVED2` | `FsGaWemEscalation_Reserved2` | TField |  |  |
| 16 | `FS.GA.WEM.ESCALATION.RESERVED1` | `FsGaWemEscalation_Reserved1` | TField |  |  |
| 17 | `FS.GA.WEM.ESCALATION.LOCAL.REF` | `FsGaWemEscalation_LocalRef` |  |  |  |
| 18 | `FS.GA.WEM.ESCALATION.OVERRIDE` | `FsGaWemEscalation_Override` |  |  |  |
| 19 | `FS.GA.WEM.ESCALATION.RECORD.STATUS` | `FsGaWemEscalation_RecordStatus` | String |  |  |
| 20 | `FS.GA.WEM.ESCALATION.CURR.NO` | `FsGaWemEscalation_CurrNo` | String |  |  |
| 21 | `FS.GA.WEM.ESCALATION.INPUTTER` | `FsGaWemEscalation_Inputter` |  |  |  |
| 22 | `FS.GA.WEM.ESCALATION.DATE.TIME` | `FsGaWemEscalation_DateTime` |  |  |  |
| 23 | `FS.GA.WEM.ESCALATION.AUTHORISER` | `FsGaWemEscalation_Authoriser` | String |  |  |
| 24 | `FS.GA.WEM.ESCALATION.CO.CODE` | `FsGaWemEscalation_CoCode` | String |  |  |
| 25 | `FS.GA.WEM.ESCALATION.DEPT.CODE` | `FsGaWemEscalation_DeptCode` | String |  |  |
| 26 | `FS.GA.WEM.ESCALATION.AUDITOR.CODE` | `FsGaWemEscalation_AuditorCode` | String |  |  |
| 27 | `FS.GA.WEM.ESCALATION.AUDIT.DATE.TIME` | `FsGaWemEscalation_AuditDateTime` | String |  |  |
