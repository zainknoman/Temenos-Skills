# PPL.CLIENTCHARGES — Table Schema

> Source: `INSERTS/I_F.PPL.CLIENTCHARGES` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCC.ClientChargesID` | `PplClientcharges_Clientchargesid` |  |  |  |
| 2 | `PPCC.CompanyID` | `PplClientcharges_Companyid` |  |  |  |
| 3 | `PPCC.FeeProduct` | `PplClientcharges_Feeproduct` |  |  |  |
| 4 | `PPCC.SourceProduct` | `PplClientcharges_Sourceproduct` |  |  |  |
| 5 | `PPCC.BusinessLine` | `PplClientcharges_Businessline` |  |  |  |
| 6 | `PPCC.ClientID` | `PplClientcharges_Clientid` |  |  |  |
| 7 | `PPCC.CustomerAccountNumberCompID` | `PplClientcharges_Customeraccountnumbercompid` |  |  |  |
| 8 | `PPCC.CustomerAccountNumber` | `PplClientcharges_Customeraccountnumber` |  |  |  |
| 9 | `PPCC.CustomerAccountCurrency` | `PplClientcharges_Customeraccountcurrency` |  |  |  |
| 10 | `PPCC.ResidencyStatus` | `PplClientcharges_Residencystatus` |  |  |  |
| 11 | `PPCC.StartDateClientCharges` | `PplClientcharges_Startdateclientcharges` |  |  |  |
| 12 | `PPCC.CommonCurrency` | `PplClientcharges_Commoncurrency` |  |  |  |
| 13 | `PPCC.EndDateClientCharges` | `PplClientcharges_Enddateclientcharges` |  |  |  |
| 14 | `PPCC.RACClientCharges` | `PplClientcharges_Racclientcharges` |  |  |  |
| 15 | `PPCC.RSCClientCharges` | `PplClientcharges_Rscclientcharges` |  |  |  |
| 16 | `PPCC.EntryUserID` | `PplClientcharges_Entryuserid` |  |  |  |
| 17 | `PPCC.EntryDateTime` | `PplClientcharges_Entrydatetime` |  |  |  |
| 18 | `PPCC.ApproverUserID` | `PplClientcharges_Approveruserid` |  |  |  |
| 19 | `PPCC.ApprovedDateTime` | `PplClientcharges_Approveddatetime` |  |  |  |
