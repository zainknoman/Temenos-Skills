# PP.HOLIDAY.LOGIC — Table Schema

> Source: `INSERTS/I_F.PP.HOLIDAY.LOGIC` in `PP_DateDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.HOL.StartDate` | `PpHolidayLogic_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 2 | `PP.HOL.EndDate` | `PpHolidayLogic_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 3 | `PP.HOL.Ranking` | `PpHolidayLogic_Ranking` |  |  |  |
| 4 | `PP.HOL.DateType` | `PpHolidayLogic_Datetype` |  |  |  |
| 5 | `PP.HOL.CreditPartyCountry` | `PpHolidayLogic_Creditpartycountry` |  |  |  |
| 6 | `PP.HOL.CreditCurrency` | `PpHolidayLogic_Creditcurrency` |  |  |  |
| 7 | `PP.HOL.BankCheckIndicator` | `PpHolidayLogic_Bankcheckindicator` |  |  |  |
| 8 | `PP.HOL.CreditPartyCountryIndicator` | `PpHolidayLogic_Creditpartycountryindicator` |  |  |  |
| 9 | `PP.HOL.DebitCurrencyIndicator` | `PpHolidayLogic_Debitcurrencyindicator` |  |  |  |
| 10 | `PP.HOL.CreditCurrencyIndicator` | `PpHolidayLogic_Creditcurrencyindicator` |  |  |  |
| 11 | `PP.HOL.ClearingChannelIndicator` | `PpHolidayLogic_Clearingchannelindicator` |  |  |  |
| 12 | `PP.HOL.TradeCurrencyIndicator` | `PpHolidayLogic_Tradecurrencyindicator` |  |  |  |
| 13 | `PP.HOL.CheckNonWorkingDayIndicator` | `PpHolidayLogic_Checknonworkingdayindicator` |  |  |  |
| 14 | `PP.HOL.DebitPartyCountry` | `PpHolidayLogic_Debitpartycountry` |  |  |  |
| 15 | `PP.HOL.DebitCurrency` | `PpHolidayLogic_Debitcurrency` |  |  |  |
| 16 | `PP.HOL.DebitPartyCountryIndicator` | `PpHolidayLogic_Debitpartycountryindicator` |  |  |  |
| 17 | `PP.HOL.Direction` | `PpHolidayLogic_Direction` |  |  |  |
| 18 | `PP.HOL.HolidaycheckforCBD` | `PpHolidayLogic_Holidaycheckforcbd` |  |  |  |
| 19 | `PP.HOL.RESERVED.3` | `PpHolidayLogic_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 20 | `PP.HOL.RESERVED.2` | `PpHolidayLogic_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 21 | `PP.HOL.RESERVED.1` | `PpHolidayLogic_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 22 | `PP.HOL.LOCAL.REF` | `PpHolidayLogic_LocalRef` |  |  |  |
| 23 | `PP.HOL.OVERRIDE` | `PpHolidayLogic_Override` |  |  |  |
| 24 | `PP.HOL.RECORD.STATUS` | `PpHolidayLogic_RecordStatus` | String |  |  |
| 25 | `PP.HOL.CURR.NO` | `PpHolidayLogic_CurrNo` | String |  |  |
| 26 | `PP.HOL.INPUTTER` | `PpHolidayLogic_Inputter` |  |  |  |
| 27 | `PP.HOL.DATE.TIME` | `PpHolidayLogic_DateTime` |  |  |  |
| 28 | `PP.HOL.AUTHORISER` | `PpHolidayLogic_Authoriser` | String |  |  |
| 29 | `PP.HOL.CO.CODE` | `PpHolidayLogic_CoCode` | String |  |  |
| 30 | `PP.HOL.DEPT.CODE` | `PpHolidayLogic_DeptCode` | String |  |  |
| 31 | `PP.HOL.AUDITOR.CODE` | `PpHolidayLogic_AuditorCode` | String |  |  |
| 32 | `PP.HOL.AUDIT.DATE.TIME` | `PpHolidayLogic_AuditDateTime` | String |  |  |
