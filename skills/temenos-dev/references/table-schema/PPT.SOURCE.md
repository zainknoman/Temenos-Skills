# PPT.SOURCE — Table Schema

> Source: `INSERTS/I_F.PPT.SOURCE` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSR.Source` | `PptSource_Source` |  |  |  |
| 2 | `PPSR.ChannelName` | `PptSource_Channelname` |  |  |  |
| 3 | `PPSR.SourceProduct` | `PptSource_Sourceproduct` |  |  |  |
| 4 | `PPSR.SourceDescription` | `PptSource_Sourcedescription` |  |  |  |
| 5 | `PPSR.RACSource` | `PptSource_Racsource` |  |  |  |
| 6 | `PPSR.RSCSource` | `PptSource_Rscsource` |  |  |  |
| 7 | `PPSR.EntryUserID` | `PptSource_Entryuserid` |  |  |  |
| 8 | `PPSR.EntryDateTime` | `PptSource_Entrydatetime` |  |  |  |
| 9 | `PPSR.ApproverUserID` | `PptSource_Approveruserid` |  |  |  |
| 10 | `PPSR.ApprovedDateTime` | `PptSource_Approveddatetime` |  |  |  |
| 11 | `PPSR.SourcePDGroup` | `PptSource_Sourcepdgroup` |  |  |  |
