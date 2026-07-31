# PPL.OUTBOUNDCDWRDGEN — Table Schema

> Source: `INSERTS/I_F.PPL.OUTBOUNDCDWRDGEN` in `PP_OutboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPOCG.CompanyID` | `PplOutboundcdwrdgen_Companyid` |  |  |  |
| 2 | `PPOCG.ReceiverBankBIC` | `PplOutboundcdwrdgen_Receiverbankbic` |  |  |  |
| 3 | `PPOCG.StartDateOutboundCodeword` | `PplOutboundcdwrdgen_Startdateoutboundcodeword` |  |  |  |
| 4 | `PPOCG.OutboundMessagePaymentType` | `PplOutboundcdwrdgen_Outboundmessagepaymenttype` |  |  |  |
| 5 | `PPOCG.TransactionCurrency` | `PplOutboundcdwrdgen_Transactioncurrency` |  |  |  |
| 6 | `PPOCG.MessagePriority` | `PplOutboundcdwrdgen_Messagepriority` |  |  |  |
| 7 | `PPOCG.OutboundInformationCode` | `PplOutboundcdwrdgen_Outboundinformationcode` |  |  |  |
| 8 | `PPOCG.OutboundCodeword` | `PplOutboundcdwrdgen_Outboundcodeword` |  |  |  |
| 9 | `PPOCG.OutboundCodewordText` | `PplOutboundcdwrdgen_Outboundcodewordtext` |  |  |  |
| 10 | `PPOCG.ProcessingSequenceNumber` | `PplOutboundcdwrdgen_Processingsequencenumber` |  |  |  |
| 11 | `PPOCG.OutboundCodewordPriority` | `PplOutboundcdwrdgen_Outboundcodewordpriority` |  |  |  |
| 12 | `PPOCG.EndDateOutboundCodeword` | `PplOutboundcdwrdgen_Enddateoutboundcodeword` |  |  |  |
| 13 | `PPOCG.RACOutboundCodeword` | `PplOutboundcdwrdgen_Racoutboundcodeword` |  |  |  |
| 14 | `PPOCG.RSCOutboundCodeword` | `PplOutboundcdwrdgen_Rscoutboundcodeword` |  |  |  |
| 15 | `PPOCG.EntryUserID` | `PplOutboundcdwrdgen_Entryuserid` |  |  |  |
| 16 | `PPOCG.EntryDateTime` | `PplOutboundcdwrdgen_Entrydatetime` |  |  |  |
| 17 | `PPOCG.ApproverUserID` | `PplOutboundcdwrdgen_Approveruserid` |  |  |  |
| 18 | `PPOCG.ApprovedDateTime` | `PplOutboundcdwrdgen_Approveddatetime` |  |  |  |
