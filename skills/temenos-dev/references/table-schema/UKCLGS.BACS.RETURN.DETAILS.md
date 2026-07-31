# UKCLGS.BACS.RETURN.DETAILS — Table Schema

> Source: `INSERTS/I_F.UKCLGS.BACS.RETURN.DETAILS` in `UKCLGS_BacsDirectCredits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BACS.RETURN.TXN.REFERENCE.ID` | `UkclgsBacsReturnDetails_TxnReferenceId` |  |  |  |
| 2 | `BACS.RETURN.ORIGINAL.TXN.DATE` | `UkclgsBacsReturnDetails_OriginalTxnDate` |  |  |  |
| 3 | `BACS.RETURN.STATUS` | `UkclgsBacsReturnDetails_Status` |  |  |  |
| 4 | `BACS.RETURN.ORIGINATOR.ACCOUNT.NUMBER` | `UkclgsBacsReturnDetails_OriginatorAccountNumber` |  |  |  |
| 5 | `BACS.RETURN.TRANSACTION.AMOUNT` | `UkclgsBacsReturnDetails_TransactionAmount` |  |  |  |
| 6 | `BACS.RETURN.LOCAL.REF` | `UkclgsBacsReturnDetails_LocalRef` |  |  |  |
| 7 | `BACS.RETURN.RESERVED.1` | `UkclgsBacsReturnDetails_Reserved1` | TField |  |  |
| 8 | `BACS.RETURN.RESERVED.2` | `UkclgsBacsReturnDetails_Reserved2` | TField |  |  |
| 9 | `BACS.RETURN.RESERVED.3` | `UkclgsBacsReturnDetails_Reserved3` | TField |  |  |
| 10 | `BACS.RETURN.RESERVED.4` | `UkclgsBacsReturnDetails_Reserved4` | TField |  |  |
| 11 | `BACS.RETURN.RESERVED.5` | `UkclgsBacsReturnDetails_Reserved5` | TField |  |  |
| 12 | `BACS.RETURN.RESERVED.6` | `UkclgsBacsReturnDetails_Reserved6` | TField |  |  |
| 13 | `BACS.RETURN.RESERVED.7` | `UkclgsBacsReturnDetails_Reserved7` | TField |  |  |
| 14 | `BACS.RETURN.RESERVED.8` | `UkclgsBacsReturnDetails_Reserved8` | TField |  |  |
| 15 | `BACS.RETURN.RESERVED.9` | `UkclgsBacsReturnDetails_Reserved9` | TField |  |  |
| 16 | `BACS.RETURN.RESERVED.10` | `UkclgsBacsReturnDetails_Reserved10` | TField |  |  |
| 17 | `BACS.RETURN.RESERVED.11` | `UkclgsBacsReturnDetails_Reserved11` | TField |  |  |
| 18 | `BACS.RETURN.RESERVED.12` | `UkclgsBacsReturnDetails_Reserved12` | TField |  |  |
| 19 | `BACS.RETURN.RESERVED.13` | `UkclgsBacsReturnDetails_Reserved13` | TField |  |  |
| 20 | `BACS.RETURN.RESERVED.14` | `UkclgsBacsReturnDetails_Reserved14` | TField |  |  |
| 21 | `BACS.RETURN.RESERVED.15` | `UkclgsBacsReturnDetails_Reserved15` | TField |  |  |
| 22 | `BACS.RETURN.CREDITOR.ID` | `UkclgsBacsReturnDetails_CreditorId` |  |  |  |
| 23 | `BACS.RETURN.CLEARING.TRANSACTION.TYPE` | `UkclgsBacsReturnDetails_ClearingTransactionType` |  |  |  |
