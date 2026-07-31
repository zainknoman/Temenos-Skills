# PPL.BANKCONDITIONS — Table Schema

> Source: `INSERTS/I_F.PPL.BANKCONDITIONS` in `PP_BankConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPLBC.BankConditionsID` | `PplBankconditions_Bankconditionsid` |  |  |  |
| 2 | `PPLBC.CompanyID` | `PplBankconditions_Companyid` |  |  |  |
| 3 | `PPLBC.CorrespondentBIC` | `PplBankconditions_Correspondentbic` |  |  |  |
| 4 | `PPLBC.SLAID` | `PplBankconditions_Slaid` |  |  |  |
| 5 | `PPLBC.CurrencyCode` | `PplBankconditions_Currencycode` |  |  |  |
| 6 | `PPLBC.StartDateBankConditions` | `PplBankconditions_Startdatebankconditions` |  |  |  |
| 7 | `PPLBC.CTRNonSTPIndicator` | `PplBankconditions_Ctrnonstpindicator` |  |  |  |
| 8 | `PPLBC.BTRNonSTPIndicator` | `PplBankconditions_Btrnonstpindicator` |  |  |  |
| 9 | `PPLBC.DebitInstruction` | `PplBankconditions_Debitinstruction` |  |  |  |
| 10 | `PPLBC.CreditInstruction` | `PplBankconditions_Creditinstruction` |  |  |  |
| 11 | `PPLBC.WareHouseFlag` | `PplBankconditions_Warehouseflag` |  |  |  |
| 12 | `PPLBC.WareHouseReleaseTime` | `PplBankconditions_Warehousereleasetime` |  |  |  |
| 13 | `PPLBC.PSDECChargeCompliant` | `PplBankconditions_Psdecchargecompliant` |  |  |  |
| 14 | `PPLBC.LanguageID` | `PplBankconditions_Languageid` |  |  |  |
| 15 | `PPLBC.CreditStmtFormatName` | `PplBankconditions_Creditstmtformatname` |  |  |  |
| 16 | `PPLBC.DebitStmtFormatName` | `PplBankconditions_Debitstmtformatname` |  |  |  |
| 17 | `PPLBC.FXSpread` | `PplBankconditions_Fxspread` |  |  |  |
| 18 | `PPLBC.EndDateBankConditions` | `PplBankconditions_Enddatebankconditions` |  |  |  |
| 19 | `PPLBC.RACBankConditions` | `PplBankconditions_Racbankconditions` |  |  |  |
| 20 | `PPLBC.RSCBankConditions` | `PplBankconditions_Rscbankconditions` |  |  |  |
| 21 | `PPLBC.EntryUserID` | `PplBankconditions_Entryuserid` |  |  |  |
| 22 | `PPLBC.EntryDateTime` | `PplBankconditions_Entrydatetime` |  |  |  |
| 23 | `PPLBC.ApproverUserID` | `PplBankconditions_Approveruserid` |  |  |  |
| 24 | `PPLBC.ApprovedDateTime` | `PplBankconditions_Approveddatetime` |  |  |  |
| 25 | `PPLBC.AllowSpecialCharacterSet` | `PplBankconditions_Allowspecialcharacterset` |  |  |  |
| 26 | `PPLBC.CodePageSet` | `PplBankconditions_Codepageset` |  |  |  |
