# PPL.INBOUNDOUTBOUNDCDWMP — Table Schema

> Source: `INSERTS/I_F.PPL.INBOUNDOUTBOUNDCDWMP` in `PP_OutboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPIOC.CompanyID` | `PplInboundoutboundcdwmp_Companyid` |  |  |  |
| 2 | `PPIOC.IncomingCodeword` | `PplInboundoutboundcdwmp_Incomingcodeword` |  |  |  |
| 3 | `PPIOC.CodewordRanking` | `PplInboundoutboundcdwmp_Codewordranking` |  |  |  |
| 4 | `PPIOC.StartDateInboundOutboundCdwMp` | `PplInboundoutboundcdwmp_Startdateinboundoutboundcdwmp` |  |  |  |
| 5 | `PPIOC.IncomingCodewordText` | `PplInboundoutboundcdwmp_Incomingcodewordtext` |  |  |  |
| 6 | `PPIOC.IncomingInformationCode` | `PplInboundoutboundcdwmp_Incominginformationcode` |  |  |  |
| 7 | `PPIOC.IncomingMessagePaymentType` | `PplInboundoutboundcdwmp_Incomingmessagepaymenttype` |  |  |  |
| 8 | `PPIOC.OriginatingSource` | `PplInboundoutboundcdwmp_Originatingsource` |  |  |  |
| 9 | `PPIOC.ReceiverBankBIC` | `PplInboundoutboundcdwmp_Receiverbankbic` |  |  |  |
| 10 | `PPIOC.OutboundMessagePaymentType` | `PplInboundoutboundcdwmp_Outboundmessagepaymenttype` |  |  |  |
| 11 | `PPIOC.TransactionCurrency` | `PplInboundoutboundcdwmp_Transactioncurrency` |  |  |  |
| 12 | `PPIOC.MessagePriority` | `PplInboundoutboundcdwmp_Messagepriority` |  |  |  |
| 13 | `PPIOC.OutboundInformationCode` | `PplInboundoutboundcdwmp_Outboundinformationcode` |  |  |  |
| 14 | `PPIOC.OutboundCodeword` | `PplInboundoutboundcdwmp_Outboundcodeword` |  |  |  |
| 15 | `PPIOC.OutboundCodewordText` | `PplInboundoutboundcdwmp_Outboundcodewordtext` |  |  |  |
| 16 | `PPIOC.ProcessingSequenceNumber` | `PplInboundoutboundcdwmp_Processingsequencenumber` |  |  |  |
| 17 | `PPIOC.OutboundCodewordPriority` | `PplInboundoutboundcdwmp_Outboundcodewordpriority` |  |  |  |
| 18 | `PPIOC.EndDateInboundOutboundCdwMp` | `PplInboundoutboundcdwmp_Enddateinboundoutboundcdwmp` |  |  |  |
| 19 | `PPIOC.RACInboundOutboundCdwMp` | `PplInboundoutboundcdwmp_Racinboundoutboundcdwmp` |  |  |  |
| 20 | `PPIOC.RSCInboundOutboundCdwMp` | `PplInboundoutboundcdwmp_Rscinboundoutboundcdwmp` |  |  |  |
| 21 | `PPIOC.EntryUserID` | `PplInboundoutboundcdwmp_Entryuserid` |  |  |  |
| 22 | `PPIOC.EntryDateTime` | `PplInboundoutboundcdwmp_Entrydatetime` |  |  |  |
| 23 | `PPIOC.ApproverUserID` | `PplInboundoutboundcdwmp_Approveruserid` |  |  |  |
| 24 | `PPIOC.ApprovedDateTime` | `PplInboundoutboundcdwmp_Approveddatetime` |  |  |  |
