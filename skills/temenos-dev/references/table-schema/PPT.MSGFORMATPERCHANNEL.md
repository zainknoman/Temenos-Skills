# PPT.MSGFORMATPERCHANNEL — Table Schema

> Source: `INSERTS/I_F.PPT.MSGFORMATPERCHANNEL` in `PP_MessageAcceptanceService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPMFC.ChannelName` | `PptMsgformatperchannel_Channelname` |  |  |  |
| 2 | `PPMFC.MessageFormat` | `PptMsgformatperchannel_Messageformat` |  |  |  |
| 3 | `PPMFC.MessageDirection` | `PptMsgformatperchannel_Messagedirection` |  |  |  |
| 4 | `PPMFC.MessageForward` | `PptMsgformatperchannel_Messageforward` |  |  |  |
| 5 | `PPMFC.RACMessageFormatPerChannel` | `PptMsgformatperchannel_Racmessageformatperchannel` |  |  |  |
| 6 | `PPMFC.RSCMessageFormatPerChannel` | `PptMsgformatperchannel_Rscmessageformatperchannel` |  |  |  |
| 7 | `PPMFC.EntryUserID` | `PptMsgformatperchannel_Entryuserid` |  |  |  |
| 8 | `PPMFC.EntryDateTime` | `PptMsgformatperchannel_Entrydatetime` |  |  |  |
| 9 | `PPMFC.ApproverUserID` | `PptMsgformatperchannel_Approveruserid` |  |  |  |
| 10 | `PPMFC.ApprovedDateTime` | `PptMsgformatperchannel_Approveddatetime` |  |  |  |
