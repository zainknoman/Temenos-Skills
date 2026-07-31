# USLEND.PARTICIPANT.PAYOUT.DETAILS — Table Schema

> Source: `INSERTS/I_F.USLEND.PARTICIPANT.PAYOUT.DETAILS` in `USLEND_LoanParticipation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USLEND.PPD.LOAN.ARRANGEMENT.ID` | `UslendParticipantPayoutDetails_LoanArrangementId` | TField |  | Arrangement ID of the loan is captured in this field. |
| 2 | `USLEND.PPD.LOAN.REPAYMENT.DATE` | `UslendParticipantPayoutDetails_LoanRepaymentDate` | TField |  | It denotes the Value date of the Loan Repayment. |
| 3 | `USLEND.PPD.REPAY.PROCESSING.DATE` | `UslendParticipantPayoutDetails_RepayProcessingDate` | TField |  | This field captures the booking date of the Loan Repayment. |
| 4 | `USLEND.PPD.RESERVED9` | `UslendParticipantPayoutDetails_Reserved9` | TField |  |  |
| 5 | `USLEND.PPD.RESERVED8` | `UslendParticipantPayoutDetails_Reserved8` | TField |  |  |
| 6 | `USLEND.PPD.RESERVED7` | `UslendParticipantPayoutDetails_Reserved7` | TField |  |  |
| 7 | `USLEND.PPD.INVESTOR.DEPOSIT.ID` | `UslendParticipantPayoutDetails_InvestorDepositId` |  |  |  |
| 8 | `USLEND.PPD.PRINCIPAL.PAYOUT.AMT` | `UslendParticipantPayoutDetails_PrincipalPayoutAmt` |  |  |  |
| 9 | `USLEND.PPD.PRINCIPAL.PAYOUT.REF` | `UslendParticipantPayoutDetails_PrincipalPayoutRef` |  |  |  |
| 10 | `USLEND.PPD.INTEREST.PAYOUT.AMT` | `UslendParticipantPayoutDetails_InterestPayoutAmt` |  |  |  |
| 11 | `USLEND.PPD.INTEREST.PAYOUT.REF` | `UslendParticipantPayoutDetails_InterestPayoutRef` |  |  |  |
| 12 | `USLEND.PPD.RESERVED6` | `UslendParticipantPayoutDetails_Reserved6` | TField |  |  |
| 13 | `USLEND.PPD.RESERVED5` | `UslendParticipantPayoutDetails_Reserved5` | TField |  |  |
| 14 | `USLEND.PPD.RESERVED4` | `UslendParticipantPayoutDetails_Reserved4` | TField |  |  |
| 15 | `USLEND.PPD.RESERVED3` | `UslendParticipantPayoutDetails_Reserved3` | TField |  |  |
| 16 | `USLEND.PPD.RESERVED2` | `UslendParticipantPayoutDetails_Reserved2` | TField |  |  |
| 17 | `USLEND.PPD.RESERVED1` | `UslendParticipantPayoutDetails_Reserved1` | TField |  |  |
