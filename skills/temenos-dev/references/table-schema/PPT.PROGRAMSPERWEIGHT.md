# PPT.PROGRAMSPERWEIGHT — Table Schema

> Source: `INSERTS/I_F.PPT.PROGRAMSPERWEIGHT` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPGW.CompanyID` | `PptProgramsperweight_Companyid` |  |  |  |
| 2 | `PPPGW.CallingComponent` | `PptProgramsperweight_Callingcomponent` |  |  |  |
| 3 | `PPPGW.WeightCode` | `PptProgramsperweight_Weightcode` |  |  |  |
| 4 | `PPPGW.SpecificWeightCode` | `PptProgramsperweight_Specificweightcode` |  |  |  |
| 5 | `PPPGW.Ranking` | `PptProgramsperweight_Ranking` |  |  |  |
| 6 | `PPPGW.StartDateProgramsPerWeight` | `PptProgramsperweight_Startdateprogramsperweight` |  |  |  |
| 7 | `PPPGW.ProgramName` | `PptProgramsperweight_Programname` |  |  |  |
| 8 | `PPPGW.ProgramsPerWeightDescription` | `PptProgramsperweight_Programsperweightdescription` |  |  |  |
| 9 | `PPPGW.ProgramSkipIndicator` | `PptProgramsperweight_Programskipindicator` |  |  |  |
| 10 | `PPPGW.EndDateProgramsPerWeight` | `PptProgramsperweight_Enddateprogramsperweight` |  |  |  |
| 11 | `PPPGW.RACProgramsPerWeight` | `PptProgramsperweight_Racprogramsperweight` |  |  |  |
| 12 | `PPPGW.RSCProgramsPerWeight` | `PptProgramsperweight_Rscprogramsperweight` |  |  |  |
| 13 | `PPPGW.EntryUserID` | `PptProgramsperweight_Entryuserid` |  |  |  |
| 14 | `PPPGW.EntryDateTime` | `PptProgramsperweight_Entrydatetime` |  |  |  |
| 15 | `PPPGW.ApproverUserID` | `PptProgramsperweight_Approveruserid` |  |  |  |
| 16 | `PPPGW.ApprovedDateTime` | `PptProgramsperweight_Approveddatetime` |  |  |  |
