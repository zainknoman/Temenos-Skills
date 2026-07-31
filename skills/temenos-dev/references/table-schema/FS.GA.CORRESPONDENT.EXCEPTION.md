# FS.GA.CORRESPONDENT.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.EXCEPTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORRESPONDENT.EXCEPTION.PARENT.REF.ID` | `FsGaCorrespondentException_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORRESPONDENT.EXCEPTION.ORA.ROWID` | `FsGaCorrespondentException_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORRESPONDENT.EXCEPTION.CORRESPONDENT` | `FsGaCorrespondentException_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.CORRESPONDENT.EXCEPTION.GTI.CODE` | `FsGaCorrespondentException_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 5 | `FS.GA.CORRESPONDENT.EXCEPTION.MARGIN.ACCOUNT.NUMBER` | `FsGaCorrespondentException_MarginAccountNumber` | TField |  | Future margin account number Multifonds DB Column is NRUBR_MARG. |
| 6 | `FS.GA.CORRESPONDENT.EXCEPTION.MARGIN.SUFFIX.NUMBER` | `FsGaCorrespondentException_MarginSuffixNumber` | TField |  | Future margin account suffix number Multifonds DB Column is NSUFF_MARG. |
| 7 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED10` | `FsGaCorrespondentException_Reserved10` | TField |  |  |
| 8 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED9` | `FsGaCorrespondentException_Reserved9` | TField |  |  |
| 9 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED8` | `FsGaCorrespondentException_Reserved8` | TField |  |  |
| 10 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED7` | `FsGaCorrespondentException_Reserved7` | TField |  |  |
| 11 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED6` | `FsGaCorrespondentException_Reserved6` | TField |  |  |
| 12 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED5` | `FsGaCorrespondentException_Reserved5` | TField |  |  |
| 13 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED4` | `FsGaCorrespondentException_Reserved4` | TField |  |  |
| 14 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED3` | `FsGaCorrespondentException_Reserved3` | TField |  |  |
| 15 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED2` | `FsGaCorrespondentException_Reserved2` | TField |  |  |
| 16 | `FS.GA.CORRESPONDENT.EXCEPTION.RESERVED1` | `FsGaCorrespondentException_Reserved1` | TField |  |  |
| 17 | `FS.GA.CORRESPONDENT.EXCEPTION.LOCAL.REF` | `FsGaCorrespondentException_LocalRef` |  |  |  |
| 18 | `FS.GA.CORRESPONDENT.EXCEPTION.OVERRIDE` | `FsGaCorrespondentException_Override` |  |  |  |
| 19 | `FS.GA.CORRESPONDENT.EXCEPTION.RECORD.STATUS` | `FsGaCorrespondentException_RecordStatus` | String |  |  |
| 20 | `FS.GA.CORRESPONDENT.EXCEPTION.CURR.NO` | `FsGaCorrespondentException_CurrNo` | String |  |  |
| 21 | `FS.GA.CORRESPONDENT.EXCEPTION.INPUTTER` | `FsGaCorrespondentException_Inputter` |  |  |  |
| 22 | `FS.GA.CORRESPONDENT.EXCEPTION.DATE.TIME` | `FsGaCorrespondentException_DateTime` |  |  |  |
| 23 | `FS.GA.CORRESPONDENT.EXCEPTION.AUTHORISER` | `FsGaCorrespondentException_Authoriser` | String |  |  |
| 24 | `FS.GA.CORRESPONDENT.EXCEPTION.CO.CODE` | `FsGaCorrespondentException_CoCode` | String |  |  |
| 25 | `FS.GA.CORRESPONDENT.EXCEPTION.DEPT.CODE` | `FsGaCorrespondentException_DeptCode` | String |  |  |
| 26 | `FS.GA.CORRESPONDENT.EXCEPTION.AUDITOR.CODE` | `FsGaCorrespondentException_AuditorCode` | String |  |  |
| 27 | `FS.GA.CORRESPONDENT.EXCEPTION.AUDIT.DATE.TIME` | `FsGaCorrespondentException_AuditDateTime` | String |  |  |
