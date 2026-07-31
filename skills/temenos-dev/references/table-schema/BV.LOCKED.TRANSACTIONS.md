# BV.LOCKED.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.BV.LOCKED.TRANSACTIONS` in `AM_BackvalueTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BV.LTX.SEC.OR.ACCT.NO` | `BvLockedTransactions_SecOrAcctNo` |  |  |  |
| 2 | `BV.LTX.DEPOSITORY` | `BvLockedTransactions_Depository` |  |  |  |
| 3 | `BV.LTX.EFF.DATE` | `BvLockedTransactions_EffDate` |  |  |  |
| 4 | `BV.LTX.LOCK.DATE` | `BvLockedTransactions_LockDate` |  |  |  |
| 5 | `BV.LTX.TRANSACTION.DATE` | `BvLockedTransactions_TransactionDate` |  |  |  |
| 6 | `BV.LTX.TXN.KEY` | `BvLockedTransactions_TxnKey` |  |  |  |
