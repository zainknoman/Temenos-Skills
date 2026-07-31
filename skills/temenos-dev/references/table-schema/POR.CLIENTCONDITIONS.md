# POR.CLIENTCONDITIONS — Table Schema

> Source: `INSERTS/I_F.POR.CLIENTCONDITIONS` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPCC.CompanyID` | `PorClientconditions_Companyid` |  |  |  |
| 2 | `PPPCC.FTNumber` | `PorClientconditions_Ftnumber` |  |  |  |
| 3 | `PPPCC.DebitCreditIndicator` | `PorClientconditions_Debitcreditindicator` |  |  |  |
| 4 | `PPPCC.ClientConditionsID` | `PorClientconditions_Clientconditionsid` |  |  |  |
| 5 | `PPPCC.FXDiscount` | `PorClientconditions_Fxdiscount` |  |  |  |
| 6 | `PPPCC.LanguageID` | `PorClientconditions_Languageid` |  |  |  |
| 7 | `PPPCC.StatementFormatName` | `PorClientconditions_Statementformatname` |  |  |  |
| 8 | `PPPCC.BillingIndicator` | `PorClientconditions_Billingindicator` |  |  |  |
| 9 | `PPPCC.ChargePostingSeparately` | `PorClientconditions_Chargepostingseparately` |  |  |  |
| 10 | `PPPCC.ChargePostingDetail` | `PorClientconditions_Chargepostingdetail` |  |  |  |
| 11 | `PPPCC.VatPrincipal` | `PorClientconditions_Vatprincipal` |  |  |  |
| 12 | `PPPCC.VATOnCharge` | `PorClientconditions_Vatoncharge` |  |  |  |
| 13 | `PPPCC.NonSTPIndicator` | `PorClientconditions_Nonstpindicator` |  |  |  |
| 14 | `PPPCC.FXNonSTPIndicator` | `PorClientconditions_Fxnonstpindicator` |  |  |  |
| 15 | `PPPCC.FXNonSTPAmount` | `PorClientconditions_Fxnonstpamount` |  |  |  |
| 16 | `PPPCC.ChargeAccountCompanyID` | `PorClientconditions_Chargeaccountcompanyid` |  |  |  |
| 17 | `PPPCC.ChargeAccountNumber` | `PorClientconditions_Chargeaccountnumber` |  |  |  |
| 18 | `PPPCC.ChargeAccountCurrency` | `PorClientconditions_Chargeaccountcurrency` |  |  |  |
| 19 | `PPPCC.SpecialInstructions` | `PorClientconditions_Specialinstructions` |  |  |  |
| 20 | `PPPCC.LeadTime` | `PorClientconditions_Leadtime` |  |  |  |
| 21 | `PPPCC.AccountSubstitution` | `PorClientconditions_Accountsubstitution` |  |  |  |
| 22 | `PPPCC.ReleaseTime` | `PorClientconditions_Releasetime` |  |  |  |
| 23 | `PPPCC.FloatDays` | `PorClientconditions_Floatdays` |  |  |  |
| 24 | `PPPCC.ThresholdAmount` | `PorClientconditions_Thresholdamount` |  |  |  |
| 25 | `PPPCC.BatchACKNACKIndicator` | `PorClientconditions_Batchacknackindicator` |  |  |  |
| 26 | `PPPCC.TranNACKIndicator` | `PorClientconditions_Trannackindicator` |  |  |  |
| 27 | `PPPCC.BalanceCheckOnChgAct` | `PorClientconditions_Balancecheckonchgact` |  |  |  |
| 28 | `PPPCC.InterimStatusIndicator` | `PorClientconditions_Interimstatusindicator` |  |  |  |
| 29 | `PPPCC.CustomerStatusMessageType` | `PorClientconditions_Customerstatusmessagetype` |  |  |  |
| 30 | `PPPCC.TaxId` | `PorClientconditions_Taxid` |  |  |  |
| 31 | `PPPCC.TaxTypeId` | `PorClientconditions_Taxtypeid` |  |  |  |
