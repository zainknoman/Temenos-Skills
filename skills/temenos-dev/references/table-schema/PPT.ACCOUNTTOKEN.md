# PPT.ACCOUNTTOKEN — Table Schema

> Source: `INSERTS/I_F.PPT.ACCOUNTTOKEN` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPACT.CompanyID` | `PptAccounttoken_Companyid` |  |  |  |
| 2 | `PPACT.AccountToken` | `PptAccounttoken_Accounttoken` |  |  |  |
| 3 | `PPACT.RACAccountToken` | `PptAccounttoken_Racaccounttoken` |  |  |  |
| 4 | `PPACT.RSCAccountToken` | `PptAccounttoken_Rscaccounttoken` |  |  |  |
| 5 | `PPACT.EntryUserID` | `PptAccounttoken_Entryuserid` |  |  |  |
| 6 | `PPACT.EntryDateTime` | `PptAccounttoken_Entrydatetime` |  |  |  |
| 7 | `PPACT.ApproverUserID` | `PptAccounttoken_Approveruserid` |  |  |  |
| 8 | `PPACT.ApprovedDateTime` | `PptAccounttoken_Approveddatetime` |  |  |  |
