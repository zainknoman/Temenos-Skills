# ILMATX.TXN.MAPPING — Table Schema

> Source: `INSERTS/I_F.ILMATX.TXN.MAPPING` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MATX.MATRIX.TXN.REF` | `IlmatxTxnMapping_MatrixTxnRef` | TField |  | The Corresponding Matrix transaction reference number of the T24 transaction. |
| 2 | `MATX.CANCELLED.TXN.REF` | `IlmatxTxnMapping_CancelledTxnRef` | TField |  | The Corresponding Matrix transaction reference number of the reversal of T24 transaction. |
| 3 | `MATX.RESERVED.5` | `IlmatxTxnMapping_Reserved5` | TField |  | Reserved for future use. |
| 4 | `MATX.RESERVED.4` | `IlmatxTxnMapping_Reserved4` | TField |  | Reserved for future use. |
| 5 | `MATX.RESERVED.3` | `IlmatxTxnMapping_Reserved3` | TField |  | Reserved for future use. |
| 6 | `MATX.RESERVED.2` | `IlmatxTxnMapping_Reserved2` | TField |  | Reserved for future use. |
| 7 | `MATX.RESERVED.1` | `IlmatxTxnMapping_Reserved1` | TField |  | Reserved for future use. |
