# PP.INBOUND.CODEWORD.PDS — Table Schema

> Source: `INSERTS/I_F.PP.INBOUND.CODEWORD.PDS` in `PP_InboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.IC.CompanyID` | `PpInboundCodewordPds_Companyid` |  |  |  |
| 2 | `PP.IC.CodeWord` | `PpInboundCodewordPds_Codeword` |  |  |  |
| 3 | `PP.IC.InformationCode` | `PpInboundCodewordPds_Informationcode` |  |  |  |
| 4 | `PP.IC.MessagePaymentType` | `PpInboundCodewordPds_Messagepaymenttype` |  |  |  |
| 5 | `PP.IC.OriginatingSource` | `PpInboundCodewordPds_Originatingsource` |  |  |  |
| 6 | `PP.IC.CodeWordRanking` | `PpInboundCodewordPds_Codewordranking` |  |  |  |
| 7 | `PP.IC.CodeWordText` | `PpInboundCodewordPds_Codewordtext` |  |  |  |
| 8 | `PP.IC.CodeWordPriorityforPD` | `PpInboundCodewordPds_Codewordpriorityforpd` |  |  |  |
| 9 | `PP.IC.AdjustedMessagePriority` | `PpInboundCodewordPds_Adjustedmessagepriority` |  |  |  |
| 10 | `PP.IC.ProcessingSequenceNumber` | `PpInboundCodewordPds_Processingsequencenumber` |  |  |  |
| 11 | `PP.IC.NonSTPIndicator` | `PpInboundCodewordPds_Nonstpindicator` |  |  |  |
| 12 | `PP.IC.FeeCodewordFlag` | `PpInboundCodewordPds_Feecodewordflag` |  |  |  |
| 13 | `PP.IC.OutboundCwApplicableFlag` | `PpInboundCodewordPds_Outboundcwapplicableflag` |  |  |  |
| 14 | `PP.IC.StartDate` | `PpInboundCodewordPds_Startdate` |  |  |  |
| 15 | `PP.IC.EndDate` | `PpInboundCodewordPds_Enddate` |  |  |  |
| 16 | `PP.IC.RESERVED.5` | `PpInboundCodewordPds_Reserved5` |  |  |  |
| 17 | `PP.IC.RESERVED.4` | `PpInboundCodewordPds_Reserved4` |  |  |  |
| 18 | `PP.IC.RESERVED.3` | `PpInboundCodewordPds_Reserved3` |  |  |  |
| 19 | `PP.IC.RESERVED.2` | `PpInboundCodewordPds_Reserved2` |  |  |  |
| 20 | `PP.IC.RESERVED.1` | `PpInboundCodewordPds_Reserved1` |  |  |  |
| 21 | `PP.IC.LOCAL.REF` | `PpInboundCodewordPds_LocalRef` |  |  |  |
| 22 | `PP.IC.LinkID` | `PpInboundCodewordPds_Linkid` |  |  |  |
| 23 | `PP.IC.OVERRIDE` | `PpInboundCodewordPds_Override` |  |  |  |
