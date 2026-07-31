# HKICL.PROCESSED.PAYMENTS — Table Schema

> Source: `INSERTS/I_F.HKICL.PROCESSED.PAYMENTS` in `HKDDPR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HKICL.PROCESS.PAY.TRANSACTION.TYPE` | `HkiclProcessedPayments_TransactionType` | TField |  | Identifies the Transaction Type applicable to the transaction being processed. |
| 2 | `HKICL.PROCESS.PAY.DEBIT.ACCT.NO` | `HkiclProcessedPayments_DebitAcctNo` | TField |  | Identifies the Account being debited in respect of the transfer transaction. |
| 3 | `HKICL.PROCESS.PAY.DEBIT.CURRENCY` | `HkiclProcessedPayments_DebitCurrency` | TField |  | Defines the Currency of the Account being debited. |
| 4 | `HKICL.PROCESS.PAY.DEBIT.AMOUNT` | `HkiclProcessedPayments_DebitAmount` | TField |  | Defines the Transfer amount. |
| 5 | `HKICL.PROCESS.PAY.DEBIT.VALUE.DATE` | `HkiclProcessedPayments_DebitValueDate` | TField |  | Identifies the Date when the Debit entry is to be given value for interest purposes. |
| 6 | `HKICL.PROCESS.PAY.CREDIT.ACCT.NO` | `HkiclProcessedPayments_CreditAcctNo` | TField |  | Identifies the Account being credited in respect of the transfer transaction. |
| 7 | `HKICL.PROCESS.PAY.CREDIT.CURRENCY` | `HkiclProcessedPayments_CreditCurrency` | TField |  | Defines the Currency of the Account being credited. |
| 8 | `HKICL.PROCESS.PAY.CREDIT.AMOUNT` | `HkiclProcessedPayments_CreditAmount` | TField |  | Defines the Transfer amount. (This field will usually be used for Outward Transfers, while the Debit Amount field will usually be used for the Inward Transfers.) |
| 9 | `HKICL.PROCESS.PAY.CREDIT.VALUE.DATE` | `HkiclProcessedPayments_CreditValueDate` | TField |  | Identifies the date when the Credit entry is to be given value for interest purposes. |
| 10 | `HKICL.PROCESS.PAY.PROCESSING.DATE` | `HkiclProcessedPayments_ProcessingDate` | TField |  | Specifies on which future working day this transaction is to be processed. |
| 11 | `HKICL.PROCESS.PAY.MANDATE.REFERENCE` | `HkiclProcessedPayments_MandateReference` | TField |  |  |
| 12 | `HKICL.PROCESS.PAY.RESERVED.1` | `HkiclProcessedPayments_Reserved1` | TField |  |  |
| 13 | `HKICL.PROCESS.PAY.RESERVED.2` | `HkiclProcessedPayments_Reserved2` | TField |  |  |
| 14 | `HKICL.PROCESS.PAY.RESERVED.3` | `HkiclProcessedPayments_Reserved3` | TField |  |  |
| 15 | `HKICL.PROCESS.PAY.RESERVED.4` | `HkiclProcessedPayments_Reserved4` | TField |  |  |
| 16 | `HKICL.PROCESS.PAY.RESERVED.5` | `HkiclProcessedPayments_Reserved5` | TField |  |  |
| 17 | `HKICL.PROCESS.PAY.RESERVED.6` | `HkiclProcessedPayments_Reserved6` | TField |  |  |
| 18 | `HKICL.PROCESS.PAY.RESERVED.7` | `HkiclProcessedPayments_Reserved7` | TField |  |  |
| 19 | `HKICL.PROCESS.PAY.RESERVED.8` | `HkiclProcessedPayments_Reserved8` | TField |  |  |
| 20 | `HKICL.PROCESS.PAY.RESERVED.9` | `HkiclProcessedPayments_Reserved9` | TField |  |  |
| 21 | `HKICL.PROCESS.PAY.RESERVED.10` | `HkiclProcessedPayments_Reserved10` | TField |  |  |
| 22 | `HKICL.PROCESS.PAY.LOCAL.REF` | `HkiclProcessedPayments_LocalRef` |  |  |  |
