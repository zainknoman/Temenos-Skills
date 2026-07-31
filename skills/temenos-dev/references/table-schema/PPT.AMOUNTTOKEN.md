# PPT.AMOUNTTOKEN — Table Schema

> Source: `INSERTS/I_F.PPT.AMOUNTTOKEN` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPAMT.CompanyID` | `PptAmounttoken_Companyid` |  |  |  |
| 2 | `PPAMT.AmountToken` | `PptAmounttoken_Amounttoken` |  |  |  |
| 3 | `PPAMT.RACAmountToken` | `PptAmounttoken_Racamounttoken` |  |  |  |
| 4 | `PPAMT.RSCAmountToken` | `PptAmounttoken_Rscamounttoken` |  |  |  |
| 5 | `PPAMT.EntryUserID` | `PptAmounttoken_Entryuserid` |  |  |  |
| 6 | `PPAMT.EntryDateTime` | `PptAmounttoken_Entrydatetime` |  |  |  |
| 7 | `PPAMT.ApproverUserID` | `PptAmounttoken_Approveruserid` |  |  |  |
| 8 | `PPAMT.ApprovedDateTime` | `PptAmounttoken_Approveddatetime` |  |  |  |
