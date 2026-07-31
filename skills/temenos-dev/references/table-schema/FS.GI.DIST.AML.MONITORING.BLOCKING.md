# FS.GI.DIST.AML.MONITORING.BLOCKING — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AML.MONITORING.BLOCKING` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AML.MONITORING.BLOCKING.PARENT.REF.ID` | `FsGiDistAmlMonitoringBlocking_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AML.MONITORING.BLOCKING.ORA.ROWID` | `FsGiDistAmlMonitoringBlocking_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AML.MONITORING.BLOCKING.PARENT.ID.TYPE` | `FsGiDistAmlMonitoringBlocking_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.AML.MONITORING.BLOCKING.PARENT.ID` | `FsGiDistAmlMonitoringBlocking_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.AML.MONITORING.BLOCKING.MONITORING.BLOCK.CODE` | `FsGiDistAmlMonitoringBlocking_MonitoringBlockCode` | TField |  | The Monitoring blocking code applied on the entity based on AML Sanctions screening. For example:- PEP, Potential PEP, Diplomat etc., Multifonds DB Column is MONT_BLOCK_CODE. |
| 6 | `FS.GI.DIST.AML.MONITORING.BLOCKING.MONITORING.BLOCK.REASON` | `FsGiDistAmlMonitoringBlocking_MonitoringBlockReason` | TField |  | Monitoring blocking reason code. Multifonds DB Column is MONT_REASON_CODE. |
| 7 | `FS.GI.DIST.AML.MONITORING.BLOCKING.MONITORING.REASON.DATE` | `FsGiDistAmlMonitoringBlocking_MonitoringReasonDate` | TField |  | Monitoring blocking reason code update date. Multifonds DB Column is DMONT_REASON. |
| 8 | `FS.GI.DIST.AML.MONITORING.BLOCKING.MONITORING.INTERNAL.ID` | `FsGiDistAmlMonitoringBlocking_MonitoringInternalId` | TField |  | Unique internal monitoring blocking identifier. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED10` | `FsGiDistAmlMonitoringBlocking_Reserved10` | TField |  |  |
| 10 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED9` | `FsGiDistAmlMonitoringBlocking_Reserved9` | TField |  |  |
| 11 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED8` | `FsGiDistAmlMonitoringBlocking_Reserved8` | TField |  |  |
| 12 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED7` | `FsGiDistAmlMonitoringBlocking_Reserved7` | TField |  |  |
| 13 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED6` | `FsGiDistAmlMonitoringBlocking_Reserved6` | TField |  |  |
| 14 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED5` | `FsGiDistAmlMonitoringBlocking_Reserved5` | TField |  |  |
| 15 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED4` | `FsGiDistAmlMonitoringBlocking_Reserved4` | TField |  |  |
| 16 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED3` | `FsGiDistAmlMonitoringBlocking_Reserved3` | TField |  |  |
| 17 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED2` | `FsGiDistAmlMonitoringBlocking_Reserved2` | TField |  |  |
| 18 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RESERVED1` | `FsGiDistAmlMonitoringBlocking_Reserved1` | TField |  |  |
| 19 | `FS.GI.DIST.AML.MONITORING.BLOCKING.LOCAL.REF` | `FsGiDistAmlMonitoringBlocking_LocalRef` |  |  |  |
| 20 | `FS.GI.DIST.AML.MONITORING.BLOCKING.OVERRIDE` | `FsGiDistAmlMonitoringBlocking_Override` |  |  |  |
| 21 | `FS.GI.DIST.AML.MONITORING.BLOCKING.RECORD.STATUS` | `FsGiDistAmlMonitoringBlocking_RecordStatus` | String |  |  |
| 22 | `FS.GI.DIST.AML.MONITORING.BLOCKING.CURR.NO` | `FsGiDistAmlMonitoringBlocking_CurrNo` | String |  |  |
| 23 | `FS.GI.DIST.AML.MONITORING.BLOCKING.INPUTTER` | `FsGiDistAmlMonitoringBlocking_Inputter` |  |  |  |
| 24 | `FS.GI.DIST.AML.MONITORING.BLOCKING.DATE.TIME` | `FsGiDistAmlMonitoringBlocking_DateTime` |  |  |  |
| 25 | `FS.GI.DIST.AML.MONITORING.BLOCKING.AUTHORISER` | `FsGiDistAmlMonitoringBlocking_Authoriser` | String |  |  |
| 26 | `FS.GI.DIST.AML.MONITORING.BLOCKING.CO.CODE` | `FsGiDistAmlMonitoringBlocking_CoCode` | String |  |  |
| 27 | `FS.GI.DIST.AML.MONITORING.BLOCKING.DEPT.CODE` | `FsGiDistAmlMonitoringBlocking_DeptCode` | String |  |  |
| 28 | `FS.GI.DIST.AML.MONITORING.BLOCKING.AUDITOR.CODE` | `FsGiDistAmlMonitoringBlocking_AuditorCode` | String |  |  |
| 29 | `FS.GI.DIST.AML.MONITORING.BLOCKING.AUDIT.DATE.TIME` | `FsGiDistAmlMonitoringBlocking_AuditDateTime` | String |  |  |
