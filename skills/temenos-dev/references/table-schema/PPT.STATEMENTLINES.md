# PPT.STATEMENTLINES — Table Schema

> Source: `INSERTS/I_F.PPT.STATEMENTLINES` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSTL.StatementLineId` | `PptStatementlines_Statementlineid` |  |  |  |
| 2 | `PPSTL.StatementFormatID` | `PptStatementlines_Statementformatid` |  |  |  |
| 3 | `PPSTL.LanguageID` | `PptStatementlines_Languageid` |  |  |  |
| 4 | `PPSTL.Tag61Indicator` | `PptStatementlines_Tag61indicator` |  |  |  |
| 5 | `PPSTL.SequenceNumber` | `PptStatementlines_Sequencenumber` |  |  |  |
| 6 | `PPSTL.LiteralText` | `PptStatementlines_Literaltext` |  |  |  |
| 7 | `PPSTL.StatementTextToken` | `PptStatementlines_Statementtexttoken` |  |  |  |
| 8 | `PPSTL.StartPosition` | `PptStatementlines_Startposition` |  |  |  |
| 9 | `PPSTL.AmountFormat` | `PptStatementlines_Amountformat` |  |  |  |
| 10 | `PPSTL.LineContinuityFlag` | `PptStatementlines_Linecontinuityflag` |  |  |  |
| 11 | `PPSTL.CompactLineFlag` | `PptStatementlines_Compactlineflag` |  |  |  |
