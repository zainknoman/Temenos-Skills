# PW.INFLOW.SEQUENCE.QUEUE — Table Schema

> Source: `INSERTS/I_F.PW.INFLOW.SEQUENCE.QUEUE` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.INFQ.SEQUENCE.TYPE` | `PwInflowSequenceQueue_SequenceType` | TField |  | Describes the sequence type of the inflow request. The sequence type shall always be FULL |
| 2 | `PW.INFQ.SEQUENCE.START` | `PwInflowSequenceQueue_SequenceStart` | TField |  | Defines the start of the inflow sequence request. |
| 3 | `PW.INFQ.SEQUENCE.PACE` | `PwInflowSequenceQueue_SequencePace` | TField |  | Defines the pace difference in between each sequence requests. |
| 4 | `PW.INFQ.CURRENT.SEQUENCE` | `PwInflowSequenceQueue_CurrentSequence` | TField |  | Defines the sequence number of the request that is parked. This number along with the PW Process Definition nameform the table Id. |
| 5 | `PW.INFQ.UNIQUE.REFERENCE` | `PwInflowSequenceQueue_UniqueReference` | TField |  | Defines the UUID of the request that is parked. This identifier is sent from Inflow runtime. |
| 6 | `PW.INFQ.PAYLOAD` | `PwInflowSequenceQueue_Payload` | TField |  | Holds the entire payload for the sequence that is to be processed. The value markers in the payload are convertedto separators before storing here. |
| 7 | `PW.INFQ.RESERVED.10` | `PwInflowSequenceQueue_Reserved10` | TField |  |  |
| 8 | `PW.INFQ.RESERVED.9` | `PwInflowSequenceQueue_Reserved9` | TField |  |  |
| 9 | `PW.INFQ.RESERVED.8` | `PwInflowSequenceQueue_Reserved8` | TField |  |  |
| 10 | `PW.INFQ.RESERVED.7` | `PwInflowSequenceQueue_Reserved7` | TField |  |  |
| 11 | `PW.INFQ.RESERVED.6` | `PwInflowSequenceQueue_Reserved6` | TField |  |  |
| 12 | `PW.INFQ.RESERVED.5` | `PwInflowSequenceQueue_Reserved5` | TField |  |  |
| 13 | `PW.INFQ.RESERVED.4` | `PwInflowSequenceQueue_Reserved4` | TField |  |  |
| 14 | `PW.INFQ.RESERVED.3` | `PwInflowSequenceQueue_Reserved3` | TField |  |  |
| 15 | `PW.INFQ.RESERVED.2` | `PwInflowSequenceQueue_Reserved2` | TField |  |  |
| 16 | `PW.INFQ.RESERVED.1` | `PwInflowSequenceQueue_Reserved1` | TField |  |  |
