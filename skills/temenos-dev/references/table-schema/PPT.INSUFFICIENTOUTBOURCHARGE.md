# PPT.INSUFFICIENTOUTBOURCHARGE — Table Schema

> Source: `INSERTS/I_F.PPT.INSUFFICIENTOUTBOURCHARGE` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPIOO.CompanyID` | `PptInsufficientoutbourcharge_Companyid` |  |  |  |
| 2 | `PPIOO.Currency` | `PptInsufficientoutbourcharge_Currency` |  |  |  |
| 3 | `PPIOO.StartDateInsuffOutbOurCharge` | `PptInsufficientoutbourcharge_Startdateinsuffoutbourcharge` |  |  |  |
| 4 | `PPIOO.AccountType` | `PptInsufficientoutbourcharge_Accounttype` |  |  |  |
| 5 | `PPIOO.AccountCompanyID` | `PptInsufficientoutbourcharge_Accountcompanyid` |  |  |  |
| 6 | `PPIOO.Account` | `PptInsufficientoutbourcharge_Account` |  |  |  |
| 7 | `PPIOO.AccountCurrency` | `PptInsufficientoutbourcharge_Accountcurrency` |  |  |  |
| 8 | `PPIOO.EndDateInsuffOutbOurCharge` | `PptInsufficientoutbourcharge_Enddateinsuffoutbourcharge` |  |  |  |
| 9 | `PPIOO.RACInsufficientOutbOurCharge` | `PptInsufficientoutbourcharge_Racinsufficientoutbourcharge` |  |  |  |
| 10 | `PPIOO.RSCInsufficientOutbOurCharge` | `PptInsufficientoutbourcharge_Rscinsufficientoutbourcharge` |  |  |  |
| 11 | `PPIOO.EntryUserID` | `PptInsufficientoutbourcharge_Entryuserid` |  |  |  |
| 12 | `PPIOO.EntryDateTime` | `PptInsufficientoutbourcharge_Entrydatetime` |  |  |  |
| 13 | `PPIOO.ApproverUserID` | `PptInsufficientoutbourcharge_Approveruserid` |  |  |  |
| 14 | `PPIOO.ApprovedDateTime` | `PptInsufficientoutbourcharge_Approveddatetime` |  |  |  |
