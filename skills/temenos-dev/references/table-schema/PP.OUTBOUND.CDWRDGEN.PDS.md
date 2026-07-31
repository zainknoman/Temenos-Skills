# PP.OUTBOUND.CDWRDGEN.PDS — Table Schema

> Source: `INSERTS/I_F.PP.OUTBOUND.CDWRDGEN.PDS` in `PP_OutboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.OCG.CompanyID` | `PpOutboundCdwrdgenPds_Companyid` |  |  |  |
| 2 | `PP.OCG.ReceiverBankBIC` | `PpOutboundCdwrdgenPds_Receiverbankbic` |  |  |  |
| 3 | `PP.OCG.OutboundMessagePaymentType` | `PpOutboundCdwrdgenPds_Outboundmessagepaymenttype` |  |  |  |
| 4 | `PP.OCG.TransactionCurrency` | `PpOutboundCdwrdgenPds_Transactioncurrency` |  |  |  |
| 5 | `PP.OCG.MessagePriority` | `PpOutboundCdwrdgenPds_Messagepriority` |  |  |  |
| 6 | `PP.OCG.OutboundInformationCode` | `PpOutboundCdwrdgenPds_Outboundinformationcode` |  |  |  |
| 7 | `PP.OCG.OutboundCodeword` | `PpOutboundCdwrdgenPds_Outboundcodeword` |  |  |  |
| 8 | `PP.OCG.OutboundCodewordText` | `PpOutboundCdwrdgenPds_Outboundcodewordtext` |  |  |  |
| 9 | `PP.OCG.ProcessingSequenceNumber` | `PpOutboundCdwrdgenPds_Processingsequencenumber` |  |  |  |
| 10 | `PP.OCG.OutboundCodewordPriority` | `PpOutboundCdwrdgenPds_Outboundcodewordpriority` |  |  |  |
| 11 | `PP.OCG.StartDate` | `PpOutboundCdwrdgenPds_Startdate` |  |  |  |
| 12 | `PP.OCG.EndDate` | `PpOutboundCdwrdgenPds_Enddate` |  |  |  |
| 13 | `PP.OCG.RESERVED.5` | `PpOutboundCdwrdgenPds_Reserved5` |  |  |  |
| 14 | `PP.OCG.RESERVED.4` | `PpOutboundCdwrdgenPds_Reserved4` |  |  |  |
| 15 | `PP.OCG.RESERVED.3` | `PpOutboundCdwrdgenPds_Reserved3` |  |  |  |
| 16 | `PP.OCG.RESERVED.2` | `PpOutboundCdwrdgenPds_Reserved2` |  |  |  |
| 17 | `PP.OCG.RESERVED.1` | `PpOutboundCdwrdgenPds_Reserved1` |  |  |  |
| 18 | `PP.OCG.LOCAL.REF` | `PpOutboundCdwrdgenPds_LocalRef` |  |  |  |
| 19 | `PP.OCG.LinkID` | `PpOutboundCdwrdgenPds_Linkid` |  |  |  |
| 20 | `PP.OCG.OVERRIDE` | `PpOutboundCdwrdgenPds_Override` |  |  |  |
