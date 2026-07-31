# FS.GA.GROUP.RATING — Table Schema

> Source: `INSERTS/I_F.FS.GA.GROUP.RATING` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.GROUP.RATING.RATING.FOR.SHORT` | `FsGaGroupRating_RatingForShort` | TField |  | Rating For Short Multifonds DB Column is CRATING_S. |
| 2 | `FS.GA.GROUP.RATING.RATING.TYPE.FOR.SHORT` | `FsGaGroupRating_RatingTypeForShort` | TField |  | Rating Type For Short Multifonds DB Column is TYP_RATING_S. |
| 3 | `FS.GA.GROUP.RATING.RATING.FOR.LONG` | `FsGaGroupRating_RatingForLong` | TField |  | Rating For Long Multifonds DB Column is CRATING_L. |
| 4 | `FS.GA.GROUP.RATING.RATING.TYPE.FOR.LONG` | `FsGaGroupRating_RatingTypeForLong` | TField |  | Rating Type For Long Multifonds DB Column is TYP_RATING_L. |
| 5 | `FS.GA.GROUP.RATING.GROUP.RATING` | `FsGaGroupRating_GroupRating` | TField |  | Group Rating Multifonds DB Column is CGROUPE_RATING. |
| 6 | `FS.GA.GROUP.RATING.RESERVED10` | `FsGaGroupRating_Reserved10` | TField |  |  |
| 7 | `FS.GA.GROUP.RATING.RESERVED9` | `FsGaGroupRating_Reserved9` | TField |  |  |
| 8 | `FS.GA.GROUP.RATING.RESERVED8` | `FsGaGroupRating_Reserved8` | TField |  |  |
| 9 | `FS.GA.GROUP.RATING.RESERVED7` | `FsGaGroupRating_Reserved7` | TField |  |  |
| 10 | `FS.GA.GROUP.RATING.RESERVED6` | `FsGaGroupRating_Reserved6` | TField |  |  |
| 11 | `FS.GA.GROUP.RATING.RESERVED5` | `FsGaGroupRating_Reserved5` | TField |  |  |
| 12 | `FS.GA.GROUP.RATING.RESERVED4` | `FsGaGroupRating_Reserved4` | TField |  |  |
| 13 | `FS.GA.GROUP.RATING.RESERVED3` | `FsGaGroupRating_Reserved3` | TField |  |  |
| 14 | `FS.GA.GROUP.RATING.RESERVED2` | `FsGaGroupRating_Reserved2` | TField |  |  |
| 15 | `FS.GA.GROUP.RATING.RESERVED1` | `FsGaGroupRating_Reserved1` | TField |  |  |
| 16 | `FS.GA.GROUP.RATING.RECORD.STATUS` | `FsGaGroupRating_RecordStatus` | String |  |  |
| 17 | `FS.GA.GROUP.RATING.CURR.NO` | `FsGaGroupRating_CurrNo` | String |  |  |
| 18 | `FS.GA.GROUP.RATING.INPUTTER` | `FsGaGroupRating_Inputter` |  |  |  |
| 19 | `FS.GA.GROUP.RATING.DATE.TIME` | `FsGaGroupRating_DateTime` |  |  |  |
| 20 | `FS.GA.GROUP.RATING.AUTHORISER` | `FsGaGroupRating_Authoriser` | String |  |  |
| 21 | `FS.GA.GROUP.RATING.CO.CODE` | `FsGaGroupRating_CoCode` | String |  |  |
| 22 | `FS.GA.GROUP.RATING.DEPT.CODE` | `FsGaGroupRating_DeptCode` | String |  |  |
| 23 | `FS.GA.GROUP.RATING.AUDITOR.CODE` | `FsGaGroupRating_AuditorCode` | String |  |  |
| 24 | `FS.GA.GROUP.RATING.AUDIT.DATE.TIME` | `FsGaGroupRating_AuditDateTime` | String |  |  |
