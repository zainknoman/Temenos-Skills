# FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.PARENT.REF.ID` | `FsGiTxnPaymentUnsettleProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.ORA.ROWID` | `FsGiTxnPaymentUnsettleProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.DEAL.REFERENCE` | `FsGiTxnPaymentUnsettleProcess_DealReference` | TField |  | Deal Reference of the transaction. Multifonds DB Column is DEAL_REF. |
| 4 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.ORDER.ID` | `FsGiTxnPaymentUnsettleProcess_OrderId` | TField |  | Order number of the transaction. Multifonds DB Column is NORDER. |
| 5 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.AGENT.ID` | `FsGiTxnPaymentUnsettleProcess_AgentId` | TField |  | Agent internal ID of the transaction. Multifonds DB Column is NOUTLET. |
| 6 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.PARTIAL.SETTLEMENT.ID` | `FsGiTxnPaymentUnsettleProcess_PartialSettlementId` | TField |  | Partial settlement ID of the Transaction. Multifonds DB Column is PART_SETT_ID. |
| 7 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED10` | `FsGiTxnPaymentUnsettleProcess_Reserved10` | TField |  |  |
| 8 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED9` | `FsGiTxnPaymentUnsettleProcess_Reserved9` | TField |  |  |
| 9 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED8` | `FsGiTxnPaymentUnsettleProcess_Reserved8` | TField |  |  |
| 10 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED7` | `FsGiTxnPaymentUnsettleProcess_Reserved7` | TField |  |  |
| 11 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED6` | `FsGiTxnPaymentUnsettleProcess_Reserved6` | TField |  |  |
| 12 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED5` | `FsGiTxnPaymentUnsettleProcess_Reserved5` | TField |  |  |
| 13 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED4` | `FsGiTxnPaymentUnsettleProcess_Reserved4` | TField |  |  |
| 14 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED3` | `FsGiTxnPaymentUnsettleProcess_Reserved3` | TField |  |  |
| 15 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED2` | `FsGiTxnPaymentUnsettleProcess_Reserved2` | TField |  |  |
| 16 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RESERVED1` | `FsGiTxnPaymentUnsettleProcess_Reserved1` | TField |  |  |
| 17 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.LOCAL.REF` | `FsGiTxnPaymentUnsettleProcess_LocalRef` |  |  |  |
| 18 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.OVERRIDE` | `FsGiTxnPaymentUnsettleProcess_Override` |  |  |  |
| 19 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.RECORD.STATUS` | `FsGiTxnPaymentUnsettleProcess_RecordStatus` | String |  |  |
| 20 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.CURR.NO` | `FsGiTxnPaymentUnsettleProcess_CurrNo` | String |  |  |
| 21 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.INPUTTER` | `FsGiTxnPaymentUnsettleProcess_Inputter` |  |  |  |
| 22 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.DATE.TIME` | `FsGiTxnPaymentUnsettleProcess_DateTime` |  |  |  |
| 23 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.AUTHORISER` | `FsGiTxnPaymentUnsettleProcess_Authoriser` | String |  |  |
| 24 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.CO.CODE` | `FsGiTxnPaymentUnsettleProcess_CoCode` | String |  |  |
| 25 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.DEPT.CODE` | `FsGiTxnPaymentUnsettleProcess_DeptCode` | String |  |  |
| 26 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.AUDITOR.CODE` | `FsGiTxnPaymentUnsettleProcess_AuditorCode` | String |  |  |
| 27 | `FS.GI.TXN.PAYMENT.UNSETTLE.PROCESS.AUDIT.DATE.TIME` | `FsGiTxnPaymentUnsettleProcess_AuditDateTime` | String |  |  |
