# RC.PENDING.TXNS — Table Schema

> Source: `INSERTS/I_F.RC.PENDING.TXNS` in `RC_TransactionCycler.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.PEN.RC.DETAIL.ID` | `RcPendingTxns_RcDetailId` |  |  |  |
| 2 | `RC.PEN.RESERVED.01` | `RcPendingTxns_Reserved01` |  |  |  |
| 3 | `RC.PEN.RESERVED.02` | `RcPendingTxns_Reserved02` |  |  |  |
| 4 | `RC.PEN.RESERVED.03` | `RcPendingTxns_Reserved03` |  |  |  |
| 5 | `RC.PEN.RESERVED.04` | `RcPendingTxns_Reserved04` |  |  |  |
| 6 | `RC.PEN.RESERVED.05` | `RcPendingTxns_Reserved05` |  |  |  |
| 7 | `RC.PEN.LOCAL.REF` | `RcPendingTxns_LocalRef` |  |  |  |
| 8 | `RC.PEN.LINK.ID` | `RcPendingTxns_LinkId` | TField |  | Identifier to denote the Settlement Account is part of Multi PAYIN Settlement Group. Holds the record Id of the RC.MULTI.ACCT.LINK, which holds the list of Accounts that are linked to this Group. |
| 9 | `RC.PEN.RESERVED.07` | `RcPendingTxns_Reserved07` |  |  |  |
| 10 | `RC.PEN.RESERVED.08` | `RcPendingTxns_Reserved08` | TField |  |  |
| 11 | `RC.PEN.RESERVED.09` | `RcPendingTxns_Reserved09` | TField |  |  |
| 12 | `RC.PEN.RESERVED.10` | `RcPendingTxns_Reserved10` | TField |  |  |
