# PPT.CURRENCY — Table Schema

> Source: `INSERTS/I_F.PPT.CURRENCY` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCCY.CurrencyID` | `PptCurrency_Currencyid` |  |  |  |
| 2 | `PPCCY.CompanyID` | `PptCurrency_Companyid` |  |  |  |
| 3 | `PPCCY.CurrencyCode` | `PptCurrency_Currencycode` |  |  |  |
| 4 | `PPCCY.CountryCode` | `PptCurrency_Countrycode` |  |  |  |
| 5 | `PPCCY.CurrencyGroup` | `PptCurrency_Currencygroup` |  |  |  |
| 6 | `PPCCY.StartDateCurrency` | `PptCurrency_Startdatecurrency` |  |  |  |
| 7 | `PPCCY.CurrencyName` | `PptCurrency_Currencyname` |  |  |  |
| 8 | `PPCCY.FractionalDigit` | `PptCurrency_Fractionaldigit` |  |  |  |
| 9 | `PPCCY.CountryName` | `PptCurrency_Countryname` |  |  |  |
| 10 | `PPCCY.FXLimit` | `PptCurrency_Fxlimit` |  |  |  |
| 11 | `PPCCY.EndDateCurrency` | `PptCurrency_Enddatecurrency` |  |  |  |
| 12 | `PPCCY.RACCurrency` | `PptCurrency_Raccurrency` |  |  |  |
| 13 | `PPCCY.RSCCurrency` | `PptCurrency_Rsccurrency` |  |  |  |
| 14 | `PPCCY.EntryUserID` | `PptCurrency_Entryuserid` |  |  |  |
| 15 | `PPCCY.EntryDateTime` | `PptCurrency_Entrydatetime` |  |  |  |
| 16 | `PPCCY.ApproverUserID` | `PptCurrency_Approveruserid` |  |  |  |
| 17 | `PPCCY.ApprovedDateTime` | `PptCurrency_Approveddatetime` |  |  |  |
| 18 | `PPCCY.WeekendDay1` | `PptCurrency_Weekendday1` |  |  |  |
| 19 | `PPCCY.WeekendDay2` | `PptCurrency_Weekendday2` |  |  |  |
| 20 | `PPCCY.OverrideThroughUpload` | `PptCurrency_Overridethroughupload` |  |  |  |
