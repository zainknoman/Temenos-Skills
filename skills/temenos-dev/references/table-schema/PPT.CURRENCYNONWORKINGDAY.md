# PPT.CURRENCYNONWORKINGDAY — Table Schema

> Source: `INSERTS/I_F.PPT.CURRENCYNONWORKINGDAY` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCCH.CompanyID` | `PptCurrencynonworkingday_Companyid` |  |  |  |
| 2 | `PPCCH.CountryCode` | `PptCurrencynonworkingday_Countrycode` |  |  |  |
| 3 | `PPCCH.DayDate` | `PptCurrencynonworkingday_Daydate` |  |  |  |
| 4 | `PPCCH.CurrencyCode` | `PptCurrencynonworkingday_Currencycode` |  |  |  |
| 5 | `PPCCH.HolidayIndicator` | `PptCurrencynonworkingday_Holidayindicator` |  |  |  |
| 6 | `PPCCH.WeekendDayIndicator` | `PptCurrencynonworkingday_Weekenddayindicator` |  |  |  |
| 7 | `PPCCH.RACCurrencyNonWorkingDay` | `PptCurrencynonworkingday_Raccurrencynonworkingday` |  |  |  |
| 8 | `PPCCH.RSCCurrencyNonWorkingDay` | `PptCurrencynonworkingday_Rsccurrencynonworkingday` |  |  |  |
| 9 | `PPCCH.EntryUserID` | `PptCurrencynonworkingday_Entryuserid` |  |  |  |
| 10 | `PPCCH.EntryDateTime` | `PptCurrencynonworkingday_Entrydatetime` |  |  |  |
| 11 | `PPCCH.ApproverUserID` | `PptCurrencynonworkingday_Approveruserid` |  |  |  |
| 12 | `PPCCH.ApprovedDateTime` | `PptCurrencynonworkingday_Approveddatetime` |  |  |  |
