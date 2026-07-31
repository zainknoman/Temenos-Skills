# FS.GI.APP.COUNTRY.HOLIDAY — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.COUNTRY.HOLIDAY` in `FS_ManagerParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.COUNTRY.HOLIDAY.PARENT.REF.ID` | `FsGiAppCountryHoliday_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.COUNTRY.HOLIDAY.ORA.ROWID` | `FsGiAppCountryHoliday_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.COUNTRY.HOLIDAY.COUNTRY` | `FsGiAppCountryHoliday_Country` | TField |  | Country code for which holiday marked. Multifonds DB Column is CPAYS. |
| 4 | `FS.GI.APP.COUNTRY.HOLIDAY.HOLIDAY.DATE` | `FsGiAppCountryHoliday_HolidayDate` | TField |  | Holiday date. Multifonds DB Column is DJOUR_FERIE. |
| 5 | `FS.GI.APP.COUNTRY.HOLIDAY.NAME` | `FsGiAppCountryHoliday_Name` | TField |  | Holiday description. Multifonds DB Column is XLIBELLE. |
| 6 | `FS.GI.APP.COUNTRY.HOLIDAY.INTERNAL.ID` | `FsGiAppCountryHoliday_InternalId` | TField |  | Unique internal identifier supplied as a reference to external processes creating new details in the table. Multifonds DB Column is INTERNAL_ID. |
| 7 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED10` | `FsGiAppCountryHoliday_Reserved10` | TField |  |  |
| 8 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED9` | `FsGiAppCountryHoliday_Reserved9` | TField |  |  |
| 9 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED8` | `FsGiAppCountryHoliday_Reserved8` | TField |  |  |
| 10 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED7` | `FsGiAppCountryHoliday_Reserved7` | TField |  |  |
| 11 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED6` | `FsGiAppCountryHoliday_Reserved6` | TField |  |  |
| 12 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED5` | `FsGiAppCountryHoliday_Reserved5` | TField |  |  |
| 13 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED4` | `FsGiAppCountryHoliday_Reserved4` | TField |  |  |
| 14 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED3` | `FsGiAppCountryHoliday_Reserved3` | TField |  |  |
| 15 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED2` | `FsGiAppCountryHoliday_Reserved2` | TField |  |  |
| 16 | `FS.GI.APP.COUNTRY.HOLIDAY.RESERVED1` | `FsGiAppCountryHoliday_Reserved1` | TField |  |  |
| 17 | `FS.GI.APP.COUNTRY.HOLIDAY.LOCAL.REF` | `FsGiAppCountryHoliday_LocalRef` |  |  |  |
| 18 | `FS.GI.APP.COUNTRY.HOLIDAY.OVERRIDE` | `FsGiAppCountryHoliday_Override` |  |  |  |
| 19 | `FS.GI.APP.COUNTRY.HOLIDAY.RECORD.STATUS` | `FsGiAppCountryHoliday_RecordStatus` | String |  |  |
| 20 | `FS.GI.APP.COUNTRY.HOLIDAY.CURR.NO` | `FsGiAppCountryHoliday_CurrNo` | String |  |  |
| 21 | `FS.GI.APP.COUNTRY.HOLIDAY.INPUTTER` | `FsGiAppCountryHoliday_Inputter` |  |  |  |
| 22 | `FS.GI.APP.COUNTRY.HOLIDAY.DATE.TIME` | `FsGiAppCountryHoliday_DateTime` |  |  |  |
| 23 | `FS.GI.APP.COUNTRY.HOLIDAY.AUTHORISER` | `FsGiAppCountryHoliday_Authoriser` | String |  |  |
| 24 | `FS.GI.APP.COUNTRY.HOLIDAY.CO.CODE` | `FsGiAppCountryHoliday_CoCode` | String |  |  |
| 25 | `FS.GI.APP.COUNTRY.HOLIDAY.DEPT.CODE` | `FsGiAppCountryHoliday_DeptCode` | String |  |  |
| 26 | `FS.GI.APP.COUNTRY.HOLIDAY.AUDITOR.CODE` | `FsGiAppCountryHoliday_AuditorCode` | String |  |  |
| 27 | `FS.GI.APP.COUNTRY.HOLIDAY.AUDIT.DATE.TIME` | `FsGiAppCountryHoliday_AuditDateTime` | String |  |  |
