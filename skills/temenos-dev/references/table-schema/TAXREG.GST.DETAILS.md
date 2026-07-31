# TAXREG.GST.DETAILS — Table Schema

> Source: `INSERTS/I_F.TAXREG.GST.DETAILS` in `TAXGST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GST.DETAILS.BOOKING.DATE` | `TaxregGstDetails_BookingDate` | TField |  | Contains the run date on which the Entry was generated. This is the T24 date on which the entry was done. |
| 2 | `GST.DETAILS.VALUE.DATE` | `TaxregGstDetails_ValueDate` | TField |  | Contains the value date of the entry. |
| 3 | `GST.DETAILS.TRN.TYPE` | `TaxregGstDetails_TrnType` | TField |  | Identifies the type of transaction. The code is used to determine the type of transaction. This field will be useful for cases where tax is charged for a monthly |
| 4 | `GST.DETAILS.STOCK.EXCHANGE` | `TaxregGstDetails_StockExchange` | TField |  | Refers to the Stock Exchange of the underlying transaction that was taxed. |
| 5 | `GST.DETAILS.REVERSAL.MARKER` | `TaxregGstDetails_ReversalMarker` | TField |  | When a transaction is reversed then this field is marked as YES |
| 6 | `GST.DETAILS.CUSTOMER` | `TaxregGstDetails_Customer` |  |  |  |
| 7 | `GST.DETAILS.TXN.CCY` | `TaxregGstDetails_TxnCcy` |  |  |  |
| 8 | `GST.DETAILS.TXN.AMT` | `TaxregGstDetails_TxnAmt` |  |  |  |
| 9 | `GST.DETAILS.TXN.AMT.LCY` | `TaxregGstDetails_TxnAmtLcy` |  |  |  |
| 10 | `GST.DETAILS.GST.RATE` | `TaxregGstDetails_GstRate` |  |  |  |
| 11 | `GST.DETAILS.TAX.CODE` | `TaxregGstDetails_TaxCode` |  |  |  |
| 12 | `GST.DETAILS.TAX.TYPE` | `TaxregGstDetails_TaxType` |  |  |  |
| 13 | `GST.DETAILS.GST.TYPE` | `TaxregGstDetails_GstType` |  |  |  |
| 14 | `GST.DETAILS.PL.CATEGORY` | `TaxregGstDetails_PlCategory` |  |  |  |
| 15 | `GST.DETAILS.CHARGE.TYPE` | `TaxregGstDetails_ChargeType` |  |  |  |
| 16 | `GST.DETAILS.EXCH.RATE` | `TaxregGstDetails_ExchRate` |  |  |  |
| 17 | `GST.DETAILS.DR.ACCOUNT` | `TaxregGstDetails_DrAccount` |  |  |  |
| 18 | `GST.DETAILS.CR.ACCOUNT` | `TaxregGstDetails_CrAccount` |  |  |  |
| 19 | `GST.DETAILS.RECOV.AMT.GST.CCY` | `TaxregGstDetails_RecovAmtGstCcy` |  |  |  |
| 20 | `GST.DETAILS.IRRECOV.AMT.GST.CCY` | `TaxregGstDetails_IrrecovAmtGstCcy` |  |  |  |
| 21 | `GST.DETAILS.RECOV.AMT.LCY` | `TaxregGstDetails_RecovAmtLcy` |  |  |  |
| 22 | `GST.DETAILS.IRRECOV.AMT.LCY` | `TaxregGstDetails_IrrecovAmtLcy` |  |  |  |
| 23 | `GST.DETAILS.RECOV.AMT.FCY` | `TaxregGstDetails_RecovAmtFcy` |  |  |  |
| 24 | `GST.DETAILS.IRRECOV.AMT.FCY` | `TaxregGstDetails_IrrecovAmtFcy` |  |  |  |
| 25 | `GST.DETAILS.RECOV.ACCOUNT.NO` | `TaxregGstDetails_RecovAccountNo` |  |  |  |
| 26 | `GST.DETAILS.IRRECOV.ACCOUNT.NO` | `TaxregGstDetails_IrrecovAccountNo` |  |  |  |
| 27 | `GST.DETAILS.GST.AMT.LCY` | `TaxregGstDetails_GstAmtLcy` |  |  |  |
| 28 | `GST.DETAILS.GST.AMT.FCY` | `TaxregGstDetails_GstAmtFcy` |  |  |  |
| 29 | `GST.DETAILS.AMT.GST.CCY` | `TaxregGstDetails_AmtGstCcy` |  |  |  |
| 30 | `GST.DETAILS.GST.CCY` | `TaxregGstDetails_GstCcy` |  |  |  |
| 31 | `GST.DETAILS.COMM.AMT` | `TaxregGstDetails_CommAmt` |  |  |  |
| 32 | `GST.DETAILS.COMM.CCY` | `TaxregGstDetails_CommCcy` |  |  |  |
| 33 | `GST.DETAILS.COMM.DATE` | `TaxregGstDetails_CommDate` |  |  |  |
| 34 | `GST.DETAILS.INVOICE.NO` | `TaxregGstDetails_InvoiceNo` |  |  |  |
| 35 | `GST.DETAILS.SWEEP.DATE` | `TaxregGstDetails_SweepDate` |  |  |  |
| 36 | `GST.DETAILS.TRANSACTION.REF` | `TaxregGstDetails_TransactionRef` |  |  |  |
| 37 | `GST.DETAILS.COMMISSION.TYPE` | `TaxregGstDetails_CommissionType` |  |  |  |
| 38 | `GST.DETAILS.RESERVED.4` | `TaxregGstDetails_Reserved4` |  |  |  |
| 39 | `GST.DETAILS.RESERVED.5` | `TaxregGstDetails_Reserved5` |  |  |  |
| 40 | `GST.DETAILS.RESERVED.6` | `TaxregGstDetails_Reserved6` |  |  |  |
| 41 | `GST.DETAILS.CREDIT.NOTE.REF` | `TaxregGstDetails_CreditNoteRef` |  |  |  |
| 42 | `GST.DETAILS.REFUND.GST.TYPE` | `TaxregGstDetails_RefundGstType` |  |  |  |
| 43 | `GST.DETAILS.REFUND.TXN.REF` | `TaxregGstDetails_RefundTxnRef` |  |  |  |
| 44 | `GST.DETAILS.REFUND.COMM.CCY` | `TaxregGstDetails_RefundCommCcy` |  |  |  |
| 45 | `GST.DETAILS.REFUND.COMM.AMT` | `TaxregGstDetails_RefundCommAmt` |  |  |  |
| 46 | `GST.DETAILS.REFUND.GST.CCY` | `TaxregGstDetails_RefundGstCcy` |  |  |  |
| 47 | `GST.DETAILS.REFUND.GST.AMT` | `TaxregGstDetails_RefundGstAmt` |  |  |  |
| 48 | `GST.DETAILS.REFUND.CR.ACCT.NO` | `TaxregGstDetails_RefundCrAcctNo` |  |  |  |
| 49 | `GST.DETAILS.REFUND.NARRATIVE` | `TaxregGstDetails_RefundNarrative` |  |  |  |
| 50 | `GST.DETAILS.ORIG.INVOICE.REF` | `TaxregGstDetails_OrigInvoiceRef` |  |  |  |
| 51 | `GST.DETAILS.REFUND.TAX.ACCOUNT` | `TaxregGstDetails_RefundTaxAccount` |  |  |  |
| 52 | `GST.DETAILS.REFUND.SWEEP.DATE` | `TaxregGstDetails_RefundSweepDate` |  |  |  |
| 53 | `GST.DETAILS.REFUND.EXCH.RATE` | `TaxregGstDetails_RefundExchRate` |  |  |  |
| 54 | `GST.DETAILS.LOCAL.REF` | `TaxregGstDetails_LocalRef` |  |  |  |
| 55 | `GST.DETAILS.AA.REFERENCE` | `TaxregGstDetails_AaReference` | TField |  | Holds the Arrangement ID of the Activity. |
| 56 | `GST.DETAILS.RESERVED.11` | `TaxregGstDetails_Reserved11` | TField |  |  |
| 57 | `GST.DETAILS.RESERVED.12` | `TaxregGstDetails_Reserved12` | TField |  |  |
| 58 | `GST.DETAILS.RESERVED.13` | `TaxregGstDetails_Reserved13` | TField |  |  |
| 59 | `GST.DETAILS.RESERVED.14` | `TaxregGstDetails_Reserved14` | TField |  |  |
| 60 | `GST.DETAILS.RESERVED.15` | `TaxregGstDetails_Reserved15` | TField |  |  |
| 61 | `GST.DETAILS.RESERVED.16` | `TaxregGstDetails_Reserved16` | TField |  |  |
| 62 | `GST.DETAILS.RESERVED.17` | `TaxregGstDetails_Reserved17` | TField |  |  |
| 63 | `GST.DETAILS.RESERVED.18` | `TaxregGstDetails_Reserved18` | TField |  |  |
| 64 | `GST.DETAILS.RESERVED.19` | `TaxregGstDetails_Reserved19` | TField |  |  |
| 65 | `GST.DETAILS.LC.OPERATION.TYPE` | `TaxregGstDetails_LcOperationType` |  |  |  |
| 66 | `GST.DETAILS.DRAW.REFERENCE` | `TaxregGstDetails_DrawReference` |  |  |  |
| 67 | `GST.DETAILS.RITC.RATE` | `TaxregGstDetails_RitcRate` |  |  |  |
| 68 | `GST.DETAILS.RITC.BENEFIT` | `TaxregGstDetails_RitcBenefit` |  |  |  |
| 69 | `GST.DETAILS.PROCESSING.DATE` | `TaxregGstDetails_ProcessingDate` | TField |  | The processing date is the date on which the Entry updated the CRF. This can be same or different from Value date based on whether Trade Date, Value Dated or TDGL accounting method is used. |
| 70 | `GST.DETAILS.REFUND.REVERSAL.MARKER` | `TaxregGstDetails_RefundReversalMarker` |  |  |  |
| 71 | `GST.DETAILS.LEGAL.ENTITY.PF.ID` | `TaxregGstDetails_LegalEntityPfId` |  |  |  |
| 72 | `GST.DETAILS.CLAIM.STATUS` | `TaxregGstDetails_ClaimStatus` |  |  |  |
| 73 | `GST.DETAILS.STATUS.DATE` | `TaxregGstDetails_StatusDate` |  |  |  |
| 74 | `GST.DETAILS.REFUND.DATE` | `TaxregGstDetails_RefundDate` |  |  |  |
| 75 | `GST.DETAILS.REFUND.VALUE.DATE` | `TaxregGstDetails_RefundValueDate` |  |  |  |
| 76 | `GST.DETAILS.GSTIN` | `TaxregGstDetails_Gstin` | TField |  | GST number of customer, behalf of whom GST is collected |
| 77 | `GST.DETAILS.IRN` | `TaxregGstDetails_Irn` | TField |  | Interface Reference Number. This is the number received from Invoice Portal for Invoice sent to portal. |
| 78 | `GST.DETAILS.DRAW.TYPE` | `TaxregGstDetails_DrawType` |  |  |  |
