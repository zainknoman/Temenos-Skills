# PPT.CLEARINGCOMPANY — Table Schema

> Source: `INSERTS/I_F.PPT.CLEARINGCOMPANY` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCCM.CompanyID` | `PptClearingcompany_Companyid` |  |  |  |
| 2 | `PPCCM.NationalID` | `PptClearingcompany_Nationalid` |  |  |  |
| 3 | `PPCCM.StartDateClearingCompany` | `PptClearingcompany_Startdateclearingcompany` |  |  |  |
| 4 | `PPCCM.ClearingName` | `PptClearingcompany_Clearingname` |  |  |  |
| 5 | `PPCCM.EndDateClearingCompany` | `PptClearingcompany_Enddateclearingcompany` |  |  |  |
| 6 | `PPCCM.RACClearingCompany` | `PptClearingcompany_Racclearingcompany` |  |  |  |
| 7 | `PPCCM.RSCClearingCompany` | `PptClearingcompany_Rscclearingcompany` |  |  |  |
| 8 | `PPCCM.EntryUserID` | `PptClearingcompany_Entryuserid` |  |  |  |
| 9 | `PPCCM.EntryDateTime` | `PptClearingcompany_Entrydatetime` |  |  |  |
| 10 | `PPCCM.ApproverUserID` | `PptClearingcompany_Approveruserid` |  |  |  |
| 11 | `PPCCM.ApprovedDateTime` | `PptClearingcompany_Approveddatetime` |  |  |  |
