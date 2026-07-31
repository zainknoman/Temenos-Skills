# FS.GA.EQUIVALENCE.FEE.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCE.FEE.CODE` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUIVALENCE.FEE.CODE.PARENT.REF.ID` | `FsGaEquivalenceFeeCode_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUIVALENCE.FEE.CODE.ORA.ROWID` | `FsGaEquivalenceFeeCode_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUIVALENCE.FEE.CODE.MULTIFONDS.FEES.CODE` | `FsGaEquivalenceFeeCode_MultifondsFeesCode` | TField |  | Enter the Fee Code Multifonds DB Column is CODE_FRAIS. |
| 4 | `FS.GA.EQUIVALENCE.FEE.CODE.SWIFT.CODE` | `FsGaEquivalenceFeeCode_SwiftCode` | TField |  | Swift Code Multifonds DB Column is CODE_SWIFT. |
| 5 | `FS.GA.EQUIVALENCE.FEE.CODE.OP.CODE` | `FsGaEquivalenceFeeCode_OpCode` | TField |  | Enter the operation code Multifonds DB Column is COPER_REPRISE. |
| 6 | `FS.GA.EQUIVALENCE.FEE.CODE.FEES.DESCRIPTION` | `FsGaEquivalenceFeeCode_FeesDescription` | TField |  | Fees Description Multifonds DB Column is XLIBELLE_FRAIS. |
| 7 | `FS.GA.EQUIVALENCE.FEE.CODE.FUND.ID` | `FsGaEquivalenceFeeCode_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 8 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED10` | `FsGaEquivalenceFeeCode_Reserved10` | TField |  |  |
| 9 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED9` | `FsGaEquivalenceFeeCode_Reserved9` | TField |  |  |
| 10 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED8` | `FsGaEquivalenceFeeCode_Reserved8` | TField |  |  |
| 11 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED7` | `FsGaEquivalenceFeeCode_Reserved7` | TField |  |  |
| 12 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED6` | `FsGaEquivalenceFeeCode_Reserved6` | TField |  |  |
| 13 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED5` | `FsGaEquivalenceFeeCode_Reserved5` | TField |  |  |
| 14 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED4` | `FsGaEquivalenceFeeCode_Reserved4` | TField |  |  |
| 15 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED3` | `FsGaEquivalenceFeeCode_Reserved3` | TField |  |  |
| 16 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED2` | `FsGaEquivalenceFeeCode_Reserved2` | TField |  |  |
| 17 | `FS.GA.EQUIVALENCE.FEE.CODE.RESERVED1` | `FsGaEquivalenceFeeCode_Reserved1` | TField |  |  |
| 18 | `FS.GA.EQUIVALENCE.FEE.CODE.LOCAL.REF` | `FsGaEquivalenceFeeCode_LocalRef` |  |  |  |
| 19 | `FS.GA.EQUIVALENCE.FEE.CODE.OVERRIDE` | `FsGaEquivalenceFeeCode_Override` |  |  |  |
| 20 | `FS.GA.EQUIVALENCE.FEE.CODE.RECORD.STATUS` | `FsGaEquivalenceFeeCode_RecordStatus` | String |  |  |
| 21 | `FS.GA.EQUIVALENCE.FEE.CODE.CURR.NO` | `FsGaEquivalenceFeeCode_CurrNo` | String |  |  |
| 22 | `FS.GA.EQUIVALENCE.FEE.CODE.INPUTTER` | `FsGaEquivalenceFeeCode_Inputter` |  |  |  |
| 23 | `FS.GA.EQUIVALENCE.FEE.CODE.DATE.TIME` | `FsGaEquivalenceFeeCode_DateTime` |  |  |  |
| 24 | `FS.GA.EQUIVALENCE.FEE.CODE.AUTHORISER` | `FsGaEquivalenceFeeCode_Authoriser` | String |  |  |
| 25 | `FS.GA.EQUIVALENCE.FEE.CODE.CO.CODE` | `FsGaEquivalenceFeeCode_CoCode` | String |  |  |
| 26 | `FS.GA.EQUIVALENCE.FEE.CODE.DEPT.CODE` | `FsGaEquivalenceFeeCode_DeptCode` | String |  |  |
| 27 | `FS.GA.EQUIVALENCE.FEE.CODE.AUDITOR.CODE` | `FsGaEquivalenceFeeCode_AuditorCode` | String |  |  |
| 28 | `FS.GA.EQUIVALENCE.FEE.CODE.AUDIT.DATE.TIME` | `FsGaEquivalenceFeeCode_AuditDateTime` | String |  |  |
