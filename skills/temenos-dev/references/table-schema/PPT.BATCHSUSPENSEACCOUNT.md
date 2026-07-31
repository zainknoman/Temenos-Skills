# PPT.BATCHSUSPENSEACCOUNT — Table Schema

> Source: `INSERTS/I_F.PPT.BATCHSUSPENSEACCOUNT` in `PP_BatchServerService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBSA.CompanyID` | `PptBatchsuspenseaccount_Companyid` |  |  |  |
| 2 | `PPBSA.CurrencyCode` | `PptBatchsuspenseaccount_Currencycode` |  |  |  |
| 3 | `PPBSA.StartDateBatchSuspenseAccount` | `PptBatchsuspenseaccount_Startdatebatchsuspenseaccount` |  |  |  |
| 4 | `PPBSA.SuspenseAccountCompanyID` | `PptBatchsuspenseaccount_Suspenseaccountcompanyid` |  |  |  |
| 5 | `PPBSA.SuspenseAccount` | `PptBatchsuspenseaccount_Suspenseaccount` |  |  |  |
| 6 | `PPBSA.SuspenseAccountCurrency` | `PptBatchsuspenseaccount_Suspenseaccountcurrency` |  |  |  |
| 7 | `PPBSA.EndDateBatchSuspenseAccount` | `PptBatchsuspenseaccount_Enddatebatchsuspenseaccount` |  |  |  |
| 8 | `PPBSA.RACBatchSuspenseAccount` | `PptBatchsuspenseaccount_Racbatchsuspenseaccount` |  |  |  |
| 9 | `PPBSA.RSCBatchSuspenseAccount` | `PptBatchsuspenseaccount_Rscbatchsuspenseaccount` |  |  |  |
| 10 | `PPBSA.EntryUserID` | `PptBatchsuspenseaccount_Entryuserid` |  |  |  |
| 11 | `PPBSA.EntryDateTime` | `PptBatchsuspenseaccount_Entrydatetime` |  |  |  |
| 12 | `PPBSA.ApproverUserID` | `PptBatchsuspenseaccount_Approveruserid` |  |  |  |
| 13 | `PPBSA.ApprovedDateTime` | `PptBatchsuspenseaccount_Approveddatetime` |  |  |  |
