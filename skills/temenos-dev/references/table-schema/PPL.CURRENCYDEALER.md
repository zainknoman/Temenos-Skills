# PPL.CURRENCYDEALER — Table Schema

> Source: `INSERTS/I_F.PPL.CURRENCYDEALER` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPLCD.CompanyID` | `PplCurrencydealer_Companyid` |  |  |  |
| 2 | `PPLCD.Ranking` | `PplCurrencydealer_Ranking` |  |  |  |
| 3 | `PPLCD.Currency1` | `PplCurrencydealer_Currency1` |  |  |  |
| 4 | `PPLCD.Currency2` | `PplCurrencydealer_Currency2` |  |  |  |
| 5 | `PPLCD.BusinessLine` | `PplCurrencydealer_Businessline` |  |  |  |
| 6 | `PPLCD.BookCode` | `PplCurrencydealer_Bookcode` |  |  |  |
| 7 | `PPLCD.PostingProduct` | `PplCurrencydealer_Postingproduct` |  |  |  |
| 8 | `PPLCD.DealerDeskCode` | `PplCurrencydealer_Dealerdeskcode` |  |  |  |
| 9 | `PPLCD.RACCurrencyDealer` | `PplCurrencydealer_Raccurrencydealer` |  |  |  |
| 10 | `PPLCD.RSCCurrencyDealer` | `PplCurrencydealer_Rsccurrencydealer` |  |  |  |
| 11 | `PPLCD.EntryUserID` | `PplCurrencydealer_Entryuserid` |  |  |  |
| 12 | `PPLCD.EntryDateTime` | `PplCurrencydealer_Entrydatetime` |  |  |  |
| 13 | `PPLCD.ApproverUserID` | `PplCurrencydealer_Approveruserid` |  |  |  |
| 14 | `PPLCD.ApprovedDateTime` | `PplCurrencydealer_Approveddatetime` |  |  |  |
