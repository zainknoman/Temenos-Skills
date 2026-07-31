# NA.NEEDS.CLASS — Table Schema

> Source: `INSERTS/I_F.NA.NEEDS.CLASS` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.NC.DESCRIPTION` | `NaNeedsClass_Description` |  |  |  |
| 2 | `NA.NC.FULL.DESC` | `NaNeedsClass_FullDesc` |  |  |  |
| 3 | `NA.NC.TYPE` | `NaNeedsClass_Type` |  |  |  |
| 4 | `NA.NC.RESERVED.10` | `NaNeedsClass_Reserved10` | TField |  |  |
| 5 | `NA.NC.RESERVED.9` | `NaNeedsClass_Reserved9` | TField |  |  |
| 6 | `NA.NC.RESERVED.8` | `NaNeedsClass_Reserved8` | TField |  |  |
| 7 | `NA.NC.RESERVED.7` | `NaNeedsClass_Reserved7` | TField |  |  |
| 8 | `NA.NC.RESERVED.6` | `NaNeedsClass_Reserved6` | TField |  |  |
| 9 | `NA.NC.RESERVED.5` | `NaNeedsClass_Reserved5` | TField |  |  |
| 10 | `NA.NC.RESERVED.4` | `NaNeedsClass_Reserved4` | TField |  |  |
| 11 | `NA.NC.RESERVED.3` | `NaNeedsClass_Reserved3` | TField |  |  |
| 12 | `NA.NC.RESERVED.2` | `NaNeedsClass_Reserved2` | TField |  |  |
| 13 | `NA.NC.RESERVED.1` | `NaNeedsClass_Reserved1` | TField |  |  |
| 14 | `NA.NC.LOCAL.REF` | `NaNeedsClass_LocalRef` |  |  |  |
| 15 | `NA.NC.OVERRIDE` | `NaNeedsClass_Override` |  |  |  |
| 16 | `NA.NC.RECORD.STATUS` | `NaNeedsClass_RecordStatus` | String |  |  |
| 17 | `NA.NC.CURR.NO` | `NaNeedsClass_CurrNo` | String |  |  |
| 18 | `NA.NC.INPUTTER` | `NaNeedsClass_Inputter` |  |  |  |
| 19 | `NA.NC.DATE.TIME` | `NaNeedsClass_DateTime` |  |  |  |
| 20 | `NA.NC.AUTHORISER` | `NaNeedsClass_Authoriser` | String |  |  |
| 21 | `NA.NC.CO.CODE` | `NaNeedsClass_CoCode` | String |  |  |
| 22 | `NA.NC.DEPT.CODE` | `NaNeedsClass_DeptCode` | String |  |  |
| 23 | `NA.NC.AUDITOR.CODE` | `NaNeedsClass_AuditorCode` | String |  |  |
| 24 | `NA.NC.AUDIT.DATE.TIME` | `NaNeedsClass_AuditDateTime` | String |  |  |
