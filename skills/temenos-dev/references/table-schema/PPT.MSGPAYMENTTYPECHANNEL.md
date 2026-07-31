# PPT.MSGPAYMENTTYPECHANNEL — Table Schema

> Source: `INSERTS/I_F.PPT.MSGPAYMENTTYPECHANNEL` in `PP_MessageMappingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPMPC.ChannelName` | `PptMsgpaymenttypechannel_Channelname` |  |  |  |
| 2 | `PPMPC.MessagePaymentType` | `PptMsgpaymenttypechannel_Messagepaymenttype` |  |  |  |
| 3 | `PPMPC.RACMessagePaymentTypeChannel` | `PptMsgpaymenttypechannel_Racmessagepaymenttypechannel` |  |  |  |
| 4 | `PPMPC.RSCMessagePaymentTypeChannel` | `PptMsgpaymenttypechannel_Rscmessagepaymenttypechannel` |  |  |  |
| 5 | `PPMPC.EntryUserID` | `PptMsgpaymenttypechannel_Entryuserid` |  |  |  |
| 6 | `PPMPC.EntryDateTime` | `PptMsgpaymenttypechannel_Entrydatetime` |  |  |  |
| 7 | `PPMPC.ApproverUserID` | `PptMsgpaymenttypechannel_Approveruserid` |  |  |  |
| 8 | `PPMPC.ApprovedDateTime` | `PptMsgpaymenttypechannel_Approveddatetime` |  |  |  |
