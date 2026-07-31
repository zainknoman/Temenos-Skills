# ALE.JOURNAL.CONCAT — Table Schema

> Source: `INSERTS/I_F.ALE.JOURNAL.CONCAT` in `AC_AccountOpening.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AJC.SUM.AMOUNT` | `AleJournalConcat_SumAmount` | TField |  | This field stores the total amount reserved under that particular reservation key. |
| 2 | `AJC.TXN.DET` | `AleJournalConcat_TxnDet` |  |  |  |
