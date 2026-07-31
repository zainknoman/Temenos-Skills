# PPT.MSGPAYMENTTYPE — Table Schema

> Source: `INSERTS/I_F.PPT.MSGPAYMENTTYPE` in `PP_MessageMappingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPMPT.MessagePaymentType` | `PptMsgpaymenttype_Messagepaymenttype` |  |  |  |
| 2 | `PPMPT.MessagePaymentTypeDescription` | `PptMsgpaymenttype_Messagepaymenttypedescription` |  |  |  |
| 3 | `PPMPT.RACMessagePaymentType` | `PptMsgpaymenttype_Racmessagepaymenttype` |  |  |  |
| 4 | `PPMPT.RSCMessagePaymentType` | `PptMsgpaymenttype_Rscmessagepaymenttype` |  |  |  |
| 5 | `PPMPT.EntryUserID` | `PptMsgpaymenttype_Entryuserid` |  |  |  |
| 6 | `PPMPT.EntryDateTime` | `PptMsgpaymenttype_Entrydatetime` |  |  |  |
| 7 | `PPMPT.ApproverUserID` | `PptMsgpaymenttype_Approveruserid` |  |  |  |
| 8 | `PPMPT.ApprovedDateTime` | `PptMsgpaymenttype_Approveddatetime` |  |  |  |
| 9 | `PPMPT.OrderEntryFlag` | `PptMsgpaymenttype_Orderentryflag` |  |  |  |
