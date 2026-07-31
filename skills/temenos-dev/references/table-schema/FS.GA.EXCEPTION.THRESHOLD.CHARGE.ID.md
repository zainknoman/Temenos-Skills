# FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID — Table Schema

> Source: `INSERTS/I_F.FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.PARENT.REF.ID` | `FsGaExceptionThresholdChargeId_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.ORA.ROWID` | `FsGaExceptionThresholdChargeId_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.ID.CODE` | `FsGaExceptionThresholdChargeId_IdCode` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 4 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.CHARGE.CODE` | `FsGaExceptionThresholdChargeId_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 5 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.VALUE.OF.EXCEPTION.MONITOR` | `FsGaExceptionThresholdChargeId_ValueOfExceptionMonitor` | TField |  | User has to define the threshold amount or absolute figure for control in this field. This is in relation to the Type defined. Multifonds DB Column is MNT_PCT. |
| 6 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED10` | `FsGaExceptionThresholdChargeId_Reserved10` | TField |  |  |
| 7 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED9` | `FsGaExceptionThresholdChargeId_Reserved9` | TField |  |  |
| 8 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED8` | `FsGaExceptionThresholdChargeId_Reserved8` | TField |  |  |
| 9 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED7` | `FsGaExceptionThresholdChargeId_Reserved7` | TField |  |  |
| 10 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED6` | `FsGaExceptionThresholdChargeId_Reserved6` | TField |  |  |
| 11 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED5` | `FsGaExceptionThresholdChargeId_Reserved5` | TField |  |  |
| 12 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED4` | `FsGaExceptionThresholdChargeId_Reserved4` | TField |  |  |
| 13 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED3` | `FsGaExceptionThresholdChargeId_Reserved3` | TField |  |  |
| 14 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED2` | `FsGaExceptionThresholdChargeId_Reserved2` | TField |  |  |
| 15 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RESERVED1` | `FsGaExceptionThresholdChargeId_Reserved1` | TField |  |  |
| 16 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.LOCAL.REF` | `FsGaExceptionThresholdChargeId_LocalRef` |  |  |  |
| 17 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.OVERRIDE` | `FsGaExceptionThresholdChargeId_Override` |  |  |  |
| 18 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.RECORD.STATUS` | `FsGaExceptionThresholdChargeId_RecordStatus` | String |  |  |
| 19 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.CURR.NO` | `FsGaExceptionThresholdChargeId_CurrNo` | String |  |  |
| 20 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.INPUTTER` | `FsGaExceptionThresholdChargeId_Inputter` |  |  |  |
| 21 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.DATE.TIME` | `FsGaExceptionThresholdChargeId_DateTime` |  |  |  |
| 22 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.AUTHORISER` | `FsGaExceptionThresholdChargeId_Authoriser` | String |  |  |
| 23 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.CO.CODE` | `FsGaExceptionThresholdChargeId_CoCode` | String |  |  |
| 24 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.DEPT.CODE` | `FsGaExceptionThresholdChargeId_DeptCode` | String |  |  |
| 25 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.AUDITOR.CODE` | `FsGaExceptionThresholdChargeId_AuditorCode` | String |  |  |
| 26 | `FS.GA.EXCEPTION.THRESHOLD.CHARGE.ID.AUDIT.DATE.TIME` | `FsGaExceptionThresholdChargeId_AuditDateTime` | String |  |  |
