# FS.GA.SECURITY.RATING.LOOKUP — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.RATING.LOOKUP` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.RATING.LOOKUP.AGENCY.CODE` | `FsGaSecurityRatingLookup_AgencyCode` | TField |  | Rating Agency Code Multifonds DB Column is AGENCY_CODE. |
| 2 | `FS.GA.SECURITY.RATING.LOOKUP.AGENCY.DESCRIPTION` | `FsGaSecurityRatingLookup_AgencyDescription` | TField |  | Agency Description Multifonds DB Column is AGENCY_DESC. |
| 3 | `FS.GA.SECURITY.RATING.LOOKUP.RATING.SCALE.CODE` | `FsGaSecurityRatingLookup_RatingScaleCode` | TField |  | Rating Scale Code Multifonds DB Column is RATE_SCALE_CODE. |
| 4 | `FS.GA.SECURITY.RATING.LOOKUP.RATING.SCALE.DESCRIPTION` | `FsGaSecurityRatingLookup_RatingScaleDescription` | TField |  | Rating Scale Description Multifonds DB Column is SCALE_DESC. |
| 5 | `FS.GA.SECURITY.RATING.LOOKUP.RATING.VALUE` | `FsGaSecurityRatingLookup_RatingValue` | TField |  | Rating Value Multifonds DB Column is RATE_VALUE. |
| 6 | `FS.GA.SECURITY.RATING.LOOKUP.RANK` | `FsGaSecurityRatingLookup_Rank` | TField |  | Ranking Order Multifonds DB Column is RANK. |
| 7 | `FS.GA.SECURITY.RATING.LOOKUP.REPORT.GROUP.CODE` | `FsGaSecurityRatingLookup_ReportGroupCode` | TField |  | This field represents report group code as defined in the "GROUP_RATE" table under CMESS for the selected agency code Multifonds DB Column is REP_GRP_CODE. |
| 8 | `FS.GA.SECURITY.RATING.LOOKUP.REPORT.GROUP.DESCRIPTION` | `FsGaSecurityRatingLookup_ReportGroupDescription` | TField |  | This field displays the long description of Rating group maintained in CMESS table Multifonds DB Column is REP_GRP_DESC. |
| 9 | `FS.GA.SECURITY.RATING.LOOKUP.MANDATORY` | `FsGaSecurityRatingLookup_Mandatory` | TField | Yes | Allows defining a process/step as mandatory or not. Multifonds DB Column is MANDATORY. |
| 10 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED10` | `FsGaSecurityRatingLookup_Reserved10` | TField |  |  |
| 11 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED9` | `FsGaSecurityRatingLookup_Reserved9` | TField |  |  |
| 12 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED8` | `FsGaSecurityRatingLookup_Reserved8` | TField |  |  |
| 13 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED7` | `FsGaSecurityRatingLookup_Reserved7` | TField |  |  |
| 14 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED6` | `FsGaSecurityRatingLookup_Reserved6` | TField |  |  |
| 15 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED5` | `FsGaSecurityRatingLookup_Reserved5` | TField |  |  |
| 16 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED4` | `FsGaSecurityRatingLookup_Reserved4` | TField |  |  |
| 17 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED3` | `FsGaSecurityRatingLookup_Reserved3` | TField |  |  |
| 18 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED2` | `FsGaSecurityRatingLookup_Reserved2` | TField |  |  |
| 19 | `FS.GA.SECURITY.RATING.LOOKUP.RESERVED1` | `FsGaSecurityRatingLookup_Reserved1` | TField |  |  |
| 20 | `FS.GA.SECURITY.RATING.LOOKUP.RECORD.STATUS` | `FsGaSecurityRatingLookup_RecordStatus` | String |  |  |
| 21 | `FS.GA.SECURITY.RATING.LOOKUP.CURR.NO` | `FsGaSecurityRatingLookup_CurrNo` | String |  |  |
| 22 | `FS.GA.SECURITY.RATING.LOOKUP.INPUTTER` | `FsGaSecurityRatingLookup_Inputter` |  |  |  |
| 23 | `FS.GA.SECURITY.RATING.LOOKUP.DATE.TIME` | `FsGaSecurityRatingLookup_DateTime` |  |  |  |
| 24 | `FS.GA.SECURITY.RATING.LOOKUP.AUTHORISER` | `FsGaSecurityRatingLookup_Authoriser` | String |  |  |
| 25 | `FS.GA.SECURITY.RATING.LOOKUP.CO.CODE` | `FsGaSecurityRatingLookup_CoCode` | String |  |  |
| 26 | `FS.GA.SECURITY.RATING.LOOKUP.DEPT.CODE` | `FsGaSecurityRatingLookup_DeptCode` | String |  |  |
| 27 | `FS.GA.SECURITY.RATING.LOOKUP.AUDITOR.CODE` | `FsGaSecurityRatingLookup_AuditorCode` | String |  |  |
| 28 | `FS.GA.SECURITY.RATING.LOOKUP.AUDIT.DATE.TIME` | `FsGaSecurityRatingLookup_AuditDateTime` | String |  |  |
