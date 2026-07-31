# FS.GA.ACCOUNTING.LINK.INTERFACE — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNTING.LINK.INTERFACE` in `FS_AccountingEquivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNTING.LINK.INTERFACE.PARENT.REF.ID` | `FsGaAccountingLinkInterface_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNTING.LINK.INTERFACE.ORA.ROWID` | `FsGaAccountingLinkInterface_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNTING.LINK.INTERFACE.FUND.ID` | `FsGaAccountingLinkInterface_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.ACCOUNTING.LINK.INTERFACE.INTERFACE.PARAM.SERVICE.CODE` | `FsGaAccountingLinkInterface_InterfaceParamServiceCode` | TField |  | Service Code for which correspondent accounts equivalence to be setup Multifonds DB Column is CODE_PKG. |
| 5 | `FS.GA.ACCOUNTING.LINK.INTERFACE.EXTERNAL.CORRESPONDENT.ID` | `FsGaAccountingLinkInterface_ExternalCorrespondentId` | TField |  | External Correspondent ID Multifonds DB Column is NCORR_REP. |
| 6 | `FS.GA.ACCOUNTING.LINK.INTERFACE.REPRISE.ACCOUNT.NUMBER` | `FsGaAccountingLinkInterface_RepriseAccountNumber` | TField |  | Reprise Account Number Multifonds DB Column is NRUBR_REP. |
| 7 | `FS.GA.ACCOUNTING.LINK.INTERFACE.REPRISE.SUFFIX.NUMBER` | `FsGaAccountingLinkInterface_RepriseSuffixNumber` | TField |  | Reprise Suffix Number Multifonds DB Column is NSUFF_REP. |
| 8 | `FS.GA.ACCOUNTING.LINK.INTERFACE.EXTERNAL.HOLDER.ID` | `FsGaAccountingLinkInterface_ExternalHolderId` | TField |  | External Holder ID Multifonds DB Column is NACTIONNAIRE_REP. |
| 9 | `FS.GA.ACCOUNTING.LINK.INTERFACE.EXTERNAL.DEPOSITORY.ID` | `FsGaAccountingLinkInterface_ExternalDepositoryId` | TField |  | External Depository ID Multifonds DB Column is NDEPOSI_REP. |
| 10 | `FS.GA.ACCOUNTING.LINK.INTERFACE.INTERNAL.CORRESPONDENT.ID` | `FsGaAccountingLinkInterface_InternalCorrespondentId` | TField |  | Internal Correspondent ID Multifonds DB Column is NCORR_INT. |
| 11 | `FS.GA.ACCOUNTING.LINK.INTERFACE.GL.ACCOUNT.OF.CONTRACT` | `FsGaAccountingLinkInterface_GlAccountOfContract` | TField |  | Account Number for Contractual Instruments ex. FRAs Multifonds DB Column is NRUBR_INT. |
| 12 | `FS.GA.ACCOUNTING.LINK.INTERFACE.GL.ACCOUNT.SUFFIX.OF.CONTRACT` | `FsGaAccountingLinkInterface_GlAccountSuffixOfContract` | TField |  | Account Number Suffix for Contractual Instruments ex. FRAs Multifonds DB Column is NSUFF_INT. |
| 13 | `FS.GA.ACCOUNTING.LINK.INTERFACE.INTERNAL.HOLDER.ID` | `FsGaAccountingLinkInterface_InternalHolderId` | TField |  | Internal Holder ID Multifonds DB Column is NACTIONNAIRE_INT. |
| 14 | `FS.GA.ACCOUNTING.LINK.INTERFACE.INTERNAL.DEPOSITORY.ID` | `FsGaAccountingLinkInterface_InternalDepositoryId` | TField |  | Internal Depository ID Multifonds DB Column is NDEPOSI_INT. |
| 15 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED10` | `FsGaAccountingLinkInterface_Reserved10` | TField |  |  |
| 16 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED9` | `FsGaAccountingLinkInterface_Reserved9` | TField |  |  |
| 17 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED8` | `FsGaAccountingLinkInterface_Reserved8` | TField |  |  |
| 18 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED7` | `FsGaAccountingLinkInterface_Reserved7` | TField |  |  |
| 19 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED6` | `FsGaAccountingLinkInterface_Reserved6` | TField |  |  |
| 20 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED5` | `FsGaAccountingLinkInterface_Reserved5` | TField |  |  |
| 21 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED4` | `FsGaAccountingLinkInterface_Reserved4` | TField |  |  |
| 22 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED3` | `FsGaAccountingLinkInterface_Reserved3` | TField |  |  |
| 23 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED2` | `FsGaAccountingLinkInterface_Reserved2` | TField |  |  |
| 24 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RESERVED1` | `FsGaAccountingLinkInterface_Reserved1` | TField |  |  |
| 25 | `FS.GA.ACCOUNTING.LINK.INTERFACE.LOCAL.REF` | `FsGaAccountingLinkInterface_LocalRef` |  |  |  |
| 26 | `FS.GA.ACCOUNTING.LINK.INTERFACE.OVERRIDE` | `FsGaAccountingLinkInterface_Override` |  |  |  |
| 27 | `FS.GA.ACCOUNTING.LINK.INTERFACE.RECORD.STATUS` | `FsGaAccountingLinkInterface_RecordStatus` | String |  |  |
| 28 | `FS.GA.ACCOUNTING.LINK.INTERFACE.CURR.NO` | `FsGaAccountingLinkInterface_CurrNo` | String |  |  |
| 29 | `FS.GA.ACCOUNTING.LINK.INTERFACE.INPUTTER` | `FsGaAccountingLinkInterface_Inputter` |  |  |  |
| 30 | `FS.GA.ACCOUNTING.LINK.INTERFACE.DATE.TIME` | `FsGaAccountingLinkInterface_DateTime` |  |  |  |
| 31 | `FS.GA.ACCOUNTING.LINK.INTERFACE.AUTHORISER` | `FsGaAccountingLinkInterface_Authoriser` | String |  |  |
| 32 | `FS.GA.ACCOUNTING.LINK.INTERFACE.CO.CODE` | `FsGaAccountingLinkInterface_CoCode` | String |  |  |
| 33 | `FS.GA.ACCOUNTING.LINK.INTERFACE.DEPT.CODE` | `FsGaAccountingLinkInterface_DeptCode` | String |  |  |
| 34 | `FS.GA.ACCOUNTING.LINK.INTERFACE.AUDITOR.CODE` | `FsGaAccountingLinkInterface_AuditorCode` | String |  |  |
| 35 | `FS.GA.ACCOUNTING.LINK.INTERFACE.AUDIT.DATE.TIME` | `FsGaAccountingLinkInterface_AuditDateTime` | String |  |  |
