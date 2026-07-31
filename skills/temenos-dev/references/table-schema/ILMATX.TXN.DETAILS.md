# ILMATX.TXN.DETAILS — Table Schema

> Source: `INSERTS/I_F.ILMATX.TXN.DETAILS` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.TXN.STATUS` | `IlmatxTxnDetails_Status` |  |  |  |
| 2 | `ILMATX.TXN.TXN.ACTION` | `IlmatxTxnDetails_TxnAction` |  |  |  |
| 3 | `ILMATX.TXN.RESPONSE.TAX.AMT.CCY` | `IlmatxTxnDetails_ResponseTaxAmtCcy` |  |  |  |
| 4 | `ILMATX.TXN.RESPONSE.TAX.AMOUNT` | `IlmatxTxnDetails_ResponseTaxAmount` |  |  |  |
| 5 | `ILMATX.TXN.RESPONSE.TAX.AMT.STATUS` | `IlmatxTxnDetails_ResponseTaxAmtStatus` |  |  |  |
| 6 | `ILMATX.TXN.ACCOUNTING.ENTRY.REF` | `IlmatxTxnDetails_AccountingEntryRef` |  |  |  |
| 7 | `ILMATX.TXN.APPLICATION.NAME` | `IlmatxTxnDetails_ApplicationName` | TField |  | Specifies the Application name under which the transaction falls |
| 8 | `ILMATX.TXN.TRANSACTION.ID` | `IlmatxTxnDetails_TransactionId` | TField |  | Specifies the Transaction code of respective trade transaction. |
| 9 | `ILMATX.TXN.TOTAL.AMOUNT.RAISED` | `IlmatxTxnDetails_TotalAmountRaised` | TField |  | This field shows the Aggregate amount to be raised. |
| 10 | `ILMATX.TXN.RESERVED.2` | `IlmatxTxnDetails_Reserved2` | TField |  | Reserved for future use. |
| 11 | `ILMATX.TXN.RESERVED.1` | `IlmatxTxnDetails_Reserved1` | TField |  | Reserved for future use. |
| 12 | `ILMATX.TXN.LOCAL.REF` | `IlmatxTxnDetails_LocalRef` |  |  |  |
| 13 | `ILMATX.TXN.OVERRIDE` | `IlmatxTxnDetails_Override` |  |  |  |
| 14 | `ILMATX.TXN.RECORD.STATUS` | `IlmatxTxnDetails_RecordStatus` | String |  |  |
| 15 | `ILMATX.TXN.CURR.NO` | `IlmatxTxnDetails_CurrNo` | String |  |  |
| 16 | `ILMATX.TXN.INPUTTER` | `IlmatxTxnDetails_Inputter` |  |  |  |
| 17 | `ILMATX.TXN.DATE.TIME` | `IlmatxTxnDetails_DateTime` |  |  |  |
| 18 | `ILMATX.TXN.AUTHORISER` | `IlmatxTxnDetails_Authoriser` | String |  |  |
| 19 | `ILMATX.TXN.CO.CODE` | `IlmatxTxnDetails_CoCode` | String |  |  |
| 20 | `ILMATX.TXN.DEPT.CODE` | `IlmatxTxnDetails_DeptCode` | String |  |  |
| 21 | `ILMATX.TXN.AUDITOR.CODE` | `IlmatxTxnDetails_AuditorCode` | String |  |  |
| 22 | `ILMATX.TXN.AUDIT.DATE.TIME` | `IlmatxTxnDetails_AuditDateTime` | String |  |  |
| 23 | `ILMATX.TXN.REFUND.AMOUNT` | `IlmatxTxnDetails_RefundAmount` |  |  |  |
| 24 | `ILMATX.ACCT.ENTRY.REF.STATUS` | `IlmatxTxnDetails_AccountingEntryRefStatus` |  |  |  |
| 25 | `ILMATX.RESPONSE.DATE` | `IlmatxTxnDetails_ResponseDate` |  |  |  |
