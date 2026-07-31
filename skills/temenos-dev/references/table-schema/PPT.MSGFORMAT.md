# PPT.MSGFORMAT — Table Schema

> Source: `INSERTS/I_F.PPT.MSGFORMAT` in `PP_MessageAcceptanceService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPMF.MessageFormat` | `PptMsgformat_Messageformat` |  |  |  |
| 2 | `PPMF.MessageFormatDescription` | `PptMsgformat_Messageformatdescription` |  |  |  |
| 3 | `PPMF.MessageForward` | `PptMsgformat_Messageforward` |  |  |  |
| 4 | `PPMF.RACMessageFormat` | `PptMsgformat_Racmessageformat` |  |  |  |
| 5 | `PPMF.RSCMessageFormat` | `PptMsgformat_Rscmessageformat` |  |  |  |
| 6 | `PPMF.EntryUserID` | `PptMsgformat_Entryuserid` |  |  |  |
| 7 | `PPMF.EntryDateTime` | `PptMsgformat_Entrydatetime` |  |  |  |
| 8 | `PPMF.ApproverUserID` | `PptMsgformat_Approveruserid` |  |  |  |
| 9 | `PPMF.ApprovedDateTime` | `PptMsgformat_Approveddatetime` |  |  |  |
