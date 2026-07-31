# FS.GA.CORRESPONDENT.EQUIVALENCES — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.EQUIVALENCES` in `FS_ThirdPartyEquivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORRESPONDENT.EQUIVALENCES.PARENT.REF.ID` | `FsGaCorrespondentEquivalences_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORRESPONDENT.EQUIVALENCES.ORA.ROWID` | `FsGaCorrespondentEquivalences_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORRESPONDENT.EQUIVALENCES.SOURCE.SYSTEM.CORRESPONDENCE` | `FsGaCorrespondentEquivalences_SourceSystemCorrespondence` | TField |  | Source System Correspondence Multifonds DB Column is NCORRESP_REPRISE. |
| 4 | `FS.GA.CORRESPONDENT.EQUIVALENCES.MULTIFONDS.CORRESPONDENCE` | `FsGaCorrespondentEquivalences_MultifondsCorrespondence` | TField |  | Multifonds Correspondence Multifonds DB Column is NCORRESP_MULTIFONDS. |
| 5 | `FS.GA.CORRESPONDENT.EQUIVALENCES.CORRESPONDENT.TYPE` | `FsGaCorrespondentEquivalences_CorrespondentType` | TField |  | Type of correspondent whether broker, manager, custodian. Multifonds DB Column is CTCL. |
| 6 | `FS.GA.CORRESPONDENT.EQUIVALENCES.FUND.ID` | `FsGaCorrespondentEquivalences_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 7 | `FS.GA.CORRESPONDENT.EQUIVALENCES.DESCRIPTION` | `FsGaCorrespondentEquivalences_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 8 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED10` | `FsGaCorrespondentEquivalences_Reserved10` | TField |  |  |
| 9 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED9` | `FsGaCorrespondentEquivalences_Reserved9` | TField |  |  |
| 10 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED8` | `FsGaCorrespondentEquivalences_Reserved8` | TField |  |  |
| 11 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED7` | `FsGaCorrespondentEquivalences_Reserved7` | TField |  |  |
| 12 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED6` | `FsGaCorrespondentEquivalences_Reserved6` | TField |  |  |
| 13 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED5` | `FsGaCorrespondentEquivalences_Reserved5` | TField |  |  |
| 14 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED4` | `FsGaCorrespondentEquivalences_Reserved4` | TField |  |  |
| 15 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED3` | `FsGaCorrespondentEquivalences_Reserved3` | TField |  |  |
| 16 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED2` | `FsGaCorrespondentEquivalences_Reserved2` | TField |  |  |
| 17 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RESERVED1` | `FsGaCorrespondentEquivalences_Reserved1` | TField |  |  |
| 18 | `FS.GA.CORRESPONDENT.EQUIVALENCES.LOCAL.REF` | `FsGaCorrespondentEquivalences_LocalRef` |  |  |  |
| 19 | `FS.GA.CORRESPONDENT.EQUIVALENCES.OVERRIDE` | `FsGaCorrespondentEquivalences_Override` |  |  |  |
| 20 | `FS.GA.CORRESPONDENT.EQUIVALENCES.RECORD.STATUS` | `FsGaCorrespondentEquivalences_RecordStatus` | String |  |  |
| 21 | `FS.GA.CORRESPONDENT.EQUIVALENCES.CURR.NO` | `FsGaCorrespondentEquivalences_CurrNo` | String |  |  |
| 22 | `FS.GA.CORRESPONDENT.EQUIVALENCES.INPUTTER` | `FsGaCorrespondentEquivalences_Inputter` |  |  |  |
| 23 | `FS.GA.CORRESPONDENT.EQUIVALENCES.DATE.TIME` | `FsGaCorrespondentEquivalences_DateTime` |  |  |  |
| 24 | `FS.GA.CORRESPONDENT.EQUIVALENCES.AUTHORISER` | `FsGaCorrespondentEquivalences_Authoriser` | String |  |  |
| 25 | `FS.GA.CORRESPONDENT.EQUIVALENCES.CO.CODE` | `FsGaCorrespondentEquivalences_CoCode` | String |  |  |
| 26 | `FS.GA.CORRESPONDENT.EQUIVALENCES.DEPT.CODE` | `FsGaCorrespondentEquivalences_DeptCode` | String |  |  |
| 27 | `FS.GA.CORRESPONDENT.EQUIVALENCES.AUDITOR.CODE` | `FsGaCorrespondentEquivalences_AuditorCode` | String |  |  |
| 28 | `FS.GA.CORRESPONDENT.EQUIVALENCES.AUDIT.DATE.TIME` | `FsGaCorrespondentEquivalences_AuditDateTime` | String |  |  |
