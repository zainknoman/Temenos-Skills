# FS.GA.AUTO.PROCESS.LOG.INFO — Table Schema

> Source: `INSERTS/I_F.FS.GA.AUTO.PROCESS.LOG.INFO` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUTO.PROCESS.LOG.FUND.ID` | `FsGaAutoProcessLog_Fund` |  |  |  |
| 2 | `AUTO.PROCESS.LOG.PROCESS.DATE` | `FsGaAutoProcessLog_ProcessDate` | TField |  | Processing Date Multifonds DB Column is PROCESS_DATE. |
| 3 | `AUTO.PROCESS.LOG.SERVICE.CODE` | `FsGaAutoProcessLog_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 4 | `AUTO.PROCESS.LOG.MESSAGE` | `FsGaAutoProcessLog_Message` | TField |  | Message Multifonds DB Column is MESSAGE. |
| 5 | `AUTO.PROCESS.LOG.SESSION.NUMBER` | `FsGaAutoProcessLog_SessionNumber` | TField |  | Session Number Multifonds DB Column is NO_SESSION. |
| 6 | `AUTO.PROCESS.LOG.LOAD.NUMBER` | `FsGaAutoProcessLog_LoadNumber` | TField |  | Load Number Multifonds DB Column is NO_LOAD. |
| 7 | `AUTO.PROCESS.LOG.PROCESS.TYPE` | `FsGaAutoProcessLog_ProcessType` | TField |  | Process Type Multifonds DB Column is PROCESS_TYPE. |
| 8 | `AUTO.PROCESS.LOG.RESERVED10` | `FsGaAutoProcessLog_Reserved10` | TField |  |  |
| 9 | `AUTO.PROCESS.LOG.RESERVED9` | `FsGaAutoProcessLog_Reserved9` | TField |  |  |
| 10 | `AUTO.PROCESS.LOG.RESERVED8` | `FsGaAutoProcessLog_Reserved8` | TField |  |  |
| 11 | `AUTO.PROCESS.LOG.RESERVED7` | `FsGaAutoProcessLog_Reserved7` | TField |  |  |
| 12 | `AUTO.PROCESS.LOG.RESERVED6` | `FsGaAutoProcessLog_Reserved6` | TField |  |  |
| 13 | `AUTO.PROCESS.LOG.RESERVED5` | `FsGaAutoProcessLog_Reserved5` | TField |  |  |
| 14 | `AUTO.PROCESS.LOG.RESERVED4` | `FsGaAutoProcessLog_Reserved4` | TField |  |  |
| 15 | `AUTO.PROCESS.LOG.RESERVED3` | `FsGaAutoProcessLog_Reserved3` | TField |  |  |
| 16 | `AUTO.PROCESS.LOG.RESERVED2` | `FsGaAutoProcessLog_Reserved2` | TField |  |  |
| 17 | `AUTO.PROCESS.LOG.RESERVED1` | `FsGaAutoProcessLog_Reserved1` | TField |  |  |
| 18 | `AUTO.PROCESS.LOG.RECORD.STATUS` | `FsGaAutoProcessLog_RecordStatus` | String |  |  |
| 19 | `AUTO.PROCESS.LOG.CURR.NO` | `FsGaAutoProcessLog_CurrNo` | String |  |  |
| 20 | `AUTO.PROCESS.LOG.INPUTTER` | `FsGaAutoProcessLog_Inputter` |  |  |  |
| 21 | `AUTO.PROCESS.LOG.DATE.TIME` | `FsGaAutoProcessLog_DateTime` |  |  |  |
| 22 | `AUTO.PROCESS.LOG.AUTHORISER` | `FsGaAutoProcessLog_Authoriser` | String |  |  |
| 23 | `AUTO.PROCESS.LOG.CO.CODE` | `FsGaAutoProcessLog_CoCode` | String |  |  |
| 24 | `AUTO.PROCESS.LOG.DEPT.CODE` | `FsGaAutoProcessLog_DeptCode` | String |  |  |
| 25 | `AUTO.PROCESS.LOG.AUDITOR.CODE` | `FsGaAutoProcessLog_AuditorCode` | String |  |  |
| 26 | `AUTO.PROCESS.LOG.AUDIT.DATE.TIME` | `FsGaAutoProcessLog_AuditDateTime` | String |  |  |
