# SC.PORT.LIST.TXN — Table Schema

> Source: `INSERTS/I_F.SC.PORT.LIST.TXN` in `SC_ScfAdvisoryFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PT.CUSTOMER` | `ScPortListTxn_Customer` | TField |  | Holds the Customer Reference Validation Rule Noinput field |
| 2 | `SC.PT.PORTFOLIO` | `ScPortListTxn_Portfolio` | TField |  | Holds the Portfolio ID Validation Rule Noinput field |
| 3 | `SC.PT.TXN.APP` | `ScPortListTxn_TxnApp` | TField |  | The application that the transaction relates to (i.e SEC TRADE, DX TRADE, etc.) Validation Rule Noinput field |
| 4 | `SC.PT.TRANS.REFERENCE` | `ScPortListTxn_TransReference` | TField |  | Transaction reference from the ID Validation Rule Noinput field |
| 5 | `SC.PT.INPUT.DATE` | `ScPortListTxn_InputDate` | TField |  | The date on which the transaction is input. Validation Rule Noinput field |
| 6 | `SC.PT.TXN.DATE` | `ScPortListTxn_TxnDate` | TField |  | The date (trade date) of the transaction. Validation Rule Noinput field |
| 7 | `SC.PT.REV.DATE` | `ScPortListTxn_RevDate` | TField |  | Reversal date, if any. The date on which transaction was reversed. Validation Rule Noinput field |
| 8 | `SC.PT.RESERVED.05` | `ScPortListTxn_Reserved05` |  |  |  |
| 9 | `SC.PT.RESERVED.04` | `ScPortListTxn_Reserved04` |  |  |  |
| 10 | `SC.PT.RESERVED.03` | `ScPortListTxn_Reserved03` |  |  |  |
| 11 | `SC.PT.RESERVED.02` | `ScPortListTxn_Reserved02` |  |  |  |
| 12 | `SC.PT.RESERVED.01` | `ScPortListTxn_Reserved01` |  |  |  |
