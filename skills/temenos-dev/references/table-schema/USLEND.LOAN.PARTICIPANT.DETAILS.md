# USLEND.LOAN.PARTICIPANT.DETAILS — Table Schema

> Source: `INSERTS/I_F.USLEND.LOAN.PARTICIPANT.DETAILS` in `USLEND_LoanParticipation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USLEND.LPD.PARTICIPANT.ID` | `UslendLoanParticipantDetails_ParticipantId` |  |  |  |
| 2 | `USLEND.LPD.PARTICIPANT.PERCENTAGE` | `UslendLoanParticipantDetails_ParticipantPercentage` |  |  |  |
| 3 | `USLEND.LPD.PARTICIPANT.PAYOUT.ACCT` | `UslendLoanParticipantDetails_ParticipantPayoutAcct` |  |  |  |
| 4 | `USLEND.LPD.RESERVED9` | `UslendLoanParticipantDetails_Reserved9` | TField |  |  |
| 5 | `USLEND.LPD.RESERVED8` | `UslendLoanParticipantDetails_Reserved8` | TField |  |  |
| 6 | `USLEND.LPD.RESERVED7` | `UslendLoanParticipantDetails_Reserved7` | TField |  |  |
| 7 | `USLEND.LPD.RESERVED6` | `UslendLoanParticipantDetails_Reserved6` | TField |  |  |
| 8 | `USLEND.LPD.RESERVED5` | `UslendLoanParticipantDetails_Reserved5` | TField |  |  |
| 9 | `USLEND.LPD.RESERVED4` | `UslendLoanParticipantDetails_Reserved4` | TField |  |  |
| 10 | `USLEND.LPD.RESERVED3` | `UslendLoanParticipantDetails_Reserved3` | TField |  |  |
| 11 | `USLEND.LPD.RESERVED2` | `UslendLoanParticipantDetails_Reserved2` | TField |  |  |
| 12 | `USLEND.LPD.RESERVED1` | `UslendLoanParticipantDetails_Reserved1` | TField |  |  |
