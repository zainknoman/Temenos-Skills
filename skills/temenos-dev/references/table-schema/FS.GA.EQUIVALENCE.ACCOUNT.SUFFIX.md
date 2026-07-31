# FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX` in `FS_AccountingEquivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.PARENT.REF.ID` | `FsGaEquivalenceAccountSuffix_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.ORA.ROWID` | `FsGaEquivalenceAccountSuffix_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.EXTERNAL.ACCOUNT.SUFFIX` | `FsGaEquivalenceAccountSuffix_ExternalAccountSuffix` | TField |  | Define the external account number suffix for operation code equivalence. Multifonds DB Column is NSUFF_REPRISE. |
| 4 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.GL.ACCOUNT.SUFFIX` | `FsGaEquivalenceAccountSuffix_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 5 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.FUND.ID` | `FsGaEquivalenceAccountSuffix_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 6 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.DESCRIPTION` | `FsGaEquivalenceAccountSuffix_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED10` | `FsGaEquivalenceAccountSuffix_Reserved10` | TField |  |  |
| 8 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED9` | `FsGaEquivalenceAccountSuffix_Reserved9` | TField |  |  |
| 9 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED8` | `FsGaEquivalenceAccountSuffix_Reserved8` | TField |  |  |
| 10 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED7` | `FsGaEquivalenceAccountSuffix_Reserved7` | TField |  |  |
| 11 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED6` | `FsGaEquivalenceAccountSuffix_Reserved6` | TField |  |  |
| 12 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED5` | `FsGaEquivalenceAccountSuffix_Reserved5` | TField |  |  |
| 13 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED4` | `FsGaEquivalenceAccountSuffix_Reserved4` | TField |  |  |
| 14 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED3` | `FsGaEquivalenceAccountSuffix_Reserved3` | TField |  |  |
| 15 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED2` | `FsGaEquivalenceAccountSuffix_Reserved2` | TField |  |  |
| 16 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RESERVED1` | `FsGaEquivalenceAccountSuffix_Reserved1` | TField |  |  |
| 17 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.LOCAL.REF` | `FsGaEquivalenceAccountSuffix_LocalRef` |  |  |  |
| 18 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.OVERRIDE` | `FsGaEquivalenceAccountSuffix_Override` |  |  |  |
| 19 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.RECORD.STATUS` | `FsGaEquivalenceAccountSuffix_RecordStatus` | String |  |  |
| 20 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.CURR.NO` | `FsGaEquivalenceAccountSuffix_CurrNo` | String |  |  |
| 21 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.INPUTTER` | `FsGaEquivalenceAccountSuffix_Inputter` |  |  |  |
| 22 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.DATE.TIME` | `FsGaEquivalenceAccountSuffix_DateTime` |  |  |  |
| 23 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.AUTHORISER` | `FsGaEquivalenceAccountSuffix_Authoriser` | String |  |  |
| 24 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.CO.CODE` | `FsGaEquivalenceAccountSuffix_CoCode` | String |  |  |
| 25 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.DEPT.CODE` | `FsGaEquivalenceAccountSuffix_DeptCode` | String |  |  |
| 26 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.AUDITOR.CODE` | `FsGaEquivalenceAccountSuffix_AuditorCode` | String |  |  |
| 27 | `FS.GA.EQUIVALENCE.ACCOUNT.SUFFIX.AUDIT.DATE.TIME` | `FsGaEquivalenceAccountSuffix_AuditDateTime` | String |  |  |
