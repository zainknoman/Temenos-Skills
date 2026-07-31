# FS.GI.TXN.EOD.STATUS.REPORT — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.EOD.STATUS.REPORT` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.EOD.STATUS.REPORT.EXCHANGE.GROUP` | `FsGiTxnEodStatusReport_ExchangeGroup` | TField |  | Exchange group for which the end of day process status is being fetched. Multifonds DB Column is CGROUP_COURS. |
| 2 | `FS.GI.TXN.EOD.STATUS.REPORT.PROCESSING.DATE` | `FsGiTxnEodStatusReport_ProcessingDate` | TField |  | End of day processing date. Multifonds DB Column is DPROCESS. |
| 3 | `FS.GI.TXN.EOD.STATUS.REPORT.TASK` | `FsGiTxnEodStatusReport_Task` | TField |  | Tasks executed per specified Exchange group in the end of day process. Multifonds DB Column is TASK. |
| 4 | `FS.GI.TXN.EOD.STATUS.REPORT.MESSAGE` | `FsGiTxnEodStatusReport_Message` | TField |  | Corresponding status of the process run. Multifonds DB Column is MESSAGE. |
| 5 | `FS.GI.TXN.EOD.STATUS.REPORT.SEQUENCE.NUMBER` | `FsGiTxnEodStatusReport_SequenceNumber` | TField |  | Sequence number for internal use. Multifonds DB Column is SEQ_NO. |
| 6 | `FS.GI.TXN.EOD.STATUS.REPORT.MF.PROCESS.ID` | `FsGiTxnEodStatusReport_MfProcessId` | TField |  | MF internal process unique sequence ID. Multifonds DB Column is MF_PROC_ID. |
| 7 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED10` | `FsGiTxnEodStatusReport_Reserved10` | TField |  |  |
| 8 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED9` | `FsGiTxnEodStatusReport_Reserved9` | TField |  |  |
| 9 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED8` | `FsGiTxnEodStatusReport_Reserved8` | TField |  |  |
| 10 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED7` | `FsGiTxnEodStatusReport_Reserved7` | TField |  |  |
| 11 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED6` | `FsGiTxnEodStatusReport_Reserved6` | TField |  |  |
| 12 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED5` | `FsGiTxnEodStatusReport_Reserved5` | TField |  |  |
| 13 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED4` | `FsGiTxnEodStatusReport_Reserved4` | TField |  |  |
| 14 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED3` | `FsGiTxnEodStatusReport_Reserved3` | TField |  |  |
| 15 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED2` | `FsGiTxnEodStatusReport_Reserved2` | TField |  |  |
| 16 | `FS.GI.TXN.EOD.STATUS.REPORT.RESERVED1` | `FsGiTxnEodStatusReport_Reserved1` | TField |  |  |
| 17 | `FS.GI.TXN.EOD.STATUS.REPORT.LOCAL.REF` | `FsGiTxnEodStatusReport_LocalRef` |  |  |  |
| 18 | `FS.GI.TXN.EOD.STATUS.REPORT.OVERRIDE` | `FsGiTxnEodStatusReport_Override` |  |  |  |
| 19 | `FS.GI.TXN.EOD.STATUS.REPORT.RECORD.STATUS` | `FsGiTxnEodStatusReport_RecordStatus` | String |  |  |
| 20 | `FS.GI.TXN.EOD.STATUS.REPORT.CURR.NO` | `FsGiTxnEodStatusReport_CurrNo` | String |  |  |
| 21 | `FS.GI.TXN.EOD.STATUS.REPORT.INPUTTER` | `FsGiTxnEodStatusReport_Inputter` |  |  |  |
| 22 | `FS.GI.TXN.EOD.STATUS.REPORT.DATE.TIME` | `FsGiTxnEodStatusReport_DateTime` |  |  |  |
| 23 | `FS.GI.TXN.EOD.STATUS.REPORT.AUTHORISER` | `FsGiTxnEodStatusReport_Authoriser` | String |  |  |
| 24 | `FS.GI.TXN.EOD.STATUS.REPORT.CO.CODE` | `FsGiTxnEodStatusReport_CoCode` | String |  |  |
| 25 | `FS.GI.TXN.EOD.STATUS.REPORT.DEPT.CODE` | `FsGiTxnEodStatusReport_DeptCode` | String |  |  |
| 26 | `FS.GI.TXN.EOD.STATUS.REPORT.AUDITOR.CODE` | `FsGiTxnEodStatusReport_AuditorCode` | String |  |  |
| 27 | `FS.GI.TXN.EOD.STATUS.REPORT.AUDIT.DATE.TIME` | `FsGiTxnEodStatusReport_AuditDateTime` | String |  |  |
