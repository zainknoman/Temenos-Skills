# FS.GA.NAV.PROCESS.LOG — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.PROCESS.LOG` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.PROCESS.LOG.PARENT.REF.ID` | `FsGaNavProcessLog_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.PROCESS.LOG.ORA.ROWID` | `FsGaNavProcessLog_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.PROCESS.LOG.SEQUENCE.NUMBER` | `FsGaNavProcessLog_SequenceNumber` | TField |  | Sequence Number Multifonds DB Column is SEQ_NO. |
| 4 | `FS.GA.NAV.PROCESS.LOG.PROCESS.ID` | `FsGaNavProcessLog_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 5 | `FS.GA.NAV.PROCESS.LOG.LOAD.LOG` | `FsGaNavProcessLog_LoadLog` | TField |  | Load log flag Multifonds DB Column is LOAD_LOG. |
| 6 | `FS.GA.NAV.PROCESS.LOG.LOG.PRICING.RESCHEDULE.TIME` | `FsGaNavProcessLog_LogPricingRescheduleTime` | TField |  | Time interval (in minutes) after which the failed process will be rescheduled Multifonds DB Column is PRICE_TIME. |
| 7 | `FS.GA.NAV.PROCESS.LOG.LOG.PRICING.RESCHEDULE.NUMBER` | `FsGaNavProcessLog_LogPricingRescheduleNumber` | TField |  | Maximum number of times the failed process could be rescheduled for the day Multifonds DB Column is NB_PRICE. |
| 8 | `FS.GA.NAV.PROCESS.LOG.NUMBER.TRIALS` | `FsGaNavProcessLog_NumberTrials` | TField |  | The number of iterations finished. The value will be automatically reset to 0 when the process is rescheduled for the next day. Also have the option of resetting the value in case of any interruption. Multifonds DB Column is NB_TRIAL. |
| 9 | `FS.GA.NAV.PROCESS.LOG.RESERVED10` | `FsGaNavProcessLog_Reserved10` | TField |  |  |
| 10 | `FS.GA.NAV.PROCESS.LOG.RESERVED9` | `FsGaNavProcessLog_Reserved9` | TField |  |  |
| 11 | `FS.GA.NAV.PROCESS.LOG.RESERVED8` | `FsGaNavProcessLog_Reserved8` | TField |  |  |
| 12 | `FS.GA.NAV.PROCESS.LOG.RESERVED7` | `FsGaNavProcessLog_Reserved7` | TField |  |  |
| 13 | `FS.GA.NAV.PROCESS.LOG.RESERVED6` | `FsGaNavProcessLog_Reserved6` | TField |  |  |
| 14 | `FS.GA.NAV.PROCESS.LOG.RESERVED5` | `FsGaNavProcessLog_Reserved5` | TField |  |  |
| 15 | `FS.GA.NAV.PROCESS.LOG.RESERVED4` | `FsGaNavProcessLog_Reserved4` | TField |  |  |
| 16 | `FS.GA.NAV.PROCESS.LOG.RESERVED3` | `FsGaNavProcessLog_Reserved3` | TField |  |  |
| 17 | `FS.GA.NAV.PROCESS.LOG.RESERVED2` | `FsGaNavProcessLog_Reserved2` | TField |  |  |
| 18 | `FS.GA.NAV.PROCESS.LOG.RESERVED1` | `FsGaNavProcessLog_Reserved1` | TField |  |  |
| 19 | `FS.GA.NAV.PROCESS.LOG.LOCAL.REF` | `FsGaNavProcessLog_LocalRef` |  |  |  |
| 20 | `FS.GA.NAV.PROCESS.LOG.OVERRIDE` | `FsGaNavProcessLog_Override` |  |  |  |
| 21 | `FS.GA.NAV.PROCESS.LOG.RECORD.STATUS` | `FsGaNavProcessLog_RecordStatus` | String |  |  |
| 22 | `FS.GA.NAV.PROCESS.LOG.CURR.NO` | `FsGaNavProcessLog_CurrNo` | String |  |  |
| 23 | `FS.GA.NAV.PROCESS.LOG.INPUTTER` | `FsGaNavProcessLog_Inputter` |  |  |  |
| 24 | `FS.GA.NAV.PROCESS.LOG.DATE.TIME` | `FsGaNavProcessLog_DateTime` |  |  |  |
| 25 | `FS.GA.NAV.PROCESS.LOG.AUTHORISER` | `FsGaNavProcessLog_Authoriser` | String |  |  |
| 26 | `FS.GA.NAV.PROCESS.LOG.CO.CODE` | `FsGaNavProcessLog_CoCode` | String |  |  |
| 27 | `FS.GA.NAV.PROCESS.LOG.DEPT.CODE` | `FsGaNavProcessLog_DeptCode` | String |  |  |
| 28 | `FS.GA.NAV.PROCESS.LOG.AUDITOR.CODE` | `FsGaNavProcessLog_AuditorCode` | String |  |  |
| 29 | `FS.GA.NAV.PROCESS.LOG.AUDIT.DATE.TIME` | `FsGaNavProcessLog_AuditDateTime` | String |  |  |
