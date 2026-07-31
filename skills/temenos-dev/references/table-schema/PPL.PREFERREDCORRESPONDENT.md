# PPL.PREFERREDCORRESPONDENT — Table Schema

> Source: `INSERTS/I_F.PPL.PREFERREDCORRESPONDENT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPCT.PreferredCorrespondentID` | `PplPreferredcorrespondent_Preferredcorrespondentid` |  |  |  |
| 2 | `PPPCT.CompanyID` | `PplPreferredcorrespondent_Companyid` |  |  |  |
| 3 | `PPPCT.DestinationCountryCode` | `PplPreferredcorrespondent_Destinationcountrycode` |  |  |  |
| 4 | `PPPCT.TransactionCurrency` | `PplPreferredcorrespondent_Transactioncurrency` |  |  |  |
| 5 | `PPPCT.RoutingProduct` | `PplPreferredcorrespondent_Routingproduct` |  |  |  |
| 6 | `PPPCT.StartDatePreferredCorr` | `PplPreferredcorrespondent_Startdatepreferredcorr` |  |  |  |
| 7 | `PPPCT.PrefCorrespondentIDType` | `PplPreferredcorrespondent_Prefcorrespondentidtype` |  |  |  |
| 8 | `PPPCT.PrefCorrespondentID` | `PplPreferredcorrespondent_Prefcorrespondentid` |  |  |  |
| 9 | `PPPCT.EndDatePreferredCorr` | `PplPreferredcorrespondent_Enddatepreferredcorr` |  |  |  |
| 10 | `PPPCT.RACPreferredCorrespondent` | `PplPreferredcorrespondent_Racpreferredcorrespondent` |  |  |  |
| 11 | `PPPCT.RSCPreferredCorrespondent` | `PplPreferredcorrespondent_Rscpreferredcorrespondent` |  |  |  |
| 12 | `PPPCT.EntryUserID` | `PplPreferredcorrespondent_Entryuserid` |  |  |  |
| 13 | `PPPCT.EntryDateTime` | `PplPreferredcorrespondent_Entrydatetime` |  |  |  |
| 14 | `PPPCT.ApproverUserID` | `PplPreferredcorrespondent_Approveruserid` |  |  |  |
| 15 | `PPPCT.ApprovedDateTime` | `PplPreferredcorrespondent_Approveddatetime` |  |  |  |
