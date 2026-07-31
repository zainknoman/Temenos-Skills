# PPL.BANKCHARGES — Table Schema

> Source: `INSERTS/I_F.PPL.BANKCHARGES` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCH.BankChargesID` | `PplBankcharges_Bankchargesid` |  |  |  |
| 2 | `PPBCH.CompanyID` | `PplBankcharges_Companyid` |  |  |  |
| 3 | `PPBCH.SendingOrReceivingBankCharge` | `PplBankcharges_Sendingorreceivingbankcharge` |  |  |  |
| 4 | `PPBCH.CorrespondentBIC` | `PplBankcharges_Correspondentbic` |  |  |  |
| 5 | `PPBCH.CTRBTRIndicator` | `PplBankcharges_Ctrbtrindicator` |  |  |  |
| 6 | `PPBCH.SLACode` | `PplBankcharges_Slacode` |  |  |  |
| 7 | `PPBCH.CurrencyCode` | `PplBankcharges_Currencycode` |  |  |  |
| 8 | `PPBCH.CountryCodeDestination` | `PplBankcharges_Countrycodedestination` |  |  |  |
| 9 | `PPBCH.StartDateBankCharges` | `PplBankcharges_Startdatebankcharges` |  |  |  |
| 10 | `PPBCH.Include71GIndicator` | `PplBankcharges_Include71gindicator` |  |  |  |
| 11 | `PPBCH.CommonCurrency` | `PplBankcharges_Commoncurrency` |  |  |  |
| 12 | `PPBCH.EndDateBankCharges` | `PplBankcharges_Enddatebankcharges` |  |  |  |
| 13 | `PPBCH.RACBankCharges` | `PplBankcharges_Racbankcharges` |  |  |  |
| 14 | `PPBCH.RSCBankCharges` | `PplBankcharges_Rscbankcharges` |  |  |  |
| 15 | `PPBCH.EntryUserID` | `PplBankcharges_Entryuserid` |  |  |  |
| 16 | `PPBCH.EntryDateTime` | `PplBankcharges_Entrydatetime` |  |  |  |
| 17 | `PPBCH.ApproverUserID` | `PplBankcharges_Approveruserid` |  |  |  |
| 18 | `PPBCH.ApprovedDateTime` | `PplBankcharges_Approveddatetime` |  |  |  |
