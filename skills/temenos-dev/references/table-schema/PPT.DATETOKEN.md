# PPT.DATETOKEN — Table Schema

> Source: `INSERTS/I_F.PPT.DATETOKEN` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPDT.CompanyID` | `PptDatetoken_Companyid` |  |  |  |
| 2 | `PPDT.DateToken` | `PptDatetoken_Datetoken` |  |  |  |
| 3 | `PPDT.RACDateToken` | `PptDatetoken_Racdatetoken` |  |  |  |
| 4 | `PPDT.RSCDateToken` | `PptDatetoken_Rscdatetoken` |  |  |  |
| 5 | `PPDT.EntryUserID` | `PptDatetoken_Entryuserid` |  |  |  |
| 6 | `PPDT.EntryDateTime` | `PptDatetoken_Entrydatetime` |  |  |  |
| 7 | `PPDT.ApproverUserID` | `PptDatetoken_Approveruserid` |  |  |  |
| 8 | `PPDT.ApprovedDateTime` | `PptDatetoken_Approveddatetime` |  |  |  |
