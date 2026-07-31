# ID.WAKALA.ENTRY.DETAILS — Table Schema

> Source: `INSERTS/I_F.ID.WAKALA.ENTRY.DETAILS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.WAK.DEBIT.ACCOUNT` | `IdWakalaEntryDetails_DebitAccount` |  |  |  |
| 2 | `ID.WAK.CREDIT.ACCOUNT` | `IdWakalaEntryDetails_CreditAccount` |  |  |  |
| 3 | `ID.WAK.AMOUNT` | `IdWakalaEntryDetails_Amount` |  |  |  |
| 4 | `ID.WAK.STMT.NOS` | `IdWakalaEntryDetails_StmtNos` | TField |  |  |
| 5 | `ID.WAK.REV.STMT.REF` | `IdWakalaEntryDetails_RevStmtRef` | TField |  |  |
