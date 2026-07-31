# FS.GI.WEM.EXCEPTION.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.EXCEPTION.PROCESS` in `FS_WemProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.EXCEPTION.PROCESS.PARENT.REF.ID` | `FsGiWemExceptionProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.WEM.EXCEPTION.PROCESS.ORA.ROWID` | `FsGiWemExceptionProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.WEM.EXCEPTION.PROCESS.EXCHANGE.GROUP.PROCESS` | `FsGiWemExceptionProcess_ExchangeGroupProcess` | TField |  | Workflow Exception Management (WEM) exchange group for which there is exception. Multifonds DB Column is P_CGROUPE_COURS. |
| 4 | `FS.GI.WEM.EXCEPTION.PROCESS.TRADE.DATE.PROCESS` | `FsGiWemExceptionProcess_TradeDateProcess` | TField |  | Trade date of the WEM process. Multifonds DB Column is P_DOPER. |
| 5 | `FS.GI.WEM.EXCEPTION.PROCESS.ACCOUNTING.DATE.MF.PROCESS` | `FsGiWemExceptionProcess_AccountingDateMfProcess` | TField |  | Accounting date. Multifonds DB Column is P_DCTA. |
| 6 | `FS.GI.WEM.EXCEPTION.PROCESS.CONTROL.NUMBER.PROCESS` | `FsGiWemExceptionProcess_ControlNumberProcess` | TField |  | Unique control number. Multifonds DB Column is P_CONTROL_NO. |
| 7 | `FS.GI.WEM.EXCEPTION.PROCESS.PROCESS.GROUP.PROCESS` | `FsGiWemExceptionProcess_ProcessGroupProcess` | TField |  | Current process group for which exception is encountered. Multifonds DB Column is P_PROCESS_GROUP. |
| 8 | `FS.GI.WEM.EXCEPTION.PROCESS.WEM.PROCESS.TYPE.PROCESS` | `FsGiWemExceptionProcess_WemProcessTypeProcess` | TField |  | User defined code to describe a process type. Multifonds DB Column is P_CPROCESS. |
| 9 | `FS.GI.WEM.EXCEPTION.PROCESS.ERROR.MESSAGE.PROCESS` | `FsGiWemExceptionProcess_ErrorMessageProcess` | TField |  | Error message for the exception. Multifonds DB Column is P_ERROR_MESSAGE. |
| 10 | `FS.GI.WEM.EXCEPTION.PROCESS.JUSTIFICATION.PROCESS` | `FsGiWemExceptionProcess_JustificationProcess` | TField |  | Justification for the exception. Multifonds DB Column is P_JUSTIFICATION_CODE. |
| 11 | `FS.GI.WEM.EXCEPTION.PROCESS.LINKED.FILE.NAME.PROCESS` | `FsGiWemExceptionProcess_LinkedFileNameProcess` | TField |  | Linked file name. Multifonds DB Column is P_FILE. |
| 12 | `FS.GI.WEM.EXCEPTION.PROCESS.DESCRIPTION.PROCESS` | `FsGiWemExceptionProcess_DescriptionProcess` | TField |  | Description of approval. Multifonds DB Column is P_DESCRIPTION. |
| 13 | `FS.GI.WEM.EXCEPTION.PROCESS.REJECT.REASON.PROCESS` | `FsGiWemExceptionProcess_RejectReasonProcess` | TField |  | Reason for rejecting exception. Multifonds DB Column is P_REJECT_REASON. |
| 14 | `FS.GI.WEM.EXCEPTION.PROCESS.ACTION.PROCESS` | `FsGiWemExceptionProcess_ActionProcess` | TField |  | Action performed on the exception - Submit, Validate or Reject. Multifonds DB Column is P_ACTION. |
| 15 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED10` | `FsGiWemExceptionProcess_Reserved10` | TField |  |  |
| 16 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED9` | `FsGiWemExceptionProcess_Reserved9` | TField |  |  |
| 17 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED8` | `FsGiWemExceptionProcess_Reserved8` | TField |  |  |
| 18 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED7` | `FsGiWemExceptionProcess_Reserved7` | TField |  |  |
| 19 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED6` | `FsGiWemExceptionProcess_Reserved6` | TField |  |  |
| 20 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED5` | `FsGiWemExceptionProcess_Reserved5` | TField |  |  |
| 21 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED4` | `FsGiWemExceptionProcess_Reserved4` | TField |  |  |
| 22 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED3` | `FsGiWemExceptionProcess_Reserved3` | TField |  |  |
| 23 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED2` | `FsGiWemExceptionProcess_Reserved2` | TField |  |  |
| 24 | `FS.GI.WEM.EXCEPTION.PROCESS.RESERVED1` | `FsGiWemExceptionProcess_Reserved1` | TField |  |  |
| 25 | `FS.GI.WEM.EXCEPTION.PROCESS.LOCAL.REF` | `FsGiWemExceptionProcess_LocalRef` |  |  |  |
| 26 | `FS.GI.WEM.EXCEPTION.PROCESS.OVERRIDE` | `FsGiWemExceptionProcess_Override` |  |  |  |
| 27 | `FS.GI.WEM.EXCEPTION.PROCESS.RECORD.STATUS` | `FsGiWemExceptionProcess_RecordStatus` | String |  |  |
| 28 | `FS.GI.WEM.EXCEPTION.PROCESS.CURR.NO` | `FsGiWemExceptionProcess_CurrNo` | String |  |  |
| 29 | `FS.GI.WEM.EXCEPTION.PROCESS.INPUTTER` | `FsGiWemExceptionProcess_Inputter` |  |  |  |
| 30 | `FS.GI.WEM.EXCEPTION.PROCESS.DATE.TIME` | `FsGiWemExceptionProcess_DateTime` |  |  |  |
| 31 | `FS.GI.WEM.EXCEPTION.PROCESS.AUTHORISER` | `FsGiWemExceptionProcess_Authoriser` | String |  |  |
| 32 | `FS.GI.WEM.EXCEPTION.PROCESS.CO.CODE` | `FsGiWemExceptionProcess_CoCode` | String |  |  |
| 33 | `FS.GI.WEM.EXCEPTION.PROCESS.DEPT.CODE` | `FsGiWemExceptionProcess_DeptCode` | String |  |  |
| 34 | `FS.GI.WEM.EXCEPTION.PROCESS.AUDITOR.CODE` | `FsGiWemExceptionProcess_AuditorCode` | String |  |  |
| 35 | `FS.GI.WEM.EXCEPTION.PROCESS.AUDIT.DATE.TIME` | `FsGiWemExceptionProcess_AuditDateTime` | String |  |  |
