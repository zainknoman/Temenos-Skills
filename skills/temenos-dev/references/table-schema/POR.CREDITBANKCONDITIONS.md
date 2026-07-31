# POR.CREDITBANKCONDITIONS — Table Schema

> Source: `INSERTS/I_F.POR.CREDITBANKCONDITIONS` in `PP_BankConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPCB.CompanyID` | `PorCreditbankconditions_Companyid` |  |  |  |
| 2 | `PPPCB.FTNumber` | `PorCreditbankconditions_Ftnumber` |  |  |  |
| 3 | `PPPCB.BankConditionsID` | `PorCreditbankconditions_Bankconditionsid` |  |  |  |
| 4 | `PPPCB.ChargeAccountCompanyID` | `PorCreditbankconditions_Chargeaccountcompanyid` |  |  |  |
| 5 | `PPPCB.ChargeAccountNumber` | `PorCreditbankconditions_Chargeaccountnumber` |  |  |  |
| 6 | `PPPCB.ChargeAccountCurrency` | `PorCreditbankconditions_Chargeaccountcurrency` |  |  |  |
| 7 | `PPPCB.LanguageID` | `PorCreditbankconditions_Languageid` |  |  |  |
| 8 | `PPPCB.StatementFormatName` | `PorCreditbankconditions_Statementformatname` |  |  |  |
| 9 | `PPPCB.FXSpread` | `PorCreditbankconditions_Fxspread` |  |  |  |
| 10 | `PPPCB.CustomerStatusMessageType` | `PorCreditbankconditions_Customerstatusmessagetype` |  |  |  |
