# FS.GI.APP.CURRENCY.HOLIDAY — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.CURRENCY.HOLIDAY` in `FS_ManagerParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.CURRENCY.HOLIDAY.PARENT.REF.ID` | `FsGiAppCurrencyHoliday_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.CURRENCY.HOLIDAY.ORA.ROWID` | `FsGiAppCurrencyHoliday_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.CURRENCY.HOLIDAY.PAYMENT.CURRENCY` | `FsGiAppCurrencyHoliday_PaymentCurrency` | TField |  | Payment currency for which holiday being marked. Multifonds DB Column is CMON. |
| 4 | `FS.GI.APP.CURRENCY.HOLIDAY.CURRENCY.CALENDAR.CODE` | `FsGiAppCurrencyHoliday_CurrencyCalendarCode` | TField |  | Currency calendar code. Multifonds DB Column is CCY_INDICATOR. |
| 5 | `FS.GI.APP.CURRENCY.HOLIDAY.HOLIDAY.DATE` | `FsGiAppCurrencyHoliday_HolidayDate` | TField |  | Holiday date. Multifonds DB Column is DJOURS_FERIE. |
| 6 | `FS.GI.APP.CURRENCY.HOLIDAY.NAME` | `FsGiAppCurrencyHoliday_Name` | TField |  | Holiday description. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GI.APP.CURRENCY.HOLIDAY.INTERNAL.ID` | `FsGiAppCurrencyHoliday_InternalId` | TField |  | Unique internal identifier supplied as a reference to external processes creating new details in the table. Multifonds DB Column is INTERNAL_ID. |
| 8 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED10` | `FsGiAppCurrencyHoliday_Reserved10` | TField |  |  |
| 9 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED9` | `FsGiAppCurrencyHoliday_Reserved9` | TField |  |  |
| 10 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED8` | `FsGiAppCurrencyHoliday_Reserved8` | TField |  |  |
| 11 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED7` | `FsGiAppCurrencyHoliday_Reserved7` | TField |  |  |
| 12 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED6` | `FsGiAppCurrencyHoliday_Reserved6` | TField |  |  |
| 13 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED5` | `FsGiAppCurrencyHoliday_Reserved5` | TField |  |  |
| 14 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED4` | `FsGiAppCurrencyHoliday_Reserved4` | TField |  |  |
| 15 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED3` | `FsGiAppCurrencyHoliday_Reserved3` | TField |  |  |
| 16 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED2` | `FsGiAppCurrencyHoliday_Reserved2` | TField |  |  |
| 17 | `FS.GI.APP.CURRENCY.HOLIDAY.RESERVED1` | `FsGiAppCurrencyHoliday_Reserved1` | TField |  |  |
| 18 | `FS.GI.APP.CURRENCY.HOLIDAY.LOCAL.REF` | `FsGiAppCurrencyHoliday_LocalRef` |  |  |  |
| 19 | `FS.GI.APP.CURRENCY.HOLIDAY.OVERRIDE` | `FsGiAppCurrencyHoliday_Override` |  |  |  |
| 20 | `FS.GI.APP.CURRENCY.HOLIDAY.RECORD.STATUS` | `FsGiAppCurrencyHoliday_RecordStatus` | String |  |  |
| 21 | `FS.GI.APP.CURRENCY.HOLIDAY.CURR.NO` | `FsGiAppCurrencyHoliday_CurrNo` | String |  |  |
| 22 | `FS.GI.APP.CURRENCY.HOLIDAY.INPUTTER` | `FsGiAppCurrencyHoliday_Inputter` |  |  |  |
| 23 | `FS.GI.APP.CURRENCY.HOLIDAY.DATE.TIME` | `FsGiAppCurrencyHoliday_DateTime` |  |  |  |
| 24 | `FS.GI.APP.CURRENCY.HOLIDAY.AUTHORISER` | `FsGiAppCurrencyHoliday_Authoriser` | String |  |  |
| 25 | `FS.GI.APP.CURRENCY.HOLIDAY.CO.CODE` | `FsGiAppCurrencyHoliday_CoCode` | String |  |  |
| 26 | `FS.GI.APP.CURRENCY.HOLIDAY.DEPT.CODE` | `FsGiAppCurrencyHoliday_DeptCode` | String |  |  |
| 27 | `FS.GI.APP.CURRENCY.HOLIDAY.AUDITOR.CODE` | `FsGiAppCurrencyHoliday_AuditorCode` | String |  |  |
| 28 | `FS.GI.APP.CURRENCY.HOLIDAY.AUDIT.DATE.TIME` | `FsGiAppCurrencyHoliday_AuditDateTime` | String |  |  |
