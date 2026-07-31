# INTERAC.ENTRY.DETAILS — Table Schema

> Source: `INSERTS/I_F.INTERAC.ENTRY.DETAILS` in `CAINTR_InteracInstant.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INT.ENT.DET.DR.CR.MARKER` | `InteracEntryDetails_DrCrMarker` | TField |  |  |
| 2 | `INT.ENT.DET.DEBIT.CUSTOMER` | `InteracEntryDetails_DebitCustomer` | TField |  |  |
| 3 | `INT.ENT.DET.DEBIT.ACCOUNT` | `InteracEntryDetails_DebitAccount` | TField |  |  |
| 4 | `INT.ENT.DET.CREDIT.CUSTOMER` | `InteracEntryDetails_CreditCustomer` | TField |  |  |
| 5 | `INT.ENT.DET.CREDIT.ACCOUNT` | `InteracEntryDetails_CreditAccount` | TField |  |  |
| 6 | `INT.ENT.DET.AMOUNT` | `InteracEntryDetails_Amount` | TField |  |  |
| 7 | `INT.ENT.DET.DATE` | `InteracEntryDetails_Date` | TField |  |  |
| 8 | `INT.ENT.DET.REVERSAL.MARKER` | `InteracEntryDetails_ReversalMarker` | TField |  |  |
| 9 | `INT.ENT.DET.TRACE.NO` | `InteracEntryDetails_TraceNo` | TField |  |  |
| 10 | `INT.ENT.DET.TRANSACTION.CODE` | `InteracEntryDetails_TransactionCode` | TField |  |  |
| 11 | `INT.ENT.DET.TRANSACTION.TYPE` | `InteracEntryDetails_TransactionType` | TField |  |  |
| 12 | `INT.ENT.DET.RESERVED.9` | `InteracEntryDetails_Reserved9` | TField |  |  |
| 13 | `INT.ENT.DET.RESERVED.8` | `InteracEntryDetails_Reserved8` | TField |  |  |
| 14 | `INT.ENT.DET.RESERVED.7` | `InteracEntryDetails_Reserved7` | TField |  |  |
| 15 | `INT.ENT.DET.RESERVED.6` | `InteracEntryDetails_Reserved6` | TField |  |  |
| 16 | `INT.ENT.DET.RESERVED.5` | `InteracEntryDetails_Reserved5` | TField |  |  |
| 17 | `INT.ENT.DET.RESERVED.4` | `InteracEntryDetails_Reserved4` | TField |  |  |
| 18 | `INT.ENT.DET.RESERVED.3` | `InteracEntryDetails_Reserved3` | TField |  |  |
| 19 | `INT.ENT.DET.RESERVED.2` | `InteracEntryDetails_Reserved2` | TField |  |  |
| 20 | `INT.ENT.DET.RESERVED.1` | `InteracEntryDetails_Reserved1` | TField |  |  |
