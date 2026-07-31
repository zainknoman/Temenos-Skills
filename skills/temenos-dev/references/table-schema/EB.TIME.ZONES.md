# EB.TIME.ZONES — Table Schema

> Source: `INSERTS/I_F.EB.TIME.ZONES` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.ZN.DESCRIPTION` | `EbTimeZones_Description` |  |  |  |
| 2 | `EB.ZN.UTC.OFFSET` | `EbTimeZones_UtcOffset` | TField | Yes | Holds the UTC time difference with respective local zone time. Value of this field is displayed as an enrichment in TIME.ZONE field of COMPANY application. Validation Rules: Mandatory field. Accepts 1-35 alphanumeric values. |
| 3 | `EB.ZN.FAVORITES` | `EbTimeZones_Favorites` | TField | No | Determines whether the time zone names are set as favorites. If it is Yes , the user can choose the favorite time zones for a company profile. If it is No , the user cannot choose the favorite time zones for a company profile. Validation Rules: Optional field. YES_NULL type field. |
| 4 | `EB.ZN.SERVER.ZONE` | `EbTimeZones_ServerZone` | TField |  |  |
| 5 | `EB.ZN.RESERVED.4` | `EbTimeZones_Reserved4` | TField |  |  |
| 6 | `EB.ZN.RESERVED.3` | `EbTimeZones_Reserved3` | TField |  |  |
| 7 | `EB.ZN.RESERVED.2` | `EbTimeZones_Reserved2` | TField |  |  |
| 8 | `EB.ZN.RESERVED.1` | `EbTimeZones_Reserved1` | TField |  |  |
| 9 | `EB.ZN.RECORD.STATUS` | `EbTimeZones_RecordStatus` | String |  |  |
| 10 | `EB.ZN.CURR.NO` | `EbTimeZones_CurrNo` | String |  |  |
| 11 | `EB.ZN.INPUTTER` | `EbTimeZones_Inputter` |  |  |  |
| 12 | `EB.ZN.DATE.TIME` | `EbTimeZones_DateTime` |  |  |  |
| 13 | `EB.ZN.AUTHORISER` | `EbTimeZones_Authoriser` | String |  |  |
| 14 | `EB.ZN.CO.CODE` | `EbTimeZones_CoCode` | String |  |  |
| 15 | `EB.ZN.DEPT.CODE` | `EbTimeZones_DeptCode` | String |  |  |
| 16 | `EB.ZN.AUDITOR.CODE` | `EbTimeZones_AuditorCode` | String |  |  |
| 17 | `EB.ZN.AUDIT.DATE.TIME` | `EbTimeZones_AuditDateTime` | String |  |  |
