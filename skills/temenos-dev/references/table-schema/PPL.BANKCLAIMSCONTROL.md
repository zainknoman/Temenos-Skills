# PPL.BANKCLAIMSCONTROL — Table Schema

> Source: `INSERTS/I_F.PPL.BANKCLAIMSCONTROL` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCL.BankClaimsControlID` | `PplBankclaimscontrol_Bankclaimscontrolid` |  |  |  |
| 2 | `PPBCL.CompanyID` | `PplBankclaimscontrol_Companyid` |  |  |  |
| 3 | `PPBCL.CorrespondentBIC` | `PplBankclaimscontrol_Correspondentbic` |  |  |  |
| 4 | `PPBCL.CurrencyCode` | `PplBankclaimscontrol_Currencycode` |  |  |  |
| 5 | `PPBCL.StartDateBankClaimsControl` | `PplBankclaimscontrol_Startdatebankclaimscontrol` |  |  |  |
| 6 | `PPBCL.ClaimType` | `PplBankclaimscontrol_Claimtype` |  |  |  |
| 7 | `PPBCL.ClaimTowards` | `PplBankclaimscontrol_Claimtowards` |  |  |  |
| 8 | `PPBCL.ClaimBIC` | `PplBankclaimscontrol_Claimbic` |  |  |  |
| 9 | `PPBCL.ClaimBasis` | `PplBankclaimscontrol_Claimbasis` |  |  |  |
| 10 | `PPBCL.ClaimPeriod` | `PplBankclaimscontrol_Claimperiod` |  |  |  |
| 11 | `PPBCL.ClaimTrigger` | `PplBankclaimscontrol_Claimtrigger` |  |  |  |
| 12 | `PPBCL.IndividualGroupIndicator` | `PplBankclaimscontrol_Individualgroupindicator` |  |  |  |
| 13 | `PPBCL.EndDateBankClaimsControl` | `PplBankclaimscontrol_Enddatebankclaimscontrol` |  |  |  |
| 14 | `PPBCL.RACBankClaimsControl` | `PplBankclaimscontrol_Racbankclaimscontrol` |  |  |  |
| 15 | `PPBCL.RSCBankClaimsControl` | `PplBankclaimscontrol_Rscbankclaimscontrol` |  |  |  |
| 16 | `PPBCL.EntryUserID` | `PplBankclaimscontrol_Entryuserid` |  |  |  |
| 17 | `PPBCL.EntryDateTime` | `PplBankclaimscontrol_Entrydatetime` |  |  |  |
| 18 | `PPBCL.ApproverUserID` | `PplBankclaimscontrol_Approveruserid` |  |  |  |
| 19 | `PPBCL.ApprovedDateTime` | `PplBankclaimscontrol_Approveddatetime` |  |  |  |
