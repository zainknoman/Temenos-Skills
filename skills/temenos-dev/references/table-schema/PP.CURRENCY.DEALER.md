# PP.CURRENCY.DEALER — Table Schema

> Source: `INSERTS/I_F.PP.CURRENCY.DEALER` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.LCD.Ranking` | `PpCurrencyDealer_Ranking` |  |  |  |
| 2 | `PP.LCD.Currency1` | `PpCurrencyDealer_Currency1` |  |  |  |
| 3 | `PP.LCD.Currency2` | `PpCurrencyDealer_Currency2` |  |  |  |
| 4 | `PP.LCD.BusinessLine` | `PpCurrencyDealer_Businessline` |  |  |  |
| 5 | `PP.LCD.BookCode` | `PpCurrencyDealer_Bookcode` |  |  |  |
| 6 | `PP.LCD.PostingProduct` | `PpCurrencyDealer_Postingproduct` |  |  |  |
| 7 | `PP.LCD.DealerDeskCode` | `PpCurrencyDealer_Dealerdeskcode` |  |  |  |
| 8 | `PP.LCD.RESERVED.5` | `PpCurrencyDealer_Reserved5` | TField |  |  |
| 9 | `PP.LCD.RESERVED.4` | `PpCurrencyDealer_Reserved4` | TField |  |  |
| 10 | `PP.LCD.RESERVED.3` | `PpCurrencyDealer_Reserved3` | TField |  |  |
| 11 | `PP.LCD.RESERVED.2` | `PpCurrencyDealer_Reserved2` | TField |  |  |
| 12 | `PP.LCD.RESERVED.1` | `PpCurrencyDealer_Reserved1` | TField |  |  |
| 13 | `PP.LCD.LOCAL.REF` | `PpCurrencyDealer_LocalRef` |  |  |  |
| 14 | `PP.LCD.OVERRIDE` | `PpCurrencyDealer_Override` |  |  |  |
| 15 | `PP.LCD.RECORD.STATUS` | `PpCurrencyDealer_RecordStatus` | String |  |  |
| 16 | `PP.LCD.CURR.NO` | `PpCurrencyDealer_CurrNo` | String |  |  |
| 17 | `PP.LCD.INPUTTER` | `PpCurrencyDealer_Inputter` |  |  |  |
| 18 | `PP.LCD.DATE.TIME` | `PpCurrencyDealer_DateTime` |  |  |  |
| 19 | `PP.LCD.AUTHORISER` | `PpCurrencyDealer_Authoriser` | String |  |  |
| 20 | `PP.LCD.CO.CODE` | `PpCurrencyDealer_CoCode` | String |  |  |
| 21 | `PP.LCD.DEPT.CODE` | `PpCurrencyDealer_DeptCode` | String |  |  |
| 22 | `PP.LCD.AUDITOR.CODE` | `PpCurrencyDealer_AuditorCode` | String |  |  |
| 23 | `PP.LCD.AUDIT.DATE.TIME` | `PpCurrencyDealer_AuditDateTime` | String |  |  |
