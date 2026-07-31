# POR.STATEMENTLINE — Table Schema

> Source: `INSERTS/I_F.POR.STATEMENTLINE` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPOSL.CompanyID` | `PorStatementline_Companyid` |  |  |  |
| 2 | `PPOSL.FTNumber` | `PorStatementline_Ftnumber` |  |  |  |
| 3 | `PPOSL.PostingLineNumber` | `PorStatementline_Postinglinenumber` |  |  |  |
| 4 | `PPOSL.StatementLineNumber` | `PorStatementline_Statementlinenumber` |  |  |  |
| 5 | `PPOSL.StatementLine` | `PorStatementline_Statementline` |  |  |  |
| 6 | `PPOSL.LineContinuityFlag` | `PorStatementline_Linecontinuityflag` |  |  |  |
