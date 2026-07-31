# PPT.CLAIMS — Table Schema

> Source: `INSERTS/I_F.PPT.CLAIMS` in `PP_ClaimsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCL.CompanyID` | `PptClaims_Companyid` |  |  |  |
| 2 | `PPCL.CurrencyCode` | `PptClaims_Currencycode` |  |  |  |
| 3 | `PPCL.StartDateClaim` | `PptClaims_Startdateclaim` |  |  |  |
| 4 | `PPCL.ExpectedClaimAccountCompany` | `PptClaims_Expectedclaimaccountcompany` |  |  |  |
| 5 | `PPCL.ExpectedClaimAccount` | `PptClaims_Expectedclaimaccount` |  |  |  |
| 6 | `PPCL.ExpectedClaimAccountCurrency` | `PptClaims_Expectedclaimaccountcurrency` |  |  |  |
| 7 | `PPCL.ExpectedPLAccountCompany` | `PptClaims_Expectedplaccountcompany` |  |  |  |
| 8 | `PPCL.ExpectedPLAccount` | `PptClaims_Expectedplaccount` |  |  |  |
| 9 | `PPCL.ExpectedPLAccountCurrency` | `PptClaims_Expectedplaccountcurrency` |  |  |  |
| 10 | `PPCL.PLAccountCompany` | `PptClaims_Placcountcompany` |  |  |  |
| 11 | `PPCL.PLAccount` | `PptClaims_Placcount` |  |  |  |
| 12 | `PPCL.PLAccountCurrency` | `PptClaims_Placcountcurrency` |  |  |  |
| 13 | `PPCL.EndDateClaim` | `PptClaims_Enddateclaim` |  |  |  |
| 14 | `PPCL.RACClaim` | `PptClaims_Racclaim` |  |  |  |
| 15 | `PPCL.RSCClaim` | `PptClaims_Rscclaim` |  |  |  |
| 16 | `PPCL.EntryUserID` | `PptClaims_Entryuserid` |  |  |  |
| 17 | `PPCL.EntryDateTime` | `PptClaims_Entrydatetime` |  |  |  |
| 18 | `PPCL.ApproverUserID` | `PptClaims_Approveruserid` |  |  |  |
| 19 | `PPCL.ApprovedDateTime` | `PptClaims_Approveddatetime` |  |  |  |
