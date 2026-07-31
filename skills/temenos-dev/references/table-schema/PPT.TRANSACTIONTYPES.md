# PPT.TRANSACTIONTYPES — Table Schema

> Source: `INSERTS/I_F.PPT.TRANSACTIONTYPES` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTRN.TransactionType` | `PptTransactiontypes_Transactiontype` |  |  |  |
| 2 | `PPTRN.TransactionTypeDescription` | `PptTransactiontypes_Transactiontypedescription` |  |  |  |
| 3 | `PPTRN.RACTransactionType` | `PptTransactiontypes_Ractransactiontype` |  |  |  |
| 4 | `PPTRN.RSCTransactionType` | `PptTransactiontypes_Rsctransactiontype` |  |  |  |
| 5 | `PPTRN.EntryUserID` | `PptTransactiontypes_Entryuserid` |  |  |  |
| 6 | `PPTRN.EntryDateTime` | `PptTransactiontypes_Entrydatetime` |  |  |  |
| 7 | `PPTRN.ApproverUserID` | `PptTransactiontypes_Approveruserid` |  |  |  |
| 8 | `PPTRN.ApprovedDateTime` | `PptTransactiontypes_Approveddatetime` |  |  |  |
