# FS.GI.FUND.MANAGER — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.MANAGER` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.MANAGER.PARENT.REF.ID` | `FsGiFundManager_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.MANAGER.ORA.ROWID` | `FsGiFundManager_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.MANAGER.FUND.ID` | `FsGiFundManager_FundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.MANAGER.MANAGER.ID` | `FsGiFundManager_ManagerId` | TField |  | Central register that will represent the manager of the fund. Multifonds DB Column is NS_PORTFOLIO. |
| 5 | `FS.GI.FUND.MANAGER.SUB.RED.PERCENTAGE` | `FsGiFundManager_SubRedPercentage` | TField |  | Percentage to be allocated to the selected manager. Multifonds DB Column is PCT_ACT. |
| 6 | `FS.GI.FUND.MANAGER.PERCENTAGE` | `FsGiFundManager_Percentage` | TField |  | Global percentage is same percentage as the &apos;Sub Red Percentage&apos;. Multifonds DB Column is PCT. |
| 7 | `FS.GI.FUND.MANAGER.PRIMARY.FLAG` | `FsGiFundManager_PrimaryFlag` | TField |  | Flag to indicate the manager as the primary manager. Multifonds DB Column is PRIMARY_MAN_FLG. |
| 8 | `FS.GI.FUND.MANAGER.THRESHOLD.MANAGER.FLAG` | `FsGiFundManager_ThresholdManagerFlag` | TField |  | Flag to indicate the manager as the threshold manager to allocate threshold amount. If a transaction is placed for an amount less than the threshold, the threshold manager will get the total amount of the transaction Multifonds DB Column is THRESHOLD_MAN_FLG. |
| 9 | `FS.GI.FUND.MANAGER.THRESHOLD` | `FsGiFundManager_Threshold` | TField |  | Threshold amount. Multifonds DB Column is THRESHOLD. |
| 10 | `FS.GI.FUND.MANAGER.FUND.MANAGER.INTERNAL.ID` | `FsGiFundManager_FundManagerInternalId` | TField |  | Unique internal identifier for fund manager record. Multifonds DB Column is INTERNAL_ID. |
| 11 | `FS.GI.FUND.MANAGER.RESERVED10` | `FsGiFundManager_Reserved10` | TField |  |  |
| 12 | `FS.GI.FUND.MANAGER.RESERVED9` | `FsGiFundManager_Reserved9` | TField |  |  |
| 13 | `FS.GI.FUND.MANAGER.RESERVED8` | `FsGiFundManager_Reserved8` | TField |  |  |
| 14 | `FS.GI.FUND.MANAGER.RESERVED7` | `FsGiFundManager_Reserved7` | TField |  |  |
| 15 | `FS.GI.FUND.MANAGER.RESERVED6` | `FsGiFundManager_Reserved6` | TField |  |  |
| 16 | `FS.GI.FUND.MANAGER.RESERVED5` | `FsGiFundManager_Reserved5` | TField |  |  |
| 17 | `FS.GI.FUND.MANAGER.RESERVED4` | `FsGiFundManager_Reserved4` | TField |  |  |
| 18 | `FS.GI.FUND.MANAGER.RESERVED3` | `FsGiFundManager_Reserved3` | TField |  |  |
| 19 | `FS.GI.FUND.MANAGER.RESERVED2` | `FsGiFundManager_Reserved2` | TField |  |  |
| 20 | `FS.GI.FUND.MANAGER.RESERVED1` | `FsGiFundManager_Reserved1` | TField |  |  |
| 21 | `FS.GI.FUND.MANAGER.LOCAL.REF` | `FsGiFundManager_LocalRef` |  |  |  |
| 22 | `FS.GI.FUND.MANAGER.OVERRIDE` | `FsGiFundManager_Override` |  |  |  |
| 23 | `FS.GI.FUND.MANAGER.RECORD.STATUS` | `FsGiFundManager_RecordStatus` | String |  |  |
| 24 | `FS.GI.FUND.MANAGER.CURR.NO` | `FsGiFundManager_CurrNo` | String |  |  |
| 25 | `FS.GI.FUND.MANAGER.INPUTTER` | `FsGiFundManager_Inputter` |  |  |  |
| 26 | `FS.GI.FUND.MANAGER.DATE.TIME` | `FsGiFundManager_DateTime` |  |  |  |
| 27 | `FS.GI.FUND.MANAGER.AUTHORISER` | `FsGiFundManager_Authoriser` | String |  |  |
| 28 | `FS.GI.FUND.MANAGER.CO.CODE` | `FsGiFundManager_CoCode` | String |  |  |
| 29 | `FS.GI.FUND.MANAGER.DEPT.CODE` | `FsGiFundManager_DeptCode` | String |  |  |
| 30 | `FS.GI.FUND.MANAGER.AUDITOR.CODE` | `FsGiFundManager_AuditorCode` | String |  |  |
| 31 | `FS.GI.FUND.MANAGER.AUDIT.DATE.TIME` | `FsGiFundManager_AuditDateTime` | String |  |  |
