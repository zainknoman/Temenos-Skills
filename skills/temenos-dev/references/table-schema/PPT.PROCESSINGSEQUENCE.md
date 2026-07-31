# PPT.PROCESSINGSEQUENCE — Table Schema

> Source: `INSERTS/I_F.PPT.PROCESSINGSEQUENCE` in `PP_InboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPSS.CompanyID` | `PptProcessingsequence_Companyid` |  |  |  |
| 2 | `PPPSS.ProcessingSequenceNumber` | `PptProcessingsequence_Processingsequencenumber` |  |  |  |
| 3 | `PPPSS.StartDateProcessingSequence` | `PptProcessingsequence_Startdateprocessingsequence` |  |  |  |
| 4 | `PPPSS.ProcessingSequenceDescription` | `PptProcessingsequence_Processingsequencedescription` |  |  |  |
| 5 | `PPPSS.ProcessingSequenceRoutineName` | `PptProcessingsequence_Processingsequenceroutinename` |  |  |  |
| 6 | `PPPSS.InboundProcessingSequenceFlag` | `PptProcessingsequence_Inboundprocessingsequenceflag` |  |  |  |
| 7 | `PPPSS.OutboundProcessingSequenceFlag` | `PptProcessingsequence_Outboundprocessingsequenceflag` |  |  |  |
| 8 | `PPPSS.EndDateProcessingSequence` | `PptProcessingsequence_Enddateprocessingsequence` |  |  |  |
| 9 | `PPPSS.RACProcessingSequence` | `PptProcessingsequence_Racprocessingsequence` |  |  |  |
| 10 | `PPPSS.RSCProcessingSequence` | `PptProcessingsequence_Rscprocessingsequence` |  |  |  |
| 11 | `PPPSS.EntryUserID` | `PptProcessingsequence_Entryuserid` |  |  |  |
| 12 | `PPPSS.EntryDateTime` | `PptProcessingsequence_Entrydatetime` |  |  |  |
| 13 | `PPPSS.ApproverUserID` | `PptProcessingsequence_Approveruserid` |  |  |  |
| 14 | `PPPSS.ApprovedDateTime` | `PptProcessingsequence_Approveddatetime` |  |  |  |
