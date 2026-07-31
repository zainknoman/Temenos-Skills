# PPT.HOLIDAYLOGIC — Table Schema

> Source: `INSERTS/I_F.PPT.HOLIDAYLOGIC` in `PP_DateDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPHOL.CompanyID` | `PptHolidaylogic_Companyid` |  |  |  |
| 2 | `PPHOL.DateType` | `PptHolidaylogic_Datetype` |  |  |  |
| 3 | `PPHOL.CreditPartyCountry` | `PptHolidaylogic_Creditpartycountry` |  |  |  |
| 4 | `PPHOL.CreditCurrency` | `PptHolidaylogic_Creditcurrency` |  |  |  |
| 5 | `PPHOL.StartDateHolidayLogic` | `PptHolidaylogic_Startdateholidaylogic` |  |  |  |
| 6 | `PPHOL.Ranking` | `PptHolidaylogic_Ranking` |  |  |  |
| 7 | `PPHOL.BankCheckIndicator` | `PptHolidaylogic_Bankcheckindicator` |  |  |  |
| 8 | `PPHOL.CreditPartyCountryIndicator` | `PptHolidaylogic_Creditpartycountryindicator` |  |  |  |
| 9 | `PPHOL.DebitCurrencyIndicator` | `PptHolidaylogic_Debitcurrencyindicator` |  |  |  |
| 10 | `PPHOL.CreditCurrencyIndicator` | `PptHolidaylogic_Creditcurrencyindicator` |  |  |  |
| 11 | `PPHOL.ClearingChannelIndicator` | `PptHolidaylogic_Clearingchannelindicator` |  |  |  |
| 12 | `PPHOL.TradeCurrencyIndicator` | `PptHolidaylogic_Tradecurrencyindicator` |  |  |  |
| 13 | `PPHOL.CheckNonWorkingDayIndicator` | `PptHolidaylogic_Checknonworkingdayindicator` |  |  |  |
| 14 | `PPHOL.EndDateHolidayLogic` | `PptHolidaylogic_Enddateholidaylogic` |  |  |  |
| 15 | `PPHOL.RACHolidayLogic` | `PptHolidaylogic_Racholidaylogic` |  |  |  |
| 16 | `PPHOL.RSCHolidayLogic` | `PptHolidaylogic_Rscholidaylogic` |  |  |  |
| 17 | `PPHOL.EntryUserID` | `PptHolidaylogic_Entryuserid` |  |  |  |
| 18 | `PPHOL.EntryDateTime` | `PptHolidaylogic_Entrydatetime` |  |  |  |
| 19 | `PPHOL.ApproverUserID` | `PptHolidaylogic_Approveruserid` |  |  |  |
| 20 | `PPHOL.ApprovedDateTime` | `PptHolidaylogic_Approveddatetime` |  |  |  |
| 21 | `PPHOL.DebitPartyCountry` | `PptHolidaylogic_Debitpartycountry` |  |  |  |
| 22 | `PPHOL.DebitCurrency` | `PptHolidaylogic_Debitcurrency` |  |  |  |
| 23 | `PPHOL.DebitPartyCountryIndicator` | `PptHolidaylogic_Debitpartycountryindicator` |  |  |  |
