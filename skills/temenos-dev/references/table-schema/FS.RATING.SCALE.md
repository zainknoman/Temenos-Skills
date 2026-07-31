# FS.RATING.SCALE — Table Schema

> Source: `INSERTS/I_F.FS.RATING.SCALE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.RATING.SCALE.DESCRIPTION` | `FsRatingScale_Description` |  |  |  |
| 2 | `FS.RATING.SCALE.FILTER.KEY` | `FsRatingScale_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.RATING.SCALE.RECORD.ID` | `FsRatingScale_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.RATING.SCALE.RESERVED10` | `FsRatingScale_Reserved10` | TField |  |  |
| 5 | `FS.RATING.SCALE.RESERVED9` | `FsRatingScale_Reserved9` | TField |  |  |
| 6 | `FS.RATING.SCALE.RESERVED8` | `FsRatingScale_Reserved8` | TField |  |  |
| 7 | `FS.RATING.SCALE.RESERVED7` | `FsRatingScale_Reserved7` | TField |  |  |
| 8 | `FS.RATING.SCALE.RESERVED6` | `FsRatingScale_Reserved6` | TField |  |  |
| 9 | `FS.RATING.SCALE.RESERVED5` | `FsRatingScale_Reserved5` | TField |  |  |
| 10 | `FS.RATING.SCALE.RESERVED4` | `FsRatingScale_Reserved4` | TField |  |  |
| 11 | `FS.RATING.SCALE.RESERVED3` | `FsRatingScale_Reserved3` | TField |  |  |
| 12 | `FS.RATING.SCALE.RESERVED2` | `FsRatingScale_Reserved2` | TField |  |  |
| 13 | `FS.RATING.SCALE.RESERVED1` | `FsRatingScale_Reserved1` | TField |  |  |
| 14 | `FS.RATING.SCALE.LOCAL.REF` | `FsRatingScale_LocalRef` |  |  |  |
| 15 | `FS.RATING.SCALE.OVERRIDE` | `FsRatingScale_Override` |  |  |  |
| 16 | `FS.RATING.SCALE.RECORD.STATUS` | `FsRatingScale_RecordStatus` | String |  |  |
| 17 | `FS.RATING.SCALE.CURR.NO` | `FsRatingScale_CurrNo` | String |  |  |
| 18 | `FS.RATING.SCALE.INPUTTER` | `FsRatingScale_Inputter` |  |  |  |
| 19 | `FS.RATING.SCALE.DATE.TIME` | `FsRatingScale_DateTime` |  |  |  |
| 20 | `FS.RATING.SCALE.AUTHORISER` | `FsRatingScale_Authoriser` | String |  |  |
| 21 | `FS.RATING.SCALE.CO.CODE` | `FsRatingScale_CoCode` | String |  |  |
| 22 | `FS.RATING.SCALE.DEPT.CODE` | `FsRatingScale_DeptCode` | String |  |  |
| 23 | `FS.RATING.SCALE.AUDITOR.CODE` | `FsRatingScale_AuditorCode` | String |  |  |
| 24 | `FS.RATING.SCALE.AUDIT.DATE.TIME` | `FsRatingScale_AuditDateTime` | String |  |  |
