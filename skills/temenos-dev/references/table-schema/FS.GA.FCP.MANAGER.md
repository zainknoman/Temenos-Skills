# FS.GA.FCP.MANAGER — Table Schema

> Source: `INSERTS/I_F.FS.GA.FCP.MANAGER` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FCP.MANAGER.PARENT.REF.ID` | `FsGaFcpManager_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FCP.MANAGER.ORA.ROWID` | `FsGaFcpManager_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FCP.MANAGER.FUND.ID` | `FsGaFcpManager_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FCP.MANAGER.MANAGER.CODE` | `FsGaFcpManager_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 5 | `FS.GA.FCP.MANAGER.SUBS.RED.SUFFIX` | `FsGaFcpManager_SubsRedSuffix` | TField |  | Subs Red Suffix Multifonds DB Column is SUB_RED_NSUFF. |
| 6 | `FS.GA.FCP.MANAGER.RESERVED10` | `FsGaFcpManager_Reserved10` | TField |  |  |
| 7 | `FS.GA.FCP.MANAGER.RESERVED9` | `FsGaFcpManager_Reserved9` | TField |  |  |
| 8 | `FS.GA.FCP.MANAGER.RESERVED8` | `FsGaFcpManager_Reserved8` | TField |  |  |
| 9 | `FS.GA.FCP.MANAGER.RESERVED7` | `FsGaFcpManager_Reserved7` | TField |  |  |
| 10 | `FS.GA.FCP.MANAGER.RESERVED6` | `FsGaFcpManager_Reserved6` | TField |  |  |
| 11 | `FS.GA.FCP.MANAGER.RESERVED5` | `FsGaFcpManager_Reserved5` | TField |  |  |
| 12 | `FS.GA.FCP.MANAGER.RESERVED4` | `FsGaFcpManager_Reserved4` | TField |  |  |
| 13 | `FS.GA.FCP.MANAGER.RESERVED3` | `FsGaFcpManager_Reserved3` | TField |  |  |
| 14 | `FS.GA.FCP.MANAGER.RESERVED2` | `FsGaFcpManager_Reserved2` | TField |  |  |
| 15 | `FS.GA.FCP.MANAGER.RESERVED1` | `FsGaFcpManager_Reserved1` | TField |  |  |
| 16 | `FS.GA.FCP.MANAGER.LOCAL.REF` | `FsGaFcpManager_LocalRef` |  |  |  |
| 17 | `FS.GA.FCP.MANAGER.OVERRIDE` | `FsGaFcpManager_Override` |  |  |  |
| 18 | `FS.GA.FCP.MANAGER.RECORD.STATUS` | `FsGaFcpManager_RecordStatus` | String |  |  |
| 19 | `FS.GA.FCP.MANAGER.CURR.NO` | `FsGaFcpManager_CurrNo` | String |  |  |
| 20 | `FS.GA.FCP.MANAGER.INPUTTER` | `FsGaFcpManager_Inputter` |  |  |  |
| 21 | `FS.GA.FCP.MANAGER.DATE.TIME` | `FsGaFcpManager_DateTime` |  |  |  |
| 22 | `FS.GA.FCP.MANAGER.AUTHORISER` | `FsGaFcpManager_Authoriser` | String |  |  |
| 23 | `FS.GA.FCP.MANAGER.CO.CODE` | `FsGaFcpManager_CoCode` | String |  |  |
| 24 | `FS.GA.FCP.MANAGER.DEPT.CODE` | `FsGaFcpManager_DeptCode` | String |  |  |
| 25 | `FS.GA.FCP.MANAGER.AUDITOR.CODE` | `FsGaFcpManager_AuditorCode` | String |  |  |
| 26 | `FS.GA.FCP.MANAGER.AUDIT.DATE.TIME` | `FsGaFcpManager_AuditDateTime` | String |  |  |
