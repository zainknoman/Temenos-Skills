# FS.GA.NAV.VALIDATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.VALIDATION` in `FS_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.VALIDATION.PARENT.REF.ID` | `FsGaNavValidation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.VALIDATION.ORA.ROWID` | `FsGaNavValidation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.VALIDATION.FUND.ID` | `FsGaNavValidation_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.NAV.VALIDATION.INTERNAL.TRANSACTION.ENTRY.NUM` | `FsGaNavValidation_InternalTransactionEntryNum` | TField |  | This is the internal entry number for a transaction. Multifonds DB Column is NECRITURE. |
| 5 | `FS.GA.NAV.VALIDATION.APPLICATION` | `FsGaNavValidation_Application` | TField |  | Define the application for which the setup is applicable Multifonds DB Column is APPLICATION. |
| 6 | `FS.GA.NAV.VALIDATION.PROCESS.GROUP` | `FsGaNavValidation_ProcessGroup` | TField |  | Group of Processes ex. PGXX. Used for executing multiple process at a time. Multifonds DB Column is PROCESS_GRP. |
| 7 | `FS.GA.NAV.VALIDATION.NAV.GROUP.CODE` | `FsGaNavValidation_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 8 | `FS.GA.NAV.VALIDATION.RESERVED10` | `FsGaNavValidation_Reserved10` | TField |  |  |
| 9 | `FS.GA.NAV.VALIDATION.RESERVED9` | `FsGaNavValidation_Reserved9` | TField |  |  |
| 10 | `FS.GA.NAV.VALIDATION.RESERVED8` | `FsGaNavValidation_Reserved8` | TField |  |  |
| 11 | `FS.GA.NAV.VALIDATION.RESERVED7` | `FsGaNavValidation_Reserved7` | TField |  |  |
| 12 | `FS.GA.NAV.VALIDATION.RESERVED6` | `FsGaNavValidation_Reserved6` | TField |  |  |
| 13 | `FS.GA.NAV.VALIDATION.RESERVED5` | `FsGaNavValidation_Reserved5` | TField |  |  |
| 14 | `FS.GA.NAV.VALIDATION.RESERVED4` | `FsGaNavValidation_Reserved4` | TField |  |  |
| 15 | `FS.GA.NAV.VALIDATION.RESERVED3` | `FsGaNavValidation_Reserved3` | TField |  |  |
| 16 | `FS.GA.NAV.VALIDATION.RESERVED2` | `FsGaNavValidation_Reserved2` | TField |  |  |
| 17 | `FS.GA.NAV.VALIDATION.RESERVED1` | `FsGaNavValidation_Reserved1` | TField |  |  |
| 18 | `FS.GA.NAV.VALIDATION.LOCAL.REF` | `FsGaNavValidation_LocalRef` |  |  |  |
| 19 | `FS.GA.NAV.VALIDATION.OVERRIDE` | `FsGaNavValidation_Override` |  |  |  |
| 20 | `FS.GA.NAV.VALIDATION.RECORD.STATUS` | `FsGaNavValidation_RecordStatus` | String |  |  |
| 21 | `FS.GA.NAV.VALIDATION.CURR.NO` | `FsGaNavValidation_CurrNo` | String |  |  |
| 22 | `FS.GA.NAV.VALIDATION.INPUTTER` | `FsGaNavValidation_Inputter` |  |  |  |
| 23 | `FS.GA.NAV.VALIDATION.DATE.TIME` | `FsGaNavValidation_DateTime` |  |  |  |
| 24 | `FS.GA.NAV.VALIDATION.AUTHORISER` | `FsGaNavValidation_Authoriser` | String |  |  |
| 25 | `FS.GA.NAV.VALIDATION.CO.CODE` | `FsGaNavValidation_CoCode` | String |  |  |
| 26 | `FS.GA.NAV.VALIDATION.DEPT.CODE` | `FsGaNavValidation_DeptCode` | String |  |  |
| 27 | `FS.GA.NAV.VALIDATION.AUDITOR.CODE` | `FsGaNavValidation_AuditorCode` | String |  |  |
| 28 | `FS.GA.NAV.VALIDATION.AUDIT.DATE.TIME` | `FsGaNavValidation_AuditDateTime` | String |  |  |
