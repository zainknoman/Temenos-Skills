# FS.RATING.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.RATING.GROUP` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.RATING.GROUP.DESCRIPTION` | `FsRatingGroup_Description` |  |  |  |
| 2 | `FS.RATING.GROUP.FILTER.KEY` | `FsRatingGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.RATING.GROUP.RECORD.ID` | `FsRatingGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.RATING.GROUP.RESERVED10` | `FsRatingGroup_Reserved10` | TField |  |  |
| 5 | `FS.RATING.GROUP.RESERVED9` | `FsRatingGroup_Reserved9` | TField |  |  |
| 6 | `FS.RATING.GROUP.RESERVED8` | `FsRatingGroup_Reserved8` | TField |  |  |
| 7 | `FS.RATING.GROUP.RESERVED7` | `FsRatingGroup_Reserved7` | TField |  |  |
| 8 | `FS.RATING.GROUP.RESERVED6` | `FsRatingGroup_Reserved6` | TField |  |  |
| 9 | `FS.RATING.GROUP.RESERVED5` | `FsRatingGroup_Reserved5` | TField |  |  |
| 10 | `FS.RATING.GROUP.RESERVED4` | `FsRatingGroup_Reserved4` | TField |  |  |
| 11 | `FS.RATING.GROUP.RESERVED3` | `FsRatingGroup_Reserved3` | TField |  |  |
| 12 | `FS.RATING.GROUP.RESERVED2` | `FsRatingGroup_Reserved2` | TField |  |  |
| 13 | `FS.RATING.GROUP.RESERVED1` | `FsRatingGroup_Reserved1` | TField |  |  |
| 14 | `FS.RATING.GROUP.LOCAL.REF` | `FsRatingGroup_LocalRef` |  |  |  |
| 15 | `FS.RATING.GROUP.OVERRIDE` | `FsRatingGroup_Override` |  |  |  |
| 16 | `FS.RATING.GROUP.RECORD.STATUS` | `FsRatingGroup_RecordStatus` | String |  |  |
| 17 | `FS.RATING.GROUP.CURR.NO` | `FsRatingGroup_CurrNo` | String |  |  |
| 18 | `FS.RATING.GROUP.INPUTTER` | `FsRatingGroup_Inputter` |  |  |  |
| 19 | `FS.RATING.GROUP.DATE.TIME` | `FsRatingGroup_DateTime` |  |  |  |
| 20 | `FS.RATING.GROUP.AUTHORISER` | `FsRatingGroup_Authoriser` | String |  |  |
| 21 | `FS.RATING.GROUP.CO.CODE` | `FsRatingGroup_CoCode` | String |  |  |
| 22 | `FS.RATING.GROUP.DEPT.CODE` | `FsRatingGroup_DeptCode` | String |  |  |
| 23 | `FS.RATING.GROUP.AUDITOR.CODE` | `FsRatingGroup_AuditorCode` | String |  |  |
| 24 | `FS.RATING.GROUP.AUDIT.DATE.TIME` | `FsRatingGroup_AuditDateTime` | String |  |  |
