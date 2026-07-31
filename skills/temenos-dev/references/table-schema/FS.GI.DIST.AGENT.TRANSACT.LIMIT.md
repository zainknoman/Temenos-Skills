# FS.GI.DIST.AGENT.TRANSACT.LIMIT — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.TRANSACT.LIMIT` in `FS_InvestmentRestrictions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.PARENT.REF.ID` | `FsGiDistAgentTransactLimit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.ORA.ROWID` | `FsGiDistAgentTransactLimit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.AGENT.ID` | `FsGiDistAgentTransactLimit_AgentId` | TField |  | Agent internal ID. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.OPERATION.CODE` | `FsGiDistAgentTransactLimit_OperationCode` | TField |  | Operation code for which the transaction limit check is applicable. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.TA.FUND.ID` | `FsGiDistAgentTransactLimit_TaFundId` | TField |  | Fund for which the transaction limit is applicable. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.SHARE.CLASS.CODE` | `FsGiDistAgentTransactLimit_ShareClassCode` | TField |  | Fund share class code for which the transaction limit is applicable. Multifonds DB Column is TPART. |
| 7 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.PAYMENT.CURRENCY` | `FsGiDistAgentTransactLimit_PaymentCurrency` | TField |  | Payment currency (in 3 letter ISO format eg. &apos;USD&apos;). Multifonds DB Column is CMON. |
| 8 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.MINIMUM.LIMIT` | `FsGiDistAgentTransactLimit_MinimumLimit` | TField |  | Minimum transaction limit check that will be performed at order level for a fund share class. Multifonds DB Column is NMIN_LIMIT. |
| 9 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.MAXIMUM.LIMIT` | `FsGiDistAgentTransactLimit_MaximumLimit` | TField |  | Maximum transaction limit check that will be performed at order level for a fund share class. Multifonds DB Column is NMAX_LIMIT. |
| 10 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.MINIMUM.BATCH.LIMIT` | `FsGiDistAgentTransactLimit_MinimumBatchLimit` | TField |  | Minimum transaction limit check that will be performed at batch process level for a fund share class. Multifonds DB Column is NBATCH_LIMIT. |
| 11 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.FIRST.SUBSCRIPTION.FLAG` | `FsGiDistAgentTransactLimit_FirstSubscriptionFlag` | TField |  | Its an internal technical flag to indicate the transaction limits defined for the fund share class first subscription functionality. Multifonds DB Column is FLG_FIRST_SUB. |
| 12 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.AGENT.TRNS.LIMIT.ID` | `FsGiDistAgentTransactLimit_AgentTrnsLimitId` | TField |  | Unique internal identifiter for agent transaction limit record. Multifonds DB Column is INTERNAL_ID. |
| 13 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.FUND.ID` | `FsGiDistAgentTransactLimit_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 14 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.CLASS.CURRENCY` | `FsGiDistAgentTransactLimit_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 15 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED10` | `FsGiDistAgentTransactLimit_Reserved10` | TField |  |  |
| 16 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED9` | `FsGiDistAgentTransactLimit_Reserved9` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED8` | `FsGiDistAgentTransactLimit_Reserved8` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED7` | `FsGiDistAgentTransactLimit_Reserved7` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED6` | `FsGiDistAgentTransactLimit_Reserved6` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED5` | `FsGiDistAgentTransactLimit_Reserved5` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED4` | `FsGiDistAgentTransactLimit_Reserved4` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED3` | `FsGiDistAgentTransactLimit_Reserved3` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED2` | `FsGiDistAgentTransactLimit_Reserved2` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RESERVED1` | `FsGiDistAgentTransactLimit_Reserved1` | TField |  |  |
| 25 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.LOCAL.REF` | `FsGiDistAgentTransactLimit_LocalRef` |  |  |  |
| 26 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.OVERRIDE` | `FsGiDistAgentTransactLimit_Override` |  |  |  |
| 27 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.RECORD.STATUS` | `FsGiDistAgentTransactLimit_RecordStatus` | String |  |  |
| 28 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.CURR.NO` | `FsGiDistAgentTransactLimit_CurrNo` | String |  |  |
| 29 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.INPUTTER` | `FsGiDistAgentTransactLimit_Inputter` |  |  |  |
| 30 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.DATE.TIME` | `FsGiDistAgentTransactLimit_DateTime` |  |  |  |
| 31 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.AUTHORISER` | `FsGiDistAgentTransactLimit_Authoriser` | String |  |  |
| 32 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.CO.CODE` | `FsGiDistAgentTransactLimit_CoCode` | String |  |  |
| 33 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.DEPT.CODE` | `FsGiDistAgentTransactLimit_DeptCode` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.AUDITOR.CODE` | `FsGiDistAgentTransactLimit_AuditorCode` | String |  |  |
| 35 | `FS.GI.DIST.AGENT.TRANSACT.LIMIT.AUDIT.DATE.TIME` | `FsGiDistAgentTransactLimit_AuditDateTime` | String |  |  |
