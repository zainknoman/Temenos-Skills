# FS.RATING.AGENCY — Table Schema

> Source: `INSERTS/I_F.FS.RATING.AGENCY` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.RATING.AGENCY.DESCRIPTION` | `FsRatingAgency_Description` |  |  |  |
| 2 | `FS.RATING.AGENCY.FILTER.KEY` | `FsRatingAgency_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.RATING.AGENCY.RECORD.ID` | `FsRatingAgency_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.RATING.AGENCY.RESERVED10` | `FsRatingAgency_Reserved10` | TField |  |  |
| 5 | `FS.RATING.AGENCY.RESERVED9` | `FsRatingAgency_Reserved9` | TField |  |  |
| 6 | `FS.RATING.AGENCY.RESERVED8` | `FsRatingAgency_Reserved8` | TField |  |  |
| 7 | `FS.RATING.AGENCY.RESERVED7` | `FsRatingAgency_Reserved7` | TField |  |  |
| 8 | `FS.RATING.AGENCY.RESERVED6` | `FsRatingAgency_Reserved6` | TField |  |  |
| 9 | `FS.RATING.AGENCY.RESERVED5` | `FsRatingAgency_Reserved5` | TField |  |  |
| 10 | `FS.RATING.AGENCY.RESERVED4` | `FsRatingAgency_Reserved4` | TField |  |  |
| 11 | `FS.RATING.AGENCY.RESERVED3` | `FsRatingAgency_Reserved3` | TField |  |  |
| 12 | `FS.RATING.AGENCY.RESERVED2` | `FsRatingAgency_Reserved2` | TField |  |  |
| 13 | `FS.RATING.AGENCY.RESERVED1` | `FsRatingAgency_Reserved1` | TField |  |  |
| 14 | `FS.RATING.AGENCY.LOCAL.REF` | `FsRatingAgency_LocalRef` |  |  |  |
| 15 | `FS.RATING.AGENCY.OVERRIDE` | `FsRatingAgency_Override` |  |  |  |
| 16 | `FS.RATING.AGENCY.RECORD.STATUS` | `FsRatingAgency_RecordStatus` | String |  |  |
| 17 | `FS.RATING.AGENCY.CURR.NO` | `FsRatingAgency_CurrNo` | String |  |  |
| 18 | `FS.RATING.AGENCY.INPUTTER` | `FsRatingAgency_Inputter` |  |  |  |
| 19 | `FS.RATING.AGENCY.DATE.TIME` | `FsRatingAgency_DateTime` |  |  |  |
| 20 | `FS.RATING.AGENCY.AUTHORISER` | `FsRatingAgency_Authoriser` | String |  |  |
| 21 | `FS.RATING.AGENCY.CO.CODE` | `FsRatingAgency_CoCode` | String |  |  |
| 22 | `FS.RATING.AGENCY.DEPT.CODE` | `FsRatingAgency_DeptCode` | String |  |  |
| 23 | `FS.RATING.AGENCY.AUDITOR.CODE` | `FsRatingAgency_AuditorCode` | String |  |  |
| 24 | `FS.RATING.AGENCY.AUDIT.DATE.TIME` | `FsRatingAgency_AuditDateTime` | String |  |  |
