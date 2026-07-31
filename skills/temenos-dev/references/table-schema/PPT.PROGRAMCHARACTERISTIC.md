# PPT.PROGRAMCHARACTERISTIC — Table Schema

> Source: `INSERTS/I_F.PPT.PROGRAMCHARACTERISTIC` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPGC.ProgramName` | `PptProgramcharacteristic_Programname` |  |  |  |
| 2 | `PPPGC.ProgramType` | `PptProgramcharacteristic_Programtype` |  |  |  |
| 3 | `PPPGC.ComponentName` | `PptProgramcharacteristic_Componentname` |  |  |  |
| 4 | `PPPGC.ComponentService` | `PptProgramcharacteristic_Componentservice` |  |  |  |
| 5 | `PPPGC.RACProgramCharacteristic` | `PptProgramcharacteristic_Racprogramcharacteristic` |  |  |  |
| 6 | `PPPGC.RSCProgramCharacteristic` | `PptProgramcharacteristic_Rscprogramcharacteristic` |  |  |  |
| 7 | `PPPGC.EntryUserID` | `PptProgramcharacteristic_Entryuserid` |  |  |  |
| 8 | `PPPGC.EntryDateTime` | `PptProgramcharacteristic_Entrydatetime` |  |  |  |
| 9 | `PPPGC.ApproverUserID` | `PptProgramcharacteristic_Approveruserid` |  |  |  |
| 10 | `PPPGC.ApprovedDateTime` | `PptProgramcharacteristic_Approveddatetime` |  |  |  |
