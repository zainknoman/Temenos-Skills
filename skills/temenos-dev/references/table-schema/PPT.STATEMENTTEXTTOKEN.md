# PPT.STATEMENTTEXTTOKEN — Table Schema

> Source: `INSERTS/I_F.PPT.STATEMENTTEXTTOKEN` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSTT.CompanyID` | `PptStatementtexttoken_Companyid` |  |  |  |
| 2 | `PPSTT.StatementTextToken` | `PptStatementtexttoken_Statementtexttoken` |  |  |  |
| 3 | `PPSTT.RACStatementTextToken` | `PptStatementtexttoken_Racstatementtexttoken` |  |  |  |
| 4 | `PPSTT.RSCStatementTextToken` | `PptStatementtexttoken_Rscstatementtexttoken` |  |  |  |
| 5 | `PPSTT.EntryUserID` | `PptStatementtexttoken_Entryuserid` |  |  |  |
| 6 | `PPSTT.EntryDateTime` | `PptStatementtexttoken_Entrydatetime` |  |  |  |
| 7 | `PPSTT.ApproverUserID` | `PptStatementtexttoken_Approveruserid` |  |  |  |
| 8 | `PPSTT.ApprovedDateTime` | `PptStatementtexttoken_Approveddatetime` |  |  |  |
