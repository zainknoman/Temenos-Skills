# SEAT.HEAT.MAP — Table Schema

> Source: `INSERTS/I_F.SEAT.HEAT.MAP` in `SE_SeatHeatMap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.HM.TEST.APPLICATION` | `SeatHeatMap_TestApplication` |  |  |  |
| 2 | `SE.HM.TRANSACTION.TYPE` | `SeatHeatMap_TransactionType` |  |  |  |
| 3 | `SE.HM.WORKLOW.NAME` | `SeatHeatMap_WorklowName` |  |  |  |
| 4 | `SE.HM.RUN.DATES` | `SeatHeatMap_RunDates` |  |  |  |
| 5 | `SE.HM.TEST.FILE` | `SeatHeatMap_TestFile` |  |  |  |
| 6 | `SE.HM.TEST.COMPONENT` | `SeatHeatMap_TestComponent` |  |  |  |
| 7 | `SE.HM.TEST.STAGE` | `SeatHeatMap_TestStage` |  |  |  |
| 8 | `SE.HM.TEST.FIELDS` | `SeatHeatMap_TestFields` |  |  |  |
| 9 | `SE.HM.SCRIPT.ID` | `SeatHeatMap_ScriptId` |  |  |  |
| 10 | `SE.HM.RESERVED.10` | `SeatHeatMap_Reserved10` | TField |  |  |
| 11 | `SE.HM.RESERVED.9` | `SeatHeatMap_Reserved9` | TField |  |  |
| 12 | `SE.HM.RESERVED.8` | `SeatHeatMap_Reserved8` | TField |  |  |
| 13 | `SE.HM.RESERVED.7` | `SeatHeatMap_Reserved7` | TField |  |  |
| 14 | `SE.HM.RESERVED.6` | `SeatHeatMap_Reserved6` | TField |  |  |
| 15 | `SE.HM.RESERVED.5` | `SeatHeatMap_Reserved5` | TField |  |  |
| 16 | `SE.HM.RESERVED.4` | `SeatHeatMap_Reserved4` | TField |  |  |
| 17 | `SE.HM.RESERVED.3` | `SeatHeatMap_Reserved3` | TField |  |  |
| 18 | `SE.HM.RESERVED.2` | `SeatHeatMap_Reserved2` | TField |  |  |
| 19 | `SE.HM.RESERVED.1` | `SeatHeatMap_Reserved1` | TField |  |  |
