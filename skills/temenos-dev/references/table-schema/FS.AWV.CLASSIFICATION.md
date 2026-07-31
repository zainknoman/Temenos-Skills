# FS.AWV.CLASSIFICATION — Table Schema

> Source: `INSERTS/I_F.FS.AWV.CLASSIFICATION` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.AWV.CLASSIFICATION.DESCRIPTION` | `FsAwvClassification_Description` |  |  |  |
| 2 | `FS.AWV.CLASSIFICATION.FILTER.KEY` | `FsAwvClassification_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.AWV.CLASSIFICATION.RECORD.ID` | `FsAwvClassification_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.AWV.CLASSIFICATION.RESERVED10` | `FsAwvClassification_Reserved10` | TField |  |  |
| 5 | `FS.AWV.CLASSIFICATION.RESERVED9` | `FsAwvClassification_Reserved9` | TField |  |  |
| 6 | `FS.AWV.CLASSIFICATION.RESERVED8` | `FsAwvClassification_Reserved8` | TField |  |  |
| 7 | `FS.AWV.CLASSIFICATION.RESERVED7` | `FsAwvClassification_Reserved7` | TField |  |  |
| 8 | `FS.AWV.CLASSIFICATION.RESERVED6` | `FsAwvClassification_Reserved6` | TField |  |  |
| 9 | `FS.AWV.CLASSIFICATION.RESERVED5` | `FsAwvClassification_Reserved5` | TField |  |  |
| 10 | `FS.AWV.CLASSIFICATION.RESERVED4` | `FsAwvClassification_Reserved4` | TField |  |  |
| 11 | `FS.AWV.CLASSIFICATION.RESERVED3` | `FsAwvClassification_Reserved3` | TField |  |  |
| 12 | `FS.AWV.CLASSIFICATION.RESERVED2` | `FsAwvClassification_Reserved2` | TField |  |  |
| 13 | `FS.AWV.CLASSIFICATION.RESERVED1` | `FsAwvClassification_Reserved1` | TField |  |  |
| 14 | `FS.AWV.CLASSIFICATION.LOCAL.REF` | `FsAwvClassification_LocalRef` |  |  |  |
| 15 | `FS.AWV.CLASSIFICATION.OVERRIDE` | `FsAwvClassification_Override` |  |  |  |
| 16 | `FS.AWV.CLASSIFICATION.RECORD.STATUS` | `FsAwvClassification_RecordStatus` | String |  |  |
| 17 | `FS.AWV.CLASSIFICATION.CURR.NO` | `FsAwvClassification_CurrNo` | String |  |  |
| 18 | `FS.AWV.CLASSIFICATION.INPUTTER` | `FsAwvClassification_Inputter` |  |  |  |
| 19 | `FS.AWV.CLASSIFICATION.DATE.TIME` | `FsAwvClassification_DateTime` |  |  |  |
| 20 | `FS.AWV.CLASSIFICATION.AUTHORISER` | `FsAwvClassification_Authoriser` | String |  |  |
| 21 | `FS.AWV.CLASSIFICATION.CO.CODE` | `FsAwvClassification_CoCode` | String |  |  |
| 22 | `FS.AWV.CLASSIFICATION.DEPT.CODE` | `FsAwvClassification_DeptCode` | String |  |  |
| 23 | `FS.AWV.CLASSIFICATION.AUDITOR.CODE` | `FsAwvClassification_AuditorCode` | String |  |  |
| 24 | `FS.AWV.CLASSIFICATION.AUDIT.DATE.TIME` | `FsAwvClassification_AuditDateTime` | String |  |  |
