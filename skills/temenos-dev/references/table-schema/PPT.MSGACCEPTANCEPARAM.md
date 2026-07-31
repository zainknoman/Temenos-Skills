# PPT.MSGACCEPTANCEPARAM — Table Schema

> Source: `INSERTS/I_F.PPT.MSGACCEPTANCEPARAM` in `PP_MessageAcceptanceService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPMAP.QueueName` | `PptMsgacceptanceparam_Queuename` |  |  |  |
| 2 | `PPMAP.IncomingMsgDirectory` | `PptMsgacceptanceparam_Incomingmsgdirectory` |  |  |  |
| 3 | `PPMAP.OriginatingChannel` | `PptMsgacceptanceparam_Originatingchannel` |  |  |  |
| 4 | `PPMAP.SingleMultipleIndicator` | `PptMsgacceptanceparam_Singlemultipleindicator` |  |  |  |
| 5 | `PPMAP.ValidateAPI` | `PptMsgacceptanceparam_Validateapi` |  |  |  |
| 6 | `PPMAP.CheckDuplicateIndicator` | `PptMsgacceptanceparam_Checkduplicateindicator` |  |  |  |
| 7 | `PPMAP.ACKRequiredIndicator` | `PptMsgacceptanceparam_Ackrequiredindicator` |  |  |  |
| 8 | `PPMAP.ACKAPI` | `PptMsgacceptanceparam_Ackapi` |  |  |  |
| 9 | `PPMAP.ACKNACKQueue` | `PptMsgacceptanceparam_Acknackqueue` |  |  |  |
| 10 | `PPMAP.MessageConversionFormat` | `PptMsgacceptanceparam_Messageconversionformat` |  |  |  |
| 11 | `PPMAP.RACMessageAcceptanceParameter` | `PptMsgacceptanceparam_Racmessageacceptanceparameter` |  |  |  |
| 12 | `PPMAP.RSCMessageAcceptanceParameter` | `PptMsgacceptanceparam_Rscmessageacceptanceparameter` |  |  |  |
| 13 | `PPMAP.EntryUserID` | `PptMsgacceptanceparam_Entryuserid` |  |  |  |
| 14 | `PPMAP.EntryDateTime` | `PptMsgacceptanceparam_Entrydatetime` |  |  |  |
| 15 | `PPMAP.ApproverUserID` | `PptMsgacceptanceparam_Approveruserid` |  |  |  |
| 16 | `PPMAP.ApprovedDateTime` | `PptMsgacceptanceparam_Approveddatetime` |  |  |  |
| 17 | `PPMAP.ReadMessageAPI` | `PptMsgacceptanceparam_Readmessageapi` |  |  |  |
| 18 | `PPMAP.InterpretAPI` | `PptMsgacceptanceparam_Interpretapi` |  |  |  |
| 19 | `PPMAP.MessageForwardAPI` | `PptMsgacceptanceparam_Messageforwardapi` |  |  |  |
| 20 | `PPMAP.MessageForwardQueue` | `PptMsgacceptanceparam_Messageforwardqueue` |  |  |  |
