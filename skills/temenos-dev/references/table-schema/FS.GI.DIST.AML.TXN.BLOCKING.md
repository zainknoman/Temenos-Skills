# FS.GI.DIST.AML.TXN.BLOCKING — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AML.TXN.BLOCKING` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AML.TXN.BLOCKING.PARENT.REF.ID` | `FsGiDistAmlTxnBlocking_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AML.TXN.BLOCKING.ORA.ROWID` | `FsGiDistAmlTxnBlocking_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AML.TXN.BLOCKING.PARENT.ID.TYPE` | `FsGiDistAmlTxnBlocking_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.AML.TXN.BLOCKING.PARENT.ID` | `FsGiDistAmlTxnBlocking_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.AML.TXN.BLOCKING.TRANSACTION.BLOCKING.CODE` | `FsGiDistAmlTxnBlocking_TransactionBlockingCode` | TField |  | It specifies the code to block the entity for specific transactions. Multifonds DB Column is BLOCK_CODE. |
| 6 | `FS.GI.DIST.AML.TXN.BLOCKING.TXN.BLOCKING.SEQUENCE.NUMBER` | `FsGiDistAmlTxnBlocking_TxnBlockingSequenceNumber` | TField |  | Sequence number for sorting of tranasction blocking codes within a single entity. Multifonds DB Column is SEQ_NO. |
| 7 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED10` | `FsGiDistAmlTxnBlocking_Reserved10` | TField |  |  |
| 8 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED9` | `FsGiDistAmlTxnBlocking_Reserved9` | TField |  |  |
| 9 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED8` | `FsGiDistAmlTxnBlocking_Reserved8` | TField |  |  |
| 10 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED7` | `FsGiDistAmlTxnBlocking_Reserved7` | TField |  |  |
| 11 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED6` | `FsGiDistAmlTxnBlocking_Reserved6` | TField |  |  |
| 12 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED5` | `FsGiDistAmlTxnBlocking_Reserved5` | TField |  |  |
| 13 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED4` | `FsGiDistAmlTxnBlocking_Reserved4` | TField |  |  |
| 14 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED3` | `FsGiDistAmlTxnBlocking_Reserved3` | TField |  |  |
| 15 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED2` | `FsGiDistAmlTxnBlocking_Reserved2` | TField |  |  |
| 16 | `FS.GI.DIST.AML.TXN.BLOCKING.RESERVED1` | `FsGiDistAmlTxnBlocking_Reserved1` | TField |  |  |
| 17 | `FS.GI.DIST.AML.TXN.BLOCKING.LOCAL.REF` | `FsGiDistAmlTxnBlocking_LocalRef` |  |  |  |
| 18 | `FS.GI.DIST.AML.TXN.BLOCKING.OVERRIDE` | `FsGiDistAmlTxnBlocking_Override` |  |  |  |
| 19 | `FS.GI.DIST.AML.TXN.BLOCKING.RECORD.STATUS` | `FsGiDistAmlTxnBlocking_RecordStatus` | String |  |  |
| 20 | `FS.GI.DIST.AML.TXN.BLOCKING.CURR.NO` | `FsGiDistAmlTxnBlocking_CurrNo` | String |  |  |
| 21 | `FS.GI.DIST.AML.TXN.BLOCKING.INPUTTER` | `FsGiDistAmlTxnBlocking_Inputter` |  |  |  |
| 22 | `FS.GI.DIST.AML.TXN.BLOCKING.DATE.TIME` | `FsGiDistAmlTxnBlocking_DateTime` |  |  |  |
| 23 | `FS.GI.DIST.AML.TXN.BLOCKING.AUTHORISER` | `FsGiDistAmlTxnBlocking_Authoriser` | String |  |  |
| 24 | `FS.GI.DIST.AML.TXN.BLOCKING.CO.CODE` | `FsGiDistAmlTxnBlocking_CoCode` | String |  |  |
| 25 | `FS.GI.DIST.AML.TXN.BLOCKING.DEPT.CODE` | `FsGiDistAmlTxnBlocking_DeptCode` | String |  |  |
| 26 | `FS.GI.DIST.AML.TXN.BLOCKING.AUDITOR.CODE` | `FsGiDistAmlTxnBlocking_AuditorCode` | String |  |  |
| 27 | `FS.GI.DIST.AML.TXN.BLOCKING.AUDIT.DATE.TIME` | `FsGiDistAmlTxnBlocking_AuditDateTime` | String |  |  |
