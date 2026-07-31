# FS.GA.EQUIVALENCES.ENTRY.NUMBER — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCES.ENTRY.NUMBER` in `FS_AccountingEquivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.PARENT.REF.ID` | `FsGaEquivalencesEntryNumber_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.ORA.ROWID` | `FsGaEquivalencesEntryNumber_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.FUND.ID` | `FsGaEquivalencesEntryNumber_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.SERVICE.CODE` | `FsGaEquivalencesEntryNumber_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.EXTERNAL.REFERENCE` | `FsGaEquivalencesEntryNumber_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 6 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.MULTIFONDS.ENTRY.NUMBER` | `FsGaEquivalencesEntryNumber_MultifondsEntryNumber` | TField |  | Transaction reference number generated in MultiFonds Multifonds DB Column is NUM_MULTIFONDS. |
| 7 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.DEAL.STATUS.CODE` | `FsGaEquivalencesEntryNumber_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 8 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.ENTRY.DATE` | `FsGaEquivalencesEntryNumber_EntryDate` | TField |  | Transaction Entry date Multifonds DB Column is DAT_ECR. |
| 9 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.SOURCE.SYSTEM.DETAILS` | `FsGaEquivalencesEntryNumber_SourceSystemDetails` | TField |  | Source System Details Multifonds DB Column is REPRISE. |
| 10 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.ARCHIVE` | `FsGaEquivalencesEntryNumber_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 11 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED10` | `FsGaEquivalencesEntryNumber_Reserved10` | TField |  |  |
| 12 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED9` | `FsGaEquivalencesEntryNumber_Reserved9` | TField |  |  |
| 13 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED8` | `FsGaEquivalencesEntryNumber_Reserved8` | TField |  |  |
| 14 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED7` | `FsGaEquivalencesEntryNumber_Reserved7` | TField |  |  |
| 15 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED6` | `FsGaEquivalencesEntryNumber_Reserved6` | TField |  |  |
| 16 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED5` | `FsGaEquivalencesEntryNumber_Reserved5` | TField |  |  |
| 17 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED4` | `FsGaEquivalencesEntryNumber_Reserved4` | TField |  |  |
| 18 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED3` | `FsGaEquivalencesEntryNumber_Reserved3` | TField |  |  |
| 19 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED2` | `FsGaEquivalencesEntryNumber_Reserved2` | TField |  |  |
| 20 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RESERVED1` | `FsGaEquivalencesEntryNumber_Reserved1` | TField |  |  |
| 21 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.LOCAL.REF` | `FsGaEquivalencesEntryNumber_LocalRef` |  |  |  |
| 22 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.OVERRIDE` | `FsGaEquivalencesEntryNumber_Override` |  |  |  |
| 23 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.RECORD.STATUS` | `FsGaEquivalencesEntryNumber_RecordStatus` | String |  |  |
| 24 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.CURR.NO` | `FsGaEquivalencesEntryNumber_CurrNo` | String |  |  |
| 25 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.INPUTTER` | `FsGaEquivalencesEntryNumber_Inputter` |  |  |  |
| 26 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.DATE.TIME` | `FsGaEquivalencesEntryNumber_DateTime` |  |  |  |
| 27 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.AUTHORISER` | `FsGaEquivalencesEntryNumber_Authoriser` | String |  |  |
| 28 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.CO.CODE` | `FsGaEquivalencesEntryNumber_CoCode` | String |  |  |
| 29 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.DEPT.CODE` | `FsGaEquivalencesEntryNumber_DeptCode` | String |  |  |
| 30 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.AUDITOR.CODE` | `FsGaEquivalencesEntryNumber_AuditorCode` | String |  |  |
| 31 | `FS.GA.EQUIVALENCES.ENTRY.NUMBER.AUDIT.DATE.TIME` | `FsGaEquivalencesEntryNumber_AuditDateTime` | String |  |  |
