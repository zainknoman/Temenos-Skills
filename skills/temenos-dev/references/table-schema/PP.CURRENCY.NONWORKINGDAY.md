# PP.CURRENCY.NONWORKINGDAY — Table Schema

> Source: `INSERTS/I_F.PP.CURRENCY.NONWORKINGDAY` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CCH.CompanyID` | `PpCurrencyNonworkingday_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.CCH.DayDate` | `PpCurrencyNonworkingday_Daydate` |  |  |  |
| 3 | `PP.CCH.HolidayIndicator` | `PpCurrencyNonworkingday_Holidayindicator` |  |  |  |
| 4 | `PP.CCH.WeekendDayIndicator` | `PpCurrencyNonworkingday_Weekenddayindicator` |  |  |  |
| 5 | `PP.CCH.RESERVED.5` | `PpCurrencyNonworkingday_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.CCH.RESERVED.4` | `PpCurrencyNonworkingday_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.CCH.RESERVED.3` | `PpCurrencyNonworkingday_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.CCH.RESERVED.2` | `PpCurrencyNonworkingday_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.CCH.RESERVED.1` | `PpCurrencyNonworkingday_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 10 | `PP.CCH.LOCAL.REF` | `PpCurrencyNonworkingday_LocalRef` |  |  |  |
| 11 | `PP.CCH.OVERRIDE` | `PpCurrencyNonworkingday_Override` |  |  |  |
| 12 | `PP.CCH.RECORD.STATUS` | `PpCurrencyNonworkingday_RecordStatus` | String |  |  |
| 13 | `PP.CCH.CURR.NO` | `PpCurrencyNonworkingday_CurrNo` | String |  |  |
| 14 | `PP.CCH.INPUTTER` | `PpCurrencyNonworkingday_Inputter` |  |  |  |
| 15 | `PP.CCH.DATE.TIME` | `PpCurrencyNonworkingday_DateTime` |  |  |  |
| 16 | `PP.CCH.AUTHORISER` | `PpCurrencyNonworkingday_Authoriser` | String |  |  |
| 17 | `PP.CCH.CO.CODE` | `PpCurrencyNonworkingday_CoCode` | String |  |  |
| 18 | `PP.CCH.DEPT.CODE` | `PpCurrencyNonworkingday_DeptCode` | String |  |  |
| 19 | `PP.CCH.AUDITOR.CODE` | `PpCurrencyNonworkingday_AuditorCode` | String |  |  |
| 20 | `PP.CCH.AUDIT.DATE.TIME` | `PpCurrencyNonworkingday_AuditDateTime` | String |  |  |
