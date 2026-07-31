# FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.PARENT.REF.ID` | `FsGiFundLegalEntityTxnFdTdsk_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.ORA.ROWID` | `FsGiFundLegalEntityTxnFdTdsk_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.LEGAL.ENTITY.ID` | `FsGiFundLegalEntityTxnFdTdsk_LegalEntityId` | TField |  | Legal Entity internal ID . Multifonds DB Column is NTFC. |
| 4 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.OPERATION.CODE` | `FsGiFundLegalEntityTxnFdTdsk_OperationCode` | TField |  | The operation code for which the fund trading desk is applicable. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.IN.SCOPE.FLAG` | `FsGiFundLegalEntityTxnFdTdsk_InScopeFlag` | TField |  | Flag indicates that the transaction is inscope of fund trading desk. Multifonds DB Column is FLG_SCOPE. |
| 6 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.FX.EXPORT.EXCEP.ID` | `FsGiFundLegalEntityTxnFdTdsk_FxExportExcepId` | TField |  | Unique internal identifier for operation code in scope of fund trading desk. Multifonds DB Column is INTERNAL_ID. |
| 7 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED10` | `FsGiFundLegalEntityTxnFdTdsk_Reserved10` | TField |  |  |
| 8 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED9` | `FsGiFundLegalEntityTxnFdTdsk_Reserved9` | TField |  |  |
| 9 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED8` | `FsGiFundLegalEntityTxnFdTdsk_Reserved8` | TField |  |  |
| 10 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED7` | `FsGiFundLegalEntityTxnFdTdsk_Reserved7` | TField |  |  |
| 11 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED6` | `FsGiFundLegalEntityTxnFdTdsk_Reserved6` | TField |  |  |
| 12 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED5` | `FsGiFundLegalEntityTxnFdTdsk_Reserved5` | TField |  |  |
| 13 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED4` | `FsGiFundLegalEntityTxnFdTdsk_Reserved4` | TField |  |  |
| 14 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED3` | `FsGiFundLegalEntityTxnFdTdsk_Reserved3` | TField |  |  |
| 15 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED2` | `FsGiFundLegalEntityTxnFdTdsk_Reserved2` | TField |  |  |
| 16 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RESERVED1` | `FsGiFundLegalEntityTxnFdTdsk_Reserved1` | TField |  |  |
| 17 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.LOCAL.REF` | `FsGiFundLegalEntityTxnFdTdsk_LocalRef` |  |  |  |
| 18 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.OVERRIDE` | `FsGiFundLegalEntityTxnFdTdsk_Override` |  |  |  |
| 19 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.RECORD.STATUS` | `FsGiFundLegalEntityTxnFdTdsk_RecordStatus` | String |  |  |
| 20 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.CURR.NO` | `FsGiFundLegalEntityTxnFdTdsk_CurrNo` | String |  |  |
| 21 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.INPUTTER` | `FsGiFundLegalEntityTxnFdTdsk_Inputter` |  |  |  |
| 22 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.DATE.TIME` | `FsGiFundLegalEntityTxnFdTdsk_DateTime` |  |  |  |
| 23 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.AUTHORISER` | `FsGiFundLegalEntityTxnFdTdsk_Authoriser` | String |  |  |
| 24 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.CO.CODE` | `FsGiFundLegalEntityTxnFdTdsk_CoCode` | String |  |  |
| 25 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.DEPT.CODE` | `FsGiFundLegalEntityTxnFdTdsk_DeptCode` | String |  |  |
| 26 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.AUDITOR.CODE` | `FsGiFundLegalEntityTxnFdTdsk_AuditorCode` | String |  |  |
| 27 | `FS.GI.FUND.LEGAL.ENTITY.TXN.FD.TDSK.AUDIT.DATE.TIME` | `FsGiFundLegalEntityTxnFdTdsk_AuditDateTime` | String |  |  |
