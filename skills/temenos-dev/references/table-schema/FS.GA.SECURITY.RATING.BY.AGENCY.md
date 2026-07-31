# FS.GA.SECURITY.RATING.BY.AGENCY — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.RATING.BY.AGENCY` in `FS_SecurityMasterMarketData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.RATING.BY.AGENCY.PARENT.REF.ID` | `FsGaSecurityRatingByAgency_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SECURITY.RATING.BY.AGENCY.ORA.ROWID` | `FsGaSecurityRatingByAgency_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SECURITY.RATING.BY.AGENCY.INTERNAL.SECURITY.ID` | `FsGaSecurityRatingByAgency_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.SECURITY.RATING.BY.AGENCY.SECURITY.DESCRIPTION` | `FsGaSecurityRatingByAgency_SecurityDescription` | TField |  | Description of security Multifonds DB Column is NOMVAL. |
| 5 | `FS.GA.SECURITY.RATING.BY.AGENCY.ID.CODE` | `FsGaSecurityRatingByAgency_IdCode` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 6 | `FS.GA.SECURITY.RATING.BY.AGENCY.EXTERNAL.SEC.ID` | `FsGaSecurityRatingByAgency_ExternalSecId` | TField |  | External Security Id Multifonds DB Column is EXT_SEC_ID. |
| 7 | `FS.GA.SECURITY.RATING.BY.AGENCY.AGENCY.CODE` | `FsGaSecurityRatingByAgency_AgencyCode` | TField |  | Rating Agency Code Multifonds DB Column is AGENCY_CODE. |
| 8 | `FS.GA.SECURITY.RATING.BY.AGENCY.AGENCY.DESCRIPTION` | `FsGaSecurityRatingByAgency_AgencyDescription` | TField |  | Agency Description Multifonds DB Column is AGENCY_DESC. |
| 9 | `FS.GA.SECURITY.RATING.BY.AGENCY.EFFECTIVE.DATES` | `FsGaSecurityRatingByAgency_EffectiveDates` | TField |  | Effective Dates Multifonds DB Column is EFFECT_DATE. |
| 10 | `FS.GA.SECURITY.RATING.BY.AGENCY.RATING.SCALE.CODE` | `FsGaSecurityRatingByAgency_RatingScaleCode` | TField |  | Rating Scale Code Multifonds DB Column is RATE_SCALE_CODE. |
| 11 | `FS.GA.SECURITY.RATING.BY.AGENCY.RATING.SCALE.DESCRIPTION` | `FsGaSecurityRatingByAgency_RatingScaleDescription` | TField |  | Rating Scale Description Multifonds DB Column is SCALE_DESC. |
| 12 | `FS.GA.SECURITY.RATING.BY.AGENCY.RATING.VALUE` | `FsGaSecurityRatingByAgency_RatingValue` | TField |  | Rating Value Multifonds DB Column is RATE_VALUE. |
| 13 | `FS.GA.SECURITY.RATING.BY.AGENCY.SHORT.DESC` | `FsGaSecurityRatingByAgency_ShortDesc` | TField |  | This can be used to provide a Short description of the fields like security,Ctable,Account Group etc. Multifonds DB Column is ABREGE. |
| 14 | `FS.GA.SECURITY.RATING.BY.AGENCY.ENHANCED.YIELD` | `FsGaSecurityRatingByAgency_EnhancedYield` | TField |  | Enhanced Yield Multifonds DB Column is FLG_ENH_YLD. |
| 15 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED10` | `FsGaSecurityRatingByAgency_Reserved10` | TField |  |  |
| 16 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED9` | `FsGaSecurityRatingByAgency_Reserved9` | TField |  |  |
| 17 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED8` | `FsGaSecurityRatingByAgency_Reserved8` | TField |  |  |
| 18 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED7` | `FsGaSecurityRatingByAgency_Reserved7` | TField |  |  |
| 19 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED6` | `FsGaSecurityRatingByAgency_Reserved6` | TField |  |  |
| 20 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED5` | `FsGaSecurityRatingByAgency_Reserved5` | TField |  |  |
| 21 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED4` | `FsGaSecurityRatingByAgency_Reserved4` | TField |  |  |
| 22 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED3` | `FsGaSecurityRatingByAgency_Reserved3` | TField |  |  |
| 23 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED2` | `FsGaSecurityRatingByAgency_Reserved2` | TField |  |  |
| 24 | `FS.GA.SECURITY.RATING.BY.AGENCY.RESERVED1` | `FsGaSecurityRatingByAgency_Reserved1` | TField |  |  |
| 25 | `FS.GA.SECURITY.RATING.BY.AGENCY.LOCAL.REF` | `FsGaSecurityRatingByAgency_LocalRef` |  |  |  |
| 26 | `FS.GA.SECURITY.RATING.BY.AGENCY.OVERRIDE` | `FsGaSecurityRatingByAgency_Override` |  |  |  |
| 27 | `FS.GA.SECURITY.RATING.BY.AGENCY.RECORD.STATUS` | `FsGaSecurityRatingByAgency_RecordStatus` | String |  |  |
| 28 | `FS.GA.SECURITY.RATING.BY.AGENCY.CURR.NO` | `FsGaSecurityRatingByAgency_CurrNo` | String |  |  |
| 29 | `FS.GA.SECURITY.RATING.BY.AGENCY.INPUTTER` | `FsGaSecurityRatingByAgency_Inputter` |  |  |  |
| 30 | `FS.GA.SECURITY.RATING.BY.AGENCY.DATE.TIME` | `FsGaSecurityRatingByAgency_DateTime` |  |  |  |
| 31 | `FS.GA.SECURITY.RATING.BY.AGENCY.AUTHORISER` | `FsGaSecurityRatingByAgency_Authoriser` | String |  |  |
| 32 | `FS.GA.SECURITY.RATING.BY.AGENCY.CO.CODE` | `FsGaSecurityRatingByAgency_CoCode` | String |  |  |
| 33 | `FS.GA.SECURITY.RATING.BY.AGENCY.DEPT.CODE` | `FsGaSecurityRatingByAgency_DeptCode` | String |  |  |
| 34 | `FS.GA.SECURITY.RATING.BY.AGENCY.AUDITOR.CODE` | `FsGaSecurityRatingByAgency_AuditorCode` | String |  |  |
| 35 | `FS.GA.SECURITY.RATING.BY.AGENCY.AUDIT.DATE.TIME` | `FsGaSecurityRatingByAgency_AuditDateTime` | String |  |  |
