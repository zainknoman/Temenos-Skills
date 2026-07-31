# FS.GA.WEM.ESCALATION.ALERTS — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.ESCALATION.ALERTS` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.ESCALATION.ALERTS.PARENT.REF.ID` | `FsGaWemEscalationAlerts_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.ESCALATION.ALERTS.ORA.ROWID` | `FsGaWemEscalationAlerts_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.ESCALATION.ALERTS.CONTROL.ID` | `FsGaWemEscalationAlerts_ControlId` | TField |  | Control ID Multifonds DB Column is CONTROL_ID. |
| 4 | `FS.GA.WEM.ESCALATION.ALERTS.OPERATOR` | `FsGaWemEscalationAlerts_Operator` | TField |  | Operator for Threshold Multifonds DB Column is OPERATOR. |
| 5 | `FS.GA.WEM.ESCALATION.ALERTS.THRESHOLD` | `FsGaWemEscalationAlerts_Threshold` | TField |  | Threshold Multifonds DB Column is THRESHOLD. |
| 6 | `FS.GA.WEM.ESCALATION.ALERTS.EMAIL.ID` | `FsGaWemEscalationAlerts_EmailId` | TField |  | The mail ID of the authorised user to which a notification mail to be sent Multifonds DB Column is EMAIL_ID. |
| 7 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED10` | `FsGaWemEscalationAlerts_Reserved10` | TField |  |  |
| 8 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED9` | `FsGaWemEscalationAlerts_Reserved9` | TField |  |  |
| 9 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED8` | `FsGaWemEscalationAlerts_Reserved8` | TField |  |  |
| 10 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED7` | `FsGaWemEscalationAlerts_Reserved7` | TField |  |  |
| 11 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED6` | `FsGaWemEscalationAlerts_Reserved6` | TField |  |  |
| 12 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED5` | `FsGaWemEscalationAlerts_Reserved5` | TField |  |  |
| 13 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED4` | `FsGaWemEscalationAlerts_Reserved4` | TField |  |  |
| 14 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED3` | `FsGaWemEscalationAlerts_Reserved3` | TField |  |  |
| 15 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED2` | `FsGaWemEscalationAlerts_Reserved2` | TField |  |  |
| 16 | `FS.GA.WEM.ESCALATION.ALERTS.RESERVED1` | `FsGaWemEscalationAlerts_Reserved1` | TField |  |  |
| 17 | `FS.GA.WEM.ESCALATION.ALERTS.LOCAL.REF` | `FsGaWemEscalationAlerts_LocalRef` |  |  |  |
| 18 | `FS.GA.WEM.ESCALATION.ALERTS.OVERRIDE` | `FsGaWemEscalationAlerts_Override` |  |  |  |
| 19 | `FS.GA.WEM.ESCALATION.ALERTS.RECORD.STATUS` | `FsGaWemEscalationAlerts_RecordStatus` | String |  |  |
| 20 | `FS.GA.WEM.ESCALATION.ALERTS.CURR.NO` | `FsGaWemEscalationAlerts_CurrNo` | String |  |  |
| 21 | `FS.GA.WEM.ESCALATION.ALERTS.INPUTTER` | `FsGaWemEscalationAlerts_Inputter` |  |  |  |
| 22 | `FS.GA.WEM.ESCALATION.ALERTS.DATE.TIME` | `FsGaWemEscalationAlerts_DateTime` |  |  |  |
| 23 | `FS.GA.WEM.ESCALATION.ALERTS.AUTHORISER` | `FsGaWemEscalationAlerts_Authoriser` | String |  |  |
| 24 | `FS.GA.WEM.ESCALATION.ALERTS.CO.CODE` | `FsGaWemEscalationAlerts_CoCode` | String |  |  |
| 25 | `FS.GA.WEM.ESCALATION.ALERTS.DEPT.CODE` | `FsGaWemEscalationAlerts_DeptCode` | String |  |  |
| 26 | `FS.GA.WEM.ESCALATION.ALERTS.AUDITOR.CODE` | `FsGaWemEscalationAlerts_AuditorCode` | String |  |  |
| 27 | `FS.GA.WEM.ESCALATION.ALERTS.AUDIT.DATE.TIME` | `FsGaWemEscalationAlerts_AuditDateTime` | String |  |  |
