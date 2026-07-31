# CO.EXCEPTIONS — Table Schema

> Source: `INSERTS/I_F.CO.EXCEPTIONS` in `CO_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.EXC.SOURCE.APPLICATION` | `CoExceptions_SourceApplication` | TField |  |  |
| 2 | `CO.EXC.EXCEPTION.APPLICATION` | `CoExceptions_ExceptionApplication` |  |  |  |
| 3 | `CO.EXC.EXCEPTION.ID` | `CoExceptions_ExceptionId` |  |  |  |
| 4 | `CO.EXC.EXCEPTION.MSG` | `CoExceptions_ExceptionMsg` |  |  |  |
| 5 | `CO.EXC.UPDATED.DATE` | `CoExceptions_UpdatedDate` |  |  |  |
| 6 | `CO.EXC.UPDATED.TIME` | `CoExceptions_UpdatedTime` |  |  |  |
