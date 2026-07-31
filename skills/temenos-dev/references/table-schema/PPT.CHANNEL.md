# PPT.CHANNEL — Table Schema

> Source: `INSERTS/I_F.PPT.CHANNEL` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCHL.ChannelName` | `PptChannel_Channelname` |  |  |  |
| 2 | `PPCHL.ChannelDescription` | `PptChannel_Channeldescription` |  |  |  |
| 3 | `PPCHL.RACChannel` | `PptChannel_Racchannel` |  |  |  |
| 4 | `PPCHL.RSCChannel` | `PptChannel_Rscchannel` |  |  |  |
| 5 | `PPCHL.EntryUserID` | `PptChannel_Entryuserid` |  |  |  |
| 6 | `PPCHL.EntryDateTime` | `PptChannel_Entrydatetime` |  |  |  |
| 7 | `PPCHL.ApproverUserID` | `PptChannel_Approveruserid` |  |  |  |
| 8 | `PPCHL.ApprovedDateTime` | `PptChannel_Approveddatetime` |  |  |  |
