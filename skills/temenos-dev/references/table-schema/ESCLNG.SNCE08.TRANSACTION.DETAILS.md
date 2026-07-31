# ESCLNG.SNCE08.TRANSACTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.ESCLNG.SNCE08.TRANSACTION.DETAILS` in `ESCLNG_MiscellaneousPayments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCLNG.AMOUNT` | `EsclngSnce08TransactionDetails_Amount` | TField |  |  |
| 2 | `ESCLNG.DIRECTION` | `EsclngSnce08TransactionDetails_Direction` | TField |  | Direction of the transaction (OUTWARD/INWARD) |
| 3 | `ESCLNG.TRANSACTION.NATURE` | `EsclngSnce08TransactionDetails_TransactionNature` | TField |  | Nature of the transaction (Payment/Collection) |
| 4 | `ESCLNG.STATUS` | `EsclngSnce08TransactionDetails_Status` | TField |  | Status of the Transaction |
| 5 | `ESCLNG.LOCAL.REF` | `EsclngSnce08TransactionDetails_LocalRef` |  |  |  |
