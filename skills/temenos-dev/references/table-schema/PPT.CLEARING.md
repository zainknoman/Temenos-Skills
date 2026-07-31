# PPT.CLEARING — Table Schema

> Source: `INSERTS/I_F.PPT.CLEARING` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCG.CompanyID` | `PptClearing_Companyid` |  |  |  |
| 2 | `PPCG.ClearingID` | `PptClearing_Clearingid` |  |  |  |
| 3 | `PPCG.ClearingCurrency` | `PptClearing_Clearingcurrency` |  |  |  |
| 4 | `PPCG.StartDateClearing` | `PptClearing_Startdateclearing` |  |  |  |
| 5 | `PPCG.ClearingCountryCode` | `PptClearing_Clearingcountrycode` |  |  |  |
| 6 | `PPCG.ClearingName` | `PptClearing_Clearingname` |  |  |  |
| 7 | `PPCG.ClearingFileTransactionInd` | `PptClearing_Clearingfiletransactionind` |  |  |  |
| 8 | `PPCG.RTGSSystem` | `PptClearing_Rtgssystem` |  |  |  |
| 9 | `PPCG.EndDateClearing` | `PptClearing_Enddateclearing` |  |  |  |
| 10 | `PPCG.RACClearing` | `PptClearing_Racclearing` |  |  |  |
| 11 | `PPCG.RSCClearing` | `PptClearing_Rscclearing` |  |  |  |
| 12 | `PPCG.EntryUserID` | `PptClearing_Entryuserid` |  |  |  |
| 13 | `PPCG.EntryDateTime` | `PptClearing_Entrydatetime` |  |  |  |
| 14 | `PPCG.ApproverUserID` | `PptClearing_Approveruserid` |  |  |  |
| 15 | `PPCG.ApprovedDateTime` | `PptClearing_Approveddatetime` |  |  |  |
| 16 | `PPCG.SendingBIC` | `PptClearing_Sendingbic` |  |  |  |
| 17 | `PPCG.RMACheck` | `PptClearing_Rmacheck` |  |  |  |
| 18 | `PPCG.MaxTransPerBulk` | `PptClearing_Maxtransperbulk` |  |  |  |
| 19 | `PPCG.MaxBulksPerFile` | `PptClearing_Maxbulksperfile` |  |  |  |
| 20 | `PPCG.MaxFilesPerCycle` | `PptClearing_Maxfilespercycle` |  |  |  |
| 21 | `PPCG.BulkingCriteriaAPI` | `PptClearing_Bulkingcriteriaapi` |  |  |  |
| 22 | `PPCG.FileGenerationRequired` | `PptClearing_Filegenerationrequired` |  |  |  |
| 23 | `PPCG.FilingCriteriaAPI` | `PptClearing_Filingcriteriaapi` |  |  |  |
| 24 | `PPCG.ClearingBIC` | `PptClearing_Clearingbic` |  |  |  |
