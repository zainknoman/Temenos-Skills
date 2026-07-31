# FS.GI.TXN.EOD.REGISTER.POSITION — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.EOD.REGISTER.POSITION` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.EOD.REGISTER.POSITION.LEGAL.ENTITY.ID` | `FsGiTxnEodRegisterPosition_LegalEntityId` | TField |  | Legal entity ID. Multifonds DB Column is NTFC. |
| 2 | `FS.GI.TXN.EOD.REGISTER.POSITION.FUND.ID` | `FsGiTxnEodRegisterPosition_FundId` | TField |  | Fund internal ID Multifonds DB Column is NPTF. |
| 3 | `FS.GI.TXN.EOD.REGISTER.POSITION.SHARE.CLASS.CODE` | `FsGiTxnEodRegisterPosition_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 4 | `FS.GI.TXN.EOD.REGISTER.POSITION.AGENT.ID` | `FsGiTxnEodRegisterPosition_AgentId` | TField |  | Agent ID linked to the register. Multifonds DB Column is NOUTLET. |
| 5 | `FS.GI.TXN.EOD.REGISTER.POSITION.QUANTITY` | `FsGiTxnEodRegisterPosition_Quantity` | TField |  | Quantity of shares held by the register. Multifonds DB Column is QUANTITY. |
| 6 | `FS.GI.TXN.EOD.REGISTER.POSITION.REGISTER.ID` | `FsGiTxnEodRegisterPosition_RegisterId` | TField |  | Register ID linked to the agent. Multifonds DB Column is NREGISTER. |
| 7 | `FS.GI.TXN.EOD.REGISTER.POSITION.ACCOUNTING.DATE.MF` | `FsGiTxnEodRegisterPosition_AccountingDateMf` | TField |  | Application date when end of day processed. Multifonds DB Column is DCTA. |
| 8 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED10` | `FsGiTxnEodRegisterPosition_Reserved10` | TField |  |  |
| 9 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED9` | `FsGiTxnEodRegisterPosition_Reserved9` | TField |  |  |
| 10 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED8` | `FsGiTxnEodRegisterPosition_Reserved8` | TField |  |  |
| 11 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED7` | `FsGiTxnEodRegisterPosition_Reserved7` | TField |  |  |
| 12 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED6` | `FsGiTxnEodRegisterPosition_Reserved6` | TField |  |  |
| 13 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED5` | `FsGiTxnEodRegisterPosition_Reserved5` | TField |  |  |
| 14 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED4` | `FsGiTxnEodRegisterPosition_Reserved4` | TField |  |  |
| 15 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED3` | `FsGiTxnEodRegisterPosition_Reserved3` | TField |  |  |
| 16 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED2` | `FsGiTxnEodRegisterPosition_Reserved2` | TField |  |  |
| 17 | `FS.GI.TXN.EOD.REGISTER.POSITION.RESERVED1` | `FsGiTxnEodRegisterPosition_Reserved1` | TField |  |  |
| 18 | `FS.GI.TXN.EOD.REGISTER.POSITION.LOCAL.REF` | `FsGiTxnEodRegisterPosition_LocalRef` |  |  |  |
| 19 | `FS.GI.TXN.EOD.REGISTER.POSITION.OVERRIDE` | `FsGiTxnEodRegisterPosition_Override` |  |  |  |
| 20 | `FS.GI.TXN.EOD.REGISTER.POSITION.RECORD.STATUS` | `FsGiTxnEodRegisterPosition_RecordStatus` | String |  |  |
| 21 | `FS.GI.TXN.EOD.REGISTER.POSITION.CURR.NO` | `FsGiTxnEodRegisterPosition_CurrNo` | String |  |  |
| 22 | `FS.GI.TXN.EOD.REGISTER.POSITION.INPUTTER` | `FsGiTxnEodRegisterPosition_Inputter` |  |  |  |
| 23 | `FS.GI.TXN.EOD.REGISTER.POSITION.DATE.TIME` | `FsGiTxnEodRegisterPosition_DateTime` |  |  |  |
| 24 | `FS.GI.TXN.EOD.REGISTER.POSITION.AUTHORISER` | `FsGiTxnEodRegisterPosition_Authoriser` | String |  |  |
| 25 | `FS.GI.TXN.EOD.REGISTER.POSITION.CO.CODE` | `FsGiTxnEodRegisterPosition_CoCode` | String |  |  |
| 26 | `FS.GI.TXN.EOD.REGISTER.POSITION.DEPT.CODE` | `FsGiTxnEodRegisterPosition_DeptCode` | String |  |  |
| 27 | `FS.GI.TXN.EOD.REGISTER.POSITION.AUDITOR.CODE` | `FsGiTxnEodRegisterPosition_AuditorCode` | String |  |  |
| 28 | `FS.GI.TXN.EOD.REGISTER.POSITION.AUDIT.DATE.TIME` | `FsGiTxnEodRegisterPosition_AuditDateTime` | String |  |  |
