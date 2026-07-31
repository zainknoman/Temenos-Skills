# PPL.LORONOSTROACCOUNT — Table Schema

> Source: `INSERTS/I_F.PPL.LORONOSTROACCOUNT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPLNA.LoroNostroAccountID` | `PplLoronostroaccount_Loronostroaccountid` |  |  |  |
| 2 | `PPLNA.CompanyID` | `PplLoronostroaccount_Companyid` |  |  |  |
| 3 | `PPLNA.BICCode` | `PplLoronostroaccount_Biccode` |  |  |  |
| 4 | `PPLNA.AccountNumberType` | `PplLoronostroaccount_Accountnumbertype` |  |  |  |
| 5 | `PPLNA.AccountNumberCompanyID` | `PplLoronostroaccount_Accountnumbercompanyid` |  |  |  |
| 6 | `PPLNA.AccountNumber` | `PplLoronostroaccount_Accountnumber` |  |  |  |
| 7 | `PPLNA.AccountCurrency` | `PplLoronostroaccount_Accountcurrency` |  |  |  |
| 8 | `PPLNA.StartDateAccount` | `PplLoronostroaccount_Startdateaccount` |  |  |  |
| 9 | `PPLNA.OwningBIC` | `PplLoronostroaccount_Owningbic` |  |  |  |
| 10 | `PPLNA.PreferredDebitAccountNumber` | `PplLoronostroaccount_Preferreddebitaccountnumber` |  |  |  |
| 11 | `PPLNA.ChargesIndicator` | `PplLoronostroaccount_Chargesindicator` |  |  |  |
| 12 | `PPLNA.PreferredCreditAccountNumber` | `PplLoronostroaccount_Preferredcreditaccountnumber` |  |  |  |
| 13 | `PPLNA.EndDateAccount` | `PplLoronostroaccount_Enddateaccount` |  |  |  |
| 14 | `PPLNA.RACLoroNostroAccount` | `PplLoronostroaccount_Racloronostroaccount` |  |  |  |
| 15 | `PPLNA.RSCLoroNostroAccount` | `PplLoronostroaccount_Rscloronostroaccount` |  |  |  |
| 16 | `PPLNA.EntryUserID` | `PplLoronostroaccount_Entryuserid` |  |  |  |
| 17 | `PPLNA.EntryDateTime` | `PplLoronostroaccount_Entrydatetime` |  |  |  |
| 18 | `PPLNA.ApproverUserID` | `PplLoronostroaccount_Approveruserid` |  |  |  |
| 19 | `PPLNA.ApprovedDateTime` | `PplLoronostroaccount_Approveddatetime` |  |  |  |
| 20 | `PPLNA.AccountNumberInHoldingBk` | `PplLoronostroaccount_Accountnumberinholdingbk` |  |  |  |
| 21 | `PPLNA.AccountShortName` | `PplLoronostroaccount_Accountshortname` |  |  |  |
