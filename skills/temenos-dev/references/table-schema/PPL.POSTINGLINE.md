# PPL.POSTINGLINE — Table Schema

> Source: `INSERTS/I_F.PPL.POSTINGLINE` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPLI.PostingLineId` | `PplPostingline_Postinglineid` |  |  |  |
| 2 | `PPLI.PostingSetId` | `PplPostingline_Postingsetid` |  |  |  |
| 3 | `PPLI.SequenceNumber` | `PplPostingline_Sequencenumber` |  |  |  |
| 4 | `PPLI.PartyFlag` | `PplPostingline_Partyflag` |  |  |  |
| 5 | `PPLI.AccountToken` | `PplPostingline_Accounttoken` |  |  |  |
| 6 | `PPLI.AmountToken` | `PplPostingline_Amounttoken` |  |  |  |
| 7 | `PPLI.BookingDate` | `PplPostingline_Bookingdate` |  |  |  |
| 8 | `PPLI.ValueDateToken` | `PplPostingline_Valuedatetoken` |  |  |  |
| 9 | `PPLI.BookingCode` | `PplPostingline_Bookingcode` |  |  |  |
| 10 | `PPLI.SuppressZeroFlag` | `PplPostingline_Suppresszeroflag` |  |  |  |
| 11 | `PPLI.StatementFormat` | `PplPostingline_Statementformat` |  |  |  |
