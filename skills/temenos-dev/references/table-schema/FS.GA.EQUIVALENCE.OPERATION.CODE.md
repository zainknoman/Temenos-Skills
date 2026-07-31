# FS.GA.EQUIVALENCE.OPERATION.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCE.OPERATION.CODE` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUIVALENCE.OPERATION.CODE.PARENT.REF.ID` | `FsGaEquivalenceOperationCode_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUIVALENCE.OPERATION.CODE.ORA.ROWID` | `FsGaEquivalenceOperationCode_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUIVALENCE.OPERATION.CODE.OPERATION.CODE` | `FsGaEquivalenceOperationCode_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 4 | `FS.GA.EQUIVALENCE.OPERATION.CODE.OPERATION.CODES.EQUIVALENCE` | `FsGaEquivalenceOperationCode_OperationCodesEquivalence` | TField |  | Equivalence of the operation codes Multifonds DB Column is EQUI_COPER. |
| 5 | `FS.GA.EQUIVALENCE.OPERATION.CODE.FUND.ID` | `FsGaEquivalenceOperationCode_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 6 | `FS.GA.EQUIVALENCE.OPERATION.CODE.REVISED.OPERATION.CODE` | `FsGaEquivalenceOperationCode_RevisedOperationCode` | TField |  | Revised operation code Multifonds DB Column is REV_EQUI_COPER. |
| 7 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED10` | `FsGaEquivalenceOperationCode_Reserved10` | TField |  |  |
| 8 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED9` | `FsGaEquivalenceOperationCode_Reserved9` | TField |  |  |
| 9 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED8` | `FsGaEquivalenceOperationCode_Reserved8` | TField |  |  |
| 10 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED7` | `FsGaEquivalenceOperationCode_Reserved7` | TField |  |  |
| 11 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED6` | `FsGaEquivalenceOperationCode_Reserved6` | TField |  |  |
| 12 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED5` | `FsGaEquivalenceOperationCode_Reserved5` | TField |  |  |
| 13 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED4` | `FsGaEquivalenceOperationCode_Reserved4` | TField |  |  |
| 14 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED3` | `FsGaEquivalenceOperationCode_Reserved3` | TField |  |  |
| 15 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED2` | `FsGaEquivalenceOperationCode_Reserved2` | TField |  |  |
| 16 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RESERVED1` | `FsGaEquivalenceOperationCode_Reserved1` | TField |  |  |
| 17 | `FS.GA.EQUIVALENCE.OPERATION.CODE.LOCAL.REF` | `FsGaEquivalenceOperationCode_LocalRef` |  |  |  |
| 18 | `FS.GA.EQUIVALENCE.OPERATION.CODE.OVERRIDE` | `FsGaEquivalenceOperationCode_Override` |  |  |  |
| 19 | `FS.GA.EQUIVALENCE.OPERATION.CODE.RECORD.STATUS` | `FsGaEquivalenceOperationCode_RecordStatus` | String |  |  |
| 20 | `FS.GA.EQUIVALENCE.OPERATION.CODE.CURR.NO` | `FsGaEquivalenceOperationCode_CurrNo` | String |  |  |
| 21 | `FS.GA.EQUIVALENCE.OPERATION.CODE.INPUTTER` | `FsGaEquivalenceOperationCode_Inputter` |  |  |  |
| 22 | `FS.GA.EQUIVALENCE.OPERATION.CODE.DATE.TIME` | `FsGaEquivalenceOperationCode_DateTime` |  |  |  |
| 23 | `FS.GA.EQUIVALENCE.OPERATION.CODE.AUTHORISER` | `FsGaEquivalenceOperationCode_Authoriser` | String |  |  |
| 24 | `FS.GA.EQUIVALENCE.OPERATION.CODE.CO.CODE` | `FsGaEquivalenceOperationCode_CoCode` | String |  |  |
| 25 | `FS.GA.EQUIVALENCE.OPERATION.CODE.DEPT.CODE` | `FsGaEquivalenceOperationCode_DeptCode` | String |  |  |
| 26 | `FS.GA.EQUIVALENCE.OPERATION.CODE.AUDITOR.CODE` | `FsGaEquivalenceOperationCode_AuditorCode` | String |  |  |
| 27 | `FS.GA.EQUIVALENCE.OPERATION.CODE.AUDIT.DATE.TIME` | `FsGaEquivalenceOperationCode_AuditDateTime` | String |  |  |
