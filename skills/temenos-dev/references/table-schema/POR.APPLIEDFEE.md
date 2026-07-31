# POR.APPLIEDFEE — Table Schema

> Source: `INSERTS/I_F.POR.APPLIEDFEE` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPAF.CompanyID` | `PorAppliedfee_Companyid` |  |  |  |
| 2 | `PPPAF.FTNumber` | `PorAppliedfee_Ftnumber` |  |  |  |
| 3 | `PPPAF.ChargePartyIndicator` | `PorAppliedfee_Chargepartyindicator` |  |  |  |
| 4 | `PPPAF.FeeType` | `PorAppliedfee_Feetype` |  |  |  |
| 5 | `PPPAF.ChargeSign` | `PorAppliedfee_Chargesign` |  |  |  |
| 6 | `PPPAF.TypeOfCharge` | `PorAppliedfee_Typeofcharge` |  |  |  |
| 7 | `PPPAF.FeeDescription` | `PorAppliedfee_Feedescription` |  |  |  |
| 8 | `PPPAF.ChargeAmount` | `PorAppliedfee_Chargeamount` |  |  |  |
| 9 | `PPPAF.ChargeAmountCurrency` | `PorAppliedfee_Chargeamountcurrency` |  |  |  |
| 10 | `PPPAF.ChargeAmountLocalCurrency` | `PorAppliedfee_Chargeamountlocalcurrency` |  |  |  |
| 11 | `PPPAF.LocalCurrencyCode` | `PorAppliedfee_Localcurrencycode` |  |  |  |
| 12 | `PPPAF.ChargeAmountFeeCurrency` | `PorAppliedfee_Chargeamountfeecurrency` |  |  |  |
| 13 | `PPPAF.FeeCurrencyCode` | `PorAppliedfee_Feecurrencycode` |  |  |  |
| 14 | `PPPAF.PLAccountCompany` | `PorAppliedfee_Placcountcompany` |  |  |  |
| 15 | `PPPAF.PLAccountNumber` | `PorAppliedfee_Placcountnumber` |  |  |  |
| 16 | `PPPAF.PLAccountCurrency` | `PorAppliedfee_Placcountcurrency` |  |  |  |
| 17 | `PPPAF.ParentChildIndicator` | `PorAppliedfee_Parentchildindicator` |  |  |  |
| 18 | `PPPAF.OutgoingOurChargeIndicator` | `PorAppliedfee_Outgoingourchargeindicator` |  |  |  |
| 19 | `PPPAF.ClientChargesID` | `PorAppliedfee_Clientchargesid` |  |  |  |
| 20 | `PPPAF.BankChargesID` | `PorAppliedfee_Bankchargesid` |  |  |  |
| 21 | `PPPAF.TaxIndicator` | `PorAppliedfee_Taxindicator` |  |  |  |
| 22 | `PPPAF.TaxPercentage` | `PorAppliedfee_Taxpercentage` |  |  |  |
| 23 | `PPPAF.AmountForTaxLocalCurrency` | `PorAppliedfee_Amountfortaxlocalcurrency` |  |  |  |
| 24 | `PPPAF.AmountForTaxFeeCurrency` | `PorAppliedfee_Amountfortaxfeecurrency` |  |  |  |
| 25 | `PPPAF.TaxAmount` | `PorAppliedfee_Taxamount` |  |  |  |
| 26 | `PPPAF.TaxAmountLocalCcy` | `PorAppliedfee_Taxamountlocalccy` |  |  |  |
