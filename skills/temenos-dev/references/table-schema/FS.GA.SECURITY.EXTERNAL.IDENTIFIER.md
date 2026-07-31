# FS.GA.SECURITY.EXTERNAL.IDENTIFIER — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.EXTERNAL.IDENTIFIER` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.PARENT.REF.ID` | `FsGaSecurityExternalIdentifier_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.ORA.ROWID` | `FsGaSecurityExternalIdentifier_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.INTERNAL.SECURITY.ID` | `FsGaSecurityExternalIdentifier_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.ID.CODE` | `FsGaSecurityExternalIdentifier_IdCode` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 5 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.EXTERNAL.SECURITY.ID` | `FsGaSecurityExternalIdentifier_ExternalSecurityId` | TField |  | The External identification code for Security like 01 for Telekurs, 03 for Sedol. Also used for other provider identifiers Multifonds DB Column is SEC_ID. |
| 6 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.IDENTIFIER.TYPE` | `FsGaSecurityExternalIdentifier_IdentifierType` | TField |  | Corresponds to Idenfier Code type like security,Future,option and Industry type Multifonds DB Column is ID_TYPE. |
| 7 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.REAL.EXPORT` | `FsGaSecurityExternalIdentifier_RealExport` | TField |  | Real Export Multifonds DB Column is REAL_EXPORT. |
| 8 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED10` | `FsGaSecurityExternalIdentifier_Reserved10` | TField |  |  |
| 9 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED9` | `FsGaSecurityExternalIdentifier_Reserved9` | TField |  |  |
| 10 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED8` | `FsGaSecurityExternalIdentifier_Reserved8` | TField |  |  |
| 11 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED7` | `FsGaSecurityExternalIdentifier_Reserved7` | TField |  |  |
| 12 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED6` | `FsGaSecurityExternalIdentifier_Reserved6` | TField |  |  |
| 13 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED5` | `FsGaSecurityExternalIdentifier_Reserved5` | TField |  |  |
| 14 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED4` | `FsGaSecurityExternalIdentifier_Reserved4` | TField |  |  |
| 15 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED3` | `FsGaSecurityExternalIdentifier_Reserved3` | TField |  |  |
| 16 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED2` | `FsGaSecurityExternalIdentifier_Reserved2` | TField |  |  |
| 17 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RESERVED1` | `FsGaSecurityExternalIdentifier_Reserved1` | TField |  |  |
| 18 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.LOCAL.REF` | `FsGaSecurityExternalIdentifier_LocalRef` |  |  |  |
| 19 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.OVERRIDE` | `FsGaSecurityExternalIdentifier_Override` |  |  |  |
| 20 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.RECORD.STATUS` | `FsGaSecurityExternalIdentifier_RecordStatus` | String |  |  |
| 21 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.CURR.NO` | `FsGaSecurityExternalIdentifier_CurrNo` | String |  |  |
| 22 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.INPUTTER` | `FsGaSecurityExternalIdentifier_Inputter` |  |  |  |
| 23 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.DATE.TIME` | `FsGaSecurityExternalIdentifier_DateTime` |  |  |  |
| 24 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.AUTHORISER` | `FsGaSecurityExternalIdentifier_Authoriser` | String |  |  |
| 25 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.CO.CODE` | `FsGaSecurityExternalIdentifier_CoCode` | String |  |  |
| 26 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.DEPT.CODE` | `FsGaSecurityExternalIdentifier_DeptCode` | String |  |  |
| 27 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.AUDITOR.CODE` | `FsGaSecurityExternalIdentifier_AuditorCode` | String |  |  |
| 28 | `FS.GA.SECURITY.EXTERNAL.IDENTIFIER.AUDIT.DATE.TIME` | `FsGaSecurityExternalIdentifier_AuditDateTime` | String |  |  |
