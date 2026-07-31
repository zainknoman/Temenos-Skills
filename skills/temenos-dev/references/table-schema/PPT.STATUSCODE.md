# PPT.STATUSCODE — Table Schema

> Source: `INSERTS/I_F.PPT.STATUSCODE` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSCD.StatusCode` | `PptStatuscode_Statuscode` |  |  |  |
| 2 | `PPSCD.StatusDescription` | `PptStatuscode_Statusdescription` |  |  |  |
| 3 | `PPSCD.RACStatusCode` | `PptStatuscode_Racstatuscode` |  |  |  |
| 4 | `PPSCD.RSCStatusCode` | `PptStatuscode_Rscstatuscode` |  |  |  |
| 5 | `PPSCD.EntryUserID` | `PptStatuscode_Entryuserid` |  |  |  |
| 6 | `PPSCD.EntryDateTime` | `PptStatuscode_Entrydatetime` |  |  |  |
| 7 | `PPSCD.ApproverUserID` | `PptStatuscode_Approveruserid` |  |  |  |
| 8 | `PPSCD.ApprovedDateTime` | `PptStatuscode_Approveddatetime` |  |  |  |
