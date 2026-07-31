# FS.GA.CORRESPONDENT.QUALIFICATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.QUALIFICATION` in `FS_ThirdParties.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORRESPONDENT.QUALIFICATION.PARENT.REF.ID` | `FsGaCorrespondentQualification_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORRESPONDENT.QUALIFICATION.ORA.ROWID` | `FsGaCorrespondentQualification_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORRESPONDENT.QUALIFICATION.CORRESPONDENT` | `FsGaCorrespondentQualification_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.CORRESPONDENT.QUALIFICATION.QUALIFICATION` | `FsGaCorrespondentQualification_Qualification` | TField |  | This field displays different qualifications that can be linked to a correspondent in central register Multifonds DB Column is QUALIFICATION. |
| 5 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED10` | `FsGaCorrespondentQualification_Reserved10` | TField |  |  |
| 6 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED9` | `FsGaCorrespondentQualification_Reserved9` | TField |  |  |
| 7 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED8` | `FsGaCorrespondentQualification_Reserved8` | TField |  |  |
| 8 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED7` | `FsGaCorrespondentQualification_Reserved7` | TField |  |  |
| 9 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED6` | `FsGaCorrespondentQualification_Reserved6` | TField |  |  |
| 10 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED5` | `FsGaCorrespondentQualification_Reserved5` | TField |  |  |
| 11 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED4` | `FsGaCorrespondentQualification_Reserved4` | TField |  |  |
| 12 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED3` | `FsGaCorrespondentQualification_Reserved3` | TField |  |  |
| 13 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED2` | `FsGaCorrespondentQualification_Reserved2` | TField |  |  |
| 14 | `FS.GA.CORRESPONDENT.QUALIFICATION.RESERVED1` | `FsGaCorrespondentQualification_Reserved1` | TField |  |  |
| 15 | `FS.GA.CORRESPONDENT.QUALIFICATION.LOCAL.REF` | `FsGaCorrespondentQualification_LocalRef` |  |  |  |
| 16 | `FS.GA.CORRESPONDENT.QUALIFICATION.OVERRIDE` | `FsGaCorrespondentQualification_Override` |  |  |  |
| 17 | `FS.GA.CORRESPONDENT.QUALIFICATION.RECORD.STATUS` | `FsGaCorrespondentQualification_RecordStatus` | String |  |  |
| 18 | `FS.GA.CORRESPONDENT.QUALIFICATION.CURR.NO` | `FsGaCorrespondentQualification_CurrNo` | String |  |  |
| 19 | `FS.GA.CORRESPONDENT.QUALIFICATION.INPUTTER` | `FsGaCorrespondentQualification_Inputter` |  |  |  |
| 20 | `FS.GA.CORRESPONDENT.QUALIFICATION.DATE.TIME` | `FsGaCorrespondentQualification_DateTime` |  |  |  |
| 21 | `FS.GA.CORRESPONDENT.QUALIFICATION.AUTHORISER` | `FsGaCorrespondentQualification_Authoriser` | String |  |  |
| 22 | `FS.GA.CORRESPONDENT.QUALIFICATION.CO.CODE` | `FsGaCorrespondentQualification_CoCode` | String |  |  |
| 23 | `FS.GA.CORRESPONDENT.QUALIFICATION.DEPT.CODE` | `FsGaCorrespondentQualification_DeptCode` | String |  |  |
| 24 | `FS.GA.CORRESPONDENT.QUALIFICATION.AUDITOR.CODE` | `FsGaCorrespondentQualification_AuditorCode` | String |  |  |
| 25 | `FS.GA.CORRESPONDENT.QUALIFICATION.AUDIT.DATE.TIME` | `FsGaCorrespondentQualification_AuditDateTime` | String |  |  |
