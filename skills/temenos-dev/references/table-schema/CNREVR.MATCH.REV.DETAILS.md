# CNREVR.MATCH.REV.DETAILS — Table Schema

> Source: `INSERTS/I_F.CNREVR.MATCH.REV.DETAILS` in `CNREVR_MatchingReversal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CNREVR.MR.MR.ACCOUNT` | `CnrevrMatchRevDetails_MrAccount` | TField |  | The internal account for which the Matching reversal transaction happened |
| 2 | `CNREVR.MR.ORIGINAL.TXN.DATE` | `CnrevrMatchRevDetails_OriginalTxnDate` | TField |  | Update of Original Transaction Date |
| 3 | `CNREVR.MR.ORIGINAL.TXN.REFERENCE` | `CnrevrMatchRevDetails_OriginalTxnReference` | TField |  |  |
| 4 | `CNREVR.MR.ORIGINAL.TXN.CURRENCY` | `CnrevrMatchRevDetails_OriginalTxnCurrency` | TField |  | Update of Original Transaction currency |
| 5 | `CNREVR.MR.ORIGINAL.TXN.AMOUNT` | `CnrevrMatchRevDetails_OriginalTxnAmount` | TField |  | Update of Original Transaction amount |
| 6 | `CNREVR.MR.REVERSAL.DATE` | `CnrevrMatchRevDetails_ReversalDate` |  |  |  |
| 7 | `CNREVR.MR.REVERSAL.REFERENCE` | `CnrevrMatchRevDetails_ReversalReference` |  |  |  |
| 8 | `CNREVR.MR.REVERSAL.AMOUNT.LCY` | `CnrevrMatchRevDetails_ReversalAmountLcy` |  |  |  |
| 9 | `CNREVR.MR.REVERSAL.AMOUNT.FCY` | `CnrevrMatchRevDetails_ReversalAmountFcy` |  |  |  |
| 10 | `CNREVR.MR.MID.RATE` | `CnrevrMatchRevDetails_MidRate` | TField |  | This Field denotes the mid rate in case of cross currency transaction |
| 11 | `CNREVR.MR.TRANSACTION.RECONCILED` | `CnrevrMatchRevDetails_TransactionReconciled` | TField |  | Will update on successful authorization of contra matching reversal |
