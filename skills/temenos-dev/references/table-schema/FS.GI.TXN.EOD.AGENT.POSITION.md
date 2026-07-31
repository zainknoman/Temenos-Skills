# FS.GI.TXN.EOD.AGENT.POSITION — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.EOD.AGENT.POSITION` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.EOD.AGENT.POSITION.LEGAL.ENTITY.ID` | `FsGiTxnEodAgentPosition_LegalEntityId` | TField |  | Legal Entity ID. Multifonds DB Column is NTFC. |
| 2 | `FS.GI.TXN.EOD.AGENT.POSITION.FUND.ID` | `FsGiTxnEodAgentPosition_FundId` | TField |  | Fund internal ID in which the register has invested. Multifonds DB Column is NPTF. |
| 3 | `FS.GI.TXN.EOD.AGENT.POSITION.SHARE.CLASS.CODE` | `FsGiTxnEodAgentPosition_ShareClassCode` | TField |  | Fund share class code in which the register has invested. Multifonds DB Column is TPART. |
| 4 | `FS.GI.TXN.EOD.AGENT.POSITION.AGENT.ID` | `FsGiTxnEodAgentPosition_AgentId` | TField |  | Agent internal ID linked to the register. Multifonds DB Column is NOUTLET. |
| 5 | `FS.GI.TXN.EOD.AGENT.POSITION.QUANTITY` | `FsGiTxnEodAgentPosition_Quantity` | TField |  | Quantity of shares held by the register. Multifonds DB Column is QUANTITY. |
| 6 | `FS.GI.TXN.EOD.AGENT.POSITION.SHARE.PRICE` | `FsGiTxnEodAgentPosition_SharePrice` | TField |  | Applied share price. Multifonds DB Column is MNT_UNIT. |
| 7 | `FS.GI.TXN.EOD.AGENT.POSITION.POSITION` | `FsGiTxnEodAgentPosition_Position` | TField |  | Agent position for the register. Multifonds DB Column is POSITION. |
| 8 | `FS.GI.TXN.EOD.AGENT.POSITION.ACCOUNTING.DATE.MF` | `FsGiTxnEodAgentPosition_AccountingDateMf` | TField |  | Application date when end of day is processed. Multifonds DB Column is DCTA. |
| 9 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED10` | `FsGiTxnEodAgentPosition_Reserved10` | TField |  |  |
| 10 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED9` | `FsGiTxnEodAgentPosition_Reserved9` | TField |  |  |
| 11 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED8` | `FsGiTxnEodAgentPosition_Reserved8` | TField |  |  |
| 12 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED7` | `FsGiTxnEodAgentPosition_Reserved7` | TField |  |  |
| 13 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED6` | `FsGiTxnEodAgentPosition_Reserved6` | TField |  |  |
| 14 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED5` | `FsGiTxnEodAgentPosition_Reserved5` | TField |  |  |
| 15 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED4` | `FsGiTxnEodAgentPosition_Reserved4` | TField |  |  |
| 16 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED3` | `FsGiTxnEodAgentPosition_Reserved3` | TField |  |  |
| 17 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED2` | `FsGiTxnEodAgentPosition_Reserved2` | TField |  |  |
| 18 | `FS.GI.TXN.EOD.AGENT.POSITION.RESERVED1` | `FsGiTxnEodAgentPosition_Reserved1` | TField |  |  |
| 19 | `FS.GI.TXN.EOD.AGENT.POSITION.LOCAL.REF` | `FsGiTxnEodAgentPosition_LocalRef` |  |  |  |
| 20 | `FS.GI.TXN.EOD.AGENT.POSITION.OVERRIDE` | `FsGiTxnEodAgentPosition_Override` |  |  |  |
| 21 | `FS.GI.TXN.EOD.AGENT.POSITION.RECORD.STATUS` | `FsGiTxnEodAgentPosition_RecordStatus` | String |  |  |
| 22 | `FS.GI.TXN.EOD.AGENT.POSITION.CURR.NO` | `FsGiTxnEodAgentPosition_CurrNo` | String |  |  |
| 23 | `FS.GI.TXN.EOD.AGENT.POSITION.INPUTTER` | `FsGiTxnEodAgentPosition_Inputter` |  |  |  |
| 24 | `FS.GI.TXN.EOD.AGENT.POSITION.DATE.TIME` | `FsGiTxnEodAgentPosition_DateTime` |  |  |  |
| 25 | `FS.GI.TXN.EOD.AGENT.POSITION.AUTHORISER` | `FsGiTxnEodAgentPosition_Authoriser` | String |  |  |
| 26 | `FS.GI.TXN.EOD.AGENT.POSITION.CO.CODE` | `FsGiTxnEodAgentPosition_CoCode` | String |  |  |
| 27 | `FS.GI.TXN.EOD.AGENT.POSITION.DEPT.CODE` | `FsGiTxnEodAgentPosition_DeptCode` | String |  |  |
| 28 | `FS.GI.TXN.EOD.AGENT.POSITION.AUDITOR.CODE` | `FsGiTxnEodAgentPosition_AuditorCode` | String |  |  |
| 29 | `FS.GI.TXN.EOD.AGENT.POSITION.AUDIT.DATE.TIME` | `FsGiTxnEodAgentPosition_AuditDateTime` | String |  |  |
