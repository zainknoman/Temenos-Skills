# FS.GA.MULTI.LANGUAGE.DESCRIPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.MULTI.LANGUAGE.DESCRIPTION` in `FS_StaticMasterConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.PARENT.REF.ID` | `FsGaMultiLanguageDescription_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.ORA.ROWID` | `FsGaMultiLanguageDescription_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.IDENTIFIER.TYPE` | `FsGaMultiLanguageDescription_IdentifierType` | TField |  | Corresponds to Idenfier Code type like security,Future,option and Industry type Multifonds DB Column is ID_TYPE. |
| 4 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.INSTRUMENT.ID` | `FsGaMultiLanguageDescription_InstrumentId` | TField |  | Security Identifier Multifonds DB Column is ID_NO. |
| 5 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.LANGUAGE` | `FsGaMultiLanguageDescription_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 6 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.DESC` | `FsGaMultiLanguageDescription_Desc` | TField |  | Description of the security Multifonds DB Column is DESCR. |
| 7 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.SECURITY.LONG.DESCRIPTION` | `FsGaMultiLanguageDescription_SecurityLongDescription` | TField |  | Enter or modify the short description in the default language. Multifonds DB Column is DESCR_LONG. |
| 8 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.SPECIFIC.DESCRIPTION` | `FsGaMultiLanguageDescription_SpecificDescription` | TField |  | Specific description as mentioned in the FDSEC15 screen used in relation with the specific share class description functionality. Multifonds DB Column is DESCR_SPEC. |
| 9 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED10` | `FsGaMultiLanguageDescription_Reserved10` | TField |  |  |
| 10 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED9` | `FsGaMultiLanguageDescription_Reserved9` | TField |  |  |
| 11 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED8` | `FsGaMultiLanguageDescription_Reserved8` | TField |  |  |
| 12 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED7` | `FsGaMultiLanguageDescription_Reserved7` | TField |  |  |
| 13 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED6` | `FsGaMultiLanguageDescription_Reserved6` | TField |  |  |
| 14 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED5` | `FsGaMultiLanguageDescription_Reserved5` | TField |  |  |
| 15 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED4` | `FsGaMultiLanguageDescription_Reserved4` | TField |  |  |
| 16 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED3` | `FsGaMultiLanguageDescription_Reserved3` | TField |  |  |
| 17 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED2` | `FsGaMultiLanguageDescription_Reserved2` | TField |  |  |
| 18 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RESERVED1` | `FsGaMultiLanguageDescription_Reserved1` | TField |  |  |
| 19 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.LOCAL.REF` | `FsGaMultiLanguageDescription_LocalRef` |  |  |  |
| 20 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.OVERRIDE` | `FsGaMultiLanguageDescription_Override` |  |  |  |
| 21 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.RECORD.STATUS` | `FsGaMultiLanguageDescription_RecordStatus` | String |  |  |
| 22 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.CURR.NO` | `FsGaMultiLanguageDescription_CurrNo` | String |  |  |
| 23 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.INPUTTER` | `FsGaMultiLanguageDescription_Inputter` |  |  |  |
| 24 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.DATE.TIME` | `FsGaMultiLanguageDescription_DateTime` |  |  |  |
| 25 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.AUTHORISER` | `FsGaMultiLanguageDescription_Authoriser` | String |  |  |
| 26 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.CO.CODE` | `FsGaMultiLanguageDescription_CoCode` | String |  |  |
| 27 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.DEPT.CODE` | `FsGaMultiLanguageDescription_DeptCode` | String |  |  |
| 28 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.AUDITOR.CODE` | `FsGaMultiLanguageDescription_AuditorCode` | String |  |  |
| 29 | `FS.GA.MULTI.LANGUAGE.DESCRIPTION.AUDIT.DATE.TIME` | `FsGaMultiLanguageDescription_AuditDateTime` | String |  |  |
