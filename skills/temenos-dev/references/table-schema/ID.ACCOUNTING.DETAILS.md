# ID.ACCOUNTING.DETAILS — Table Schema

> Source: `INSERTS/I_F.ID.ACCOUNTING.DETAILS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.AD.PDS.ACTION.REF` | `IdAccountingDetails_PdsActionRef` | TField |  | This field should contain a valid PDS action reference Number. Validation Rules: 1. This field will hold the valid PDS Action Reference. 2. This is an ID Component. |
| 2 | `ID.AD.ENTRY.TYPE` | `IdAccountingDetails_EntryType` |  |  |  |
| 3 | `ID.AD.DEBIT.ACCOUNT` | `IdAccountingDetails_DebitAccount` |  |  |  |
| 4 | `ID.AD.CREDIT.ACCOUNT` | `IdAccountingDetails_CreditAccount` |  |  |  |
| 5 | `ID.AD.CR.TXN.CODE` | `IdAccountingDetails_CrTxnCode` |  |  |  |
| 6 | `ID.AD.DB.TXN.CODE` | `IdAccountingDetails_DbTxnCode` |  |  |  |
| 7 | `ID.AD.AMOUNT` | `IdAccountingDetails_Amount` |  |  |  |
| 8 | `ID.AD.STMT.REF` | `IdAccountingDetails_StmtRef` |  |  |  |
| 9 | `ID.AD.REV.STMT.REF` | `IdAccountingDetails_RevStmtRef` |  |  |  |
| 10 | `ID.AD.RESERVED.5` | `IdAccountingDetails_Reserved5` | TField |  |  |
| 11 | `ID.AD.RESERVED.4` | `IdAccountingDetails_Reserved4` | TField |  |  |
| 12 | `ID.AD.RESERVED.3` | `IdAccountingDetails_Reserved3` | TField |  |  |
| 13 | `ID.AD.RESERVED.2` | `IdAccountingDetails_Reserved2` | TField |  |  |
| 14 | `ID.AD.RESERVED.1` | `IdAccountingDetails_Reserved1` | TField |  |  |
