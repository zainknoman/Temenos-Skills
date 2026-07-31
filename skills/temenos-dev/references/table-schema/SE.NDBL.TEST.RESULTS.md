# SE.NDBL.TEST.RESULTS — Table Schema

> Source: `INSERTS/I_F.SE.NDBL.TEST.RESULTS` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NDBL.TR.TEST.NUMBER` | `SeNdblTestResults_TestNumber` |  |  |  |
| 2 | `NDBL.TR.TEST.DESCRIPTION` | `SeNdblTestResults_TestDescription` |  |  |  |
| 3 | `NDBL.TR.EXPECTED.VALUE` | `SeNdblTestResults_ExpectedValue` |  |  |  |
| 4 | `NDBL.TR.RESULT` | `SeNdblTestResults_Result` |  |  |  |
| 5 | `NDBL.TR.ACTUAL.VALUE` | `SeNdblTestResults_ActualValue` |  |  |  |
| 6 | `NDBL.TR.RESERVED.5` | `SeNdblTestResults_Reserved5` | TField |  |  |
| 7 | `NDBL.TR.RESERVED.4` | `SeNdblTestResults_Reserved4` | TField |  |  |
| 8 | `NDBL.TR.RESERVED.3` | `SeNdblTestResults_Reserved3` | TField |  |  |
| 9 | `NDBL.TR.RESERVED.2` | `SeNdblTestResults_Reserved2` | TField |  |  |
| 10 | `NDBL.TR.RESERVED.1` | `SeNdblTestResults_Reserved1` | TField |  |  |
