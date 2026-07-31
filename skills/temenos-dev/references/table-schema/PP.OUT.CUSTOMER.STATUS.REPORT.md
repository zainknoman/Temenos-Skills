# PP.OUT.CUSTOMER.STATUS.REPORT — Table Schema

> Source: `INSERTS/I_F.PP.OUT.CUSTOMER.STATUS.REPORT` in `PP_CustomerPaymentStatusReport.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCSR.MessageReference` | `PpOutCustomerStatusReport_Messagereference` | TField |  |  |
| 2 | `PPCSR.CreatedDateTime` | `PpOutCustomerStatusReport_Createddatetime` | TField |  |  |
| 3 | `PPCSR.CompanyBIC` | `PpOutCustomerStatusReport_Companybic` | TField |  |  |
| 4 | `PPCSR.OriginatingReference` | `PpOutCustomerStatusReport_Originatingreference` | TField |  |  |
| 5 | `PPCSR.MessageFormat` | `PpOutCustomerStatusReport_Messageformat` | TField |  |  |
| 6 | `PPCSR.ReceivedDateTime` | `PpOutCustomerStatusReport_Receiveddatetime` | TField |  |  |
| 7 | `PPCSR.AcknowledgementType` | `PpOutCustomerStatusReport_Acknowledgementtype` | TField |  |  |
| 8 | `PPCSR.ResponseCodeLevel` | `PpOutCustomerStatusReport_Responsecodelevel` | TField |  |  |
| 9 | `PPCSR.BatchReference` | `PpOutCustomerStatusReport_Batchreference` | TField |  |  |
| 10 | `PPCSR.NumberOfChildren` | `PpOutCustomerStatusReport_Numberofchildren` | TField |  |  |
| 11 | `PPCSR.ReasonCode` | `PpOutCustomerStatusReport_Reasoncode` | TField |  |  |
| 12 | `PPCSR.ReasonCodeDesc` | `PpOutCustomerStatusReport_Reasoncodedesc` | TField |  |  |
| 13 | `PPCSR.BulkAmount` | `PpOutCustomerStatusReport_Bulkamount` | TField |  |  |
| 14 | `PPCSR.TransactionAmount` | `PpOutCustomerStatusReport_Transactionamount` |  |  |  |
| 15 | `PPCSR.TxnReferenceIncoming` | `PpOutCustomerStatusReport_Txnreferenceincoming` |  |  |  |
| 16 | `PPCSR.CustomerSpecifiedReference` | `PpOutCustomerStatusReport_Customerspecifiedreference` |  |  |  |
| 17 | `PPCSR.TransactionStatus` | `PpOutCustomerStatusReport_Transactionstatus` |  |  |  |
| 18 | `PPCSR.TxnReasonCode` | `PpOutCustomerStatusReport_Txnreasoncode` |  |  |  |
| 19 | `PPCSR.TxnReasonCodeDesc` | `PpOutCustomerStatusReport_Txnreasoncodedesc` |  |  |  |
| 20 | `PPCSR.CreditPartyFreeLines` | `PpOutCustomerStatusReport_Creditpartyfreelines` |  |  |  |
| 21 | `PPCSR.DebitPartyFreeLines` | `PpOutCustomerStatusReport_Debitpartyfreelines` |  |  |  |
| 22 | `PPCSR.TransformedTxn` | `PpOutCustomerStatusReport_Transformedtxn` | TField |  |  |
