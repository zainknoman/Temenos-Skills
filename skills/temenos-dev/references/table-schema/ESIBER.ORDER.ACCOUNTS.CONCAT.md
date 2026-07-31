# ESIBER.ORDER.ACCOUNTS.CONCAT — Table Schema

> Source: `INSERTS/I_F.ESIBER.ORDER.ACCOUNTS.CONCAT` in `ESIBER_OrderAccounts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESIBER.CONTIGENT.EXECUTION.DATE` | `EsiberOrderAccountsConcat_ExecutionDate` | TField |  |  |
| 2 | `ESIBER.CONTIGENT.RETURN.REJECT.DATE` | `EsiberOrderAccountsConcat_ReturnRejectDate` | TField |  | This field reserved for future use |
| 3 | `ESIBER.CONTIGENT.STATUS` | `EsiberOrderAccountsConcat_Status` | TField |  | This field reserved for future use |
| 4 | `ESIBER.CONTIGENT.STAGE` | `EsiberOrderAccountsConcat_Stage` | TField |  | This field reserved for future use |
| 5 | `ESIBER.CONTIGENT.ORDER.ACCOUNT` | `EsiberOrderAccountsConcat_OrderAccount` | TField |  | This field reserved for future use |
| 6 | `ESIBER.CONTIGENT.MEMO.ACCOUNT` | `EsiberOrderAccountsConcat_MemoAccount` | TField |  | This field reserved for future use |
| 7 | `ESIBER.CONTIGENT.TRANSACTION.AMOUNT` | `EsiberOrderAccountsConcat_TransactionAmount` | TField |  | This field reserved for future use |
| 8 | `ESIBER.CONTIGENT.SETTLEMENT.DATE` | `EsiberOrderAccountsConcat_SettlementDate` | TField |  | This field is to store Settlement Date |
