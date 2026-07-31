# PP.INBOUND.OUTBOUND.CDWMP.PDS — Table Schema

> Source: `INSERTS/I_F.PP.INBOUND.OUTBOUND.CDWMP.PDS` in `PP_OutboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ICM.CompanyID` | `PpInboundOutboundCdwmpPds_Companyid` |  |  |  |
| 2 | `PP.ICM.IncomingCodeword` | `PpInboundOutboundCdwmpPds_Incomingcodeword` |  |  |  |
| 3 | `PP.ICM.IncomingInformationCode` | `PpInboundOutboundCdwmpPds_Incominginformationcode` |  |  |  |
| 4 | `PP.ICM.OriginatingSource` | `PpInboundOutboundCdwmpPds_Originatingsource` |  |  |  |
| 5 | `PP.ICM.ReceiverBankBIC` | `PpInboundOutboundCdwmpPds_Receiverbankbic` |  |  |  |
| 6 | `PP.ICM.CodewordRanking` | `PpInboundOutboundCdwmpPds_Codewordranking` |  |  |  |
| 7 | `PP.ICM.IncomingCodewordText` | `PpInboundOutboundCdwmpPds_Incomingcodewordtext` |  |  |  |
| 8 | `PP.ICM.IncomingMessagePaymentType` | `PpInboundOutboundCdwmpPds_Incomingmessagepaymenttype` |  |  |  |
| 9 | `PP.ICM.OutboundMessagePaymentType` | `PpInboundOutboundCdwmpPds_Outboundmessagepaymenttype` |  |  |  |
| 10 | `PP.ICM.TransactionCurrency` | `PpInboundOutboundCdwmpPds_Transactioncurrency` |  |  |  |
| 11 | `PP.ICM.MessagePriority` | `PpInboundOutboundCdwmpPds_Messagepriority` |  |  |  |
| 12 | `PP.ICM.OutboundInformationCode` | `PpInboundOutboundCdwmpPds_Outboundinformationcode` |  |  |  |
| 13 | `PP.ICM.OutboundCodeword` | `PpInboundOutboundCdwmpPds_Outboundcodeword` |  |  |  |
| 14 | `PP.ICM.OutboundCodewordText` | `PpInboundOutboundCdwmpPds_Outboundcodewordtext` |  |  |  |
| 15 | `PP.ICM.ProcessingSequenceNumber` | `PpInboundOutboundCdwmpPds_Processingsequencenumber` |  |  |  |
| 16 | `PP.ICM.OutboundCodewordPriority` | `PpInboundOutboundCdwmpPds_Outboundcodewordpriority` |  |  |  |
| 17 | `PP.ICM.StartDate` | `PpInboundOutboundCdwmpPds_Startdate` |  |  |  |
| 18 | `PP.ICM.EndDate` | `PpInboundOutboundCdwmpPds_Enddate` |  |  |  |
| 19 | `PP.ICM.RESERVED.5` | `PpInboundOutboundCdwmpPds_Reserved5` |  |  |  |
| 20 | `PP.ICM.RESERVED.4` | `PpInboundOutboundCdwmpPds_Reserved4` |  |  |  |
| 21 | `PP.ICM.RESERVED.3` | `PpInboundOutboundCdwmpPds_Reserved3` |  |  |  |
| 22 | `PP.ICM.RESERVED.2` | `PpInboundOutboundCdwmpPds_Reserved2` |  |  |  |
| 23 | `PP.ICM.RESERVED.1` | `PpInboundOutboundCdwmpPds_Reserved1` |  |  |  |
| 24 | `PP.ICM.LOCAL.REF` | `PpInboundOutboundCdwmpPds_LocalRef` |  |  |  |
| 25 | `PP.ICM.LinkID` | `PpInboundOutboundCdwmpPds_Linkid` |  |  |  |
| 26 | `PP.ICM.OVERRIDE` | `PpInboundOutboundCdwmpPds_Override` |  |  |  |
