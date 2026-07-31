# PW.INFLOW.SEQUENCE — Table Schema

> Source: `INSERTS/I_F.PW.INFLOW.SEQUENCE` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.INF.SEQ.SEQUENCE.TYPE` | `PwInflowSequence_SequenceType` | TField |  | Describes the sequence type of the inflow request. Validation: Should be either PARTIAL or FULL. |
| 2 | `PW.INF.SEQ.SEQUENCE.START` | `PwInflowSequence_SequenceStart` | TField |  | Defines the start of the inflow sequence request. |
| 3 | `PW.INF.SEQ.SEQUENCE.PACE` | `PwInflowSequence_SequencePace` | TField |  | Defines the pace difference in between each sequence requests. |
| 4 | `PW.INF.SEQ.LAST.PROCESSED` | `PwInflowSequence_LastProcessed` | TField |  | Defines the sequence number of the request which was last processed successfully. |
| 5 | `PW.INF.SEQ.RESERVED.10` | `PwInflowSequence_Reserved10` | TField |  |  |
| 6 | `PW.INF.SEQ.RESERVED.9` | `PwInflowSequence_Reserved9` | TField |  |  |
| 7 | `PW.INF.SEQ.RESERVED.8` | `PwInflowSequence_Reserved8` | TField |  |  |
| 8 | `PW.INF.SEQ.RESERVED.7` | `PwInflowSequence_Reserved7` | TField |  |  |
| 9 | `PW.INF.SEQ.RESERVED.6` | `PwInflowSequence_Reserved6` | TField |  |  |
| 10 | `PW.INF.SEQ.RESERVED.5` | `PwInflowSequence_Reserved5` | TField |  |  |
| 11 | `PW.INF.SEQ.RESERVED.4` | `PwInflowSequence_Reserved4` | TField |  |  |
| 12 | `PW.INF.SEQ.RESERVED.3` | `PwInflowSequence_Reserved3` | TField |  |  |
| 13 | `PW.INF.SEQ.RESERVED.2` | `PwInflowSequence_Reserved2` | TField |  |  |
| 14 | `PW.INF.SEQ.RESERVED.1` | `PwInflowSequence_Reserved1` | TField |  |  |
