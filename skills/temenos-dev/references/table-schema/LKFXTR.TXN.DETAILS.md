# LKFXTR.TXN.DETAILS — Table Schema

> Source: `INSERTS/I_F.LKFXTR.TXN.DETAILS` in `LKFXTR_ForexTransactionReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKFXTR.TXN.DET.TRANS.DIRECTION` | `LkfxtrTxnDetails_TransDirection` |  |  |  |
| 2 | `LKFXTR.TXN.DET.SYSTEM.ID` | `LkfxtrTxnDetails_SystemId` |  |  |  |
| 3 | `LKFXTR.TXN.DET.TRANSACTION.DATE` | `LkfxtrTxnDetails_TransactionDate` |  |  |  |
| 4 | `LKFXTR.TXN.DET.BRANCH.ID` | `LkfxtrTxnDetails_BranchId` |  |  |  |
| 5 | `LKFXTR.TXN.DET.TRANS.STATUS` | `LkfxtrTxnDetails_TransStatus` |  |  |  |
| 6 | `LKFXTR.TXN.DET.AMOUNT` | `LkfxtrTxnDetails_Amount` |  |  |  |
| 7 | `LKFXTR.TXN.DET.CURRENCY` | `LkfxtrTxnDetails_Currency` |  |  |  |
| 8 | `LKFXTR.TXN.DET.EXCHANGE.RATE` | `LkfxtrTxnDetails_ExchangeRate` |  |  |  |
| 9 | `LKFXTR.TXN.DET.CUSTOMER` | `LkfxtrTxnDetails_Customer` |  |  |  |
| 10 | `LKFXTR.TXN.DET.BENEFICIARY.REMITTER` | `LkfxtrTxnDetails_BeneficiaryRemitter` |  |  |  |
| 11 | `LKFXTR.TXN.DET.SERIAL.NUMBER` | `LkfxtrTxnDetails_SerialNumber` |  |  |  |
| 12 | `LKFXTR.TXN.DET.NARRATIVE` | `LkfxtrTxnDetails_Narrative` |  |  |  |
| 13 | `LKFXTR.TXN.DET.TRANS.EXTRACTED` | `LkfxtrTxnDetails_TransExtracted` | TField |  |  |
