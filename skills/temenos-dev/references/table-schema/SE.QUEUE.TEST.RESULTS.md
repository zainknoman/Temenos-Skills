# SE.QUEUE.TEST.RESULTS — Table Schema

> Source: `INSERTS/I_F.SE.QUEUE.TEST.RESULTS` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `QUEUE.TR.TEST.NUMBER` | `SeQueueTestResults_TestNumber` |  |  |  |
| 2 | `QUEUE.TR.TEST.DESCRIPTION` | `SeQueueTestResults_TestDescription` |  |  |  |
| 3 | `QUEUE.TR.RESULT` | `SeQueueTestResults_Result` |  |  |  |
| 4 | `QUEUE.TR.RESERVED.5` | `SeQueueTestResults_Reserved5` | TField |  |  |
| 5 | `QUEUE.TR.RESERVED.4` | `SeQueueTestResults_Reserved4` | TField |  |  |
| 6 | `QUEUE.TR.RESERVED.3` | `SeQueueTestResults_Reserved3` | TField |  |  |
| 7 | `QUEUE.TR.RESERVED.2` | `SeQueueTestResults_Reserved2` | TField |  |  |
| 8 | `QUEUE.TR.RESERVED.1` | `SeQueueTestResults_Reserved1` | TField |  |  |
