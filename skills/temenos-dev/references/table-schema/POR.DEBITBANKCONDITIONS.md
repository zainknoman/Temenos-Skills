# POR.DEBITBANKCONDITIONS — Table Schema

> Source: `INSERTS/I_F.POR.DEBITBANKCONDITIONS` in `PP_BankConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPDB.CompanyID` | `PorDebitbankconditions_Companyid` |  |  |  |
| 2 | `PPPDB.FTNumber` | `PorDebitbankconditions_Ftnumber` |  |  |  |
| 3 | `PPPDB.BankConditionsID` | `PorDebitbankconditions_Bankconditionsid` |  |  |  |
| 4 | `PPPDB.CTRNonSTPIndicator` | `PorDebitbankconditions_Ctrnonstpindicator` |  |  |  |
| 5 | `PPPDB.BTRNonSTPIndicator` | `PorDebitbankconditions_Btrnonstpindicator` |  |  |  |
| 6 | `PPPDB.DebitInstruction` | `PorDebitbankconditions_Debitinstruction` |  |  |  |
| 7 | `PPPDB.CreditInstruction` | `PorDebitbankconditions_Creditinstruction` |  |  |  |
| 8 | `PPPDB.WarehouseFlag` | `PorDebitbankconditions_Warehouseflag` |  |  |  |
| 9 | `PPPDB.WarehouseReleaseTime` | `PorDebitbankconditions_Warehousereleasetime` |  |  |  |
| 10 | `PPPDB.ChargeAccountCompanyID` | `PorDebitbankconditions_Chargeaccountcompanyid` |  |  |  |
| 11 | `PPPDB.ChargeAccountNumber` | `PorDebitbankconditions_Chargeaccountnumber` |  |  |  |
| 12 | `PPPDB.ChargeAccountCurrency` | `PorDebitbankconditions_Chargeaccountcurrency` |  |  |  |
| 13 | `PPPDB.LanguageID` | `PorDebitbankconditions_Languageid` |  |  |  |
| 14 | `PPPDB.StatementFormatName` | `PorDebitbankconditions_Statementformatname` |  |  |  |
| 15 | `PPPDB.FXSpread` | `PorDebitbankconditions_Fxspread` |  |  |  |
| 16 | `PPPDB.CustomerStatusMessageType` | `PorDebitbankconditions_Customerstatusmessagetype` |  |  |  |
