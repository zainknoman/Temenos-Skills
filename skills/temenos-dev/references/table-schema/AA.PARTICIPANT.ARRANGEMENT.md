# AA.PARTICIPANT.ARRANGEMENT — Table Schema

> Source: `INSERTS/I_F.AA.PARTICIPANT.ARRANGEMENT` in `AA_Participant.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PART.ARR.ARRANGEMENT.ID` | `AaParticipantArrangement_ArrangementId` |  |  |  |
| 2 | `AA.PART.ARR.RESERVED.01` | `AaParticipantArrangement_Reserved01` |  |  |  |
| 3 | `AA.PART.ARR.RESERVED.02` | `AaParticipantArrangement_Reserved02` |  |  |  |
| 4 | `AA.PART.ARR.ACCOUNT.ID` | `AaParticipantArrangement_AccountId` |  |  |  |
| 5 | `AA.PART.ARR.RESERVED.03` | `AaParticipantArrangement_Reserved03` |  |  |  |
| 6 | `AA.PART.ARR.RESERVED.04` | `AaParticipantArrangement_Reserved04` |  |  |  |
| 7 | `AA.PART.ARR.RESERVED.05` | `AaParticipantArrangement_Reserved05` |  |  |  |
| 8 | `AA.PART.ARR.RESERVED.06` | `AaParticipantArrangement_Reserved06` |  |  |  |
| 9 | `AA.PART.ARR.RESERVED.07` | `AaParticipantArrangement_Reserved07` |  |  |  |
