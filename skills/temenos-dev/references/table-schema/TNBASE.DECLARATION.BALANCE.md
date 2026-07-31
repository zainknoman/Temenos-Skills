# TNBASE.DECLARATION.BALANCE — Table Schema

> Source: `INSERTS/I_F.TNBASE.DECLARATION.BALANCE` in `TNBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNBASE.DEC.BAL.UNDECLARED.TXN.ID` | `TnbaseDeclarationBalance_UndeclaredTxnId` |  |  |  |
| 2 | `TNBASE.DEC.BAL.CUMULATIVE.TXN.AMOUNT` | `TnbaseDeclarationBalance_CumulativeTxnAmount` | TField |  | Total Amount exchanged by the customer |
| 3 | `TNBASE.DEC.BAL.DECLARATION.ID.CCY` | `TnbaseDeclarationBalance_DeclarationIdCcy` |  |  |  |
| 4 | `TNBASE.DEC.BAL.DECLARATION.EXPIRY` | `TnbaseDeclarationBalance_DeclarationExpiry` |  |  |  |
| 5 | `TNBASE.DEC.BAL.DECLARED.AMOUNT.LCY` | `TnbaseDeclarationBalance_DeclaredAmountLcy` |  |  |  |
| 6 | `TNBASE.DEC.BAL.UTILIZED.AMOUNT.LCY` | `TnbaseDeclarationBalance_UtilizedAmountLcy` |  |  |  |
| 7 | `TNBASE.DEC.BAL.TRANSACTION.ID` | `TnbaseDeclarationBalance_TransactionId` |  |  |  |
| 8 | `TNBASE.DEC.BAL.RESERVED.10` | `TnbaseDeclarationBalance_Reserved10` | TField |  | Field for future use |
| 9 | `TNBASE.DEC.BAL.RESERVED.9` | `TnbaseDeclarationBalance_Reserved9` | TField |  | Field for future use |
| 10 | `TNBASE.DEC.BAL.RESERVED.8` | `TnbaseDeclarationBalance_Reserved8` | TField |  | Field for future use |
| 11 | `TNBASE.DEC.BAL.RESERVED.7` | `TnbaseDeclarationBalance_Reserved7` | TField |  | Field for future use |
| 12 | `TNBASE.DEC.BAL.RESERVED.6` | `TnbaseDeclarationBalance_Reserved6` | TField |  | Field for future use |
| 13 | `TNBASE.DEC.BAL.RESERVED.5` | `TnbaseDeclarationBalance_Reserved5` | TField |  | Field for future use |
| 14 | `TNBASE.DEC.BAL.RESERVED.4` | `TnbaseDeclarationBalance_Reserved4` | TField |  | Field for future use |
| 15 | `TNBASE.DEC.BAL.RESERVED.3` | `TnbaseDeclarationBalance_Reserved3` | TField |  | Field for future use |
| 16 | `TNBASE.DEC.BAL.RESERVED.2` | `TnbaseDeclarationBalance_Reserved2` | TField |  | Field for future use |
| 17 | `TNBASE.DEC.BAL.RESERVED.1` | `TnbaseDeclarationBalance_Reserved1` | TField |  | Field for future use |
