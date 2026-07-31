# FS.GA.CORRESPONDENT.IDENTIFICATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.IDENTIFICATION` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORRESPONDENT.IDENTIFICATION.PARENT.REF.ID` | `FsGaCorrespondentIdentification_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORRESPONDENT.IDENTIFICATION.ORA.ROWID` | `FsGaCorrespondentIdentification_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORRESPONDENT.IDENTIFICATION.CORRESPONDENT` | `FsGaCorrespondentIdentification_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.CORRESPONDENT.IDENTIFICATION.ID.CODE` | `FsGaCorrespondentIdentification_IdCode` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 5 | `FS.GA.CORRESPONDENT.IDENTIFICATION.CORRESPONDENT.ID` | `FsGaCorrespondentIdentification_CorrespondentId` | TField |  | External ID of Correspondant. Example for BIC code or for several other external reporting purpose. Multifonds DB Column is COR_ID. |
| 6 | `FS.GA.CORRESPONDENT.IDENTIFICATION.CORRESPONDENT.SHORT.NAME` | `FsGaCorrespondentIdentification_CorrespondentShortName` | TField |  | Specify short name of correspondant ID. Multifonds DB Column is SHORT_ID. |
| 7 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED10` | `FsGaCorrespondentIdentification_Reserved10` | TField |  |  |
| 8 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED9` | `FsGaCorrespondentIdentification_Reserved9` | TField |  |  |
| 9 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED8` | `FsGaCorrespondentIdentification_Reserved8` | TField |  |  |
| 10 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED7` | `FsGaCorrespondentIdentification_Reserved7` | TField |  |  |
| 11 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED6` | `FsGaCorrespondentIdentification_Reserved6` | TField |  |  |
| 12 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED5` | `FsGaCorrespondentIdentification_Reserved5` | TField |  |  |
| 13 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED4` | `FsGaCorrespondentIdentification_Reserved4` | TField |  |  |
| 14 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED3` | `FsGaCorrespondentIdentification_Reserved3` | TField |  |  |
| 15 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED2` | `FsGaCorrespondentIdentification_Reserved2` | TField |  |  |
| 16 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RESERVED1` | `FsGaCorrespondentIdentification_Reserved1` | TField |  |  |
| 17 | `FS.GA.CORRESPONDENT.IDENTIFICATION.LOCAL.REF` | `FsGaCorrespondentIdentification_LocalRef` |  |  |  |
| 18 | `FS.GA.CORRESPONDENT.IDENTIFICATION.OVERRIDE` | `FsGaCorrespondentIdentification_Override` |  |  |  |
| 19 | `FS.GA.CORRESPONDENT.IDENTIFICATION.RECORD.STATUS` | `FsGaCorrespondentIdentification_RecordStatus` | String |  |  |
| 20 | `FS.GA.CORRESPONDENT.IDENTIFICATION.CURR.NO` | `FsGaCorrespondentIdentification_CurrNo` | String |  |  |
| 21 | `FS.GA.CORRESPONDENT.IDENTIFICATION.INPUTTER` | `FsGaCorrespondentIdentification_Inputter` |  |  |  |
| 22 | `FS.GA.CORRESPONDENT.IDENTIFICATION.DATE.TIME` | `FsGaCorrespondentIdentification_DateTime` |  |  |  |
| 23 | `FS.GA.CORRESPONDENT.IDENTIFICATION.AUTHORISER` | `FsGaCorrespondentIdentification_Authoriser` | String |  |  |
| 24 | `FS.GA.CORRESPONDENT.IDENTIFICATION.CO.CODE` | `FsGaCorrespondentIdentification_CoCode` | String |  |  |
| 25 | `FS.GA.CORRESPONDENT.IDENTIFICATION.DEPT.CODE` | `FsGaCorrespondentIdentification_DeptCode` | String |  |  |
| 26 | `FS.GA.CORRESPONDENT.IDENTIFICATION.AUDITOR.CODE` | `FsGaCorrespondentIdentification_AuditorCode` | String |  |  |
| 27 | `FS.GA.CORRESPONDENT.IDENTIFICATION.AUDIT.DATE.TIME` | `FsGaCorrespondentIdentification_AuditDateTime` | String |  |  |
