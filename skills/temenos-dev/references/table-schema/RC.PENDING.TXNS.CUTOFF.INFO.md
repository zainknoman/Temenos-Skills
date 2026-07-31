# RC.PENDING.TXNS.CUTOFF.INFO — Table Schema

> Source: `INSERTS/I_F.RC.PENDING.TXNS.CUTOFF.INFO` in `RC_TransactionCycler.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.PTCI.ACCOUNT.NO` | `RcPendingTxnsCutoffInfo_AccountNo` | TField |  | Account Number for which the RC.DETAIL record is created to retry the pending transactions |
| 2 | `RC.PTCI.CUTOFF.DATE.TIME` | `RcPendingTxnsCutoffInfo_CutoffDateTime` |  |  |  |
| 3 | `RC.PTCI.RC.DETAIL.ID` | `RcPendingTxnsCutoffInfo_RcDetailId` |  |  |  |
