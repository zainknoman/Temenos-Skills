# FS.GA.TRANSACTION.ORDER.EQUIVALENCE — Table Schema

> Source: `INSERTS/I_F.FS.GA.TRANSACTION.ORDER.EQUIVALENCE` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.PARENT.REF.ID` | `FsGaTransactionOrderEquivalence_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.ORA.ROWID` | `FsGaTransactionOrderEquivalence_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.FUND.ID` | `FsGaTransactionOrderEquivalence_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.INTERFACE.TRAN.IDENTIFIER` | `FsGaTransactionOrderEquivalence_InterfaceTranIdentifier` | TField |  | Interface Transaction Identifier Multifonds DB Column is TYPE_TRS. |
| 5 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.SORT.ORDER` | `FsGaTransactionOrderEquivalence_SortOrder` | TField |  | Sort Order Multifonds DB Column is SORT_ORDER. |
| 6 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED10` | `FsGaTransactionOrderEquivalence_Reserved10` | TField |  |  |
| 7 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED9` | `FsGaTransactionOrderEquivalence_Reserved9` | TField |  |  |
| 8 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED8` | `FsGaTransactionOrderEquivalence_Reserved8` | TField |  |  |
| 9 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED7` | `FsGaTransactionOrderEquivalence_Reserved7` | TField |  |  |
| 10 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED6` | `FsGaTransactionOrderEquivalence_Reserved6` | TField |  |  |
| 11 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED5` | `FsGaTransactionOrderEquivalence_Reserved5` | TField |  |  |
| 12 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED4` | `FsGaTransactionOrderEquivalence_Reserved4` | TField |  |  |
| 13 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED3` | `FsGaTransactionOrderEquivalence_Reserved3` | TField |  |  |
| 14 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED2` | `FsGaTransactionOrderEquivalence_Reserved2` | TField |  |  |
| 15 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RESERVED1` | `FsGaTransactionOrderEquivalence_Reserved1` | TField |  |  |
| 16 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.LOCAL.REF` | `FsGaTransactionOrderEquivalence_LocalRef` |  |  |  |
| 17 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.OVERRIDE` | `FsGaTransactionOrderEquivalence_Override` |  |  |  |
| 18 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.RECORD.STATUS` | `FsGaTransactionOrderEquivalence_RecordStatus` | String |  |  |
| 19 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.CURR.NO` | `FsGaTransactionOrderEquivalence_CurrNo` | String |  |  |
| 20 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.INPUTTER` | `FsGaTransactionOrderEquivalence_Inputter` |  |  |  |
| 21 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.DATE.TIME` | `FsGaTransactionOrderEquivalence_DateTime` |  |  |  |
| 22 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.AUTHORISER` | `FsGaTransactionOrderEquivalence_Authoriser` | String |  |  |
| 23 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.CO.CODE` | `FsGaTransactionOrderEquivalence_CoCode` | String |  |  |
| 24 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.DEPT.CODE` | `FsGaTransactionOrderEquivalence_DeptCode` | String |  |  |
| 25 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.AUDITOR.CODE` | `FsGaTransactionOrderEquivalence_AuditorCode` | String |  |  |
| 26 | `FS.GA.TRANSACTION.ORDER.EQUIVALENCE.AUDIT.DATE.TIME` | `FsGaTransactionOrderEquivalence_AuditDateTime` | String |  |  |
