# FS.GA.QUOTATION.PLACE.CALENDAR — Table Schema

> Source: `INSERTS/I_F.FS.GA.QUOTATION.PLACE.CALENDAR` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.QUOTATION.PLACE.CALENDAR.QUOTATION.PLACE` | `FsGaQuotationPlaceCalendar_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 2 | `FS.GA.QUOTATION.PLACE.CALENDAR.FROM.DATE` | `FsGaQuotationPlaceCalendar_FromDate` | TField |  | Date from which the process/report have to be run. Multifonds DB Column is DATE_FROM. |
| 3 | `FS.GA.QUOTATION.PLACE.CALENDAR.TO.DATE` | `FsGaQuotationPlaceCalendar_ToDate` | TField |  | Date upto which the process/report have to be run. Multifonds DB Column is DATE_TO. |
| 4 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED10` | `FsGaQuotationPlaceCalendar_Reserved10` | TField |  |  |
| 5 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED9` | `FsGaQuotationPlaceCalendar_Reserved9` | TField |  |  |
| 6 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED8` | `FsGaQuotationPlaceCalendar_Reserved8` | TField |  |  |
| 7 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED7` | `FsGaQuotationPlaceCalendar_Reserved7` | TField |  |  |
| 8 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED6` | `FsGaQuotationPlaceCalendar_Reserved6` | TField |  |  |
| 9 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED5` | `FsGaQuotationPlaceCalendar_Reserved5` | TField |  |  |
| 10 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED4` | `FsGaQuotationPlaceCalendar_Reserved4` | TField |  |  |
| 11 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED3` | `FsGaQuotationPlaceCalendar_Reserved3` | TField |  |  |
| 12 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED2` | `FsGaQuotationPlaceCalendar_Reserved2` | TField |  |  |
| 13 | `FS.GA.QUOTATION.PLACE.CALENDAR.RESERVED1` | `FsGaQuotationPlaceCalendar_Reserved1` | TField |  |  |
| 14 | `FS.GA.QUOTATION.PLACE.CALENDAR.RECORD.STATUS` | `FsGaQuotationPlaceCalendar_RecordStatus` | String |  |  |
| 15 | `FS.GA.QUOTATION.PLACE.CALENDAR.CURR.NO` | `FsGaQuotationPlaceCalendar_CurrNo` | String |  |  |
| 16 | `FS.GA.QUOTATION.PLACE.CALENDAR.INPUTTER` | `FsGaQuotationPlaceCalendar_Inputter` |  |  |  |
| 17 | `FS.GA.QUOTATION.PLACE.CALENDAR.DATE.TIME` | `FsGaQuotationPlaceCalendar_DateTime` |  |  |  |
| 18 | `FS.GA.QUOTATION.PLACE.CALENDAR.AUTHORISER` | `FsGaQuotationPlaceCalendar_Authoriser` | String |  |  |
| 19 | `FS.GA.QUOTATION.PLACE.CALENDAR.CO.CODE` | `FsGaQuotationPlaceCalendar_CoCode` | String |  |  |
| 20 | `FS.GA.QUOTATION.PLACE.CALENDAR.DEPT.CODE` | `FsGaQuotationPlaceCalendar_DeptCode` | String |  |  |
| 21 | `FS.GA.QUOTATION.PLACE.CALENDAR.AUDITOR.CODE` | `FsGaQuotationPlaceCalendar_AuditorCode` | String |  |  |
| 22 | `FS.GA.QUOTATION.PLACE.CALENDAR.AUDIT.DATE.TIME` | `FsGaQuotationPlaceCalendar_AuditDateTime` | String |  |  |
