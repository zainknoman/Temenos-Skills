# PPL.INBOUNDCODEWORD — Table Schema

> Source: `INSERTS/I_F.PPL.INBOUNDCODEWORD` in `PP_InboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPIC.CompanyID` | `PplInboundcodeword_Companyid` |  |  |  |
| 2 | `PPIC.CodeWord` | `PplInboundcodeword_Codeword` |  |  |  |
| 3 | `PPIC.StartDateInboundCodeWord` | `PplInboundcodeword_Startdateinboundcodeword` |  |  |  |
| 4 | `PPIC.CodeWordRanking` | `PplInboundcodeword_Codewordranking` |  |  |  |
| 5 | `PPIC.CodeWordText` | `PplInboundcodeword_Codewordtext` |  |  |  |
| 6 | `PPIC.InformationCode` | `PplInboundcodeword_Informationcode` |  |  |  |
| 7 | `PPIC.MessagePaymentType` | `PplInboundcodeword_Messagepaymenttype` |  |  |  |
| 8 | `PPIC.OriginatingSource` | `PplInboundcodeword_Originatingsource` |  |  |  |
| 9 | `PPIC.CodeWordPriorityforPD` | `PplInboundcodeword_Codewordpriorityforpd` |  |  |  |
| 10 | `PPIC.AdjustedMessagePriority` | `PplInboundcodeword_Adjustedmessagepriority` |  |  |  |
| 11 | `PPIC.ProcessingSequenceNumber` | `PplInboundcodeword_Processingsequencenumber` |  |  |  |
| 12 | `PPIC.NonSTPIndicator` | `PplInboundcodeword_Nonstpindicator` |  |  |  |
| 13 | `PPIC.FeeCodewordFlag` | `PplInboundcodeword_Feecodewordflag` |  |  |  |
| 14 | `PPIC.OutboundCodewordApplicableFlag` | `PplInboundcodeword_Outboundcodewordapplicableflag` |  |  |  |
| 15 | `PPIC.EndDateInboundCodeWord` | `PplInboundcodeword_Enddateinboundcodeword` |  |  |  |
| 16 | `PPIC.RACInboundCodeWord` | `PplInboundcodeword_Racinboundcodeword` |  |  |  |
| 17 | `PPIC.RSCInboundCodeWord` | `PplInboundcodeword_Rscinboundcodeword` |  |  |  |
| 18 | `PPIC.EntryUserID` | `PplInboundcodeword_Entryuserid` |  |  |  |
| 19 | `PPIC.EntryDateTime` | `PplInboundcodeword_Entrydatetime` |  |  |  |
| 20 | `PPIC.ApproverUserID` | `PplInboundcodeword_Approveruserid` |  |  |  |
| 21 | `PPIC.ApprovedDateTime` | `PplInboundcodeword_Approveddatetime` |  |  |  |
