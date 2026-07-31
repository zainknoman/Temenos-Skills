# FS.GA.EQUIVALENCE.CONTRACT.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCE.CONTRACT.CODE` in `FS_AccountingEquivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.PARENT.REF.ID` | `FsGaEquivalenceContractCode_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.ORA.ROWID` | `FsGaEquivalenceContractCode_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.FUND.ID` | `FsGaEquivalenceContractCode_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.SERVICE.CODE` | `FsGaEquivalenceContractCode_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.EXTERNAL.REFERENCE` | `FsGaEquivalenceContractCode_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 6 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.MULTIFONDS.ENTRY.NUMBER` | `FsGaEquivalenceContractCode_MultifondsEntryNumber` | TField |  | Transaction reference number generated in MultiFonds Multifonds DB Column is NUM_MULTIFONDS. |
| 7 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.DEAL.STATUS.CODE` | `FsGaEquivalenceContractCode_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 8 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.INTERNAL.SECURITY.ID` | `FsGaEquivalenceContractCode_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 9 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.ENTRY.DATE` | `FsGaEquivalenceContractCode_EntryDate` | TField |  | Transaction Entry date Multifonds DB Column is DAT_ECR. |
| 10 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.ARCHIVE` | `FsGaEquivalenceContractCode_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 11 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED10` | `FsGaEquivalenceContractCode_Reserved10` | TField |  |  |
| 12 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED9` | `FsGaEquivalenceContractCode_Reserved9` | TField |  |  |
| 13 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED8` | `FsGaEquivalenceContractCode_Reserved8` | TField |  |  |
| 14 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED7` | `FsGaEquivalenceContractCode_Reserved7` | TField |  |  |
| 15 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED6` | `FsGaEquivalenceContractCode_Reserved6` | TField |  |  |
| 16 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED5` | `FsGaEquivalenceContractCode_Reserved5` | TField |  |  |
| 17 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED4` | `FsGaEquivalenceContractCode_Reserved4` | TField |  |  |
| 18 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED3` | `FsGaEquivalenceContractCode_Reserved3` | TField |  |  |
| 19 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED2` | `FsGaEquivalenceContractCode_Reserved2` | TField |  |  |
| 20 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RESERVED1` | `FsGaEquivalenceContractCode_Reserved1` | TField |  |  |
| 21 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.LOCAL.REF` | `FsGaEquivalenceContractCode_LocalRef` |  |  |  |
| 22 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.OVERRIDE` | `FsGaEquivalenceContractCode_Override` |  |  |  |
| 23 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.RECORD.STATUS` | `FsGaEquivalenceContractCode_RecordStatus` | String |  |  |
| 24 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.CURR.NO` | `FsGaEquivalenceContractCode_CurrNo` | String |  |  |
| 25 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.INPUTTER` | `FsGaEquivalenceContractCode_Inputter` |  |  |  |
| 26 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.DATE.TIME` | `FsGaEquivalenceContractCode_DateTime` |  |  |  |
| 27 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.AUTHORISER` | `FsGaEquivalenceContractCode_Authoriser` | String |  |  |
| 28 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.CO.CODE` | `FsGaEquivalenceContractCode_CoCode` | String |  |  |
| 29 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.DEPT.CODE` | `FsGaEquivalenceContractCode_DeptCode` | String |  |  |
| 30 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.AUDITOR.CODE` | `FsGaEquivalenceContractCode_AuditorCode` | String |  |  |
| 31 | `FS.GA.EQUIVALENCE.CONTRACT.CODE.AUDIT.DATE.TIME` | `FsGaEquivalenceContractCode_AuditDateTime` | String |  |  |
