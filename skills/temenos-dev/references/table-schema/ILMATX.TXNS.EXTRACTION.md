# ILMATX.TXNS.EXTRACTION — Table Schema

> Source: `INSERTS/I_F.ILMATX.TXNS.EXTRACTION` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MATX.TRADE.TXNS` | `IlmatxTxnsExtraction_TradeTxns` |  |  |  |
| 2 | `MATX.TRANSFER.TXNS` | `IlmatxTxnsExtraction_TransferTxns` |  |  |  |
| 3 | `MATX.POS.TRANSFER.TXNS` | `IlmatxTxnsExtraction_PosTransferTxns` |  |  |  |
| 4 | `MATX.ENTITLEMENT.TXNS` | `IlmatxTxnsExtraction_EntitlementTxns` |  |  |  |
| 5 | `MATX.SAFEKEEP.FEES.TXNS` | `IlmatxTxnsExtraction_SafekeepFeesTxns` |  |  |  |
| 6 | `MATX.DX.TRADE.TXNS` | `IlmatxTxnsExtraction_DxTradeTxns` |  |  |  |
| 7 | `MATX.DX.CLOSEOUT.TXNS` | `IlmatxTxnsExtraction_DxCloseoutTxns` |  |  |  |
| 8 | `MATX.SBL.TXNS` | `IlmatxTxnsExtraction_SblTxns` |  |  |  |
| 9 | `MATX.RESERVED.5` | `IlmatxTxnsExtraction_Reserved5` | TField |  | Reserved for future use. |
| 10 | `MATX.RESERVED.4` | `IlmatxTxnsExtraction_Reserved4` | TField |  | Reserved for future use. |
| 11 | `MATX.RESERVED.3` | `IlmatxTxnsExtraction_Reserved3` | TField |  | Reserved for future use. |
| 12 | `MATX.RESERVED.2` | `IlmatxTxnsExtraction_Reserved2` | TField |  | Reserved for future use. |
| 13 | `MATX.RESERVED.1` | `IlmatxTxnsExtraction_Reserved1` | TField |  | Reserved for future use. |
| 14 | `MATRIX.TXN.TYPE` | `IlmatxTxnsExtraction_MatxTxnType` |  |  |  |
