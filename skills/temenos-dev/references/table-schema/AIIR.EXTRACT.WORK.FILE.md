# AIIR.EXTRACT.WORK.FILE — Table Schema

> Source: `INSERTS/I_F.AIIR.EXTRACT.WORK.FILE` in `AUIVIC_InvestmentIncomeReport.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AIIR.WORK.EXTRACT.LINE` | `AiirExtractWorkFile_ExtractLine` |  |  |  |
| 2 | `AIIR.WORK.RESERVED.1` | `AiirExtractWorkFile_Reserved1` | TField |  | Reserved for future use |
| 3 | `AIIR.WORK.RESERVED.2` | `AiirExtractWorkFile_Reserved2` | TField |  | Reserved for future use |
| 4 | `AIIR.WORK.RESERVED.3` | `AiirExtractWorkFile_Reserved3` | TField |  | Reserved for future use |
| 5 | `AIIR.WORK.RESERVED.4` | `AiirExtractWorkFile_Reserved4` | TField |  | Reserved for future use |
| 6 | `AIIR.WORK.RESERVED.5` | `AiirExtractWorkFile_Reserved5` | TField |  | Reserved for future use |
| 7 | `AIIR.WORK.RESERVED.6` | `AiirExtractWorkFile_Reserved6` | TField |  | Reserved for future use |
| 8 | `AIIR.WORK.RESERVED.7` | `AiirExtractWorkFile_Reserved7` | TField |  | Reserved for future use |
| 9 | `AIIR.WORK.RESERVED.8` | `AiirExtractWorkFile_Reserved8` | TField |  | Reserved for future use |
| 10 | `AIIR.WORK.RESERVED.9` | `AiirExtractWorkFile_Reserved9` | TField |  | Reserved for future use |
| 11 | `AIIR.WORK.RESERVED.10` | `AiirExtractWorkFile_Reserved10` | TField |  | Reserved for future use |
| 12 | `AIIR.WORK.LOCAL.REF` | `AiirExtractWorkFile_LocalRef` |  |  |  |
